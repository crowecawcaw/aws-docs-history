# CreateLocationObjectStorage

Creates a transfer _location_ for an object storage system. AWS DataSync can use this location as a source or destination for transferring data. You
can make transfers with or without a [DataSync
agent](do-i-need-datasync-agent.md#when-agent-required "do-i-need-datasync-agent.md#when-agent-required").

Before you begin, make sure that you understand the [prerequisites](create-object-location.md#create-object-location-prerequisites "create-object-location.md#create-object-location-prerequisites") for DataSync to work with object storage systems.

## Request Syntax

```
{
   "AccessKey": "`string`",
   "AgentArns": [ "`string`" ],
   "BucketName": "`string`",
   "CmkSecretConfig": {
      "KmsKeyArn": "`string`",
      "SecretArn": "`string`"
   },
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "`string`",
      "SecretArn": "`string`"
   },
   "SecretKey": "`string`",
   "ServerCertificate": `blob`,
   "ServerHostname": "`string`",
   "ServerPort": `number`,
   "ServerProtocol": "`string`",
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

**[AccessKey](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the access key (for example, a user name) if credentials are required to
authenticate with the object storage server.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

Pattern: `^.*$`

Required: No

**[AgentArns](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

(Optional) Specifies the Amazon Resource Names (ARNs) of the DataSync agents
that can connect with your object storage system. If you are setting up an agentless
cross-cloud transfer, you do not need to specify a value for this parameter.

###### Note

Make sure you configure this parameter correctly when you first create your storage
location. You cannot add or remove agents from a storage location after you create
it.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 4 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**[BucketName](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the name of the object storage bucket involved in the transfer.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `^[a-zA-Z0-9_\-\+\.\(\)\$\p{Zs}]+$`

Required: Yes

**[CmkSecretConfig](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies configuration information for a DataSync-managed secret, which
includes the `SecretKey` that DataSync uses to access a specific object
storage location, with a customer-managed AWS KMS key.

When you include this paramater as part of a `CreateLocationObjectStorage`
request, you provide only the KMS key ARN. DataSync uses this KMS key together with the value you specify for the `SecretKey` parameter
to create a DataSync-managed secret to store the location access credentials.

Make sure the DataSync has permission to access the KMS key that
you specify.

###### Note

You can use either `CmkSecretConfig` (with `SecretKey`) or
`CustomSecretConfig` (without `SecretKey`) to provide credentials
for a `CreateLocationObjectStorage` request. Do not provide both parameters for
the same request.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

Required: No

**[CustomSecretConfig](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies configuration information for a customer-managed Secrets Manager secret where
the secret key for a specific object storage location is stored in plain text. This
configuration includes the secret ARN, and the ARN for an IAM role that
provides access to the secret.

###### Note

You can use either `CmkSecretConfig` (with `SecretKey`) or
`CustomSecretConfig` (without `SecretKey`) to provide credentials
for a `CreateLocationObjectStorage` request. Do not provide both parameters for
the same request.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

Required: No

**[SecretKey](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

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

**[ServerCertificate](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

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

Type: Base64-encoded binary data object

Length Constraints: Maximum length of 32768.

Required: No

**[ServerHostname](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the domain name or IP address (IPv4 or IPv6) of the object storage server that
your DataSync agent connects to.

Type: String

Length Constraints: Maximum length of 255.

Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`

Required: Yes

**[ServerPort](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the port that your object storage server accepts inbound network traffic on (for
example, port 443).

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 65536.

Required: No

**[ServerProtocol](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the protocol that your object storage server uses to communicate. If not specified, the default
value is `HTTPS`.

Type: String

Valid Values: `HTTPS | HTTP`

Required: No

**[Subdirectory](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the object prefix for your object storage server. If this is a source location,
DataSync only copies objects with this prefix. If this is a destination location,
DataSync writes all objects with this prefix.

Type: String

Length Constraints: Maximum length of 4096.

Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\p{Zs}]*$`

Required: No

**[Tags](#API_CreateLocationObjectStorage_RequestSyntax "#API_CreateLocationObjectStorage_RequestSyntax")**

Specifies the key-value pair that represents a tag that you want to add to the resource.
Tags can help you manage, filter, and search for your resources. We recommend creating a name
tag for your location.

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

**[LocationArn](#API_CreateLocationObjectStorage_ResponseSyntax "#API_CreateLocationObjectStorage_ResponseSyntax")**

Specifies the ARN of the object storage system location that you create.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationObjectStorage.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationObjectStorage.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationObjectStorage.md")
