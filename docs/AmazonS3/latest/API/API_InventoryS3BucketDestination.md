# InventoryS3BucketDestination

Contains the bucket name, file format, bucket owner (optional), and prefix (optional) where
 S3 Inventory results are published.


## Contents





**Bucket** 


The Amazon Resource Name (ARN) of the bucket where inventory results will be published.


Type: String


Required: Yes




**Format** 


Specifies the output format of the inventory results.


Type: String


Valid Values: `CSV | ORC | Parquet`



Required: Yes




**AccountId** 


The account ID that owns the destination S3 bucket. If no account ID is provided, the owner is not
 validated before exporting data. 


###### Note

 Although this value is optional, we strongly recommend that you set it to help prevent problems
 if the destination bucket ownership changes. 


Type: String


Required: No




**Encryption** 


Contains the type of server-side encryption used to encrypt the inventory results.


Type: [InventoryEncryption](API_InventoryEncryption.md "API_InventoryEncryption.md") data type


Required: No




**Prefix** 


The prefix that is prepended to all inventory results.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryS3BucketDestination "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InventoryS3BucketDestination")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryS3BucketDestination "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InventoryS3BucketDestination")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryS3BucketDestination "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InventoryS3BucketDestination")
