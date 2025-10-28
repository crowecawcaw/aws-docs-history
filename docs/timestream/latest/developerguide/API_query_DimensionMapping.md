For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# DimensionMapping

This type is used to map column(s) from the query result to a dimension in the
destination table.

## Contents

**DimensionValueType**

Type for the dimension.

Type: String

Valid Values: `VARCHAR`

Required: Yes

**Name**

Column name from query result.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/DimensionMapping.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/DimensionMapping.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DimensionMapping.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/DimensionMapping.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DimensionMapping.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/DimensionMapping.md")
