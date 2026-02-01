# StartJobRun

Runs a DataBrew job.

## Request Syntax

```
POST /jobs/`name`/startJobRun HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_StartJobRun_RequestSyntax "#API_StartJobRun_RequestSyntax")**

The name of the job to be run.

Length Constraints: Minimum length of 1. Maximum length of 240.

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

**[RunId](#API_StartJobRun_ResponseSyntax "#API_StartJobRun_ResponseSyntax")**

A system-generated identifier for this particular job run.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/StartJobRun.md "../../../goto/cli2/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/StartJobRun.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForCpp/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForGoV2/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForKotlin/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/StartJobRun.md "../../../goto/boto3/databrew-2017-07-25/StartJobRun.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/StartJobRun.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/StartJobRun.md")
