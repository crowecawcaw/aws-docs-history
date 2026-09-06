

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Setting up Strategy Recommendations
<a name="setting-up"></a>

Before you use Migration Hub Strategy Recommendations for the first time, complete the following tasks:

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Strategy Recommendations users and roles](#setting-up-iam-non-admin)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Strategy Recommendations users and roles
<a name="setting-up-iam-non-admin"></a>

We recommend that you create two roles for Strategy Recommendations:
+ To access the console, create a role with both the `AWSMigrationHubFullAccess` and the `AWSMigrationHubStrategyConsoleFullAccess` managed policies attached.
+ To access the Strategy Recommendations application data collector, create a role with the `AWSMigrationHubStrategyCollector` managed policy attached.

IAM managed policies define the level of access to a service by users. The AWS Migration Hub `AWSMigrationHubFullAccess` managed policy grants access to the Migration Hub console. For more information, see [ Migration Hub Roles and Policies](https://docs.aws.amazon.com/migrationhub/latest/ug/policy-templates.html). For information about the `AWSMigrationHubStrategyConsoleFullAccess` and `AWSMigrationHubStrategyCollector` managed policies, see [AWS managed policies for Migration Hub Strategy Recommendations](security-iam-awsmanpol.md). 

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.