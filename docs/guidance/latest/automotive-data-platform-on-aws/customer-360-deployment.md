# Deployment guide

Deploy the Customer 360 solution in 5 phases using the provided CDK stacks.

## Prerequisites

**AWS account requirements**:
\* Admin access or equivalent permissions
\* Quick Suite Enterprise subscription
\* Bedrock model access (Claude 3.5 Sonnet)
\* Service quotas for S3, Glue, Athena, Aurora

**Local environment**:
\* AWS CLI configured
\* Node.js 18+ installed
\* Python 3.9+ installed
\* CDK CLI: `npm install -g aws-cdk`

## Deployment phases

**Phase 1: Data Lake Foundation** (10 minutes)

```
cd guidance-for-agentic-customer-360
make phase1
```

Creates S3 bucket, Glue database, Athena workgroup, Lake Formation permissions.

**Phase 2: ETL & Prerequisites** (5 minutes)

```
make phase2
```

Creates Glue crawler, IAM roles, Quick Suite data source.

**Phase 3: Data Generation** (20 minutes)

```
make phase3
```

Generates 500K customers, 1.4M interactions, 8 Athena views.

**Phase 4: Quick Suite Dashboards** (15 minutes)

```
make phase4
```

Creates 8 datasets, dashboard, demo user.

**Phase 5: Bedrock AI Agent** (30 minutes)

```
make phase5
```

Deploys Aurora cluster, Knowledge Base, Bedrock Agent, Lambda functions.

## Verification

**Check data**:

```
aws s3 ls s3://automotive-cx-data-lake-<ACCOUNT-ID>/raw/
aws athena start-query-execution \
  --query-string "SELECT COUNT(*) FROM customers" \
  --query-execution-context Database=cx_analytics
```

**Check Quick Suite**:

```
aws quicksight list-data-sets --aws-account-id <ACCOUNT-ID>
aws quicksight list-dashboards --aws-account-id <ACCOUNT-ID>
```

**Check Bedrock**:

```
aws bedrock-agent list-knowledge-bases
aws bedrock-agent list-agents
```
