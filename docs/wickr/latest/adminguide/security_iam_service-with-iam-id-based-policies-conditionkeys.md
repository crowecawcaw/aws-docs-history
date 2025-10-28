This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Policy

condition keys for Wickr

**Supports service-specific policy condition keys:**

No

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

To see a list of Wickr condition keys, see [Condition Keys for AWS Wickr](../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-policy-keys "../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and resources you
can use a condition key, see [Actions Defined by AWS Wickr](../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions "../../../IAM/latest/UserGuide/list_awswickr.md#awswickr-actions-as-permissions").

To view examples of Wickr identity-based policies, see [Identity-based policy examples for
AWS Wickr](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").
