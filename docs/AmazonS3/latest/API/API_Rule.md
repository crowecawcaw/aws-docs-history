# Rule

Specifies lifecycle rules for an Amazon S3 bucket. For more information, see [Put Bucket Lifecycle Configuration](RESTBucketPUTlifecycle.md "RESTBucketPUTlifecycle.md") in
 the *Amazon S3 API Reference*. For examples, see [Put Bucket Lifecycle Configuration Examples](API_PutBucketLifecycleConfiguration.md#API_PutBucketLifecycleConfiguration_Examples "API_PutBucketLifecycleConfiguration.md#API_PutBucketLifecycleConfiguration_Examples").


## Contents





**Prefix** 


Object key prefix that identifies one or more objects to which this rule applies.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: Yes




**Status** 


If `Enabled`, the rule is currently being applied. If `Disabled`, the rule is
 not currently being applied.


Type: String


Valid Values: `Enabled | Disabled`



Required: Yes




**AbortIncompleteMultipartUpload** 


Specifies the days since the initiation of an incomplete multipart upload that Amazon S3 will wait before
 permanently removing all parts of the upload. For more information, see  [Aborting
 Incomplete Multipart Uploads Using a Bucket Lifecycle Configuration](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config "https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config") in the
 *Amazon S3 User Guide*.


Type: [AbortIncompleteMultipartUpload](API_AbortIncompleteMultipartUpload.md "API_AbortIncompleteMultipartUpload.md") data type


Required: No




**Expiration** 


Specifies the expiration for the lifecycle of the object.


Type: [LifecycleExpiration](API_LifecycleExpiration.md "API_LifecycleExpiration.md") data type


Required: No




**ID** 


Unique identifier for the rule. The value can't be longer than 255 characters.


Type: String


Required: No




**NoncurrentVersionExpiration** 


Specifies when noncurrent object versions expire. Upon expiration, Amazon S3 permanently deletes the
 noncurrent object versions. You set this lifecycle configuration action on a bucket that has versioning
 enabled (or suspended) to request that Amazon S3 delete noncurrent object versions at a specific period in
 the object's lifetime.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: [NoncurrentVersionExpiration](API_NoncurrentVersionExpiration.md "API_NoncurrentVersionExpiration.md") data type


Required: No




**NoncurrentVersionTransition** 


Container for the transition rule that describes when noncurrent objects transition to the
 `STANDARD_IA`, `ONEZONE_IA`, `INTELLIGENT_TIERING`,
 `GLACIER_IR`, `GLACIER`, or `DEEP_ARCHIVE` storage class. If your
 bucket is versioning-enabled (or versioning is suspended), you can set this action to request that Amazon S3
 transition noncurrent object versions to the `STANDARD_IA`, `ONEZONE_IA`,
 `INTELLIGENT_TIERING`, `GLACIER_IR`, `GLACIER`, or
 `DEEP_ARCHIVE` storage class at a specific period in the object's lifetime.


Type: [NoncurrentVersionTransition](API_NoncurrentVersionTransition.md "API_NoncurrentVersionTransition.md") data type


Required: No




**Transition** 


Specifies when an object transitions to a specified storage class. For more information about Amazon S3
 lifecycle configuration rules, see [Transitioning Objects Using
 Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/lifecycle-transition-general-considerations.html") in the *Amazon S3 User Guide*.


Type: [Transition](API_Transition.md "API_Transition.md") data type


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Rule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/Rule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Rule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/Rule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Rule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/Rule")
