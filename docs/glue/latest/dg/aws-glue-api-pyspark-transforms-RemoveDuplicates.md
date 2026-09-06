

# RemoveDuplicates class
<a name="aws-glue-api-pyspark-transforms-RemoveDuplicates"></a>

 The `RemoveDuplicates` transform deletes an entire row, if a duplicate value is encountered in a selected source column. 

## Example
<a name="pyspark-RemoveDuplicates-examples"></a>

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
<a name="pyspark-RemoveDuplicates-output"></a>

 The output will be a PySpark DataFrame with duplicates removed based on the `source_column_1` column. The resulting `df\_output` DataFrame will contain the following rows: 

```
```
+---------------+---------------+
|source_column_1|source_column_2|
+---------------+---------------+
| 105.111| 13.12|
| 13.12| 13.12|
| null| 13.12|
+---------------+---------------+
```
```

 Note that the rows with `source_column_1` values of `13.12` and `null` appear only once in the output DataFrame, as the duplicates have been removed based on the `source_column_1` column. 

## Methods
<a name="aws-glue-api-pyspark-transforms-RemoveDuplicates-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-pyspark-transforms-RemoveDuplicates-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describe)

## \_\_call\_\_(spark\_context, data\_frame, source\_column)
<a name="aws-glue-api-pyspark-transforms-RemoveDuplicates-__call__"></a>

 The `RemoveDuplicates` transform deletes an entire row, if a duplicate value is encountered in a selected source column. 
+ `source_column` – The name of an existing column.

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-RemoveDuplicates-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).