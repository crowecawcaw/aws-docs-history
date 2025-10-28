# DestinationToCreate

Describes the new or existing destination file system for the replication
configuration.

- If you want to replicate to a new file system, do not specify the File System ID
  for the destination file system. Amazon EFS creates a new, empty file system.
  For One Zone storage, specify the Availability Zone to create the file system in. To
  use an AWS Key Management Service key other than the default KMS key, then
  specify it. For more information, see [Configuring replication to new Amazon EFS file system](create-replication.md "create-replication.md") in the _Amazon EFS User
  Guide_.

###### Note

After the file system is created, you cannot change the KMS key or the performance mode.

- If you want to replicate to an existing file system that's in the same account
  as the source file system, then you need to
  provide the ID or Amazon Resource Name (ARN) of the file system to which to replicate. The file system's replication
  overwrite protection must be disabled. For more information, see [Replicating to
  an existing file system](efs-replication.md#replicate-existing-destination "efs-replication.md#replicate-existing-destination") in the _Amazon EFS User
  Guide_.
- If you are replicating the file system to a file system that's in a different account than the
  source file system (cross-account replication), you need to provide the ARN for the file system and the IAM role that allows Amazon EFS to perform
  replication on the destination account. The file system's replication overwrite protection
  must be disabled. For more information, see [Replicating across AWS accounts](cross-account-replication.md "cross-account-replication.md") in the _Amazon EFS User
  Guide_.

## Contents

**AvailabilityZoneName**

To create a file system that uses One Zone storage, specify the name of the
Availability Zone in which to create the destination file system.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

Required: No

**FileSystemId**

The ID or ARN of the file system to use for the destination.
For cross-account replication, this must be an ARN. The file system's
replication overwrite replication must be disabled. If no ID or ARN is
specified, then a new file system is created.

###### Note

When you initially configure replication to an existing file system, Amazon EFS
writes data to or removes existing data from the destination file system to match data in
the source file system. If you don't want to change data in the destination file system,
then you should replicate to a new file system instead. For more information, see [https://docs.aws.amazon.com/efs/latest/ug/create-replication.html](create-replication.md "create-replication.md").

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: No

**KmsKeyId**

Specify the AWS Key Management Service (AWS KMS) key that you want to use to
encrypt the destination file system. If you do not specify a KMS key, Amazon EFS uses your default KMS key for Amazon EFS,
`/aws/elasticfilesystem`. This ID can be in one of the following formats:

- Key ID - The unique identifier of the key, for example
  `1234abcd-12ab-34cd-56ef-1234567890ab`.
- ARN - The ARN for the key, for example
  `arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`.
- Key alias - A previously created display name for a key, for example
  `alias/projectKey1`.
- Key alias ARN - The ARN for a key alias, for example
  `arn:aws:kms:us-west-2:444455556666:alias/projectKey1`.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`

Required: No

**Region**

To create a file system that uses Regional storage, specify the AWS Region in which to create the destination file system. The Region must be enabled
for the AWS account that owns the source file system. For more information, see
[Managing AWS Regions](../../../general/latest/gr/rande-manage.md#rande-manage-enable "../../../general/latest/gr/rande-manage.md#rande-manage-enable") in the _AWS General
Reference Reference Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `^[a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-{0,1}[0-9]{0,1}$`

Required: No

**RoleArn**

Amazon Resource Name (ARN) of the IAM role in the source account that allows
Amazon EFS to perform replication on its behalf. This is optional for same-account
replication and required for cross-account replication.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DestinationToCreate.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DestinationToCreate.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DestinationToCreate.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DestinationToCreate.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DestinationToCreate.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DestinationToCreate.md")
