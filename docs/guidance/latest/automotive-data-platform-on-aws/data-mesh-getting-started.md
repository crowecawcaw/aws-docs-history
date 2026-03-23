# Getting started

## Platform Foundation Deployment (Optional)

Deploy SageMaker Unified Studio for centralized data governance.

## Prerequisites

- Customer 360 and/or Predictive Maintenance already deployed
- AWS IAM Identity Center configured
- VPC with private subnets

## Deploy SageMaker Unified Studio

```
# Navigate to platform foundation directory
cd automotive-data-platform-on-aws/platform-foundation

# Install dependencies
npm install

# Deploy
cdk deploy PlatformFoundationStack
```

**Deployment time**: 60 minutes

**What gets deployed**:

- SageMaker Unified Studio domain
- Amazon DataZone domain
- Lake Formation resource shares
- IAM roles for cross-domain access

## Register Data Products

**Register Customer 360**:

1. Open DataZone console
2. Create project: "Customer Analytics"
3. Publish data product:
   - Name: `customer-360-analytics`
   - Source: Glue Data Catalog `cx_analytics`
   - Tables: All 11 tables
   - Access: Request-based approval

**Register Predictive Maintenance**:

1. Create project: "Vehicle Intelligence"
2. Publish data product:
   - Name: `predictive-maintenance`
   - Source: Glue Data Catalog `mmt_predictive_maintenance`
   - Tables: All prediction tables
   - Access: Automated approval for anonymized data

## Configure Cross-Domain Access

```
# Grant Customer Analytics project access to Predictive Maintenance data
aws datazone create-subscription-grant \
  --domain-identifier dzd-... \
  --granted-entity '{"listing":{"identifier":"lst-...","revision":"1"}}' \
  --subscription-target-identifier st-... \
  --region us-east-1
```

## Test Cross-Domain Query

```
-- Query combining Customer 360 and Predictive Maintenance data
SELECT
  c.customer_id,
  c.health_score,
  c.nps,
  p.risk_level,
  p.days_to_failure,
```
