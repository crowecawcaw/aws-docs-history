

# Getting started
<a name="pm-getting-started"></a>

This section provides an overview of how to implement the Predictive Maintenance pattern, including model training, inference pipeline setup, and alert configuration.

## How the Predictive Maintenance Model Works
<a name="how-the-predictive-maintenance-model-works"></a>

The solution implements a tire pressure anomaly detection system using a multi-stage machine learning pipeline. Here’s how it works step-by-step:

### Step 1: Data Collection and Preparation
<a name="step-1-data-collection-and-preparation"></a>

The system begins by collecting tire pressure telemetry from your vehicle fleet stored in Amazon Redshift. An AWS Glue ETL job runs hourly to extract new sensor readings and transform them into a standardized format.

 **What happens:** 
+ Tire pressure readings are extracted from Redshift (or S3 if using data lake)
+ Data is validated and cleansed to remove sensor errors
+ Readings are normalized and aggregated by vehicle and tire position
+ Processed data is stored in S3 in Parquet format for efficient querying

 **Key outputs:** Hourly batches of clean telemetry data ready for analysis

### Step 2: Feature Engineering
<a name="step-2-feature-engineering"></a>

Raw pressure readings are transformed into meaningful features that the ML model can learn from. This includes calculating pressure trends, rate of change, and statistical patterns.

 **What happens:** 
+ Time-series features are calculated (rolling averages, standard deviations)
+ Pressure drop rates are computed over 6-hour, 12-hour, and 24-hour windows
+ Contextual features are added (temperature, vehicle load, driving conditions)
+ Historical baseline pressures are retrieved for comparison

 **Key outputs:** Feature dataset with 20\+ engineered attributes per tire reading

### Step 3: Model Training
<a name="step-3-model-training"></a>

A Random Cut Forest (RCF) algorithm trains on historical data to learn normal tire pressure patterns. The model identifies what "healthy" tire behavior looks like across different conditions.

 **What happens:** 
+ Amazon SageMaker trains an RCF model on 30 days of historical data
+ The model learns normal pressure patterns for different vehicle types and conditions
+ Training runs weekly (configurable) to adapt to seasonal changes
+ Model artifacts are versioned and stored in S3

 **Key outputs:** Trained anomaly detection model that scores tire readings from 0-1 (0=normal, 1=anomalous)

### Step 4: Batch Inference
<a name="step-4-batch-inference"></a>

The trained model processes new tire readings daily, generating anomaly scores that indicate the likelihood of a tire issue developing.

 **What happens:** 
+ SageMaker Batch Transform runs inference on the latest telemetry data
+ Each tire reading receives an anomaly score
+ Scores above 0.7 trigger alerts for potential issues
+ Predictions include 7-14 day advance warning before likely failure

 **Key outputs:** Daily predictions with anomaly scores and estimated failure dates

### Step 5: Filter-Based Validation
<a name="step-5-filter-based-validation"></a>

A parallel statistical filter validates ML predictions using physics-based rules. This catches rapid pressure drops that might indicate immediate leaks.

 **What happens:** 
+ Pressure drop rates are compared against threshold values
+ Leak rates are calculated using time-series regression
+ Alerts are generated for drops exceeding 2 PSI per hour
+ Results are cross-referenced with ML predictions

 **Key outputs:** Validated alerts with both ML and statistical confidence scores

### Step 6: Alert Consolidation and Delivery
<a name="step-6-alert-consolidation-and-delivery"></a>

Alerts from both pipelines are merged, deduplicated, and delivered to your maintenance systems via API or SNS notifications.

 **What happens:** 
+ Duplicate alerts are removed (same vehicle/tire from both pipelines)
+ Severity levels are assigned (Critical: >5 PSI drop, Warning: 2-5 PSI drop)
+ Alert state is tracked in DynamoDB to prevent duplicate notifications
+ Alerts are sent to fleet management systems via REST API or email

 **Key outputs:** Actionable maintenance alerts with vehicle ID, tire position, severity, and predicted failure date

## Implementation Overview
<a name="implementation-overview"></a>

The reference implementation uses AWS CDK (Python) to deploy the infrastructure. A typical deployment bootstraps the CDK environment, deploys the stacks (data storage, ETL pipelines, ML components, filtering logic, alerts, and monitoring), then completes a one-time manual step to configure the Redshift Datashare permissions described in the Data Source section above.

 **Deployment time**: 30-45 minutes for the CDK stacks; additional time for the Redshift datashare configuration.

## Configure Environment Variables
<a name="configure-environment-variables"></a>

Key configuration parameters for this pattern:

```
# AWS Configuration
AWS_ACCOUNT_ID=<account-id>
AWS_REGION=us-east-1

# Redshift Configuration
REDSHIFT_DATABASE=telemetry_db
REDSHIFT_SCHEMA=public

# S3 Configuration
RAW_DATA_BUCKET=predictive-maintenance-raw
ETL_DATA_BUCKET=predictive-maintenance-etl
ML_FEATURES_BUCKET=predictive-maintenance-ml-features

# ML Configuration
TRAINING_INSTANCE_TYPE=ml.m5.xlarge
INFERENCE_INSTANCE_TYPE=ml.m5.large
MODEL_TRAINING_SCHEDULE=cron(0 2 ? * SUN *)  # Weekly Sunday 2 AM
INFERENCE_SCHEDULE=cron(0 6 * * ? *)         # Daily 6 AM

# Alerts Configuration
ALERT_SNS_EMAIL=fleet-managers@example.com
ALERT_API_ENDPOINT=https://relay-garage-system.example.com/api/alerts
```

## CMS Integration: Quick Start
<a name="cms-integration-quick-start"></a>

For customers using the [CMS](https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/developer-guide.html), follow these steps to connect the tire prediction model to your CMS telemetry pipeline.

### Step 1: Generate training data
<a name="step-1-generate-training-data"></a>

The solution includes a synthetic data generator that creates realistic tire telemetry with injected anomalies:

```
cd guidance-for-predictive-maintenance
python3 scripts/generate_training_data.py
```

This creates 721,024 records across 50 vehicles over 6 months, including:
+ Normal driving patterns with seasonal temperature effects
+ Slow leaks (8% of vehicle-tires, 0.3–1.2 PSI/day loss)
+ Punctures (4%, sudden pressure drop)
+ Valve failures (3%, intermittent pressure loss)
+ Overinflation events (2%)

Output: `data/training/tire_telemetry_full.parquet` (17.5 MB)

### Step 2: Train the model
<a name="step-2-train-the-model"></a>

 **Option A: Command line** 

```
python3 scripts/train_model.py \
  --region us-east-2 \
  --role-arn arn:aws:iam::<account-id>:role/cms-sagemaker-execution-role \
  --bucket cms-tire-prediction-<account-id>-<region> \
  --deploy
```

 **Option B: SageMaker notebook** 

Open `notebooks/train_tire_model.ipynb` in SageMaker Studio or a local Jupyter environment. The notebook provides:
+ Data exploration and visualization (pressure distributions, slow leak examples)
+ Feature preparation and normalization
+ Model training with progress monitoring
+ Evaluation with precision/recall/F1 metrics
+ Anomaly score distribution visualization
+ Endpoint deployment and SSM configuration

Both options train a SageMaker Random Cut Forest model (\~3 minutes), deploy a real-time endpoint (\~5 minutes), and save configuration to SSM Parameter Store.

### Step 3: Deploy CMS integration
<a name="step-3-deploy-cms-integration"></a>

Deploy the CDK stack to create the prediction Lambdas and EventBridge schedule:

```
cd source/infrastructure
DEPLOYMENT_STAGE=prod cdk deploy tire-predictive-maintenance-stack
```

This creates:
+  `cms-{stage}-daily-tire-check` Lambda — runs daily, detects slow leak trends
+  `cms-{stage}-blowout-risk` Lambda — real-time highway blowout risk assessment
+ EventBridge schedule (daily at 10 AM UTC)
+ IAM roles with least-privilege permissions
+ S3 bucket for training artifacts

### Step 4: Verify end-to-end
<a name="step-4-verify-end-to-end"></a>

Start a simulation in the CMS Fleet Manager UI with the "Tire pressure below safe threshold" maintenance event selected. Within 2 minutes:

1. The simulator gradually drops tire pressure from 32 PSI toward 20 PSI

1. The Flink MaintenanceProcessor detects `maintenance.tire_pressure` when pressure crosses 28 PSI

1. A maintenance alert appears on the vehicle detail page with a $35 estimated repair cost

1. The daily tire check Lambda (when run) detects the pressure trend and writes a `prediction.tire_slow_leak` warning

For highway blowout risk testing, select "Highway blowout risk" which creates a composite condition: tire pressure drops below 30 PSI while vehicle speed exceeds 60 mph. The SageMaker endpoint evaluates the multi-signal risk pattern and writes a `prediction.blowout_risk` alert.

### SSM Parameters
<a name="ssm-parameters"></a>

After training, the following parameters are available:


| Parameter | Description | 
| --- | --- | 
|  `/tire-prediction/{stage}/normalization-stats`  | Feature normalization (mean/std per feature) | 
|  `/tire-prediction/{stage}/anomaly-threshold`  | Anomaly score threshold for blowout risk detection | 
|  `/tire-prediction/{stage}/endpoint-name`  | SageMaker endpoint name for real-time inference | 

## Adapting this pattern to a different asset class
<a name="adapting-this-pattern-to-a-different-asset-class"></a>

Everything above this point is written against the tire reference implementation. If you’re adapting the pattern to a different asset — manufacturing equipment, HVAC, stationary batteries, or anything else with time-series sensor telemetry and a maintenance program — the pieces that change and the pieces that carry over are:

 **Changes per asset class**:
+ The telemetry schema (tire pressure/temperature → vibration, current draw, acoustic signature, or whatever your sensors emit)
+ The domain-specific feature engineering (leak rate → wear rate, thermal drift, whatever rate-of-change matters for your failure mode)
+ The alert threshold and severity bands (28 PSI / 80 PSI → whatever your asset’s safe operating range is)
+ The algorithm choice, per [Choosing an approach](pm-inference-strategy.md) above — RCF is not mandatory; pick based on whether you have labeled failure history

 **Carries over unchanged**:
+ The five-stage architecture: ingestion, feature engineering, model training, inference, alert consolidation
+ The dual-pipeline design (a trained model plus a cheap statistical filter as a lower-cost complement)
+ The Step Functions orchestration pattern for training and inference schedules
+ The alert-consolidation and deduplication logic in the Alert Management System

The reference CDK stacks in `guidance-for-predictive-maintenance/` are tire-specific, but the stack boundaries (Data, ETL, ML, Filtering, Alerts, Monitoring) reflect the architecture, not the domain — a new asset class is a new Glue schema and a new set of engineered features inside the same six stacks, not a rewrite of the pattern.