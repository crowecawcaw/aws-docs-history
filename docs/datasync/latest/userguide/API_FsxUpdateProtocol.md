# FsxUpdateProtocol

Specifies the data transfer protocol that AWS DataSync uses to access your
Amazon FSx file system.

###### Note

You can't update the Network File System (NFS) protocol configuration for FSx for ONTAP locations. DataSync currently only supports NFS version 3 with
this location type.

## Contents

**NFS**

Specifies the Network File System (NFS) protocol configuration that DataSync
uses to access your FSx for OpenZFS file system or FSx for ONTAP file
system's storage virtual machine (SVM).

Type: [FsxProtocolNfs](API_FsxProtocolNfs.md "API_FsxProtocolNfs.md") object

Required: No

**SMB**

Specifies the Server Message Block (SMB) protocol configuration that DataSync
uses to access your FSx for ONTAP file system's storage virtual machine
(SVM).

Type: [FsxUpdateProtocolSmb](API_FsxUpdateProtocolSmb.md "API_FsxUpdateProtocolSmb.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocol.md "../../../goto/SdkForCpp/datasync-2018-11-09/FsxUpdateProtocol.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocol.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/FsxUpdateProtocol.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocol.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/FsxUpdateProtocol.md")
