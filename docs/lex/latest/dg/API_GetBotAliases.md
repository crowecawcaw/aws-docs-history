End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBotAliases

Returns a list of aliases for a specified Amazon Lex bot.

This operation requires permissions for the
`lex:GetBotAliases` action.

## Request Syntax

```
GET /bots/`botName`/aliases/?maxResults=`maxResults`&nameContains=`nameContains`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[botName](#API_GetBotAliases_RequestSyntax "#API_GetBotAliases_RequestSyntax")**

The name of the bot.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[maxResults](#API_GetBotAliases_RequestSyntax "#API_GetBotAliases_RequestSyntax")**

The maximum number of aliases to return in the response. The
default is 50. .

Valid Range: Minimum value of 1. Maximum value of 50.

**[nameContains](#API_GetBotAliases_RequestSyntax "#API_GetBotAliases_RequestSyntax")**

Substring to match in bot alias names. An alias will be returned if
any part of its name matches the substring. For example, "xyz" matches
both "xyzabc" and "abcxyz."

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[nextToken](#API_GetBotAliases_RequestSyntax "#API_GetBotAliases_RequestSyntax")**

A pagination token for fetching the next page of aliases. If the
response to this call is truncated, Amazon Lex returns a pagination token in
the response. To fetch the next page of aliases, specify the pagination
token in the next request.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "BotAliases": [
      {
         "botName": "***string***",
         "botVersion": "***string***",
         "checksum": "***string***",
         "conversationLogs": {
            "iamRoleArn": "***string***",
            "logSettings": [
               {
                  "destination": "***string***",
                  "kmsKeyArn": "***string***",
                  "logType": "***string***",
                  "resourceArn": "***string***",
                  "resourcePrefix": "***string***"
               }
            ]
         },
         "createdDate": ***number***,
         "description": "***string***",
         "lastUpdatedDate": ***number***,
         "name": "***string***"
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[BotAliases](#API_GetBotAliases_ResponseSyntax "#API_GetBotAliases_ResponseSyntax")**

An array of `BotAliasMetadata` objects, each describing
a bot alias.

Type: Array of [BotAliasMetadata](API_BotAliasMetadata.md "API_BotAliasMetadata.md") objects

**[nextToken](#API_GetBotAliases_ResponseSyntax "#API_GetBotAliases_ResponseSyntax")**

A pagination token for fetching next page of aliases. If the
response to this call is truncated, Amazon Lex returns a pagination token in
the response. To fetch the next page of aliases, specify the pagination
token in the next request.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBotAliases.md "../../../goto/cli2/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBotAliases.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBotAliases.md "../../../goto/boto3/lex-models-2017-04-19/GetBotAliases.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotAliases.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotAliases.md")
