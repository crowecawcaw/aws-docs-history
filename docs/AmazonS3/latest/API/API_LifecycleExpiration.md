# LifecycleExpiration

Container for the expiration for the lifecycle of the object.

For more information see, [Managing your storage lifecycle](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md") in
 the *Amazon S3 User Guide*.


## Contents





**Date** 


Indicates at what date the object is to be moved or deleted. The date value must conform to the ISO
 8601 format. The time is always midnight UTC.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: Timestamp


Required: No




**Days** 


Indicates the lifetime, in days, of the objects that are subject to the rule. The value must be a
 non-zero positive integer.


Type: Integer


Required: No




**ExpiredObjectDeleteMarker** 


Indicates whether Amazon S3 will remove a delete marker with no noncurrent versions. If set to true, the
 delete marker will be expired; if set to false the policy takes no action. This cannot be specified with
 Days or Date in a Lifecycle Expiration Policy.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.


Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleExpiration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/LifecycleExpiration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleExpiration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/LifecycleExpiration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleExpiration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/LifecycleExpiration")
