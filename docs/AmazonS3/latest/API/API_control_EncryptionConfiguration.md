# EncryptionConfiguration

Specifies encryption-related information for an Amazon S3 bucket that is a destination for
 replicated objects. If you're specifying a customer managed KMS key, we recommend using a
 fully qualified KMS key ARN. If you use a KMS key alias instead, then AWS KMS resolves
 the key within the requester’s account. This behavior can result in data that's encrypted
 with a KMS key that belongs to the requester, and not the bucket owner.

###### Note

This is not supported by Amazon S3 on Outposts buckets.


## Contents





**ReplicaKmsKeyID** 


Specifies the ID of the customer managed AWS KMS key that's stored in AWS Key Management Service (AWS KMS)
 for the destination bucket. This ID is either the Amazon Resource Name (ARN) for the
 KMS key or the alias ARN for the KMS key. Amazon S3 uses this KMS key to encrypt
 replica objects. Amazon S3 supports only symmetric encryption KMS keys. For more information,
 see [Symmetric encryption
 KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks "https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks") in the *AWS Key Management Service Developer
 Guide*.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/EncryptionConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/EncryptionConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/EncryptionConfiguration")
