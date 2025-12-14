# UpdateLocationHdfs

Modifies the following configuration parameters of the Hadoop Distributed File System
(HDFS) transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with an HDFS cluster](create-hdfs-location.md "create-hdfs-location.md").

## Request Syntax

```
{
   "AgentArns": [ "`string`" ],
   "AuthenticationType": "`string`",
   "BlockSize": `number`,
   "KerberosKeytab": `blob`,
   "KerberosKrb5Conf": `blob`,
   "KerberosPrincipal": "`string`",
   "KmsKeyProviderUri": "`string`",
   "LocationArn": "`string`",
   "NameNodes": [
      {
         "Hostname": "`string`",
         "Port": `number`
      }
   ],
   "QopConfiguration": {
      "DataTransferProtection": "`string`",
      "RpcProtection": "`string`"
   },
   "ReplicationFactor": `number`,
   "SimpleUser": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AgentArns](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your
HDFS cluster.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**[AuthenticationType](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The type of authentication used to determine the identity of the user.

Type: String

Valid Values: `SIMPLE | KERBEROS`

Required: No

**[BlockSize](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The size of the data blocks to write into the HDFS cluster.

Type: Integer

Valid Range: Minimum value of 1048576. Maximum value of 1073741824.

Required: No

**[KerberosKeytab](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The Kerberos key table (keytab) that contains mappings between the defined Kerberos
principal and the encrypted keys. You can load the keytab from a file by providing the file's
address.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 65536.

Required: No

**[KerberosKrb5Conf](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The `krb5.conf` file that contains the Kerberos configuration information. You
can load the `krb5.conf` file by providing the file's address. If you're using the
AWS CLI, it performs the base64 encoding for you. Otherwise, provide the
base64-encoded text.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 131072.

Required: No

**[KerberosPrincipal](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The Kerberos principal with access to the files and folders on the HDFS cluster.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.+$`

Required: No

**[KmsKeyProviderUri](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The URI of the HDFS cluster's Key Management Server (KMS).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^kms:\/\/http[s]?@(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9]))*:[0-9]{1,5}\/kms$`

Required: No

**[LocationArn](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The Amazon Resource Name (ARN) of the source HDFS cluster location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[NameNodes](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The NameNode that manages the HDFS namespace. The NameNode performs operations such as
opening, closing, and renaming files and directories. The NameNode contains the information to
map blocks of data to the DataNodes. You can use only one NameNode.

Type: Array of [HdfsNameNode](API_HdfsNameNode.md "API_HdfsNameNode.md") objects

Array Members: Minimum number of 1 item.

Required: No

**[QopConfiguration](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC)
and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS)
cluster.

Type: [QopConfiguration](API_QopConfiguration.md "API_QopConfiguration.md") object

Required: No

**[ReplicationFactor](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The number of DataNodes to replicate the data to when writing to the HDFS cluster.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 512.

Required: No

**[SimpleUser](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

The user name used to identify the client on the host operating system.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[_.A-Za-z0-9][-_.A-Za-z0-9]*$`

Required: No

**[Subdirectory](#API_UpdateLocationHdfs_RequestSyntax "#API_UpdateLocationHdfs_RequestSyntax")**

A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write
data to the HDFS cluster.

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationHdfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationHdfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationHdfs.md")
