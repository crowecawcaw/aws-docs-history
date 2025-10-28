# RootDirectory

Specifies the directory on the Amazon EFS file system that the access point
provides access to. The access point exposes the specified file system path as the root
directory of your file system to applications using the access point. NFS clients using the
access point can only access data in the access point's `RootDirectory` and its
subdirectories.

## Contents

**CreationInfo**

(Optional) Specifies the POSIX IDs and permissions to apply to the access point's
`RootDirectory`. If the `RootDirectory` > `Path`
specified does not exist, EFS creates the root directory using the
`CreationInfo` settings when a client connects to an access point. When
specifying the `CreationInfo`, you must provide values for all properties.

###### Important

If you do not provide `CreationInfo` and the specified `RootDirectory` > `Path` does not exist,
attempts to mount the file system using the access point will fail.

Type: [CreationInfo](API_CreationInfo.md "API_CreationInfo.md") object

Required: No

**Path**

Specifies the path on the EFS file system to expose as the root directory to
NFS clients using the access point to access the EFS file system. A path can have
up to four subdirectories. If the specified path does not exist, you are required to provide
the `CreationInfo`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^(\/|(\/(?!\.)+[^$#<>;`|&?{}^\*/\n]+){1,4})$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/RootDirectory.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/RootDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/RootDirectory.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/RootDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/RootDirectory.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/RootDirectory.md")
