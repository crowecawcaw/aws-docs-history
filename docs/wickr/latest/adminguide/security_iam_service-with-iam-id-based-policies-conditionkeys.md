

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Policy condition keys for Wickr
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

**Supports service-specific policy condition keys:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

To see a list of Wickr condition keys, see [Condition Keys for AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-policy-keys) in the *Service Authorization Reference*. To learn with which actions and resources you can use a condition key, see [Actions Defined by AWS Wickr](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awswickr.html#awswickr-actions-as-permissions).

Wickr supports the following global condition keys for controlling access based on network tags:
+ `aws:ResourceTag/{{tag-key}}` – Controls access based on a tag attached to a network.
+ `aws:RequestTag/{{tag-key}}` – Controls which tag values can be included in a request.
+ `aws:TagKeys` – Controls which tag keys can be included in a request.

For an example that uses a network tag to control access, see [Control access to Wickr networks based on tags](security_iam_id-based-policy-examples-resource-tags.md).