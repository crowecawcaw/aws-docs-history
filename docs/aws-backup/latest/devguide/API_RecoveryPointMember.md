# RecoveryPointMember

This is a recovery point which is a child (nested) recovery point
of a parent (composite) recovery point. These recovery points
can be disassociated from their parent (composite) recovery
point, in which case they will no longer be a member.

## Contents

**BackupVaultName**

The name of the backup vault
(the logical container in which backups are stored).

Type: String

Pattern: `^[a-zA-Z0-9\-\_]{2,50}$`

Required: No

**RecoveryPointArn**

The Amazon Resource Name (ARN) of the parent (composite)
recovery point.

Type: String

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) that uniquely identifies
a saved resource.

Type: String

Required: No

**ResourceType**

The AWS resource type that is saved as
a recovery point.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointMember.md "../../../goto/SdkForCpp/backup-2018-11-15/RecoveryPointMember.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointMember.md "../../../goto/SdkForJavaV2/backup-2018-11-15/RecoveryPointMember.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointMember.md "../../../goto/SdkForRubyV3/backup-2018-11-15/RecoveryPointMember.md")
