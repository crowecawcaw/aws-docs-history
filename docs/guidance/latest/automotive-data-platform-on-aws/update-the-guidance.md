# Update the guidance

This chapter describes how to update the Automotive Data Platform components.

## Update Strategy

The platform uses infrastructure as code (CDK) for updates, enabling safe, repeatable deployments with automatic rollback on failure.

**Update types**:

- Infrastructure updates: CDK stack changes
- Data model updates: Schema changes, new tables
- Dashboard updates: New visuals, dataset changes
- ML model updates: Retrain with new data, deploy new versions
- Code updates: Lambda functions, Glue jobs

## Customer 360 Updates

### Update Infrastructure

```
# Pull latest code
cd automotive-data-platform-on-aws/guidance-for-agentic-customer-360
git pull origin main

# Update CDK dependencies
cd deployment/cdk
npm update

# Deploy updated stacks
cdk deploy --all
```

### Update Data Model

**Add new table**:

```
# Add table definition to CDK stack
# Edit: deployment/cdk/lib/glue-catalog-stack.ts

# Deploy changes
cdk deploy GlueCatalogStack

# Run crawler to discover new data
aws glue start-crawler --name cx-analytics-crawler
```

**Add new Athena view**:

```
# Create view SQL file
# Edit: deployment/athena-queries/create_new_view.sql

# Execute view creation
aws athena start-query-execution \
  --query-string "$(cat deployment/athena-queries/create_new_view.sql)" \
  --query-execution-context Database=cx_analytics \
  --result-configuration OutputLocation=s3://automotive-cx-data-lake-$(aws sts get-caller-identity --query Account --output text)/athena-results/
```

### Update Quick Suite Dashboards

```
# Update dataset definitions
cd deployment/scripts
python3 update_quicksight_datasets.py

# Export updated dashboard
aws quicksight describe-dashboard \
  --aws-account-id $(aws sts get-caller-identity --query Account --output text) \
  --dashboard-id customer-360-dashboard \
  --region us-east-1 > ../quicksight/dashboard-definition-new.json

# Import updated dashboard
python3 import_dashboard.py
```

### Update Bedrock Agent

**Update agent instructions**:

```
# Update agent
aws bedrock-agent update-agent \
  --agent-id AGENT_ID \
  --agent-name customer-360-agent \
  --instruction "Updated instructions..." \
  --foundation-model anthropic.claude-3-5-sonnet-20241022-v2:0

# Prepare new version
aws bedrock-agent prepare-agent --agent-id AGENT_ID

# Update alias to point to new version
aws bedrock-agent update-agent-alias \
  --agent-id AGENT_ID \
  --agent-alias-id ALIAS_ID \
  --agent-alias-name production \
  --routing-configuration agentVersion=DRAFT
```

**Update action groups**:

```
# Update Lambda function code
cd deployment/lambda/bedrock-agent-athena-query
zip -r function.zip .
aws lambda update-function-code \
  --function-name bedrock-agent-athena-query \
  --zip-file fileb://function.zip

# Update agent action group
aws bedrock-agent update-agent-action-group \
  --agent-id AGENT_ID \
  --agent-version DRAFT \
  --action-group-id ACTION_GROUP_ID \
  --action-group-name query-athena
```

## Predictive Maintenance Updates

### Update Infrastructure

```
# Pull latest code
cd automotive-data-platform-on-aws/guidance-for-predictive-maintenance
git pull origin main

# Update dependencies
cd deployment
npm update
pip3 install -r requirements.txt --upgrade

# Deploy updated stacks
cdk deploy --all
```

### Retrain ML Model

```
# Trigger training pipeline manually
aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:REGION:ACCOUNT:stateMachine:ml-training-pipeline \
  --input '{"training_date":"2026-01-28"}'

# Monitor training progress
aws sagemaker describe-training-job \
  --training-job-name tire-prediction-rcf-20260128

# New model automatically deployed via Step Functions
```

### Update Inference Configuration

```
# Update endpoint instance type
aws sagemaker update-endpoint \
  --endpoint-name tire-prediction-endpoint \
  --endpoint-config-name tire-prediction-config-v2

# Update auto-scaling policy
aws application-autoscaling put-scaling-policy \
  --service-namespace sagemaker \
  --resource-id endpoint/tire-prediction-endpoint/variant/AllTraffic \
  --scalable-dimension sagemaker:variant:DesiredInstanceCount \
  --policy-name tire-prediction-scaling \
  --policy-type TargetTrackingScaling \
  --target-tracking-scaling-policy-configuration \
    '{"TargetValue":1000.0,"PredefinedMetricSpecification":{"PredefinedMetricType":"SageMakerVariantInvocationsPerInstance"}}'
```

### Update Alert Configuration

```
# Update SNS topic subscriptions
aws sns subscribe \
  --topic-arn arn:aws:sns:REGION:ACCOUNT:tire-alert-notifications \
  --protocol email \
  --notification-endpoint new-manager@example.com

# Update alert Lambda function
cd deployment/lambda/generate-alerts
zip -r function.zip .
aws lambda update-function-code \
  --function-name generate-alerts \
  --zip-file fileb://function.zip
```

## Platform Foundation Updates

### Update SageMaker Unified Studio

```
# Update domain configuration
aws sagemaker update-domain \
  --domain-id d-... \
  --default-user-settings file://user-settings.json

# Update DataZone domain
aws datazone update-domain \
  --identifier dzd-... \
  --description "Updated description"
```

### Update Data Product Definitions

```
# Update data product metadata
aws datazone update-asset \
  --domain-identifier dzd-... \
  --identifier ast-... \
  --name customer-360-analytics \
  --description "Updated description with new features"
```

## Zero-Downtime Updates

### Blue-Green Deployment for SageMaker

```
# Create new endpoint configuration
aws sagemaker create-endpoint-config \
  --endpoint-config-name tire-prediction-config-v2 \
  --production-variants \
    VariantName=AllTraffic,ModelName=tire-prediction-model-new,InitialInstanceCount=2,InstanceType=ml.m5.large

# Update endpoint (automatic blue-green deployment)
aws sagemaker update-endpoint \
  --endpoint-name tire-prediction-endpoint \
  --endpoint-config-name tire-prediction-config-v2 \
  --retain-all-variant-properties

# Traffic shifts gradually to new version
# Rollback automatically if errors detected
```

### Lambda Function Versioning

```
# Publish new version
aws lambda publish-version \
  --function-name bedrock-agent-athena-query

# Update alias to new version
aws lambda update-alias \
  --function-name bedrock-agent-athena-query \
  --name production \
  --function-version 2 \
  --routing-config AdditionalVersionWeights={"1"=0.1}

# Gradually shift traffic: 90% v2, 10% v1
# Monitor for errors, then shift 100% to v2
```

## Rollback Procedures

### Rollback CDK Stack

```
# Rollback to previous stack version
aws cloudformation cancel-update-stack \
  --stack-name cx360-dev-data-lake

# Or deploy previous version from Git
git checkout previous-commit
cdk deploy
```

### Rollback SageMaker Endpoint

```
# Update endpoint to previous configuration
aws sagemaker update-endpoint \
  --endpoint-name tire-prediction-endpoint \
  --endpoint-config-name tire-prediction-config-v1
```

### Rollback Bedrock Agent

```
# Update alias to previous version
aws bedrock-agent update-agent-alias \
  --agent-id AGENT_ID \
  --agent-alias-id ALIAS_ID \
  --routing-configuration agentVersion=1
```

## Update Best Practices

- Test updates in development environment first
- Use CDK diff to preview changes before deployment
- Enable CloudFormation stack termination protection for production
- Tag resources with version numbers for tracking
- Maintain rollback plans for critical updates
- Monitor CloudWatch metrics after updates
- Use canary deployments for high-risk changes
- Document all configuration changes
- Schedule updates during low-traffic periods
- Communicate updates to stakeholders
