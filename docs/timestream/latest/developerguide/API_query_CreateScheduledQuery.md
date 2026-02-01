For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# CreateScheduledQuery

Create a scheduled query that will be run on your behalf at the configured schedule.
Timestream assumes the execution role provided as part of the
`ScheduledQueryExecutionRoleArn` parameter to run the query. You can use
the `NotificationConfiguration` parameter to configure notification for your
scheduled query operations.

## Request Syntax

```
{
   "ClientToken": "`string`",
   "ErrorReportConfiguration": {
      "S3Configuration": {
         "BucketName": "`string`",
         "EncryptionOption": "`string`",
         "ObjectKeyPrefix": "`string`"
      }
   },
   "KmsKeyId": "`string`",
   "Name": "`string`",
   "NotificationConfiguration": {
      "SnsConfiguration": {
         "TopicArn": "`string`"
      }
   },
   "QueryString": "`string`",
   "ScheduleConfiguration": {
      "ScheduleExpression": "`string`"
   },
   "ScheduledQueryExecutionRoleArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "TargetConfiguration": {
      "TimestreamConfiguration": {
         "DatabaseName": "`string`",
         "DimensionMappings": [
            {
               "DimensionValueType": "`string`",
               "Name": "`string`"
            }
         ],
         "MeasureNameColumn": "`string`",
         "MixedMeasureMappings": [
            {
               "MeasureName": "`string`",
               "MeasureValueType": "`string`",
               "MultiMeasureAttributeMappings": [
                  {
                     "MeasureValueType": "`string`",
                     "SourceColumn": "`string`",
                     "TargetMultiMeasureAttributeName": "`string`"
                  }
               ],
               "SourceColumn": "`string`",
               "TargetMeasureName": "`string`"
            }
         ],
         "MultiMeasureMappings": {
            "MultiMeasureAttributeMappings": [
               {
                  "MeasureValueType": "`string`",
                  "SourceColumn": "`string`",
                  "TargetMultiMeasureAttributeName": "`string`"
               }
            ],
            "TargetMultiMeasureName": "`string`"
         },
         "TableName": "`string`",
         "TimeColumn": "`string`"
      }
   }
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ClientToken](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

Using a ClientToken makes the call to CreateScheduledQuery idempotent, in other words,
making the same request repeatedly will produce the same result. Making multiple
identical CreateScheduledQuery requests has the same effect as making a single request.

- If CreateScheduledQuery is called without a `ClientToken`, the
  Query SDK generates a `ClientToken` on your behalf.
- After 8 hours, any request with the same `ClientToken` is treated
  as a new request.

Type: String

Length Constraints: Minimum length of 32. Maximum length of 128.

Required: No

**[ErrorReportConfiguration](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

Configuration for error reporting. Error reports will be generated when a problem is
encountered when writing the query results.

Type: [ErrorReportConfiguration](API_query_ErrorReportConfiguration.md "API_query_ErrorReportConfiguration.md") object

Required: Yes

**[KmsKeyId](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

The Amazon KMS key used to encrypt the scheduled query resource, at-rest. If the
Amazon KMS key is not specified, the scheduled query resource will be encrypted with a
Timestream owned Amazon KMS key. To specify a KMS key, use the key ID, key ARN, alias
name, or alias ARN. When using an alias name, prefix the name with
_alias/_

If ErrorReportConfiguration uses `SSE_KMS` as encryption type, the same
KmsKeyId is used to encrypt the error report at rest.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**[Name](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

Name of the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[a-zA-Z0-9|!\-_*'\(\)]([a-zA-Z0-9]|[!\-_*'\(\)\/.])+`

Required: Yes

**[NotificationConfiguration](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

Notification configuration for the scheduled query. A notification is sent by
Timestream when a query run finishes, when the state is updated or when you delete it.

Type: [NotificationConfiguration](API_query_NotificationConfiguration.md "API_query_NotificationConfiguration.md") object

Required: Yes

**[QueryString](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

The query string to run. Parameter names can be specified in the query string
`@` character followed by an identifier. The named Parameter
`@scheduled_runtime` is reserved and can be used in the query to get the
time at which the query is scheduled to run.

The timestamp calculated according to the ScheduleConfiguration parameter, will be the
value of `@scheduled_runtime` paramater for each query run. For example,
consider an instance of a scheduled query executing on 2021-12-01 00:00:00. For this
instance, the `@scheduled_runtime` parameter is initialized to the timestamp
2021-12-01 00:00:00 when invoking the query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 262144.

Required: Yes

**[ScheduleConfiguration](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

The schedule configuration for the query.

Type: [ScheduleConfiguration](API_query_ScheduleConfiguration.md "API_query_ScheduleConfiguration.md") object

Required: Yes

**[ScheduledQueryExecutionRoleArn](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

The ARN for the IAM role that Timestream will assume when running the scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: Yes

**[Tags](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

A list of key-value pairs to label the scheduled query.

Type: Array of [Tag](API_query_Tag.md "API_query_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

**[TargetConfiguration](#API_query_CreateScheduledQuery_RequestSyntax "#API_query_CreateScheduledQuery_RequestSyntax")**

Configuration used for writing the result of a query.

Type: [TargetConfiguration](API_query_TargetConfiguration.md "API_query_TargetConfiguration.md") object

Required: No

## Response Syntax

```
{
   "Arn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Arn](#API_query_CreateScheduledQuery_ResponseSyntax "#API_query_CreateScheduledQuery_ResponseSyntax")**

ARN for the created scheduled query.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have the necessary permissions to access the account settings.

HTTP Status Code: 400

**ConflictException**

Unable to poll results for a cancelled query.

HTTP Status Code: 400

**InternalServerException**

An internal server error occurred while processing the request.

HTTP Status Code: 400

**InvalidEndpointException**

The requested endpoint is invalid.

HTTP Status Code: 400

**ServiceQuotaExceededException**

You have exceeded the service quota.

HTTP Status Code: 400

**ThrottlingException**

The request was throttled due to excessive requests.

HTTP Status Code: 400

**ValidationException**

Invalid or malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/cli2/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/DotNetSDKV4/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForCpp/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForGoV2/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForJavaV2/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForJavaScriptV3/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForKotlin/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForPHPV3/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for Python](../../../goto/boto3/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/boto3/timestream-query-2018-11-01/CreateScheduledQuery.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-query-2018-11-01/CreateScheduledQuery.md "../../../goto/SdkForRubyV3/timestream-query-2018-11-01/CreateScheduledQuery.md")
