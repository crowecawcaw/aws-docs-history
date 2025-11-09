# IoT Observability and Management

The System Monitoring provides comprehensive observability and operational management for the AWS IoT Core layer of the Connected Mobility guidance. Built as a serverless web application with React frontend and Python Lambda backend, the console delivers real-time visibility into device connectivity, MQTT topics, subscriptions, rules, and lifecycle events.

**Architecture**:

- **Frontend**: React application with CloudScape Design System hosted on S3 and distributed via CloudFront
- **Backend**: Python Lambda functions with FastAPI framework behind API Gateway
- **Data Storage**: Amazon Aurora PostgreSQL Serverless v2 for lifecycle events and metadata
- **Authentication**: Amazon Cognito (global regions) or OIDC-compatible IdP (China regions)
- **Telemetry Storage**: S3 with Apache Iceberg table format for vehicle data archival
- **Monitoring**: CloudWatch Logs and Metrics with optional OpenSearch integration for cost optimization

**Dashboard and Metrics**:

The dashboard provides real-time operational metrics and KPIs:

- **Connection Statistics**: Total connected devices, connection rate trends, geographic distribution
- **Message Throughput**: Messages per second, hourly/daily volumes, peak traffic analysis
- **Topic Activity**: Active topics, message counts per topic, subscription patterns
- **Rule Execution**: Rule success/failure rates, action execution metrics, error rates
- **System Health**: IoT Core service status, rule engine performance, data pipeline health
  Metrics are aggregated from CloudWatch and Aurora database queries, with 5-second refresh intervals for real-time monitoring.

**Connection Management**:

Track and manage all vehicle connections to IoT Core:

- **Active Connections**: Real-time list of connected vehicles with client IDs, IP addresses, connection timestamps
- **Connection History**: Historical connection records with connect/disconnect events, session durations
- **Connection Details**: Per-vehicle view showing session identifier, principal identifier (certificate ARN), protocol version
- **Disconnect Analysis**: Disconnect reasons (client-initiated, network timeout, authentication failure), disconnect timestamps
- **Geographic Distribution**: Connection origins by region and availability zone
  Connection data is captured via IoT Lifecycle Events and stored in Aurora PostgreSQL for fast querying and historical analysis.

**Subscription Tracking**:

Monitor MQTT topic subscriptions across the fleet:

- **Active Subscriptions**: Real-time list of client subscriptions with topic filters, QoS levels
- **Subscription History**: Historical subscribe/unsubscribe events with timestamps
- **Topic Patterns**: Analysis of subscription patterns (wildcard usage, topic hierarchies)
- **Subscription Conflicts**: Detection of overlapping or conflicting subscriptions
- **Per-Client Subscriptions**: Detailed view of all topics subscribed by each vehicle
  Subscription events are captured via IoT Rules Engine and stored in Aurora.

**Topic Management**:

Comprehensive MQTT topic monitoring and analysis:

- **Topic Inventory**: Complete list of active topics with message counts, last activity timestamps
- **Topic Hierarchy**: Visual representation of topic structure
- **Message Volume**: Messages per topic over time, peak usage identification
- **Retained Messages**: Management of MQTT retained messages with content preview and deletion
- **Topic Permissions**: IoT policy analysis showing which clients can publish/subscribe to topics
  Topic data is aggregated from CloudWatch Logs and IoT Core API queries.

**IoT Rules Engine Monitoring**:

Monitor and manage IoT Core rules for telemetry routing:

- **Rule List**: All configured rules with status (enabled/disabled), SQL statements, actions
- **Rule Execution Metrics**: Success/failure counts, execution duration, throttling events
- **Action Status**: Per-action metrics (Kafka, S3, CloudWatch Logs) with error rates
- **Rule Creation**: Web-based rule editor with SQL validation and action configuration
- **Rule Testing**: Test rules with sample payloads before deployment
- **Error Analysis**: Detailed error logs for failed rule executions with root cause identification
  Rule metrics are sourced from CloudWatch Metrics and CloudWatch Logs.

**Log Tracing and Debugging**:

Advanced log analysis for troubleshooting connectivity and message delivery issues:

- **Connection Logs**: Detailed logs of connection attempts, authentication results, TLS handshake details
- **Message Logs**: Per-message tracing with client ID, topic, payload size, delivery status
- **Error Logs**: Centralized error log aggregation from IoT Core, Rules Engine, and Lambda functions
- **Log Search**: Full-text search across all logs with filters (time range, client ID, topic, error type)
- **Log Export**: Export logs to S3 for long-term retention and compliance
  Logs are ingested from CloudWatch Logs with optional export to OpenSearch for advanced analytics.

**Alarm Management**:

Proactive alerting for operational issues:

- **Alarm Configuration**: Define alarms for connection failures, message delivery errors, rule execution failures
- **Alarm History**: Historical alarm events with timestamps, severity levels, affected resources
- **Alarm Notifications**: Integration with SNS for email/SMS notifications to operations teams
- **Alarm Dashboards**: Visual representation of alarm states (OK, ALARM, INSUFFICIENT_DATA)
- **Alarm Suppression**: Temporary suppression of alarms during maintenance windows
  Alarms are configured via CloudWatch Alarms and recorded in Aurora for historical analysis.

**User and Policy Management**:

Manage IoT Core authentication and authorization:

- **User Management**: Create and manage username/password credentials for IoT Core custom authorizer
- **Policy Management**: Create, edit, and assign IoT policies to devices and users
- **Policy Simulator**: Test policy permissions before deployment to prevent connectivity issues
- **Certificate Management**: View and manage X.509 certificates attached to devices
- **Authorization Logs**: Audit logs of authorization decisions (allow/deny) with policy evaluation details
  User credentials are stored in Aurora with bcrypt password hashing. Policies are managed via IoT Core API.

**Vehicle Data Storage (Apache Iceberg)**:

Long-term telemetry storage for analytics and compliance:

- **Iceberg Tables**: Vehicle telemetry stored in S3 as Apache Iceberg tables with schema evolution support
- **Data Ingestion**: IoT Rules Engine routes messages to Kinesis Data Firehose for streaming ingestion
- **Partitioning**: Date-based partitioning (year/month/day/hour) for efficient querying
- **Schema Management**: Automatic schema detection and evolution as telemetry fields change
- **Query Integration**: Compatible with Amazon Athena, AWS Glue, and Apache Spark for analytics
- **Data Lifecycle**: S3 lifecycle policies for transitioning old data to Glacier or deletion
  Iceberg table metadata is managed via AWS Glue Data Catalog with Lambda-based schema migration.

**Integration with Connected Mobility Guidance**:

The Observability Console integrates seamlessly with the Connected Mobility guidance:

- **IoT Core Layer**: Provides visibility into the ingestion layer before messages reach MSK
- **Troubleshooting**: Debug connectivity issues, certificate problems, and policy misconfigurations
- **Operational Metrics**: Monitor IoT Core performance and identify bottlenecks
- **Compliance**: Audit logs and connection history for regulatory compliance
- **Cost Optimization**: Identify unused topics, inefficient rules, and opportunities for Basic Ingest
  The console complements the Fleet Management Dashboard by focusing on IoT Core infrastructure rather than vehicle business logic.

**Deployment and Configuration**:

- **CDK Deployment**: Single-stack CDK deployment with all resources (Aurora, Lambda, CloudFront, Cognito)
- **Environment Variables**: Configurable via .env file (admin email, Aurora capacity, VPC settings)
- **Regional Support**: Global regions with Cognito, China regions with OIDC integration
- **Custom Domains**: Support for custom CloudFront domains with SSL certificates
- **VPC Integration**: Optional deployment into existing VPCs with private subnets for Aurora
  Deployment takes approximately 30 minutes and requires IoT Core logging to be enabled beforehand.

**Security and Access Control**:

- **Authentication**: Cognito user pools with email/password, MFA support, password policies
- **Authorization**: API Gateway Lambda authorizer validates JWT tokens from Cognito
- **Encryption**: TLS 1.2+ for all API calls, Aurora encryption at rest with KMS
- **Network Isolation**: Aurora in private/isolated subnets with no internet access
- **Audit Logging**: CloudTrail logs for all API Gateway and Lambda invocations
- **IAM Roles**: Least-privilege IAM roles for Lambda functions with resource-based policies

**Scalability and Performance**:

- **Serverless Architecture**: Auto-scaling Lambda functions and Aurora Serverless v2 (4-16 ACUs)
- **CloudFront Caching**: Static assets cached at edge locations for sub-100ms page loads
- **API Caching**: Optional API Gateway caching to reduce Lambda invocations
- **Database Connection Pooling**: SQLAlchemy connection pooling for efficient Aurora connections
- **Batch Processing**: SQS queues for lifecycle events with Lambda batch processing (up to 10 messages)
  The console supports fleets of 10,000+ vehicles with real-time updates and sub-second query response times.
