# Destination

Describes the destination file system in the replication configuration.

## Contents

**FileSystemId**

The ID of the destination Amazon EFS file system.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

**Region**

The AWS Region in which the destination file system is located.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`

Required: Yes

**Status**

Describes the status of the replication configuration. For more information
about replication status, see [Viewing
replication details](awsbackup.md#restoring-backup-efsmonitoring-replication-status.html "awsbackup.md#restoring-backup-efsmonitoring-replication-status.html") in the _Amazon EFS User Guide_.

Type: String

Valid Values: `ENABLED | ENABLING | DELETING | ERROR | PAUSED | PAUSING`

Required: Yes

**LastReplicatedTimestamp**

The time when the most recent sync was successfully completed on the destination file
system. Any changes to data on the source file system that occurred before this time have been
successfully replicated to the destination file system. Any changes that occurred after this
time might not be fully replicated.

Type: Timestamp

Required: No

**OwnerId**

ID of the AWS account in which the destination file system resides.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

Required: No

**RoleArn**

Amazon Resource Name (ARN) of the IAM role in the source account that allows
Amazon EFS to perform replication on its behalf. This is optional for same-account
replication and required for cross-account replication.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

**StatusMessage**

Message that provides details about the `PAUSED` or `ERRROR` state
of the replication destination configuration. For more information
about replication status messages, see [Viewing
replication details](awsbackup.md#restoring-backup-efsmonitoring-replication-status.html "awsbackup.md#restoring-backup-efsmonitoring-replication-status.html") in the _Amazon EFS User Guide_.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/Destination.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/Destination.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/Destination.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/Destination.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/Destination.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/Destination.md")
