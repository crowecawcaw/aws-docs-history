# MountTargetDescription

Provides a description of a mount target.

## Contents

**FileSystemId**

The ID of the file system for which the mount target is intended.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

**LifeCycleState**

Lifecycle state of the mount target.

Type: String

Valid Values: `creating | available | updating | deleting | deleted | error`

Required: Yes

**MountTargetId**

System-assigned mount target ID.

Type: String

Length Constraints: Minimum length of 13. Maximum length of 45.

Pattern: `^fsmt-[0-9a-f]{8,40}$`

Required: Yes

**SubnetId**

The ID of the mount target's subnet.

Type: String

Length Constraints: Minimum length of 15. Maximum length of 47.

Pattern: `^subnet-[0-9a-f]{8,40}$`

Required: Yes

**AvailabilityZoneId**

The unique and consistent identifier of the Availability Zone that the mount target resides in.
For example, `use1-az1` is an AZ ID for the us-east-1 Region and it
has the same location in every AWS account.

Type: String

Required: No

**AvailabilityZoneName**

The name of the Availability Zone in which the mount target is located. Availability Zones are
independently mapped to names for each AWS account. For example, the
Availability Zone `us-east-1a` for your AWS account might not be the
same location as `us-east-1a` for another AWS account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

Required: No

**IpAddress**

The IPv4 address for the mount target.

Type: String

Length Constraints: Minimum length of 7. Maximum length of 15.

Pattern: `^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$`

Required: No

**Ipv6Address**

The IPv6 address for the mount target.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 39.

Required: No

**NetworkInterfaceId**

The ID of the network interface that Amazon EFS created when it created the mount
target.

Type: String

Required: No

**OwnerId**

AWS account ID that owns the resource.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

Required: No

**VpcId**

The virtual private cloud (VPC) ID that the mount target is configured in.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/MountTargetDescription.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/MountTargetDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/MountTargetDescription.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/MountTargetDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/MountTargetDescription.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/MountTargetDescription.md")
