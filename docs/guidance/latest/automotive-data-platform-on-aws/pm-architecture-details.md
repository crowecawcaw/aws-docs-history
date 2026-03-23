# Architecture details

Amazon Redshift stores vehicle telemetry data from connected fleets, with AWS Lambda querying tire pressure readings hourly via Redshift Data API, while AWS Glue ETL jobs transform raw sensor data into standardized formats for downstream processing.

AWS Glue processes telemetry through parallel pipelines: the ML ETL prepares features for model training, while the Root ETL validates and enriches sensor readings, with both pipelines storing intermediate results in Amazon S3 using Parquet format for efficient columnar analytics.

Amazon SageMaker trains Random Cut Forest anomaly detection models weekly on historical tire pressure patterns, with SageMaker Batch Transform running daily inference to generate anomaly scores that predict tire failures 7-14 days in advance.

AWS Step Functions orchestrates the ML workflow from data validation through feature engineering, model training, evaluation, and deployment, while Amazon EventBridge schedules training runs weekly and inference jobs daily to maintain prediction accuracy.

A parallel filter-based pipeline uses statistical analysis to detect rapid pressure drops exceeding 2 PSI per hour, calculating leak rates through time-series regression and cross-referencing results with ML predictions for validation.

Amazon DynamoDB tracks alert state to prevent duplicate notifications, while AWS Lambda consolidates predictions from both ML and filter pipelines, assigns severity levels based on pressure drop rates, and delivers alerts to fleet management systems via REST API or Amazon SNS.

Amazon API Gateway provides real-time access to prediction data and alert history, enabling integration with dealer management systems, mobile apps, and customer notification workflows with sub-second latency.

## Data Source Configuration

**Redshift Datashare Approach**:

- Results uploaded to S3 raw data bucket
- Requires manual permission setup

**Alternative S3 Unload Approach**:

- Redshift UNLOAD command writes directly to S3
- Bypasses Lambda query function
- May require ETL adjustments for format differences
- Suitable for high-volume data transfers

**Data Schema**:

- Vehicle identifier (AAID)
- Tire position (front_left, front_right, rear_left, rear_right)
- Tire pressure (PSI)
- Tire temperature (Fahrenheit)
- Event timestamp
- Odometer reading
- Vehicle metadata (make, model, year)

## Root ETL Pipeline

The Root ETL pipeline ingests, processes, and prepares telemetry data for both ML and filtering approaches.

### Step 1: Data Ingestion

**CloudWatch Events Rule**: `query-cron-job`

- Schedule: Hourly (e.g., 0 \* \* \* \*)
- Target: Lambda function `redshift-query-lambda`

**Lambda Function**: `redshift-query-lambda`

- Runtime: Python 3.11
- Memory: 512 MB
- Timeout: 5 minutes
- VPC: Enabled for Redshift access

**Query Logic**:

```
SELECT
  aaid,
  tpms_avmtireposition AS tire_position,
  tpms_avmtirepressure AS tire_pressure,
  tpms_avmtiretemperature AS tire_temperature,
  event_timestamp,
  odometer,
  vehicle_make,
  vehicle_model
FROM redshift_datashare.tire_telemetry
WHERE event_timestamp >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
  AND event_timestamp < CURRENT_TIMESTAMP
ORDER BY aaid, event_timestamp
```

**Output**:

- Destination: S3 bucket `mmt-predictive-maintenance-raw-{account-id}`
- Format: CSV with headers
- Partitioning: By date and hour (year/month/day/hour)
- Compression: Gzip

### Step 2: Data Transformation

**CloudWatch Events Rule**: `etl-cron-job`

- Schedule: Hourly, offset by 30 minutes (30 \* \* \* \*)
- Target: AWS Glue job `root-etl-pipeline`

**AWS Glue Job**: `root-etl-pipeline`

- Glue version: 4.0
- Worker type: G.1X (4 vCPU, 16 GB memory)
- Number of workers: 5
- Timeout: 30 minutes
- Job language: PySpark

**Transformation Steps**:

1. **Data Cleaning**
   - Remove rows with null tire pressure or temperature
   - Filter out erroneous values (pressure < 0 or > 100 PSI)
   - Handle missing timestamps

2. **Unit Conversions**
   - Convert temperature to Celsius if needed
   - Standardize pressure units to PSI
   - Normalize tire position labels

3. **Data Weaving**
   - Merge data from multiple tables based on AAID and timestamp
   - Join vehicle metadata (make, model, year)
   - Create unified telemetry records

4. **Output Formatting**
   - Convert to simplified CSV format
   - Add computed columns (e.g., pressure differential)
   - Partition by date and hour

**Output**:

- Destination: S3 bucket `mmt-predictive-maintenance-etl-{account-id}`
- Format: CSV with headers
- Partitioning: By date and hour
- Compression: Snappy
- Schema: Unified telemetry with 15+ columns

## Machine Learning Approach

The ML approach uses unsupervised anomaly detection with Amazon SageMaker’s Random Cut Forest algorithm.

### ML ETL Pipeline

**Step Function**: `ml-etl-pipeline`

- Schedule: Daily at 2 AM
- Timeout: 2 hours
- Error handling: Retry 3 times with exponential backoff

**Step 1: Determine Paths**

- Lambda function: `ml-etl-path-resolver`
- Logic: Calculate input path for previous day’s data, output path for processed data
- Output: Paths passed to Glue job

**Step 2: Feature Engineering**

- AWS Glue job: `ml-feature-engineering`
- Worker type: G.2X (8 vCPU, 32 GB memory)
- Number of workers: 10

**Processing Stages**:

1. **Add Metadata**
   - Vehicle make, model, year
   - Tire age and mileage
   - Service history flags
   - Alert metadata for downstream processing

2. **Resample Data**
   - Group by: AAID, tire position
   - Interval: 1 day (from hourly granularity)
   - Aggregations: Mean, median, mode, std dev, min, max
   - Reduces data volume by 24x

3. **Engineer Features**
   - Leak rate: Change in pressure over time
   - Temperature differential: Difference from ambient
   - Pressure variance: Std dev over rolling 7-day window
   - Speed correlation: Correlation between speed and pressure
   - Odometer delta: Miles driven per day

4. **Encode and Normalize**
   - Categorical encoding: One-hot encode tire position, vehicle make
   - Normalization: StandardScaler for continuous features
   - Feature scaling: All features scaled to [0, 1] range

**Output**:

- Destination: S3 bucket `mmt-predictive-maintenance-ml-features-{account-id}`
- Format: CSV with 25+ engineered features
- Partitioning: By date
- Ready for SageMaker training and inference

### ML Training Pipeline

**Step Function**: `ml-training-pipeline`

- Schedule: Weekly on Sunday at 2 AM
- Timeout: 3 hours

**Steps**:

1. **Generate Training Job ID**
   - Lambda: Create unique training job name with timestamp
   - Format: `tire-prediction-rcf-{timestamp}`

2. **Start SageMaker Training**
   - Algorithm: Random Cut Forest (built-in SageMaker algorithm)
   - Instance type: ml.m5.xlarge
   - Instance count: 1
   - Volume size: 30 GB
   - Max runtime: 2 hours
   - Spot instances: Enabled (70% cost savings)

**Hyperparameters**:

```
{
  "num_trees": 100,
  "num_samples_per_tree": 256,
  "feature_dim": 25,
  "eval_metrics": ["accuracy", "precision", "recall"]
}
```

**Training Data**:

- Input: S3 path to ML features (last 90 days)
- Content type: text/csv
- S3 data distribution: FullyReplicated
  1.  **Create SageMaker Model**

- Model name: `tire-prediction-model-{timestamp}`
- Model artifacts: From training job output
- Inference image: SageMaker RCF inference container
  1.  **Update SSM Parameter**

- Parameter: `/mmt/predictive-maintenance/latest-model`
- Value: Model name
- Type: String
- Used by inference pipeline to get latest model
  1.  **Send Notification**

- SNS topic: `ml-training-notifications`
- Message: Training completion status, model metrics
- Recipients: ML team, operations team

**Model Evaluation**:

- Unsupervised learning (no labeled failure data)
- Metrics: Anomaly score distribution, outlier percentage
- Validation: Compare predictions on holdout set with known failures

### ML Inference Pipeline

**Step Function**: `ml-inference-pipeline`

- Schedule: Daily at 6 AM
- Timeout: 2 hours

**Steps**:

1. **Determine Input Path and Model**
   - Lambda: `ml-inference-path-resolver`
   - Logic: Get previous day’s feature data path
   - Retrieve latest model name from SSM Parameter

2. **Start Batch Transform Job**
   - Job name: `tire-prediction-inference-{timestamp}`
   - Model: Retrieved from SSM Parameter
   - Instance type: ml.m5.large
   - Instance count: 2
   - Max payload: 6 MB
   - Batch strategy: MultiRecord

**Transform Configuration**:

- Input: S3 path to yesterday’s features
- Output: S3 bucket `mmt-predictive-maintenance-raw-predictions-{account-id}`
- Content type: text/csv
- Split type: Line
- Compression: None
  1.  **Monitor Transform Job**

- Lambda: `monitor-transform-job`
- Logic: Poll job status every 60 seconds
- Timeout: 2 hours
- Error handling: Fail Step Function if job fails
  1.  **Process Predictions**

- Lambda: `process-predictions`
- Runtime: Python 3.11
- Memory: 1024 MB
- Timeout: 10 minutes

**Processing Logic**:

```
def process_predictions(raw_predictions):
    # Add CSV headers back
    predictions_df = add_headers(raw_predictions)

    # Determine anomaly based on score threshold
    predictions_df['is_anomaly'] = predictions_df['anomaly_score'] > 0.75

    # Calculate time to reach 80 PSI (critical threshold)
    predictions_df['time_to_80_psi'] = calculate_time_to_threshold(
        current_pressure=predictions_df['tire_pressure'],
        leak_rate=predictions_df['leak_rate'],
        threshold=80
    )

    # Classify severity
    predictions_df['severity'] = classify_severity(
        anomaly_score=predictions_df['anomaly_score'],
        time_to_80_psi=predictions_df['time_to_80_psi']
    )

    return predictions_df
```

**Severity Classification**:

- Critical: time_to_80_psi < 3 days
- High: time_to_80_psi 3-7 days
- Medium: time_to_80_psi 7-14 days
- Low: time_to_80_psi > 14 days

**Output**:

- Destination: S3 bucket `mmt-predictive-maintenance-processed-predictions-{account-id}`
- Format: CSV with headers
- Columns: AAID, tire_position, anomaly_score, is_anomaly, time_to_80_psi, severity, leak_rate
- Triggers: S3 event notification to alerts Lambda

## Filtering Approach

The filtering approach uses a stepwise filter-based algorithm to identify gradual tire leaks without machine learning.

### Core Algorithm

**Purpose**: Detect slow tire leaks that might not be immediately apparent

**Process**:

1. Analyze historical tire pressure data over 7-14 day windows
2. Apply filtering algorithms to reduce noise from temperature variations
3. Calculate leak rates (PSI per day)
4. Classify leak severity based on rate and current pressure
5. Estimate time until tire reaches critical threshold (80 PSI)

### Data Processing Pipeline

**Step Function**: `filtering-pipeline`

- Schedule: Daily at 8 AM
- Timeout: 1 hour

**Lambda Function**: `filtering-algorithm`

- Runtime: Python 3.11
- Memory: 2048 MB
- Timeout: 15 minutes
- Concurrency: 10

**Algorithm Steps**:

1. **Load Historical Data**
   - Query last 14 days of ETL data from S3
   - Group by AAID and tire position
   - Sort by timestamp

2. **Apply Filters**
   - Moving average filter (7-day window) to smooth pressure readings
   - Temperature compensation to adjust for ambient temperature effects
   - Outlier removal using IQR method

3. **Calculate Leak Rate**
   - Linear regression on filtered pressure over time
   - Slope = leak rate (PSI per day)
   - R-squared > 0.7 indicates consistent leak pattern

4. **Detect Leaks**
   - Leak detected if: leak_rate < -0.5 PSI/day
   - Gradual leak: -0.5 to -2 PSI/day
   - Fast leak: < -2 PSI/day

5. **Estimate Time to Critical**
   - Current pressure - 80 PSI = pressure_delta
   - time_to_critical = pressure_delta / abs(leak_rate)
   - Adjust for confidence interval

### Filtering and Aggregation

**Deduplication**:

- Prevent duplicate alerts for same tire
- Check if alert already exists in last 7 days
- Update existing alert if leak rate worsens

**Aggregation**:

- Group alerts by vehicle (AAID)
- Prioritize by severity (critical > high > medium)
- Batch alerts for same vehicle into single notification

### Scheduling

**CloudWatch Events Rule**: `filtering-schedule`

- Schedule: Daily at 8 AM
- Target: Step Function `filtering-pipeline`
- Retry: 3 attempts on failure

## Alerts Approach

Both ML and filtering approaches generate alerts that integrate with maintenance scheduling systems.

### Alert Generation

**S3 Event Notification**:

- Bucket: `mmt-predictive-maintenance-processed-predictions-{account-id}`
- Event: s3:ObjectCreated:\*
- Target: Lambda function `generate-alerts`

**Lambda Function**: `generate-alerts`

- Runtime: Python 3.11
- Memory: 512 MB
- Timeout: 5 minutes

**Alert Logic**:

1. Read processed predictions from S3
2. Filter for high and critical severity only
3. Check for existing alerts (deduplication)
4. Format alert payload for relay garage system
5. Send to alerts API and SNS topic

### Alert Format

**Relay Garage System Format**:

```
{
  "alert_id": "uuid",
  "aaid": "vehicle-12345",
  "tire_position": "front_left",
  "alert_type": "tire_leak",
  "severity": "high",
  "leak_rate": -1.2,
  "current_pressure": 28.5,
  "time_to_80_psi": 9,
  "recommendation": "Schedule tire inspection within 7 days",
  "source": "ml_model",
  "confidence": 0.92,
  "timestamp": "2026-01-28T12:00:00Z"
}
```

### Alert Delivery

**Amazon SNS Topic**: `tire-alert-notifications`

**Subscriptions**:

- Email: Fleet managers, service coordinators
- SMS: On-call technicians for critical alerts
- HTTPS: Relay garage system webhook
- SQS: Queue for batch processing

**Amazon API Gateway**: `alerts-api`

- Endpoint: `POST /alerts`
- Authentication: API key
- Rate limiting: 100 requests/second
- Integration: Lambda function writes to DynamoDB

**Amazon DynamoDB Table**: `tire-alerts`

- Partition key: AAID
- Sort key: timestamp
- TTL: 90 days
- GSI: severity-timestamp-index for querying by severity

### Alert Status Tracking

**Status Values**:

- `new`: Alert generated, not yet acknowledged
- `acknowledged`: Fleet manager reviewed alert
- `scheduled`: Service appointment created
- `completed`: Tire serviced or replaced
- `false_positive`: Alert determined to be incorrect

**Update Mechanism**:

- API Gateway endpoint: `PUT /alerts/{alert_id}/status`
- Lambda function updates DynamoDB
- EventBridge rule triggers on status change
- Feedback loop for model improvement

## Deployment Architecture

**Infrastructure as Code**: AWS CDK (Python)

**CDK Stacks**:

1. **Data Stack** - S3 buckets, Glue databases
2. **ETL Stack** - Glue jobs, Lambda functions, CloudWatch Events
3. **ML Stack** - SageMaker training, batch transform, Step Functions
4. **Filtering Stack** - Lambda functions, Step Functions
5. **Alerts Stack** - SNS topics, API Gateway, DynamoDB
6. **Monitoring Stack** - CloudWatch dashboards, alarms

**Deployment Steps**:

1. Clone repository
2. Install dependencies: `npm install`
3. Bootstrap CDK: `cdk bootstrap`
4. Deploy stacks: `cdk deploy --all`
5. Manual step: Configure Redshift datashare permissions
6. Verify: Check CloudWatch Logs for successful ETL runs

**Deployment Time**: 30-45 minutes

**Cost Estimate**:

- S3 storage: $23/month (1 TB)
- Glue ETL: $44/month (hourly jobs)
- SageMaker training: $50/month (weekly)
- SageMaker inference: $100/month (daily batch transform)
- Lambda: $10/month
- DynamoDB: $5/month
- Total: ~$220-450/month depending on fleet size

**Cleanup**:

- `cdk destroy --all` removes all stacks
- S3 buckets must be emptied manually before deletion
- DynamoDB table deleted (backup recommended)
- CloudWatch Logs retained for 30 days
