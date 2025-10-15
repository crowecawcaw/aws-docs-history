# InventoryConfiguration

Specifies the S3 Inventory configuration for an Amazon S3 bucket. For more information, see [GET Bucket
 inventory](RESTBucketGETInventoryConfig.md "RESTBucketGETInventoryConfig.md") in the *Amazon S3 API Reference*. 


## Contents





**Destination** 


Contains information about where to publish the inventory results.


Type: [InventoryDestination](API_InventoryDestination.md "API_InventoryDestination.md") data type


Required: Yes




**Id** 


The ID used to identify the inventory configuration.


Type: String


Required: Yes




**IncludedObjectVersions** 


Object versions to include in the inventory list. If set to `All`, the list includes all
 the object versions, which adds the version-related fields `VersionId`,
 `IsLatest`, and `DeleteMarker` to the list. If set to `Current`, the
 list does not contain these version-related fields.


Type: String


Valid Values: `All | Current`



Required: Yes




**IsEnabled** 


Specifies whether the inventory is enabled or disabled. If set to `True`, an inventory
 list is generated. If set to `False`, no inventory list is generated.


Type: Boolean


Required: Yes




**Schedule** 


Specifies the schedule for generating inventory results.


Type: [InventorySchedule](API_InventorySchedule.md "API_InventorySchedule.md") data type


Required: Yes




**Filter** 


Specifies an inventory filter. The inventory only includes objects that meet the filter's
 criteria.


Type: [InventoryFilter](API_InventoryFilter.md "API_InventoryFilter.md") data type


Required: No




**OptionalFields** 


Contains the optional fields that are included in the inventory results.


Type: Array of strings


Valid Values: `Size | LastModifiedDate | StorageClass | ETag | IsMultipartUploaded | ReplicationStatus | EncryptionStatus | ObjectLockRetainUntilDate | ObjectLockMode | ObjectLockLegalHoldStatus | IntelligentTieringAccessTier | BucketKeyStatus | ChecksumAlgorithm | ObjectAccessControlList | ObjectOwner`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryConfiguration")
