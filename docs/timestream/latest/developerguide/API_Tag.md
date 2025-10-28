For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Tag

A tag is a label that you assign to a Timestream database and/or table. Each tag consists of a key and
an optional value, both of which you define. With tags, you can categorize databases and/or tables, for example, by
purpose, owner, or environment.

## Contents

**Key**

The key of the tag. Tag keys are case sensitive.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

**Value**

The value of the tag. Tag values are case-sensitive and can be null.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 256.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Tag.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Tag.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Tag.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Tag.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Tag.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Tag.md")
