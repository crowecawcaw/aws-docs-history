End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ActiveContextTimeToLive

The length of time or number of turns that a context remains
active.

## Contents

**timeToLiveInSeconds**

The number of seconds that the context should be active after it is
first sent in a `PostContent` or `PostText`
response. You can set the value between 5 and 86,400 seconds (24
hours).

Type: Integer

Valid Range: Minimum value of 5. Maximum value of 86400.

Required: No

**turnsToLive**

The number of conversation turns that the context should be active. A
conversation turn is one `PostContent` or `PostText`
request and the corresponding response from Amazon Lex.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 20.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/ActiveContextTimeToLive.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/ActiveContextTimeToLive.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ActiveContextTimeToLive.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ActiveContextTimeToLive.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ActiveContextTimeToLive.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ActiveContextTimeToLive.md")
