

# Monitoring and alerting
<a name="emr-dq-monitoring"></a>

## Amazon CloudWatch metrics
<a name="emr-dq-cw-metrics"></a>

Set `enableDataQualityCloudWatchMetrics` to `true` in the `EvaluateDataQuality` transform's `publishing_options` to emit per-run metrics to the `Glue Data Quality` namespace in Amazon CloudWatch. For Data Quality runs on Amazon EMR, metrics have a `Platform` dimension that indicates the Amazon EMR deployment mode that produced the run (for example, `emr-ec2`, `emr-eks`, or `emr-serverless`), together with an `EvaluationContext` dimension, so you can build alarms per dataset and per deployment mode.


| Metric | Description | 
| --- | --- | 
| glue.data.quality.rules.passed | Number of rules in the ruleset that passed on this run. | 
| glue.data.quality.rules.failed | Number of rules in the ruleset that failed on this run. | 

The same metric names are emitted by AWS Glue Data Quality, so alarms built against the `Glue Data Quality` namespace apply to both engines. For a walkthrough of building a CloudWatch alarm on these metrics, see [Setting up alerts, deployments, and scheduling](https://docs.aws.amazon.com/glue/latest/dg/data-quality-alerts.html) in the *AWS Glue Developer Guide*.

## Viewing results in the AWS Glue console
<a name="emr-dq-studio-view"></a>

When your application sets `publishToDataCatalogTarget` with a `DatabaseName` and `TableName`, each run is attributed to that AWS Glue Data Catalog table and is visible in the AWS Glue console:

1. Open the AWS Glue console and choose **Data Catalog**, then **Databases**.

1. Choose the database your application targeted, then choose the table.

1. Open the *Data quality* tab to see the run history for that table, including runs from Amazon EMR Data Quality and from AWS Glue ETL that share the same catalog target.

Without `publishToDataCatalogTarget`, results are not attributed to a catalog table and the AWS Glue console does not display them. Use the AWS Glue Data Quality APIs or the AWS CLI to retrieve those runs. See [Retrieving historical results](emr-dq-working-with-results.md#emr-dq-retrieve-results).

### Limitations
<a name="emr-dq-studio-view-limitations"></a>

The *Data quality* tab shows the overall data quality score and run metadata for each run. Per-rule outcomes and `FailureReason` values are not displayed in the console; retrieve them with `GetDataQualityResultV2` or `BatchGetDataQualityResultV2` (see [Retrieving historical results](emr-dq-working-with-results.md#emr-dq-retrieve-results)).