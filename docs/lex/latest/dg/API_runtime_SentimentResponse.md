End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# SentimentResponse

The sentiment expressed in an utterance.

When the bot is configured to send utterances to Amazon Comprehend for
sentiment analysis, this field structure contains the result of the
analysis.

## Contents

**sentimentLabel**

The inferred sentiment that Amazon Comprehend has the highest
confidence in.

Type: String

Required: No

**sentimentScore**

The likelihood that the sentiment was correctly inferred.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/SentimentResponse.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/SentimentResponse.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/SentimentResponse.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/SentimentResponse.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/SentimentResponse.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/SentimentResponse.md")
