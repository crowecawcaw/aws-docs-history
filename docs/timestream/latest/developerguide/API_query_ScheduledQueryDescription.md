For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ScheduledQueryDescription

Structure that describes scheduled query.

## Contents

**Arn**

Scheduled query ARN.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**Name**

Name of the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`

Required: Yes

**NotificationConfiguration**

Notification configuration.

Type: [NotificationConfiguration](API_query_NotificationConfiguration.md "API_query_NotificationConfiguration.md") object

Required: Yes

**QueryString**

The query to be run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 262144.

Required: Yes

**ScheduleConfiguration**

Schedule configuration.

Type: [ScheduleConfiguration](API_query_ScheduleConfiguration.md "API_query_ScheduleConfiguration.md") object

Required: Yes

**State**

State of the scheduled query.

Type: String

Valid Values: `ENABLED | DISABLED`

Required: Yes

**CreationTime**

Creation time of the scheduled query.

Type: Timestamp

Required: No

**ErrorReportConfiguration**

Error-reporting configuration for the scheduled query.

Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md "API_query_ErrorReportConfiguration.md") object

Required: No

**KmsKeyId**

A customer provided KMS key used to encrypt the scheduled query resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**LastRunSummary**

Runtime summary for the last scheduled query run.

Type: [ScheduledQueryRunSummary](API_query_ScheduledQueryRunSummary.md "API_query_ScheduledQueryRunSummary.md") object

Required: No

**NextInvocationTime**

The next time the scheduled query is scheduled to run.

Type: Timestamp

Required: No

**PreviousInvocationTime**

Last time the query was run.

Type: Timestamp

Required: No

**RecentlyFailedRuns**

Runtime summary for the last five failed scheduled query runs.

Type: Array of [ScheduledQueryRunSummary](API_query_ScheduledQueryRunSummary.md "API_query_ScheduledQueryRunSummary.md") objects

Required: No

**ScheduledQueryExecutionRoleArn**

IAM role that Timestream uses to run the schedule query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**TargetConfiguration**

Scheduled query target store configuration.

Type: [TargetConfiguration](API_query_TargetConfiguration.md "API_query_TargetConfiguration.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryDescription.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/ScheduledQueryDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryDescription.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/ScheduledQueryDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryDescription.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/ScheduledQueryDescription.md")
