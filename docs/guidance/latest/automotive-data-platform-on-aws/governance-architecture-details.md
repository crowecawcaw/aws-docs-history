

# Architecture details
<a name="governance-architecture-details"></a>

The Governance Framework implements detailed technical components for multi-region data governance with centralized control and distributed processing.

## AWS Lake Formation Configuration
<a name="aws-lake-formation-configuration"></a>

 **Central Governance Setup**:
+ Data Lake Administrator: Centralized governance team role
+ Cross-region resource shares: Enable anonymized data access in consumer regions
+ Permission model: Tag-based access control (TBAC) for scalable policy management
+ Audit integration: All permission grants/revocations logged to CloudTrail

 **Resource Shares**:
+ Share anonymized data catalog to global consumer regions through resource links
+ PII data catalog remains in EU region only, never shared
+ Enforce encryption in transit for all cross-region access
+ Resource link permissions inherited from producer region

 **Permission Policies**:
+ Vehicle Owner: Read own PII data only (row-level security filtering by VIN)
+ R&D Team: Read all anonymized data, explicit deny on PII tables
+ Compliance Team: Read all data with mandatory audit trail
+ Data Engineer: Full access for data pipeline management with MFA requirement

## AWS CloudTrail Organization Trail
<a name="aws-cloudtrail-organization-trail"></a>

 **Trail Configuration**:
+ Organization trail: Logs all accounts and regions
+ S3 bucket: Centralized audit log storage with cross-region replication
+ Encryption: SSE-KMS with customer-managed key
+ Log file validation: Enabled for tamper detection
+ S3 Object Lock: Compliance mode with customer-defined retention supporting regulatory requirements

 **Events Logged**:
+ All Lake Formation permission grants, revocations, and access attempts
+ All S3 data access (read, write, delete) with requester identity
+ All Athena queries with user identity and query text
+ All Glue job executions with input/output data locations
+ All API Gateway requests with source IP and authentication details

 **Integration**:
+ CloudWatch Logs: Real-time monitoring with metric filters for suspicious activity
+ Amazon Athena: Query analysis for compliance reporting
+ AWS Security Hub: Security findings aggregation
+ Amazon QuickSight: Compliance dashboards showing access patterns

## Amazon Macie Configuration
<a name="amazon-macie-configuration"></a>

 **Automated Discovery**:
+ Scan frequency: Daily automated scans of all S3 buckets
+ Scope: All buckets in EU producer region containing vehicle data
+ Sensitive data types: Email, phone, SSN, credit card, GPS coordinates
+ Custom identifiers: VIN patterns (17-character alphanumeric), license plate formats, driver ID patterns

 **PII Detection**:
+ High confidence: Automatic classification as PII with immediate alerting
+ Medium confidence: Manual review queue for data stewards
+ Low confidence: Logged for investigation and pattern refinement

 **Remediation Workflows**:
+ Automated: Lambda function moves PII files to restricted bucket with stricter access controls
+ Manual: Data steward review and reclassification through console
+ Alerting: SNS notification to security team for new PII discoveries with severity classification

 **Findings Integration**:
+ AWS Security Hub: Centralized security findings
+ Amazon EventBridge: Trigger automated remediation workflows
+ CloudWatch Metrics: Track PII discovery trends over time

## Security Architecture
<a name="security-architecture"></a>

 **Encryption**:
+ At Rest: AWS KMS with customer-managed keys per region, separate keys for PII and anonymized data stores
+ In Transit: TLS 1.3 for all data transfers between regions and to external parties

 **Network Isolation**:
+ VPC endpoints for AWS services
+ PrivateLink for cross-region connectivity
+ No public internet exposure for data processing

 **Identity and Access**:
+ Identity Federation: Amazon Cognito with MFA for vehicle owner access, IAM Identity Center (SSO) for internal users
+ Service-to-Service: IAM roles with least privilege for automated access between AWS services
+ Data Masking: Lake Formation column-level security automatically redacts PII for non-authorized users

 **Audit Immutability**:
+ S3 Object Lock in compliance mode ensures CloudTrail logs cannot be tampered with or deleted during retention periods

## High-Level Architecture
<a name="high-level-architecture"></a>

The architecture consists of:

1.  **Central Governance Hub**: AWS Lake Formation enforces global access policies, AWS Glue Data Catalog maintains centralized metadata, CloudTrail provides audit logging

1.  **EU Producer Region**: Vehicle data collection, PII classification, anonymization processing, and dual data stores (PII \+ anonymized)

1.  **Global Consumer Regions**: R&D analytics access to anonymized data only through Lake Formation resource links

1.  **Governance Layer**: Cross-region policies enforced through Lake Formation resource shares and IAM roles

1.  **Audit Layer**: Centralized CloudTrail logging with S3 Object Lock for tamper-proof audit trails

## Multi-Region Data Flow
<a name="multi-region-data-flow"></a>

The solution manages data flow across three patterns:

### Pattern 1: EU Vehicle Data Collection and Classification
<a name="pattern-1-eu-vehicle-data-collection-and-classification"></a>

 **Data Generation**: Connected vehicles in EU generate telemetry and diagnostic data transmitted via AWS IoT Core using MQTT over TLS with X.509 certificate authentication.

 **Data Ingestion**: AWS IoT Core receives vehicle telemetry and routes to Amazon Kinesis Data Streams. Amazon Data Firehose delivers data to Amazon S3 raw storage in EU region.

 **Data Classification**: AWS Glue Data Quality validates incoming data against automotive-specific rules. AWS Glue ETL Streaming performs real-time anonymization, separating telemetry into two data stores.

 **PII Data Store**: Contains precise GPS coordinates, driver information, detailed vehicle identifiers (VIN, license plate), protected by Lake Formation policies and S3 Object Lock. Data remains in EU region with replication disabled.

 **Anonymized Data Store**: Contains hashed identifiers (SHA-256 of VIN), city-level locations (no precise coordinates), aggregated sensor metrics (5-minute averages), anonymized driver patterns. Enabled for cross-region replication to global consumer regions.

 **Consent Check**: Custom workflows validate customer consent before any data sharing with third parties.

### Pattern 2: Cross-Region Analytics Access
<a name="pattern-2-cross-region-analytics-access"></a>

 **Resource Link Creation**: Lake Formation creates resource links in consumer regions that point to anonymized data tables in the producer region.

 **Permission Enforcement**: When R&D teams in consumer regions query data through resource links, Lake Formation enforces permissions defined in the producer region, ensuring PII tables are never accessible.

 **Data Access**: Amazon SageMaker notebooks and Amazon QuickSight dashboards in consumer regions query anonymized data through Athena, with all access logged in CloudTrail.

 **Audit Trail**: CloudTrail logs capture all cross-region access attempts with user identity, timestamp, and data accessed.

### Pattern 3: Vehicle Owner Data Access (EU Data Act Support)
<a name="pattern-3-vehicle-owner-data-access-eu-data-act-support"></a>

 **Customer Request**: Vehicle owner requests their data through User Portal (React SPA hosted on S3 \+ CloudFront).

 **Authentication**: Amazon Cognito User Pool authenticates user with MFA requirement.

 **Authorization**: API Gateway Lambda authorizer verifies VIN ownership before granting access.

 **Data Retrieval**: Lake Formation validates permissions, allowing access only to owner’s own PII data.

 **Format Conversion**: Data provided in machine-readable formats (JSON, CSV) supporting GDPR Article 20 and EU Data Act Article 4 requirements.

 **Secure Delivery**: Encrypted transfer via API Gateway with all operations logged in CloudTrail.

 **Third-Party Sharing**: If customer grants consent, API Gateway endpoints enable controlled data sharing with external parties (repair shops, insurance companies) with temporary Lake Formation permissions and complete audit logging.