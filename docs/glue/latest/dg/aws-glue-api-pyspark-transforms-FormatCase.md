

# FormatCase class
<a name="aws-glue-api-pyspark-transforms-FormatCase"></a>

The `FormatCase` transform changes each string in a column to the specified case type.

## Example
<a name="pyspark-FormatCase-examples"></a>

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

datasource1 = spark.read.json("s3://${BUCKET}/json/zips/raw/data")

try:
    df_output = data_cleaning.FormatCase.apply(
        data_frame=datasource1,
        spark_context=sc,
        source_column="city",
        case_type="LOWER"
    )    
except:
    print("Unexpected Error happened ")
    raise
```

## Output
<a name="pyspark-FormatCase-output"></a>

 The `FormatCase` transformation will convert the values in the `city` column to lowercase based on the `case\_type="LOWER"` parameter. The resulting `df\_output` DataFrame will contain all columns from the original `datasource1` DataFrame, but with the `city` column values in lowercase. 

## Methods
<a name="aws-glue-api-pyspark-transforms-FormatCase-_methods"></a>
+ [\_\_call\_\_](#aws-glue-api-pyspark-transforms-FormatCase-__call__)
+ [apply](#aws-glue-api-crawler-pyspark-transforms-FormatCase-apply)
+ [name](#aws-glue-api-crawler-pyspark-transforms-FormatCase-name)
+ [describeArgs](#aws-glue-api-crawler-pyspark-transforms-FormatCase-describeArgs)
+ [describeReturn](#aws-glue-api-crawler-pyspark-transforms-FormatCase-describeReturn)
+ [describeTransform](#aws-glue-api-crawler-pyspark-transforms-FormatCase-describeTransform)
+ [describeErrors](#aws-glue-api-crawler-pyspark-transforms-FormatCase-describeErrors)
+ [describe](#aws-glue-api-crawler-pyspark-transforms-FormatCase-describe)

## \_\_call\_\_(spark\_context, data\_frame, source\_column, case\_type)
<a name="aws-glue-api-pyspark-transforms-FormatCase-__call__"></a>

The `FormatCase` transform changes each string in a column to the specified case type.
+ `source_column` – The name of an existing column.
+ `case_type` – Supported case types are `CAPITAL`,`LOWER`, `UPPER`, `SENTENCE`. 

## apply(cls, \*args, \*\*kwargs)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-apply"></a>

Inherited from `GlueTransform` [apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply).

## name(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-name"></a>

Inherited from `GlueTransform` [name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name).

## describeArgs(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-describeArgs"></a>

Inherited from `GlueTransform` [describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs).

## describeReturn(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-describeReturn"></a>

Inherited from `GlueTransform` [describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn).

## describeTransform(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-describeTransform"></a>

Inherited from `GlueTransform` [describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform).

## describeErrors(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-describeErrors"></a>

Inherited from `GlueTransform` [describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors).

## describe(cls)
<a name="aws-glue-api-crawler-pyspark-transforms-FormatCase-describe"></a>

Inherited from `GlueTransform` [describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe).