For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryTemporalRangeMax

Provides insights into the table with the most sub-optimal temporal pruning scanned by your query.

## Contents

**TableArn**

The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**Value**

The maximum duration in nanoseconds between the start and end of the query.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryTemporalRangeMax.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryTemporalRangeMax.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryTemporalRangeMax.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryTemporalRangeMax.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryTemporalRangeMax.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryTemporalRangeMax.md")
