# S3SetObjectRetentionOperation

Contains the configuration parameters for the Object Lock retention action for an
 S3 Batch Operations job. Batch Operations passes every object to the underlying
 `PutObjectRetention`
 API
 operation. For more information, see [Using S3 Object Lock retention
 with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html") in the *Amazon S3 User Guide*.

###### Note

This functionality is not supported by directory buckets.


## Contents





**Retention** 


Contains the Object Lock retention mode to be applied to all objects in the Batch Operations
 job. For more information, see [Using S3 Object Lock retention
 with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-retention-date.html") in the *Amazon S3 User Guide*.


Type: [S3Retention](API_control_S3Retention.md "API_control_S3Retention.md") data type


Required: Yes




**BypassGovernanceRetention** 


Indicates if the action should be applied to objects in the Batch Operations job even if they
 have Object Lock  `GOVERNANCE` type in place.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectRetentionOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectRetentionOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectRetentionOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectRetentionOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectRetentionOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectRetentionOperation")
