End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBots

Returns bot information as follows:

- If you provide the `nameContains` field, the
  response includes information for the `$LATEST` version of
  all bots whose name contains the specified string.
- If you don't specify the `nameContains` field, the
  operation returns information about the `$LATEST` version
  of all of your bots.
  This operation requires permission for the `lex:GetBots`
  action.

## Request Syntax

```
GET /bots/?maxResults=`maxResults`&nameContains=`nameContains`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_GetBots_RequestSyntax "#API_GetBots_RequestSyntax")**

The maximum number of bots to return in the response that the
request will return. The default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[nameContains](#API_GetBots_RequestSyntax "#API_GetBots_RequestSyntax")**

Substring to match in bot names. A bot will be returned if any part
of its name matches the substring. For example, "xyz" matches both
"xyzabc" and "abcxyz."

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[nextToken](#API_GetBots_RequestSyntax "#API_GetBots_RequestSyntax")**

A pagination token that fetches the next page of bots. If the
response to this call is truncated, Amazon Lex returns a pagination token in
the response. To fetch the next page of bots, specify the pagination token
in the next request.

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

**[bots](#API_GetBots_ResponseSyntax "#API_GetBots_ResponseSyntax")**

An array of `botMetadata` objects, with one entry for
each bot.

Type: Array of [BotMetadata](API_BotMetadata.md "API_BotMetadata.md") objects

**[nextToken](#API_GetBots_ResponseSyntax "#API_GetBots_ResponseSyntax")**

If the response is truncated, it includes a pagination token that
you can specify in your next request to fetch the next page of bots.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBots.md "../../../goto/cli2/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBots.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBots.md "../../../goto/boto3/lex-models-2017-04-19/GetBots.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBots.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBots.md")
