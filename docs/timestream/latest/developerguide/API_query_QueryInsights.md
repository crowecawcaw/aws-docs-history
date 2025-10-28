For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# QueryInsights

`QueryInsights` is a performance tuning feature that helps you optimize your queries, reducing costs and improving performance. With `QueryInsights`, you can assess the pruning efficiency of your queries and identify areas for improvement to enhance query performance. With `QueryInsights`, you can also analyze the effectiveness of your queries in terms of temporal and spatial pruning, and identify opportunities to improve performance. Specifically, you can evaluate how well your queries use time-based and partition key-based indexing strategies to optimize data retrieval. To optimize query performance, it's essential that you fine-tune both the temporal and spatial parameters that govern query execution.

The key metrics provided by `QueryInsights` are `QuerySpatialCoverage` and `QueryTemporalRange`. `QuerySpatialCoverage` indicates how much of the spatial axis the query scans, with lower values being more efficient. `QueryTemporalRange` shows the time range scanned, with narrower ranges being more performant.

**Benefits of QueryInsights**

The following are the key benefits of using `QueryInsights`:

- **Identifying inefficient queries** – `QueryInsights` provides information on the time-based and attribute-based pruning of the tables accessed by the query. This information helps you identify the tables that are sub-optimally accessed.
- **Optimizing your data model and partitioning** – You can use the `QueryInsights` information to access and fine-tune your data model and partitioning strategy.
- **Tuning queries** – `QueryInsights` highlights opportunities to use indexes more effectively.

###### Note

The maximum number of `Query` API requests you're allowed to make with `QueryInsights` enabled is 1 query per second (QPS). If you exceed this query rate, it might result in throttling.

## Contents

**Mode**

Provides the following modes to enable `QueryInsights`:

- `ENABLED_WITH_RATE_CONTROL` – Enables `QueryInsights` for the queries being processed. This mode also includes a rate control mechanism, which limits the `QueryInsights` feature to 1 query per second (QPS).
- `DISABLED` – Disables `QueryInsights`.

Type: String

Valid Values: `ENABLED_WITH_RATE_CONTROL | DISABLED`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryInsights.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/QueryInsights.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryInsights.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/QueryInsights.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryInsights.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/QueryInsights.md")
