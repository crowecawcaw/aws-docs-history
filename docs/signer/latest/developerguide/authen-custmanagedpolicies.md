# Customer managed policies for

Signer

Customer managed policies are standalone identity-based policies that an
administrator creates and can attach to multiple users, groups, or roles in your
AWS account. Administrators can manage and create policies using the [AWS Management Console](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md"), the
[AWS Command Line Interface
(AWS CLI)](../../../IAM/latest/UserGuide/access_policies_create-cli.md "../../../IAM/latest/UserGuide/access_policies_create-cli.md"), or the [IAM API](../../../IAM/latest/UserGuide/access_policies_create-api.md "../../../IAM/latest/UserGuide/access_policies_create-api.md").

**To manage policies in the AWS Management Console**

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
