# CreateSchedule

Creates a new schedule for one or more DataBrew jobs. Jobs can be run at a specific
date and time, or at regular intervals.

## Request Syntax

```
POST /schedules HTTP/1.1
Content-type: application/json

{
   "CronExpression": "`string`",
   "JobNames": [ "`string`" ],
   "Name": "`string`",
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[CronExpression](#API_CreateSchedule_RequestSyntax "#API_CreateSchedule_RequestSyntax")**

The date or dates and time or times when the jobs are to be run. For more information,
see [Cron
expressions](jobs.md "jobs.md") in the _AWS Glue DataBrew Developer
Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: Yes

**[Name](#API_CreateSchedule_RequestSyntax "#API_CreateSchedule_RequestSyntax")**

A unique name for the schedule. Valid characters are alphanumeric (A-Z, a-z, 0-9),
hyphen (-), period (.), and space.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[JobNames](#API_CreateSchedule_RequestSyntax "#API_CreateSchedule_RequestSyntax")**

The name or names of one or more jobs to be run.

Type: Array of strings

Array Members: Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: No

**[Tags](#API_CreateSchedule_RequestSyntax "#API_CreateSchedule_RequestSyntax")**

Metadata tags to apply to this schedule.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_CreateSchedule_ResponseSyntax "#API_CreateSchedule_ResponseSyntax")**

The name of the schedule that was created.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/CreateSchedule.md "../../../goto/cli2/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/CreateSchedule.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForCpp/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForGoV2/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForKotlin/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/CreateSchedule.md "../../../goto/boto3/databrew-2017-07-25/CreateSchedule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateSchedule.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateSchedule.md")
