# IpToInt class

The `IpToInt` transform converts the Internet Protocol version 4 (IPv4) value of the source column or
other value to the corresponding integer value in the target column, and returns the result in a new column.

## Example

For AWS Glue 4.0 and above, create or update job arguments with `key: --enable-glue-di-transforms, value: true`

```
from pyspark.context import SparkContext
from awsgluedi.transforms import *

sc = SparkContext()

input_df = spark.createDataFrame(
    [
        ("192.0.0.1",),
        ("10.10.10.10",),
        ("1.2.3.4",),
        ("1.2.3.6",),
        ("http://12.13.14.15",),
        ("https://16.17.18.19",),
        ("1.2.3.4",),
        (None,),
        ("abc",),
        ("abc.abc.abc.abc",),
        ("321.123.123.123",),
        ("244.4.4.4",),
        ("255.255.255.255",),
    ],
    ["source_column_ip"],
)

    df_output = web_functions.IpToInt.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="source_column_ip",
        target_column="target_column",
        value=None
    )
    df_output.show()

```

## Output

The output will be:

```

```

+----------------+---------------+
|source_column_ip| target_column|
+----------------+---------------+
| 192.0.0.1| 3221225473|
| 10.10.10.10| 168427722|
| 1.2.3.4| 16909060|
| 1.2.3.6| 16909062|
|http://12.13.14.15| null|
|https://16.17.18.19| null|
| 1.2.3.4| 16909060|
| null| null|
| abc| null|
|abc.abc.abc.abc| null|
| 321.123.123.123| null|
| 244.4.4.4| 4102444804|
| 255.255.255.255| 4294967295|
+----------------+---------------+

```

```

The `IpToInt` transformation takes the `source\_column` as `"source\_column\_ip"` and the `target\_column`
as `"target\_column"` and converts the valid IPv4 address strings in the `source\_column\_ip` column to their corresponding
32-bit integer representation and stores the result in the `target\_column` column.

For valid IPv4 address strings (e.g., "192.0.0.1", "10.10.10.10", "1.2.3.4"), the transformation successfully converts them
to their integer representation (e.g., 3221225473, 168427722, 16909060).
For strings that are not valid IPv4 addresses (e.g., URLs, non-IP strings like "abc", invalid IP formats like "abc.abc.abc.abc"),
the `target\_column` value is set to `null`.
For `null` values in the `source\_column\_ip` column, the `target\_column` value is also set to `null`.

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-IpToInt-__call__ "#aws-glue-api-pyspark-transforms-IpToInt-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-IpToInt-apply "#aws-glue-api-crawler-pyspark-transforms-IpToInt-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-IpToInt-name "#aws-glue-api-crawler-pyspark-transforms-IpToInt-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeArgs "#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeReturn "#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeTransform "#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeErrors "#aws-glue-api-crawler-pyspark-transforms-IpToInt-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-IpToInt-describe "#aws-glue-api-crawler-pyspark-transforms-IpToInt-describe")

## \_\_call\_\_(spark_context,

data_frame,
target_column,
source_column=None,
value=None)

The `IpToInt` transform converts the Internet Protocol version 4 (IPv4) value of the source column or
other value to the corresponding integer value in the target column, and returns the result in a new column.

- `sourceColumn` – The name of an existing column.
- `value` – A character string to evaluate.
- `targetColumn` – The name of the new column to be created.

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
