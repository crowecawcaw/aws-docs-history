# UpdateLocationEfs

Modifies the following configuration parameters of the Amazon EFS transfer
location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with Amazon EFS](create-efs-location.md "create-efs-location.md").

## Request Syntax

```
{
   "AccessPointArn": "`string`",
   "FileSystemAccessRoleArn": "`string`",
   "InTransitEncryption": "`string`",
   "LocationArn": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AccessPointArn](#API_UpdateLocationEfs_RequestSyntax "#API_UpdateLocationEfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses
to mount your Amazon EFS file system.

For more information, see [Accessing
restricted Amazon EFS file systems](create-efs-location.md#create-efs-location-iam "create-efs-location.md#create-efs-location-iam").

Type: String

Length Constraints: Maximum length of 128.

Pattern: `(^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$)|(^$)`

Required: No

**[FileSystemAccessRoleArn](#API_UpdateLocationEfs_RequestSyntax "#API_UpdateLocationEfs_RequestSyntax")**

Specifies an AWS Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.

For information on creating this role, see [Creating a DataSync
IAM role for Amazon EFS file system access](create-efs-location.md#create-efs-location-iam-role "create-efs-location.md#create-efs-location-iam-role").

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `(^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$)|(^$)`

Required: No

**[InTransitEncryption](#API_UpdateLocationEfs_RequestSyntax "#API_UpdateLocationEfs_RequestSyntax")**

Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2
encryption when it transfers data to or from your Amazon EFS file system.

If you specify an access point using `AccessPointArn` or an IAM
role using `FileSystemAccessRoleArn`, you must set this parameter to
`TLS1_2`.

Type: String

Valid Values: `NONE | TLS1_2`

Required: No

**[LocationArn](#API_UpdateLocationEfs_RequestSyntax "#API_UpdateLocationEfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the Amazon EFS transfer location that
you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[Subdirectory](#API_UpdateLocationEfs_RequestSyntax "#API_UpdateLocationEfs_RequestSyntax")**

Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or
destination location).

By default, DataSync uses the root directory (or [access point](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") if you provide one by using
`AccessPointArn`). You can also include subdirectories using forward slashes (for
example, `/path/to/folder`).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationEfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationEfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationEfs.md")
