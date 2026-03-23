# Troubleshooting

This chapter provides solutions to common issues encountered when deploying and operating the Automotive Data Platform.

## Customer 360 Issues

### Glue Crawler Failures

**Symptom**: Crawler fails with "Insufficient permissions" error

**Solution**:

```
# Grant Lake Formation permissions
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::ACCOUNT:role/AWSGlueServiceRole-cx360 \
  --resource '{"Database":{"Name":"cx_analytics"}}' \
  --permissions CREATE_TABLE ALTER DROP

# Grant S3 permissions
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::ACCOUNT:role/AWSGlueServiceRole-cx360 \
  --resource '{"DataLocation":{"ResourceArn":"arn:aws:s3:::automotive-cx-data-lake-<ACCOUNT-ID>"}}' \
  --permissions DATA_LOCATION_ACCESS
```

**Symptom**: Crawler completes but no tables created

**Solution**: Check S3 data exists and is in correct format

```
# Verify data exists
aws s3 ls s3://automotive-cx-data-lake-<ACCOUNT-ID>/processed/customers/ --recursive

# Check Parquet file validity
aws s3 cp s3://automotive-cx-data-lake-<ACCOUNT-ID>/processed/customers/part-00000.parquet - | head

# Re-run crawler
aws glue start-crawler --name cx-analytics-crawler
```

### Athena Query Failures

**Symptom**: "HIVE_PARTITION_SCHEMA_MISMATCH" error

**Solution**: Drop and recreate table

```
-- Drop table
DROP TABLE cx_analytics.customers;

-- Re-run crawler to recreate with correct schema
```

**Symptom**: "Access Denied" when querying table

**Solution**: Grant Lake Formation permissions

```
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::ACCOUNT:user/USERNAME \
  --resource '{"Table":{"DatabaseName":"cx_analytics","Name":"customers"}}' \
  --permissions SELECT
```

**Symptom**: Query times out after 30 minutes

**Solution**: Optimize query with partitioning

```
-- Use partition pruning
SELECT * FROM cx_analytics.customers
WHERE year = '2026' AND month = '01'
LIMIT 1000;

-- Check partitions exist
SHOW PARTITIONS cx_analytics.customers;
```

### Quick Suite Issues

**Symptom**: Dataset refresh fails with "Access Denied"

**Solution**: Update Quick Suite service role permissions

```
# Attach Lake Formation permissions to Quick Suite role
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::ACCOUNT:role/aws-quicksight-service-role-v0 \
  --resource '{"Table":{"DatabaseName":"cx_analytics","TableWildcard":{}}}' \
  --permissions SELECT
```

**Symptom**: Dashboard shows "No data available"

**Solution**: Refresh datasets manually

```
# Trigger dataset refresh
aws quicksight create-ingestion \
  --aws-account-id <ACCOUNT-ID> \
  --data-set-id DATASET_ID \
  --ingestion-id $(date +%s)
```

**Symptom**: User cannot access dashboard

**Solution**: Grant dashboard permissions

```
aws quicksight update-dashboard-permissions \
  --aws-account-id <ACCOUNT-ID> \
  --dashboard-id customer-360-dashboard \
  --grant-permissions Principal=arn:aws:quicksight:REGION:ACCOUNT:user/default/USERNAME,Actions=quicksight:DescribeDashboard,quicksight:ListDashboardVersions,quicksight:QueryDashboard
```

### Bedrock Agent Issues

**Symptom**: Agent returns "I don’t have access to that information"

**Solution**: Verify Knowledge Base sync and Lambda permissions

```
# Check Knowledge Base sync status
aws bedrock-agent get-knowledge-base --knowledge-base-id KB_ID

# Test Lambda function directly
aws lambda invoke \
  --function-name bedrock-agent-athena-query \
  --payload '{"query":"SELECT COUNT(*) FROM cx_analytics.customers"}' \
  response.json

cat response.json
```

**Symptom**: Agent responses are slow (>30 seconds)

**Solution**: Optimize Athena queries and increase Lambda memory

```
# Increase Lambda memory
aws lambda update-function-configuration \
  --function-name bedrock-agent-athena-query \
  --memory-size 1024 \
  --timeout 60

# Add Athena result caching
# Edit Lambda to check for cached results before querying
```

**Symptom**: Agent exposes PII in responses

**Solution**: Enable Bedrock Guardrails

```
# Create guardrail
aws bedrock create-guardrail \
  --name customer-360-guardrail \
  --blocked-input-messaging "I cannot process requests containing PII" \
  --blocked-outputs-messaging "I cannot provide responses containing PII" \
  --content-policy-config '{"filtersConfig":[{"type":"PII","inputStrength":"HIGH","outputStrength":"HIGH"}]}'

# Update agent to use guardrail
aws bedrock-agent update-agent \
  --agent-id AGENT_ID \
  --guardrail-configuration guardrailIdentifier=GUARDRAIL_ID,guardrailVersion=1
```

### Aurora Issues

**Symptom**: Cannot connect to Aurora cluster

**Solution**: Verify security group and network configuration

```
# Check cluster status
aws rds describe-db-clusters \
  --db-cluster-identifier cx360-kb-cluster \
  --query 'DBClusters[0].Status'

# Verify security group allows Lambda access
aws ec2 describe-security-groups \
  --group-ids sg-... \
  --query 'SecurityGroups[0].IpPermissions'

# Test connectivity from Lambda
aws lambda invoke \
  --function-name test-aurora-connection \
  response.json
```

**Symptom**: Vector search is slow

**Solution**: Rebuild HNSW index

```
-- Connect to Aurora
psql -h CLUSTER_ENDPOINT -U postgres -d bedrock_kb

-- Rebuild index
REINDEX INDEX bedrock_integration.bedrock_kb_embedding_idx;

-- Analyze table
ANALYZE bedrock_integration.bedrock_kb;
```

## Predictive Maintenance Issues

### Redshift Datashare Issues

**Symptom**: Cannot query datashare tables

**Solution**: Verify datashare permissions

```
-- In consumer account
SELECT * FROM svv_datashares;

-- Grant permissions to role
GRANT USAGE ON DATABASE tire_telemetry_db TO IAM_ROLE 'arn:aws:iam::ACCOUNT:role/lambda-execution-role';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO IAM_ROLE 'arn:aws:iam::ACCOUNT:role/lambda-execution-role';
```

**Symptom**: Datashare not visible in consumer account

**Solution**: Accept datashare invitation

```
-- List pending datashares
SELECT * FROM svv_datashare_consumers WHERE share_name = 'tire_telemetry_share';

-- Create database from datashare
CREATE DATABASE tire_telemetry_db FROM DATASHARE tire_telemetry_share
OF ACCOUNT 'PRODUCER_ACCOUNT' NAMESPACE 'NAMESPACE_GUID';
```

### Glue ETL Issues

**Symptom**: Root ETL job fails with "No data found"

**Solution**: Verify Redshift query Lambda executed successfully

```
# Check Lambda logs
aws logs tail /aws/lambda/redshift-query-lambda --follow

# Verify data in S3 raw bucket
aws s3 ls s3://mmt-predictive-maintenance-raw-<ACCOUNT-ID>/ --recursive

# Manually trigger Lambda
aws lambda invoke \
  --function-name redshift-query-lambda \
  response.json
```

**Symptom**: ETL job runs out of memory

**Solution**: Increase DPU allocation

```
# Update Glue job
aws glue update-job \
  --job-name root-etl-pipeline \
  --job-update '{"MaxCapacity":20}'

# Or use G.2X workers for more memory
aws glue update-job \
  --job-name root-etl-pipeline \
  --job-update '{"WorkerType":"G.2X","NumberOfWorkers":10}'
```

### SageMaker Training Issues

**Symptom**: Training job fails with "ResourceLimitExceeded"

**Solution**: Request quota increase or use different instance type

```
# Check current quotas
aws service-quotas get-service-quota \
  --service-code sagemaker \
  --quota-code L-... \
  --region us-east-1

# Use smaller instance type
# Edit Step Function to use ml.m5.large instead of ml.m5.xlarge
```

**Symptom**: Training job fails with "AlgorithmError"

**Solution**: Check training data format and hyperparameters

```
# View training logs
aws logs tail /aws/sagemaker/TrainingJobs --follow

# Verify training data
aws s3 cp s3://mmt-predictive-maintenance-ml-features-<ACCOUNT-ID>/features/2026/01/28/part-00000.csv - | head

# Check for NaN or infinite values
# Ensure all features are numeric
```

**Symptom**: Model accuracy is poor

**Solution**: Retrain with more data or adjust hyperparameters

```
# Increase training data window from 30 to 90 days
# Edit ML ETL Lambda to include more historical data

# Adjust hyperparameters
# Edit Step Function training step:
{
  "num_trees": 200,
  "num_samples_per_tree": 512,
  "feature_dim": 25
}
```

### Inference Issues

**Symptom**: Batch transform job fails

**Solution**: Check input data format

```
# View transform logs
aws logs tail /aws/sagemaker/TransformJobs --follow

# Verify input data matches training format
aws s3 cp s3://mmt-predictive-maintenance-ml-features-<ACCOUNT-ID>/features/latest/part-00000.csv - | head

# Ensure no header row in inference data
```

**Symptom**: Predictions are all the same value

**Solution**: Check feature engineering and model version

```
# Verify correct model is deployed
aws ssm get-parameter \
  --name /mmt/predictive-maintenance/latest-model \
  --query 'Parameter.Value'

# Check feature statistics
# Ensure features have variance (not all constant)
```

### Alert Issues

**Symptom**: No alerts generated despite high-risk predictions

**Solution**: Check S3 event notification and Lambda function

```
# Verify S3 event notification configured
aws s3api get-bucket-notification-configuration \
  --bucket mmt-predictive-maintenance-processed-predictions-<ACCOUNT-ID>

# Check Lambda logs
aws logs tail /aws/lambda/generate-alerts --follow

# Manually trigger alert Lambda
aws lambda invoke \
  --function-name generate-alerts \
  --payload file://test-event.json \
  response.json
```

**Symptom**: Duplicate alerts sent

**Solution**: Implement deduplication logic

```
# Check DynamoDB for existing alert
response = dynamodb.get_item(
    TableName='tire-alerts',
    Key={'aaid': aaid, 'timestamp': timestamp}
)

if 'Item' in response:
    # Alert already exists, skip
    return
```

## Platform Foundation Issues

### DataZone Issues

**Symptom**: Cannot publish data product

**Solution**: Verify Lake Formation permissions

```
# Grant DataZone role access to Glue catalog
aws lakeformation grant-permissions \
  --principal DataLakePrincipalIdentifier=arn:aws:iam::ACCOUNT:role/AmazonDataZoneRole \
  --resource '{"Database":{"Name":"cx_analytics"}}' \
  --permissions DESCRIBE
```

**Symptom**: Cross-domain query fails

**Solution**: Verify resource share accepted

```
# List resource shares
aws ram get-resource-shares \
  --resource-owner OTHER-ACCOUNTS

# Accept resource share
aws ram accept-resource-share-invitation \
  --resource-share-invitation-arn arn:aws:ram:...
```

## General Debugging Techniques

### CloudWatch Logs Insights

```
# Find errors in Lambda logs
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 20

# Find slow Athena queries
fields @timestamp, queryExecutionId, query, executionTime
| filter executionTime > 60000
| sort executionTime desc
```

### X-Ray Tracing

```
# View trace map
aws xray get-trace-graph \
  --trace-ids TRACE_ID

# Find slow segments
aws xray get-trace-summaries \
  --start-time $(date -u -d '1 hour ago' +%s) \
  --end-time $(date -u +%s) \
  --filter-expression 'duration > 5'
```

### Cost Analysis

```
# Check unexpected costs
aws ce get-cost-and-usage \
  --time-period Start=2026-01-01,End=2026-01-31 \
  --granularity DAILY \
  --metrics BlendedCost \
  --group-by Type=SERVICE

# Identify expensive resources
aws ce get-cost-and-usage \
  --time-period Start=2026-01-01,End=2026-01-31 \
  --granularity DAILY \
  --metrics BlendedCost \
  --group-by Type=TAG,Key=Name
```

## Getting Support

**AWS Support**:

- Open case in AWS Console
- Include: Stack name, error message, CloudWatch Logs
- Attach: CloudFormation events, Lambda logs

**Community Support**:

- GitHub Issues: https://github.com/aws-solutions-library-samples/guidance-for-automotive-data-platform-on-aws/issues
- AWS re:Post: https://repost.aws/tags/automotive
- AWS Forums: https://forums.aws.amazon.com/

**Documentation**:

- AWS Service documentation
- Solution README files
- Architecture diagrams
