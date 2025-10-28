# FileSystemDescription

A description of the file system.

## Contents

**CreationTime**

The time that the file system was created, in seconds (since
1970-01-01T00:00:00Z).

Type: Timestamp

Required: Yes

**CreationToken**

The opaque string specified in the request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

Required: Yes

**FileSystemId**

The ID of the file system, assigned by Amazon EFS.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

**LifeCycleState**

The lifecycle phase of the file system.

Type: String

Valid Values: `creating | available | updating | deleting | deleted | error`

Required: Yes

**NumberOfMountTargets**

The current number of mount targets that the file system has. For more information, see [CreateMountTarget](API_CreateMountTarget.md "API_CreateMountTarget.md").

Type: Integer

Valid Range: Minimum value of 0.

Required: Yes

**OwnerId**

The AWS account that created the file system.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

Required: Yes

**PerformanceMode**

The performance mode of the file system.

Type: String

Valid Values: `generalPurpose | maxIO`

Required: Yes

**SizeInBytes**

The latest known metered size (in bytes) of data stored in the file system, in its
`Value` field, and the time at which that size was determined in its
`Timestamp` field. The `Timestamp` value is the integer number of
seconds since 1970-01-01T00:00:00Z. The `SizeInBytes` value doesn't represent
the size of a consistent snapshot of the file system, but it is eventually consistent when
there are no writes to the file system. That is, `SizeInBytes` represents actual
size only if the file system is not modified for a period longer than a couple of hours.
Otherwise, the value is not the exact size that the file system was at any point in time.

Type: [FileSystemSize](API_FileSystemSize.md "API_FileSystemSize.md") object

Required: Yes

**Tags**

The tags associated with the file system, presented as an array of `Tag`
objects.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: Yes

**AvailabilityZoneId**

The unique and consistent identifier of the Availability Zone in which the file system is
located, and is valid only for One Zone file systems. For example,
`use1-az1` is an Availability Zone ID for the us-east-1 AWS Region, and
it has the same location in every AWS account.

Type: String

Required: No

**AvailabilityZoneName**

Describes the AWS Availability Zone in which the file system is located, and is
valid only for One Zone file systems. For more information, see [Using EFS storage
classes](storage-classes.md "storage-classes.md") in the _Amazon EFS User Guide_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

Required: No

**Encrypted**

A Boolean value that, if true, indicates that the file system is encrypted.

Type: Boolean

Required: No

**FileSystemArn**

The Amazon Resource Name (ARN) for the EFS file system, in the
format
`arn:aws:elasticfilesystem:*region*:*account-id*:file-system/*file-system-id*`.
Example with sample data:
`arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-01234567`

Type: String

Required: No

**FileSystemProtection**

Describes the protection on the file system.

Type: [FileSystemProtectionDescription](API_FileSystemProtectionDescription.md "API_FileSystemProtectionDescription.md") object

Required: No

**KmsKeyId**

The ID of an AWS KMS key used to protect the encrypted file system.

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}|mrk-[0-9a-f]{32}|alias/[a-zA-Z0-9/_-]+|(arn:aws[-a-z]*:kms:[a-z0-9-]+:\d{12}:((key/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})|(key/mrk-[0-9a-f]{32})|(alias/[a-zA-Z0-9/_-]+))))$`

Required: No

**Name**

You can add tags to a file system, including a `Name` tag. For more
information, see [CreateFileSystem](API_CreateFileSystem.md "API_CreateFileSystem.md"). If the file system has a `Name` tag, Amazon EFS returns
the value in this field.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

**ProvisionedThroughputInMibps**

The amount of provisioned throughput, measured in MiBps, for the file system. Valid for
file systems using `ThroughputMode` set to `provisioned`.

Type: Double

Valid Range: Minimum value of 1.0.

Required: No

**ThroughputMode**

Displays the file system's throughput mode. For more information, see
[Throughput modes](performance.md#throughput-modes "performance.md#throughput-modes")
in the _Amazon EFS User Guide_.

Type: String

Valid Values: `bursting | provisioned | elastic`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemDescription.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemDescription.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemDescription.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemDescription.md")
