# IntToIp class

The `IntToIp` transform converts the integer value of source column or other value to the corresponding
IPv4 value in then target column, and returns the result in a new column.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [
        (3221225473,),
        (0,),
        (1,),
        (100,),
        (168430090,),
        (4294967295,),
        (4294967294,),
        (4294967296,),
        (-1,),
        (None,),
    ],
    ["source_column_int"],
)

try:
    df_output = web_functions.IntToIp.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column_int",
        target_column="target_column",
        value=None
    )
    df_output.show()
except:
    print("Unexpected Error happened ")
    raise

```

## Output

The output will be:

```

```

+---------------+---------------+
|source_column_int|target_column| +---------------+---------------+
| 3221225473| 192.0.0.1 |
| 0| 0.0.0.0 |
| 1| 0.0.0.1 |
| 100| 0.0.0.100|
| 168430090 | 10.0.0.10 |
| 4294967295| 255.255.255.255|
| 4294967294| 255.255.255.254|
| 4294967296| null |
| -1| null |
| null| null | +---------------+---------------+ ` ` The `IntToIp.apply` transformation takes the `source\_column` as `"source\_column\_int"` and the `target\_column` as `"target\_column"` and converts the integer values in the `source\_column\_int` column to their corresponding IPv4 address representation and stores the result in the `target\_column` column. For valid integer values within the range of IPv4 addresses (0 to 4294967295), the transformation successfully converts them to their IPv4 address representation (e.g., 192.0.0.1, 0.0.0.0, 10.0.0.10, 255.255.255.255). For integer values outside the valid range (e.g., 4294967296, -1), the `target\_column` value is set to `null`. For `null` values in the `source\_column\_int` column, the `target\_column` value is also set to `null`. ## Methods <br>• [\_\_call\_\_](#aws-glue-api-pyspark-transforms-IntToIp-__call__ "#aws-glue-api-pyspark-transforms-IntToIp-__call__") <br>• [apply](#aws-glue-api-crawler-pyspark-transforms-IntToIp-apply "#aws-glue-api-crawler-pyspark-transforms-IntToIp-apply") <br>• [name](#aws-glue-api-crawler-pyspark-transforms-IntToIp-name "#aws-glue-api-crawler-pyspark-transforms-IntToIp-name") <br>• [describeArgs](#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeArgs "#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeArgs") <br>• [describeReturn](#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeReturn "#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeReturn") <br>• [describeTransform](#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeTransform "#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeTransform") <br>• [describeErrors](#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeErrors "#aws-glue-api-crawler-pyspark-transforms-IntToIp-describeErrors") <br>• [describe](#aws-glue-api-crawler-pyspark-transforms-IntToIp-describe "#aws-glue-api-crawler-pyspark-transforms-IntToIp-describe") ## \_\_call\_\_(spark_context, data_frame, target_column, source_column=None, value=None) The `IntToIp` transform converts the integer value of source column or other value to the corresponding IPv4 value in then target column, and returns the result in a new column. <br>• `sourceColumn` – The name of an existing column. <br>• `value` – A character string to evaluate. <br>• `targetColumn` – The name of the new column to be created. ## apply(cls, \*args, \*\*kwargs) Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply"). ## name(cls) Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name"). ## describeArgs(cls) Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs"). ## describeReturn(cls) Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn"). ## describeTransform(cls) Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform"). ## describeErrors(cls) Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors"). ## describe(cls) Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
