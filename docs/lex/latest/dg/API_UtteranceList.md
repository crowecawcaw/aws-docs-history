End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# UtteranceList

Provides a list of utterances that have been made to a specific
version of your bot. The list contains a maximum of 100
utterances.

## Contents

**botVersion**

The version of the bot that processed the list.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: No

**utterances**

One or more [UtteranceData](API_UtteranceData.md "API_UtteranceData.md") objects that contain
information about the utterances that have been made to a bot. The maximum
number of object is 100.

Type: Array of [UtteranceData](API_UtteranceData.md "API_UtteranceData.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/UtteranceList.md "../../../goto/SdkForCpp/lex-models-2017-04-19/UtteranceList.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/UtteranceList.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/UtteranceList.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/UtteranceList.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/UtteranceList.md")
