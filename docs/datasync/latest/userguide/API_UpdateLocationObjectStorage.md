# UpdateLocationObjectStorage

Modifies the following configuration parameters of the object storage transfer location
that you're using with AWS DataSync.

For more information, see [Configuring DataSync
transfers with an object storage system](create-object-location.md "create-object-location.md").

## Request Syntax

```
{
   "AccessKey": "`string`",
   "AgentArns": [ "`string`" ],
   "CmkSecretConfig": {
      "KmsKeyArn": "`string`",
      "SecretArn": "`string`"
   },
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "`string`",
      "SecretArn": "`string`"
   },
   "LocationArn": "`string`",
   "SecretKey": "`string`",
   "ServerCertificate": `blob`,
   "ServerHostname": "`string`",
   "ServerPort": `number`,
   "ServerProtocol": "`string`",
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AccessKey](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the access key (for example, a user name) if credentials are required to
authenticate with the object storage server.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Pattern: `^.*$`

Required: No

**[AgentArns](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents
that can connect with your object storage system. If you are setting up an agentless
cross-cloud transfer, you do not need to specify a value for this parameter.

###### Note

You cannot add or remove agents from a storage location after you initially create
it.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**[CmkSecretConfig](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies configuration information for a DataSync-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

Required: No

**[CustomSecretConfig](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies configuration information for a customer-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

Required: No

**[LocationArn](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the ARN of the object storage system location that you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[SecretKey](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the secret key (for example, a password) if credentials are required to
authenticate with the object storage server.

###### Note

If you provide a secret using `SecretKey`, but do not provide secret
configuration details using `CmkSecretConfig` or `CustomSecretConfig`,
then DataSync stores the token using your AWS account's Secrets Manager secret.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Pattern: `^.*$`

Required: No

**[ServerCertificate](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies a certificate chain for DataSync to authenticate with your object
storage system if the system uses a private or self-signed certificate authority (CA). You
must specify a single `.pem` file with a full certificate chain (for example,
`file:///home/user/.ssh/object_storage_certificates.pem`).

The certificate chain might include:

- The object storage system's certificate
- All intermediate certificates (if there are any)
- The root certificate of the signing CA

You can concatenate your certificates into a `.pem` file (which can be up to
32768 bytes before base64 encoding). The following example `cat` command creates an
`object_storage_certificates.pem` file that includes three certificates:

`cat object_server_certificate.pem intermediate_certificate.pem
 ca_root_certificate.pem > object_storage_certificates.pem`

To use this parameter, configure `ServerProtocol` to `HTTPS`.

Updating this parameter doesn't interfere with tasks that you have in progress.

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 32768.

Required: No

**[ServerHostname](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that
your DataSync agent connects to.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`

Required: No

**[ServerPort](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the port that your object storage server accepts inbound network traffic on (for
example, port 443).

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 65536.

Required: No

**[ServerProtocol](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the protocol that your object storage server uses to communicate.

Type: String

Valid Values: `HTTPS | HTTP`

Required: No

**[Subdirectory](#API_UpdateLocationObjectStorage_RequestSyntax "#API_UpdateLocationObjectStorage_RequestSyntax")**

Specifies the object prefix for your object storage server. If this is a source location,
DataSync only copies objects with this prefix. If this is a destination location, DataSync
writes all objects with this prefix.

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationObjectStorage.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationObjectStorage.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationObjectStorage.md")
