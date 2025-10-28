# FlagDuplicateRows class

The `FlagDuplicateRows` transform returns a new column with a specified value in each row
that indicates whether that row is an exact match of an earlier row in the dataset. When matches are found,
they are flagged as duplicates. The initial occurrence is not flagged, because it doesn't match an earlier row.

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
    df_output = data_quality.FlagDuplicateRows.apply(
        data_frame=input_df,
        spark_context=sc,
        target_column="flag_row",
        true_string="True",
        false_string="False",
        target_index=1
    )
except:
    print("Unexpected Error happened ")
    raise

```

## Output

The output will be a PySpark DataFrame with an additional column `flag_row`
that indicates whether a row is a duplicate or not, based on the `source_column_1` column.
The resulting `df\_output` DataFrame will contain the following rows:

```

```

+---------------+---------------+--------+
|source_column_1|source_column_2|flag_row| +---------------+---------------+--------+
| 105.111| 13.12| False|
| 13.12| 13.12| True|
| null| 13.12| True|
| 13.12| 13.12| True|
| null| 13.12| True| +---------------+---------------+--------+ ` ` The `flag_row` column indicates whether a row is a duplicate or not. The `true\_string` is set to "True", and the `false\_string` is set to "False". The `target\_index` is set to 1, which means that the `flag_row` column will be inserted at the second position (index 1) in the output DataFrame. ## Methods <br>• [\_\_call\_\_](#aws-glue-api-pyspark-transforms-FlagDuplicateRows-__call__ "#aws-glue-api-pyspark-transforms-FlagDuplicateRows-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-apply "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-name "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeArgs "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeReturn "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeTransform "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeErrors "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describe "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicateRows-describe") ## \_\_call\_\_(spark_context, data_frame, target_column, true_string=DEFAULT_TRUE_STRING, false_string=DEFAULT_FALSE_STRING, target_index=None) The `FlagDuplicateRows` transform returns a new column with a specified value in each row that indicates whether that row is an exact match of an earlier row in the dataset. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged, because it doesn't match an earlier row. <br>• `true_string` – Value to be inserted if the row matches an earlier row. <br>• `false_string` – Value to be inserted if the row is unique. <br>• `target_column` – Name of the new column that is inserted in the dataset. ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
