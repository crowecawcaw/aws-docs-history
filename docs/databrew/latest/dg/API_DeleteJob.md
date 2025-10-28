# DeleteJob

Deletes the specified DataBrew job.

## Request Syntax

```
DELETE /jobs/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DeleteJob_RequestSyntax "#API_DeleteJob_RequestSyntax")**

The name of the job to be deleted.

Length Constraints: Minimum length of 1. Maximum length of 240.

Required: Yes

## Request Body

The request does not have a request body.

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

**[Name](#API_DeleteJob_ResponseSyntax "#API_DeleteJob_ResponseSyntax")**

The name of the job that you deleted.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 240.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DeleteJob.md "../../../goto/cli2/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/DeleteJob.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForCpp/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DeleteJob.md "../../../goto/boto3/databrew-2017-07-25/DeleteJob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DeleteJob.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DeleteJob.md")
