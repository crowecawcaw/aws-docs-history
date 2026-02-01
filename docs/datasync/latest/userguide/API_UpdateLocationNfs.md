# UpdateLocationNfs

Modifies the following configuration parameters of the Network File System (NFS) transfer
location that you're using with AWS DataSync.

For more information, see [Configuring transfers with an NFS
file server](create-nfs-location.md "create-nfs-location.md").

## Request Syntax

```
{
   "LocationArn": "`string`",
   "MountOptions": {
      "Version": "`string`"
   },
   "OnPremConfig": {
      "AgentArns": [ "`string`" ]
   },
   "ServerHostname": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_UpdateLocationNfs_RequestSyntax "#API_UpdateLocationNfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the NFS transfer location that you want to
update.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[MountOptions](#API_UpdateLocationNfs_RequestSyntax "#API_UpdateLocationNfs_RequestSyntax")**

Specifies how DataSync can access a location using the NFS protocol.

Type: [NfsMountOptions](API_NfsMountOptions.md "API_NfsMountOptions.md") object

Required: No

**[OnPremConfig](#API_UpdateLocationNfs_RequestSyntax "#API_UpdateLocationNfs_RequestSyntax")**

The AWS DataSync agents that can connect to your Network File System (NFS)
file server.

Type: [OnPremConfig](API_OnPremConfig.md "API_OnPremConfig.md") object

Required: No

**[ServerHostname](#API_UpdateLocationNfs_RequestSyntax "#API_UpdateLocationNfs_RequestSyntax")**

Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your
DataSync agent connects to.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`

Required: No

**[Subdirectory](#API_UpdateLocationNfs_RequestSyntax "#API_UpdateLocationNfs_RequestSyntax")**

Specifies the export path in your NFS file server that you want DataSync to
mount.

This path (or a subdirectory of the path) is where DataSync transfers data to or
from. For information on configuring an export for DataSync, see [Accessing NFS file servers](create-nfs-location.md#accessing-nfs "create-nfs-location.md#accessing-nfs").

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]+$`

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationNfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationNfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationNfs.md")
