# CreateLocationFsxOpenZfs

Creates a transfer _location_ for an Amazon FSx for OpenZFS file
system. AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync
[accesses
FSx for OpenZFS file systems](create-openzfs-location.md#create-openzfs-access "create-openzfs-location.md#create-openzfs-access").

###### Note

Request parameters related to `SMB` aren't supported with the
`CreateLocationFsxOpenZfs` operation.

## Request Syntax

```
{
   "FsxFilesystemArn": "`string`",
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
   "SecurityGroupArns": [ "`string`" ],
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

**[FsxFilesystemArn](#API_CreateLocationFsxOpenZfs_RequestSyntax "#API_CreateLocationFsxOpenZfs_RequestSyntax")**

The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`

Required: Yes

**[Protocol](#API_CreateLocationFsxOpenZfs_RequestSyntax "#API_CreateLocationFsxOpenZfs_RequestSyntax")**

The type of protocol that AWS DataSync uses to access your file system.

Type: [FsxProtocol](API_FsxProtocol.md "API_FsxProtocol.md") object

Required: Yes

**[SecurityGroupArns](#API_CreateLocationFsxOpenZfs_RequestSyntax "#API_CreateLocationFsxOpenZfs_RequestSyntax")**

The ARNs of the security groups that are used to configure the FSx for OpenZFS file
system.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

Required: Yes

**[Subdirectory](#API_CreateLocationFsxOpenZfs_RequestSyntax "#API_CreateLocationFsxOpenZfs_RequestSyntax")**

A subdirectory in the location's path that must begin with `/fsx`. DataSync uses this subdirectory to read or write data (depending on whether the file
system is a source or destination location).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[^\u0000\u0085\u2028\u2029\r\n]{1,4096}$`

Required: No

**[Tags](#API_CreateLocationFsxOpenZfs_RequestSyntax "#API_CreateLocationFsxOpenZfs_RequestSyntax")**

The key-value pair that represents a tag that you want to add to the resource. The value
can be an empty string. This value helps you manage, filter, and search for your resources. We
recommend that you create a name tag for your location.

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

**[LocationArn](#API_CreateLocationFsxOpenZfs_ResponseSyntax "#API_CreateLocationFsxOpenZfs_ResponseSyntax")**

The ARN of the FSx for OpenZFS file system location that you created.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationFsxOpenZfs.md")
