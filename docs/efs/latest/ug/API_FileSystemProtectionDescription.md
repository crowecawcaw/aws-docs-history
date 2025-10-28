# FileSystemProtectionDescription

Describes the protection on a file system.

## Contents

**ReplicationOverwriteProtection**

The status of the file system's replication overwrite protection.

- `ENABLED` – The file system cannot be used as the destination file
  system in a replication configuration. The file system is writeable. Replication overwrite
  protection is `ENABLED` by default.
- `DISABLED` – The file system can be used as the destination file
  system in a replication configuration. The file system is read-only and can only be
  modified by EFS replication.
- `REPLICATING` – The file system is being used as the destination
  file system in a replication configuration. The file system is read-only and is modified
  only by EFS replication.

If the replication configuration is deleted, the file system's replication overwrite
protection is re-enabled, the file system becomes writeable.

Type: String

Valid Values: `ENABLED | DISABLED | REPLICATING`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemProtectionDescription.md")
