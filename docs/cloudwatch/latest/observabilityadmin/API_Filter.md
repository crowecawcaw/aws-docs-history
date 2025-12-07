# Filter

A single filter condition that specifies behavior, requirement, and matching conditions
for WAF log records.

## Contents

**Behavior**

The action to take for log records matching this filter (KEEP or DROP).

Type: String

Valid Values: `KEEP | DROP`

Required: No

**Conditions**

The list of conditions that determine if a log record matches this filter.

Type: Array of [Condition](API_Condition.md "API_Condition.md") objects

Array Members: Minimum number of 1 item.

Required: No

**Requirement**

Whether the log record must meet all conditions (MEETS_ALL) or any condition (MEETS_ANY)
to match this filter.

Type: String

Valid Values: `MEETS_ALL | MEETS_ANY`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/Filter.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/Filter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/Filter.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/Filter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/Filter.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/Filter.md")
