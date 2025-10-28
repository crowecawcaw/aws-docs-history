# DescribeLocationEfs

Provides details about how an AWS DataSync transfer location for an Amazon EFS file system is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationEfs_RequestSyntax "#API_DescribeLocationEfs_RequestSyntax")**

The Amazon Resource Name (ARN) of the Amazon EFS file system location that you
want information about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AccessPointArn": "***string***",
   "CreationTime": ***number***,
   "Ec2Config": {
      "SecurityGroupArns": [ "***string***" ],
      "SubnetArn": "***string***"
   },
   "FileSystemAccessRoleArn": "***string***",
   "InTransitEncryption": "***string***",
   "LocationArn": "***string***",
   "LocationUri": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccessPointArn](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The ARN of the access point that DataSync uses to access the Amazon EFS
file system.

For more information, see [Accessing
restricted file systems](create-efs-location.md#create-efs-location-iam "create-efs-location.md#create-efs-location-iam").

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):elasticfilesystem:[a-z\-0-9]+:[0-9]{12}:access-point/fsap-[0-9a-f]{8,40}$`

**[CreationTime](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The time that the location was created.

Type: Timestamp

**[Ec2Config](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The subnet and security groups that AWS DataSync uses to connect to one of your
Amazon EFS file system's [mount targets](../../../efs/latest/ug/accessing-fs.md "../../../efs/latest/ug/accessing-fs.md").

Type: [Ec2Config](API_Ec2Config.md "API_Ec2Config.md") object

**[FileSystemAccessRoleArn](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The AWS Identity and Access Management (IAM) role that allows DataSync to
access your Amazon EFS file system.

For more information, see [Creating a DataSync
IAM role for file system access](create-efs-location.md#create-efs-location-iam-role "create-efs-location.md#create-efs-location-iam-role").

Type: String

Length Constraints: Maximum length of 2048.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):iam::[0-9]{12}:role/.*$`

**[InTransitEncryption](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

Indicates whether DataSync uses Transport Layer Security (TLS) encryption when
transferring data to or from the Amazon EFS file system.

Type: String

Valid Values: `NONE | TLS1_2`

**[LocationArn](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The ARN of the Amazon EFS file system location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationEfs_ResponseSyntax "#API_DescribeLocationEfs_ResponseSyntax")**

The URL of the Amazon EFS file system location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

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

The following example shows how to get information about a specific Amazon EFS
file system location.

```
{
  "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-12abcdef012345678"
}
```

### Sample Response

The following example returns location details about an Amazon EFS file
system.

```
{
    "CreationTime": 1653319021.353,
    "Ec2Config": {
        "SubnetArn": "arn:aws:ec2:us-east-2:111222333444:subnet/subnet-1234567890abcdef1",
        "SecurityGroupArns": [
            "arn:aws:ec2:us-east-2:111222333444:security-group/sg-1234567890abcdef2"
        ]
    },
    "LocationArn": "arn:aws:datasync:us-east-2:111222333444:location/loc-abcdef01234567890",
    "LocationUri": "efs://us-east-2.fs-021345abcdef6789/"
}
```

### Sample Response: Describing a location for a restricted Amazon EFS file

system

The following example returns location details about an Amazon EFS file system
with restricted access, including the `AccessPointArn`,
`FileSystemAccessRoleArn`, and `InTransitEncryption`
elements.

```
{
    "CreationTime": 1653319021.353,
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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationEfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationEfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationEfs.md")
