

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Encrypting data at rest
<a name="encryption-at-rest"></a>

Amazon Fraud Detector encrypts your data at rest with your choice of an encryption key. You can choose one of the following:
+ An AWS owned [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). If you don't specify an encryption key your data is encrypted with this key by default.
+ A customer managed [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys). You can control access to your customer managed KMS key using [key policies](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key_permissions). For information on creating and managing customer managed KMS key, see [Key management](key-management.md).