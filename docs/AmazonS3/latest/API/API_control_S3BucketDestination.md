# S3BucketDestination

A container for the bucket where the Amazon S3 Storage Lens metrics export files are
 located.


## Contents





**AccountId** 


The account ID of the owner of the S3 Storage Lens metrics export bucket.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




**Arn** 


The Amazon Resource Name (ARN) of the bucket. This property is read-only and follows the
 following format: `arn:aws:s3:*us-east-1*:*example-account-id*:bucket/*your-destination-bucket-name*`



Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:s3:.*`



Required: Yes




**Format** 



Type: String


Valid Values: `CSV | Parquet`



Required: Yes




**OutputSchemaVersion** 


The schema version of the export file.


Type: String


Valid Values: `V_1`



Required: Yes




**Encryption** 


The container for the type encryption of the metrics exports in this bucket.


Type: [StorageLensDataExportEncryption](API_control_StorageLensDataExportEncryption.md "API_control_StorageLensDataExportEncryption.md") data type


Required: No




**Prefix** 


The prefix of the destination bucket where the metrics export will be delivered.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3BucketDestination "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3BucketDestination")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3BucketDestination "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3BucketDestination")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3BucketDestination "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3BucketDestination")
