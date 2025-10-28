For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QuerySpatialCoverage

Provides insights into the spatial coverage of the query, including the table with sub-optimal (max) spatial pruning. This information can help you identify areas for improvement in your partitioning strategy to enhance spatial pruning

For example, you can do the following with the `QuerySpatialCoverage` information:

- Add measure_name or use [customer-defined partition key](customer-defined-partition-keys.md "customer-defined-partition-keys.md") (CDPK) predicates.
- If you've already done the preceding action, remove functions around them or clauses, such as `LIKE`.

## Contents

**Max**

Provides insights into the spatial coverage of the executed query and the table with the most inefficient spatial pruning.

- `Value` – The maximum ratio of spatial coverage.
- `TableArn` – The Amazon Resource Name (ARN) of the table with sub-optimal spatial pruning.
- `PartitionKey` – The partition key used for partitioning, which can be a default `measure_name` or a CDPK.

Type: [QuerySpatialCoverageMax](API_query_QuerySpatialCoverageMax.md "API_query_QuerySpatialCoverageMax.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverage.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QuerySpatialCoverage.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverage.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QuerySpatialCoverage.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverage.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QuerySpatialCoverage.md")
