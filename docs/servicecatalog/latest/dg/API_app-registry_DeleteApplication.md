# DeleteApplication

Deletes an application that is specified either by its application ID, name, or ARN. All associated attribute groups and resources must be disassociated from it before deleting an application.

## Request Syntax

```
DELETE /applications/`application` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_DeleteApplication_RequestSyntax "#API_app-registry_DeleteApplication_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "application": {
      "arn": "***string***",
      "creationTime": "***string***",
      "description": "***string***",
      "id": "***string***",
      "lastUpdateTime": "***string***",
      "name": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[application](#API_app-registry_DeleteApplication_ResponseSyntax "#API_app-registry_DeleteApplication_ResponseSyntax")**

Information about the deleted application.

Type: [ApplicationSummary](API_app-registry_ApplicationSummary.md "API_app-registry_ApplicationSummary.md") object

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/DeleteApplication.md")
