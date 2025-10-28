For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ParameterMapping

Mapping for named parameters.

## Contents

**Name**

Parameter name.

Type: String

Required: Yes

**Type**

Contains the data type of a column in a query result set. The data type can be scalar
or complex. The supported scalar data types are integers, Boolean, string, double,
timestamp, date, time, and intervals. The supported complex data types are arrays, rows,
and timeseries.

Type: [Type](API_query_Type.md "API_query_Type.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ParameterMapping.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ParameterMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ParameterMapping.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ParameterMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ParameterMapping.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ParameterMapping.md")
