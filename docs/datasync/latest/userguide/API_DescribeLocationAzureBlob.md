# DescribeLocationAzureBlob

Provides details about how an AWS DataSync transfer location for Microsoft Azure
Blob Storage is configured.

## Request Syntax

```
{
   "LocationArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[LocationArn](#API_DescribeLocationAzureBlob_RequestSyntax "#API_DescribeLocationAzureBlob_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of your Azure Blob Storage transfer
location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

Required: Yes

## Response Syntax

```
{
   "AccessTier": "***string***",
   "AgentArns": [ "***string***" ],
   "AuthenticationType": "***string***",
   "BlobType": "***string***",
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
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccessTier](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The access tier that you want your objects or files transferred into. This only applies
when using the location as a transfer destination. For more information, see [Access tiers](creating-azure-blob-location.md#azure-blob-access-tiers "creating-azure-blob-location.md#azure-blob-access-tiers").

Type: String

Valid Values: `HOT | COOL | ARCHIVE`

**[AgentArns](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The ARNs of the DataSync agents that can connect with your Azure Blob Storage
container.

Type: Array of strings

Array Members: Minimum number of 1 item. Maximum number of 4 items.

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

**[AuthenticationType](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The authentication method DataSync uses to access your Azure Blob Storage.
DataSync can access blob storage using a shared access signature (SAS).

Type: String

Valid Values: `SAS | NONE`

**[BlobType](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The type of blob that you want your objects or files to be when transferring them into
Azure Blob Storage. Currently, DataSync only supports moving data into Azure Blob
Storage as block blobs. For more information on blob types, see the [Azure Blob Storage documentation](https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs "https://learn.microsoft.com/en-us/rest/api/storageservices/understanding-block-blobs--append-blobs--and-page-blobs").

Type: String

Valid Values: `BLOCK`

**[CmkSecretConfig](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as an
authentication token that DataSync uses to access a specific storage location, with
a customer-managed AWS KMS key.

Type: [CmkSecretConfig](API_CmkSecretConfig.md "API_CmkSecretConfig.md") object

**[CreationTime](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The time that your Azure Blob Storage transfer location was created.

Type: Timestamp

**[CustomSecretConfig](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

Describes configuration information for a customer-managed secret, such as an
authentication token that DataSync uses to access a specific storage location, with
a customer-managed AWS KMS key.

Type: [CustomSecretConfig](API_CustomSecretConfig.md "API_CustomSecretConfig.md") object

**[LocationArn](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The ARN of your Azure Blob Storage transfer location.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

**[LocationUri](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

The URL of the Azure Blob Storage container involved in your transfer.

Type: String

Length Constraints: Maximum length of 4360.

Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

**[ManagedSecretConfig](#API_DescribeLocationAzureBlob_ResponseSyntax "#API_DescribeLocationAzureBlob_ResponseSyntax")**

Describes configuration information for a DataSync-managed secret, such as an
authentication token that DataSync uses to access a specific storage location.
DataSync uses the default AWS-managed KMS key to
encrypt this secret in AWS Secrets Manager.

Type: [ManagedSecretConfig](API_ManagedSecretConfig.md "API_ManagedSecretConfig.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/cli2/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForCpp/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/boto3/datasync-2018-11-09/DescribeLocationAzureBlob.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationAzureBlob.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationAzureBlob.md")
