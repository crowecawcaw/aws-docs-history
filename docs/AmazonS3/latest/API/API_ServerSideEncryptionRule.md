# ServerSideEncryptionRule

Specifies the default server-side encryption configuration.

###### Note


* **General purpose buckets** - If you're specifying a customer
 managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key
 alias instead, then AWS KMS resolves the key within the requester’s account. This behavior can
 result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket
 owner.
* **Directory buckets** -
 When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

## Contents





**ApplyServerSideEncryptionByDefault** 


Specifies the default server-side encryption to apply to new objects in the bucket. If a PUT Object
 request doesn't specify any server-side encryption, this default encryption will be applied.


Type: [ServerSideEncryptionByDefault](API_ServerSideEncryptionByDefault.md "API_ServerSideEncryptionByDefault.md") data type


Required: No




**BucketKeyEnabled** 


Specifies whether Amazon S3 should use an S3 Bucket Key with server-side encryption using KMS (SSE-KMS)
 for new objects in the bucket. Existing objects are not affected. Setting the
 `BucketKeyEnabled` element to `true` causes Amazon S3 to use an S3 Bucket Key. 


###### Note


* **General purpose buckets** - By default, S3 Bucket Key is not
 enabled. For more information, see [Amazon S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html") in the
 *Amazon S3 User Guide*.
* **Directory buckets** -
 S3 Bucket Keys are always enabled for `GET` and `PUT` operations in a directory bucket and can’t be disabled. S3 Bucket Keys aren't supported, when you copy SSE-KMS encrypted objects from general purpose buckets 
to directory buckets, from directory buckets to general purpose buckets, or between directory buckets, through [CopyObject](API_CopyObject.md "API_CopyObject.md"), [UploadPartCopy](API_UploadPartCopy.md "API_UploadPartCopy.md"), [the Copy operation in Batch Operations](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops "https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-objects-Batch-Ops"), or 
 [the import jobs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job "https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-import-job"). In this case, Amazon S3 makes a call to AWS KMS every time a copy request is made for a KMS-encrypted object.

Type: Boolean


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ServerSideEncryptionRule "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ServerSideEncryptionRule")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ServerSideEncryptionRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ServerSideEncryptionRule")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ServerSideEncryptionRule "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ServerSideEncryptionRule")
