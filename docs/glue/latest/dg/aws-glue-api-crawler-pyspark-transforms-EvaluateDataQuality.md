# EvaluateDataQuality class

Evaluates a data quality ruleset against a `DynamicFrame` and returns a new
`DynamicFrame` with results of the evaluation.

## Example

The following example code demonstrates how to evaluate data quality for a
`DynamicFrame` and then view the data quality results.

```
from awsglue.transforms import *
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsgluedq.transforms import EvaluateDataQuality

#Create Glue context
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# Define DynamicFrame
legislatorsAreas = glueContext.create_dynamic_frame.from_catalog(
    database="legislators", table_name="areas_json")

# Create data quality ruleset
ruleset = """Rules = [ColumnExists "id", IsComplete "id"]"""

# Evaluate data quality
dqResults = EvaluateDataQuality.apply(
    frame=legislatorsAreas,
    ruleset=ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "legislatorsAreas",
        "enableDataQualityCloudWatchMetrics": True,
        "enableDataQualityResultsPublishing": True,
        "resultsS3Prefix": "amzn-s3-demo-bucket1",
    },
)


# Inspect data quality results
dqResults.printSchema()
dqResults.toDF().show()
```

````
root
|-- Rule: string
|-- Outcome: string
|-- FailureReason: string
|-- EvaluatedMetrics: map
|    |-- keyType: string
|    |-- valueType: double +-----------------------+-------+-------------+---------------------------------------+
|Rule                   |Outcome|FailureReason|EvaluatedMetrics                       | +-----------------------+-------+-------------+---------------------------------------+
|ColumnExists "id"      |Passed |null         |{}                                     |
|IsComplete "id"        |Passed |null         |{Column.first_name.Completeness -> 1.0}| +-----------------------+-------+-------------+---------------------------------------+ ``` ## Methods <br>• [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-__call__ "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-apply "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-name "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeArgs "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeReturn "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeTransform "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeErrors "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describe "#aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality-describe") ## \_\_call\_\_(frame, ruleset, publishing\_options = {}) <br>• `frame` – The `DynamicFrame` that you want evaluate the data quality of. <br>• `ruleset` – A Data Quality Definition Language (DQDL) ruleset in string format. To learn more about DQDL, see the [Data Quality Definition Language (DQDL) reference](dqdl.md "dqdl.md") guide. <br>• `publishing_options` – A dictionary that specifies the following options for publishing evaluation results and metrics: + `dataQualityEvaluationContext` – A string that specifies the namespace under which AWS Glue should publish Amazon CloudWatch metrics and the data quality results. The aggregated metrics appear in CloudWatch, while the full results appear in the AWS Glue Studio interface. <br>• Required: No <br>• Default value: `default_context` + `enableDataQualityCloudWatchMetrics` – Specifies whether the results of the data quality evaluation should be published to CloudWatch. You specify a namespace for the metrics using the `dataQualityEvaluationContext` option. <br>• Required: No <br>• Default value: False + `enableDataQualityResultsPublishing` – Specifies whether the data quality results should be visible on the **Data Quality** tab in the AWS Glue Studio interface. <br>• Required: No <br>• Default value: True + `resultsS3Prefix` – Specifies the Amazon S3 location where AWS Glue can write the data quality evaluation results. <br>• Required: No <br>• Default value: "" (empty string) ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
````
