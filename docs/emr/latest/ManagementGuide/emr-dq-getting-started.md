

# Getting started with Amazon EMR Data Quality
<a name="emr-dq-getting-started"></a>

This section walks you through running your first Amazon EMR Data Quality evaluation end to end: the permissions your Amazon EMR Spark application needs, and a walkthrough that submits a DQDL ruleset against a DataFrame on Amazon EMR and retrieves the result.
+ [Prerequisites](#emr-dq-prerequisites)
+ [Run your first evaluation](#emr-dq-walkthrough)

## Prerequisites
<a name="emr-dq-prerequisites"></a>

### IAM permissions
<a name="emr-dq-prerequisites-iam"></a>

The IAM role that your Amazon EMR Spark workload assumes — the EC2 instance profile attached to the cluster, or a per-step runtime role — must grant the following permissions to run Data Quality and publish results.


| Action | When required | 
| --- | --- | 
| glue:PublishDataQuality | To publish each evaluation to AWS Glue Data Quality so you can view history, compare runs, and feed anomaly detection. Publishing is on by default (enableDataQualityResultsPublishing is True), so grant this permission unless you explicitly opt out by setting the option to False. | 
| glue:AccessDataQualityRuntimeConfiguration | To fetch publishing configuration from the service when the library initializes publishing. Required whenever publishing is enabled; without it, the library silently disables publishing for the run. | 
| cloudwatch:PutMetricData | To emit per-run pass and fail metrics to Amazon CloudWatch for dashboards and alarms. Required only when you set enableDataQualityCloudWatchMetrics to True. | 
| glue:GetTable, glue:GetDatabase | To read catalog table metadata. Required when the input DataFrame is read from a AWS Glue Data Catalog table, or when the application passes publishToDataCatalogTarget so the service can attribute the run to a specific catalog table. | 
| glue:GetDataQualityRuleset | To fetch a saved ruleset from the AWS Glue Data Catalog. Required only when your Spark script loads a ruleset from the catalog instead of defining DQDL inline. See [Fetching a saved ruleset from the AWS Glue Data Catalog](#emr-dq-saved-rulesets). | 

The following inline policy grants the minimum set of permissions required to publish Data Quality results from an Amazon EMR Spark application.

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
<a name="emr-dq-walkthrough"></a>

1. **Create an Amazon EMR cluster or application.** Use release `emr-spark-8.1.0` or later on Amazon EMR on EC2, Amazon EMR on EKS, or Amazon EMR Serverless. Attach a role that has the permissions listed in [IAM permissions](#emr-dq-prerequisites-iam).

   For example, to create an Amazon EMR on EC2 cluster, run:

   ```
   aws emr create-cluster --release-label emr-spark-8.1.0 \
   --applications Name=Spark \
   --region us-east-1 \
   --name My_Spark_DataQuality_Cluster \
   --log-uri s3://{{amzn-s3-demo-bucket}}/ \
   --instance-type m5.xlarge \
   --instance-count 2 \
   --service-role EMR_DefaultRole_V2 \
   --ec2-attributes InstanceProfile=EMR_EC2_DefaultRole,SubnetId={{subnet-1234567890abcdef0}}
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

1. **Submit the application.** Submit the script the same way you submit any other Spark application for your Amazon EMR deployment mode.

------
#### [ Amazon EMR on EC2 ]

   ```
   aws emr add-steps --cluster-id {{j-1234567890ABC}} \
   --steps Type=Spark,Name="dq-example",ActionOnFailure=CONTINUE,Args=[s3://{{amzn-s3-demo-bucket}}/scripts/dq_example.py]
   ```

------
#### [ Amazon EMR on EKS ]

   ```
   aws emr-containers start-job-run \
   --virtual-cluster-id {{<virtual-cluster-id>}} \
   --name dq-example \
   --execution-role-arn {{<execution-role-arn>}} \
   --release-label emr-spark-8.1.0 \
   --job-driver '{
       "sparkSubmitJobDriver": {
           "entryPoint": "s3://{{amzn-s3-demo-bucket}}/scripts/dq_example.py"
       }
   }'
   ```

------
#### [ Amazon EMR Serverless ]

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

------

1. **Retrieve the result.** After the application finishes, list the run and fetch its detail with the AWS Glue Data Quality APIs or the AWS CLI. If your application also sets `publishToDataCatalogTarget` with a `DatabaseName` and `TableName`, the run appears on the *Data quality* tab of that catalog table in the AWS Glue console (see [Viewing results in the AWS Glue console](emr-dq-monitoring.md#emr-dq-studio-view)). Otherwise, use the API or AWS CLI to retrieve the run.

   ```
   aws glue list-data-quality-results-v2 --max-results 5
   
   aws glue get-data-quality-result-v2 --result-id {{<result-id>}}
   ```

   To narrow the list to runs of a specific dataset, pass the `EvaluationContext` that your application used (for example, `orders_daily`) to `ListDataQualityStatistics`. When your application reads from a AWS Glue Data Catalog table, you can additionally filter `list-data-quality-results-v2` by `DataSource.GlueTable`.

## Fetching a saved ruleset from the AWS Glue Data Catalog
<a name="emr-dq-saved-rulesets"></a>

Instead of defining your ruleset inline in each Spark script, you can author a ruleset once in the AWS Glue Data Catalog and fetch it from your Amazon EMR Spark application at runtime. This lets you version a ruleset in one place and share it across Amazon EMR Spark workloads, AWS Glue ETL jobs, and evaluations.

1. **Create the ruleset in AWS Glue.** Author and save the ruleset using one of the following paths:
   + In the AWS Glue console. See [Creating a new ruleset](https://docs.aws.amazon.com/glue/latest/dg/data-quality-getting-started.html#data-quality-create-ruleset) in the *AWS Glue Developer Guide*.
   + Through the AWS Glue Data Quality API. See [`CreateDataQualityRuleset`](https://docs.aws.amazon.com/glue/latest/webapi/API_CreateDataQualityRuleset.html) in the *AWS Glue API Reference*.

1. **Grant the Spark workload role access.** Add `glue:GetDataQualityRuleset` to the role that your Amazon EMR Spark application assumes.

1. **Fetch the ruleset in your Spark script.** Call `GetDataQualityRuleset` with boto3, extract the `Ruleset` field, and pass the DQDL string to `EvaluateDataQuality.apply`.

   ```
   import boto3
   from awsdataquality.transforms import EvaluateDataQuality
   
   glue = boto3.client("glue")
   response = glue.get_data_quality_ruleset(Name="{{orders_quality}}")
   ruleset = response["Ruleset"]
   
   results = EvaluateDataQuality.apply(
       frame=df,
       ruleset=ruleset,
       publishing_options={
           "dataQualityEvaluationContext": "orders_daily",
           "enableDataQualityResultsPublishing": True,
       },
   )
   ```