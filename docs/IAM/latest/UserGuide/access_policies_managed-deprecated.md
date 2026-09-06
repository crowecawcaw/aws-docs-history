

# Deprecated AWS managed policies
<a name="access_policies_managed-deprecated"></a>

To simplify the assignment of permissions, AWS provides [managed policies](access_policies_managed-vs-inline.md)—predefined policies that are ready to be attached to your IAM users, groups, and roles.

Sometimes AWS needs to add a new permission to an existing policy, such as when a new service is introduced. Adding a new permission to an existing policy does not disrupt or remove any feature or ability.

However, AWS might choose to create a *new* policy when the needed changes could impact customers if they were applied to an existing policy. For example, removing permissions from an existing policy could break the permissions of any IAM entity or application that depended upon it, potentially disrupting a critical operation.

Therefore, when such a change is required, AWS creates a completely new policy with the required changes and makes it available to customers. The old policy is then marked *deprecated*. For more information, see [Deprecated AWS managed policies](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/about-managed-policy-reference.html#deprecated-managed-policies) in *AWS Managed Policy Reference Guide*.