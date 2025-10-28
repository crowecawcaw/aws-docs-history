# ConditionParameter

Includes information about tags you define to assign tagged resources to a backup
plan.

Include the prefix `aws:ResourceTag` in your tags.
For example, `"aws:ResourceTag/TagKey1": "Value1"`.

## Contents

**ConditionKey**

The key in a key-value pair. For example, in the tag `Department:
 Accounting`, `Department` is the key.

Type: String

Required: No

**ConditionValue**

The value in a key-value pair. For example, in the tag `Department:
 Accounting`, `Accounting` is the value.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ConditionParameter.md "../../../goto/SdkForCpp/backup-2018-11-15/ConditionParameter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ConditionParameter.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ConditionParameter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ConditionParameter.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ConditionParameter.md")
