AWS Audit Manager is no longer open to new customers. Existing customers
can continue to use the service as normal. For more information, see
[AWS Audit Manager availability change](audit-manager-availability-change.md "audit-manager-availability-change.md").

# Prerequisites for setting up AWS Audit Manager

Before you can use AWS Audit Manager, you must make sure that you have properly set up your
AWS account and user permissions.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Add the required permissions to access and enable Audit Manager](#attach-IAM "#attach-IAM")
- [Next steps](#setup-prerequisites-next-steps "#setup-prerequisites-next-steps")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Add the required permissions to access and enable Audit Manager

You must give users the required permissions to enable Audit Manager. For users who need
full access to Audit Manager, use the [AWSAuditManagerAdministratorAccess](../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md "../../../aws-managed-policy/latest/reference/AWSAuditManagerAdministratorAccess.md") managed policy. This is an AWS
managed policy that’s available in your AWS account, and it’s the recommended
policy for Audit Manager administrators.

###### Tip

As a security best practice, we recommend that you get started with AWS
managed policies and then move toward least-privilege permissions. AWS managed
policies grant permissions for many common use cases. However, keep in mind that
because AWS managed policies are available for use by all AWS customers,
they might not grant least-privilege permissions for your specific use cases. As
a result, we recommend that you reduce permissions further by defining [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies") that are specific to
your use cases. For more information, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _AWS Identity and Access Management User Guide._

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Next steps

Now that you've set up your AWS account and granted the required permissions,
you're ready to enable Audit Manager. For step-by-step instructions, see [Enabling AWS Audit Manager](setup-audit-manager.md "setup-audit-manager.md").
