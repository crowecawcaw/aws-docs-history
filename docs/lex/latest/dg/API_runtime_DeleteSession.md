End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# DeleteSession

Removes session information for a specified bot, alias, and user ID.

## Request Syntax

```
DELETE /bot/`botName`/alias/`botAlias`/user/`userId`/session HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[botAlias](#API_runtime_DeleteSession_RequestSyntax "#API_runtime_DeleteSession_RequestSyntax")**

The alias in use for the bot that contains the session data.

Required: Yes

**[botName](#API_runtime_DeleteSession_RequestSyntax "#API_runtime_DeleteSession_RequestSyntax")**

The name of the bot that contains the session data.

Required: Yes

**[userId](#API_runtime_DeleteSession_RequestSyntax "#API_runtime_DeleteSession_RequestSyntax")**

The identifier of the user associated with the session data.

Length Constraints: Minimum length of 2. Maximum length of 100.

Pattern: `[0-9a-zA-Z._:-]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "botAlias": "***string***",
   "botName": "***string***",
   "sessionId": "***string***",
   "userId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[botAlias](#API_runtime_DeleteSession_ResponseSyntax "#API_runtime_DeleteSession_ResponseSyntax")**

The alias in use for the bot associated with the session data.

Type: String

**[botName](#API_runtime_DeleteSession_ResponseSyntax "#API_runtime_DeleteSession_ResponseSyntax")**

The name of the bot associated with the session data.

Type: String

**[sessionId](#API_runtime_DeleteSession_ResponseSyntax "#API_runtime_DeleteSession_ResponseSyntax")**

The unique identifier for the session.

Type: String

**[userId](#API_runtime_DeleteSession_ResponseSyntax "#API_runtime_DeleteSession_ResponseSyntax")**

The ID of the client application user.

Type: String

Length Constraints: Minimum length of 2. Maximum length of 100.

Pattern: `[0-9a-zA-Z._:-]+`

## Errors

**BadRequestException**

Request validation failed, there is no usable message in the context,
or the bot build failed, is still in progress, or contains unbuilt
changes.

HTTP Status Code: 400

**ConflictException**

Two clients are using the same AWS account, Amazon Lex bot, and user
ID.

HTTP Status Code: 409

**InternalFailureException**

Internal service error. Retry the call.

HTTP Status Code: 500

**LimitExceededException**

Exceeded a limit.

HTTP Status Code: 429

**NotFoundException**

The resource (such as the Amazon Lex bot or an alias) that is referred
to is not found.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/cli2/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/DotNetSDKV4/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForGoV2/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForJavaScriptV3/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForKotlin/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForPHPV3/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for Python](../../../goto/boto3/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/boto3/runtime.lex-2016-11-28/DeleteSession.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/DeleteSession.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/DeleteSession.md")
