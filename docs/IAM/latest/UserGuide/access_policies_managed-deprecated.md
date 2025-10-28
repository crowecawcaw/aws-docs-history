# Deprecated AWS managed policies

To simplify the assignment of permissions, AWS provides [managed policies](access_policies_managed-vs-inline.md "access_policies_managed-vs-inline.md")—predefined policies
that are ready to be attached to your IAM users, groups, and roles.

Sometimes AWS needs to add a new permission to an existing policy, such as when a new
service is introduced. Adding a new permission to an existing policy does not disrupt or remove
any feature or ability.

However, AWS might choose to create a _new_ policy when the needed
changes could impact customers if they were applied to an existing policy. For example, removing
permissions from an existing policy could break the permissions of any IAM entity or
application that depended upon it, potentially disrupting a critical operation.

Therefore, when such a change is required, AWS creates a completely new policy with the
required changes and makes it available to customers. The old policy is then marked
_deprecated_. For more information, see [Deprecated AWS managed policies](../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md#deprecated-managed-policies "../../../aws-managed-policy/latest/reference/about-managed-policy-reference.md#deprecated-managed-policies") in _AWS Managed Policy Reference Guide_.
