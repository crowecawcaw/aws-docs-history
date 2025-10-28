For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# TimeSeriesDataPoint

The timeseries data type represents the values of a measure over time. A time series
is an array of rows of timestamps and measure values, with rows sorted in ascending
order of time. A TimeSeriesDataPoint is a single data point in the time series. It
represents a tuple of (time, measure value) in a time series.

## Contents

**Time**

The timestamp when the measure value was collected.

Type: String

Required: Yes

**Value**

The measure value for the data point.

Type: [Datum](API_query_Datum.md "API_query_Datum.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/TimeSeriesDataPoint.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/TimeSeriesDataPoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/TimeSeriesDataPoint.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/TimeSeriesDataPoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/TimeSeriesDataPoint.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/TimeSeriesDataPoint.md")
