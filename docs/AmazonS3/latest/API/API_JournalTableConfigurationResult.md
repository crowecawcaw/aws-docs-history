# JournalTableConfigurationResult


 The journal table configuration for the S3 Metadata configuration.
 


## Contents





**RecordExpiration** 



 The journal table record expiration settings for the journal table.
 


Type: [RecordExpiration](API_RecordExpiration.md "API_RecordExpiration.md") data type


Required: Yes




**TableName** 



 The name of the journal table.
 


Type: String


Required: Yes




**TableStatus** 


 The status of the journal table. The status values are: 



* `CREATING` - The journal table is in the process of being created in the specified
 table bucket.
* `ACTIVE` - The journal table has been created successfully, and records are being
 delivered to the table.
* `FAILED` - Amazon S3 is unable to create the journal table, or Amazon S3 is unable to deliver
 records.

Type: String


Required: Yes




**Error** 


 If an S3 Metadata V1 `CreateBucketMetadataTableConfiguration` or V2 
 `CreateBucketMetadataConfiguration` request succeeds, but S3 Metadata was
 unable to create the table, this structure contains the error code and error message. 


###### Note

If you created your S3 Metadata configuration before July 15, 2025, we recommend that you delete 
 and re-create your configuration by using [CreateBucketMetadataConfiguration](API_CreateBucketMetadataConfiguration.md "API_CreateBucketMetadataConfiguration.md") so that you can expire journal table records and create 
 a live inventory table.


Type: [ErrorDetails](API_ErrorDetails.md "API_ErrorDetails.md") data type


Required: No




**TableArn** 



 The Amazon Resource Name (ARN) for the journal table.
 


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/JournalTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/JournalTableConfigurationResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/JournalTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/JournalTableConfigurationResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/JournalTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/JournalTableConfigurationResult")
