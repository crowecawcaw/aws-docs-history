# GetBucketMetadataTableConfiguration

###### Important


 We recommend that you retrieve your S3 Metadata configurations by using the V2 
 [GetBucketMetadataTableConfiguration](API_GetBucketMetadataTableConfiguration.md "API_GetBucketMetadataTableConfiguration.md") API operation. We no longer recommend using the V1 
 `GetBucketMetadataTableConfiguration` API operation.
 

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete 
 and re-create your configuration by using [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md") so that you can expire journal table records and create 
 a live inventory table.

 Retrieves the V1 S3 Metadata configuration for a general purpose bucket. For more information, see
 [Accelerating
 data discovery with S3 Metadata](../userguide/metadata-tables-overview.md "../userguide/metadata-tables-overview.md") in the *Amazon S3 User Guide*. 

###### Note

You can use the V2 `GetBucketMetadataConfiguration` API operation with V1 or V2 
 metadata table configurations. However, if you try to use the V1 
 `GetBucketMetadataTableConfiguration` API operation with V2 configurations, you
 will receive an HTTP `405 Method Not Allowed` error.

Make sure that you update your processes to use the new V2 API operations
 (`CreateBucketMetadataConfiguration`, `GetBucketMetadataConfiguration`, and
 `DeleteBucketMetadataConfiguration`) instead of the V1 API operations. 



Permissions

To use this operation, you must have the `s3:GetBucketMetadataTableConfiguration`
 permission. For more information, see [Setting up permissions for
 configuring metadata tables](../userguide/metadata-tables-permissions.md "../userguide/metadata-tables-permissions.md") in the *Amazon S3 User Guide*. 



The following operations are related to `GetBucketMetadataTableConfiguration`:


* [CreateBucketMetadataTableConfiguration](API_CreateBucketMetadataTableConfiguration.md "API_CreateBucketMetadataTableConfiguration.md")
* [DeleteBucketMetadataTableConfiguration](API_DeleteBucketMetadataTableConfiguration.md "API_DeleteBucketMetadataTableConfiguration.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /?metadataTable HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-expected-bucket-owner: `ExpectedBucketOwner`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_GetBucketMetadataTableConfiguration_RequestSyntax "#API_GetBucketMetadataTableConfiguration_RequestSyntax")**


 The general purpose bucket that corresponds to the metadata table configuration that you want to
 retrieve. 


Required: Yes




**[x-amz-expected-bucket-owner](#API_GetBucketMetadataTableConfiguration_RequestSyntax "#API_GetBucketMetadataTableConfiguration_RequestSyntax")**


 The expected owner of the general purpose bucket that you want to retrieve the metadata table
 configuration for. 




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetBucketMetadataTableConfigurationResult](#AmazonS3-GetBucketMetadataTableConfiguration-response-GetBucketMetadataTableConfigurationResult "#AmazonS3-GetBucketMetadataTableConfiguration-response-GetBucketMetadataTableConfigurationResult")>
   <[MetadataTableConfigurationResult](#AmazonS3-GetBucketMetadataTableConfiguration-response-MetadataTableConfigurationResult "#AmazonS3-GetBucketMetadataTableConfiguration-response-MetadataTableConfigurationResult")>
      <[S3TablesDestinationResult](API_MetadataTableConfigurationResult.md#AmazonS3-Type-MetadataTableConfigurationResult-S3TablesDestinationResult "API_MetadataTableConfigurationResult.md#AmazonS3-Type-MetadataTableConfigurationResult-S3TablesDestinationResult")>
         <[TableArn](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableArn "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableArn")>***string***</[TableArn](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableArn "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableArn")>
         <[TableBucketArn](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableBucketArn "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableBucketArn")>***string***</[TableBucketArn](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableBucketArn "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableBucketArn")>
         <[TableName](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableName "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableName")>***string***</[TableName](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableName "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableName")>
         <[TableNamespace](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableNamespace "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableNamespace")>***string***</[TableNamespace](API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableNamespace "API_S3TablesDestinationResult.md#AmazonS3-Type-S3TablesDestinationResult-TableNamespace")>
      </[S3TablesDestinationResult](API_MetadataTableConfigurationResult.md#AmazonS3-Type-MetadataTableConfigurationResult-S3TablesDestinationResult "API_MetadataTableConfigurationResult.md#AmazonS3-Type-MetadataTableConfigurationResult-S3TablesDestinationResult")>
   </[MetadataTableConfigurationResult](#AmazonS3-GetBucketMetadataTableConfiguration-response-MetadataTableConfigurationResult "#AmazonS3-GetBucketMetadataTableConfiguration-response-MetadataTableConfigurationResult")>
   <[Status](#AmazonS3-GetBucketMetadataTableConfiguration-response-Status "#AmazonS3-GetBucketMetadataTableConfiguration-response-Status")>***string***</[Status](#AmazonS3-GetBucketMetadataTableConfiguration-response-Status "#AmazonS3-GetBucketMetadataTableConfiguration-response-Status")>
   <[Error](#AmazonS3-GetBucketMetadataTableConfiguration-response-Error "#AmazonS3-GetBucketMetadataTableConfiguration-response-Error")>
      <[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>***string***</[ErrorCode](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorCode")>
      <[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>***string***</[ErrorMessage](API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage "API_ErrorDetails.md#AmazonS3-Type-ErrorDetails-ErrorMessage")>
   </[Error](#AmazonS3-GetBucketMetadataTableConfiguration-response-Error "#AmazonS3-GetBucketMetadataTableConfiguration-response-Error")>
</[GetBucketMetadataTableConfigurationResult](#AmazonS3-GetBucketMetadataTableConfiguration-response-GetBucketMetadataTableConfigurationResult "#AmazonS3-GetBucketMetadataTableConfiguration-response-GetBucketMetadataTableConfigurationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetBucketMetadataTableConfigurationResult](#API_GetBucketMetadataTableConfiguration_ResponseSyntax "#API_GetBucketMetadataTableConfiguration_ResponseSyntax")**


Root level tag for the GetBucketMetadataTableConfigurationResult parameters.


Required: Yes




**[Error](#API_GetBucketMetadataTableConfiguration_ResponseSyntax "#API_GetBucketMetadataTableConfiguration_ResponseSyntax")**


 If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was
 unable to create the table, this structure contains the error code and error message. 


Type: [ErrorDetails](API_ErrorDetails.md "API_ErrorDetails.md") data type




**[MetadataTableConfigurationResult](#API_GetBucketMetadataTableConfiguration_ResponseSyntax "#API_GetBucketMetadataTableConfiguration_ResponseSyntax")**


 The V1 S3 Metadata configuration for a general purpose bucket. 


Type: [MetadataTableConfigurationResult](API_MetadataTableConfigurationResult.md "API_MetadataTableConfigurationResult.md") data type




**[Status](#API_GetBucketMetadataTableConfiguration_ResponseSyntax "#API_GetBucketMetadataTableConfiguration_ResponseSyntax")**


 The status of the metadata table. The status values are: 



* `CREATING` - The metadata table is in the process of being created in the specified
 table bucket.
* `ACTIVE` - The metadata table has been created successfully, and records are being
 delivered to the table.
* `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver
 records. See `ErrorDetails` for details.

Type: String




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/GetBucketMetadataTableConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfiguration")
