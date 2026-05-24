AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Setting up Strategy Recommendations

Before you use Migration Hub Strategy Recommendations for the first time, complete the following tasks:

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Strategy Recommendations users and roles](#setting-up-iam-non-admin "#setting-up-iam-non-admin")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Strategy Recommendations users and roles

We recommend that you create two roles for Strategy Recommendations:

- To access the console, create a role with both the `AWSMigrationHubFullAccess`
  and the `AWSMigrationHubStrategyConsoleFullAccess` managed policies attached.
- To access the Strategy Recommendations application data collector, create a role with the
  `AWSMigrationHubStrategyCollector` managed policy attached.

IAM managed policies define the level of access to a service by users. The AWS Migration Hub
`AWSMigrationHubFullAccess` managed policy grants access to the Migration Hub console. For
more information, see [Migration Hub Roles and Policies](../../../migrationhub/latest/ug/policy-templates.md "../../../migrationhub/latest/ug/policy-templates.md"). For
information about the `AWSMigrationHubStrategyConsoleFullAccess` and
`AWSMigrationHubStrategyCollector` managed policies, see [AWS managed policies for Migration Hub Strategy Recommendations](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.
