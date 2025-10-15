# S3SetObjectLegalHoldOperation

Contains the configuration for an S3 Object Lock legal hold operation that an
 S3 Batch Operations job passes
 to
 every object to the underlying
 `PutObjectLegalHold`
 API
 operation. For more information, see [Using S3 Object Lock legal hold
 with S3 Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/batch-ops-legal-hold.html") in the *Amazon S3 User Guide*.

###### Note

This functionality is not supported by directory buckets.


## Contents





**LegalHold** 


Contains the Object Lock legal hold status to be applied to all objects in the
 Batch Operations job.


Type: [S3ObjectLockLegalHold](API_control_S3ObjectLockLegalHold.md "API_control_S3ObjectLockLegalHold.md") data type


Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectLegalHoldOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3SetObjectLegalHoldOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectLegalHoldOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3SetObjectLegalHoldOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectLegalHoldOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3SetObjectLegalHoldOperation")
