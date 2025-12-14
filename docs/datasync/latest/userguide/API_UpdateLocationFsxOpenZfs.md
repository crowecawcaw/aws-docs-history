# UpdateLocationFsxOpenZfs

Modifies the following configuration parameters of the Amazon FSx for OpenZFS
transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with FSx for OpenZFS](create-openzfs-location.md "create-openzfs-location.md").

###### Note

Request parameters related to `SMB` aren't supported with the
`UpdateLocationFsxOpenZfs` operation.

## Request Syntax

```
{
   "LocationArn": "`string`",
   "Protocol": {
      "NFS": {
         "MountOptions": {
            "Version": "`string`"
         }
      },
      "SMB": {
         "Domain": "`string`",
         "MountOptions": {
            "Version": "`string`"
         },
         "Password": "`string`",
         "User": "`string`"
      }
   },
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_UpdateLocationFsxOpenZfs_RequestSyntax "#API_UpdateLocationFsxOpenZfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the FSx for OpenZFS transfer
location that you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Protocol](#API_UpdateLocationFsxOpenZfs_RequestSyntax "#API_UpdateLocationFsxOpenZfs_RequestSyntax")**

Specifies the data transfer protocol that AWS DataSync uses to access your
Amazon FSx file system.

Type: [FsxProtocol](API_FsxProtocol.md "API_FsxProtocol.md") object

Required: No

**[Subdirectory](#API_UpdateLocationFsxOpenZfs_RequestSyntax "#API_UpdateLocationFsxOpenZfs_RequestSyntax")**

Specifies a subdirectory in the location's path that must begin with `/fsx`.
DataSync uses this subdirectory to read or write data (depending on whether the
file system is a source or destination location).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationFsxOpenZfs.md")
