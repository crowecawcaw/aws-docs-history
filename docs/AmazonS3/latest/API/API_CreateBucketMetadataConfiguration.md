# CreateBucketMetadataConfiguration

Creates an S3 Metadata V2 metadata configuration for a general purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*.



Permissions

To use this operation, you must have the following permissions. For more information, see
 [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.


If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service
 (AWS KMS) keys (SSE-KMS), you need additional permissions in your KMS key policy. For more
 information, see [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.


If you also want to integrate your table bucket with AWS analytics services so that you can
 query your metadata table, you need additional permissions. For more information, see  [Integrating
 Amazon S3 Tables with AWS analytics services](../userguide/s3-tables-integrating-aws.md "../userguide/s3-tables-integrating-aws.md") in the
 *Amazon S3 User Guide*.


To query your metadata tables, you need additional permissions. For more information, see 
 [Permissions for querying metadata tables](../userguide/metadata-tables-bucket-query-permissions.md "../userguide/metadata-tables-bucket-query-permissions.md") in the *Amazon S3 User Guide*.



* `s3:CreateBucketMetadataTableConfiguration`



###### Note

The IAM policy action name is the same for the V1 and V2 API operations.
* `s3tables:CreateTableBucket`
* `s3tables:CreateNamespace`
* `s3tables:GetTable`
* `s3tables:CreateTable`
* `s3tables:PutTablePolicy`
* `s3tables:PutTableEncryption`
* `kms:DescribeKey`


The following operations are related to `CreateBucketMetadataConfiguration`:


* [DeleteBucketMetadataConfiguration](API_DeleteBucketMetadataConfiguration.md "API_DeleteBucketMetadataConfiguration.md")
* [GetBucketMetadataConfiguration](API_GetBucketMetadataConfiguration.md "API_GetBucketMetadataConfiguration.md")
* [UpdateBucketMetadataInventoryTableConfiguration](API_UpdateBucketMetadataInventoryTableConfiguration.md "API_UpdateBucketMetadataInventoryTableConfiguration.md")
* [UpdateBucketMetadataJournalTableConfiguration](API_UpdateBucketMetadataJournalTableConfiguration.md "API_UpdateBucketMetadataJournalTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /?metadataConfiguration HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[MetadataConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-MetadataConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-MetadataConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[JournalTableConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-JournalTableConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-JournalTableConfiguration")>
      <[EncryptionConfiguration](API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-EncryptionConfiguration "API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-EncryptionConfiguration")>
         <[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>`string`</[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>
         <[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>`string`</[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>
      </[EncryptionConfiguration](API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-EncryptionConfiguration "API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-EncryptionConfiguration")>
      <[RecordExpiration](API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-RecordExpiration "API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-RecordExpiration")>
         <[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>`integer`</[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>
         <[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>`string`</[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>
      </[RecordExpiration](API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-RecordExpiration "API_JournalTableConfiguration.md#AmazonS3-Type-JournalTableConfiguration-RecordExpiration")>
   </[JournalTableConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-JournalTableConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-JournalTableConfiguration")>
   <[InventoryTableConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-InventoryTableConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-InventoryTableConfiguration")>
      <[ConfigurationState](API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-ConfigurationState "API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-ConfigurationState")>`string`</[ConfigurationState](API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-ConfigurationState "API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-ConfigurationState")>
      <[EncryptionConfiguration](API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-EncryptionConfiguration "API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-EncryptionConfiguration")>
         <[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>`string`</[KmsKeyArn](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-KmsKeyArn")>
         <[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>`string`</[SseAlgorithm](API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm "API_MetadataTableEncryptionConfiguration.md#AmazonS3-Type-MetadataTableEncryptionConfiguration-SseAlgorithm")>
      </[EncryptionConfiguration](API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-EncryptionConfiguration "API_InventoryTableConfiguration.md#AmazonS3-Type-InventoryTableConfiguration-EncryptionConfiguration")>
   </[InventoryTableConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-InventoryTableConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-InventoryTableConfiguration")>
</[MetadataConfiguration](#AmazonS3-CreateBucketMetadataConfiguration-request-MetadataConfiguration "#AmazonS3-CreateBucketMetadataConfiguration-request-MetadataConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The general purpose bucket that you want to create the metadata configuration for.
 


Required: Yes




**[Content-MD5](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The `Content-MD5` header for the metadata configuration.
 




**[x-amz-expected-bucket-owner](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The expected owner of the general purpose bucket that corresponds to your metadata configuration.
 




**[x-amz-sdk-checksum-algorithm](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The checksum algorithm to use with your metadata configuration.
 


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[MetadataConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**


Root level tag for the MetadataConfiguration parameters.


Required: Yes




**[InventoryTableConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The inventory table configuration for a metadata configuration.
 


Type: [InventoryTableConfiguration](API_InventoryTableConfiguration.md "API_InventoryTableConfiguration.md") data type


Required: No




**[JournalTableConfiguration](#API_CreateBucketMetadataConfiguration_RequestSyntax "#API_CreateBucketMetadataConfiguration_RequestSyntax")**



 The journal table configuration for a metadata configuration.
 


Type: [JournalTableConfiguration](API_JournalTableConfiguration.md "API_JournalTableConfiguration.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateBucketMetadataConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketMetadataConfiguration")
