# CreateBucketMetadataTableConfiguration

###### Important


 We recommend that you create your S3 Metadata configurations by using the V2 
 [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md") API operation. We no longer recommend using the V1 
 `CreateBucketMetadataTableConfiguration` API operation.
 

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete 
 and re-create your configuration by using [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md") so that you can expire journal table records and create 
 a live inventory table.

Creates a V1 S3 Metadata configuration for a general purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*.



Permissions

To use this operation, you must have the following permissions. For more information, see
 [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.


If you want to encrypt your metadata tables with server-side encryption with AWS Key Management Service
 (AWS KMS) keys (SSE-KMS), you need additional permissions. For more
 information, see [Setting up permissions for configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the
 *Amazon S3 User Guide*.


If you also want to integrate your table bucket with AWS analytics services so that you can
 query your metadata table, you need additional permissions. For more information, see  [Integrating
 Amazon S3 Tables with AWS analytics services](../userguide/s3-tables-integrating-aws.md "../userguide/s3-tables-integrating-aws.md") in the
 *Amazon S3 User Guide*.



* `s3:CreateBucketMetadataTableConfiguration`
* `s3tables:CreateNamespace`
* `s3tables:GetTable`
* `s3tables:CreateTable`
* `s3tables:PutTablePolicy`


The following operations are related to `CreateBucketMetadataTableConfiguration`:


* [DeleteBucketMetadataTableConfiguration](API_DeleteBucketMetadataTableConfiguration.md "API_DeleteBucketMetadataTableConfiguration.md")
* [GetBucketMetadataTableConfiguration](API_GetBucketMetadataTableConfiguration.md "API_GetBucketMetadataTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /?metadataTable HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
Content-MD5: `ContentMD5`
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
<?xml version="1.0" encoding="UTF-8"?>
<[MetadataTableConfiguration](#AmazonS3-CreateBucketMetadataTableConfiguration-request-MetadataTableConfiguration "#AmazonS3-CreateBucketMetadataTableConfiguration-request-MetadataTableConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[S3TablesDestination](#AmazonS3-CreateBucketMetadataTableConfiguration-request-S3TablesDestination "#AmazonS3-CreateBucketMetadataTableConfiguration-request-S3TablesDestination")>
      <[TableBucketArn](API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableBucketArn "API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableBucketArn")>`string`</[TableBucketArn](API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableBucketArn "API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableBucketArn")>
      <[TableName](API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableName "API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableName")>`string`</[TableName](API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableName "API_S3TablesDestination.md#AmazonS3-Type-S3TablesDestination-TableName")>
   </[S3TablesDestination](#AmazonS3-CreateBucketMetadataTableConfiguration-request-S3TablesDestination "#AmazonS3-CreateBucketMetadataTableConfiguration-request-S3TablesDestination")>
</[MetadataTableConfiguration](#AmazonS3-CreateBucketMetadataTableConfiguration-request-MetadataTableConfiguration "#AmazonS3-CreateBucketMetadataTableConfiguration-request-MetadataTableConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


 The general purpose bucket that you want to create the metadata table configuration for. 


Required: Yes




**[Content-MD5](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


 The `Content-MD5` header for the metadata table configuration. 




**[x-amz-expected-bucket-owner](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


 The expected owner of the general purpose bucket that corresponds to your metadata table configuration.
 




**[x-amz-sdk-checksum-algorithm](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


 The checksum algorithm to use with your metadata table configuration. 


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





## Request Body


The request accepts the following data in XML format.





**[MetadataTableConfiguration](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


Root level tag for the MetadataTableConfiguration parameters.


Required: Yes




**[S3TablesDestination](#API_CreateBucketMetadataTableConfiguration_RequestSyntax "#API_CreateBucketMetadataTableConfiguration_RequestSyntax")**


 The destination information for the metadata table configuration. The destination table bucket must
 be in the same Region and AWS account as the general purpose bucket. The specified metadata table name
 must be unique within the `aws_s3_metadata` namespace in the destination table bucket.
 


Type: [S3TablesDestination](API_S3TablesDestination.md "API_S3TablesDestination.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/CreateBucketMetadataTableConfiguration")
