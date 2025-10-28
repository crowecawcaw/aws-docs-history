Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Encrypting data at rest

Amazon Fraud Detector encrypts your data at rest with your choice of an encryption key. You can choose one of the following:

- An AWS owned [KMS key](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"). If you don't specify an encryption key your data is encrypted with this key by default.
- A customer managed [KMS key](../../../kms/latest/developerguide/concepts.md#master_keys "../../../kms/latest/developerguide/concepts.md#master_keys"). You can control access to your customer managed KMS key using [key policies](../../../kms/latest/developerguide/concepts.md#key_permissions "../../../kms/latest/developerguide/concepts.md#key_permissions").
  For information on creating and managing customer managed KMS key, see [Key management](key-management.md "key-management.md").
