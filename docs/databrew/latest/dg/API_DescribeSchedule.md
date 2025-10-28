# DescribeSchedule

Returns the definition of a specific DataBrew schedule.

## Request Syntax

```
GET /schedules/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeSchedule_RequestSyntax "#API_DescribeSchedule_RequestSyntax")**

The name of the schedule to be described.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": ***number***,
   "CreatedBy": "***string***",
   "CronExpression": "***string***",
   "JobNames": [ "***string***" ],
   "LastModifiedBy": "***string***",
   "LastModifiedDate": ***number***,
   "Name": "***string***",
   "ResourceArn": "***string***",
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The name of the schedule.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[CreateDate](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The date and time that the schedule was created.

Type: Timestamp

**[CreatedBy](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The identifier (user name) of the user who created the schedule.

Type: String

**[CronExpression](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The date or dates and time or times when the jobs are to be run for the schedule. For
more information, see [Cron expressions](jobs.md "jobs.md") in the
_AWS Glue DataBrew Developer Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

**[JobNames](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The name or names of one or more jobs to be run by using the schedule.

Type: Array of strings

Array Members: Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 240.

**[LastModifiedBy](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The identifier (user name) of the user who last modified the schedule.

Type: String

**[LastModifiedDate](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The date and time that the schedule was last modified.

Type: Timestamp

**[ResourceArn](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

The Amazon Resource Name (ARN) of the schedule.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[Tags](#API_DescribeSchedule_ResponseSyntax "#API_DescribeSchedule_ResponseSyntax")**

Metadata tags associated with this schedule.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeSchedule.md "../../../goto/cli2/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeSchedule.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeSchedule.md "../../../goto/boto3/databrew-2017-07-25/DescribeSchedule.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeSchedule.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeSchedule.md")
