# StopJobRun

Stops a particular run of a job.

## Request Syntax

```
POST /jobs/`name`/jobRun/`runId`/stopJobRun HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_StopJobRun_RequestSyntax "#API_StopJobRun_RequestSyntax")**

The name of the job to be stopped.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

**[runId](#API_StopJobRun_RequestSyntax "#API_StopJobRun_RequestSyntax")**

The ID of the job run to be stopped.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "RunId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RunId](#API_StopJobRun_ResponseSyntax "#API_StopJobRun_ResponseSyntax")**

The ID of the job run that you stopped.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/StopJobRun.md "../../../goto/cli2/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/StopJobRun.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForCpp/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForGoV2/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForKotlin/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/StopJobRun.md "../../../goto/boto3/databrew-2017-07-25/StopJobRun.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/StopJobRun.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/StopJobRun.md")
