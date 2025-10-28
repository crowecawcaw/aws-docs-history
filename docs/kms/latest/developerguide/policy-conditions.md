# Condition keys for AWS KMS

You can specify conditions in the [key policies](key-policies.md "key-policies.md") and [IAM policies](iam-policies.md "iam-policies.md") that control access to AWS KMS resources. The
policy statement is effective only when the conditions are true. For example, you might want a
policy statement to take effect only after a specific date. Or, you might want a policy
statement to control access only when a specific value appears in an API request.

To specify conditions, you use _condition keys_ in the [`Condition`
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy statement with [IAM condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"). Some condition keys apply generally to AWS; others are specific to
AWS KMS.

Condition key values must adhere to the character and encoding rules for AWS KMS key policies
and IAM policies. For details about key policy document rules, see [Key policy format](key-policy-overview.md#key-policy-format "key-policy-overview.md#key-policy-format"). For details about IAM
policy document rules, see [IAM name
requirements](../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names "../../../IAM/latest/UserGuide/reference_iam-quotas.md#reference_iam-quotas-names") in the _IAM User Guide_..

###### Topics

- [AWS global condition keys](conditions-aws.md "conditions-aws.md")
- [AWS KMS condition keys](conditions-kms.md "conditions-kms.md")
- [AWS KMS condition keys for attested platforms](conditions-attestation.md "conditions-attestation.md")
