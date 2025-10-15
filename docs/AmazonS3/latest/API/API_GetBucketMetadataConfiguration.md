# GetBucketMetadataConfiguration

Retrieves the S3 Metadata configuration for a general purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*. 

###### Note

You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 
 metadata configurations. However, if you try to use the V1 
 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you
 will receive an HTTP `405 Method Not Allowed` error.



Permissions

To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration`
 permission. For more information, see [Setting up permissions for
 configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the *Amazon S3 User Guide*. 


###### Note

The IAM policy action name is the same for the V1 and V2 API operations.



The following operations are related to `GetBucketMetadataConfiguration`:


* [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md")
* [DeleteBucketMetadataConfiguration](API_DeleteBucketMetadataConfiguration.md "API_DeleteBucketMetadataConfiguration.md")
* [UpdateBucketMetadataInventoryTableConfiguration](API_UpdateBucketMetadataInventoryTableConfiguration.md "API_UpdateBucketMetadataInventoryTableConfiguration.md")
* [UpdateBucketMetadataJournalTableConfiguration](API_UpdateBucketMetadataJournalTableConfiguration.md "API_UpdateBucketMetadataJournalTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?metadataConfiguration HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketMetadataConfiguration_RequestSyntax "#API_GetBucketMetadataConfiguration_RequestSyntax")**



 The general purpose bucket that corresponds to the metadata configuration that you want to
 retrieve.
 


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketMetadataConfiguration_RequestSyntax "#API_GetBucketMetadataConfiguration_RequestSyntax")**



 The expected owner of the general purpose bucket that you want to retrieve the metadata table
 configuration for.
 




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetBucketMetadataConfigurationResult](#AmazonS3-GetBucketMetadataConfiguration-response-GetBucketMetadataConfigurationResult "#AmazonS3-GetBucketMetadataConfiguration-response-GetBucketMetadataConfigurationResult")>
   <[MetadataConfigurationResult](#AmazonS3-GetBucketMetadataConfiguration-response-MetadataConfigurationResult "#AmazonS3-GetBucketMetadataConfiguration-response-MetadataConfigurationResult")>
      <[DestinationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-DestinationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-DestinationResult")>
         <[TableBucketArn](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketArn "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketArn")>***string***</[TableBucketArn](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketArn "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketArn")>
         <[TableBucketType](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketType "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketType")>***string***</[TableBucketType](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketType "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableBucketType")>
         <[TableNamespace](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableNamespace "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableNamespace")>***string***</[TableNamespace](API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableNamespace "API_DestinationResult.md#AmazonS3-Type-DestinationResult-TableNamespace")>
      </[DestinationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-DestinationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-DestinationResult")>
      <[InventoryTableConfigurationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-InventoryTableConfigurationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-InventoryTableConfigurationResult")>
         <[ConfigurationState](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-ConfigurationState "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-ConfigurationState")>***string***</[ConfigurationState](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-ConfigurationState "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-ConfigurationState")>
         <[Error](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-Error "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-Error")>
            <[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>***string***</[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>
            <[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>***string***</[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>
         </[Error](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-Error "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-Error")>
         <[TableArn](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableArn "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableArn")>***string***</[TableArn](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableArn "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableArn")>
         <[TableName](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableName "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableName")>***string***</[TableName](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableName "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableName")>
         <[TableStatus](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableStatus "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableStatus")>***string***</[TableStatus](API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableStatus "API_InventoryTableConfigurationResult.md#AmazonS3-Type-InventoryTableConfigurationResult-TableStatus")>
      </[InventoryTableConfigurationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-InventoryTableConfigurationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-InventoryTableConfigurationResult")>
      <[JournalTableConfigurationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-JournalTableConfigurationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-JournalTableConfigurationResult")>
         <[Error](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-Error "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-Error")>
            <[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>***string***</[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>
            <[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>***string***</[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>
         </[Error](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-Error "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-Error")>
         <[RecordExpiration](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-RecordExpiration "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-RecordExpiration")>
            <[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>***integer***</[Days](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Days")>
            <[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>***string***</[Expiration](API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration "API_RecordExpiration.md#AmazonS3-Type-RecordExpiration-Expiration")>
         </[RecordExpiration](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-RecordExpiration "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-RecordExpiration")>
         <[TableArn](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableArn "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableArn")>***string***</[TableArn](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableArn "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableArn")>
         <[TableName](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableName "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableName")>***string***</[TableName](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableName "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableName")>
         <[TableStatus](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableStatus "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableStatus")>***string***</[TableStatus](API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableStatus "API_JournalTableConfigurationResult.md#AmazonS3-Type-JournalTableConfigurationResult-TableStatus")>
      </[JournalTableConfigurationResult](API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-JournalTableConfigurationResult "API_MetadataConfigurationResult.md#AmazonS3-Type-MetadataConfigurationResult-JournalTableConfigurationResult")>
   </[MetadataConfigurationResult](#AmazonS3-GetBucketMetadataConfiguration-response-MetadataConfigurationResult "#AmazonS3-GetBucketMetadataConfiguration-response-MetadataConfigurationResult")>
</[GetBucketMetadataConfigurationResult](#AmazonS3-GetBucketMetadataConfiguration-response-GetBucketMetadataConfigurationResult "#AmazonS3-GetBucketMetadataConfiguration-response-GetBucketMetadataConfigurationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketMetadataConfigurationResult](#API_GetBucketMetadataConfiguration_ResponseSyntax "#API_GetBucketMetadataConfiguration_ResponseSyntax")**


Root level tag for the GetBucketMetadataConfigurationResult parameters.


Required: Yes




**[MetadataConfigurationResult](#API_GetBucketMetadataConfiguration_ResponseSyntax "#API_GetBucketMetadataConfiguration_ResponseSyntax")**



 The metadata configuration for a general purpose bucket.
 


Type: [MetadataConfigurationResult](API_MetadataConfigurationResult.md "API_MetadataConfigurationResult.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataConfiguration")
