# Key management for Amazon Detective

Because Detective does not store any personally identifiable customer data, it uses
AWS managed keys.

This type of KMS key can be used across multiple accounts. See the [description
of AWS owned keys in the AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk").

This type of KMS key rotates automatically every one year (approximately 365 days). See the [description of key
rotation in the AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").
