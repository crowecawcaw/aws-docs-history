For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# TimestreamConfiguration

Configuration to write data into Timestream database and table. This configuration
allows the user to map the query result select columns into the destination table
columns.

## Contents

**DatabaseName**

Name of Timestream database to which the query result will be written.

Type: String

Required: Yes

**DimensionMappings**

This is to allow mapping column(s) from the query result to the dimension in the
destination table.

Type: Array of [DimensionMapping](API_query_DimensionMapping.md "API_query_DimensionMapping.md") objects

Required: Yes

**TableName**

Name of Timestream table that the query result will be written to. The table should be
within the same database that is provided in Timestream configuration.

Type: String

Required: Yes

**TimeColumn**

Column from query result that should be used as the time column in destination table.
Column type for this should be TIMESTAMP.

Type: String

Required: Yes

**MeasureNameColumn**

Name of the measure column.

Type: String

Required: No

**MixedMeasureMappings**

Specifies how to map measures to multi-measure records.

Type: Array of [MixedMeasureMapping](API_query_MixedMeasureMapping.md "API_query_MixedMeasureMapping.md") objects

Array Members: Minimum number of 1 item.

Required: No

**MultiMeasureMappings**

Multi-measure mappings.

Type: [MultiMeasureMappings](API_query_MultiMeasureMappings.md "API_query_MultiMeasureMappings.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/TimestreamConfiguration.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/TimestreamConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/TimestreamConfiguration.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/TimestreamConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/TimestreamConfiguration.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/TimestreamConfiguration.md")
