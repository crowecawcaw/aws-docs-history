# GetApplication

Retrieves metadata information
about one
of your applications.
The application can be specified
by its ARN, ID, or name
(which is unique
within one account
in one region
at a given point
in time).
Specify
by ARN or ID
in automated workflows
if you want
to make sure
that the exact same application is returned or a `ResourceNotFoundException` is thrown,
avoiding the ABA addressing problem.

## Request Syntax

```
GET /applications/`application` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_GetApplication_RequestSyntax "#API_app-registry_GetApplication_RequestSyntax")**

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
   "applicationTag": {
      "***string***" : "***string***"
   },
   "arn": "***string***",
   "associatedResourceCount": ***number***,
   "creationTime": "***string***",
   "description": "***string***",
   "id": "***string***",
   "integrations": {
      "applicationTagResourceGroup": {
         "arn": "***string***",
         "errorMessage": "***string***",
         "state": "***string***"
      },
      "resourceGroup": {
         "arn": "***string***",
         "errorMessage": "***string***",
         "state": "***string***"
      }
   },
   "lastUpdateTime": "***string***",
   "name": "***string***",
   "tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applicationTag](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

A key-value pair that identifies an associated resource.

Type: String to string map

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

**[arn](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The Amazon resource name (ARN) that specifies the application across services.

Type: String

Pattern: `arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[a-z0-9]+`

**[associatedResourceCount](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The number of top-level resources that were registered as part of this application.

Type: Integer

Valid Range: Minimum value of 0.

**[creationTime](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The ISO-8601 formatted timestamp of the moment when the application was created.

Type: Timestamp

**[description](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The description of the application.

Type: String

Length Constraints: Maximum length of 1024.

**[id](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The identifier of the application.

Type: String

Length Constraints: Fixed length of 26.

Pattern: `[a-z0-9]+`

**[integrations](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The information
about the integration
of the application
with other services,
such as
AWS Resource Groups.

Type: [Integrations](API_app-registry_Integrations.md "API_app-registry_Integrations.md") object

**[lastUpdateTime](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The ISO-8601 formatted timestamp of the moment when the application was last updated.

Type: Timestamp

**[name](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

The name of the application. The name must be unique in the region in which you are creating the application.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

**[tags](#API_app-registry_GetApplication_ResponseSyntax "#API_app-registry_GetApplication_ResponseSyntax")**

Key-value pairs associated with the application.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 50 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Key Pattern: `^([\p{L}\p{Z}\p{N}_.:\/=+\-@]*)$`

Value Length Constraints: Maximum length of 256.

Value Pattern: `[\p{L}\p{Z}\p{N}_.:/=+\-@]*`

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

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetApplication.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetApplication.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetApplication.md")
