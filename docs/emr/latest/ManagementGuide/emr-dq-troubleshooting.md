

# Troubleshooting
<a name="emr-dq-troubleshooting"></a>
+ Anomaly detection requires at least three published data points for an `EvaluationContext` before it can score a run. Keep `enableDataQualityResultsPublishing` set to `true` from the first run onward.
+ **Rule results don't appear anywhere in AWS Glue Data Quality.** Confirm that `enableDataQualityResultsPublishing` is set to `true` in the transform options, and that the role that runs your Amazon EMR Spark application has `glue:AccessDataQualityRuntimeConfiguration`. Without the permission, the library silently disables publishing while evaluation continues in-process; the transform still returns a result DataFrame but nothing is persisted to AWS Glue Data Quality.
+ **Results don't appear under my AWS Glue Data Catalog table in the console.** To attribute an Amazon EMR run to a specific catalog table, pass the `publishToDataCatalogTarget` transform option with `DatabaseName` and `TableName` (and optionally `CatalogId`). This option only takes effect when publishing is already set up as described in the previous bullet. Without this option, runs are grouped only by `EvaluationContext`.
+ **Runs from Amazon EMR and AWS Glue are not linked in the console.** Both engines must use the same `EvaluationContext` value. See [Comparing runs across Amazon EMR and AWS Glue](emr-dq-working-with-results.md#emr-dq-compare-runs).

For general AWS Glue Data Quality concepts, DQDL semantics, and pricing, see [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html) in the *AWS Glue Developer Guide*.