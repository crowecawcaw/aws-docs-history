# IsEven class

The `IsEven` transform returns a Boolean value in a new column that indicates whether the source
column or value is even. If the source column or value is a decimal, the result is false.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [(5,), (0,), (-1,), (2,), (None,)],
    ["source_column"],
)

try:
    df_output = math_functions.IsEven.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column",
        target_column="target_column",
        value=None,
        true_string="Even",
        false_string="Not even",
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

+------------+------------+
|source_column|target_column|
+------------+------------+
| 5| Not even|
| 0| Even|
| -1| Not even|
| 2| Even|
| null| null|
+------------+------------+

```

```

The `IsEven` transformation takes the `source\_column` as "source_column" and the `target\_column` as "target_column".
It checks if the value in the `"source\_column"` is even or not. If the value is even, it sets the `"target\_column"`
value to the `true\_string` "Even". If the value is odd, it sets the `"target\_column"` value to the `false\_string` "Not even".
If the `"source\_column"` value is `null`, the `"target\_column"` value is set to `null`.

The transformation correctly identifies the even numbers (0 and 2) and sets the `"target\_column"` value to "Even".
For odd numbers (5 and -1), it sets the `"target\_column"` value to "Not even". For the `null` value in `"source\_column"`,
the `"target\_column"` value is set to `null`.

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-IsEven-__call__ "#aws-glue-api-pyspark-transforms-IsEven-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-IsEven-apply "#aws-glue-api-crawler-pyspark-transforms-IsEven-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-IsEven-name "#aws-glue-api-crawler-pyspark-transforms-IsEven-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-IsEven-describeArgs "#aws-glue-api-crawler-pyspark-transforms-IsEven-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-IsEven-describeReturn "#aws-glue-api-crawler-pyspark-transforms-IsEven-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-IsEven-describeTransform "#aws-glue-api-crawler-pyspark-transforms-IsEven-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-IsEven-describeErrors "#aws-glue-api-crawler-pyspark-transforms-IsEven-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-IsEven-describe "#aws-glue-api-crawler-pyspark-transforms-IsEven-describe")

## \_\_call\_\_(spark_context,

data_frame,
target_column,
source_column=None,
true_string=DEFAULT_TRUE_STRING,
false_string=DEFAULT_FALSE_STRING,
value=None)

The `IsEven` transform returns a Boolean value in a new column that indicates whether the source
column or value is even. If the source column or value is a decimal, the result is false.

- `source_column` – The name of an existing column.
- `target_column` – The name of the new column to be created.
- `true_string` – A string that indicates whether the value is even.
- `false_string` – A string that indicates whether the value is not even.

## apply(cls, \*args, \*\*kwargs)

Inherited from `GlueTransform`
[apply](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-apply").

## name(cls)

Inherited from `GlueTransform`
[name](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-name").

## describeArgs(cls)

Inherited from `GlueTransform`
[describeArgs](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeArgs").

## describeReturn(cls)

Inherited from `GlueTransform`
[describeReturn](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeReturn").

## describeTransform(cls)

Inherited from `GlueTransform`
[describeTransform](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeTransform").

## describeErrors(cls)

Inherited from `GlueTransform`
[describeErrors](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describeErrors").

## describe(cls)

Inherited from `GlueTransform`
[describe](aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe "aws-glue-api-crawler-pyspark-transforms-GlueTransform.md#aws-glue-api-crawler-pyspark-transforms-GlueTransform-describe").
