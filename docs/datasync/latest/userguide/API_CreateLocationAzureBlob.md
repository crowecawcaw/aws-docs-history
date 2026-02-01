# CreateLocationAzureBlob

Creates a transfer _location_ for a Microsoft Azure Blob Storage
container. AWS DataSync can use this location as a transfer source or destination.
You can make transfers with or without a [DataSync agent](creating-azure-blob-location.md#azure-blob-creating-agent "creating-azure-blob-location.md#azure-blob-creating-agent") that connects to your
container.

Before you begin, make sure you know [how DataSync accesses Azure Blob Storage](creating-azure-blob-location.md#azure-blob-access "creating-azure-blob-location.md#azure-blob-access") and works with [access tiers](creating-azure-blob-location.md#azure-blob-access-tiers "creating-azure-blob-location.md#azure-blob-access-tiers") and [blob types](creating-azure-blob-location.md#blob-types "creating-azure-blob-location.md#blob-types").

## Request Syntax

```
{
   "AccessTier": "`string`",
   "AgentArns": [ "`string`" ],
   "AuthenticationType": "`string`",
   "BlobType": "`string`",
   "CmkSecretConfig": {
      "KmsKeyArn": "`string`",
      "SecretArn": "`string`"
   },
   "ContainerUrl": "`string`",
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "`string`",
      "SecretArn": "`string`"
   },
   "SasConfiguration": {
      "Token": "`string`"
   },
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

**[AccessTier](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies the access tier that you want your objects or files transferred into. This only
applies when using the location as a transfer destination. For more information, see [Access tiers](creating-azure-blob-location.md#azure-blob-access-tiers "creating-azure-blob-location.md#azure-blob-access-tiers").

Type: String

Valid Values: `HOT | COOL | ARCHIVE`

Required: No

**[AgentArns](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that
can connect with your Azure Blob Storage container. If you are setting up an agentless
cross-cloud transfer, you do not need to specify a value for this parameter.

You can specify more than one agent. For more information, see [Using multiple
agents for your transfer](multiple-agents.md "multiple-agents.md").

###### Note

Make sure you configure this parameter correctly when you first create your storage
location. You cannot add or remove agents from a storage location after you create
it.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**[AuthenticationType](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies the authentication method DataSync uses to access your Azure Blob
Storage. DataSync can access blob storage using a shared access signature
(SAS).

Type: String

Valid Values: `SAS | NONE`

Required: Yes

**[BlobType](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies the type of blob that you want your objects or files to be when transferring
them into Azure Blob Storage. Currently, DataSync only supports moving data into
Azure Blob Storage as block blobs. For more information on blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs "https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs").

Type: String

Valid Values: `BLOCK`

Required: No

**[CmkSecretConfig](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies configuration information for a DataSync-managed secret, which
includes the authentication token that DataSync uses to access a specific AzureBlob
storage location, with a customer-managed AWS KMS key.

When you include this parameter as part of a `CreateLocationAzureBlob` request,
you provide only the KMS key ARN. DataSync uses this KMS key together with the authentication token you specify for
`SasConfiguration` to create a DataSync-managed secret to store the
location access credentials.

Make sure that DataSync has permission to access the KMS key that
you specify.

###### Note

You can use either `CmkSecretConfig` (with `SasConfiguration`) or
`CustomSecretConfig` (without `SasConfiguration`) to provide
credentials for a `CreateLocationAzureBlob` request. Do not provide both
parameters for the same request.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

Required: No

**[ContainerUrl](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies the URL of the Azure Blob Storage container involved in your transfer.

Type: String

Length Constraints: Maximum length of 325.

Pattern: `^https:\/\/[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}\/[a-z0-9](-?[a-z0-9]){2,62}$`

Required: Yes

**[CustomSecretConfig](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies configuration information for a customer-managed Secrets Manager secret where
the authentication token for an AzureBlob storage location is stored in plain text, in Secrets
Manager. This configuration includes the secret ARN, and the ARN for an IAM role
that provides access to the secret.

###### Note

You can use either `CmkSecretConfig` (with `SasConfiguration`) or
`CustomSecretConfig` (without `SasConfiguration`) to provide
credentials for a `CreateLocationAzureBlob` request. Do not provide both
parameters for the same request.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

Required: No

**[SasConfiguration](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies the SAS configuration that allows DataSync to access your Azure Blob
Storage.

###### Note

If you provide an authentication token using `SasConfiguration`, but do not
provide secret configuration details using `CmkSecretConfig` or
`CustomSecretConfig`, then DataSync stores the token using your
AWS account's secrets manager secret.

Type: [AzureBlobSasConfiguration](API_AzureBlobSasConfiguration.md "API_AzureBlobSasConfiguration.md") object

Required: No

**[Subdirectory](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies path segments if you want to limit your transfer to a virtual directory in your
container (for example, `/my/images`).

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`

Required: No

**[Tags](#API_CreateLocationAzureBlob_RequestSyntax "#API_CreateLocationAzureBlob_RequestSyntax")**

Specifies labels that help you categorize, filter, and search for your AWS
resources. We recommend creating at least a name tag for your transfer location.

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

**[LocationArn](#API_CreateLocationAzureBlob_ResponseSyntax "#API_CreateLocationAzureBlob_ResponseSyntax")**

The ARN of the Azure Blob Storage transfer location that you created.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/cli2/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForCpp/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForGoV2/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForKotlin/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/boto3/datasync-2018-11-09/CreateLocationAzureBlob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationAzureBlob.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/CreateLocationAzureBlob.md")
