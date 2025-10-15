# UpdateBucketMetadataInventoryTableConfiguration

Enables or disables a live inventory table for an S3 Metadata configuration on a general 
 purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*.



Permissions

To use this operation, you must have the following permissions. For more information, see
 [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.


If you want to encrypt your inventory table with server-side encryption with AWS Key Management Service
 (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more
 information, see [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.



* `s3:UpdateBucketMetadataInventoryTableConfiguration`
* `s3tables:CreateTableBucket`
* `s3tables:CreateNamespace`
* `s3tables:GetTable`
* `s3tables:CreateTable`
* `s3tables:PutTablePolicy`
* `s3tables:PutTableEncryption`
* `kms:DescribeKey`


The following operations are related to `UpdateBucketMetadataInventoryTableConfiguration`:


* [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md")
* [DeleteBucketMetadataConfiguration](API_DeleteBucketMetadataConfiguration.md "API_DeleteBucketMetadataConfiguration.md")
* [GetBucketMetadataConfiguration](API_GetBucketMetadataConfiguration.md "API_GetBucketMetadataConfiguration.md")
* [UpdateBucketMetadataJournalTableConfiguration](API_UpdateBucketMetadataJournalTableConfiguration.md "API_UpdateBucketMetadataJournalTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?metadataInventoryTable HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[InventoryTableConfiguration](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-InventoryTableConfiguration "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-InventoryTableConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[ConfigurationState](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-ConfigurationState "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-ConfigurationState")>`string`</[ConfigurationState](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-ConfigurationState "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-ConfigurationState")>
   <[EncryptionConfiguration](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-EncryptionConfiguration "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-EncryptionConfiguration")>
      <[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>`string`</[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>
      <[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>`string`</[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>
   </[EncryptionConfiguration](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-EncryptionConfiguration "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-EncryptionConfiguration")>
</[InventoryTableConfiguration](#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-InventoryTableConfiguration "#AmazonS3-UpdateBucketMetadataInventoryTableConfiguration-request-InventoryTableConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The general purpose bucket that corresponds to the metadata configuration that you want to 
 enable or disable an inventory table for.
 


Required: Yes




**[Content-MD5](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The `Content-MD5` header for the inventory table configuration.
 




**[x-amz-expected-bucket-owner](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The expected owner of the general purpose bucket that corresponds to the metadata table 
 configuration that you want to enable or disable an inventory table for.
 




**[x-amz-sdk-checksum-algorithm](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The checksum algorithm to use with your inventory table configuration.
 


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[InventoryTableConfiguration](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**


Root level tag for the InventoryTableConfiguration parameters.


Required: Yes




**[ConfigurationState](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The configuration state of the inventory table, indicating whether the inventory table is enabled 
 or disabled.
 


Type: String


Valid Values: `ENABLED | DISABLED`



Required: Yes




**[EncryptionConfiguration](#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataInventoryTableConfiguration_RequestSyntax")**



 The encryption configuration for the inventory table.
 


Type: [MetadataTableEncryptionConfiguration](API_MetadataTableEncryptionConfiguration.md "API_MetadataTableEncryptionConfiguration.md") data type


Required: No




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataInventoryTableConfiguration")
