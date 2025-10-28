For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryTemporalRange

Provides insights into the temporal range of the query, including the table with the largest (max) time range.

## Contents

**Max**

Encapsulates the following properties that provide insights into the most sub-optimal performing table on the temporal axis:

- `Value` – The maximum duration in nanoseconds between the start and end of the query.
- `TableArn` – The Amazon Resource Name (ARN) of the table which is queried with the largest time range.

Type: [QueryTemporalRangeMax](API_query_QueryTemporalRangeMax.md "API_query_QueryTemporalRangeMax.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryTemporalRange.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryTemporalRange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryTemporalRange.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryTemporalRange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryTemporalRange.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryTemporalRange.md")
