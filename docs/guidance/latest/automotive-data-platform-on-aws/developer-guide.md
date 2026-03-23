# Developer guide

This chapter provides guidance for developers who want to customize and extend the Automotive Data Platform.

## Repository Structure

```
automotive-data-platform-on-aws/
├── guidance-for-agentic-customer-360/
│   ├── deployment/
│   │   ├── cdk/                    # CDK infrastructure code
│   │   ├── scripts/                # Python deployment scripts
│   │   ├── lambda/                 # Lambda function code
│   │   └── athena-queries/         # SQL view definitions
│   ├── source/
│   │   ├── data-generation/        # Synthetic data generators
│   │   └── quick-suite/            # Dashboard definitions
│   ├── Makefile                    # Deployment automation
│   └── README.md
├── guidance-for-predictive-maintenance/
│   ├── deployment/
│   │   ├── lib/                    # CDK stack definitions
│   │   ├── lambda/                 # Lambda functions
│   │   └── glue/                   # Glue job scripts
│   ├── source/
│   │   └── ml/                     # ML training code
│   └── README.md
├── platform-foundation/
│   └── cdk/                        # SageMaker Unified Studio CDK
└── datasource/
    └── cx-analytics/               # Shared data generators
```

## Customizing Customer 360

### Adding New Data Sources

**Step 1: Create Glue table definition**

Edit `deployment/cdk/lib/glue-catalog-stack.ts`:

```
new glue.CfnTable(this, 'NewDataTable', {
  databaseName: 'cx_analytics',
  catalogId: this.account,
  tableInput: {
    name: 'new_data_source',
    storageDescriptor: {
      location: `s3://${dataBucket.bucketName}/processed/new_data_source/`,
      inputFormat: 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat',
      outputFormat: 'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat',
      serdeInfo: {
        serializationLibrary: 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe',
      },
      columns: [
        { name: 'id', type: 'string' },
        { name: 'value', type: 'double' },
        { name: 'timestamp', type: 'timestamp' },
      ],
    },
  },
});
```

**Step 2: Create ETL job to ingest data**

Create `deployment/glue/ingest-new-data.py`:

```
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME', 'SOURCE_PATH', 'TARGET_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Read source data
df = spark.read.format('csv').option('header', 'true').load(args['SOURCE_PATH'])

# Transform data
df_transformed = df.select('id', 'value', 'timestamp')

# Write to S3 in Parquet format
df_transformed.write.mode('overwrite').parquet(args['TARGET_PATH'])

job.commit()
```

**Step 3: Create Athena view**

Create `deployment/athena-queries/create_new_data_view.sql`:

```
CREATE OR REPLACE VIEW cx_analytics.new_data_summary AS
SELECT
  DATE_TRUNC('day', timestamp) AS date,
  COUNT(*) AS record_count,
  AVG(value) AS avg_value,
  MAX(value) AS max_value
FROM cx_analytics.new_data_source
GROUP BY DATE_TRUNC('day', timestamp)
ORDER BY date DESC;
```

### Creating Custom Dashboards

**Step 1: Create Quick Suite dataset**

```
import boto3

quicksight = boto3.client('quicksight')

response = quicksight.create_data_set(
    AwsAccountId='123456789012',
    DataSetId='new-data-summary',
    Name='New Data Summary',
    PhysicalTableMap={
        'athena-table': {
            'RelationalTable': {
                'DataSourceArn': 'arn:aws:quicksight:us-east-1:123456789012:datasource/cx-analytics-athena',
                'Schema': 'cx_analytics',
                'Name': 'new_data_summary',
                'InputColumns': [
                    {'Name': 'date', 'Type': 'DATETIME'},
                    {'Name': 'record_count', 'Type': 'INTEGER'},
                    {'Name': 'avg_value', 'Type': 'DECIMAL'},
                ]
            }
        }
    },
    ImportMode='DIRECT_QUERY'
)
```

**Step 2: Add visual to dashboard**

Use Quick Suite console to add visuals, or export/import dashboard JSON with new visual definitions.

### Extending Bedrock Agent

**Add new action group**:

Create `deployment/lambda/bedrock-agent-new-action/index.py`:

```
import json
import boto3

def lambda_handler(event, context):
    action = event['actionGroup']
    function = event['function']
    parameters = event.get('parameters', [])

    if function == 'analyze_new_metric':
        # Implement custom logic
        result = analyze_metric(parameters)

        return {
            'response': {
                'actionGroup': action,
                'function': function,
                'functionResponse': {
                    'responseBody': {
                        'TEXT': {
                            'body': json.dumps(result)
                        }
                    }
                }
            }
        }
```

**Register action group with agent**:

```
aws bedrock-agent create-agent-action-group \
  --agent-id AGENT_ID \
  --agent-version DRAFT \
  --action-group-name analyze-new-metric \
  --action-group-executor lambda=arn:aws:lambda:REGION:ACCOUNT:function:bedrock-agent-new-action \
  --function-schema file://action-schema.json
```

## Customizing Predictive Maintenance

### Training Custom ML Models

**Step 1: Create custom training script**

Create `source/ml/custom_model.py`:

```
import pandas as pd
import sagemaker
from sagemaker.sklearn import SKLearn

# Load training data
df = pd.read_csv('s3://bucket/features/train.csv')

# Define custom model
estimator = SKLearn(
    entry_point='train.py',
    role='arn:aws:iam::ACCOUNT:role/SageMakerRole',
    instance_type='ml.m5.xlarge',
    framework_version='1.0-1',
    hyperparameters={
        'n_estimators': 100,
        'max_depth': 10
    }
)

# Train model
estimator.fit({'train': 's3://bucket/features/'})
```

**Step 2: Update Step Function to use custom model**

Edit training pipeline Step Function definition to reference custom training script.

### Adding New Telemetry Signals

**Step 1: Update Redshift query**

Edit `deployment/lambda/redshift-query-lambda/index.py`:

```
query = """
SELECT
  aaid,
  tire_pressure,
  tire_temperature,
  new_signal_1,  -- Add new signal
  new_signal_2,  -- Add new signal
  event_timestamp
FROM tire_telemetry
WHERE event_timestamp >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
"""
```

**Step 2: Update feature engineering**

Edit `deployment/glue/ml-feature-engineering.py` to include new signals in feature calculations.

**Step 3: Retrain model with new features**

Trigger training pipeline to retrain model with expanded feature set.

### Custom Alert Logic

Edit `deployment/lambda/generate-alerts/index.py`:

```
def classify_severity(anomaly_score, time_to_80_psi, new_factor):
    # Custom severity logic
    if new_factor > threshold:
        return 'critical'
    elif time_to_80_psi < 3:
        return 'high'
    elif time_to_80_psi < 7:
        return 'medium'
    else:
        return 'low'
```

## Data Mesh Best Practices

### Domain Ownership

- Assign clear ownership for each data product
- Document data product SLAs and quality metrics
- Implement automated data quality checks
- Provide self-service access through DataZone

### Data Product Design

- Treat data as a product with consumers in mind
- Provide comprehensive documentation
- Version data schemas with backward compatibility
- Implement monitoring and alerting

### Cross-Domain Data Sharing

- Use Lake Formation for fine-grained access control
- Implement data contracts between domains
- Track data lineage with DataZone
- Audit all cross-domain access

## Security Best Practices

- Use least privilege IAM policies
- Enable encryption at rest and in transit
- Rotate credentials regularly with Secrets Manager
- Implement network isolation with VPC
- Enable CloudTrail logging for all API calls
- Use Bedrock Guardrails to filter PII
- Implement row-level security with Lake Formation
- Audit permissions quarterly

## Performance Optimization

### Athena Query Optimization

- Use partition pruning: `WHERE year='2026' AND month='01'`
- Select only needed columns: `SELECT id, name` not `SELECT *`
- Use columnar formats: Parquet with Snappy compression
- Enable result caching for repeated queries
- Use CTAS for complex transformations

### Glue Job Optimization

- Use appropriate worker types (G.1X, G.2X)
- Enable job bookmarks for incremental processing
- Partition output data by date
- Use pushdown predicates to filter early
- Monitor DPU usage and adjust allocation

### SageMaker Optimization

- Use Spot instances for training (70% savings)
- Enable auto-scaling for inference endpoints
- Use batch transform for bulk predictions
- Monitor endpoint utilization
- Use multi-model endpoints for multiple models

## CI/CD Integration

### GitHub Actions Example

```
name: Deploy Customer 360
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: '18'
      - name: Install dependencies
        run: |
          cd guidance-for-agentic-customer-360/deployment/cdk
          npm install
      - name: Deploy
        run: |
          cd guidance-for-agentic-customer-360
          make deploy
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          AWS_REGION: us-east-1
```

### Testing

- Unit tests for Lambda functions
- Integration tests for ETL pipelines
- End-to-end tests for complete workflows
- Load tests for API endpoints
- Data quality tests for outputs

## Additional Resources

- AWS CDK Documentation: https://docs.aws.amazon.com/cdk/
- AWS Glue Documentation: https://docs.aws.amazon.com/glue/
- Amazon Bedrock Documentation: https://docs.aws.amazon.com/bedrock/
- Amazon SageMaker Documentation: https://docs.aws.amazon.com/sagemaker/
- AWS Lake Formation Documentation: https://docs.aws.amazon.com/lake-formation/
