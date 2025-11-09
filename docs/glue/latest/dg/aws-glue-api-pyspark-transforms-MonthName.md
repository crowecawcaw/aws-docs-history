# MonthName class

The `MonthName` transform creates a new column containing the name of the month, from a string that represents a date.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")

input_df = spark.createDataFrame(
    [
        ("20-2018-12",),
        ("2018-20-12",),
        ("20182012",),
        ("12202018",),
        ("20122018",),
        ("20-12-2018",),
        ("12/20/2018",),
        ("02/02/02",),
        ("02 02 2009",),
        ("02/02/2009",),
        ("August/02/2009",),
        ("02/june/2009",),
        ("02/2020/june",),
        ("2013-02-21 06:35:45.658505",),
        ("August 02 2009",),
        ("2013/02/21",),
        (None,),
    ],
    ["column_1"],
)

try:
    df_output = datetime_functions.MonthName.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="column_1",
        target_column="target_column"
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
| column_1|target_column|
+------------+------------+
|20-2018-12 | December |
|2018-20-12 | null |
| 20182012| null |
| 12202018| null |
| 20122018| null |
|20-12-2018 | December |
|12/20/2018 | December |
| 02/02/02 | February |
|02 02 2009 | February |
|02/02/2009 | February |
|August/02/2009| August |
|02/june/2009| null |
|02/2020/june| null |
|2013-02-21 06:35:45.658505| February |
|August 02 2009| August |
| 2013/02/21| February |
| null | null |
+------------+------------+

```

```

The `MonthName` transformation takes the `source\_column` as `"column\_1"` and the `target\_column` as `"target\_column"`.
It attempts to extract the month name from the date/time strings in the `"column\_1"` column and places it in the
`"target\_column"` column. If the date/time string is in an unrecognized format or cannot be parsed, the
`"target\_column"` value is set to `null`.

The transformation successfully extracts the month name from various date/time formats, such as "20-12-2018", "12/20/2018",
"02/02/2009", "2013-02-21 06:35:45.658505", and "August 02 2009".

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-MonthName-__call__ "#aws-glue-api-pyspark-transforms-MonthName-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-MonthName-apply "#aws-glue-api-crawler-pyspark-transforms-MonthName-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-MonthName-name "#aws-glue-api-crawler-pyspark-transforms-MonthName-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-MonthName-describeArgs "#aws-glue-api-crawler-pyspark-transforms-MonthName-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-MonthName-describeReturn "#aws-glue-api-crawler-pyspark-transforms-MonthName-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-MonthName-describeTransform "#aws-glue-api-crawler-pyspark-transforms-MonthName-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-MonthName-describeErrors "#aws-glue-api-crawler-pyspark-transforms-MonthName-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-MonthName-describe "#aws-glue-api-crawler-pyspark-transforms-MonthName-describe")

## \_\_call\_\_(spark_context,

data_frame,
target_column,
source_column=None,
value=None)

The `MonthName` transform creates a new column containing the name of the month, from a string that represents a date.

- `source_column` – The name of an existing column.
- `value` – A character string to evaluate..
- `target_column` – A name for the newly created column.

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
