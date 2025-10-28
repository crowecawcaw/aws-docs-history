# Cross-service confused deputy prevention

The confused deputy problem is a security issue where an entity
that doesn't have permission to perform an action can coerce a
more-privileged entity to perform the action. In AWS,
cross-service impersonation can result in the confused deputy
problem. Cross-service impersonation can occur when one service
(the _calling service_) calls another service
(the _called service_). The calling service can
be manipulated to use its permissions to act on another customer's
resources in a way it should not otherwise have permission to
access. To prevent this, AWS provides tools that help you protect
your data for all services with service principals that have been
given access to resources in your account.

We recommend using the
[AWS:SourceArn](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourcearn")
and
[AWS:SourceAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-sourceaccount")
global condition context keys in resource policies to limit the
permissions that Amazon Connect gives another service to the
resource. If you use both global condition context keys, the
AWS:SourceAccount value and the account in the AWS:SourceArn value
must use the same account ID when used in the same policy
statement.

The most effective way to protect against the confused deputy
problem is to use the exact Amazon Resource Name (ARN) of the
resource you want to allow. If you don't know the full ARN of the
resource or if you are specifying multiple resources, use the
AWS:SourceArn global context condition key with wildcards (\*) for
the unknown portions of the ARN. For example,
arn:AWS:servicename::region-name::your AWS account ID:\*.

For an example of an assume role policy that shows how you can
prevent a confused deputy issue, see
[Confused
deputy prevention policy](../../../transcribe/latest/dg/security_iam_id-based-policy-examples.md#confused-deputy-policy "../../../transcribe/latest/dg/security_iam_id-based-policy-examples.md#confused-deputy-policy").
