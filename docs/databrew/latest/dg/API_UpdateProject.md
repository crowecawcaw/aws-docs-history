# UpdateProject

Modifies the definition of an existing DataBrew project.

## Request Syntax

```
PUT /projects/`name` HTTP/1.1
Content-type: application/json

{
   "RoleArn": "`string`",
   "Sample": {
      "Size": `number`,
      "Type": "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_UpdateProject_RequestSyntax "#API_UpdateProject_RequestSyntax")**

The name of the project to be updated.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[RoleArn](#API_UpdateProject_RequestSyntax "#API_UpdateProject_RequestSyntax")**

The Amazon Resource Name (ARN) of the IAM role to be assumed for this request.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**[Sample](#API_UpdateProject_RequestSyntax "#API_UpdateProject_RequestSyntax")**

Represents the sample size and sampling type for DataBrew to use for interactive data
analysis.

Type: [Sample](API_Sample.md "API_Sample.md") object

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "LastModifiedDate": ***number***,
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_UpdateProject_ResponseSyntax "#API_UpdateProject_ResponseSyntax")**

The name of the project that you updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[LastModifiedDate](#API_UpdateProject_ResponseSyntax "#API_UpdateProject_ResponseSyntax")**

The date and time that the project was last modified.

Type: Timestamp

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UpdateProject.md "../../../goto/cli2/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateProject.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForCpp/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UpdateProject.md "../../../goto/boto3/databrew-2017-07-25/UpdateProject.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateProject.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateProject.md")
