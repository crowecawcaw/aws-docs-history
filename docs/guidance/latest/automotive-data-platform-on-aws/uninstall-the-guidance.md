# Uninstall the guidance

This chapter describes how to completely remove the Automotive Data Platform from your AWS account.

###### Warning

Uninstalling the solution will permanently delete all data, configurations, and resources. This action cannot be undone. Ensure you have backups of any data you wish to retain.

## Customer 360 Cleanup

### Automated Cleanup

```
# Navigate to project directory
cd automotive-data-platform-on-aws/guidance-for-agentic-customer-360

# Run cleanup command
make cleanup

# Confirm deletion when prompted
```

**What gets deleted**:

- Bedrock Agent and Knowledge Base
- Aurora PostgreSQL cluster (with final snapshot)
- Quick Suite dashboards, datasets, and users
- Athena views
- Glue crawler and tables
- S3 buckets (after emptying)
- CloudFormation stacks
- IAM roles and policies
- Lake Formation permissions

**Cleanup time**: 15-20 minutes

### Manual Cleanup Steps

If automated cleanup fails, follow these manual steps:

#### Step 1: Delete Bedrock Resources

```
# Delete agent alias
aws bedrock-agent delete-agent-alias \
  --agent-id AGENT_ID \
  --agent-alias-id ALIAS_ID

# Delete agent
aws bedrock-agent delete-agent \
  --agent-id AGENT_ID

# Delete Knowledge Base
aws bedrock-agent delete-knowledge-base \
  --knowledge-base-id KB_ID

# Delete data source
aws bedrock-agent delete-data-source \
  --knowledge-base-id KB_ID \
  --data-source-id DS_ID
```

#### Step 2: Delete Aurora Cluster

```
# Create final snapshot (optional but recommended)
aws rds create-db-cluster-snapshot \
  --db-cluster-snapshot-identifier cx360-final-snapshot \
  --db-cluster-identifier cx360-kb-cluster

# Delete cluster (skip final snapshot if already created)
aws rds delete-db-cluster \
  --db-cluster-identifier cx360-kb-cluster \
  --skip-final-snapshot
```

#### Step 3: Delete Quick Suite Resources

```
# Delete dashboard
aws quicksight delete-dashboard \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --dashboard-id customer-360-dashboard

# Delete analysis
aws quicksight delete-analysis \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --analysis-id customer-360-analysis

# Delete datasets (repeat for all 8 datasets)
aws quicksight delete-data-set \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --data-set-id DATASET_ID

# Delete users
aws quicksight delete-user \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --namespace default \
  --user-name demo-viewer

# Delete data source
aws quicksight delete-data-source \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --data-source-id cx-analytics-athena
```

#### Step 4: Delete Athena Resources

```
# Delete views (repeat for all 8 views)
aws athena start-query-execution \
  --query-string "DROP VIEW IF EXISTS cx_analytics.customer_health_scores" \
  --query-execution-context Database=cx_analytics \
  --result-configuration OutputLocation=s3://automotive-cx-data-lake-$(aws sts get-caller-identity --query Account --output text)/athena-results/

# Delete workgroup
aws athena delete-work-group \
  --work-group cx-analytics-workgroup \
  --recursive-delete-option
```

#### Step 5: Delete Glue Resources

```
# Delete crawler
aws glue delete-crawler --name cx-analytics-crawler

# Delete tables (repeat for all 11 tables)
aws glue delete-table \
  --database-name cx_analytics \
  --name customers

# Delete database
aws glue delete-database --name cx_analytics
```

#### Step 6: Empty and Delete S3 Buckets

```
# Empty bucket
aws s3 rm s3://automotive-cx-data-lake-$(aws sts get-caller-identity --query Account --output text) --recursive

# Delete bucket
aws s3 rb s3://automotive-cx-data-lake-$(aws sts get-caller-identity --query Account --output text)
```

#### Step 7: Delete CloudFormation Stacks

```
# Delete stacks in reverse order
aws cloudformation delete-stack --stack-name cx360-dev-bedrock
aws cloudformation delete-stack --stack-name cx360-dev-etl
aws cloudformation delete-stack --stack-name cx360-dev-data-lake

# Wait for deletion to complete
aws cloudformation wait stack-delete-complete --stack-name cx360-dev-bedrock
aws cloudformation wait stack-delete-complete --stack-name cx360-dev-etl
aws cloudformation wait stack-delete-complete --stack-name cx360-dev-data-lake
```

#### Step 8: Delete Lake Formation Permissions

```
# Revoke all permissions
aws lakeformation batch-revoke-permissions \
  --entries file://revoke-permissions.json

# Remove data lake administrators
aws lakeformation put-data-lake-settings \
  --data-lake-settings '{"DataLakeAdmins":[]}'
```

## Predictive Maintenance Cleanup

### Automated Cleanup

```
# Navigate to project directory
cd automotive-data-platform-on-aws/guidance-for-predictive-maintenance/deployment

# Destroy all CDK stacks
cdk destroy --all

# Confirm deletion when prompted
```

**What gets deleted**:

- SageMaker endpoints and models
- Step Functions state machines
- Lambda functions
- Glue jobs and database
- DynamoDB tables
- SNS topics and subscriptions
- API Gateway
- S3 buckets (after emptying)
- CloudFormation stacks
- IAM roles and policies

**Cleanup time**: 10-15 minutes

### Manual Cleanup Steps

#### Step 1: Delete SageMaker Resources

```
# Delete endpoint
aws sagemaker delete-endpoint \
  --endpoint-name tire-prediction-endpoint

# Delete endpoint configuration
aws sagemaker delete-endpoint-config \
  --endpoint-config-name tire-prediction-config

# Delete model
aws sagemaker delete-model \
  --model-name tire-prediction-model

# Delete training jobs (optional, auto-deleted after 120 days)
aws sagemaker stop-training-job \
  --training-job-name tire-prediction-rcf-20260128
```

#### Step 2: Delete Step Functions

```
# Delete state machines
aws stepfunctions delete-state-machine \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT:stateMachine:ml-etl-pipeline

aws stepfunctions delete-state-machine \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT:stateMachine:ml-training-pipeline

aws stepfunctions delete-state-machine \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT:stateMachine:ml-inference-pipeline

aws stepfunctions delete-state-machine \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT:stateMachine:filtering-pipeline
```

#### Step 3: Delete Lambda Functions

```
# List and delete all Lambda functions
aws lambda list-functions \
  --query 'Functions[?contains(FunctionName, `mmt-predictive-maintenance`)].FunctionName' \
  --output text | xargs -n1 aws lambda delete-function --function-name
```

#### Step 4: Delete Glue Resources

```
# Delete Glue jobs
aws glue delete-job --job-name root-etl-pipeline
aws glue delete-job --job-name ml-feature-engineering

# Delete database
aws glue delete-database --name mmt_predictive_maintenance
```

#### Step 5: Delete DynamoDB Tables

```
# Delete table
aws dynamodb delete-table --table-name tire-alerts
```

#### Step 6: Delete SNS Topics

```
# Delete topic
aws sns delete-topic \
  --topic-arn arn:aws:sns:REGION:ACCOUNT:tire-alert-notifications
```

#### Step 7: Delete API Gateway

```
# Delete API
aws apigateway delete-rest-api --rest-api-id API_ID
```

#### Step 8: Empty and Delete S3 Buckets

```
# Empty all buckets
aws s3 rm s3://mmt-predictive-maintenance-raw-$(aws sts get-caller-identity --query Account --output text) --recursive
aws s3 rm s3://mmt-predictive-maintenance-etl-$(aws sts get-caller-identity --query Account --output text) --recursive
aws s3 rm s3://mmt-predictive-maintenance-ml-features-$(aws sts get-caller-identity --query Account --output text) --recursive
aws s3 rm s3://mmt-predictive-maintenance-predictions-$(aws sts get-caller-identity --query Account --output text) --recursive

# Delete buckets
aws s3 rb s3://mmt-predictive-maintenance-raw-$(aws sts get-caller-identity --query Account --output text)
aws s3 rb s3://mmt-predictive-maintenance-etl-$(aws sts get-caller-identity --query Account --output text)
aws s3 rb s3://mmt-predictive-maintenance-ml-features-$(aws sts get-caller-identity --query Account --output text)
aws s3 rb s3://mmt-predictive-maintenance-predictions-$(aws sts get-caller-identity --query Account --output text)
```

#### Step 9: Delete CloudFormation Stacks

```
# Delete all stacks
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-MonitoringStack
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-AlertsStack
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-FilteringStack
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-MlStack
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-EtlStack
aws cloudformation delete-stack --stack-name mmt-predictive-maintenance-DataStack
```

## Platform Foundation Cleanup

### Delete SageMaker Unified Studio

```
# Delete domain
aws sagemaker delete-domain \
  --domain-id d-... \
  --retention-policy HomeEfsFileSystem=Delete
```

### Delete DataZone Resources

```
# Delete projects
aws datazone delete-project \
  --domain-identifier dzd-... \
  --identifier prj-...

# Delete domain
aws datazone delete-domain \
  --identifier dzd-...
```

### Delete Lake Formation Resource Shares

```
# List resource shares
aws ram get-resource-shares \
  --resource-owner SELF \
  --query 'resourceShares[].resourceShareArn'

# Delete resource shares
aws ram delete-resource-share \
  --resource-share-arn arn:aws:ram:...
```

## Data Retention Considerations

Before uninstalling, consider backing up:

### Customer 360 Data

```
# Export customer data
aws s3 sync s3://automotive-cx-data-lake-<ACCOUNT-ID>/processed/ ./backup/customer-360/

# Export Athena query history
aws athena list-query-executions \
  --work-group cx-analytics-workgroup \
  --max-results 1000 > athena-query-history.json

# Export Quick Suite dashboard definition
aws quicksight describe-dashboard \
  --aws-account-id <ACCOUNT-ID> \
  --dashboard-id customer-360-dashboard > dashboard-backup.json
```

### Predictive Maintenance Data

```
# Export predictions
aws s3 sync s3://mmt-predictive-maintenance-predictions-<ACCOUNT-ID>/ ./backup/predictions/

# Export DynamoDB alerts
aws dynamodb scan \
  --table-name tire-alerts \
  --output json > alerts-backup.json

# Export trained models
aws s3 sync s3://sagemaker-REGION-<ACCOUNT-ID>/tire-prediction/ ./backup/models/
```

### Aurora Snapshots

```
# Create final snapshot before deletion
aws rds create-db-cluster-snapshot \
  --db-cluster-snapshot-identifier cx360-final-snapshot-$(date +%Y%m%d) \
  --db-cluster-identifier cx360-kb-cluster

# Snapshots are retained even after cluster deletion
# Delete snapshot manually when no longer needed:
aws rds delete-db-cluster-snapshot \
  --db-cluster-snapshot-identifier cx360-final-snapshot-20260128
```

## Verify Complete Removal

```
# Check for remaining CloudFormation stacks
aws cloudformation list-stacks \
  --stack-status-filter CREATE_COMPLETE UPDATE_COMPLETE \
  --query 'StackSummaries[?contains(StackName, `cx360`) || contains(StackName, `mmt-predictive-maintenance`)].StackName'

# Check for remaining S3 buckets
aws s3 ls | grep -E 'automotive-cx-data-lake|mmt-predictive-maintenance'

# Check for remaining Lambda functions
aws lambda list-functions \
  --query 'Functions[?contains(FunctionName, `bedrock-agent`) || contains(FunctionName, `mmt`)].FunctionName'

# Check for remaining SageMaker endpoints
aws sagemaker list-endpoints \
  --name-contains tire-prediction

# Check for remaining Glue databases
aws glue get-databases \
  --query 'DatabaseList[?contains(Name, `cx_analytics`) || contains(Name, `mmt_predictive_maintenance`)].Name'
```

## Cost After Uninstall

After uninstalling, you may still incur costs for:

- S3 snapshots (Aurora, RDS)
- CloudWatch Logs retention
- CloudTrail logs in S3
- Athena query results in S3

To eliminate all costs:

```
# Delete Aurora snapshots
aws rds delete-db-cluster-snapshot \
  --db-cluster-snapshot-identifier cx360-final-snapshot

# Delete CloudWatch log groups
aws logs delete-log-group --log-group-name /aws/lambda/bedrock-agent-athena-query
aws logs delete-log-group --log-group-name /aws-glue/jobs/output

# Empty CloudTrail S3 bucket (if dedicated to this solution)
aws s3 rm s3://cloudtrail-bucket-<ACCOUNT-ID> --recursive
```

## Re-deployment

To re-deploy the solution after uninstalling:

1. Follow the deployment instructions in the Deploy the Solution chapters
2. All resources will be created fresh
3. No data from previous deployment will be retained
4. New resource IDs will be generated
