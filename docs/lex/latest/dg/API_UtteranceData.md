End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# UtteranceData

Provides information about a single utterance that was made to your
bot.

## Contents

**count**

The number of times that the utterance was processed.

Type: Integer

Required: No

**distinctUsers**

The total number of individuals that used the utterance.

Type: Integer

Required: No

**firstUtteredDate**

The date that the utterance was first recorded.

Type: Timestamp

Required: No

**lastUtteredDate**

The date that the utterance was last recorded.

Type: Timestamp

Required: No

**utteranceString**

The text that was entered by the user or the text representation of
an audio clip.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/UtteranceData.md "../../../goto/SdkForCpp/lex-models-2017-04-19/UtteranceData.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/UtteranceData.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/UtteranceData.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/UtteranceData.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/UtteranceData.md")
