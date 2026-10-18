

# Working with results
<a name="emr-dq-working-with-results"></a>

This section covers how to read Amazon EMR Data Quality results after a run completes: retrieving history through the AWS Glue Data Quality APIs, interpreting the result DataFrame, comparing runs across engines, and configuring where results are stored. Every result also carries a `Dimensions` map with the originating `Platform` (for example, `emr-ec2`, `emr-eks`, `emr-serverless`, or `glue-etl`), which you can use to filter runs by engine when retrieving history.
+ [Retrieving historical results](#emr-dq-retrieve-results)
+ [Result DataFrame schema](#emr-dq-result-schema)
+ [Comparing runs across Amazon EMR and AWS Glue](#emr-dq-compare-runs)
+ [Where results are stored](#emr-dq-result-destinations)

## Retrieving historical results
<a name="emr-dq-retrieve-results"></a>

Results from Amazon EMR runs are readable through the same AWS Glue Data Quality APIs used for AWS Glue runs. Each API has a corresponding AWS CLI command, which is the primary way to inspect runs that are not attributed to a catalog table (see [Viewing results in the AWS Glue console](emr-dq-monitoring.md#emr-dq-studio-view)).


| API | Purpose | AWS CLI command | IAM action | 
| --- | --- | --- | --- | 
| ListDataQualityResultsV2 | Enumerate result IDs, optionally filtered by dataset, ruleset, or time range. | aws glue list-data-quality-results-v2 | glue:ListDataQualityResults | 
| GetDataQualityResultV2 | Retrieve the full result for one run, including per-rule outcome and observed values. | aws glue get-data-quality-result-v2 | glue:GetDataQualityResult | 
| BatchGetDataQualityResultV2 | Retrieve up to 100 results in a single call. | aws glue batch-get-data-quality-result-v2 | glue:BatchGetDataQualityResult | 
| ListDataQualityStatistics | Retrieve the time series of a specific statistic (for example, RowCount) for a given EvaluationContext. | aws glue list-data-quality-statistics | glue:ListDataQualityStatistics | 

Grant these actions to whichever identity reads results after a run completes (your developer identity, a downstream AWS Lambda function, or a reporting pipeline). The Spark workload role does not need these actions — it only publishes results.

Each result returned by these APIs includes a `Dimensions` map that identifies the Amazon EMR run. All results have `Platform` (`emr-ec2`, `emr-eks`, or `emr-serverless`), `RunId`, and `ClusterId`. Amazon EMR on EKS also populates `EksClusterName` when the EKS cluster name is set on the virtual cluster, and Amazon EMR Serverless also populates `ApplicationName` when the application has a name. Pass `Dimensions` to `ListDataQualityResultsV2` to filter history, for example `{"Platform": "emr-ec2"}`.

## Result DataFrame schema
<a name="emr-dq-result-schema"></a>

The DataFrame returned by `EvaluateDataQuality.apply` has one row per rule. The columns are:


| Column | Type | Description | 
| --- | --- | --- | 
| Rule | string | The DQDL source of the rule, exactly as written in the ruleset. | 
| Outcome | string | One of Passed, Failed, or Error. Failed means the rule was evaluated and did not pass; Error means the rule could not be evaluated (for example, because a referenced column was missing). | 
| FailureReason | string | Populated for Failed and Error outcomes. Includes the observed value and the reason the rule did not pass. | 
| EvaluatedMetrics | map<string, double> | The statistics the rule computed, keyed by analyzer name (for example, Dataset.\*.RowCount). | 

To gate a downstream write on the result of a Data Quality evaluation, require every row to have `Outcome = 'Passed'`, or equivalently filter out any row whose `Outcome` is in `('Failed', 'Error')`. See [Where to validate in your pipeline](emr-data-quality.md#emr-dq-validation-stages) for a working example.

## Comparing runs across Amazon EMR and AWS Glue
<a name="emr-dq-compare-runs"></a>

Runs that share an `EvaluationContext` are linked into a single logical dataset regardless of which engine produced them. That means a ruleset that runs on AWS Glue ETL for a nightly batch and on Amazon EMR for an intra-day incremental run feed the same anomaly-detection model and appear together in `ListDataQualityResultsV2` filters. When both runs also set `publishToDataCatalogTarget` against the same catalog table, the shared history is visible on the *Data quality* tab of that table in the AWS Glue console.

Choose `EvaluationContext` values that identify the *dataset* being validated, not the engine that runs the validation. Good examples: `orders_daily`, `clickstream_hourly`, `customers_snapshot`. Avoid engine or job-name suffixes such as `orders_daily_emr`.

## Where results are stored
<a name="emr-dq-result-destinations"></a>

Each Data Quality evaluation can land in up to three destinations, controlled by options you pass to the transform.

AWS Glue Data Quality service (default)  
With `enableDataQualityResultsPublishing` set to `true` (the default), each run is published to the AWS Glue Data Quality service and is readable through the V2 APIs listed in [Retrieving historical results](#emr-dq-retrieve-results), the AWS CLI, and the AWS Glue console.

AWS Glue Data Catalog table attribution  
When your application passes `publishToDataCatalogTarget` with `DatabaseName`, `TableName`, and optionally `CatalogId`, the service attributes the run to that catalog table and the result appears in the *Data quality* tab of that table in the AWS Glue console. This option only attributes the result to the table; Amazon EMR Data Quality does not write the result to the catalog table itself. Catalog attribution requires `enableDataQualityResultsPublishing` to be `true` (the default).

Amazon S3 (JSON output)  
Set `resultsS3Prefix` in `publishing_options` to also write the result DataFrame to a prefix in your own Amazon S3 bucket. The library writes partitioned JSON (by year, month, and day) so you can inspect the raw rule outcomes outside of the AWS Glue Data Quality APIs. The role that runs your Amazon EMR Spark application needs `s3:PutObject` on the target prefix.

The Amazon S3 destination is independent of the other two. Catalog attribution requires publishing to the AWS Glue Data Quality service to be enabled, which it is by default.