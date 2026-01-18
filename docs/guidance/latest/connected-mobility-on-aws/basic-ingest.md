# Basic Ingest and IoT Rules Engine

The basic ingest layer uses AWS IoT Core Rules Engine to route vehicle telemetry directly to Amazon MSK without intermediate processing, minimizing latency and eliminating per-message costs through Basic Ingest.

**Cost Optimization with Basic Ingest**:

- **Zero Messaging Costs**: Basic Ingest eliminates the $1.00 per million messages charge for IoT Core messaging
- **Direct MSK Routing**: Messages bypass the IoT Core message broker and route directly to MSK, saving 40% on ingestion costs
- **No Lambda Required**: Direct integration eliminates Lambda invocation costs ($0.20 per million invocations)
- **Cost Comparison**:
  - Standard IoT Core: $1.00/million messages + $0.20/million Lambda invocations = $1.20/million
  - Basic Ingest: $0.00/million messages (only MSK storage and throughput costs)
  - Savings: 100% reduction in IoT Core messaging costs

**IoT Rules Engine Architecture**:

- **SQL-Based Routing**: Rules use SQL-like syntax to filter, transform, and route messages based on content
- **Direct MSK Integration**: The `cms_telemetry_to_msk` rule routes messages directly to MSK without Lambda or Kinesis intermediaries
- **Parallel Processing**: Rules engine processes messages in parallel, maintaining sub-second latency even at high throughput
- **Error Handling**: Failed messages are routed to error topics for retry or dead-letter queue processing

**Rule Configuration**:

```
 SELECT * FROM 'fleet/+/vehicle/+/telemetry'
```

This rule matches all telemetry messages from any fleet and vehicle, routing them to the MSK `raw-telemetry` topic. The wildcard pattern (+) enables dynamic fleet and vehicle registration without rule updates.

**SCRAM Authentication Implementation**:

AWS IoT Core uses SASL/SCRAM-SHA-512 authentication to securely connect to Amazon MSK. This implementation requires specific configuration in AWS Secrets Manager.

**Secrets Manager Secret Structure**:

The secret name MUST follow this exact pattern:

```
AmazonMSK_{cluster-name}_{username}
```

Example: `AmazonMSK_connected-mobility-cluster_iot-core-user`

**Secret Value Format**:

The secret value must be a JSON object with exactly these keys:

```
 {
  "username": "iot-core-user",
  "password": "your-secure-password-here"
}
```

**Critical Implementation Requirements**:

1. **Prefix Requirement**: The secret name MUST start with `AmazonMSK_` - this is a hard requirement for IoT Core to discover the secret
2. **Cluster Name Match**: The cluster name in the secret must exactly match the MSK cluster name
3. **Username Match**: The username in the secret value must match the username in the secret name
4. **JSON Format**: The secret value must be valid JSON with `username` and `password` keys (not key-value pairs)
5. **IAM Permissions**: IoT Core service role must have `secretsmanager:GetSecretValue` permission for the secret

**MSK SCRAM User Configuration**:

Before IoT Core can authenticate, the SCRAM user must be created in MSK:

```
 # Create SCRAM secret in Secrets Manager
aws secretsmanager create-secret \
  --name AmazonMSK_connected-mobility-cluster_iot-core-user \
  --secret-string '{"username":"iot-core-user","password":"SecurePassword123!"}'

# Associate secret with MSK cluster
aws kafka batch-associate-scram-secret \
  --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/connected-mobility-cluster/uuid \
  --secret-arn-list arn:aws:secretsmanager:us-east-1:123456789012:secret:AmazonMSK_connected-mobility-cluster_iot-core-user

# Create Kafka ACLs for the user
kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:iot-core-user \
  --operation Write --topic raw-telemetry

kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:iot-core-user \
  --operation Describe --topic raw-telemetry

kafka-acls --bootstrap-server $BOOTSTRAP_SERVERS \
  --command-config client.properties \
  --add --allow-principal User:iot-core-user \
  --operation DescribeConfigs --cluster
```

**IoT Rule Action Configuration**:

The IoT Rule action must specify the MSK cluster, topic, and authentication details:

```
 {
  "kafka": {
    "destinationArn": "arn:aws:kafka:us-east-1:123456789012:cluster/connected-mobility-cluster/uuid",
    "topic": "raw-telemetry",
    "key": "${vehicle_id}",
    "partition": "${partition}",
    "clientProperties": {
      "bootstrap.servers": "b-1.cluster.kafka.us-east-1.amazonaws.com:9096,b-2.cluster.kafka.us-east-1.amazonaws.com:9096,b-3.cluster.kafka.us-east-1.amazonaws.com:9096",
      "security.protocol": "SASL_SSL",
      "sasl.mechanism": "SCRAM-SHA-512",
      "sasl.scram.username": "${get_secret('AmazonMSK_connected-mobility-cluster_iot-core-user', 'SecretString', 'username')}",
      "sasl.scram.password": "${get_secret('AmazonMSK_connected-mobility-cluster_iot-core-user', 'SecretString', 'password')}"
    }
  }
}
```

**Key Implementation Details**:

- **Bootstrap Servers**: Must include all broker endpoints with port 9096 (SASL_SSL)
- **Security Protocol**: Must be `SASL_SSL` for SCRAM authentication with TLS encryption
- **SASL Mechanism**: Must be `SCRAM-SHA-512` (MSK supports SHA-256 and SHA-512)
- **Dynamic Secret Retrieval**: `get_secret()` function retrieves credentials from Secrets Manager at runtime
- **Message Key**: Uses `vehicle_id` to ensure messages from the same vehicle go to the same partition
- **Partition Strategy**: Optional partition field for explicit partition assignment

**VPC Connectivity Requirements**:

- **VPC Peering or PrivateLink**: IoT Core must have network connectivity to MSK cluster in private subnets
- **Security Groups**: MSK security group must allow inbound traffic on port 9096 from IoT Core service
- **DNS Resolution**: IoT Core must be able to resolve MSK broker DNS names
- **Network ACLs**: Subnet NACLs must allow bidirectional traffic on port 9096

**Automatic Credential Rotation**:

- **Secrets Manager Rotation**: Configure automatic rotation every 30-90 days
- **Zero-Downtime Rotation**: IoT Core automatically picks up new credentials without rule updates
- **Rotation Lambda**: Custom Lambda function updates both Secrets Manager and MSK SCRAM credentials
- **Monitoring**: CloudWatch alarms notify when rotation fails

**Scalability and Elasticity**:

- **Automatic Scaling**: Rules engine scales automatically based on message volume without configuration
- **No Provisioning**: Serverless architecture eliminates capacity planning and over-provisioning
- **Cost Efficiency**: Basic Ingest pricing (no per-message charge) reduces costs by 40% compared to standard IoT Core pricing
- **Throughput Limits**: Supports 1M+ messages/second per rule with automatic distribution across multiple rule instances

**Error Handling and Monitoring**:

- **Error Action**: Configure error action to republish failed messages to `$aws/rules/cms_telemetry_to_msk/error` topic
- **CloudWatch Metrics**:
  **`RuleMessageThrottled`: Messages throttled due to MSK capacity limits**
  `RuleNotFound`: Messages sent to non-existent topics
  **`ParseError`: Malformed messages that fail SQL parsing**
  `Success`: Successfully delivered messages
- **CloudWatch Logs**: Enable rule execution logs for debugging authentication and connectivity issues
- **Alarms**: Set alarms on error rates > 1% for proactive issue detection

**Event-Driven Benefits**:

- **Zero Polling**: Messages are pushed to MSK immediately upon receipt, eliminating polling overhead
- **Decoupled Architecture**: IoT Core and MSK operate independently; failures in one don’t affect the other
- **Multiple Destinations**: Single rule can route to multiple MSK topics, S3, DynamoDB, or Lambda simultaneously
- **Conditional Routing**: Use SQL WHERE clauses to route different message types to different topics

**Extensibility**:

The ingest layer can be extended for additional use cases:

- **Message Enrichment**: Add metadata (timestamp, region, account ID) using SQL functions
- **Data Filtering**: Filter out diagnostic messages or low-priority telemetry to reduce costs
- **Multi-Region Replication**: Route messages to MSK clusters in multiple regions for disaster recovery
- **Real-Time Alerting**: Add rules to detect critical conditions and trigger immediate Lambda notifications
- **Data Transformation**: Use SQL functions to transform message format before MSK ingestion
- **Topic Routing**: Route different message types (telemetry, diagnostics, commands) to separate MSK topics

**Troubleshooting Common Issues**:

1. **Authentication Failures**:
   - Verify secret name starts with `AmazonMSK_`
   - Confirm username in secret matches username in secret name
   - Check IAM permissions for `secretsmanager:GetSecretValue`
   - Verify SCRAM user is associated with MSK cluster

2. **Connectivity Issues**:
   - Verify VPC connectivity between IoT Core and MSK
   - Check security group rules allow port 9096
   - Confirm bootstrap servers are correct and reachable
   - Test DNS resolution of broker endpoints

3. **Authorization Failures**:
   - Verify Kafka ACLs grant Write permission to topic
   - Check ACLs grant Describe permission to topic
   - Confirm ACLs grant DescribeConfigs permission to cluster

4. **Performance Issues**:
   - Monitor MSK broker CPU and network utilization
   - Check for partition hot spots (uneven message distribution)
   - Verify message batching is enabled in rule configuration
   - Consider increasing MSK broker instance size
