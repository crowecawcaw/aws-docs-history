# CreationInfo

Required if the `RootDirectory` > `Path` specified does not exist.
Specifies the POSIX IDs and permissions to apply to the access point's `RootDirectory` > `Path`.
If the access point root directory does not exist, EFS creates it with these settings when a client connects to the access point.
When specifying `CreationInfo`, you must include values for all properties.

Amazon EFS creates a root directory only if you have provided the CreationInfo: OwnUid, OwnGID, and permissions for the directory.
If you do not provide this information, Amazon EFS does not create the root directory. If the root directory does not exist, attempts to mount
using the access point will fail.

###### Important

If you do not provide `CreationInfo` and the specified `RootDirectory` does not exist,
attempts to mount the file system using the access point will fail.

## Contents

**OwnerGid**

Specifies the POSIX group ID to apply to the `RootDirectory`. Accepts values from 0 to 2^32 (4294967295).

Type: Long

Valid Range: Minimum value of 0. Maximum value of 4294967295.

Required: Yes

**OwnerUid**

Specifies the POSIX user ID to apply to the `RootDirectory`. Accepts values from 0 to 2^32 (4294967295).

Type: Long

Valid Range: Minimum value of 0. Maximum value of 4294967295.

Required: Yes

**Permissions**

Specifies the POSIX permissions to apply to the `RootDirectory`, in the format of an octal number representing the file's mode bits.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 4.

Pattern: `^[0-7]{3,4}$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreationInfo.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/CreationInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreationInfo.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/CreationInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreationInfo.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/CreationInfo.md")
