# Authorization with IAM identity-based

policies and DynamoDB resource-based policies

**Identity-based policies** are attached to an identity, such
as IAM users, groups of users, and roles. These are IAM policy documents that control what
actions an identity can perform, on which resources, and under what conditions. Identity-based
policies can be [managed](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md") or [inline](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") policies.

**Resource-based policies** are IAM policy documents that
you attach to a resource, such as a DynamoDB table. These policies grant the specified principal
permission to perform specific actions on that resource and defines under what conditions this
applies. For example, the resource-based policy for a DynamoDB table also includes the index
associated with the table. Resource-based policies are inline policies. There are no managed
resource-based policies.

For more information about these policies, see [Identity-based policies
and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _IAM User Guide_.

If the IAM principal is from the same account as the resource owner, a resource-based
policy is sufficient to specify access permissions to the resource. You can still choose to
have an IAM identity-based policy along with a resource-based policy. For cross-account
access, you must explicitly allow access in both the identity and resource policies as
specified in [Cross-account access with resource-based policies
in DynamoDB](rbac-cross-account-access.md "rbac-cross-account-access.md"). When you use both types of policies, a policy
is evaluated as described in [Determining whether a request is allowed or denied within an account](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow").
