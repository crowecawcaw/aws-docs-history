

# FillWithMode class
<a name="aws-glue-api-pyspark-transforms-FillWithMode"></a>

 The `FillWithMode` transform formats a column according to the phone numberformat you specify. You can also specify tie-breaker logic, where some of the values are identical. For example, consider the following values: `1 2 2 3 3 4` 

 A modeType of `MINIMUM` causes `FillWithMode` to return 2 as the mode value. If modeType is `MAXIMUM`, the mode is 3. For `AVERAGE`, the mode is 2.5. 

## Example
<a name="pyspark-FillWithMode-examples"></a>

```
from awsglue.context import *
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [
        (105.111, 13.12),
        (1055.123, 13.12),
        (None, 13.12),
        (13.12, 13.12),
        (None, 13.12),
    ],
    ["source_column_1", "source_column_2"],
)

try:
    df_output = data_quality.FillWithMode.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column_1",
        mode_type="MAXIMUM"
    )
    df_output.show()    
except:
    print("Unexpected Error happened ")
    raise
```

## Output
<a name="pyspark-FillWithMode-output"></a>

 The output of the given code will be: 

```
```
+---------------+---------------+
|source_column_1|source_column_2|
+---------------+---------------+
| 105.111| 13.12|
| 1055.123| 13.12|
| 1055.123| 13.12|
| 13.12| 13.12|
| 1055.123| 13.12|
+---------------+---------------+
```
```

 The `FillWithMode` transformation from the `awsglue.data\_quality` module is applied to the `input\_df` DataFrame. It replaces the `null` values in the `source_column_1` column with the maximum value (`mode\_type="MAXIMUM"`) from the non-null values in that column. 

 In this case, the maximum value in the `source_column_1` column is `1055.123`. Therefore, the `null` values in `source_column_1` are replaced by `1055.123` in the output DataFrame `df\_output`. 

## Methods
<a name="aws-glue-api-pyspark-transforms-FillWithMode-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-pyspark-transforms-FillWithMode-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-FillWithMode-describe)

## \_\_call\_\_(spark\_context, data\_frame, source\_column, mode\_type)
<a name="aws-glue-api-pyspark-transforms-FillWithMode-__call__"></a>

 The `FillWithMode` transform formats the case of strings in a column. 
+ `source_column` – The name of an existing column.
+ `mode_type` – How to resolve tie values in the data. This value must be one of `MINIMUM`, `NONE`, `AVERAGE`, or `MAXIMUM`. 

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FillWithMode-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).