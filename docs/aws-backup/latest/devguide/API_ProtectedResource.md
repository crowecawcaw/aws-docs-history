# ProtectedResource

A structure that contains information about a backed-up resource.

## Contents

**LastBackupTime**

The date and time a resource was last backed up, in Unix format and Coordinated
Universal Time (UTC). The value of `LastBackupTime` is accurate to milliseconds.
For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087
AM.

Type: Timestamp

Required: No

**LastBackupVaultArn**

The ARN (Amazon Resource Name) of the backup vault
that contains the most recent backup recovery point.

Type: String

Required: No

**LastRecoveryPointArn**

The ARN (Amazon Resource Name) of the most
recent recovery point.

Type: String

Required: No

**ResourceArn**

An Amazon Resource Name (ARN) that uniquely identifies a resource. The format of the ARN
depends on the resource type.

Type: String

Required: No

**ResourceName**

The non-unique name of the resource that
belongs to the specified backup.

Type: String

Required: No

**ResourceType**

The type of AWS resource; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database. For
Windows Volume Shadow Copy Service (VSS) backups, the only supported resource type is
Amazon EC2.

Type: String

Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ProtectedResource.md "../../../goto/SdkForCpp/backup-2018-11-15/ProtectedResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ProtectedResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ProtectedResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ProtectedResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ProtectedResource.md")
