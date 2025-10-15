# LifecycleRule

A lifecycle rule for individual objects in an Amazon S3 bucket.

For more information see, [Managing your storage lifecycle](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in
 the *Amazon S3 User Guide*.


## Contents





**Status** 


If 'Enabled', the rule is currently being applied. If 'Disabled', the rule is not currently being
 applied.


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


Specifies the expiration for the lifecycle of the object in the form of date, days and, whether the
 object has a delete marker.


Type: [LifecycleExpiration](API_LifecycleExpiration.md "API_LifecycleExpiration.md") data type


Required: No




**Filter** 


The `Filter` is used to identify objects that a Lifecycle Rule applies to. A
 `Filter` must have exactly one of `Prefix`, `Tag`,
 `ObjectSizeGreaterThan`, `ObjectSizeLessThan`, or `And` specified.
 `Filter` is required if the `LifecycleRule` does not contain a
 `Prefix` element.


For more information about `Tag` filters, see [Adding filters to Lifecycle rules](../userguide/intro-lifecycle-filters.md "../userguide/intro-lifecycle-filters.md")
 in the *Amazon S3 User Guide*.


###### Note


`Tag` filters are not supported for directory buckets.


Type: [LifecycleRuleFilter](API_LifecycleRuleFilter.md "API_LifecycleRuleFilter.md") data type


Required: No




**ID** 


Unique identifier for the rule. The value cannot be longer than 255 characters.


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




**NoncurrentVersionTransitions** 


Specifies the transition rule for the lifecycle rule that describes when noncurrent objects
 transition to a specific storage class. If your bucket is versioning-enabled (or versioning is
 suspended), you can set this action to request that Amazon S3 transition noncurrent object versions to a
 specific storage class at a set period in the object's lifetime.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: Array of [NoncurrentVersionTransition](API_NoncurrentVersionTransition.md "API_NoncurrentVersionTransition.md") data types


Required: No




**Prefix** 



*This member has been deprecated.*



 The general purpose bucket prefix that identifies one or more objects to which the rule applies. We recommend using `Filter` instead of `Prefix` for new PUTs. Previous configurations where a prefix is defined will continue to operate as before.


###### Important

Replacement must be made for object keys containing special characters (such as carriage returns) when using 
 XML requests. For more information, see [XML related object key constraints](../userguide/object-keys.md#object-key-xml-related-constraints "../userguide/object-keys.md#object-key-xml-related-constraints").


Type: String


Required: No




**Transitions** 


Specifies when an Amazon S3 object transitions to a specified storage class.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: Array of [Transition](API_Transition.md "API_Transition.md") data types


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleRule")
