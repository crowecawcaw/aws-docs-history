# BackupPolicy

The backup policy for the file system used to create automatic daily backups. If status has a value of
`ENABLED`, the file system is being automatically backed up. For more information, see [Automatic backups](awsbackup.md#automatic-backups "awsbackup.md#automatic-backups").

## Contents

**Status**

Describes the status of the file system's backup policy.

- **`ENABLED`** – EFS is automatically
  backing up the file system.
- **`ENABLING`** – EFS is turning on
  automatic backups for the file system.
- **`DISABLED`** – Automatic back ups are turned
  off for the file system.
- **`DISABLING`** – EFS is turning off
  automatic backups for the file system.

Type: String

Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/BackupPolicy.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/BackupPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/BackupPolicy.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/BackupPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/BackupPolicy.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/BackupPolicy.md")
