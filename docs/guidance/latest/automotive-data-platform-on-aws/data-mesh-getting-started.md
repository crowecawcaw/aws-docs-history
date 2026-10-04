

# Getting started
<a name="data-mesh-getting-started"></a>

## Foundation Deployment
<a name="foundation-deployment"></a>

Deploy the complete Automotive Data Platform foundation — DataZone V2 domain and all 10 core governed data products plus the 8 dealer- and parts-domain products — with a single command. See [Platform foundation](platform-foundation.md) for the full deploy runbook, stage-gate model, and stack naming conventions.

## Prerequisites
<a name="prerequisites"></a>
+ AWS account with CDK bootstrapped in `us-east-1` 
+ AWS IAM Identity Center (IDC) configured in the account
+ Python 3.12\+ and Node.js 22.x LTS for CDK
+ Docker (for Lambda bundling)

## Deploy the Foundation
<a name="deploy-the-foundation"></a>

```
# Bootstrap account-level resources (once per account)
make bootstrap

# Deploy all seven per-stage stacks in dependency order
make deploy STAGE=staging
```

 **Deployment time**: 45–90 minutes

 **What gets deployed**:
+  `adp-staging-foundation-network`: VPC with private subnets and VPC endpoints
+  `adp-staging-foundation-lake`: S3 Iceberg lake \+ KMS \+ 11 Glue databases (10 core products \+ 1 dimensions)
+  `adp-staging-foundation-datazone`: DataZone V2 domain \+ IAM roles
+  `adp-staging-foundation-datazone-projects`: 9 core-producer projects \+ 1 smoke-test consumer project
+  `adp-staging-foundation-governance`: Lake Formation tags \+ CloudTrail trail \+ 3 IDC groups; IaC cross-account LF grants to CMS/DMS consumer roles when supplied by context
+  `adp-staging-foundation-dealer-domain`: `adp_staging_dealer_domain` Glue database \+ 1 DataZone project \+ Glue/PySpark generator role for 5 dealer-ops products
+  `adp-staging-foundation-parts-domain`: `adp_staging_parts_domain` Glue database \+ 1 DataZone project \+ generator role for 3 ACES/PIES parts products

## Subscribe to Data Products
<a name="subscribe-to-data-products"></a>

After deployment, consumers discover and subscribe to data products through the DataZone V2 portal:

1. Open the DataZone V2 data portal URL (output by the `datazone` stack)

1. Log in with IAM Identity Center credentials

1. Browse the catalog — all 10 core data products plus the 8 dealer- and parts-domain products are discoverable

1. Submit subscription requests; producer domain owners approve via the DataZone V2 workflow

1. Lake Formation grants column-level read permissions automatically upon approval

## Query Subscribed Data
<a name="query-subscribed-data"></a>

```
-- Query combining customer_360 and service_records data products
-- (after subscription approval)
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