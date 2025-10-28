For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryInsightsResponse

Provides various insights and metrics related to the query that you executed.

## Contents

**OutputBytes**

Indicates the size of query result set in bytes. You can use this data to validate if the result set has changed as part of the query tuning exercise.

Type: Long

Required: No

**OutputRows**

Indicates the total number of rows returned as part of the query result set. You can use this data to validate if the number of rows in the result set have changed as part of the query tuning exercise.

Type: Long

Required: No

**QuerySpatialCoverage**

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning.

Type: [QuerySpatialCoverage](API_query_QuerySpatialCoverage.md "API_query_QuerySpatialCoverage.md") object

Required: No

**QueryTableCount**

Indicates the number of tables in the query.

Type: Long

Required: No

**QueryTemporalRange**

Provides insights into the temporal range of the query, including the table with the largest (max) time range. Following are some of the potential options for optimizing time-based pruning:

- Add missing time-predicates.
- Remove functions around the time predicates.
- Add time predicates to all the sub-queries.

Type: [QueryTemporalRange](API_query_QueryTemporalRange.md "API_query_QueryTemporalRange.md") object

Required: No

**UnloadPartitionCount**

Indicates the partitions created by the `Unload` operation.

Type: Long

Required: No

**UnloadWrittenBytes**

Indicates the size, in bytes, written by the `Unload` operation.

Type: Long

Required: No

**UnloadWrittenRows**

Indicates the rows written by the `Unload` query.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryInsightsResponse.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryInsightsResponse.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryInsightsResponse.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryInsightsResponse.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryInsightsResponse.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryInsightsResponse.md")
