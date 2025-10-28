End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# DeleteBot

Deletes all versions of the bot, including the `$LATEST`
version. To delete a specific version of the bot, use the [DeleteBotVersion](API_DeleteBotVersion.md "API_DeleteBotVersion.md") operation. The `DeleteBot`
operation doesn't immediately remove the bot schema. Instead, it is marked
for deletion and removed later.

Amazon Lex stores utterances indefinitely for improving the ability of
your bot to respond to user inputs. These utterances are not removed when
the bot is deleted. To remove the utterances, use the [DeleteUtterances](API_DeleteUtterances.md "API_DeleteUtterances.md") operation.

If a bot has an alias, you can't delete it. Instead, the
`DeleteBot` operation returns a
`ResourceInUseException` exception that includes a reference
to the alias that refers to the bot. To remove the reference to the bot,
delete the alias. If you get the same exception again, delete the
referring alias until the `DeleteBot` operation is
successful.

This operation requires permissions for the
`lex:DeleteBot` action.

## Request Syntax

```
DELETE /bots/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DeleteBot_RequestSyntax "#API_DeleteBot_RequestSyntax")**

The name of the bot. The name is case sensitive.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

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

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

**ResourceInUseException**

The resource that you are attempting to delete is referred to by
another resource. Use this information to remove references to the
resource that you are trying to delete.

The body of the exception contains a JSON object that describes the
resource.

`{ "resourceType": BOT | BOTALIAS | BOTCHANNEL |
 INTENT,`

`"resourceReference": {`

`"name": *string*, "version":
 *string* } }`

**exampleReference**

Describes the resource that refers to the resource that you are
attempting to delete. This object is returned as part of the
`ResourceInUseException` exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/DeleteBot.md "../../../goto/cli2/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/DeleteBot.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/DeleteBot.md "../../../goto/boto3/lex-models-2017-04-19/DeleteBot.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteBot.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteBot.md")
