# Architecture steps

The architecture follows a linear data flow optimized for automotive telemetry processing:

1. **Connected Vehicles** - Electric and connected vehicles communicate with AWS using MQTT over TLS, sending JSON-formatted telemetry data including GPS coordinates, speed, battery status, and diagnostic information. Each vehicle authenticates using unique X.509 certificates provisioned during vehicle onboarding.
2. **Device Authentication (AWS IoT Core)** - IoT Core authenticates each vehicle connection using X.509 certificates and validates device policies. Supports fleet provisioning for automated vehicle onboarding and certificate lifecycle management.
3. **Message Ingestion (AWS IoT Core)** - IoT Core receives vehicle telemetry on the `topic/telemetry` topic with QoS 1 (at least once delivery). The IoT Rules Engine routes messages to Amazon MSK using the `cms_telemetry_to_msk` rule with automatic retry and error handling.
4. **Message Streaming (Amazon MSK)** - MSK cluster ingests high-volume telemetry (1M+ messages/second) into the `raw-telemetry` topic. Uses SCRAM authentication with credentials stored in AWS Secrets Manager. Multi-AZ deployment ensures high availability with automatic failover.
5. **Stream Processing (Apache Flink)** - Flink applications consume from the raw telemetry topic and perform real-time processing using IAM authentication (AWS_MSK_IAM). Applications include:
   - Telemetry decoder for message validation and transformation
   - Trip aggregator for combining messages into complete trip records
   - Safety event detector for identifying harsh driving behaviors
   - Maintenance alert generator for predictive maintenance

6. **Processed Topics** - Flink routes processed data to specific Kafka topics (`trips`, `safety-events`, `maintenance-alerts`) based on data type and business logic. This topic-based routing enables downstream consumers to subscribe to specific data types.
7. **Data Storage (Amazon DynamoDB)** - Processed data is stored in optimized DynamoDB tables designed for high-throughput queries. Separate tables for trips, safety events, maintenance records, and raw telemetry enable efficient query patterns. DynamoDB Streams enable real-time change data capture for downstream processing.
8. **Archival Storage (Amazon S3)** - Historical data is archived to S3 for long-term retention and analytics. S3 lifecycle policies automatically transition data to lower-cost storage tiers. Data is partitioned by date and vehicle ID for efficient querying with Amazon Athena.
9. **Fleet Management Dashboard** - React-based web application provides real-time fleet monitoring, vehicle details, trip history, and safety event visualization. Hosted on S3 and delivered via CloudFront for global low-latency access.
10. **User Authentication (Amazon Cognito)** - Cognito User Pools manage fleet manager accounts with support for MFA and custom attributes. Cognito Identity Pools provide temporary AWS credentials for secure API access.
11. **Monitoring (Amazon CloudWatch)** - Comprehensive monitoring tracks message throughput, processing latency, error rates, and system health across all components. Custom metrics and alarms enable proactive issue detection and resolution.
