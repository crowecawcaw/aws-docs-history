End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBotVersions

Gets information about all of the versions of a bot.

The `GetBotVersions` operation returns a
`BotMetadata` object for each version of a bot. For example,
if a bot has three numbered versions, the `GetBotVersions`
operation returns four `BotMetadata` objects in the response,
one for each numbered version and one for the `$LATEST`
version.

The `GetBotVersions` operation always returns at least
one version, the `$LATEST` version.

This operation requires permissions for the
`lex:GetBotVersions` action.

## Request Syntax

```
GET /bots/`name`/versions/?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_GetBotVersions_RequestSyntax "#API_GetBotVersions_RequestSyntax")**

The maximum number of bot versions to return in the response. The
default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[name](#API_GetBotVersions_RequestSyntax "#API_GetBotVersions_RequestSyntax")**

The name of the bot for which versions should be
returned.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[nextToken](#API_GetBotVersions_RequestSyntax "#API_GetBotVersions_RequestSyntax")**

A pagination token for fetching the next page of bot versions. If
the response to this call is truncated, Amazon Lex returns a pagination token
in the response. To fetch the next page of versions, specify the
pagination token in the next request.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "bots": [
      {
         "createdDate": ***number***,
         "description": "***string***",
         "lastUpdatedDate": ***number***,
         "name": "***string***",
         "status": "***string***",
         "version": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[bots](#API_GetBotVersions_ResponseSyntax "#API_GetBotVersions_ResponseSyntax")**

An array of `BotMetadata` objects, one for each numbered
version of the bot plus one for the `$LATEST`
version.

Type: Array of [BotMetadata](API_BotMetadata.md "API_BotMetadata.md") objects

**[nextToken](#API_GetBotVersions_ResponseSyntax "#API_GetBotVersions_ResponseSyntax")**

A pagination token for fetching the next page of bot versions. If
the response to this call is truncated, Amazon Lex returns a pagination token
in the response. To fetch the next page of versions, specify the
pagination token in the next request.

Type: String

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBotVersions.md "../../../goto/cli2/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBotVersions.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBotVersions.md "../../../goto/boto3/lex-models-2017-04-19/GetBotVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotVersions.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotVersions.md")
