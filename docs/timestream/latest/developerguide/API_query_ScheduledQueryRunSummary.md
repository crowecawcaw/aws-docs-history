For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ScheduledQueryRunSummary

Run summary for the scheduled query

## Contents

**ErrorReportLocation**

S3 location for error report.

Type: [ErrorReportLocation](API_query_ErrorReportLocation.md "API_query_ErrorReportLocation.md") object

Required: No

**ExecutionStats**

Runtime statistics for a scheduled run.

Type: [ExecutionStats](API_query_ExecutionStats.md "API_query_ExecutionStats.md") object

Required: No

**FailureReason**

Error message for the scheduled query in case of failure. You might have to look at
the error report to get more detailed error reasons.

Type: String

Required: No

**InvocationTime**

InvocationTime for this run. This is the time at which the query is scheduled to run.
Parameter `@scheduled_runtime` can be used in the query to get the value.

Type: Timestamp

Required: No

**QueryInsightsResponse**

Provides various insights and metrics related to the run summary of the scheduled query.

Type: [ScheduledQueryInsightsResponse](API_query_ScheduledQueryInsightsResponse.md "API_query_ScheduledQueryInsightsResponse.md") object

Required: No

**RunStatus**

The status of a scheduled query run.

Type: String

Valid Values: `AUTO_TRIGGER_SUCCESS | AUTO_TRIGGER_FAILURE | MANUAL_TRIGGER_SUCCESS | MANUAL_TRIGGER_FAILURE`

Required: No

**TriggerTime**

The actual time when the query was run.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryRunSummary.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryRunSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryRunSummary.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryRunSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryRunSummary.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryRunSummary.md")
