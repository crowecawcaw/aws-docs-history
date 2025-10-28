# Condition

Contains an array of triplets made up of a condition type (such as
`StringEquals`), a key, and a value. Used to filter resources using their
tags and assign them to a backup plan. Case sensitive.

## Contents

**ConditionKey**

The key in a key-value pair. For example, in the tag `Department:
 Accounting`, `Department` is the key.

Type: String

Required: Yes

**ConditionType**

An operation applied to a key-value pair used to assign resources to your backup plan.
Condition only supports `StringEquals`. For more flexible assignment options,
including `StringLike` and the ability to exclude resources from your backup
plan, use `Conditions` (with an "s" on the end) for your [`BackupSelection`](API_BackupSelection.md "API_BackupSelection.md").

Type: String

Valid Values: `STRINGEQUALS`

Required: Yes

**ConditionValue**

The value in a key-value pair. For example, in the tag `Department:
 Accounting`, `Accounting` is the value.

Type: String

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/Condition.md "../../../goto/SdkForCpp/backup-2018-11-15/Condition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/Condition.md "../../../goto/SdkForJavaV2/backup-2018-11-15/Condition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/Condition.md "../../../goto/SdkForRubyV3/backup-2018-11-15/Condition.md")
