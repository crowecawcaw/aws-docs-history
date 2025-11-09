# EvaluateDataQuality class

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| AWS Glue Data Quality is in preview release for AWS Glue and is subject to change. |

**Package: com.amazonaws.services.glue.dq**

```
object EvaluateDataQuality
```

## Def apply

```
def apply(frame: DynamicFrame,
            ruleset: String,
            publishingOptions: JsonOptions = JsonOptions.empty): DynamicFrame
```

Evaluates a data quality ruleset against a `DynamicFrame`, and returns a new
`DynamicFrame` with results of the evaluation. To learn more about AWS Glue Data Quality, see
[AWS Glue Data Quality](glue-data-quality.md "glue-data-quality.md").

- `frame` – The `DynamicFrame` that you want to evaluate the
  data quality of.
- `ruleset` – A Data Quality Definition Language (DQDL) ruleset in
  string format. To learn more about DQDL, see the [Data Quality Definition Language (DQDL) reference](dqdl.md "dqdl.md") guide.
- `publishingOptions` – A dictionary that specifies the following
  options for publishing evaluation results and metrics:
  - `dataQualityEvaluationContext` – A string that specifies the
    namespace under which AWS Glue should publish Amazon CloudWatch metrics and the
    data quality results. The aggregated metrics appear in CloudWatch, while the full results
    appear in the AWS Glue Studio interface.
    - Required: No
    - Default value: `default_context`

  - `enableDataQualityCloudWatchMetrics` – Specifies whether the
    results of the data quality evaluation should be published to CloudWatch. You specify a
    namespace for the metrics using the `dataQualityEvaluationContext`
    option.
    - Required: No
    - Default value: False

  - `enableDataQualityResultsPublishing` – Specifies whether the data
    quality results should be visible on the **Data Quality** tab in the
    AWS Glue Studio interface.
    - Required: No
    - Default value: True

  - `resultsS3Prefix` – Specifies the Amazon S3 location
    where AWS Glue can write the data quality evaluation results.
    - Required: No
    - Default value: "" (empty string)

## Example

The following example code demonstrates how to evaluate data quality for a
`DynamicFrame` before performing a `SelectFields` transform. The
script verifies that all data quality rules pass before it attempts the transform.

```
import com.amazonaws.services.glue.GlueContext
import com.amazonaws.services.glue.MappingSpec
import com.amazonaws.services.glue.errors.CallSite
import com.amazonaws.services.glue.util.GlueArgParser
import com.amazonaws.services.glue.util.Job
import com.amazonaws.services.glue.util.JsonOptions
import org.apache.spark.SparkContext
import scala.collection.JavaConverters._
import com.amazonaws.services.glue.dq.EvaluateDataQuality

object GlueApp {
  def main(sysArgs: Array[String]) {
    val spark: SparkContext = new SparkContext()
    val glueContext: GlueContext = new GlueContext(spark)
    // @params: [JOB_NAME]
    val args = GlueArgParser.getResolvedOptions(sysArgs, Seq("JOB_NAME").toArray)
    Job.init(args("JOB_NAME"), glueContext, args.asJava)

    // Create DynamicFrame with data
    val Legislators_Area = glueContext.getCatalogSource(database="legislators", tableName="areas_json", transformationContext="S3bucket_node1").getDynamicFrame()

    // Define data quality ruleset
    val DQ_Ruleset = """
      Rules = [ColumnExists "id"]
    """

    // Evaluate data quality
    val DQ_Results = EvaluateDataQuality.apply(frame=Legislators_Area, ruleset=DQ_Ruleset, publishingOptions=JsonOptions("""{"dataQualityEvaluationContext": "Legislators_Area", "enableDataQualityMetrics": "true", "enableDataQualityResultsPublishing": "true"}"""))
    assert(DQ_Results.filter(_.getField("Outcome").contains("Failed")).count == 0, "Failing DQ rules for Legislators_Area caused the job to fail.")

    // Script generated for node Select Fields
    val SelectFields_Results = Legislators_Area.selectFields(paths=Seq("id", "name"), transformationContext="Legislators_Area")

    Job.commit()
  }
}
```
