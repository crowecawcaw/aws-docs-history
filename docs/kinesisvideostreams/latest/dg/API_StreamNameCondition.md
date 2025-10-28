# StreamNameCondition

Specifies the condition that streams must satisfy to be returned when you list
streams (see the `ListStreams` API). A condition has a comparison operation
and a value. Currently, you can specify only the `BEGINS_WITH` operator,
which finds streams whose names start with a given prefix.

## Contents

**ComparisonOperator**

A comparison operator. Currently, you can specify only the `BEGINS_WITH`
operator, which finds streams whose names start with a given prefix.

Type: String

Valid Values: `BEGINS_WITH`

Required: No

**ComparisonValue**

A value to compare.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_.-]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StreamNameCondition.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/StreamNameCondition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StreamNameCondition.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/StreamNameCondition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StreamNameCondition.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/StreamNameCondition.md")
