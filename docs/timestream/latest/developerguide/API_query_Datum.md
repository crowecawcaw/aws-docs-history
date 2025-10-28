For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Datum

Datum represents a single data point in a query result.

## Contents

**ArrayValue**

Indicates if the data point is an array.

Type: Array of [Datum](API_query_Datum.md "API_query_Datum.md") objects

Required: No

**NullValue**

Indicates if the data point is null.

Type: Boolean

Required: No

**RowValue**

Indicates if the data point is a row.

Type: [Row](API_query_Row.md "API_query_Row.md") object

Required: No

**ScalarValue**

Indicates if the data point is a scalar value such as integer, string, double, or
Boolean.

Type: String

Required: No

**TimeSeriesValue**

Indicates if the data point is a timeseries data type.

Type: Array of [TimeSeriesDataPoint](API_query_TimeSeriesDataPoint.md "API_query_TimeSeriesDataPoint.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/Datum.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/Datum.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Datum.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Datum.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Datum.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Datum.md")
