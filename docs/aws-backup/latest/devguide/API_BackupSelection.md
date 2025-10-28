# BackupSelection

Used to specify a set of resources to a backup plan.

We recommend that you specify conditions, tags, or resources to include or exclude.
Otherwise, Backup attempts to select all supported and opted-in storage resources, which
could have unintended cost implications.

For more information, see [Assigning resources programmatically](assigning-resources.md#assigning-resources-json "assigning-resources.md#assigning-resources-json").

## Contents

**IamRoleArn**

The ARN of the IAM role that AWS Backup uses to authenticate when backing up the
target resource; for example, `arn:aws:iam::123456789012:role/S3Access`.

Type: String

Required: Yes

**SelectionName**

The display name of a resource selection document. Must contain 1 to 50 alphanumeric or
'-\_.' characters.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: Yes

**Conditions**

The conditions that you define to assign resources to your backup plans using tags. For example,
`"StringEquals": { "ConditionKey": "aws:ResourceTag/backup", "ConditionValue": "daily" }`.

`Conditions` supports `StringEquals`,
`StringLike`, `StringNotEquals`, and
`StringNotLike`. Condition operators are case sensitive.

If you specify multiple conditions, the resources much match all conditions (AND logic).

Type: [Conditions](API_Conditions.md "API_Conditions.md") object

Required: No

**ListOfTags**

We recommend that you use the `Conditions` parameter instead of this parameter.

The conditions that you define to assign resources to your backup plans using tags. For example,
`"StringEquals": { "ConditionKey": "backup", "ConditionValue": "daily"}`.

`ListOfTags` supports only `StringEquals`. Condition operators are case sensitive.

If you specify multiple conditions, the resources much match any of the conditions (OR logic).

Type: Array of [Condition](API_Condition.md "API_Condition.md") objects

Required: No

**NotResources**

The Amazon Resource Names (ARNs) of the resources to exclude from a backup plan. The maximum number
of ARNs is 500 without wildcards, or 30 ARNs with wildcards.

If you need to exclude many resources from a backup plan, consider a different resource
selection strategy, such as assigning only one or a few resource types or refining your
resource selection using tags.

Type: Array of strings

Required: No

**Resources**

The Amazon Resource Names (ARNs) of the resources to assign to a backup plan. The maximum number of
ARNs is 500 without wildcards, or 30 ARNs with wildcards.

If you need to assign many resources to a backup plan, consider a different resource
selection strategy, such as assigning all resources of a resource type or refining your
resource selection using tags.

If you specify multiple ARNs, the resources much match any of the ARNs (OR logic).

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/BackupSelection.md "../../../goto/SdkForCpp/backup-2018-11-15/BackupSelection.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/BackupSelection.md "../../../goto/SdkForJavaV2/backup-2018-11-15/BackupSelection.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/BackupSelection.md "../../../goto/SdkForRubyV3/backup-2018-11-15/BackupSelection.md")
