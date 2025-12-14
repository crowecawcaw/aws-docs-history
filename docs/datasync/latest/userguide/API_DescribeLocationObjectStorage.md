# DescribeLocationObjectStorage

Provides details about how an AWS DataSync transfer location for an object
storage system is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationObjectStorage_RequestSyntax "#API_DescribeLocationObjectStorage_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the object storage system location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AccessKey": "***string***",
   "AgentArns": [ "***string***" ],
   "CmkSecretConfig": {
      "KmsKeyArn": "***string***",
      "SecretArn": "***string***"
   },
   "CreationTime": ***number***,
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "***string***",
      "SecretArn": "***string***"
   },
   "LocationArn": "***string***",
   "LocationUri": "***string***",
   "ManagedSecretConfig": {
      "SecretArn": "***string***"
   },
   "ServerCertificate": ***blob***,
   "ServerPort": ***number***,
   "ServerProtocol": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccessKey](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The access key (for example, a user name) required to authenticate with the object storage
system.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Pattern: `^.*$`

**[AgentArns](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The ARNs of the DataSync agents that can connect with your object storage
system.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[CmkSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

**[CreationTime](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The time that the location was created.

Type: Timestamp

**[CustomSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

Describes configuration information for a customer-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

**[LocationArn](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The ARN of the object storage system location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The URI of the object storage system location.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[ManagedSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.

Type: [ManagedSecretConfig](API_ManagedSecretConfig.md "API_ManagedSecretConfig.md") object

**[ServerCertificate](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The certificate chain for DataSync to authenticate with your object storage
system if the system uses a private or self-signed certificate authority (CA).

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 32768.

**[ServerPort](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The port that your object storage server accepts inbound network traffic on (for example,
port 443).

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 65536.

**[ServerProtocol](#API_DescribeLocationObjectStorage_ResponseSyntax "#API_DescribeLocationObjectStorage_ResponseSyntax")**

The protocol that your object storage system uses to communicate.

Type: String

Valid Values: `HTTPS | HTTP`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationObjectStorage.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationObjectStorage.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationObjectStorage.md")
