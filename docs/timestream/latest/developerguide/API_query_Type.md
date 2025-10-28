For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Type

Contains the data type of a column in a query result set. The data type can be scalar
or complex. The supported scalar data types are integers, Boolean, string, double,
timestamp, date, time, and intervals. The supported complex data types are arrays, rows,
and timeseries.

## Contents

**ArrayColumnInfo**

Indicates if the column is an array.

Type: [ColumnInfo](API_query_ColumnInfo.md "API_query_ColumnInfo.md") object

Required: No

**RowColumnInfo**

Indicates if the column is a row.

Type: Array of [ColumnInfo](API_query_ColumnInfo.md "API_query_ColumnInfo.md") objects

Required: No

**ScalarType**

Indicates if the column is of type string, integer, Boolean, double, timestamp, date,
time. For more information, see [Supported data
types](supported-data-types.md "supported-data-types.md").

Type: String

Valid Values: `VARCHAR | BOOLEAN | BIGINT | DOUBLE | TIMESTAMP | DATE | TIME | INTERVAL_DAY_TO_SECOND | INTERVAL_YEAR_TO_MONTH | UNKNOWN | INTEGER`

Required: No

**TimeSeriesMeasureValueColumnInfo**

Indicates if the column is a timeseries data type.

Type: [ColumnInfo](API_query_ColumnInfo.md "API_query_ColumnInfo.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/Type.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/Type.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Type.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/Type.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Type.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/Type.md")
