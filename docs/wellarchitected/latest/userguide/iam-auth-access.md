

# Providing users, groups, or roles access to AWS WA Tool
<a name="iam-auth-access"></a>

You can grant users, groups, or roles full control or read-only access to AWS Well-Architected Tool.

**Provide access to AWS WA Tool**

1. To provide access, add permissions to your users, groups, or roles:
   + Users and groups in AWS IAM Identity Center:

     Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
   + Users managed in IAM through an identity provider:

     Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
   + IAM users:
     + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
     + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

1. To grant full control, apply the **WellArchitectedConsoleFullAccess** managed policy to the permission set or role.

   Full access allows the principal to perform all actions in AWS WA Tool. This access is required to define workloads, delete workloads, view workloads, update workloads, share workloads, create custom lenses, and share custom lenses.

1. To grant read-only access, apply the ** WellArchitectedConsoleReadOnlyAccess** managed policy to the permission set or role. Principals with this role can only view resources.

For more information on these policies, see [AWS managed policies for AWS Well-Architected Tool](security-iam-awsmanpol.md).