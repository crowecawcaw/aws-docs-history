# Getting started

## Foundation Deployment

Deploy the complete Automotive Data Platform foundation — DataZone V2 domain and all 9 governed data products — with a single command. See [Platform foundation](platform-foundation.md "platform-foundation.md") for the full deploy runbook, stage-gate model, and stack naming conventions.

## Prerequisites

- AWS account with CDK bootstrapped in `us-east-1`
- AWS IAM Identity Center (IDC) configured in the account
- Python 3.12+ and Node.js 22.x LTS for CDK
- Docker (for Lambda bundling)

## Deploy the Foundation

```
# Bootstrap account-level resources (once per account)
make bootstrap

# Deploy all five per-stage stacks in dependency order
make deploy STAGE=staging
```

**Deployment time**: 45–90 minutes

**What gets deployed**:

- `adp-staging-foundation-network`: VPC with private subnets and VPC endpoints
- `adp-staging-foundation-lake`: S3 Iceberg lake + KMS + 10 Glue databases
- `adp-staging-foundation-datazone`: DataZone V2 domain + IAM roles
- `adp-staging-foundation-datazone-projects`: 9 producer projects + 1 smoke-test consumer project (all 9 data products registered)
- `adp-staging-foundation-governance`: Lake Formation tags + CloudTrail trail + 3 IDC groups

## Subscribe to Data Products

After deployment, consumers discover and subscribe to data products through the DataZone V2 portal:

1. Open the DataZone V2 data portal URL (output by the `datazone` stack)
2. Log in with IAM Identity Center credentials
3. Browse the catalog — all 9 data products are discoverable
4. Submit subscription requests; producer domain owners approve via the DataZone V2 workflow
5. Lake Formation grants column-level read permissions automatically upon approval

## Query Subscribed Data

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
