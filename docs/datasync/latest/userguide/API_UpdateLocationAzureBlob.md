# UpdateLocationAzureBlob

Modifies the following configurations of the Microsoft Azure Blob Storage transfer
location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with Azure Blob Storage](creating-azure-blob-location.md "creating-azure-blob-location.md").

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
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "`string`",
      "SecretArn": "`string`"
   },
   "LocationArn": "`string`",
   "SasConfiguration": {
      "Token": "`string`"
   },
   "Subdirectory": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[AccessTier](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies the access tier that you want your objects or files transferred into. This only
applies when using the location as a transfer destination. For more information, see [Access tiers](creating-azure-blob-location.md#azure-blob-access-tiers "creating-azure-blob-location.md#azure-blob-access-tiers").

Type: String

Valid Values: `HOT | COOL | ARCHIVE`

Required: No

**[AgentArns](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

(Optional) Specifies the Amazon Resource Name (ARN) of the DataSync agent that
can connect with your Azure Blob Storage container. If you are setting up an agentless
cross-cloud transfer, you do not need to specify a value for this parameter.

You can specify more than one agent. For more information, see [Using multiple
agents for your transfer](multiple-agents.md "multiple-agents.md").

###### Note

You cannot add or remove agents from a storage location after you initially create
it.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 8 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

Required: No

**[AuthenticationType](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies the authentication method DataSync uses to access your Azure Blob
Storage. DataSync can access blob storage using a shared access signature
(SAS).

Type: String

Valid Values: `SAS | NONE`

Required: No

**[BlobType](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies the type of blob that you want your objects or files to be when transferring
them into Azure Blob Storage. Currently, DataSync only supports moving data into
Azure Blob Storage as block blobs. For more information on blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs "https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs").

Type: String

Valid Values: `BLOCK`

Required: No

**[CmkSecretConfig](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies configuration information for a DataSync-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

Required: No

**[CustomSecretConfig](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies configuration information for a customer-managed secret, such as an
authentication token or set of credentials that DataSync uses to access a specific
transfer location, and a customer-managed AWS KMS key.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

Required: No

**[LocationArn](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies the ARN of the Azure Blob Storage transfer location that you're updating.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

**[SasConfiguration](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies the SAS configuration that allows DataSync to access your Azure Blob
Storage.

Type: [AzureBlobSasConfiguration](API_AzureBlobSasConfiguration.md "API_AzureBlobSasConfiguration.md") object

Required: No

**[Subdirectory](#API_UpdateLocationAzureBlob_RequestSyntax "#API_UpdateLocationAzureBlob_RequestSyntax")**

Specifies path segments if you want to limit your transfer to a virtual directory in your
container (for example, `/my/images`).

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^[\p{L}\p{M}\p{Z}\p{S}\p{N}\p{P}\p{C}]*$`

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/cli2/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForCpp/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/boto3/datasync-2018-11-09/UpdateLocationAzureBlob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationAzureBlob.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationAzureBlob.md")
