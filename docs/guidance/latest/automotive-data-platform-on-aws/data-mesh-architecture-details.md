# Architecture details

## SageMaker Unified Studio

**Domain**: `automotive-data-platform`

**Configuration**:

- SSO: AWS IAM Identity Center
- VPC: Dedicated VPC with private subnets
- Encryption: KMS customer-managed keys
- Networking: VPC endpoints for AWS services

**Projects**:

- Customer Analytics: Customer 360 data product
- Vehicle Intelligence: Predictive Maintenance data product
- Compliance: Governance and audit data product

**Environments**:

- Development: Sandbox for experimentation
- Staging: Pre-production testing
- Production: Live data products

## Data Product Registration

### Customer 360 Data Product

**Registration**:

- Name: `customer-360-analytics`
- Owner: Customer Experience team
- Description: Unified customer profiles with health scores and sentiment
- SLA: 99.9% availability, data freshness < 24 hours
- Schema: Glue Data Catalog tables
- Access: Request via DataZone portal

**Metadata**:

- Business glossary: Customer, Health Score, NPS, Churn Risk
- Technical documentation: Schema definitions, query examples
- Quality metrics: Completeness, accuracy, timeliness
- Usage examples: Sample queries, dashboard templates

### Predictive Maintenance Data Product

**Registration**:

- Name: `predictive-maintenance`
- Owner: Vehicle Operations team
- Description: ML predictions for tire failures and component issues
- SLA: 99.5% availability, prediction latency < 1 second
- Schema: API specification, DynamoDB tables
- Access: API key via DataZone portal

**Metadata**:

- Business glossary: Tire Failure, Anomaly Score, Risk Level
- Technical documentation: API reference, model documentation
- Quality metrics: Prediction accuracy, false positive rate
- Usage examples: API calls, integration patterns

## Cross-Domain Data Sharing

**Scenario**: Customer Analytics team wants to enrich customer profiles with predictive maintenance data

**Process**:

1. Customer Analytics team discovers Predictive Maintenance data product in DataZone
2. Request access via DataZone portal
3. Vehicle Operations team approves request (automated for anonymized data)
4. Lake Formation grants read permissions
5. Customer Analytics team queries both data products via Athena
6. DataZone tracks lineage showing data flow between domains

**Query Example**:

```
SELECT
  c.customer_id,
  c.health_score,
  c.nps,
  p.risk_level,
  p.days_to_failure
FROM customer_360.customers c
JOIN predictive_maintenance.predictions p
  ON c.vin = p.vin
WHERE c.health_score < 50
  AND p.risk_level = 'high'
```

## Governance Policies

**Data Classification**:

- Public: Aggregated metrics, no customer identifiers
- Internal: Customer profiles with hashed IDs
- Confidential: PII data, financial information
- Restricted: Biometric data, health information

**Access Policies**:

- Public: All authenticated users
- Internal: Domain team members
- Confidential: Authorized personnel with business justification
- Restricted: Compliance approval required

**Data Retention**:

- Transactional data: 7 years
- Analytical data: 3 years
- Logs and audit trails: 10 years
- Temporary data: 90 days

## Deployment Architecture

**Infrastructure**:

- CloudFormation stack: `automotive-platform-foundation`
- Resources: SageMaker Unified Studio domain, DataZone, Lake Formation
- Deployment time: 1-2 hours

**Integration**:

- Customer 360 registers as data product
