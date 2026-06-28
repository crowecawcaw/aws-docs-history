# Architecture overview

The Predictive Maintenance solution follows a multi-stage architecture that processes vehicle telemetry data through parallel prediction pipelines.

![Predictive Maintenance Architecture](images/predictive.png)

## High-Level Architecture

The architecture consists of:

1. **Data Source Layer**: Amazon Redshift cluster containing vehicle telemetry data
2. **ETL Processing Layer**: AWS Glue jobs that transform and prepare data hourly
3. **Prediction Layer**: Dual-path processing with ML and filter-based approaches
4. **Alert Layer**: Consolidation and delivery of maintenance alerts
5. **Storage Layer**: Amazon S3 for intermediate data and Amazon DynamoDB for alert state

## Data Flow

The solution processes data through the following stages:

### Stage 1: Data Ingestion

- Telemetry data is accessed from Amazon Redshift via Datashare or S3 unload
- Root ETL pipeline runs hourly to extract new data
- Data is transformed into standardized formats and stored in S3

### Stage 2: Parallel Processing

Two independent pipelines process the data:

**Machine Learning Pipeline:**
\* ML ETL prepares features from historical data
\* Training pipeline updates models weekly using Amazon SageMaker
\* Inference pipeline runs batch predictions on new data
\* Anomaly scores are generated for each vehicle/tire combination

**Filter-Based Pipeline:**
\* Statistical filters analyze pressure trends
\* Leak rates are calculated using time-series analysis
\* Alerts are generated when thresholds are exceeded

### Stage 3: Alert Consolidation

- Results from both pipelines are merged
- Duplicate alerts are deduplicated
- Severity levels are assigned based on leak rates
- Alert status is tracked in DynamoDB

### Stage 4: Alert Delivery

- Alerts are formatted for downstream systems
- Integration APIs provide real-time access to alert data
- Historical alert data is maintained for analysis

## Key AWS Services

The solution leverages the following AWS services:

- **Amazon Redshift**: Source data warehouse for vehicle telemetry
- **AWS Glue**: Serverless ETL for data transformation
- **Amazon SageMaker**: ML model training and batch inference
- **Amazon S3**: Data lake storage for intermediate and processed data
- **Amazon DynamoDB**: Alert state management and tracking
- **AWS Lambda**: Event-driven processing and orchestration
- **Amazon EventBridge**: Scheduling and workflow coordination
- **AWS Step Functions**: ML pipeline orchestration
