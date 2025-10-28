# NfsMountOptions

Specifies how DataSync can access a location using the NFS protocol.

## Contents

**Version**

Specifies the NFS version that you want DataSync to use when mounting your NFS
share. If the server refuses to use the version specified, the task fails.

You can specify the following options:

- `AUTOMATIC` (default): DataSync chooses NFS version 4.1.
- `NFS3`: Stateless protocol version that allows for asynchronous writes on
  the server.
- `NFSv4_0`: Stateful, firewall-friendly protocol version that supports
  delegations and pseudo file systems.
- `NFSv4_1`: Stateful protocol version that supports sessions, directory
  delegations, and parallel data processing. NFS version 4.1 also includes all features
  available in version 4.0.

###### Note

DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

Type: String

Valid Values: `AUTOMATIC | NFS3 | NFS4_0 | NFS4_1`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/NfsMountOptions.md "../../../goto/SdkForCpp/datasync-2018-11-09/NfsMountOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/NfsMountOptions.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/NfsMountOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/NfsMountOptions.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/NfsMountOptions.md")
