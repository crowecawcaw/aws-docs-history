# RemoveDuplicates class

The `RemoveDuplicates` transform deletes an entire row, if a duplicate value is encountered in a
selected source column.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [
        (105.111, 13.12),
        (13.12, 13.12),
        (None, 13.12),
        (13.12, 13.12),
        (None, 13.12),
    ],
    ["source_column_1", "source_column_2"],
)

try:
    df_output = data_quality.RemoveDuplicates.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column_1"
    )
except:
    print("Unexpected Error happened ")
    raise

```

## Output

The output will be a PySpark DataFrame with duplicates removed based on the
`source_column_1` column. The resulting `df\_output` DataFrame will contain the following rows:

```

```

+---------------+---------------+
|source_column_1|source_column_2| +---------------+---------------+
| 105.111| 13.12|
| 13.12| 13.12|
| null| 13.12| +---------------+---------------+ ` ` Note that the rows with `source_column_1` values of `13.12` and `null` appear only once in the output DataFrame, as the duplicates have been removed based on the `source_column_1` column. ## Methods <br>• [\_\_call\_\_](#aws-glue-api-pyspark-transforms-RemoveDuplicates-__call__ "#aws-glue-api-pyspark-transforms-RemoveDuplicates-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-apply "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-name "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeArgs "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeReturn "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeTransform "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeErrors "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describe "#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describe") ## \_\_call\_\_(spark_context, data_frame, source_column) The `RemoveDuplicates` transform deletes an entire row, if a duplicate value is encountered in a selected source column. <br>• `source_column` – The name of an existing column. ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
