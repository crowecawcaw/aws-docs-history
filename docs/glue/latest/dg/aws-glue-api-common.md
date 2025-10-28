# Common data types

The Common data types describes miscellaneous common data types in AWS Glue.

## Tag structure

The `Tag` object represents a label that you can assign to
an AWS resource. Each tag consists of a key and an optional value,
both of which you define.

For more information about tags, and controlling access to resources
in AWS Glue, see [AWS Tags in AWS Glue](monitor-tags.md "monitor-tags.md") and [Specifying
AWS Glue Resource ARNs](glue-specifying-resource-arns.md "glue-specifying-resource-arns.md") in the developer guide.

###### Fields

- `key` – UTF-8 string, not less than 1 or more than 128 bytes long.

The tag key. The key is required when you create a tag on an object. The key
is case-sensitive, and must not contain the prefix aws.

- `value` – UTF-8 string, not more than 256 bytes long.

The tag value. The value is optional when you create a tag on an object. The
value is case-sensitive, and must not contain the prefix aws.

## DecimalNumber structure

Contains a numeric value in decimal format.

###### Fields

- `UnscaledValue` – _Required:_ Blob.

The unscaled numeric value.

- `Scale` – _Required:_ Number (integer).

The scale that determines where the decimal point falls in the unscaled
value.

## ErrorDetail structure

Contains details about an error.

###### Fields

- `ErrorCode` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](#aws-glue-api-regex-oneLine "#aws-glue-api-regex-oneLine").

The code associated with this error.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](#aws-glue-api-regex-uri "#aws-glue-api-regex-uri").

A message describing the error.

## PropertyPredicate structure

Defines a property predicate.

###### Fields

- `Key` – Value string, not less than 1 or more than 1024 bytes long.

The key of the property.

- `Value` – Value string, not less than 1 or more than 1024 bytes long.

The value of the property.

- `Comparator` – UTF-8 string (valid values: `EQUALS` | `GREATER_THAN` | `LESS_THAN` | `GREATER_THAN_EQUALS` | `LESS_THAN_EQUALS`).

The comparator used to compare this property to others.

## ResourceUri structure

The URIs for function resources.

###### Fields

- `ResourceType` – UTF-8 string (valid values: `JAR` | `FILE` | `ARCHIVE`).

The type of the resource.

- `Uri` – Uniform resource identifier (uri), not less than 1 or more than 1024 bytes long, matching the [URI address multi-line string pattern](#aws-glue-api-regex-uri "#aws-glue-api-regex-uri").

The URI for accessing the resource.

## ColumnStatistics structure

Represents the generated column-level statistics for a table or partition.

###### Fields

- `ColumnName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](#aws-glue-api-regex-oneLine "#aws-glue-api-regex-oneLine").

Name of column which statistics belong to.

- `ColumnType` – _Required:_ Type name, not more than 20000 bytes long, matching the [Single-line string pattern](#aws-glue-api-regex-oneLine "#aws-glue-api-regex-oneLine").

The data type of the column.

- `AnalyzedTime` – _Required:_ Timestamp.

The timestamp of when column statistics were generated.

- `StatisticsData` – _Required:_ A [ColumnStatisticsData](#aws-glue-api-common-ColumnStatisticsData "#aws-glue-api-common-ColumnStatisticsData") object.

A `ColumnStatisticData` object that contains the statistics
data values.

## ColumnStatisticsError structure

Encapsulates a `ColumnStatistics` object that failed and
the reason for failure.

###### Fields

- `ColumnStatistics` – A [ColumnStatistics](#aws-glue-api-common-ColumnStatistics "#aws-glue-api-common-ColumnStatistics") object.

The `ColumnStatistics` of the column.

- `Error` – An [ErrorDetail](#aws-glue-api-common-ErrorDetail "#aws-glue-api-common-ErrorDetail") object.

An error message with the reason for the failure of an operation.

## ColumnError structure

Encapsulates a column name that failed and the reason for failure.

###### Fields

- `ColumnName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](#aws-glue-api-regex-oneLine "#aws-glue-api-regex-oneLine").

The name of the column that failed.

- `Error` – An [ErrorDetail](#aws-glue-api-common-ErrorDetail "#aws-glue-api-common-ErrorDetail") object.

An error message with the reason for the failure of an operation.

## ColumnStatisticsData structure

Contains the individual types of column statistics data. Only one data
object should be set and indicated by the `Type` attribute.

###### Fields

- `Type` – _Required:_ UTF-8 string (valid values: `BOOLEAN` | `DATE` | `DECIMAL` | `DOUBLE` | `LONG` | `STRING` | `BINARY`).

The type of column statistics data.

- `BooleanColumnStatisticsData` – A [BooleanColumnStatisticsData](#aws-glue-api-common-BooleanColumnStatisticsData "#aws-glue-api-common-BooleanColumnStatisticsData") object.

Boolean column statistics data.

- `DateColumnStatisticsData` – A [DateColumnStatisticsData](#aws-glue-api-common-DateColumnStatisticsData "#aws-glue-api-common-DateColumnStatisticsData") object.

Date column statistics data.

- `DecimalColumnStatisticsData` – A [DecimalColumnStatisticsData](#aws-glue-api-common-DecimalColumnStatisticsData "#aws-glue-api-common-DecimalColumnStatisticsData") object.

Decimal column statistics data. UnscaledValues within are Base64-encoded
binary objects storing big-endian, two's complement representations of the
decimal's unscaled value.

- `DoubleColumnStatisticsData` – A [DoubleColumnStatisticsData](#aws-glue-api-common-DoubleColumnStatisticsData "#aws-glue-api-common-DoubleColumnStatisticsData") object.

Double column statistics data.

- `LongColumnStatisticsData` – A [LongColumnStatisticsData](#aws-glue-api-common-LongColumnStatisticsData "#aws-glue-api-common-LongColumnStatisticsData") object.

Long column statistics data.

- `StringColumnStatisticsData` – A [StringColumnStatisticsData](#aws-glue-api-common-StringColumnStatisticsData "#aws-glue-api-common-StringColumnStatisticsData") object.

String column statistics data.

- `BinaryColumnStatisticsData` – A [BinaryColumnStatisticsData](#aws-glue-api-common-BinaryColumnStatisticsData "#aws-glue-api-common-BinaryColumnStatisticsData") object.

Binary column statistics data.

## BooleanColumnStatisticsData structure

Defines column statistics supported for Boolean data columns.

###### Fields

- `NumberOfTrues` – _Required:_ Number (long), not more than None.

The number of true values in the column.

- `NumberOfFalses` – _Required:_ Number (long), not more than None.

The number of false values in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

## DateColumnStatisticsData structure

Defines column statistics supported for timestamp data columns.

###### Fields

- `MinimumValue` – Timestamp.

The lowest value in the column.

- `MaximumValue` – Timestamp.

The highest value in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

- `NumberOfDistinctValues` – _Required:_ Number (long), not more than None.

The number of distinct values in a column.

## DecimalColumnStatisticsData structure

Defines column statistics supported for fixed-point number data columns.

###### Fields

- `MinimumValue` – A [DecimalNumber](#aws-glue-api-common-DecimalNumber "#aws-glue-api-common-DecimalNumber") object.

The lowest value in the column.

- `MaximumValue` – A [DecimalNumber](#aws-glue-api-common-DecimalNumber "#aws-glue-api-common-DecimalNumber") object.

The highest value in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

- `NumberOfDistinctValues` – _Required:_ Number (long), not more than None.

The number of distinct values in a column.

## DoubleColumnStatisticsData structure

Defines column statistics supported for floating-point number data
columns.

###### Fields

- `MinimumValue` – Number (double).

The lowest value in the column.

- `MaximumValue` – Number (double).

The highest value in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

- `NumberOfDistinctValues` – _Required:_ Number (long), not more than None.

The number of distinct values in a column.

## LongColumnStatisticsData structure

Defines column statistics supported for integer data columns.

###### Fields

- `MinimumValue` – Number (long).

The lowest value in the column.

- `MaximumValue` – Number (long).

The highest value in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

- `NumberOfDistinctValues` – _Required:_ Number (long), not more than None.

The number of distinct values in a column.

## StringColumnStatisticsData structure

Defines column statistics supported for character sequence data values.

###### Fields

- `MaximumLength` – _Required:_ Number (long), not more than None.

The size of the longest string in the column.

- `AverageLength` – _Required:_ Number (double), not more than None.

The average string length in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

- `NumberOfDistinctValues` – _Required:_ Number (long), not more than None.

The number of distinct values in a column.

## BinaryColumnStatisticsData structure

Defines column statistics supported for bit sequence data values.

###### Fields

- `MaximumLength` – _Required:_ Number (long), not more than None.

The size of the longest bit sequence in the column.

- `AverageLength` – _Required:_ Number (double), not more than None.

The average bit sequence length in the column.

- `NumberOfNulls` – _Required:_ Number (long), not more than None.

The number of null values in the column.

## String patterns

The API uses the following regular expressions to define what
is valid content for various string parameters and members:

- Single-line string pattern –
  "`[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`"
- URI address multi-line string pattern –
  "`[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`"
- A Logstash Grok string pattern –
  "`[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\t]*`"
- Identifier string pattern –
  "`[A-Za-z_][A-Za-z0-9_]*`"
- AWS IAM ARN string pattern –
  "`arn:aws:iam::\d{12}:role/.*`"
- Version string pattern –
  "`^[a-zA-Z0-9-_]+$`"
- Log group string pattern –
  "`[\.\-_/#A-Za-z0-9]+`"
- Log-stream string pattern –
  "`[^:*]*`"
- Custom string pattern #10 –
  "`[a-zA-Z0-9-_]+`"
- Custom string pattern #11 –
  "`[-a-zA-Z0-9+=/:_]*`"
- Custom string pattern #12 –
  "`[\S\s]*`"
- Custom string pattern #13 –
  "`.*\S.*`"
- Custom string pattern #14 –
  "`[a-zA-Z0-9-=._/@]+`"
- Custom string pattern #15 –
  "`[1-9][0-9]*|[1-9][0-9]*-[1-9][0-9]*`"
- Custom string pattern #16 –
  "`[A-Z][A-Za-z\.]+`"
- Custom string pattern #17 –
  "`[\S]*`"
- Custom string pattern #18 –
  "`[\w]*`"
- Custom string pattern #19 –
  "`arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`"
- Custom string pattern #20 –
  "`subnet-[a-z0-9]+`"
- Custom string pattern #21 –
  "`\d{12}`"
- Custom string pattern #22 –
  "`([a-z]+)-([a-z]+-)?([a-z]+)-[0-9]+[a-z]+`"
- Custom string pattern #23 –
  "`[a-zA-Z0-9.-]*`"
- Custom string pattern #24 –
  "`arn:aws[a-z0-9\-]*:lambda:[a-z0-9\-]+:\d{12}:function:([\w\-]{1,64})`"
- Custom string pattern #25 –
  "`^(?!(.*[.\/\\]|aws:)).*$`"
- Custom string pattern #26 –
  "`[^\r\n]`"
- Custom string pattern #27 –
  "`^\w+\.\w+\.\w+$`"
- Custom string pattern #28 –
  "`^\w+\.\w+$`"
- Custom string pattern #29 –
  "`^$|arn:aws[a-z0-9-]*:kms:.*`"
- Custom string pattern #30 –
  "`arn:aws[^:]*:iam::[0-9]*:role/.+`"
- Custom string pattern #31 –
  "`[\.\-_A-Za-z0-9]+`"
- Custom string pattern #32 –
  "`^s3://([^/]+)/([^/]+/)*([^/]+)$`"
- Custom string pattern #33 –
  "`.*`"
- Custom string pattern #34 –
  "`^(Sun|Mon|Tue|Wed|Thu|Fri|Sat):([01]?[0-9]|2[0-3])$`"
- Custom string pattern #35 –
  "`[a-zA-Z0-9_.-]+`"
- Custom string pattern #36 –
  "`^arn:aws(-(cn|us-gov|iso(-[bef])?))?:secretsmanager:.*$`"
- Custom string pattern #37 –
  "`\S+`"
- Custom string pattern #38 –
  "`^[\x20-\x7E]*$`"
- Custom string pattern #39 –
  "`^([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_=]+)\.([a-zA-Z0-9_\-\+\/=]*)`"
- Custom string pattern #40 –
  "`^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`"
- Custom string pattern #41 –
  "`^(https?):\/\/[^\s/$.?#].[^\s]*$`"
- Custom string pattern #42 –
  "`arn:aws:kms:.*`"
- Custom string pattern #43 –
  "`^subnet-[a-z0-9]+$`"
- Custom string pattern #44 –
  "`[\p{L}\p{N}\p{P}]*`"
- Custom string pattern #45 –
  "`[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`"
- Custom string pattern #46 –
  "`[a-zA-Z0-9-_$#.]+`"
- Custom string pattern #47 –
  "`^\d{12}$`"
- Custom string pattern #48 –
  "`^(\w+\.)+\w+$`"
- Custom string pattern #49 –
  "`^([2-3]|3[.]9)$`"
- Custom string pattern #50 –
  "`arn:aws(-(cn|us-gov|iso(-[bef])?))?:glue:.*`"
- Custom string pattern #51 –
  "`[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}`"
- Custom string pattern #52 –
  "`(^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::\w{12}:root)`"
- Custom string pattern #53 –
  "`^arn:aws(-(cn|us-gov|iso(-[bef])?))?:iam::[0-9]{12}:role/.+`"
- Custom string pattern #54 –
  "`[\s\S]*`"
- Custom string pattern #55 –
  "`([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF]|[^\S\r\n"'= ;])*`"
- Custom string pattern #56 –
  "`^[A-Z\_]+$`"
- Custom string pattern #57 –
  "`^[A-Za-z0-9]+$`"
- Custom string pattern #58 –
  "`[*A-Za-z0-9_-]*`"
- Custom string pattern #59 –
  "`([\u0020-\u007E\r\s\n])*`"
- Custom string pattern #60 –
  "`[A-Za-z0-9_-]*`"
- Custom string pattern #61 –
  "`([\u0009\u000B\u000C\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF])*`"
- Custom string pattern #62 –
  "`([\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\s])*`"
- Custom string pattern #63 –
  "`([^\r\n])*`"
