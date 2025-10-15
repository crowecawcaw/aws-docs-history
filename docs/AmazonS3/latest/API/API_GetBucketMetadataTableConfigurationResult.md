# GetBucketMetadataTableConfigurationResult

 The V1 S3 Metadata configuration for a general purpose bucket. 

###### Note

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete 
 and re-create your configuration by using [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md") so that you can expire journal table records and create 
 a live inventory table.


## Contents





**MetadataTableConfigurationResult** 


 The V1 S3 Metadata configuration for a general purpose bucket. 


Type: [MetadataTableConfigurationResult](API_MetadataTableConfigurationResult.md "API_MetadataTableConfigurationResult.md") data type


Required: Yes




**Status** 


 The status of the metadata table. The status values are: 



* `CREATING` - The metadata table is in the process of being created in the specified
 table bucket.
* `ACTIVE` - The metadata table has been created successfully, and records are being
 delivered to the table.
* `FAILED` - Amazon S3 is unable to create the metadata table, or Amazon S3 is unable to deliver
 records. See `ErrorDetails` for details.

Type: String


Required: Yes




**Error** 


 If the `CreateBucketMetadataTableConfiguration` request succeeds, but S3 Metadata was
 unable to create the table, this structure contains the error code and error message. 


Type: [ErrorDetails](API_ErrorDetails.md "API_ErrorDetails.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/GetBucketMetadataTableConfigurationResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/GetBucketMetadataTableConfigurationResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/GetBucketMetadataTableConfigurationResult")
