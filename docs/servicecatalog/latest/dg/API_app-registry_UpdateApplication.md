# UpdateApplication

Updates an existing application with new attributes.

## Request Syntax

```
PATCH /applications/`application` HTTP/1.1
Content-type: application/json

{
   "description": "`string`",
   "name": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_UpdateApplication_RequestSyntax "#API_app-registry_UpdateApplication_RequestSyntax")**

The name, ID, or ARN
of the application
that will be updated.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[description](#API_app-registry_UpdateApplication_RequestSyntax "#API_app-registry_UpdateApplication_RequestSyntax")**

The new description of the application.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[name](#API_app-registry_UpdateApplication_RequestSyntax "#API_app-registry_UpdateApplication_RequestSyntax")**

Deprecated: The new name of the application. The name must be unique in the region in which you are
updating the application. Please do not use this field as we have stopped supporting name updates.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "application": {
      "applicationTag": {
         "***string***" : "***string***"
      },
      "arn": "***string***",
      "creationTime": "***string***",
      "description": "***string***",
      "id": "***string***",
      "lastUpdateTime": "***string***",
      "name": "***string***",
      "tags": {
         "***string***" : "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[application](#API_app-registry_UpdateApplication_ResponseSyntax "#API_app-registry_UpdateApplication_ResponseSyntax")**

The updated information of the application.

Type: [Application](API_app-registry_Application.md "API_app-registry_Application.md") object

## Errors

**ConflictException**

There was a conflict when processing the request (for example, a resource with the given
name already exists within the account).

HTTP Status Code: 409

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource does not exist.

HTTP Status Code: 404

**ThrottlingException**

The maximum number
of API requests
has been exceeded.

**message**

A message associated with the Throttling exception.

**serviceCode**

The originating service code.

HTTP Status Code: 429

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/UpdateApplication.md")
