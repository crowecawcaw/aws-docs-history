End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetBuiltinIntents

Gets a list of built-in intents that meet the specified
criteria.

This operation requires permission for the
`lex:GetBuiltinIntents` action.

## Request Syntax

```
GET /builtins/intents/?locale=`locale`&maxResults=`maxResults`&nextToken=`nextToken`&signatureContains=`signatureContains` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[locale](#API_GetBuiltinIntents_RequestSyntax "#API_GetBuiltinIntents_RequestSyntax")**

A list of locales that the intent supports.

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

**[maxResults](#API_GetBuiltinIntents_RequestSyntax "#API_GetBuiltinIntents_RequestSyntax")**

The maximum number of intents to return in the response. The
default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[nextToken](#API_GetBuiltinIntents_RequestSyntax "#API_GetBuiltinIntents_RequestSyntax")**

A pagination token that fetches the next page of intents. If this
API call is truncated, Amazon Lex returns a pagination token in the response.
To fetch the next page of intents, use the pagination token in the next
request.

**[signatureContains](#API_GetBuiltinIntents_RequestSyntax "#API_GetBuiltinIntents_RequestSyntax")**

Substring to match in built-in intent signatures. An intent will be
returned if any part of its signature matches the substring. For example,
"xyz" matches both "xyzabc" and "abcxyz." To find the signature for an
intent, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents "https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents") in the _Alexa Skills
Kit_.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "intents": [
      {
         "signature": "***string***",
         "supportedLocales": [ "***string***" ]
      }
   ],
   "nextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[intents](#API_GetBuiltinIntents_ResponseSyntax "#API_GetBuiltinIntents_ResponseSyntax")**

An array of `builtinIntentMetadata` objects, one for
each intent in the response.

Type: Array of [BuiltinIntentMetadata](API_BuiltinIntentMetadata.md "API_BuiltinIntentMetadata.md") objects

**[nextToken](#API_GetBuiltinIntents_ResponseSyntax "#API_GetBuiltinIntents_ResponseSyntax")**

A pagination token that fetches the next page of intents. If the
response to this API call is truncated, Amazon Lex returns a pagination token
in the response. To fetch the next page of intents, specify the pagination
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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/cli2/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/boto3/lex-models-2017-04-19/GetBuiltinIntents.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBuiltinIntents.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetBuiltinIntents.md")
