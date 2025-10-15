# S3CopyObjectOperation

Contains
 the configuration parameters for a PUT Copy object operation. S3 Batch Operations passes every
 object to the underlying
 `CopyObject`
 API
 operation. For more information about the parameters for this operation,
 see [CopyObject](RESTObjectCOPY.md "RESTObjectCOPY.md").


## Contents





**AccessControlGrants** 



###### Note

This functionality is not supported by directory buckets.


Type: Array of [S3Grant](API_control_S3Grant.md "API_control_S3Grant.md") data types


Required: No




**BucketKeyEnabled** 


Specifies whether Amazon S3 should use an S3 Bucket Key for object encryption with
 server-side encryption using AWS KMS (SSE-KMS). Setting this header to `true`
 causes Amazon S3 to use an S3 Bucket Key for object encryption with SSE-KMS.


Specifying this header with an *Copy* action doesn’t affect
 *bucket-level* settings for S3 Bucket Key.


###### Note


**Directory buckets** - S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.


Type: Boolean


Required: No




**CannedAccessControlList** 



###### Note

This functionality is not supported by directory buckets.


Type: String


Valid Values: `private | public-read | public-read-write | aws-exec-read | authenticated-read | bucket-owner-read | bucket-owner-full-control`



Required: No




**ChecksumAlgorithm** 


Indicates the algorithm
 that
 you want Amazon S3 to use to create the checksum. For more
 information,
 see  [Checking object
 integrity](../userguide/checking-object-integrity.md "../userguide/checking-object-integrity.md") in the *Amazon S3 User Guide*.


Type: String


Valid Values: `CRC32 | CRC32C | SHA1 | SHA256 | CRC64NVME`



Required: No




**MetadataDirective** 



Type: String


Valid Values: `COPY | REPLACE`



Required: No




**ModifiedSinceConstraint** 



Type: Timestamp


Required: No




**NewObjectMetadata** 


If you don't provide this parameter, Amazon S3 copies all the metadata from the original
 objects. If you specify an empty set, the new objects will have no tags. Otherwise, Amazon S3
 assigns the supplied tags to the new objects.


Type: [S3ObjectMetadata](API_control_S3ObjectMetadata.md "API_control_S3ObjectMetadata.md") data type


Required: No




**NewObjectTagging** 


Specifies a list of tags to add to the destination objects after they are copied. If
 `NewObjectTagging` is not specified, the tags of the source objects are
 copied to destination objects by default.


###### Note


**Directory buckets** - Tags aren't supported by
 directory buckets. If your source objects have tags and your destination bucket is a
 directory bucket, specify an empty tag set in the `NewObjectTagging` field
 to prevent copying the source object tags to the directory bucket.


Type: Array of [S3Tag](API_control_S3Tag.md "API_control_S3Tag.md") data types


Required: No




**ObjectLockLegalHoldStatus** 


The legal hold status to be applied to all objects in the Batch Operations job.


###### Note

This functionality is not supported by directory buckets.


Type: String


Valid Values: `OFF | ON`



Required: No




**ObjectLockMode** 


The retention mode to be applied to all objects in the Batch Operations job.


###### Note

This functionality is not supported by directory buckets.


Type: String


Valid Values: `COMPLIANCE | GOVERNANCE`



Required: No




**ObjectLockRetainUntilDate** 


The date when the applied object retention configuration expires on all objects in the
 Batch Operations job.


###### Note

This functionality is not supported by directory buckets.


Type: Timestamp


Required: No




**RedirectLocation** 


If the destination bucket is configured as a website, specifies an optional metadata
 property for website redirects, `x-amz-website-redirect-location`. Allows
 webpage redirects if the object copy is accessed through a website endpoint.


###### Note

This functionality is not supported by directory buckets.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Required: No




**RequesterPays** 



###### Note

This functionality is not supported by directory buckets.


Type: Boolean


Required: No




**SSEAwsKmsKeyId** 


Specifies the AWS KMS key ID (Key ID, Key ARN, or Key Alias) to use for object encryption. If the KMS key doesn't exist in the same
 account that's issuing the command, you must use the full Key ARN not the Key ID.


###### Note


**Directory buckets** - If you specify `SSEAlgorithm` with `KMS`, you must specify the `SSEAwsKmsKeyId` parameter with the ID (Key ID or Key ARN) of the AWS KMS 
 symmetric encryption customer managed key to use. Otherwise, you get an HTTP `400 Bad Request` error. The key alias format of the KMS key isn't supported. To encrypt new object copies in a directory bucket with SSE-KMS, you must specify SSE-KMS as the directory bucket's default encryption configuration with a KMS key (specifically, a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk")). 
 The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported. Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket for the lifetime of the bucket. 
After you specify a customer managed key for SSE-KMS as the bucket default encryption, you can't override the customer managed key for the bucket's SSE-KMS configuration. 
Then, when you specify server-side encryption settings for new object copies with SSE-KMS, you must make sure the encryption key is the same customer managed key that you specified for the directory bucket's default encryption configuration. 
 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Required: No




**StorageClass** 


Specify the storage class for the destination objects in a `Copy`
 operation.


###### Note


**Directory buckets**  -
 This functionality is not supported by directory buckets. 


Type: String


Valid Values: `STANDARD | STANDARD_IA | ONEZONE_IA | GLACIER | INTELLIGENT_TIERING | DEEP_ARCHIVE | GLACIER_IR`



Required: No




**TargetKeyPrefix** 


Specifies the folder prefix
 that
 you
 want
 the objects to be
 copied
 into. For example, to copy objects into a folder named
 `Folder1` in the destination bucket, set the
 `TargetKeyPrefix`
 property
 to `Folder1`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Required: No




**TargetResource** 


Specifies the destination bucket
 Amazon Resource Name
 (ARN)
 for the batch copy operation.



* **General purpose buckets** - For example, to copy
 objects to a general purpose bucket named `destinationBucket`, set the
 `TargetResource` property to
 `arn:aws:s3:::destinationBucket`.
* **Directory buckets** - For example, to copy
 objects to a directory bucket named `destinationBucket` in the Availability Zone
 identified by the AZ ID `usw2-az1`, set the `TargetResource`
 property to
 `arn:aws:s3express:*region*:*account\_id*:/bucket/*destination\_bucket\_base\_name*--*usw2-az1*--x-s3`.
 A directory bucket as a destination bucket can be in Availability Zone or Local Zone. 


###### Note

Copying objects across different AWS Regions isn't supported when the source
 or destination bucket is in AWS Local Zones. The source and destination buckets must
 have the same parent AWS Region. Otherwise, you get an HTTP `400 Bad
 Request` error with the error code `InvalidRequest`.

Type: String


Length Constraints: Minimum length of 1. Maximum length of 128.


Pattern: `arn:[^:]+:(s3|s3express):.*`



Required: No




**UnModifiedSinceConstraint** 



Type: Timestamp


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3CopyObjectOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/S3CopyObjectOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3CopyObjectOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/S3CopyObjectOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3CopyObjectOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/S3CopyObjectOperation")
