AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# NotifyMigrationTaskState

Notifies Migration Hub of the current status, progress, or other detail regarding a
migration task. This API has the following traits:

- Migration tools will call the `NotifyMigrationTaskState` API to share
  the latest progress and status.
- `MigrationTaskName` is used for addressing updates to the correct
  target.
- `ProgressUpdateStream` is used for access control and to provide a
  namespace for each migration tool.

## Request Syntax

```
{
   "DryRun": `boolean`,
   "MigrationTaskName": "`string`",
   "NextUpdateSeconds": `number`,
   "ProgressUpdateStream": "`string`",
   "Task": {
      "ProgressPercent": `number`,
      "Status": "`string`",
      "StatusDetail": "`string`"
   },
   "UpdateDateTime": `number`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DryRun](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

Optional boolean flag to indicate whether any effect should take place. Used to test if
the caller has permission to make the call.

Type: Boolean

Required: No

**[MigrationTaskName](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

Unique identifier that references the migration task. _Do not store personal
data in this field._

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[^:|]+`

Required: Yes

**[NextUpdateSeconds](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

Number of seconds after the UpdateDateTime within which the Migration Hub can expect an
update. If Migration Hub does not receive an update within the specified interval, then the
migration task will be considered stale.

Type: Integer

Valid Range: Minimum value of 0.

Required: Yes

**[ProgressUpdateStream](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

The name of the ProgressUpdateStream.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[^/:|\000-\037]+`

Required: Yes

**[Task](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

Information about the task's progress and status.

Type: [Task](API_Task.md "API_Task.md") object

Required: Yes

**[UpdateDateTime](#API_NotifyMigrationTaskState_RequestSyntax "#API_NotifyMigrationTaskState_RequestSyntax")**

The timestamp when the task was gathered.

Type: Timestamp

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**AccessDeniedException**

You do not have sufficient access to perform this action.

HTTP Status Code: 400

**DryRunOperation**

Exception raised to indicate a successfully authorized action when the
`DryRun` flag is set to "true".

HTTP Status Code: 400

**HomeRegionNotSetException**

The home region is not set. Set the home region to continue.

HTTP Status Code: 400

**InternalServerError**

Exception raised when an internal, configuration, or dependency error is
encountered.

HTTP Status Code: 500

**InvalidInputException**

Exception raised when the provided input violates a policy constraint or is entered in
the wrong format or data type.

HTTP Status Code: 400

**ResourceNotFoundException**

Exception raised when the request references a resource (Application Discovery Service
configuration, update stream, migration task, etc.) that does not exist in Application
Discovery Service (Application Discovery Service) or in Migration Hub's repository.

HTTP Status Code: 400

**ServiceUnavailableException**

Exception raised when there is an internal, configuration, or dependency error
encountered.

HTTP Status Code: 500

**ThrottlingException**

The request was denied due to request throttling.

**Message**

A message that provides information about the exception.

**RetryAfterSeconds**

The number of seconds the caller should wait before retrying.

HTTP Status Code: 400

**UnauthorizedOperation**

Exception raised to indicate a request was not authorized when the `DryRun`
flag is set to "true".

HTTP Status Code: 400

## Examples

### Notify the migration task state to Migration Hub

The following example communicates the latest progress and updates to Migration
Hub using the values passed to the required parameters `MigrationTaskName`
and `ProgressUpdateStream` to tag the correct target and its migration
tool. The other parameters in the example are also required to provide details of the
task state.

#### Sample Request

```

{
    "MigrationTaskName": "sms-12de3cf1a",
    "NextUpdateSeconds": 60,
    "ProgressUpdateStream": "SMS",
    "Task": {
       "ProgressPercent": 77,
       "Status": "IN_PROGRESS",
       "StatusDetail": "Migration: Copying image data"
    },
    "UpdateDateTime": 1493660853
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/cli2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/DotNetSDKV4/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForCpp/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForGoV2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForJavaV2/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForJavaScriptV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForKotlin/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForPHPV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for Python](../../../goto/boto3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/boto3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md "../../../goto/SdkForRubyV3/AWSMigrationHub-2017-05-31/NotifyMigrationTaskState.md")
