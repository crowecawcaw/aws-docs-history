# ReplicationConfigurationDescription

Describes the replication configuration for a specific file system.

## Contents

**CreationTime**

Describes when the replication configuration was created.

Type: Timestamp

Required: Yes

**Destinations**

An array of destination objects. Only one destination object is supported.

Type: Array of [Destination](API_Destination.md "API_Destination.md") objects

Required: Yes

**OriginalSourceFileSystemArn**

The Amazon Resource Name (ARN) of the original source EFS file
system in the replication configuration.

Type: String

Required: Yes

**SourceFileSystemArn**

The Amazon Resource Name (ARN) of the current source file system in the
replication configuration.

Type: String

Required: Yes

**SourceFileSystemId**

The ID of the source Amazon EFS file system that is being replicated.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

**SourceFileSystemRegion**

The AWS Region in which the source EFS file system is
located.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`

Required: Yes

**SourceFileSystemOwnerId**

ID of the AWS account in which the source file system resides.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/ReplicationConfigurationDescription.md")
