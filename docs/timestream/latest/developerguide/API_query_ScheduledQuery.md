For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ScheduledQuery

Scheduled Query

## Contents

**Arn**

The Amazon Resource Name.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**Name**

The name of the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`

Required: Yes

**State**

State of scheduled query.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

**CreationTime**

The creation time of the scheduled query.

Type: Timestamp

Required: No

**ErrorReportConfiguration**

Configuration for scheduled query error reporting.

Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md "API_query_ErrorReportConfiguration.md") object

Required: No

**LastRunStatus**

Status of the last scheduled query run.

Type: String

Valid Values: `AUTO_TRIGGER_SUCCESS | AUTO_TRIGGER_FAILURE | MANUAL_TRIGGER_SUCCESS | MANUAL_TRIGGER_FAILURE`

Required: No

**NextInvocationTime**

The next time the scheduled query is to be run.

Type: Timestamp

Required: No

**PreviousInvocationTime**

The last time the scheduled query was run.

Type: Timestamp

Required: No

**TargetDestination**

Target data source where final scheduled query result will be written.

Type: [TargetDestination](API_query_TargetDestination.md "API_query_TargetDestination.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQuery.md")
