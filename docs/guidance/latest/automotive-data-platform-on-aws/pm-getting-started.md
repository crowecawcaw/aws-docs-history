# Getting started

This section provides step-by-step instructions for deploying the Predictive Maintenance solution, including model training, inference pipeline setup, and alert configuration.

## How the Predictive Maintenance Model Works

The solution implements a tire pressure anomaly detection system using a multi-stage machine learning pipeline. Here’s how it works step-by-step:

### Step 1: Data Collection and Preparation

The system begins by collecting tire pressure telemetry from your vehicle fleet stored in Amazon Redshift. An AWS Glue ETL job runs hourly to extract new sensor readings and transform them into a standardized format.

**What happens:**

- Tire pressure readings are extracted from Redshift (or S3 if using data lake)
- Data is validated and cleansed to remove sensor errors
- Readings are normalized and aggregated by vehicle and tire position
- Processed data is stored in S3 in Parquet format for efficient querying

**Key outputs:** Hourly batches of clean telemetry data ready for analysis

### Step 2: Feature Engineering

Raw pressure readings are transformed into meaningful features that the ML model can learn from. This includes calculating pressure trends, rate of change, and statistical patterns.

**What happens:**

- Time-series features are calculated (rolling averages, standard deviations)
- Pressure drop rates are computed over 6-hour, 12-hour, and 24-hour windows
- Contextual features are added (temperature, vehicle load, driving conditions)
- Historical baseline pressures are retrieved for comparison

**Key outputs:** Feature dataset with 20+ engineered attributes per tire reading

### Step 3: Model Training

A Random Cut Forest (RCF) algorithm trains on historical data to learn normal tire pressure patterns. The model identifies what "healthy" tire behavior looks like across different conditions.

**What happens:**

- Amazon SageMaker trains an RCF model on 30 days of historical data
- The model learns normal pressure patterns for different vehicle types and conditions
- Training runs weekly (configurable) to adapt to seasonal changes
- Model artifacts are versioned and stored in S3

**Key outputs:** Trained anomaly detection model that scores tire readings from 0-1 (0=normal, 1=anomalous)

### Step 4: Batch Inference

The trained model processes new tire readings daily, generating anomaly scores that indicate the likelihood of a tire issue developing.

**What happens:**

- SageMaker Batch Transform runs inference on the latest telemetry data
- Each tire reading receives an anomaly score
- Scores above 0.7 trigger alerts for potential issues
- Predictions include 7-14 day advance warning before likely failure

**Key outputs:** Daily predictions with anomaly scores and estimated failure dates

### Step 5: Filter-Based Validation

A parallel statistical filter validates ML predictions using physics-based rules. This catches rapid pressure drops that might indicate immediate leaks.

**What happens:**

- Pressure drop rates are compared against threshold values
- Leak rates are calculated using time-series regression
- Alerts are generated for drops exceeding 2 PSI per hour
- Results are cross-referenced with ML predictions

**Key outputs:** Validated alerts with both ML and statistical confidence scores

### Step 6: Alert Consolidation and Delivery

Alerts from both pipelines are merged, deduplicated, and delivered to your maintenance systems via API or SNS notifications.

**What happens:**

- Duplicate alerts are removed (same vehicle/tire from both pipelines)
- Severity levels are assigned (Critical: >5 PSI drop, Warning: 2-5 PSI drop)
- Alert state is tracked in DynamoDB to prevent duplicate notifications
- Alerts are sent to fleet management systems via REST API or email

**Key outputs:** Actionable maintenance alerts with vehicle ID, tire position, severity, and predicted failure date

## Implementation Steps

```
# Install CDK dependencies
cd deployment
npm install

# Install Python dependencies
pip3 install -r requirements.txt

# Return to project root
cd ..
```

## Configure Environment Variables

```
# Copy example environment file
cp .env.example .env

# Edit .env file
nano .env
```

**Required environment variables**:

```
# AWS Configuration
AWS_ACCOUNT_ID=123456789012
AWS_REGION=us-east-1
AWS_PROFILE=default

# Redshift Configuration
REDSHIFT_DATASHARE_ARN=arn:aws:redshift:us-east-1:123456789012:datashare:...
REDSHIFT_DATABASE=telemetry_db
REDSHIFT_SCHEMA=public

# S3 Configuration
RAW_DATA_BUCKET=mmt-predictive-maintenance-raw
ETL_DATA_BUCKET=mmt-predictive-maintenance-etl
ML_FEATURES_BUCKET=mmt-predictive-maintenance-ml-features

# ML Configuration
TRAINING_INSTANCE_TYPE=ml.m5.xlarge
INFERENCE_INSTANCE_TYPE=ml.m5.large
MODEL_TRAINING_SCHEDULE=cron(0 2 ? * SUN *)  # Weekly Sunday 2 AM
INFERENCE_SCHEDULE=cron(0 6 * * ? *)         # Daily 6 AM

# Alerts Configuration
ALERT_SNS_EMAIL=fleet-managers@example.com
ALERT_API_ENDPOINT=https://relay-garage-system.example.com/api/alerts
```

## Bootstrap CDK (First-Time Only)

```
# Bootstrap CDK
cdk bootstrap aws://ACCOUNT-ID/REGION
```

## Deploy Infrastructure Stacks

```
# Synthesize CloudFormation templates
cdk synth

# Deploy all stacks
cdk deploy --all

# Or deploy stacks individually:
cdk deploy DataStack
cdk deploy EtlStack
cdk deploy MlStack
cdk deploy FilteringStack
cdk deploy AlertsStack
cdk deploy MonitoringStack
```

**Deployment time**: 30 minutes

**What gets deployed**:

1. **DataStack**
   - S3 buckets: raw, etl, ml-features, predictions
   - Glue database: `mmt_predictive_maintenance`
   - DynamoDB table: `tire-alerts`

2. **EtlStack**
   - Lambda: `redshift-query-lambda`
   - Glue job: `root-etl-pipeline`
   - CloudWatch Events: Hourly triggers
   - IAM roles: Glue and Lambda execution roles

3. **MlStack**
   - Step Functions: `ml-etl-pipeline`, `ml-training-pipeline`, `ml-inference-pipeline`
   - Lambda: Path resolvers, monitoring functions
   - Glue job: `ml-feature-engineering`
   - SSM Parameter: `/mmt/predictive-maintenance/latest-model`

4. **FilteringStack**
   - Step Function: `filtering-pipeline`
   - Lambda: `filtering-algorithm`
   - CloudWatch Events: Daily trigger

5. **AlertsStack**
   - Lambda: `generate-alerts`
   - SNS topic: `tire-alert-notifications`
   - API Gateway: `alerts-api`
   - S3 event notifications

6. **MonitoringStack**
   - CloudWatch dashboards
   - CloudWatch alarms
   - X-Ray tracing

**Verification**:

```
# Check all stacks
aws cloudformation list-stacks \
  --stack-status-filter CREATE_COMPLETE \
  --region us-east-1 \
  --query 'StackSummaries[?contains(StackName, `mmt-predictive-maintenance`)].StackName'

# Verify S3 buckets
aws s3 ls | grep mmt-predictive-maintenance

# Verify Glue database
aws glue get-database \
  --name mmt_predictive_maintenance \
  --region us-east-1

# Verify Step Functions
aws stepfunctions list-state-machines \
  --region us-east-1 \
  --query 'stateMachines[?contains(name, `ml`)].name'
```

## Manual Step: Configure Redshift Datashare

**Important**: This step must be completed manually before the ETL pipeline can run.

**Option 1: Redshift Datashare (Recommended)**

```
-- In the source Redshift cluster, create datashare
CREATE DATASHARE tire_telemetry_share;

-- Add schema to datashare
ALTER DATASHARE tire_telemetry_share ADD SCHEMA public;

-- Add tables to datashare
ALTER DATASHARE tire_telemetry_share ADD TABLE public.tire_telemetry;
ALTER DATASHARE tire_telemetry_share ADD TABLE public.vehicle_metadata;

-- Grant usage to consumer account
GRANT USAGE ON DATASHARE tire_telemetry_share TO ACCOUNT '123456789012';
```

**In the consumer account (where solution is deployed)**:

```
-- Create database from datashare
CREATE DATABASE tire_telemetry_db FROM DATASHARE tire_telemetry_share
OF ACCOUNT '987654321098' NAMESPACE 'source-namespace-guid';

-- Grant permissions to Lambda execution role
GRANT USAGE ON DATABASE tire_telemetry_db TO IAM_ROLE 'arn:aws:iam::123456789012:role/mmt-lambda-execution-role';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO IAM_ROLE 'arn:aws:iam::123456789012:role/mmt-lambda-execution-role';
```

**Option 2: S3 Unload (Alternative)**

If using S3 unload instead of datashare:

1. Configure Redshift to UNLOAD data to S3 raw bucket hourly
2. Remove `redshift-query-lambda` from deployment
3. Update `root-etl-pipeline` Glue job to read from S3 directly

## Trigger Initial ETL Run

```
# Manually trigger the query Lambda
aws lambda invoke \
  --function-name redshift-query-lambda \
  --region us-east-1 \
  response.json

# Check response
cat response.json

# Wait 30 minutes, then trigger ETL Glue job
aws glue start-job-run \
  --job-name root-etl-pipeline \
  --region us-east-1

# Monitor job status
aws glue get-job-run \
  --job-name root-etl-pipeline \
  --run-id jr_... \
  --region us-east-1 \
  --query 'JobRun.JobRunState'
```

## Trigger Initial ML Training

```
# Start ML ETL pipeline
aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:ml-etl-pipeline \
  --region us-east-1

# Wait for completion (check in console or poll status)

# Start ML training pipeline
aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:ml-training-pipeline \
  --region us-east-1

# Monitor training in SageMaker console
# Training takes ~30-45 minutes
```

## Test Inference Pipeline

```
# After training completes, run inference
aws stepfunctions start-execution \
  --state-machine-arn arn:aws:states:us-east-1:123456789012:stateMachine:ml-inference-pipeline \
  --region us-east-1

# Check predictions in S3
aws s3 ls s3://mmt-predictive-maintenance-processed-predictions-$(aws sts get-caller-identity --query Account --output text)/

# Query predictions in DynamoDB
aws dynamodb scan \
  --table-name tire-alerts \
  --region us-east-1 \
  --limit 10
```

## Configure Alert Notifications

```
# Subscribe email to SNS topic
aws sns subscribe \
  --topic-arn arn:aws:sns:us-east-1:123456789012:tire-alert-notifications \
  --protocol email \
  --notification-endpoint fleet-manager@example.com \
  --region us-east-1

# Confirm subscription via email
```
