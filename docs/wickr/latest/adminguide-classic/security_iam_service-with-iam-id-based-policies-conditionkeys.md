

This guide documents the classic version of the AWS Wickr administration console, released before March 13, 2025. For documentation on the new AWS Wickr administration console, see [ Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html).

# Policy condition keys for Wickr
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** No 

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Wickr condition keys, see [Condition Keys for AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-actions-as-permissions).

To view examples of Wickr identity-based policies, see [Identity-based policy examples for AWS Wickr](security_iam_id-based-policy-examples.md).