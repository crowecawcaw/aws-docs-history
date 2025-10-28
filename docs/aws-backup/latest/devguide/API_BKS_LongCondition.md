# LongCondition

The long condition contains a `Value`
and can optionally contain an `Operator`.

## Contents

**Value**

The value of an item included in one of the search
item filters.

Type: Long

Required: Yes

**Operator**

A string that defines what values will be
returned.

If this is included, avoid combinations of
operators that will return all possible values.
For example, including both `EQUALS_TO`
and `NOT_EQUALS_TO` with a value of `4`
will return all values.

Type: String

Valid Values: `EQUALS_TO | NOT_EQUALS_TO | LESS_THAN_EQUAL_TO | GREATER_THAN_EQUAL_TO`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/LongCondition.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/LongCondition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/LongCondition.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/LongCondition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/LongCondition.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/LongCondition.md")
