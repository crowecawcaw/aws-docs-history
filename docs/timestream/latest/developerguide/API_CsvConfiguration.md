For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CsvConfiguration

A delimited data format where the column separator can be a comma and the record separator is a newline
character.

## Contents

**ColumnSeparator**

Column separator can be one of comma (','), pipe ('|), semicolon (';'), tab('/t'), or blank space (' ').

Type: String

Length Constraints: Fixed length of 1.

Required: No

**EscapeChar**

Escape character can be one of

Type: String

Length Constraints: Fixed length of 1.

Required: No

**NullValue**

Can be blank space (' ').

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**QuoteChar**

Can be single quote (') or double quote (").

Type: String

Length Constraints: Fixed length of 1.

Required: No

**TrimWhiteSpace**

Specifies to trim leading and trailing white space.

Type: Boolean

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/CsvConfiguration.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/CsvConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CsvConfiguration.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/CsvConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CsvConfiguration.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/CsvConfiguration.md")
