End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# OutputContext

The specification of an output context that is set when an intent is
fulfilled.

## Contents

**name**

The name of the context.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**timeToLiveInSeconds**

The number of seconds that the context should be active after it is
first sent in a `PostContent` or `PostText`
response. You can set the value between 5 and 86,400 seconds (24
hours).

Type: Integer

Valid Range: Minimum value of 5. Maximum value of 86400.

Required: Yes

**turnsToLive**

The number of conversation turns that the context should be active. A
conversation turn is one `PostContent` or `PostText`
request and the corresponding response from Amazon Lex.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 20.

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/OutputContext.md "../../../goto/SdkForCpp/lex-models-2017-04-19/OutputContext.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/OutputContext.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/OutputContext.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/OutputContext.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/OutputContext.md")
