# Amazon Inspector and AWS Organizations

Amazon Inspector is an automated vulnerability management service that continually scans Amazon EC2
and container workloads for software vulnerabilities and unintended network exposure.

Using Amazon Inspector you can manage multiple accounts that are associated through AWS Organizations by
simply delegating an administrator account for Amazon Inspector. The delegated administrator
manages Amazon Inspector for the organization and is granted special permissions to perform tasks
on behalf of your organization such as:

- Enable or disable scans for member accounts
- View aggregated finding data from the entire organization
- Create and manage suppression rules
  For more information, see [Managing multiple accounts
  with AWS Organizations](../../../inspector/latest/user/managing-multiple-accounts.md "../../../inspector/latest/user/managing-multiple-accounts.md") in the _Amazon Inspector User Guide_.

Use the following information to help you integrate Amazon Inspector with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Amazon Inspector to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Amazon Inspector and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForAmazonInspector2`

For more information, see [Using service-linked
roles with Amazon Inspector](../../../inspector/latest/user/using-service-linked-roles.md "../../../inspector/latest/user/using-service-linked-roles.md") in the _Amazon Inspector User Guide_.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon Inspector grant access to the following service
principals:

- `inspector2.amazonaws.com`

## To enable trusted access with

Amazon Inspector

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

Amazon Inspector requires trusted access to AWS Organizations before you can designate a member account to
be the delegated administrator for this service for your organization.

When you designate a delegated administrator for Amazon Inspector, Amazon Inspector automatically
enables trusted access for Amazon Inspector for your organization.

However, if you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, then you must explicitly call the
`EnableAWSServiceAccess` operation and provide the service principal as a
parameter. Then you can call `EnableDelegatedAdminAccount` to delegate the
Inspector administrator account.

You can enable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To enable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable Amazon Inspector as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal inspector2.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

###### Note

If you are using the `EnableAWSServiceAccess` API, you need to also call
[`EnableDelegatedAdminAccount`](../../../inspector/v2/APIReference/API_EnableDelegatedAdminAccount.md "../../../inspector/v2/APIReference/API_EnableDelegatedAdminAccount.md") to delegate the Inspector
administrator account.

## To disable trusted access with

Amazon Inspector

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Only an administrator in the AWS Organizations management account can disable trusted access
with Amazon Inspector.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable Amazon Inspector as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal inspector2.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Amazon Inspector

With Amazon Inspector you can manage multiple accounts in an organization using a delegated
administrator with AWS Organizations service.

The AWS Organizations management account designates an account within the organization as the
delegated administrator account for Amazon Inspector. The delegated administrator manages Amazon Inspector for
the organization and is granted special permissions to perform tasks on behalf of your
organization such as: enable or disable scans for member accounts, view aggregated
finding data from the entire organization, and create and manage suppression
rules

For information on how a delegated administrator manages organization accounts, see
[Understanding the
relationship between administrator and member accounts](../../../inspector/latest/user/admin-member-relationship.md "../../../inspector/latest/user/admin-member-relationship.md") in the
_Amazon Inspector User Guide_.

Only an administrator in the organization management account can configure a delegated
administrator for Amazon Inspector.

You can specify a delegated administrator account from the Amazon Inspector console or API, or by
using the Organizations CLI or SDK operation.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for Amazon Inspector in the organization

To configure a delegated administrator using the Amazon Inspector console, see [Step 1: Enable Amazon Inspector - Multi-account environment](../../../inspector/latest/user/getting_started_tutorial.md#tutorial_enable_scans "../../../inspector/latest/user/getting_started_tutorial.md#tutorial_enable_scans") in the
_Amazon Inspector User Guide_.

###### Note

You must call `inspector2:enableDelegatedAdminAccount` in each region where you
use Amazon Inspector.

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$` **aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal inspector2.amazonaws.com**
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service principal
  `account.amazonaws.com` as parameters.

## Disabling a delegated administrator

for Amazon Inspector

Only an administrator in the AWS Organizations management account can remove a delegated
administrator account from the organization.

You can remove the delegated administrator using either the Amazon Inspector console or API, or
by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation. To remove a delegated administrator using the Amazon Inspector console, see [Removing a delegated administrator](../../../inspector/latest/user/remove-delegated-admin.md "../../../inspector/latest/user/remove-delegated-admin.md") in the _Amazon Inspector User
Guide_.
