# CreateLocationEfs

Creates a transfer _location_ for an Amazon EFS file system.
AWS DataSync can use this location as a source or destination for transferring
data.

Before you begin, make sure that you understand how DataSync
[accesses
Amazon EFS file systems](create-efs-location.md#create-efs-location-access "create-efs-location.md#create-efs-location-access").

## Request Syntax

```
{
   "AccessPointArn": "`string`",
   "Ec2Config": {
      "SecurityGroupArns": [ "`string`" ],
      "SubnetArn": "`string`"
   },
   "EfsFilesystemArn": "`string`",
   "FileSystemAccessRoleArn": "`string`",
   "InTransitEncryption": "`string`",
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

**[AccessPointArn](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses
to mount your Amazon EFS file system.

For more information, see [Accessing
restricted file systems](create-efs-location.md#create-efs-location-iam "create-efs-location.md#create-efs-location-iam").

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$`

Required: No

**[Ec2Config](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies the subnet and security groups DataSync uses to connect to one of
your Amazon EFS file system's [mount targets](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md").

Type: [Ec2Config](API_Ec2Config.md "API_Ec2Config.md") object

Required: Yes

**[EfsFilesystemArn](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies the ARN for your Amazon EFS file system.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]{8,40}$`

Required: Yes

**[FileSystemAccessRoleArn](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies an AWS Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.

For information on creating this role, see [Creating a DataSync
IAM role for file system access](create-efs-location.md#create-efs-location-iam-role "create-efs-location.md#create-efs-location-iam-role").

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`

Required: No

**[InTransitEncryption](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2
encryption when it transfers data to or from your Amazon EFS file system.

If you specify an access point using `AccessPointArn` or an IAM
role using `FileSystemAccessRoleArn`, you must set this parameter to
`TLS1_2`.

Type: String

Valid Values: `NONE | TLS1_2`

Required: No

**[Subdirectory](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or
destination location).

By default, DataSync uses the root directory (or [access point](../../../efs/latest/ug/efs-access-points.md "../../../efs/latest/ug/efs-access-points.md") if you provide one by using
`AccessPointArn`). You can also include subdirectories using forward slashes (for
example, `/path/to/folder`).

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

Required: No

**[Tags](#API_CreateLocationEfs_RequestSyntax "#API_CreateLocationEfs_RequestSyntax")**

Specifies the key-value pair that represents a tag that you want to add to the
resource. The value can be an empty string. This value helps you manage, filter, and search
for your resources. We recommend that you create a name tag for your location.

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

**[LocationArn](#API_CreateLocationEfs_ResponseSyntax "#API_CreateLocationEfs_ResponseSyntax")**

The Amazon Resource Name (ARN) of the Amazon EFS file system location that you
create.

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

### Sample Request

The following example creates a location for an Amazon EFS file system.

```
{
    "Ec2Config": {
        "SubnetArn": "arn:aws:ec2:us-east-2:11122233344:subnet/subnet-1234567890abcdef1",
        "SecurityGroupArns": [
            "arn:aws:ec2:us-east-2:11122233344:security-group/sg-1234567890abcdef2"
        ]
    },
    "EfsFilesystemArn": "arn:aws:elasticfilesystem:us-east-2:111222333444:file-system/fs-021345abcdef6789",
    "Subdirectory": "/mount/path",
    "Tags": [{
        "Key": "Name",
        "Value": "ElasticFileSystem-1"
    }]
}
```

### Sample Request: Creating a location for a restricted Amazon EFS file

system

The following example creates a location for an Amazon EFS file system with
restricted access. In this kind of scenario, you might have to specify values for
`AccessPointArn`, `FileSystemAccessRoleArn`, and
`InTransitEncryption` in your request.

```
{
    "AccessPointArn": "arn:aws:elasticfilesystem:us-east-2:111222333444:access-point/fsap-1234567890abcdef0",
    "Ec2Config": {
        "SubnetArn": "arn:aws:ec2:us-east-2:111222333444:subnet/subnet-1234567890abcdef1",
        "SecurityGroupArns": [
            "arn:aws:ec2:us-east-2:111222333444:security-group/sg-1234567890abcdef2"
        ]
    },
    "FileSystemAccessRoleArn": "arn:aws:iam::111222333444:role/AwsDataSyncFullAccessNew",
    "InTransitEncryption": "TLS1_2",
    "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-abcdef01234567890",
    "LocationUri": "efs://us-east-2.fs-021345abcdef6789/",
    "Subdirectory": "/mount/path",
    "Tags": [{
        "Key": "Name",
        "Value": "ElasticFileSystem-1"
    }]
}
```

### Sample Response

A response returns the location ARN of the Amazon EFS file system.

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-12abcdef012345678"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationEfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationEfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationEfs.md")
