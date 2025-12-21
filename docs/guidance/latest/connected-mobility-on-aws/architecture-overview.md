# Architecture overview

The Guidance for Connected Mobility on AWS implements a modern, event-driven architecture designed for automotive-scale data processing. Built on AWS managed services, the guidance demonstrates enterprise best practices for handling millions of vehicle telemetry messages per second while maintaining sub-second processing latency.

The architecture is organized into distinct layers that work together to provide end-to-end connected vehicle capabilities:

**Connectivity Layer** - Secure vehicle-to-cloud communication using AWS IoT Core with mutual TLS authentication and X.509 certificates. Supports MQTT protocol for efficient, bidirectional messaging at automotive scale.

**Ingestion Layer** - High-throughput message streaming using Amazon MSK (managed Apache Kafka) with SCRAM authentication. Provides durable, ordered message delivery with multi-AZ replication for reliability.

**Processing Layer** - Real-time stream processing using Apache Flink on Amazon Kinesis Data Analytics. Performs stateful computations including trip aggregation, safety event detection, and predictive maintenance analysis.

**Storage Layer** - Dual-purpose data storage with DynamoDB for operational queries (single-digit millisecond latency) and S3 for analytical workloads and long-term archival.

**Application Layer** - Fleet management dashboard built with React and CloudScape Design System, delivered globally via CloudFront with Cognito authentication.

The guidance uses a phase-based deployment approach, allowing organizations to start with basic fleet management capabilities (Phase 1-2) and progressively add real-time telemetry processing (Phase 3-6) as their connected vehicle program matures. This incremental approach reduces initial complexity, accelerates time-to-value, and allows teams to build operational expertise before scaling to full production workloads.

## Architecture diagram

The following diagram illustrates the complete Connected Mobility guidance architecture, showing all components and data flows from vehicle ingestion through processing to storage and user interface.

![Connected Mobility Complete Architecture](/images/guidance/latest/connected-mobility-on-aws/images/architecture_final.png)

**Key Data Flows**:

1. **Telemetry Ingestion**: Vehicles and simulator publish compressed telemetry to IoT Core using Basic Ingest (zero messaging cost)
2. **Message Routing**: IoT Rule decompresses payloads and routes to MSK via VPC destination using SCRAM authentication
3. **Stream Processing**: Five Flink applications consume from Kafka topics using IAM authentication and process telemetry in parallel
4. **Data Storage**: Processed data written to DynamoDB (structured), S3 (archive), and Redis (real-time cache)
5. **User Access**: Fleet managers access UI via CloudFront, which calls API Gateway and Lambda to retrieve data from storage layers
6. **Observability**: CloudWatch captures logs and metrics from all services; Aurora stores IoT lifecycle events

**Security Boundaries**:

- VPC isolation for MSK and Flink with private subnets
- SCRAM authentication for IoT Core to MSK
- IAM authentication for Flink to MSK
- Cognito user pools for UI authentication
- KMS encryption for data at rest

**Scalability Points**:

- MSK: Add brokers and partitions for higher throughput
- Flink: Increase parallelism (KPUs) for processing capacity
- DynamoDB: Auto-scaling for read/write capacity
- Redis: Cluster mode for distributed caching
- CloudFront: Global edge caching for UI performance
