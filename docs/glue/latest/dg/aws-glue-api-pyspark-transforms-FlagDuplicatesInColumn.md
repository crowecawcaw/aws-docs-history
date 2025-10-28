# FlagDuplicatesInColumn class

The `FlagDuplicatesInColumn` transform returns a new column with a specified value in each row
that indicates whether the value in the row's source column matches a value in an earlier row of
the source column. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged,
because it doesn't match an earlier row.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

datasource1 = spark.read.json("s3://${BUCKET}/json/zips/raw/data")

try:
    df_output = column.FlagDuplicatesInColumn.apply(
        data_frame=datasource1,
        spark_context=sc,
        source_column="city",
        target_column="flag_col",
        true_string="True",
        false_string="False"
    )
except:
    print("Unexpected Error happened ")
    raise

```

## Output

The `FlagDuplicatesInColumn` transformation will add a new column `flag\_col` to the `df\_output` DataFrame.
This column will contain a string value indicating whether the corresponding row has a duplicate value in the `city`
column or not. If a row has a duplicate `city` value, the `flag\_col` will contain the `true\_string` value "True".
If a row has a unique `city` value, the `flag\_col` will contain the `false\_string` value "False".

The resulting `df\_output` DataFrame will contain all columns from the original `datasource1` DataFrame, plus the additional
`flag\_col` column indicating duplicate `city` values.

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-FlagDuplicatesInColumn-__call__ "#aws-glue-api-pyspark-transforms-FlagDuplicatesInColumn-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-apply "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-name "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeArgs "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeReturn "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeTransform "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeErrors "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describe "#aws-glue-api-crawler-pyspark-transforms-FlagDuplicatesInColumn-describe")

## \_\_call\_\_(spark_context,

data_frame,
source_column,
target_column,
true_string=DEFAULT_TRUE_STRING,
false_string=DEFAULT_FALSE_STRING)

The `FlagDuplicatesInColumn` transform returns a new column with a specified value in each row
that indicates whether the value in the row's source column matches a value in an earlier row of
the source column. When matches are found, they are flagged as duplicates. The initial occurrence is not flagged,
because it doesn't match an earlier row.

- `source_column` – Name of the source column.
- `target_column` – Name of the target column.
- `true_string` – String to be inserted in the target column when a source column value
  duplicates an earlier value in that column.
- `false_string` – String to be inserted in the target column when a source column value is
  distinct from earlier values in that column.

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
