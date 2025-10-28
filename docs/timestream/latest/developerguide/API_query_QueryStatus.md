For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryStatus

Information about the status of the query, including progress and bytes
scanned.

## Contents

**CumulativeBytesMetered**

The amount of data scanned by the query in bytes that you will be charged for. This is
a cumulative sum and represents the total amount of data that you will be charged for
since the query was started. The charge is applied only once and is either applied when
the query completes running or when the query is cancelled.

Type: Long

Required: No

**CumulativeBytesScanned**

The amount of data scanned by the query in bytes. This is a cumulative sum and
represents the total amount of bytes scanned since the query was started.

Type: Long

Required: No

**ProgressPercentage**

The progress of the query, expressed as a percentage.

Type: Double

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryStatus.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryStatus.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryStatus.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryStatus.md")
