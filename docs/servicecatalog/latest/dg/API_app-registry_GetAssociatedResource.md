# GetAssociatedResource

Gets the resource associated with the application.

## Request Syntax

```
GET /applications/`application`/resources/`resourceType`/`resource`?maxResults=`maxResults`&nextToken=`nextToken`&resourceTagStatus=`resourceTagStatus` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[maxResults](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

The maximum number of results to return. If the parameter is omitted, it defaults to 25. The value is optional.

Valid Range: Minimum value of 1. Maximum value of 100.

**[nextToken](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

A unique pagination token for each page of results.
Make the call again with the returned token to retrieve the next page of results.

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

**[resource](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

The name or ID of the resource associated with the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `\S+`

Required: Yes

**[resourceTagStatus](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

States whether an application tag is applied, not applied, in the process of being applied, or skipped.

Array Members: Minimum number of 1 item. Maximum number of 4 items.

Valid Values: `SUCCESS | FAILED | IN_PROGRESS | SKIPPED`

**[resourceType](#API_app-registry_GetAssociatedResource_RequestSyntax "#API_app-registry_GetAssociatedResource_RequestSyntax")**

The type of resource associated with the application.

Valid Values: `CFN_STACK | RESOURCE_TAG_VALUE`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "applicationTagResult": {
      "applicationTagStatus": "***string***",
      "errorMessage": "***string***",
      "nextToken": "***string***",
      "resources": [
         {
            "errorMessage": "***string***",
            "resourceArn": "***string***",
            "resourceType": "***string***",
            "status": "***string***"
         }
      ]
   },
   "options": [ "***string***" ],
   "resource": {
      "arn": "***string***",
      "associationTime": "***string***",
      "integrations": {
         "resourceGroup": {
            "arn": "***string***",
            "errorMessage": "***string***",
            "state": "***string***"
         }
      },
      "name": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applicationTagResult](#API_app-registry_GetAssociatedResource_ResponseSyntax "#API_app-registry_GetAssociatedResource_ResponseSyntax")**

The result of the application that's tag applied to a resource.

Type: [ApplicationTagResult](API_app-registry_ApplicationTagResult.md "API_app-registry_ApplicationTagResult.md") object

**[options](#API_app-registry_GetAssociatedResource_ResponseSyntax "#API_app-registry_GetAssociatedResource_ResponseSyntax")**

Determines whether an application tag is applied or skipped.

Type: Array of strings

Valid Values: `APPLY_APPLICATION_TAG | SKIP_APPLICATION_TAG`

**[resource](#API_app-registry_GetAssociatedResource_ResponseSyntax "#API_app-registry_GetAssociatedResource_ResponseSyntax")**

The resource associated with the application.

Type: [Resource](API_app-registry_Resource.md "API_app-registry_Resource.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetAssociatedResource.md")
