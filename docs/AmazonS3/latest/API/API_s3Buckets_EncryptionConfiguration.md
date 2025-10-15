# EncryptionConfiguration

Configuration specifying how data should be encrypted. This structure defines the encryption algorithm and optional KMS key to be used for server-side encryption.


## Contents





**sseAlgorithm** 


The server-side encryption algorithm to use. Valid values are `AES256` for S3-managed encryption keys, or `aws:kms` for AWS KMS-managed encryption keys. If you choose SSE-KMS encryption you must grant the S3 Tables maintenance principal access to your KMS key. For more information, see [Permissions requirements for S3 Tables SSE-KMS encryption](../userguide/s3-tables-kms-permissions.md "../userguide/s3-tables-kms-permissions.md").


Type: String


Valid Values: `AES256 | aws:kms`



Required: Yes




**kmsKeyArn** 


The Amazon Resource Name (ARN) of the KMS key to use for encryption. This field is required only when `sseAlgorithm` is set to `aws:kms`.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `(arn:aws[-a-z0-9]*:kms:[-a-z0-9]*:[0-9]{12}:key/.+)`



Required: No




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForCpp/s3tables-2018-05-10/EncryptionConfiguration")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3tables-2018-05-10/EncryptionConfiguration")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/EncryptionConfiguration "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3tables-2018-05-10/EncryptionConfiguration")
