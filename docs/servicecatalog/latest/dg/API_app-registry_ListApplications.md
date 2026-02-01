# ListApplications

Retrieves a list of all of your applications. Results are paginated.

## Request Syntax

```
GET /applications?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_app-registry_ListApplications_RequestSyntax "#API_app-registry_ListApplications_RequestSyntax")**

The upper bound of the number of results to return (cannot exceed 25). If this parameter is omitted, it defaults to 25. This value is optional.

Valid Range: Minimum value of 1. Maximum value of 100.

**[nextToken](#API_app-registry_ListApplications_RequestSyntax "#API_app-registry_ListApplications_RequestSyntax")**

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
   "applications": [
      {
         "arn": "***string***",
         "creationTime": "***string***",
         "description": "***string***",
         "id": "***string***",
         "lastUpdateTime": "***string***",
         "name": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[applications](#API_app-registry_ListApplications_ResponseSyntax "#API_app-registry_ListApplications_ResponseSyntax")**

This list of applications.

Type: Array of [ApplicationSummary](API_app-registry_ApplicationSummary.md "API_app-registry_ApplicationSummary.md") objects

**[nextToken](#API_app-registry_ListApplications_ResponseSyntax "#API_app-registry_ListApplications_ResponseSyntax")**

The token to use to get the next page of results after a previous API call.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2024.

Pattern: `[A-Za-z0-9+/=]+`

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/DotNetSDKV4/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/ListApplications.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListApplications.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/ListApplications.md")
