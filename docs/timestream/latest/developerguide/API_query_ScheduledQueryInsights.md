For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ScheduledQueryInsights

Encapsulates settings for enabling `QueryInsights` on an `ExecuteScheduledQueryRequest`.

## Contents

**Mode**

Provides the following modes to enable `ScheduledQueryInsights`:

- `ENABLED_WITH_RATE_CONTROL` – Enables `ScheduledQueryInsights` for the queries being processed. This mode also includes a rate control mechanism, which limits the `QueryInsights` feature to 1 query per second (QPS).
- `DISABLED` – Disables `ScheduledQueryInsights`.

Type: String

Valid Values: `ENABLED_WITH_RATE_CONTROL | DISABLED`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryInsights.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryInsights.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryInsights.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryInsights.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryInsights.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryInsights.md")
