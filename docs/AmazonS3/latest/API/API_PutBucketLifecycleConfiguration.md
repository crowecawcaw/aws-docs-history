# PutBucketLifecycleConfiguration

Creates a new lifecycle configuration for the bucket or replaces an existing lifecycle
 configuration. Keep in mind that this will overwrite an existing lifecycle configuration, so if you want
 to retain any configuration details, they must be included in the new lifecycle configuration. For
 information about lifecycle configuration, see [Managing your storage
 lifecycle](../userguide/object-lifecycle-mgmt.md "../userguide/object-lifecycle-mgmt.md").

###### Note

Bucket lifecycle configuration now supports specifying a lifecycle rule using an object key name
 prefix, one or more object tags, object size, or any combination of these. Accordingly, this section
 describes the latest API. The previous version of the API supported filtering based only on an object
 key name prefix, which is supported for backward compatibility. For the related API description, see
 [PutBucketLifecycle](API_PutBucketLifecycle.md "API_PutBucketLifecycle.md").



Rules

You specify the lifecycle configuration in your request body. The lifecycle configuration is
 specified as XML consisting of one or more rules. An Amazon S3 Lifecycle configuration can have up to
 1,000 rules. This limit is not adjustable.


Bucket lifecycle configuration supports specifying a lifecycle rule using an object key name
 prefix, one or more object tags, object size, or any combination of these. Accordingly, this
 section describes the latest API. The previous version of the API supported filtering based only
 on an object key name prefix, which is supported for backward compatibility for general purpose
 buckets. For the related API description, see [PutBucketLifecycle](API_PutBucketLifecycle.md "API_PutBucketLifecycle.md"). 


###### Note

Lifecyle configurations for directory buckets only support expiring objects and cancelling
 multipart uploads. Expiring of versioned objects,transitions and tag filters are not
 supported.


A lifecycle rule consists of the following:



* A filter identifying a subset of objects to which the rule applies. The filter can be
 based on a key name prefix, object tags, object size, or any combination of these.
* A status indicating whether the rule is in effect.
* One or more lifecycle transition and expiration actions that you want Amazon S3 to perform on
 the objects identified by the filter. If the state of your bucket is versioning-enabled or
 versioning-suspended, you can have many versions of the same object (one current version and
 zero or more noncurrent versions). Amazon S3 provides predefined actions that you can specify for
 current and noncurrent object versions.

For more information, see [Object Lifecycle Management](https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html") and
 [Lifecycle
 Configuration Elements](https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/intro-lifecycle-rules.html").



Permissions


* **General purpose bucket permissions** - By default, all Amazon S3
 resources are private, including buckets, objects, and related subresources (for example,
 lifecycle configuration and website configuration). Only the resource owner (that is, the
 AWS account that created it) can access the resource. The resource owner can optionally
 grant access permissions to others by writing an access policy. For this operation, a user
 must have the `s3:PutLifecycleConfiguration` permission.


You can also explicitly deny permissions. An explicit deny also supersedes any other
 permissions. If you want to block users or accounts from removing or deleting objects from
 your bucket, you must deny them permissions for the following actions:




	+ `s3:DeleteObject`
	+ `s3:DeleteObjectVersion`
	+ `s3:PutLifecycleConfiguration`
	
	
	
	For more information about permissions, see [Managing Access Permissions to
	 Your Amazon S3 Resources](../userguide/s3-access-control.md "../userguide/s3-access-control.md").


* **Directory bucket permissions** - You must have the
 `s3express:PutLifecycleConfiguration` permission in an IAM identity-based policy
 to use this operation. Cross-account access to this API operation isn't supported. The
 resource owner can optionally grant access permissions to others by creating a role or user
 for them as long as they are within the same account as the owner and resource.


For more information about directory bucket policies and permissions, see [Authorizing Regional endpoint APIs with IAM](../userguide/s3-express-security-iam.md "../userguide/s3-express-security-iam.md") in the *Amazon S3 User
 Guide*.


###### Note


**Directory buckets**  - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format `https://s3express-control.*region-code*.amazonaws.com/*bucket-name*`. Virtual-hosted-style requests aren't supported. 
For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](../userguide/endpoint-directory-buckets-AZ.md "../userguide/endpoint-directory-buckets-AZ.md") in the
 *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](../userguide/s3-lzs-for-directory-buckets.md "../userguide/s3-lzs-for-directory-buckets.md") in the
 *Amazon S3 User Guide*.


HTTP Host header syntax


**Directory buckets**  - The HTTP Host header syntax is
 `s3express-control.*region*.amazonaws.com`.


The following operations are related to `PutBucketLifecycleConfiguration`:



* [GetBucketLifecycleConfiguration](API_GetBucketLifecycleConfiguration.md "API_GetBucketLifecycleConfiguration.md")
* [DeleteBucketLifecycle](API_DeleteBucketLifecycle.md "API_DeleteBucketLifecycle.md")


###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /?lifecycle HTTP/1.1
Host: `Bucket`.s3.amazonaws.com
x-amz-sdk-checksum-algorithm: `ChecksumAlgorithm`
x-amz-expected-bucket-owner: `ExpectedBucketOwner`
x-amz-transition-default-minimum-object-size: `TransitionDefaultMinimumObjectSize`
<?xml version="1.0" encoding="UTF-8"?>
<[LifecycleConfiguration](#AmazonS3-PutBucketLifecycleConfiguration-request-LifecycleConfiguration "#AmazonS3-PutBucketLifecycleConfiguration-request-LifecycleConfiguration") xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <[Rule](#AmazonS3-PutBucketLifecycleConfiguration-request-Rules "#AmazonS3-PutBucketLifecycleConfiguration-request-Rules")>
      <[AbortIncompleteMultipartUpload](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload")>
         <[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>`integer`</[DaysAfterInitiation](API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation "API_AbortIncompleteMultipartUpload.md#AmazonS3-Type-AbortIncompleteMultipartUpload-DaysAfterInitiation")>
      </[AbortIncompleteMultipartUpload](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-AbortIncompleteMultipartUpload")>
      <[Expiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration")>
         <[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>`timestamp`</[Date](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Date")>
         <[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>`integer`</[Days](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-Days")>
         <[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>`boolean`</[ExpiredObjectDeleteMarker](API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker "API_LifecycleExpiration.md#AmazonS3-Type-LifecycleExpiration-ExpiredObjectDeleteMarker")>
      </[Expiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Expiration")>
      <[Filter](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter")>
         <[And](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And")>
            <[ObjectSizeGreaterThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan")>`long`</[ObjectSizeGreaterThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeGreaterThan")>
            <[ObjectSizeLessThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan")>`long`</[ObjectSizeLessThan](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-ObjectSizeLessThan")>
            <[Prefix](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix")>`string`</[Prefix](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Prefix")>
            <[Tag](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags")>
               <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
               <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
            </[Tag](API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags "API_LifecycleRuleAndOperator.md#AmazonS3-Type-LifecycleRuleAndOperator-Tags")>
            ...
         </[And](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-And")>
         <[ObjectSizeGreaterThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan")>`long`</[ObjectSizeGreaterThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeGreaterThan")>
         <[ObjectSizeLessThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan")>`long`</[ObjectSizeLessThan](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-ObjectSizeLessThan")>
         <[Prefix](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix")>`string`</[Prefix](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Prefix")>
         <[Tag](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag")>
            <[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>`string`</[Key](API_Tag.md#AmazonS3-Type-Tag-Key "API_Tag.md#AmazonS3-Type-Tag-Key")>
            <[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>`string`</[Value](API_Tag.md#AmazonS3-Type-Tag-Value "API_Tag.md#AmazonS3-Type-Tag-Value")>
         </[Tag](API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag "API_LifecycleRuleFilter.md#AmazonS3-Type-LifecycleRuleFilter-Tag")>
      </[Filter](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Filter")>
      <[ID](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID")>`string`</[ID](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-ID")>
      <[NoncurrentVersionExpiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>`integer`</[NewerNoncurrentVersions](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>`integer`</[NoncurrentDays](API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays "API_NoncurrentVersionExpiration.md#AmazonS3-Type-NoncurrentVersionExpiration-NoncurrentDays")>
      </[NoncurrentVersionExpiration](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionExpiration")>
      <[NoncurrentVersionTransition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions")>
         <[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>`integer`</[NewerNoncurrentVersions](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NewerNoncurrentVersions")>
         <[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>`integer`</[NoncurrentDays](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-NoncurrentDays")>
         <[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>`string`</[StorageClass](API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass "API_NoncurrentVersionTransition.md#AmazonS3-Type-NoncurrentVersionTransition-StorageClass")>
      </[NoncurrentVersionTransition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-NoncurrentVersionTransitions")>
      ...
      <[Prefix](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix")>`string`</[Prefix](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Prefix")>
      <[Status](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status")>`string`</[Status](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Status")>
      <[Transition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions")>
         <[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>`timestamp`</[Date](API_Transition.md#AmazonS3-Type-Transition-Date "API_Transition.md#AmazonS3-Type-Transition-Date")>
         <[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>`integer`</[Days](API_Transition.md#AmazonS3-Type-Transition-Days "API_Transition.md#AmazonS3-Type-Transition-Days")>
         <[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>`string`</[StorageClass](API_Transition.md#AmazonS3-Type-Transition-StorageClass "API_Transition.md#AmazonS3-Type-Transition-StorageClass")>
      </[Transition](API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions "API_LifecycleRule.md#AmazonS3-Type-LifecycleRule-Transitions")>
      ...
   </[Rule](#AmazonS3-PutBucketLifecycleConfiguration-request-Rules "#AmazonS3-PutBucketLifecycleConfiguration-request-Rules")>
   ...
</[LifecycleConfiguration](#AmazonS3-PutBucketLifecycleConfiguration-request-LifecycleConfiguration "#AmazonS3-PutBucketLifecycleConfiguration-request-LifecycleConfiguration")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Bucket](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


The name of the bucket for which to set the configuration.


Required: Yes




**[x-amz-expected-bucket-owner](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


The account ID of the expected bucket owner. If the account ID that you provide does not match the actual owner of the bucket, the request fails with the HTTP status code `403 Forbidden` (access denied).


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.




**[x-amz-sdk-checksum-algorithm](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


Indicates the algorithm used to create the checksum for the request when you use the SDK. This header will not provide any
 additional functionality if you don't use the SDK. When you send this header, there must be a corresponding `x-amz-checksum` or
 `x-amz-trailer` header sent. Otherwise, Amazon S3 fails the request with the HTTP status code `400 Bad Request`. For more
 information, see [Checking object integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in
 the *Amazon S3 User Guide*.


If you provide an individual checksum, Amazon S3 ignores any provided `ChecksumAlgorithm`
 parameter.


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`





**[x-amz-transition-default-minimum-object-size](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


Indicates which default minimum object size behavior is applied to the lifecycle
 configuration.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.



* `all_storage_classes_128K` - Objects smaller than 128 KB will not transition to
 any storage class by default.
* `varies_by_storage_class` - Objects smaller than 128 KB will transition to Glacier
 Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes
 will prevent transitions smaller than 128 KB.

To customize the minimum object size for any transition you can add a filter that specifies a custom
 `ObjectSizeGreaterThan` or `ObjectSizeLessThan` in the body of your transition
 rule. Custom filters always take precedence over the default transition behavior.


Valid Values: `varies_by_storage_class | all_storage_classes_128K`





## Request Body


The request accepts the following data in XML format.





**[LifecycleConfiguration](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


Root level tag for the LifecycleConfiguration parameters.


Required: Yes




**[Rule](#API_PutBucketLifecycleConfiguration_RequestSyntax "#API_PutBucketLifecycleConfiguration_RequestSyntax")**


A lifecycle rule for individual objects in an Amazon S3 bucket.


Type: Array of [LifecycleRule](API_LifecycleRule.md "API_LifecycleRule.md") data types


Required: Yes




## Response Syntax



```
HTTP/1.1 200
x-amz-transition-default-minimum-object-size: `TransitionDefaultMinimumObjectSize`

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[x-amz-transition-default-minimum-object-size](#API_PutBucketLifecycleConfiguration_ResponseSyntax "#API_PutBucketLifecycleConfiguration_ResponseSyntax")**


Indicates which default minimum object size behavior is applied to the lifecycle
 configuration.


###### Note

This parameter applies to general purpose buckets only. It is not supported for directory bucket
 lifecycle configurations.



* `all_storage_classes_128K` - Objects smaller than 128 KB will not transition to
 any storage class by default.
* `varies_by_storage_class` - Objects smaller than 128 KB will transition to Glacier
 Flexible Retrieval or Glacier Deep Archive storage classes. By default, all other storage classes
 will prevent transitions smaller than 128 KB.

To customize the minimum object size for any transition you can add a filter that specifies a custom
 `ObjectSizeGreaterThan` or `ObjectSizeLessThan` in the body of your transition
 rule. Custom filters always take precedence over the default transition behavior.


Valid Values: `varies_by_storage_class | all_storage_classes_128K`





## Examples


### Example 1: Add lifecycle configuration - bucket not versioning-enabled


The following lifecycle configuration for a general purpose bucket specifies two rules, each
 with one action.



* The `Transition` action requests Amazon S3 to transition objects with the "documents/"
 prefix to the GLACIER storage class 30 days after creation.
* The `Expiration` action requests Amazon S3 to delete objects with the "logs/" prefix
 365 days after creation.


```

            
<LifecycleConfiguration>
  <Rule>
    <ID>id1</ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>GLACIER</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
         
```

### Example 2: Adding a lifecycle configuration to a general purpose bucket


The following is a sample `PUT /?lifecycle` request that adds the preceding lifecycle
 configuration to a general purpose bucket.



```

PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:11:21 GMT
Content-MD5: q6yJDlIkcBaGGfb3QLY69A==
Authorization: authorization string
Content-Length: 415

<LifecycleConfiguration>
  <Rule>
    <ID>id1</ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Transition>
      <Days>30</Days>
      <StorageClass>GLACIER</StorageClass>
    </Transition>
  </Rule>
  <Rule>
    <ID>id2</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <Expiration>
      <Days>365</Days>
    </Expiration>
  </Rule>
</LifecycleConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketLifecycleConfiguration.



```

HTTP/1.1 200 OK
x-amz-id-2: r+qR7+nhXtJDDIJ0JJYcd+1j5nM/rUFiiiZ/fNbDOsd3JUE8NWMLNHXmvPfwMpdc
x-amz-request-id: 9E26D08072A8EF9E
Date: Wed, 14 May 2014 02:11:22 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Example 3: Add a lifecycle configuration - bucket is versioning-enabled


The following lifecycle configuration for a general purpose bucket specifies two rules, each
 with one action for Amazon S3 to perform. You specify these actions when your bucket is
 versioning-enabled or versioning is suspended:



* The `NoncurrentVersionExpiration` action requests Amazon S3 to expire noncurrent
 versions of objects with the "logs/" prefix 100 days after the objects become noncurrent.
* The `NoncurrentVersionTransition` action requests Amazon S3 to transition noncurrent
 versions of objects with the "documents/" prefix to the GLACIER storage class 30 days after they
 become noncurrent.


```

<LifeCycleConfiguration>
  <Rule>
    <ID>DeleteAfterBecomingNonCurrent</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <NoncurrentVersionExpiration>
      <NoncurrentDays>100</NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID>TransitionAfterBecomingNonCurrent</ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <NoncurrentVersionTransition>
      <NoncurrentDays>30</NoncurrentDays>
      <StorageClass>GLACIER</StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
</LifeCycleConfiguration>
         
```

### Example 4: Add a lifecycle configuration to a general purpose bucket


The following is a sample `PUT /?lifecycle` request that adds the preceding lifecycle
 configuration to a `examplebucket` bucket.



```

PUT /?lifecycle HTTP/1.1
Host: examplebucket.s3.<Region>.amazonaws.com 
x-amz-date: Wed, 14 May 2014 02:21:48 GMT
Content-MD5: 96rxH9mDqVNKkaZDddgnw==
Authorization: authorization string
Content-Length: 598

<LifeCycleConfiguration>
  <Rule>
    <ID>DeleteAfterBecomingNonCurrent</ID>
    <Filter>
       <Prefix>logs/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <NoncurrentVersionExpiration>
      <NoncurrentDays>1</NoncurrentDays>
    </NoncurrentVersionExpiration>
  </Rule>
  <Rule>
    <ID>TransitionSoonAfterBecomingNonCurrent</ID>
    <Filter>
       <Prefix>documents/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <NoncurrentVersionTransition>
      <NoncurrentDays>0</NoncurrentDays>
      <StorageClass>GLACIER</StorageClass>
    </NoncurrentVersionTransition>
  </Rule>
</LifeCycleConfiguration>
         
```

### Sample Response


This example illustrates one usage of PutBucketLifecycleConfiguration.



```

HTTP/1.1 200 OK
x-amz-id-2: aXQ+KbIrmMmoO//3bMdDTw/CnjArwje+J49Hf+j44yRb/VmbIkgIO5A+PT98Cp/6k07hf+LD2mY=
x-amz-request-id: 02D7EC4C10381EB1
Date: Wed, 14 May 2014 02:21:50 GMT
Content-Length: 0
Server: AmazonS3
         
```

### Example 5: Add a lifecycle configuration to a directory bucket


The following lifecycle configuration specifies two rules, each with one action for Amazon S3 to
 perform:



* The `Expiration` action requests Amazon S3 to expire objects with object size between
 500B to 64000B and the `"myprefix/"` prefix 7 days after their creation.
* The `AbortIncompleteMultipartUpload` action requests Amazon S3 to abort incomplete
 multipart uploads 3 days after their initiation.


```

PUT /?lifecycle HTTP/1.1
Host: s3express-control.us-west-2.amazonaws.com
x-amz-sdk-checksum-algorithm: CRC32 
x-amz-checksum-crc32: UCqxTw==

<LifeCycleConfiguration>
  <Rule>
    <ID>Lifecycle expiration rule</ID>
    <Filter>
        <And>   
            <Prefix>myprefix/</Prefix>
            <ObjectSizeGreaterThan>500</ObjectSizeGreaterThan>
            <ObjectSizeLessThan>64000</ObjectSizeLessThan>
        <And> 
    <Filter>
    <Status>Enabled</Status>
    <Expiration>
         <Days>7</Days>
    <Expiration>
  </Rule>
  <Rule>
    <ID>MPU Rule</ID>
    <Filter>
       <Prefix>another_prefix/</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <AbortIncompleteMultipartUpload>
      <DaysAfterInitiation>3</DaysAfterInitiation>
    </AbortIncompleteMultipartUpload>
  </Rule>
</LifeCycleConfiguration>
         
```

### Sample Response


This example illustrates one usage of `PutBucketLifecycleConfiguration` in directory
 buckets



```

HTTP/1.1 200 OK
Server: AmazonS3
x-amz-request-id: 02D7EC4C10381EB1
x-amz-id-2: kc3B1Ns0xqzIdJNd
Content-Type: application/xml
Content-Length: 0
Date: Tue, 12 Nov 2024 18:59:45 GMT
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/cli2/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForGoV2/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForKotlin/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/boto3/s3-2006-03-01/PutBucketLifecycleConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLifecycleConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/PutBucketLifecycleConfiguration")
