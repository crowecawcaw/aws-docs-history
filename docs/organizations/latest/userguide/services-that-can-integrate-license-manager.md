# AWS License Manager and

AWS Organizations

AWS License Manager streamlines the process of bringing software vendor licenses to the cloud. As
you build out cloud infrastructure on AWS, you can save costs by using
bring-your-own-license (BYOL) opportunities—that is, by repurposing your existing
license inventory for use with cloud resources. With rule-based controls on the consumption
of licenses, administrators can set hard or soft limits on new and existing cloud
deployments, stopping noncompliant server usage before it happens.

For more information about License Manager, see the [License Manager User Guide](../../../license-manager/latest/userguide.md "../../../license-manager/latest/userguide.md").

By linking License Manager with AWS Organizations, you can:

- Enable cross-account discovery of computing
  resources throughout your organization.
- View and manage commercial Linux subscriptions that you own and run on AWS. For more information see [Linux subscriptions in AWS License Manager](../../../license-manager/latest/userguide/linux-subscriptions.md "../../../license-manager/latest/userguide/linux-subscriptions.md").
  Use the following information to help you integrate
  AWS License Manager with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked roles](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") are
automatically created in your organization's management account when you enable trusted
access. These roles allow License Manager to perform supported operations within your
organization's accounts in your organization.

You can delete or modify roles only if you disable trusted access between
License Manager and Organizations, or if you remove the member account from the organization.

- `AWSLicenseManagerMasterAccountRole`
- `AWSLicenseManagerMemberAccountRole`
- `AWSServiceRoleForAWSLicenseManagerRole`
- `AWSServiceRoleForAWSLicenseManagerLinuxSubscriptionsService`

For more information, see [License Manager–Management account
role](../../../license-manager/latest/userguide/management-role.md "../../../license-manager/latest/userguide/management-role.md"), [License Manager–Member account role](../../../license-manager/latest/userguide/member-role.md "../../../license-manager/latest/userguide/member-role.md"), and [License Manager–Linux subscriptions role](../../../license-manager/latest/userguide/linux-subscriptions-role.md "../../../license-manager/latest/userguide/linux-subscriptions-role.md").

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by License Manager grant access to the following service principals:

- `license-manager.amazonaws.com`
- `license-manager.member-account.amazonaws.com`
- `license-manager-linux-subscriptions.amazonaws.com`

## Enabling trusted access with

License Manager

You can only enable trusted access using
AWS License Manager.

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

###### To enable trusted access with License Manager

You must sign in to the License Manager console using your AWS Organizations management account and
associate it with your License Manager account. For more information, see [Settings in AWS License Manager](../../../license-manager/latest/userguide/settings.md "../../../license-manager/latest/userguide/settings.md").

## Disabling trusted access with

License Manager

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by running an Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

You can run the following command to disable AWS License Manager as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal license-manager.amazonaws.com**
```

This command produces no output when successful.

To disable trusted access for Linux subscriptions use:

```
`$`  **aws organizations disable-aws-service-access \
 --service-principal license-manager-linux-subscriptions.amazonaws.com**
```

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for License Manager

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
License Manager that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of License Manager.

To delegate a member account as an administrator for License Manager, follow the steps at [Register a
delegated administrator](../../../license-manager/latest/userguide/settings.md#delegated-administrator "../../../license-manager/latest/userguide/settings.md#delegated-administrator") in the _License Manager User Guide_.
