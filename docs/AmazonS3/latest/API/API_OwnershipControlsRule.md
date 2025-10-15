# OwnershipControlsRule

The container element for an ownership control rule.


## Contents





**ObjectOwnership** 


The container element for object ownership for a bucket's ownership controls.



`BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket
 owner if the objects are uploaded with the `bucket-owner-full-control` canned ACL.



`ObjectWriter` - The uploading account will own the object if the object is uploaded with
 the `bucket-owner-full-control` canned ACL.



`BucketOwnerEnforced` - Access control lists (ACLs) are disabled and no longer affect
 permissions. The bucket owner automatically owns and has full control over every object in the bucket.
 The bucket only accepts PUT requests that don't specify an ACL or specify bucket owner full control ACLs
 (such as the predefined `bucket-owner-full-control` canned ACL or a custom ACL in XML format
 that grants the same permissions).


By default, `ObjectOwnership` is set to `BucketOwnerEnforced` and ACLs are
 disabled. We recommend keeping ACLs disabled, except in uncommon use cases where you must control access
 for each object individually. For more information about S3 Object Ownership, see [Controlling
 ownership of objects and disabling ACLs for your bucket](../userguide/about-object-ownership.md "../userguide/about-object-ownership.md") in the
 *Amazon S3 User Guide*. 


###### Note

This functionality is not supported for directory buckets. Directory buckets use the bucket owner enforced setting for S3 Object Ownership.


Type: String


Valid Values: `BucketOwnerPreferred | ObjectWriter | BucketOwnerEnforced`



Required: Yes




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/OwnershipControlsRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/OwnershipControlsRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/OwnershipControlsRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/OwnershipControlsRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/OwnershipControlsRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/OwnershipControlsRule")
