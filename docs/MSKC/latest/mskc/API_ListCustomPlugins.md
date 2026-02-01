# ListCustomPlugins

Returns a list of all of the custom plugins in this account and Region.

## Request Syntax

```
GET /v1/custom-plugins?maxResults=`maxResults`&namePrefix=`namePrefix`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_ListCustomPlugins_RequestSyntax "#API_ListCustomPlugins_RequestSyntax")**

The maximum number of custom plugins to list in one response.

Valid Range: Minimum value of 1. Maximum value of 100.

**[namePrefix](#API_ListCustomPlugins_RequestSyntax "#API_ListCustomPlugins_RequestSyntax")**

Lists custom plugin names that start with the specified text string.

**[nextToken](#API_ListCustomPlugins_RequestSyntax "#API_ListCustomPlugins_RequestSyntax")**

If the response of a ListCustomPlugins operation is truncated, it will include a
NextToken. Send this NextToken in a subsequent request to continue listing from where the
previous operation left off.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "customPlugins": [
      {
         "creationTime": "***string***",
         "customPluginArn": "***string***",
         "customPluginState": "***string***",
         "description": "***string***",
         "latestRevision": {
            "contentType": "***string***",
            "creationTime": "***string***",
            "description": "***string***",
            "fileDescription": {
               "fileMd5": "***string***",
               "fileSize": ***number***
            },
            "location": {
               "s3Location": {
                  "bucketArn": "***string***",
                  "fileKey": "***string***",
                  "objectVersion": "***string***"
               }
            },
            "revision": ***number***
         },
         "name": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[customPlugins](#API_ListCustomPlugins_ResponseSyntax "#API_ListCustomPlugins_ResponseSyntax")**

An array of custom plugin descriptions.

Type: Array of [CustomPluginSummary](API_CustomPluginSummary.md "API_CustomPluginSummary.md") objects

**[nextToken](#API_ListCustomPlugins_ResponseSyntax "#API_ListCustomPlugins_ResponseSyntax")**

If the response of a ListCustomPlugins operation is truncated, it will include a
NextToken. Send this NextToken in a subsequent request to continue listing from where the
previous operation left off.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**BadRequestException**

HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then
retry it.

HTTP Status Code: 400

**ForbiddenException**

HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your
request.

HTTP Status Code: 403

**InternalServerErrorException**

HTTP Status Code 500: Unexpected internal server error. Retrying your request might
resolve the issue.

HTTP Status Code: 500

**NotFoundException**

HTTP Status Code 404: Resource not found due to incorrect input. Correct your request
and then retry it.

HTTP Status Code: 404

**ServiceUnavailableException**

HTTP Status Code 503: Service Unavailable. Retrying your request in some time might
resolve the issue.

HTTP Status Code: 503

**TooManyRequestsException**

HTTP Status Code 429: Limit exceeded. Resource limit reached.

HTTP Status Code: 429

**UnauthorizedException**

HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be
validated.

HTTP Status Code: 401

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/cli2/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/DotNetSDKV4/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForGoV2/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForKotlin/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForPHPV3/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for Python](../../../goto/boto3/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/boto3/kafkaconnect-2021-09-14/ListCustomPlugins.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ListCustomPlugins.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ListCustomPlugins.md")
