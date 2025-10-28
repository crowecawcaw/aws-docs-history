End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBuiltinIntent

Returns information about a built-in intent.

This operation requires permission for the
`lex:GetBuiltinIntent` action.

## Request Syntax

```
GET /builtins/intents/`signature` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[signature](#API_GetBuiltinIntent_RequestSyntax "#API_GetBuiltinIntent_RequestSyntax")**

The unique identifier for a built-in intent. To find the signature
for an intent, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents "https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents") in the _Alexa Skills
Kit_.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "signature": "***string***",
   "slots": [
      {
         "name": "***string***"
      }
   ],
   "supportedLocales": [ "***string***" ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[signature](#API_GetBuiltinIntent_ResponseSyntax "#API_GetBuiltinIntent_ResponseSyntax")**

The unique identifier for a built-in intent.

Type: String

**[slots](#API_GetBuiltinIntent_ResponseSyntax "#API_GetBuiltinIntent_ResponseSyntax")**

An array of `BuiltinIntentSlot` objects, one entry for
each slot type in the intent.

Type: Array of [BuiltinIntentSlot](API_BuiltinIntentSlot.md "API_BuiltinIntentSlot.md") objects

**[supportedLocales](#API_GetBuiltinIntent_ResponseSyntax "#API_GetBuiltinIntent_ResponseSyntax")**

A list of locales that the intent supports.

Type: Array of strings

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/cli2/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/boto3/lex-models-2017-04-19/GetBuiltinIntent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBuiltinIntent.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBuiltinIntent.md")
