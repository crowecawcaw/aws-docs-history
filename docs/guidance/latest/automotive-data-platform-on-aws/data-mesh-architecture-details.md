

# Architecture details
<a name="data-mesh-architecture-details"></a>

## DataZone V2 Domain
<a name="datazone-v2-domain"></a>

 **Domain**: `automotive-data-platform` 

See [Platform foundation](platform-foundation.md) for the full deploy topology and stack naming conventions.

 **Configuration**:
+ SSO: AWS IAM Identity Center (IDC)
+ VPC: Dedicated VPC with private subnets
+ Encryption: KMS customer-managed keys
+ Networking: VPC endpoints for AWS services

 **Projects**:
+ 9 producer projects — one per data product (`vehicle_telemetry_aggregated`, `customer_360`, `service_records`, and 6 others; see [Data products](data-products.md))
+ 1 smoke-test consumer project for subscription validation

 **Environments per project**:
+ Development: Sandbox for experimentation
+ Staging: Pre-production testing
+ Production: Live data products

## Data Product Registration
<a name="data-product-registration"></a>

The foundation deploy automatically registers all 9 governed data products in the DataZone V2 domain. See [Data products](data-products.md) for complete schemas, partition schemes, and subscription patterns for each product.

### Example: `customer_360` Data Product
<a name="example-customer_360-data-product"></a>

 **Registration** (auto-provisioned by `datazone-projects` stack):
+ Technical name: `customer_360` 
+ Owner: Customer domain producer project
+ Description: Unified customer profiles with snapshot-date partitioning
+ SLA: 99.9% availability, data freshness < 24 hours
+ Format: Apache Iceberg on S3
+ Access: Subscription request via DataZone V2 portal

 **Metadata**:
+ Business glossary: Customer, Health Score, NPS, Churn Risk
+ Technical documentation: Schema definitions, query examples
+ Quality metrics: Completeness, accuracy, timeliness
+ Usage examples: Sample queries, downstream notebook templates

### Example: `vehicle_telemetry_aggregated` Data Product
<a name="example-vehicle_telemetry_aggregated-data-product"></a>

 **Registration** (auto-provisioned by `datazone-projects` stack):
+ Technical name: `vehicle_telemetry_aggregated` 
+ Owner: Automotive domain producer project
+ Description: Hourly-aggregated vehicle telemetry, partitioned by `event_date` with 16-bucket VIN bucketing
+ Format: Apache Iceberg on S3
+ Access: Subscription request via DataZone V2 portal

 **Metadata**:
+ Business glossary: VIN, Sensor Reading, Diagnostic Code, Vehicle Health
+ Quality metrics: Completeness, accuracy, timeliness

## Cross-Domain Data Sharing
<a name="cross-domain-data-sharing"></a>

 **Scenario**: A consumer subscribes to both the `customer_360` and `service_records` data products to enrich customer profiles with service history

 **Process**:

1. Consumer discovers the `customer_360` and `service_records` data products in the DataZone V2 portal

1. Consumer submits subscription requests via the DataZone V2 portal

1. Producer domain owners approve requests (governance stack provisions Lake Formation grants automatically)

1. Lake Formation grants column-level read permissions per the data product’s access policy

1. Consumer queries both data products via Athena using the Glue Data Catalog

1. DataZone V2 tracks lineage showing data flow between producer and consumer projects

 **Query Example**:

```
SELECT
  c.customer_id,
  c.health_score,
  c.nps,
  s.service_month,
  s.repair_category
FROM customer_360.customer_360 c
JOIN service_records.service_records s
  ON c.customer_id = s.customer_id
WHERE c.health_score < 50
```

## Governance Policies
<a name="governance-policies"></a>

 **Data Classification**:
+ Public: Aggregated metrics, no customer identifiers
+ Internal: Customer profiles with hashed IDs
+ Confidential: PII data, financial information
+ Restricted: Biometric data, health information

 **Access Policies**:
+ Public: All authenticated users
+ Internal: Domain team members
+ Confidential: Authorized personnel with business justification
+ Restricted: Compliance approval required

 **Data Retention**:
+ Transactional data: 7 years
+ Analytical data: 3 years
+ Logs and audit trails: 10 years
+ Temporary data: 90 days

## Deployment Architecture
<a name="deployment-architecture"></a>

 **Infrastructure** (see [Platform foundation](platform-foundation.md) for complete topology):
+ Five per-stage CDK stacks: `network`, `lake`, `datazone`, `datazone-projects`, `governance` 
+ One account-singular bootstrap stack: `adp-shared-bootstrap` 
+ Resources: DataZone V2 domain, S3 Iceberg lake, Lake Formation tags, Macie session, CloudTrail trail, IAM Identity Center groups
+ Deployment time: 45–90 minutes via `make deploy STAGE=<stage>` 

 **Integration**:
+ All 9 data products registered automatically by the `datazone-projects` stack