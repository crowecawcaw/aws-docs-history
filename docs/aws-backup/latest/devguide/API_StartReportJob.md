# StartReportJob

Starts an on-demand report job for the specified report plan.

## Request Syntax

```
POST /audit/report-jobs/`reportPlanName` HTTP/1.1
Content-type: application/json

{
   "IdempotencyToken": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[reportPlanName](#API_StartReportJob_RequestSyntax "#API_StartReportJob_RequestSyntax")**

The unique name of a report plan.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z][_a-zA-Z0-9]*`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[IdempotencyToken](#API_StartReportJob_RequestSyntax "#API_StartReportJob_RequestSyntax")**

A customer-chosen string that you can use to distinguish between otherwise identical
calls to `StartReportJobInput`. Retrying a successful request with the same
idempotency token results in a success message with no action taken.

Type: String

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ReportJobId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ReportJobId](#API_StartReportJob_ResponseSyntax "#API_StartReportJob_ResponseSyntax")**

The identifier of the report job. A unique, randomly generated, Unicode, UTF-8 encoded
string that is at most 1,024 bytes long. The report job ID cannot be edited.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/StartReportJob.md "../../../goto/cli2/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/StartReportJob.md "../../../goto/DotNetSDKV4/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForCpp/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForGoV2/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForJavaV2/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForKotlin/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForPHPV3/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/StartReportJob.md "../../../goto/boto3/backup-2018-11-15/StartReportJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/StartReportJob.md "../../../goto/SdkForRubyV3/backup-2018-11-15/StartReportJob.md")
