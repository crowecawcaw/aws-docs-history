# ListAssociatedAttributeGroups

Lists all attribute groups that are associated with specified application. Results are paginated.

## Request Syntax

```
GET /applications/`application`/attribute-groups?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[application](#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax "#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax")**

The name or ID of the application.

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `([-.\w]+)|(arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\d:\d{12}:/applications/[-.\w]+)`

Required: Yes

**[maxResults](#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax "#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax")**

The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.

Valid Range: Minimum value of 1. Maximum value of 100.

**[nextToken](#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax "#API_app-registry_ListAssociatedAttributeGroups_RequestSyntax")**

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
   "attributeGroups": [ "***string***" ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[attributeGroups](#API_app-registry_ListAssociatedAttributeGroups_ResponseSyntax "#API_app-registry_ListAssociatedAttributeGroups_ResponseSyntax")**

A list of attribute group IDs.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[-.\w]+`

**[nextToken](#API_app-registry_ListAssociatedAttributeGroups_ResponseSyntax "#API_app-registry_ListAssociatedAttributeGroups_ResponseSyntax")**

The token to use to get the next page of results after a previous API call.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListAssociatedAttributeGroups.md")
