End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# CodeHook

Specifies a Lambda function that verifies requests to a bot or
fulfills the user's request to a bot..

## Contents

**messageVersion**

The version of the request-response that you want Amazon Lex to use to
invoke your Lambda function. For more information, see [Using Lambda Functions](using-lambda.md "using-lambda.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 5.

Required: Yes

**uri**

The Amazon Resource Name (ARN) of the Lambda function.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:aws[a-zA-Z-]*:lambda:[a-z]+-[a-z]+(-[a-z]+)*-[0-9]:[0-9]{12}:function:[a-zA-Z0-9-_]+(\/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})?(:[a-zA-Z0-9-_]+)?`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/CodeHook.md "../../../goto/SdkForCpp/lex-models-2017-04-19/CodeHook.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/CodeHook.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/CodeHook.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/CodeHook.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/CodeHook.md")
