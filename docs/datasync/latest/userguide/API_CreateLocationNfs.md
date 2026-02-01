# CreateLocationNfs

Creates a transfer _location_ for a Network File System (NFS) file
server. AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync
[accesses NFS file
servers](create-nfs-location.md#accessing-nfs "create-nfs-location.md#accessing-nfs").

## Request Syntax

```
{
   "MountOptions": {
      "Version": "`string`"
   },
   "OnPremConfig": {
      "AgentArns": [ "`string`" ]
   },
   "ServerHostname": "`string`",
   "Subdirectory": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MountOptions](#API_CreateLocationNfs_RequestSyntax "#API_CreateLocationNfs_RequestSyntax")**

Specifies the options that DataSync can use to mount your NFS file
server.

Type: [NfsMountOptions](API_NfsMountOptions.md "API_NfsMountOptions.md") object

Required: No

**[OnPremConfig](#API_CreateLocationNfs_RequestSyntax "#API_CreateLocationNfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the DataSync agent that can
connect to your NFS file server.

You can specify more than one agent. For more information, see [Using multiple DataSync agents](do-i-need-datasync-agent.md#multiple-agents "do-i-need-datasync-agent.md#multiple-agents").

Type: [OnPremConfig](API_OnPremConfig.md "API_OnPremConfig.md") object

Required: Yes

**[ServerHostname](#API_CreateLocationNfs_RequestSyntax "#API_CreateLocationNfs_RequestSyntax")**

Specifies the DNS name or IP address (IPv4 or IPv6) of the NFS file server that your DataSync agent connects to.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`

Required: Yes

**[Subdirectory](#API_CreateLocationNfs_RequestSyntax "#API_CreateLocationNfs_RequestSyntax")**

Specifies the export path in your NFS file server that you want DataSync to
mount.

This path (or a subdirectory of the path) is where DataSync transfers data to
or from. For information on configuring an export for DataSync, see [Accessing NFS file servers](create-nfs-location.md#accessing-nfs "create-nfs-location.md#accessing-nfs").

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]+$`

Required: Yes

**[Tags](#API_CreateLocationNfs_RequestSyntax "#API_CreateLocationNfs_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: No

## Response Syntax

```
{
   "LocationArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[LocationArn](#API_CreateLocationNfs_ResponseSyntax "#API_CreateLocationNfs_ResponseSyntax")**

The ARN of the transfer location that you created for your NFS file server.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## Examples

### Example

The following example creates a DataSync transfer location for an NFS file
server.

#### Sample Request

```
{
  "MountOptions": {
     "Version": : "NFS4_0"
     },
  "OnPremConfig": {
    "AgentArn": [ "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs" ]
          },

           "ServerHostname": "MyServer@amazon.com",
           "Subdirectory": "/MyFolder",
           "Tags": [
              {
                "Key": "Name",
                "Value": "FileSystem-1"
              }
           ]
}
```

### Example

The response returns the ARN of the NFS location.

#### Sample Response

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50aa"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationNfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationNfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationNfs.md")
