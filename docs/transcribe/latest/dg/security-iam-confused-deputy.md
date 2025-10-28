# Cross-service confused deputy prevention

A confused deputy is an entity (a service or an account) that is coerced by a different entity
to perform an action. This type of impersonation can happen cross-account and cross-service.

To prevent confused deputies, AWS provides tools that help you protect your data for all
services using service principals that have been given access to resources in your AWS account.
This section focuses on cross-service confused deputy prevention specific to Amazon Transcribe; however, you
can learn more about this topic in the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") section of the
_IAM User Guide_.

To limit the permissions IAM gives to Amazon Transcribe to access your
resources, we recommend using the global condition context keys [`aws:SourceArn`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn") and [`aws:SourceAccount`](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount") in your resource policies.

If you use both of these global condition context keys, and the `aws:SourceArn`
value contains the AWS account ID, the `aws:SourceAccount` value
and the AWS account in `aws:SourceArn` must use the same
AWS account ID when used in the same policy statement.

If you want only one resource to be associated with the cross-service access, use
`aws:SourceArn`. If you want to associate any resource in that AWS account with
cross-service access, use `aws:SourceAccount`.

###### Note

The most effective way to protect against the confused deputy problem is to use the
`aws:SourceArn` global condition context key with the **full ARN** of
the resource. If you don’t know the full ARN, or if you're specifying multiple resources, use the
`aws:SourceArn` global context condition key with wildcards (`*`) for the
unknown portions of the ARN. For example,
`arn:aws:transcribe::`123456789012`:*`.

For an example of an assume role policy that shows how you can prevent a confused deputy issue,
see [Confused deputy prevention policy](security_iam_id-based-policy-examples.md#confused-deputy-policy "security_iam_id-based-policy-examples.md#confused-deputy-policy").
