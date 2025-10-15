# UpdateBucketMetadataJournalTableConfiguration

Enables or disables journal table record expiration for an S3 Metadata configuration on a general 
 purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*.



Permissions

To use this operation, you must have the `s3:UpdateBucketMetadataJournalTableConfiguration`
 permission. For more information, see [Setting up permissions for
 configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the *Amazon S3 User Guide*. 



The following operations are related to `UpdateBucketMetadataJournalTableConfiguration`:


* [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md")
* [DeleteBucketMetadataConfiguration](API_DeleteBucketMetadataConfiguration.md "API_DeleteBucketMetadataConfiguration.md")
* [GetBucketMetadataConfiguration](API_GetBucketMetadataConfiguration.md "API_GetBucketMetadataConfiguration.md")
* [UpdateBucketMetadataInventoryTableConfiguration](API_UpdateBucketMetadataInventoryTableConfiguration.md "API_UpdateBucketMetadataInventoryTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?metadataJournalTable HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[JournalTableConfiguration](#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-JournalTableConfiguration "#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-JournalTableConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[RecordExpiration](#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-RecordExpiration "#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-RecordExpiration")>
      <[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>`integer`</[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>
      <[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>`string`</[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>
   </[RecordExpiration](#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-RecordExpiration "#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-RecordExpiration")>
</[JournalTableConfiguration](#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-JournalTableConfiguration "#AmazonS3-UpdateBucketMetadataJournalTableConfiguration-request-JournalTableConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**



 The general purpose bucket that corresponds to the metadata configuration that you want to 
 enable or disable journal table record expiration for.
 


Required: Yes




**[Content-MD5](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**



 The `Content-MD5` header for the journal table configuration.
 




**[x-amz-expected-bucket-owner](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**



 The expected owner of the general purpose bucket that corresponds to the metadata table 
 configuration that you want to enable or disable journal table record expiration for. 
 




**[x-amz-sdk-checksum-algorithm](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**



 The checksum algorithm to use with your journal table configuration.
 


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[JournalTableConfiguration](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**


Root level tag for the JournalTableConfiguration parameters.


Required: Yes




**[RecordExpiration](#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax "#API_UpdateBucketMetadataJournalTableConfiguration_RequestSyntax")**



 The journal table record expiration settings for the journal table.
 


Type: [RecordExpiration](API_RecordExpiration.md "API_RecordExpiration.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/UpdateBucketMetadataJournalTableConfiguration")
