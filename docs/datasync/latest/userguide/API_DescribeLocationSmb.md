# DescribeLocationSmb

Provides details about how an AWS DataSync transfer location for a Server
Message Block (SMB) file server is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationSmb_RequestSyntax "#API_DescribeLocationSmb_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the SMB location that you want information
about.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AgentArns": [ "***string***" ],
   "AuthenticationType": "***string***",
   "CmkSecretConfig": {
      "KmsKeyArn": "***string***",
      "SecretArn": "***string***"
   },
   "CreationTime": ***number***,
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "***string***",
      "SecretArn": "***string***"
   },
   "DnsIpAddresses": [ "***string***" ],
   "Domain": "***string***",
   "KerberosPrincipal": "***string***",
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "ManagedSecretConfig": {
      "SecretArn": "***string***"
   },
   "MountOptions": {
      "Version": "***string***"
   },
   "User": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AgentArns](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The ARNs of the DataSync agents that can connect with your SMB file
server.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[AuthenticationType](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The authentication protocol that DataSync uses to connect to your SMB file
server.

Type: String

Valid Values: `NTLM | KERBEROS`

**[CmkSecretConfig](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as a
`Password` or `KerberosKeytab` that DataSync uses to access
a specific storage location, with a customer-managed AWS KMS key.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

**[CreationTime](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The time that the SMB location was created.

Type: Timestamp

**[CustomSecretConfig](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

Describes configuration information for a customer-managed secret, such as a
`Password` or `KerberosKeytab` that DataSync uses to access
a specific storage location, with a customer-managed AWS KMS key.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

**[DnsIpAddresses](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The IPv4 or IPv6 addresses for the DNS servers that your SMB file server belongs to. This element
applies only if `AuthenticationType` is set to `KERBEROS`.

Type: Array of strings

Array Members: Maximum number of 2 items.

Length Constraints: Minimum length of 7. Maximum length of 39.

Pattern: `\A((25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))\z`

**[Domain](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The name of the Windows domain that the SMB file server belongs to. This element applies
only if `AuthenticationType` is set to `NTLM`.

Type: String

Length Constraints: Maximum length of 253.

Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`

**[KerberosPrincipal](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The Kerberos principal that has permission to access the files, folders, and file metadata
in your SMB file server.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^.+$`

**[LocationArn](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The ARN of the SMB location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The URI of the SMB location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[ManagedSecretConfig](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as a
`Password` or `KerberosKeytab` that DataSync uses to access
a specific storage location. DataSync uses the default AWS-managed
KMS key to encrypt this secret in AWS Secrets Manager.

Type: [ManagedSecretConfig](API_ManagedSecretConfig.md "API_ManagedSecretConfig.md") object

**[MountOptions](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The SMB protocol version that DataSync uses to access your SMB file
server.

Type: [SmbMountOptions](API_SmbMountOptions.md "API_SmbMountOptions.md") object

**[User](#API_DescribeLocationSmb_ResponseSyntax "#API_DescribeLocationSmb_ResponseSyntax")**

The user that can mount and access the files, folders, and file metadata in your SMB file
server. This element applies only if `AuthenticationType` is set to
`NTLM`.

Type: String

Length Constraints: Maximum length of 104.

Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`

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

This example illustrates one usage of DescribeLocationSmb.

#### Sample Request

```
{
  "arn:aws:datasync:us-east-1:111222333444:location/loc-0f01451b140b2af49"
}
```

### Example

This example illustrates one usage of DescribeLocationSmb.

#### Sample Response

```
{
   "AgentArns":[
      "arn:aws:datasync:us-east-2:111222333444:agent/agent-0bc3b3dc9bbc15145",
      "arn:aws:datasync:us-east-2:111222333444:agent/agent-04b3fe3d261a18c8f"
   ],
   "CreationTime":"1532660733.39",
   "Domain":"AMAZON",
   "LocationArn":"arn:aws:datasync:us-east-1:111222333444:location/loc-0f01451b140b2af49",
   "LocationUri":"smb://hostname.amazon.com/share",
   "MountOptions":{
      "Version":"SMB3"
   },
   "User":"user-1"
}

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationSmb.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationSmb.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationSmb.md")
