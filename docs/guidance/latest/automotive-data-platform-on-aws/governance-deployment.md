# Plan your deployment

## GDPR Supportive Capabilities

### Right to Access (Article 15)

**Implementation**:

- User Portal with Cognito authentication for vehicle owners
- API Gateway endpoints for programmatic data access
- Lake Formation row-level security filtering by VIN ownership
- CloudTrail logging of all access requests

**Data Scope**: All personal data including telemetry, location history, service records, consent preferences

### Right to Erasure (Article 17)

**Implementation**:

- AWS Step Functions workflow orchestrates deletion across all data stores
- Lambda functions identify all PII records associated with customer VIN
- S3 object deletion with versioning for audit trail
- DynamoDB record deletion with point-in-time recovery backup
- Glue Data Catalog metadata cleanup

**Verification**:

- Athena queries verify deletion completeness
- S3 object versioning provides audit trail of deletions
- CloudTrail logs document deletion execution

###### Note

GDPR Recital 26 mentions that properly anonymized data (irreversibly de-identified) may not be classified as personal data and could fall outside GDPR’s scope, including erasure requirements. In contrast, pseudonymized data (where re-identification remains possible) is typically treated as personal data and subject to GDPR obligations, including deletion upon request.

### Right to Portability (Article 20)

**Implementation**:

- API Gateway endpoint for data export requests
- Lambda function aggregates data from all sources (S3, DynamoDB)
- Export formats: JSON (machine-readable), CSV (human-readable)
- Secure delivery: Pre-signed S3 URL with expiration, or direct API response

**Data Scope**: All customer data in structured, commonly used format

### Consent Management (Article 7)

**Implementation**:

- DynamoDB table stores consent records with granular permissions
- Custom Lambda functions validate consent before data access
- API Gateway authorizers check consent status
- Macie monitors for unauthorized PII exposure

**Consent Granularity**: Per data type (telemetry, location, diagnostics), per purpose (R&D, third-party sharing), per partner

### Data Minimization (Article 5)

**Implementation**:

- Store only necessary customer attributes (no excessive data collection)
- S3 Intelligent-Tiering automatically archives old data to lower-cost storage
- Lifecycle policies delete data after retention period expires
- Glue Data Quality validates data necessity before storage

## EU Data Act Supportive Capabilities

### Vehicle Owner Data Access (Article 4)

**Implementation**:

- Cognito user pool for vehicle owner authentication with MFA
- API Gateway endpoints for data access with rate limiting
- Lake Formation validates VIN ownership before granting access
- CloudTrail audits all access requests

**Data Format**: Machine-readable (JSON, CSV)

### Third-Party Data Sharing (Article 5)

**Implementation**:

- API Gateway with OAuth 2.0 for third-party authentication
- Lake Formation grants temporary access based on customer consent
- CloudTrail logs all third-party data access with partner identity
- Automated access revocation when consent withdrawn

**Partner Types**: Independent repair shops, insurance companies, fleet management services, aftermarket service providers

**Data Scope**: Only consented data types, filtered by VIN and date range

## Industry-Specific Compliance Support

### Automotive Standards

**TISAX (Trusted Information Security Assessment Exchange)**:

AWS has achieved TISAX Assessment Level 3 (AL3) - Information with Very High Protection Needs - across 19 regions, including EU regions (eu-west-1 Frankfurt, eu-central-1 Ireland). This is the highest TISAX assessment level, demonstrating AWS infrastructure meets the automotive industry’s most stringent information security requirements.

Automotive customers can verify AWS’s TISAX assessment results on the ENX portal (Scope ID: S58ZW2).

**Customer Responsibility**: AWS’s TISAX AL3 assessment covers AWS infrastructure and services. Customers building applications on AWS are responsible for their own TISAX assessments, which should evaluate their application architecture, configurations, and processes in addition to the underlying AWS infrastructure.

For current TISAX-certified regions, see the [AWS Compliance Programs page](https://aws.amazon.com/compliance/tisax/ "https://aws.amazon.com/compliance/tisax/").

### Regional Data Sovereignty

**EU Data Residency**:

- PII data stored exclusively in EU regions (eu-west-1, eu-central-1)
- Lake Formation policies prevent cross-border PII replication
- CloudFormation StackSets deploy consistent policies across EU regions
- Automated compliance checks before any data movement

**China Data Localization**:

- Separate AWS China regions (cn-north-1, cn-northwest-1) for Chinese vehicle data
- Independent Lake Formation governance for China region
- No data transfer between China and global regions
- Support for China Cybersecurity Law and Personal Information Protection Law (PIPL) requirements

**US State Privacy Laws (CCPA, CPRA)**:

- Similar technical capabilities to GDPR for California residents
- "Do Not Sell My Personal Information" consent management
- Consumer rights: Access, deletion, opt-out of sale
- Annual privacy disclosures and data inventory

## Deployment Considerations

### Multi-Account Strategy

**Recommended Account Structure**:

- Central Governance Account: Lake Formation, CloudTrail organization trail, Security Hub
- EU Producer Account: IoT Core, Kinesis, Glue ETL, S3 data stores
- Global Consumer Accounts: SageMaker, QuickSight, Athena (per region)
- Security Account: GuardDuty, Macie, Config aggregation

**Benefits**: Blast radius containment, cost allocation, compliance boundary enforcement

### Infrastructure as Code

**AWS CloudFormation**:

- StackSets for multi-region Lake Formation policy deployment
- Nested stacks for modular component deployment
- Change sets for safe production updates
- Drift detection for compliance validation

**AWS CDK (Cloud Development Kit)**:

- Python/TypeScript constructs for governance components
- Reusable patterns for Lake Formation permissions
- Automated testing with CDK assertions
- CI/CD integration for automated deployment

### Cost Optimization

**Data Storage**:

- S3 Intelligent-Tiering for automatic cost optimization
- Lifecycle policies transition old data to Glacier for long-term retention
- S3 Select reduces data transfer costs for queries
- Compression (Parquet, ORC) reduces storage costs by 70-80%

**Data Processing**:

- Glue ETL auto-scaling adjusts capacity based on workload
- Athena query result reuse reduces redundant processing
- Kinesis Data Streams on-demand pricing for variable workloads
- Reserved capacity for predictable workloads (Glue DPUs)

### Operational Excellence

**Monitoring and Alerting**:

- CloudWatch dashboards for governance metrics (access patterns, PII discoveries, policy violations)
- SNS notifications for critical events (unauthorized access attempts, Macie PII findings)
- EventBridge rules for automated remediation (move PII files, revoke permissions)
- Security Hub for centralized security findings

**Backup and Disaster Recovery**:

- S3 cross-region replication for anonymized data (RPO: 15 minutes)
- DynamoDB point-in-time recovery for consent database (RPO: 5 minutes)
- CloudFormation StackSets for infrastructure recovery (RTO: 2 hours)
- Regular disaster recovery testing (quarterly)

**Documentation and Training**:

- Data governance playbook for common scenarios
- Runbooks for incident response (data breach, unauthorized access)
- Training for data stewards on Lake Formation permissions
- Compliance documentation for auditors

## Next steps

- Review the architecture overview to understand the multi-region data flow
- Plan your multi-account structure for governance separation
- Configure AWS Lake Formation for centralized access control
- Implement PII detection and anonymization workflows
- Set up audit logging and compliance reporting
