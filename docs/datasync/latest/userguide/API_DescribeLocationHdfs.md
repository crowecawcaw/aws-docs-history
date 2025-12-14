# DescribeLocationHdfs

Provides details about how an AWS DataSync transfer location for a Hadoop
Distributed File System (HDFS) is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationHdfs_RequestSyntax "#API_DescribeLocationHdfs_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the HDFS location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AgentArns": [ "***string***" ],
   "AuthenticationType": "***string***",
   "BlockSize": ***number***,
   "CreationTime": ***number***,
   "KerberosPrincipal": "***string***",
   "KmsKeyProviderUri": "***string***",
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "NameNodes": [
      {
         "Hostname": "***string***",
         "Port": ***number***
      }
   ],
   "QopConfiguration": {
      "DataTransferProtection": "***string***",
      "RpcProtection": "***string***"
   },
   "ReplicationFactor": ***number***,
   "SimpleUser": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AgentArns](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The ARNs of the DataSync agents that can connect with your HDFS cluster.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[AuthenticationType](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The type of authentication used to determine the identity of the user.

Type: String

Valid Values: `SIMPLE | KERBEROS`

**[BlockSize](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The size of the data blocks to write into the HDFS cluster.

Type: Integer

Valid Range: Minimum value of 1048576. Maximum value of 1073741824.

**[CreationTime](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The time that the HDFS location was created.

Type: Timestamp

**[KerberosPrincipal](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The Kerberos principal with access to the files and folders on the HDFS cluster. This
parameter is used if the `AuthenticationType` is defined as
`KERBEROS`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.+$`

**[KmsKeyProviderUri](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The URI of the HDFS cluster's Key Management Server (KMS).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^kms:\/\/http[s]?@(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9]))*:[0-9]{1,5}\/kms$`

**[LocationArn](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The ARN of the HDFS location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The URI of the HDFS location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[NameNodes](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The NameNode that manages the HDFS namespace.

Type: Array of [HdfsNameNode](API_HdfsNameNode.md "API_HdfsNameNode.md") objects

Array Members: Minimum number of 1 item.

**[QopConfiguration](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The Quality of Protection (QOP) configuration, which specifies the Remote Procedure Call
(RPC) and data transfer protection settings configured on the HDFS cluster.

Type: [QopConfiguration](API_QopConfiguration.md "API_QopConfiguration.md") object

**[ReplicationFactor](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The number of DataNodes to replicate the data to when writing to the HDFS cluster.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 512.

**[SimpleUser](#API_DescribeLocationHdfs_ResponseSyntax "#API_DescribeLocationHdfs_ResponseSyntax")**

The user name to identify the client on the host operating system. This parameter is used
if the `AuthenticationType` is defined as `SIMPLE`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[_.A-Za-z0-9][-_.A-Za-z0-9]*$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationHdfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationHdfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationHdfs.md")
