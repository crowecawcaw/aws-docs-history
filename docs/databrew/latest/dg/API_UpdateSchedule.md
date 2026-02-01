# UpdateSchedule

Modifies the definition of an existing DataBrew schedule.

## Request Syntax

```
PUT /schedules/`name` HTTP/1.1
Content-type: application/json

{
   "CronExpression": "`string`",
   "JobNames": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_UpdateSchedule_RequestSyntax "#API_UpdateSchedule_RequestSyntax")**

The name of the schedule to update.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[CronExpression](#API_UpdateSchedule_RequestSyntax "#API_UpdateSchedule_RequestSyntax")**

The date or dates and time or times when the jobs are to be run. For more information,
see [Cron
expressions](jobs.md "jobs.md") in the _AWS Glue DataBrew Developer
Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: Yes

**[JobNames](#API_UpdateSchedule_RequestSyntax "#API_UpdateSchedule_RequestSyntax")**

The name or names of one or more jobs to be run for this schedule.

Type: Array of strings

Array Members: Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 240.

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

**[Name](#API_UpdateSchedule_ResponseSyntax "#API_UpdateSchedule_ResponseSyntax")**

The name of the schedule that was updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UpdateSchedule.md "../../../goto/cli2/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateSchedule.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForCpp/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UpdateSchedule.md "../../../goto/boto3/databrew-2017-07-25/UpdateSchedule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateSchedule.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateSchedule.md")
