# SelectFromCollection class

Selects one `DynamicFrame` in a `DynamicFrameCollection`.

## Example

This example uses `SelectFromCollection` to select a `DynamicFrame`
from a `DynamicFrameCollection`.

**Example dataset**

The example selects two `DynamicFrames` from a
`DynamicFrameCollection` called `split_rows_collection`. The following
is the list of keys in `split_rows_collection`.

```
dict_keys(['high', 'low'])
```

**Example code**

```
# Example: Use SelectFromCollection to select
# DynamicFrames from a DynamicFrameCollection

from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import SelectFromCollection

# Create GlueContext
sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)

# Select frames and inspect entries
frame_low = SelectFromCollection.apply(dfc=split_rows_collection, key="low")
frame_low.toDF().show()

frame_high = SelectFromCollection.apply(dfc=split_rows_collection, key="high")
frame_high.toDF().show()

```

````
+---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
|  1|    0|                     fax|             202-225-3307|
|  1|    1|                   phone|             202-225-5731|
|  2|    0|                     fax|             202-225-3307|
|  2|    1|                   phone|             202-225-5731|
|  3|    0|                     fax|             202-225-3307|
|  3|    1|                   phone|             202-225-5731|
|  4|    0|                     fax|             202-225-3307|
|  4|    1|                   phone|             202-225-5731|
|  5|    0|                     fax|             202-225-3307|
|  5|    1|                   phone|             202-225-5731|
|  6|    0|                     fax|             202-225-3307|
|  6|    1|                   phone|             202-225-5731|
|  7|    0|                     fax|             202-225-3307|
|  7|    1|                   phone|             202-225-5731|
|  8|    0|                     fax|             202-225-3307|
|  8|    1|                   phone|             202-225-5731|
|  9|    0|                     fax|             202-225-3307|
|  9|    1|                   phone|             202-225-5731|
| 10|    0|                     fax|             202-225-6328|
| 10|    1|                   phone|             202-225-4576| +---+-----+------------------------+-------------------------+ only showing top 20 rows +---+-----+------------------------+-------------------------+
| id|index|contact_details.val.type|contact_details.val.value| +---+-----+------------------------+-------------------------+
| 11|    0|                     fax|             202-225-6328|
| 11|    1|                   phone|             202-225-4576|
| 11|    2|                 twitter|           RepTrentFranks|
| 12|    0|                     fax|             202-225-6328|
| 12|    1|                   phone|             202-225-4576|
| 12|    2|                 twitter|           RepTrentFranks|
| 13|    0|                     fax|             202-225-6328|
| 13|    1|                   phone|             202-225-4576|
| 13|    2|                 twitter|           RepTrentFranks|
| 14|    0|                     fax|             202-225-6328|
| 14|    1|                   phone|             202-225-4576|
| 14|    2|                 twitter|           RepTrentFranks|
| 15|    0|                     fax|             202-225-6328|
| 15|    1|                   phone|             202-225-4576|
| 15|    2|                 twitter|           RepTrentFranks|
| 16|    0|                     fax|             202-225-6328|
| 16|    1|                   phone|             202-225-4576|
| 16|    2|                 twitter|           RepTrentFranks|
| 17|    0|                     fax|             202-225-6328|
| 17|    1|                   phone|             202-225-4576| +---+-----+------------------------+-------------------------+ only showing top 20 rows ``` ## Methods <br>• [\_\_call\_\_](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-__call__ "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-apply "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-name "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeArgs "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeReturn "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeTransform "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeErrors "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describe "#aws-glue-api-crawler-pyspark-transforms-SelectFromCollection-describe") ## \_\_call\_\_(dfc, key, transformation\_ctx = "") Gets one `DynamicFrame` from a `DynamicFrameCollection`. <br>• `dfc` – The `DynamicFrameCollection` that the `DynamicFrame` should be selected from (required). <br>• `key` – The key of the `DynamicFrame` to select (required). <br>• `transformation_ctx` – A unique string that is used to identify state information (optional). ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
````
