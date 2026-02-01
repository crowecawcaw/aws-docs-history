End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# DeleteUtterances

Deletes stored utterances.

Amazon Lex stores the utterances that users send to your bot. Utterances
are stored for 15 days for use with the [GetUtterancesView](API_GetUtterancesView.md "API_GetUtterancesView.md") operation, and then stored indefinitely for use in improving the
ability of your bot to respond to user input.

Use the `DeleteUtterances` operation to manually delete
stored utterances for a specific user. When you use the
`DeleteUtterances` operation, utterances stored for improving
your bot's ability to respond to user input are deleted immediately.
Utterances stored for use with the `GetUtterancesView`
operation are deleted after 15 days.

This operation requires permissions for the
`lex:DeleteUtterances` action.

## Request Syntax

```
DELETE /bots/`botName`/utterances/`userId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[botName](#API_DeleteUtterances_RequestSyntax "#API_DeleteUtterances_RequestSyntax")**

The name of the bot that stored the utterances.

Length Constraints: Minimum length of 2. Maximum length of 50.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[userId](#API_DeleteUtterances_RequestSyntax "#API_DeleteUtterances_RequestSyntax")**

The unique identifier for the user that made the utterances. This
is the user ID that was sent in the [PostContent](API_runtime_PostContent.md "API_runtime_PostContent.md") or [PostText](API_runtime_PostText.md "API_runtime_PostText.md") operation request that contained the
utterance.

Length Constraints: Minimum length of 2. Maximum length of 100.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/cli2/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/boto3/lex-models-2017-04-19/DeleteUtterances.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteUtterances.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteUtterances.md")
