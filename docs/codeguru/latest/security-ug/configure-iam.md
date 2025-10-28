On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Configure IAM permissions

Following security best practices, create an AWS Identity and Access Management (IAM) role
with access restricted to Amazon CodeGuru Security operations and with required permissions. You
can add other permissions as needed.

The following policies provide permissions to use Amazon CodeGuru Security:

- **[AmazonCodeGuruSecurityFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityFullAccess")**: Provides full access to
  resources needed to use Amazon CodeGuru Security.
- **[AmazonCodeGuruSecurityScanAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonCodeGuruSecurityScanAccess")**: Provides access to API
  operations needed to create scans, get scan information, and get scan findings.
  For more information on these AWS managed policies, see
  [AWS managed policies for Amazon CodeGuru Security](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

You can also create custom IAM policies to allow permissions for CodeGuru Security actions
and resources. See the following topics for more information on configuring IAM roles to use
CodeGuru Security:

- [Authenticating with identities](security-iam.md#security_iam_authentication "security-iam.md#security_iam_authentication")

- [How Amazon CodeGuru Security works with IAM](security_iam_service-with-iam.md "security_iam_service-with-iam.md")

- [Identity-based policy examples for
  Amazon CodeGuru Security](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md")

## Assigning permissions

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
