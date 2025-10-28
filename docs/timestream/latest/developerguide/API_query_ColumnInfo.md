For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ColumnInfo

Contains the metadata for query results such as the column names, data types, and
other attributes.

## Contents

**Type**

The data type of the result set column. The data type can be a scalar or complex.
Scalar data types are integers, strings, doubles, Booleans, and others. Complex data
types are types such as arrays, rows, and others.

Type: [Type](API_query_Type.md "API_query_Type.md") object

Required: Yes

**Name**

The name of the result set column. The name of the result set is available for
columns of all data types except for arrays.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ColumnInfo.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ColumnInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ColumnInfo.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ColumnInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ColumnInfo.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ColumnInfo.md")
