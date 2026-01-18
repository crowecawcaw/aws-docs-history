# Amazon MSK Streaming Layer

Amazon MSK provides the durable, ordered message streaming backbone for the telemetry pipeline. The MSK cluster acts as a buffer between ingestion and processing, enabling independent scaling and fault tolerance.

**Cluster Configuration**:

The MSK cluster is deployed with specific configuration optimized for IoT telemetry workloads:

- **Kafka Version**: 3.8.x (latest stable release with enhanced performance)
- **Instance Type**: kafka.m5.large (minimum required for VPC connectivity support)
- **Broker Count**: 2 brokers for development, 3+ for production
- **Storage**: 20 GB EBS per broker (dev), 100 GB (production) with auto-expansion
- **Multi-AZ**: Brokers distributed across 2 Availability Zones for high availability

**Auto-Create Topics Configuration**:

One of the critical implementation details is enabling automatic topic creation, which simplifies deployment and allows Flink applications to create topics dynamically:

```
 auto.create.topics.enable=true
default.replication.factor=2
num.partitions=3
```

This configuration:

- **Eliminates Manual Topic Creation**: Flink applications automatically create topics on first write
- **Default Replication**: All auto-created topics have replication factor of 2 for durability
- **Default Partitions**: 3 partitions per topic enable parallel processing
- **Operational Simplicity**: No pre-deployment topic provisioning required

**Dual Authentication Support**:

The cluster supports both SCRAM and IAM authentication simultaneously, enabling different access patterns:

**SCRAM Authentication (IoT Core)**:

- **Use Case**: AWS IoT Core Rules Engine connecting to MSK
- **Port**: 9096 (SASL_SSL)
- **Mechanism**: SASL/SCRAM-SHA-512
- **Secret Naming**: `AmazonMSK_{cluster-name}_iot_user_credentials`
- **Secret Format**: JSON with `username` and `password` keys
- **KMS Encryption**: Customer-managed KMS key for secret encryption
- **Secret Association**: SCRAM secret must be associated with cluster using `batch-associate-scram-secret`

**IAM Authentication (Flink Applications)**:

- **Use Case**: Apache Flink applications on Kinesis Data Analytics
- **Port**: 9098 (SASL_SSL with IAM)
- **Mechanism**: AWS_MSK_IAM
- **No Credentials**: Uses IAM role credentials automatically
- **Fine-Grained Access**: IAM policies control topic-level permissions
- **Audit Trail**: CloudTrail logs all IAM-authenticated access

**Encryption Configuration**:

The cluster implements defense-in-depth encryption:

**Encryption at Rest**:

- **Customer-Managed KMS Key**: Dedicated KMS key for MSK cluster data volumes
- **EBS Encryption**: All broker EBS volumes encrypted with KMS key
- **Key Policy**: Root account access + IoT Core role access (added by telemetry integration stack)
- **Key Rotation**: Automatic annual key rotation enabled

**Encryption in Transit**:

- **Client-Broker**: TLS 1.2+ required for all client connections
- **In-Cluster**: TLS encryption between brokers for replication traffic
- **Certificate Management**: AWS-managed certificates for broker TLS

**VPC Connectivity**:

The MSK cluster is deployed in a dedicated VPC with specific networking configuration:

**VPC Configuration**:

- **CIDR Block**: 10.0.0.0/16 (65,536 IP addresses)
- **Private Subnets**: /24 subnets (256 IPs each) for MSK brokers
- **Public Subnets**: /24 subnets for NAT gateways and bastion hosts
- **NAT Gateway**: Single NAT gateway for cost optimization (1 per AZ for production)
- **Multi-AZ**: Subnets span 2 Availability Zones

**Security Groups**:

- **Port 9092**: Kafka PLAINTEXT (disabled in production)
- **Port 9094**: Kafka TLS (mTLS disabled for simplicity)
- **Port 9096**: Kafka SASL_SCRAM (IoT Core access)
- **Port 9098**: Kafka SASL_IAM (Flink access)
- **Self-Referencing Rule**: Allows broker-to-broker communication on all Kafka ports
- **Source CIDR**: 10.0.0.0/8 (private IP ranges only)

**VPC Connectivity Property**:

The cluster explicitly disables VPC connectivity for SASL authentication to use standard broker endpoints:

```
 {
  "vpc_connectivity": {
    "client_authentication": {
      "sasl": {
        "iam": {"enabled": false},
        "scram": {"enabled": false}
      }
    }
  }
}
```

This configuration ensures IoT Core and Flink connect via standard bootstrap servers (port 9096/9098) rather than VPC connectivity endpoints.

**Topic Structure**:

- **raw-telemetry**: Receives all vehicle telemetry from IoT Core; partitioned by vehicle ID for ordered processing
- **trips**: Aggregated trip records produced by Flink trip processor
- **safety-events**: Harsh driving events produced by Flink safety detector
- **maintenance-alerts**: Predictive maintenance alerts produced by Flink maintenance processor
- **telemetry-processed**: Validated and enriched telemetry for downstream consumers

**Partitioning Strategy**:

- **Vehicle ID Partitioning**: Messages for the same vehicle always go to the same partition, ensuring ordered processing
- **Partition Count**: 3 default partitions per auto-created topic (configurable via MSK configuration)
- **Dynamic Scaling**: Add partitions without downtime as fleet size grows
- **Consumer Groups**: Multiple Flink applications consume from the same topic independently

**CloudWatch Logging**:

- **Broker Logs**: All broker logs streamed to CloudWatch Logs
- **Log Group**: `/aws/msk/{cluster-name}-{unique-suffix}`
- **Retention**: 7 days (configurable)
- **Log Types**: Application logs, access logs, and error logs

**Scalability and Elasticity**:

- **Horizontal Scaling**: Add brokers to increase throughput from 100 MB/s to 1+ GB/s per cluster
- **Vertical Scaling**: Upgrade broker instance types (kafka.m5.large to kafka.m5.4xlarge) for higher per-broker throughput
- **Storage Scaling**: Automatically expand EBS volumes as message retention grows
- **Throughput Limits**: Each kafka.m5.large broker supports ~40 MB/s ingress and 80 MB/s egress

**Performance Optimization**:

- **Compression**: Snappy compression reduces message size by 60-70%, increasing effective throughput
- **Batching**: Producers batch messages for 10ms or 16KB, reducing per-message overhead
- **Zero-Copy**: Kafka uses sendfile() system call to transfer data from disk to network without copying to application memory
- **Page Cache**: Linux page cache keeps hot data in memory, providing sub-millisecond read latency

**Event-Driven Architecture**:

- **Publish-Subscribe**: Multiple Flink applications consume from the same topics independently
- **Message Replay**: Consumers can reprocess historical messages by resetting offsets
- **Exactly-Once Semantics**: Kafka transactions ensure messages are processed exactly once across the pipeline
- **Change Data Capture**: DynamoDB Streams can publish changes back to Kafka for event sourcing patterns

**Monitoring and Observability**:

- **CloudWatch Metrics**: CPU utilization, network throughput, disk usage, message count
- **JMX Metrics**: Exposed via CloudWatch for detailed Kafka metrics
- **Broker Health**: Automatic health checks and replacement of unhealthy brokers
- **Alarms**: CPU > 80%, disk > 85%, under-replicated partitions > 0

**ACL Configuration**:

The cluster uses the default MSK configuration with `allow.everyone.if.no.acl.found=true`, which:

- **Simplifies Initial Setup**: No ACLs required for basic operation
- **Allows All Authenticated Users**: Any user with valid SCRAM or IAM credentials can access
- **Production Hardening**: Should be disabled in production with explicit ACLs:

```
 # Grant IoT user write access to raw-telemetry topic
kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:iot-user \
  --operation Write --topic raw-telemetry

# Grant Flink role read access to raw-telemetry
kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:arn:aws:iam::123456789012:role/flink-role \
  --operation Read --topic raw-telemetry \
  --group '*'

# Grant Flink role write access to processed topics
kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:arn:aws:iam::123456789012:role/flink-role \
  --operation Write --topic trips,safety-events,maintenance-alerts,telemetry-processed
```

**Deployment Considerations**:

- **SCRAM Secret Association**: After cluster creation, associate SCRAM secret manually:

```
 aws kafka batch-associate-scram-secret \
  --cluster-arn <cluster-arn> \
  --secret-arn-list <secret-arn>
```

- **Bootstrap Servers**: Retrieved from cluster ARN after deployment
- **Connection String**: Format is `b-1.cluster.kafka.region.amazonaws.com:9096,b-2.cluster.kafka.region.amazonaws.com:9096`
- **DNS Resolution**: Ensure clients can resolve broker DNS names

**Cost Optimization**:

- **Instance Sizing**: Start with kafka.m5.large, scale up based on actual throughput
- **Storage**: Use auto-scaling storage to avoid over-provisioning
- **Broker Count**: 2 brokers for dev/test, 3+ for production
- **Data Retention**: Configure topic retention based on business requirements (default 7 days)

**Extensibility**:

The streaming layer enables numerous extension use cases:

- **Additional Processors**: Add new Flink applications to consume raw telemetry for custom analytics
- **External Integrations**: Connect Kafka Connect to stream data to Elasticsearch, Snowflake, or data warehouses
- **Real-Time Dashboards**: Stream processed topics to WebSocket APIs for live dashboard updates
- **ML Feature Store**: Consume telemetry streams to build real-time feature pipelines for ML models
- **Audit Logging**: Mirror all topics to S3 for compliance and audit requirements
- **Multi-Region Replication**: Use MirrorMaker 2 to replicate topics across regions for disaster recovery
