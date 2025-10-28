End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# ActiveContext

A context is a variable that contains information about the current
state of the conversation between a user and Amazon Lex. Context can be set
automatically by Amazon Lex when an intent is fulfilled, or it can be set at
runtime using the `PutContent`, `PutText`, or
`PutSession` operation.

## Contents

**name**

The name of the context.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**parameters**

State variables for the current context. You can use these values as
default values for slots in subsequent events.

Type: String to string map

Map Entries: Minimum number of 0 items. Maximum number of 10 items.

Key Length Constraints: Minimum length of 1. Maximum length of 100.

Value Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: Yes

**timeToLive**

The length of time or number of turns that a context remains
active.

Type: [ActiveContextTimeToLive](API_runtime_ActiveContextTimeToLive.md "API_runtime_ActiveContextTimeToLive.md") object

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/ActiveContext.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/ActiveContext.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ActiveContext.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/ActiveContext.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ActiveContext.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/ActiveContext.md")
