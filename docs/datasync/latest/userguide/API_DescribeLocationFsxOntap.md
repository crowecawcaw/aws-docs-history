# DescribeLocationFsxOntap

Provides details about how an AWS DataSync transfer location for an Amazon FSx for NetApp ONTAP file system is configured.

###### Note

If your location uses SMB, the `DescribeLocationFsxOntap` operation doesn't
actually return a `Password`.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationFsxOntap_RequestSyntax "#API_DescribeLocationFsxOntap_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP file system
location that you want information about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "CreationTime": ***number***,
   "FsxFilesystemArn": "***string***",
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "Protocol": {
      "NFS": {
         "MountOptions": {
            "Version": "***string***"
         }
      },
      "SMB": {
         "Domain": "***string***",
         "MountOptions": {
            "Version": "***string***"
         },
         "Password": "***string***",
         "User": "***string***"
      }
   },
   "SecurityGroupArns": [ "***string***" ],
   "StorageVirtualMachineArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[CreationTime](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The time that the location was created.

Type: Timestamp

**[FsxFilesystemArn](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The ARN of the FSx for ONTAP file system.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:file-system/fs-[0-9a-f]+$`

**[LocationArn](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The ARN of the FSx for ONTAP file system location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The uniform resource identifier (URI) of the FSx for ONTAP file system
location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[Protocol](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

Specifies the data transfer protocol that AWS DataSync uses to access your
Amazon FSx file system.

Type: [FsxProtocol](API_FsxProtocol.md "API_FsxProtocol.md") object

**[SecurityGroupArns](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The security groups that DataSync uses to access your FSx for ONTAP
file system.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 5 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):ec2:[a-z\-0-9]*:[0-9]{12}:security-group/sg-[a-f0-9]+$`

**[StorageVirtualMachineArn](#API_DescribeLocationFsxOntap_ResponseSyntax "#API_DescribeLocationFsxOntap_ResponseSyntax")**

The ARN of the storage virtual machine (SVM) on your FSx for ONTAP file system
where you're copying data to or from.

Type: String

Length Constraints: Maximum length of 162.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):fsx:[a-z\-0-9]+:[0-9]{12}:storage-virtual-machine/fs-[0-9a-f]+/svm-[0-9a-f]{17,}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationFsxOntap.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxOntap.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationFsxOntap.md")
