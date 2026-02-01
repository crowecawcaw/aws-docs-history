# ListAssociatedResources

Lists all
of the resources
that are associated
with the specified application.
Results are paginated.

###### Note

If you share an application,
and a consumer account associates a tag query
to the application,
all of the users
who can access the application
can also view the tag values
in all accounts
that are associated
with it
using this API.

## Request Syntax

```
GET /applications/`application`/resources?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_ListAssociatedResources_RequestSyntax "#API_app-registry_ListAssociatedResources_RequestSyntax")**

The name, ID, or ARN
of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[maxResults](#API_app-registry_ListAssociatedResources_RequestSyntax "#API_app-registry_ListAssociatedResources_RequestSyntax")**

The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.

Valid Range: Minimum value of 1. Maximum value of 100.

**[nextToken](#API_app-registry_ListAssociatedResources_RequestSyntax "#API_app-registry_ListAssociatedResources_RequestSyntax")**

The token to use to get the next page of results after a previous API call.

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "***string***",
   "resources": [
      {
         "arn": "***string***",
         "name": "***string***",
         "options": [ "***string***" ],
         "resourceDetails": {
            "tagValue": "***string***"
         },
         "resourceType": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_app-registry_ListAssociatedResources_ResponseSyntax "#API_app-registry_ListAssociatedResources_ResponseSyntax")**

The token to use to get the next page of results after a previous API call.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

**[resources](#API_app-registry_ListAssociatedResources_ResponseSyntax "#API_app-registry_ListAssociatedResources_ResponseSyntax")**

Information about the resources.

Type: Array of [ResourceInfo](API_app-registry_ResourceInfo.md "API_app-registry_ResourceInfo.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAssociatedResources.md")
