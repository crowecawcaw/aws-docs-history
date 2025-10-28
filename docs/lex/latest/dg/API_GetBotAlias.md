End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBotAlias

Returns information about an Amazon Lex bot alias. For more information
about aliases, see [Versioning and Aliases](versioning-aliases.md "versioning-aliases.md").

This operation requires permissions for the
`lex:GetBotAlias` action.

## Request Syntax

```
GET /bots/`botName`/aliases/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[botName](#API_GetBotAlias_RequestSyntax "#API_GetBotAlias_RequestSyntax")**

The name of the bot.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[name](#API_GetBotAlias_RequestSyntax "#API_GetBotAlias_RequestSyntax")**

The name of the bot alias. The name is case sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

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
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[botName](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The name of the bot that the alias points to.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[botVersion](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The version of the bot that the alias points to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[checksum](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

Checksum of the bot alias.

Type: String

**[conversationLogs](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The settings that determine how Amazon Lex uses conversation logs for the
alias.

Type: [ConversationLogsResponse](API_ConversationLogsResponse.md "API_ConversationLogsResponse.md") object

**[createdDate](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The date that the bot alias was created.

Type: Timestamp

**[description](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

A description of the bot alias.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[lastUpdatedDate](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The date that the bot alias was updated. When you create a
resource, the creation date and the last updated date are the
same.

Type: Timestamp

**[name](#API_GetBotAlias_ResponseSyntax "#API_GetBotAlias_ResponseSyntax")**

The name of the bot alias.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBotAlias.md "../../../goto/cli2/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBotAlias.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBotAlias.md "../../../goto/boto3/lex-models-2017-04-19/GetBotAlias.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotAlias.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBotAlias.md")
