End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# PredictedIntent

An intent that Amazon Lex suggests satisfies the user's intent. Includes
the name of the intent, the confidence that Amazon Lex has that the user's
intent is satisfied, and the slots defined for the intent.

## Contents

**intentName**

The name of the intent that Amazon Lex suggests satisfies the user's
intent.

Type: String

Required: No

**nluIntentConfidence**

Indicates how confident Amazon Lex is that an intent satisfies the user's
intent.

Type: [IntentConfidence](API_runtime_IntentConfidence.md "API_runtime_IntentConfidence.md") object

Required: No

**slots**

The slot and slot values associated with the predicted intent.

Type: String to string map

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/PredictedIntent.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/PredictedIntent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/PredictedIntent.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/PredictedIntent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/PredictedIntent.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/PredictedIntent.md")
