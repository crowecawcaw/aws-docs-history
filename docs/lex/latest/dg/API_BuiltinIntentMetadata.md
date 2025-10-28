End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# BuiltinIntentMetadata

Provides metadata for a built-in intent.

## Contents

**signature**

A unique identifier for the built-in intent. To find the signature
for an intent, see [Standard Built-in Intents](https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents "https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/built-in-intent-ref/standard-intents") in the _Alexa Skills
Kit_.

Type: String

Required: No

**supportedLocales**

A list of identifiers for the locales that the intent
supports.

Type: Array of strings

Valid Values: `de-DE | en-AU | en-GB | en-IN | en-US | es-419 | es-ES | es-US | fr-FR | fr-CA | it-IT | ja-JP | ko-KR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/BuiltinIntentMetadata.md "../../../goto/SdkForCpp/lex-models-2017-04-19/BuiltinIntentMetadata.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/BuiltinIntentMetadata.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/BuiltinIntentMetadata.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/BuiltinIntentMetadata.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/BuiltinIntentMetadata.md")
