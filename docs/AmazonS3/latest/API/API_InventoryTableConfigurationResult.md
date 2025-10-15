# InventoryTableConfigurationResult


 The inventory table configuration for an S3 Metadata configuration.
 


## Contents





**ConfigurationState** 



 The configuration state of the inventory table, indicating whether the inventory table is enabled 
 or disabled.
 


Type: String


Valid Values: `ENABLED | DISABLED`



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



 The Amazon Resource Name (ARN) for the inventory table.
 


Type: String


Required: No




**TableName** 



 The name of the inventory table.
 


Type: String


Required: No




**TableStatus** 


 The status of the inventory table. The status values are: 



* `CREATING` - The inventory table is in the process of being created in the specified
 AWS managed table bucket.
* `BACKFILLING` - The inventory table is in the process of being backfilled. When 
 you enable the inventory table for your metadata configuration, the table goes through a 
 process known as backfilling, during which Amazon S3 scans your general purpose bucket to retrieve 
 the initial metadata for all objects in the bucket. Depending on the number of objects in your 
 bucket, this process can take several hours. When the backfilling process is finished, the 
 status of your inventory table changes from `BACKFILLING` to `ACTIVE`. 
 After backfilling is completed, updates to your objects are reflected in the inventory table 
 within one hour.
* `ACTIVE` - The inventory table has been created successfully, and records are being
 delivered to the table.
* `FAILED` - Amazon S3 is unable to create the inventory table, or Amazon S3 is unable to deliver
 records.

Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryTableConfigurationResult")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryTableConfigurationResult")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryTableConfigurationResult "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryTableConfigurationResult")
