# ServerSideEncryptionByDefault

Describes the default server-side encryption to apply to new objects in the bucket. If a PUT Object
 request doesn't specify any server-side encryption, this default encryption will be applied. For more
 information, see [PutBucketEncryption](RESTBucketPUTencryption.md "RESTBucketPUTencryption.md").

###### Note


* **General purpose buckets** - If you don't specify a customer managed key
 at configuration, Amazon S3 automatically creates an AWS KMS key (`aws/s3`) in your AWS
 account the first time that you add an object encrypted with SSE-KMS to a bucket. By default, Amazon S3
 uses this KMS key for SSE-KMS.
* **Directory buckets** -
 Your SSE-KMS configuration can only support 1 [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") per directory bucket's lifetime. 
The [AWS managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk") (`aws/s3`) isn't supported.
* **Directory buckets** -
 For directory buckets, there are only two supported options for server-side encryption: SSE-S3 and SSE-KMS.

## Contents





**SSEAlgorithm** 


Server-side encryption algorithm to use for the default encryption.


###### Note

For directory buckets, there are only two supported values for server-side encryption: `AES256` and `aws:kms`.


Type: String


Valid Values: `AES256 | aws:fsx | aws:kms | aws:kms:dsse`



Required: Yes




**KMSMasterKeyID** 



 AWS Key Management Service (KMS) customer managed key ID to use for the default encryption. 


###### Note


* **General purpose buckets** - This parameter is allowed if and
 only if `SSEAlgorithm` is set to `aws:kms` or
 `aws:kms:dsse`.
* **Directory buckets** - This parameter is allowed if and
 only if `SSEAlgorithm` is set to `aws:kms`.

You can specify the key ID, key alias, or the Amazon Resource Name (ARN) of the KMS key.



* Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
* Key ARN:
 `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
* Key Alias: `alias/alias-name`

If you are using encryption with cross-account or AWS service operations, you must use a fully
 qualified KMS key ARN. For more information, see [Using
 encryption for cross-account operations](https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-update-bucket-policy "https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html#bucket-encryption-update-bucket-policy").


###### Note


* **General purpose buckets** - If you're specifying a customer
 managed KMS key, we recommend using a fully qualified KMS key ARN. If you use a KMS key
 alias instead, then AWS KMS resolves the key within the requester’s account. This behavior can
 result in data that's encrypted with a KMS key that belongs to the requester, and not the bucket
 owner. Also, if you use a key ID, you can run into a LogDestination undeliverable error when
 creating a VPC flow log.
* **Directory buckets** -
 When you specify an [AWS KMS customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk") for encryption in your directory bucket, only use the key ID or key ARN. The key alias format of the KMS key isn't supported.

###### Important

Amazon S3 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in
 AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html "https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html") in the *AWS Key Management Service Developer Guide*.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ServerSideEncryptionByDefault "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/ServerSideEncryptionByDefault")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ServerSideEncryptionByDefault "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/ServerSideEncryptionByDefault")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ServerSideEncryptionByDefault "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/ServerSideEncryptionByDefault")
