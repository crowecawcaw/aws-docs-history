# EncryptionConfiguration

Specifies encryption-related information for an Amazon S3 bucket that is a destination for replicated
 objects.

###### Note

If you're specifying a customer managed KMS key, we recommend using a fully qualified KMS key
 ARN. If you use a KMS key alias instead, then AWS KMS resolves the key within the requester’s account.
 This behavior can result in data that's encrypted with a KMS key that belongs to the requester, and
 not the bucket owner.


## Contents





**ReplicaKmsKeyID** 


Specifies the ID (Key ARN or Alias ARN) of the customer managed AWS KMS key stored in AWS Key
 Management Service (KMS) for the destination bucket. Amazon S3 uses this key to encrypt replica objects. Amazon S3
 only supports symmetric encryption KMS keys. For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html "https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html") in the
 *AWS Key Management Service Developer Guide*.


Type: String


Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/EncryptionConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/EncryptionConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/EncryptionConfiguration")
