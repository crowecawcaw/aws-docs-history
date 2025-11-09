# FormatPhoneNumber class

The `FormatPhoneNumber` transform returns a column in which a phone number string is
converted into a formatted value.

## Example

```
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from awsgluedi.transforms import *

sc = SparkContext()
spark = SparkSession(sc)

input_df = spark.createDataFrame(
    [
        ("408-341-5669",),
        ("4083415669",)
    ],
    ["phone"],
)

try:
    df_output = column_formatting.FormatPhoneNumber.apply(
        data_frame=input_df,
        spark_context=sc,
        source_column="phone",
        default_region="US"
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

+---------------+
| phone|
+---------------+
|(408) 341-5669|
|(408) 341-5669|
+---------------+

```

```

The `FormatPhoneNumber` transformation takes the `source\_column` as `"phone"` and the `default\_region` as `"US"`.

The transformation successfully formats both phone numbers, regardless of their initial format, to the standard US format
`(408) 341-5669`.

## Methods

- [\_\_call\_\_](#aws-glue-api-pyspark-transforms-FormatPhoneNumber-__call__ "#aws-glue-api-pyspark-transforms-FormatPhoneNumber-__call__")
- [apply](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-apply "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-apply")
- [name](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-name "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-name")
- [describeArgs](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeArgs "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeArgs")
- [describeReturn](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeReturn "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeReturn")
- [describeTransform](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeTransform "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeTransform")
- [describeErrors](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeErrors "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describeErrors")
- [describe](#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describe "#aws-glue-api-crawler-pyspark-transforms-FormatPhoneNumber-describe")

## \_\_call\_\_(spark_context,

data_frame,
source_column,
phone_number_format=None,
default_region=None,
default_region_column=None)

The `FormatPhoneNumber` transform returns a column in which a phone number string is
converted into a formatted value.

- `source_column` – The name of an existing column.
- `phone_number_format` – The format to convert the phone number to.
  If no format is specified, the default is `E.164`, an internationally-recognized standard phone number format.
  Valid values include the following:
  - E164 (omit the period after E)

- `default_region` – A valid region code consisting of two or three uppercase letters
  that specifies the region for the phone number when no country code is present in the number itself.
  At most, one of `defaultRegion` or `defaultRegionColumn` can be provided.
- `default_region_column` – The name of a column of the advanced data type `Country`.
  The region code from the specified column is used to determine the country code for the phone number when no country
  code is present in the number itself. At most, one of `defaultRegion` or `defaultRegionColumn`
  can be provided.

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
