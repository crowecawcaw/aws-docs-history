# SmbMountOptions

Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.

## Contents

**Version**

By default, DataSync automatically chooses an SMB protocol version based on
negotiation with your SMB file server. You also can configure DataSync to use a
specific SMB version, but we recommend doing this only if DataSync has trouble
negotiating with the SMB file server automatically.

These are the following options for configuring the SMB version:

- `AUTOMATIC` (default): DataSync and the SMB file server negotiate
  the highest version of SMB that they mutually support between 2.1 and 3.1.1.

This is the recommended option. If you instead choose a specific version that your
file server doesn't support, you may get an `Operation Not Supported`
error.

- `SMB3`: Restricts the protocol negotiation to only SMB version
  3.0.2.
- `SMB2`: Restricts the protocol negotiation to only SMB version 2.1.
- `SMB2_0`: Restricts the protocol negotiation to only SMB version
  2.0.
- `SMB1`: Restricts the protocol negotiation to only SMB version 1.0.

###### Note

The `SMB1` option isn't available when [creating an Amazon FSx for NetApp ONTAP location](API_CreateLocationFsxOntap.md "API_CreateLocationFsxOntap.md").

Type: String

Valid Values: `AUTOMATIC | SMB2 | SMB3 | SMB1 | SMB2_0`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/SmbMountOptions.md "../../../goto/SdkForCpp/datasync-2018-11-09/SmbMountOptions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/SmbMountOptions.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/SmbMountOptions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/SmbMountOptions.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/SmbMountOptions.md")
