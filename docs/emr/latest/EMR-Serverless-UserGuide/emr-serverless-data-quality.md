

# Amazon EMR Data Quality
<a name="emr-serverless-data-quality"></a>

Amazon EMR Data Quality, powered by [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html), lets you measure and monitor the quality of the data that your EMR Serverless Spark workloads read and write without leaving the Spark application. This page covers the EMR Serverless prerequisites and walkthrough. For concepts, APIs, monitoring, and troubleshooting, see [Amazon EMR Data Quality](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-quality.html) in the *Amazon EMR Management Guide*.

## Prerequisites
<a name="emr-serverless-dq-prerequisites"></a>

Amazon EMR Data Quality is installed by default in Amazon EMR releases emr-spark-8.1.0 and later. Only Apache Spark workloads are supported.

The IAM job runtime role that your EMR Serverless application assumes (passed via `--execution-role-arn` on `start-job-run`) must grant the following permissions to run Data Quality and publish results.


| Action | When required | 
| --- | --- | 
| glue:PublishDataQuality | To publish each evaluation to AWS Glue Data Quality so you can view history, compare runs, and feed anomaly detection. Publishing is on by default (enableDataQualityResultsPublishing is True), so grant this permission unless you explicitly opt out by setting the option to False. | 
| glue:AccessDataQualityRuntimeConfiguration | To fetch publishing configuration from the service when the library initializes publishing. Required whenever publishing is enabled; without it, the library silently disables publishing for the run. | 
| cloudwatch:PutMetricData | To emit per-run pass and fail metrics to Amazon CloudWatch for dashboards and alarms. Required only when you set enableDataQualityCloudWatchMetrics to True. | 
| glue:GetTable, glue:GetDatabase | To read catalog table metadata. Required when the input DataFrame is read from a AWS Glue Data Catalog table, or when the application passes publishToDataCatalogTarget so the service can attribute the run to a specific catalog table. | 
| glue:GetDataQualityRuleset | To fetch a saved ruleset from the AWS Glue Data Catalog. Required only when your Spark script loads a ruleset from the catalog instead of defining DQDL inline. See [Fetching a saved ruleset from the AWS Glue Data Catalog](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-getting-started.html#emr-dq-saved-rulesets). | 

The following inline policy grants the minimum set of permissions required to publish Data Quality results from an EMR Serverless Spark application.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "GlueDataQuality",
            "Effect": "Allow",
            "Action": [
                "glue:PublishDataQuality",
                "glue:AccessDataQualityRuntimeConfiguration"
            ],
            "Resource": "*"
        }
    ]
}
```

## Run your first evaluation
<a name="emr-serverless-dq-walkthrough"></a>

1. **Create an EMR Serverless application.** Use release `emr-spark-8.1.0` or later. Create a Spark application and attach a job role that has the permissions listed in [Prerequisites](#emr-serverless-dq-prerequisites).

   For example, to create a Spark application, run:

   ```
   aws emr-serverless create-application \
   --name My_Spark_DataQuality_Application \
   --release-label emr-spark-8.1.0 \
   --type SPARK
   ```

1. **Define a ruleset and evaluate it.** The following PySpark script defines a ruleset in DQDL, evaluates it against a DataFrame, and prints the per-rule outcome.

   ```
   from pyspark.sql import SparkSession
   from awsdataquality.transforms import EvaluateDataQuality
   
   spark = SparkSession.builder.appName("dq-example").getOrCreate()
   
   df = spark.read.parquet("s3://{{amzn-s3-demo-bucket}}/orders/")
   
   ruleset = """
   Rules = [
       RowCount > 1000,
       IsComplete "order_id",
       IsUnique "order_id",
       ColumnValues "status" in ["PLACED", "SHIPPED", "CANCELED"],
       Mean "order_total" between 10 and 500
   ]
   """
   
   results = EvaluateDataQuality.apply(
       frame=df,
       ruleset=ruleset,
       publishing_options={
           "dataQualityEvaluationContext": "orders_daily",
           "enableDataQualityResultsPublishing": True,
       },
   )
   
   results.show(truncate=False)
   ```

   The `results` DataFrame contains one row per rule with the following columns: `Rule`, `Outcome`, `FailureReason`, and `EvaluatedMetrics`. Rows with an `Outcome` of `Failed` include the observed value in `FailureReason`.

1. **Submit the job run.** Submit the script as a job run against your application.

   ```
   aws emr-serverless start-job-run \
   --application-id {{<application-id>}} \
   --execution-role-arn {{<execution-role-arn>}} \
   --name dq-example \
   --job-driver '{
       "sparkSubmit": {
           "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/dq_example.py"
       }
   }'
   ```

1. **Retrieve the result.** After the job run finishes, list the run and fetch its detail with the AWS Glue Data Quality APIs or the AWS CLI. If your application also sets `publishToDataCatalogTarget` with a `DatabaseName` and `TableName`, the run appears on the *Data quality* tab of that catalog table in the AWS Glue console.

   ```
   aws glue list-data-quality-results-v2 --max-results 5
   
   aws glue get-data-quality-result-v2 --result-id {{<result-id>}}
   ```

## Learn more about Amazon EMR Data Quality
<a name="emr-serverless-dq-learn-more"></a>

For the complete reference, see the following topics in the *Amazon EMR Management Guide*:
+ [Amazon EMR Data Quality overview, concepts, and limits](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-data-quality.html)
+ [Key capabilities (DQDL, analyzers, anomaly detection, dynamic rules)](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-key-capabilities.html)
+ [Fetching a saved ruleset from the AWS Glue Data Catalog](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-getting-started.html#emr-dq-saved-rulesets)
+ [Working with results](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-working-with-results.html)
+ [Monitoring and alerting with Amazon CloudWatch](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-monitoring.html)
+ [Troubleshooting](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-dq-troubleshooting.html)