# CreateLocationHdfs

Creates a transfer _location_ for a Hadoop Distributed File System
(HDFS). AWS DataSync can use this location as a source or destination for
transferring data.

Before you begin, make sure that you understand how DataSync
[accesses HDFS
clusters](create-hdfs-location.md#accessing-hdfs "create-hdfs-location.md#accessing-hdfs").

## Request Syntax

```
{
   "AgentArns": [ "`string`" ],
   "AuthenticationType": "`string`",
   "BlockSize": `number`,
   "CmkSecretConfig": {
      "KmsKeyArn": "`string`",
      "SecretArn": "`string`"
   },
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "`string`",
      "SecretArn": "`string`"
   },
   "KerberosKeytab": `blob`,
   "KerberosKrb5Conf": `blob`,
   "KerberosPrincipal": "`string`",
   "KmsKeyProviderUri": "`string`",
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

**[AgentArns](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your
HDFS cluster.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: Yes

**[AuthenticationType](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The type of authentication used to determine the identity of the user.

Type: String

Valid Values: `SIMPLE | KERBEROS`

Required: Yes

**[BlockSize](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The size of data blocks to write into the HDFS cluster. The block size must be a multiple
of 512 bytes. The default block size is 128 mebibytes (MiB).

Type: Integer

Valid Range: Minimum value of 1048576. Maximum value of 1073741824.

Required: No

**[CmkSecretConfig](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

Specifies configuration information for a DataSync-managed secret, which
includes the Kerberos keytab that DataSync uses to access a specific Hadoop
Distributed File System (HDFS) storage location, with a
customer-managed AWS KMS key.

When you include this parameter as part of a `CreateLocationHdfs` request,
you provide only the KMS key ARN. DataSync uses this KMS key together with the `KerberosKeytab` you specify for
to create a DataSync-managed secret to store the location access credentials.

Make sure that DataSync has permission to access the KMS key that
you specify. For more information, see [Using a service-managed secret encrypted with a custom AWS KMS key](location-credentials.md#service-secret-custom-key "location-credentials.md#service-secret-custom-key").

###### Note

You can use either `CmkSecretConfig` (with `KerberosKeytab`) or
`CustomSecretConfig` (without `KerberosKeytab`) to provide
credentials for a `CreateLocationHdfs` request. Do not provide both
parameters for the same request.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

Required: No

**[CustomSecretConfig](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

Specifies configuration information for a customer-managed Secrets Manager secret where
the Kerberos keytab for the HDFS storage location is stored in binary, in Secrets
Manager. This configuration includes the secret ARN, and the ARN for an IAM role
that provides access to the secret. For more information, see [Using a secret that you manage](location-credentials.md#custom-secret-custom-key "location-credentials.md#custom-secret-custom-key").

###### Note

You can use either `CmkSecretConfig` (with `KerberosKeytab`) or
`CustomSecretConfig` (without `KerberosKeytab`) to provide
credentials for a `CreateLocationHdfs` request. Do not provide both
parameters for the same request.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

Required: No

**[KerberosKeytab](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The Kerberos key table (keytab) that contains mappings between the defined Kerberos
principal and the encrypted keys. You can load the keytab from a file by providing the file's
address.

###### Note

If `KERBEROS` is specified for `AuthenticationType`, this
parameter is required.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 65536.

Required: No

**[KerberosKrb5Conf](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The `krb5.conf` file that contains the Kerberos configuration information. You
can load the `krb5.conf` file by providing the file's address. If you're using the
AWS CLI, it performs the base64 encoding for you. Otherwise, provide the
base64-encoded text.

###### Note

If `KERBEROS` is specified for `AuthenticationType`, this
parameter is required.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 131072.

Required: No

**[KerberosPrincipal](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The Kerberos principal with access to the files and folders on the HDFS cluster.

###### Note

If `KERBEROS` is specified for `AuthenticationType`, this
parameter is required.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.+$`

Required: No

**[KmsKeyProviderUri](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The URI of the HDFS cluster's Key Management Server (KMS).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^kms:\/\/http[s]?@(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9]))*:[0-9]{1,5}\/kms$`

Required: No

**[NameNodes](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The NameNode that manages the HDFS namespace. The NameNode performs operations such as
opening, closing, and renaming files and directories. The NameNode contains the information to
map blocks of data to the DataNodes. You can use only one NameNode.

Type: Array of [HdfsNameNode](API_HdfsNameNode.md "API_HdfsNameNode.md") objects

Array Members: Minimum number of 1 item.

Required: Yes

**[QopConfiguration](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC)
and data transfer protection settings configured on the Hadoop Distributed File System (HDFS)
cluster. If `QopConfiguration` isn't specified, `RpcProtection` and
`DataTransferProtection` default to `PRIVACY`. If you set
`RpcProtection` or `DataTransferProtection`, the other parameter
assumes the same value.

Type: [QopConfiguration](API_QopConfiguration.md "API_QopConfiguration.md") object

Required: No

**[ReplicationFactor](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The number of DataNodes to replicate the data to when writing to the HDFS cluster. By
default, data is replicated to three DataNodes.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 512.

Required: No

**[SimpleUser](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The user name used to identify the client on the host operating system.

###### Note

If `SIMPLE` is specified for `AuthenticationType`, this parameter
is required.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^[_.A-Za-z0-9][-_.A-Za-z0-9]*$`

Required: No

**[Subdirectory](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write
data to the HDFS cluster. If the subdirectory isn't specified, it will default to
`/`.

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`

Required: No

**[Tags](#API_CreateLocationHdfs_RequestSyntax "#API_CreateLocationHdfs_RequestSyntax")**

The key-value pair that represents the tag that you want to add to the location. The value
can be an empty string. We recommend using tags to name your resources.

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

**[LocationArn](#API_CreateLocationHdfs_ResponseSyntax "#API_CreateLocationHdfs_ResponseSyntax")**

The ARN of the source HDFS cluster location that you create.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

## Errors

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationHdfs.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationHdfs.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationHdfs.md")
