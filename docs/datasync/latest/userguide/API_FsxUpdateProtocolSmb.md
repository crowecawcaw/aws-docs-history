# FsxUpdateProtocolSmb

Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access your Amazon FSx for NetApp ONTAP file system's storage virtual machine
(SVM). For more information, see [Providing DataSync access to FSx for ONTAP file systems](create-ontap-location.md#create-ontap-location-access "create-ontap-location.md#create-ontap-location-access").

## Contents

**Domain**

Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs
to.

If you have multiple Active Directory domains in your environment, configuring this
parameter makes sure that DataSync connects to the right SVM.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^([A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252})?$`

Required: No

**MountOptions**

Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.

Type: [SmbMountOptions](API_SmbMountOptions.md "API_SmbMountOptions.md") object

Required: No

**Password**

Specifies the password of a user who has permission to access your SVM.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^.{0,104}$`

Required: No

**User**

Specifies a user that can mount and access the files, folders, and metadata in your
SVM.

For information about choosing a user with the right level of access for your transfer,
see [Using
the SMB protocol](create-ontap-location.md#create-ontap-location-smb "create-ontap-location.md#create-ontap-location-smb").

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocolSmb.md "../../../goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocolSmb.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocolSmb.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocolSmb.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocolSmb.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocolSmb.md")
