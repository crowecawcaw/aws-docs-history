End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# PutBotAlias

Creates an alias for the specified version of the bot or replaces
an alias for the specified bot. To change the version of the bot that the
alias points to, replace the alias. For more information about aliases,
see [Versioning and Aliases](versioning-aliases.md "versioning-aliases.md").

This operation requires permissions for the
`lex:PutBotAlias` action.

## Request Syntax

```
PUT /bots/`botName`/aliases/`name` HTTP/1.1
Content-type: application/json

{
   "botVersion": "`string`",
   "checksum": "`string`",
   "conversationLogs": {
      "iamRoleArn": "`string`",
      "logSettings": [
         {
            "destination": "`string`",
            "kmsKeyArn": "`string`",
            "logType": "`string`",
            "resourceArn": "`string`"
         }
      ]
   },
   "description": "`string`",
   "tags": [
      {
         "key": "`string`",
         "value": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[botName](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

The name of the bot.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[name](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

The name of the alias. The name is _not_ case
sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[botVersion](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

The version of the bot.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: Yes

**[checksum](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

Identifies a specific revision of the `$LATEST`
version.

When you create a new bot alias, leave the `checksum`
field blank. If you specify a checksum you get a
`BadRequestException` exception.

When you want to update a bot alias, set the `checksum`
field to the checksum of the most recent revision of the
`$LATEST` version. If you don't specify the `checksum` field, or if the checksum does not match the
`$LATEST` version, you get a
`PreconditionFailedException` exception.

Type: String

Required: No

**[conversationLogs](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

Settings for conversation logs for the alias.

Type: [ConversationLogsRequest](API_ConversationLogsRequest.md "API_ConversationLogsRequest.md") object

Required: No

**[description](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

A description of the alias.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Required: No

**[tags](#API_PutBotAlias_RequestSyntax "#API_PutBotAlias_RequestSyntax")**

A list of tags to add to the bot alias. You can only add tags when you
create an alias, you can't use the `PutBotAlias` operation to
update the tags on a bot alias. To update tags, use the
`TagResource` operation.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

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
   "name": "***string***",
   "tags": [
      {
         "key": "***string***",
         "value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[botName](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The name of the bot that the alias points to.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

**[botVersion](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The version of the bot that the alias points to.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

**[checksum](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The checksum for the current version of the alias.

Type: String

**[conversationLogs](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The settings that determine how Amazon Lex uses conversation logs for the
alias.

Type: [ConversationLogsResponse](API_ConversationLogsResponse.md "API_ConversationLogsResponse.md") object

**[createdDate](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The date that the bot alias was created.

Type: Timestamp

**[description](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

A description of the alias.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[lastUpdatedDate](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The date that the bot alias was updated. When you create a
resource, the creation date and the last updated date are the
same.

Type: Timestamp

**[name](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

The name of the alias.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[tags](#API_PutBotAlias_ResponseSyntax "#API_PutBotAlias_ResponseSyntax")**

A list of tags associated with a bot.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**ConflictException**

There was a conflict processing the request. Try your request
again.

HTTP Status Code: 409

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**PreconditionFailedException**

The checksum of the resource that you are trying to change does
not match the checksum in the request. Check the resource's checksum and
try again.

HTTP Status Code: 412

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/PutBotAlias.md "../../../goto/cli2/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/PutBotAlias.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForCpp/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/PutBotAlias.md "../../../goto/boto3/lex-models-2017-04-19/PutBotAlias.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/PutBotAlias.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/PutBotAlias.md")
