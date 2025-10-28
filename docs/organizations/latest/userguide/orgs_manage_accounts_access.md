# Accessing member accounts in an

organization with AWS Organizations

When you create an account in your organization, in
addition to the root user, AWS Organizations automatically creates an IAM role that is by
default named `OrganizationAccountAccessRole`. You can specify a different name
when you create it, however we recommend that you name it consistently across all of your
accounts. AWS Organizations doesn't create
any other users or roles.

To access the accounts in your organization, you must use one of
the following methods:

###### Minimum permissions

To access an AWS account from any other account in your organization, you must have
the following permission:

- `sts:AssumeRole` – The `Resource` element must be
  set to either an asterisk (\*) or the account ID number of the account with the
  user who needs to access the new member account

Using the root user (Not recommended for everyday tasks)When you create new member account in your organization, the account has no root user credentials by default.
Member accounts can't sign in to their root user or perform password recovery for their root user unless account recovery is enabled.

You can [centralize root access for member accounts](../../../IAM/latest/UserGuide/id_root-enable-root-access.md "../../../IAM/latest/UserGuide/id_root-enable-root-access.md") to remove root user credentials for existing member accounts in your organization.
Deleting root user credentials removes the root user password, access keys, signing certificates, and deactivates multi-factor authentication (MFA).
These member accounts do not have root user credentials, can't sign in as a root user, and are prevented from recovering the root user password.
New accounts you create in Organizations have no root user credentials by default.

Contact your administrator if you need to perform a task that requires root user credentials on a member account where root user credentials are not present.

To access your member account as the root user, you must go through the process for password recovery. For more information, see [I forgot my root user password for my AWS account](../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-forgot-root-password "../../../signin/latest/userguide/troubleshooting-sign-in-issues.md#troubleshoot-forgot-root-password") in the _AWS Sign-In User Guide_.

If you must access a member account using the root user, follow these best practices:

- Don't use the root user to access
  your account except to create other users and roles with more limited
  permissions. Then sign in as one of those users or roles.
- [Enable
  multi-factor authentication (MFA) on the root user](../../../IAM/latest/UserGuide/root-user-best-practices.md#ru-bp-mfa "../../../IAM/latest/UserGuide/root-user-best-practices.md#ru-bp-mfa"). Reset the
  password, and [assign an MFA
  device to the root user](../../../IAM/latest/UserGuide/id_credentials_mfa_enable.md "../../../IAM/latest/UserGuide/id_credentials_mfa_enable.md").

For the complete list of tasks that require you to sign in as the root user,
see [Tasks that require root user credentials](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks") in the _IAM User Guide_.
For additional root user security recommendations, see [Root user best practices for your AWS account](../../../IAM/latest/UserGuide/root-user-best-practices.md "../../../IAM/latest/UserGuide/root-user-best-practices.md") in the _IAM User Guide_.

Using trusted access for IAM Identity CenterUse [AWS IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md") and enable trusted access for IAM Identity Center with AWS Organizations. This
allows users to sign in to the AWS access portal with their corporate credentials
and access resources in their assigned management account or member accounts.

For more information, see [Multi-account
permissions](../../../singlesignon/latest/userguide/manage-your-accounts.md "../../../singlesignon/latest/userguide/manage-your-accounts.md") in the _AWS IAM Identity Center User Guide._ For
information about setting up trusted access for IAM Identity Center, see [AWS IAM Identity Center and
AWS Organizations](services-that-can-integrate-sso.md "services-that-can-integrate-sso.md").

Using the IAM role OrganizationAccountAccessRole If you create an account by using the tools provided as part of AWS Organizations, you can
access the account by using the preconfigured role named
`OrganizationAccountAccessRole` that exists in all new accounts that
you create this way. For more information, see [Accessing a member
account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md").

If you invite an existing account to join your organization and the account
accepts the invitation, you can then choose to create an IAM role that allows the
management account to access the invited member account. This role is intended to be
identical to the role automatically added to an account that is created with
AWS Organizations.

To create this role, see [Creating
OrganizationAccountAccessRole for an invited account with AWS Organizations](orgs_manage_accounts_create-cross-account-role.md "orgs_manage_accounts_create-cross-account-role.md").

After you
create the role, you can access it using the steps in [Accessing a member
account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md").

###### Topics

- [Creating
  an IAM access role](orgs_manage_accounts_create-cross-account-role.md "orgs_manage_accounts_create-cross-account-role.md")
- [Using the IAM access role](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md")
