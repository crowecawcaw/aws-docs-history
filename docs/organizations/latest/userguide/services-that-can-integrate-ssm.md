# AWS Systems Manager and

AWS Organizations

AWS Systems Manager is a collection of capabilities that enable visibility and control of your AWS
resources. The following Systems Manager capabilities work with Organizations across all of the AWS accounts
in your organization:

- Systems Manager Explorer, is a customizable operations dashboard that reports information
  about your AWS resources. You can synchronize operations data across all AWS accounts in your organization by using Organizations and Systems Manager Explorer. For more
  information, see [Systems Manager Explorer](../../../systems-manager/latest/userguide/Explorer.md "../../../systems-manager/latest/userguide/Explorer.md") in the _AWS Systems Manager User Guide_.
- Systems Manager Change Manager is an enterprise change management framework for requesting,
  approving, implementing, and reporting on operational changes to your application
  configuration and infrastructure. For more information, see [AWS Systems Manager Change
  Manager](../../../systems-manager/latest/userguide/change-manager.md "../../../systems-manager/latest/userguide/change-manager.md") in the _AWS Systems Manager User Guide_.
- Systems Manager OpsCenter provides a central location where operations engineers and IT professionals can view,
  investigate, and resolve operational work items (OpsItems) related to AWS resources. When you use OpsCenter with Organizations it supports working with OpsItems
  from a management account (either an Organizations management account or a Systems Manager delegated administrator account) and one other account during a single session.
  Once configured, users can perform the following types of actions:

      + Create, view, and update OpsItems in another account.
      + View detailed information about AWS resources that are specified in OpsItems in another account.
      + Start Systems Manager Automation runbooks to remediate issues with AWS resources in another account.

  For more information, see [AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.md "../../../systems-manager/latest/userguide/OpsCenter-getting-started-multiple-accounts.md") in the _AWS Systems Manager User Guide_.

- Use Quick Setup to quickly configure frequently used AWS services and features with recommended best practices. For more information, see [AWS Systems Manager Quick Setup](../../../systems-manager/latest/userguide/systems-manager-quick-setup.md "../../../systems-manager/latest/userguide/systems-manager-quick-setup.md") in the _AWS Systems Manager User Guide_.

When you register an AWS Organizations delegated administrator account for Systems Manager you can create, update, view, and delete Quick Setup configuration managers that
target organizational units in an organization. Learn more in [Using a delegated administrator for Quick Setup](../../../systems-manager/latest/userguide/quick-setup-delegated-administrator.md "../../../systems-manager/latest/userguide/quick-setup-delegated-administrator.md") in the _AWS Systems Manager User Guide_.

- When you set up the integrated console for Systems Manager, you enter a delegated administrator account. This account is used to register AWS Organizations delegated administrator accounts with Quick Setup, Explorer, CloudFormation StackSets, and Resource Explorer. Learn more in [Setting up Systems Manager integrated console for an organization
  _AWS Systems Manager User Guide_](../../../systems-manager/latest/userguide/systems-manager-setting-up-organizations.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-organizations.md").
  Use the following information to help you integrate
  AWS Systems Manager with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Systems Manager to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Systems Manager and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForAmazonSSM_AccountDiscovery`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Systems Manager grant access to the following service
principals:

- `ssm.amazonaws.com`

## Enabling trusted access with

Systems Manager

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only enable trusted access using the Organizations
tools.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Systems Manager** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Systems Manager** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Systems Manager that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Systems Manager as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal ssm.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Systems Manager

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Systems Manager requires trusted access with AWS Organizations to synchronize operations data across
AWS accounts in your organization. If you disable trusted access, then Systems Manager fails to
synchronize operations data and reports an error.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Systems Manager** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Systems Manager** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Systems Manager that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Systems Manager as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal ssm.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Systems Manager

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
Systems Manager that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of Systems Manager.

If you use Change Manager across an organization, you use a delegated administrator
account. This is the AWS account that has been designated as the account for managing
change templates, change requests, change runbooks and approval workflows in Change
Manager. The delegated account manages change activities across your organization. When
you set up your organization for use with Change Manager, you specify which of your
accounts serves in this role. It does not have to be the organization's management
account. The delegated administrator account is not required if you use Change Manager
with a single account only.

###### To designate a member account as a delegated administrator see the following

topics in the _AWS Systems Manager User Guide_:

- For Explorer and OpsCenter, see [Configuring a
  Delegated Administrator](../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator.md "../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator.md").
- For Change Manager, see [Setting up an
  organization and delegated account for Change Manager](../../../systems-manager/latest/userguide/change-manager-organization-setup.md "../../../systems-manager/latest/userguide/change-manager-organization-setup.md").
- For Quick Setup see [Register a delegated administrator for Quick Setup](../../../systems-manager/latest/userguide/quick-setup-register-delegated-administrator.md "../../../systems-manager/latest/userguide/quick-setup-register-delegated-administrator.md") .

## Disabling a delegated administrator

account for Systems Manager

###### To deregister a delegated administrator see the following

topics in the _AWS Systems Manager User Guide_:

- For Explorer and OpsCenter, see [Deregister an Explorer delegated administrator](../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator-deregister.md "../../../systems-manager/latest/userguide/Explorer-setup-delegated-administrator-deregister.md") .
- For Change Manager, see [Setting up an
  organization and delegated account for Change Manager](../../../systems-manager/latest/userguide/change-manager-organization-setup.md "../../../systems-manager/latest/userguide/change-manager-organization-setup.md").
- For Quick Setup see [Deregister a delegated administrator for Quick Setup](../../../systems-manager/latest/userguide/quick-setup-deregister-delegated-administrator.md "../../../systems-manager/latest/userguide/quick-setup-deregister-delegated-administrator.md") .
