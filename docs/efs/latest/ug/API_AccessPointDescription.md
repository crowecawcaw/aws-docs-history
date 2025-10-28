# AccessPointDescription

Provides a description of an EFS file system access point.

## Contents

**AccessPointArn**

The unique Amazon Resource Name (ARN) associated with the access
point.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}$`

Required: No

**AccessPointId**

The ID of the access point, assigned by Amazon EFS.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`

Required: No

**ClientToken**

The opaque string specified in the request to ensure idempotent creation.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `.+`

Required: No

**FileSystemId**

The ID of the EFS file system that the access point applies to.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: No

**LifeCycleState**

Identifies the lifecycle phase of the access point.

Type: String

Valid Values: `creating | available | updating | deleting | deleted | error`

Required: No

**Name**

The name of the access point. This is the value of the `Name` tag.

Type: String

Required: No

**OwnerId**

Identifies the AWS account that owns the access point resource.

Type: String

Length Constraints: Maximum length of 14.

Pattern: `^(\d{12})|(\d{4}-\d{4}-\d{4})$`

Required: No

**PosixUser**

The full POSIX identity, including the user ID, group ID, and secondary group IDs on the access point that is used for all file operations by
NFS clients using the access point.

Type: [PosixUser](API_PosixUser.md "API_PosixUser.md") object

Required: No

**RootDirectory**

The directory on the EFS file system that the access point exposes as the root
directory to NFS clients using the access point.

Type: [RootDirectory](API_RootDirectory.md "API_RootDirectory.md") object

Required: No

**Tags**

The tags associated with the access point, presented as an array of Tag objects.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/AccessPointDescription.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/AccessPointDescription.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/AccessPointDescription.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/AccessPointDescription.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/AccessPointDescription.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/AccessPointDescription.md")
