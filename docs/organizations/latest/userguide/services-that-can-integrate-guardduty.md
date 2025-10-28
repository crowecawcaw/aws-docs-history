# Amazon GuardDuty and

AWS Organizations

Amazon GuardDuty is a continuous security monitoring service that analyzes and processes a
variety data sources, using threat intelligence feeds and machine learning to identify
unexpected and potentially unauthorized and malicious activity within your AWS
environment. This can include issues like escalations of privileges, uses of exposed
credentials, communication with malicious IP addresses, URLs, or domains, or presence of malware
on your Amazon Elastic Compute Cloud instances and container workloads.

You can help simplify management of GuardDuty by using Organizations to manage GuardDuty across all of the
accounts in your organization.

For more information, see [Managing GuardDuty accounts with
AWS Organizations](../../../guardduty/latest/ug/guardduty_organizations.md "../../../guardduty/latest/ug/guardduty_organizations.md") in the _Amazon GuardDuty User Guide_

Use the following information to help you integrate
Amazon GuardDuty with AWS Organizations.

## Service-linked roles created when

you enable integration

The following service-linked roles are automatically created in your organization's management account when you enable trusted access. These roles allow GuardDuty to perform supported operations within your organization's accounts in your organization.
You can delete a role only if you disable trusted access between GuardDuty and Organizations, or if you remove the member account from the organization.

- The `AWSServiceRoleForAmazonGuardDuty` service-linked role is
  automatically created in accounts that have integrated GuardDuty with Organizations. For more
  information, see [Managing GuardDuty
  accounts with Organizations](../../../guardduty/latest/ug/guardduty_organizations.md "../../../guardduty/latest/ug/guardduty_organizations.md") in the
  _Amazon GuardDuty User Guide_
- The `AmazonGuardDutyMalwareProtectionServiceRolePolicy` service-linked role is automatically created in accounts that have enabled GuardDuty Malware Protection.
  For more information, see [Service-linked role permissions for GuardDuty Malware Protection](../../../guardduty/latest/ug/slr-permissions-malware-protection.md "../../../guardduty/latest/ug/slr-permissions-malware-protection.md") in the
  _Amazon GuardDuty User Guide_

## Service principals used by the

service-linked roles

- `guardduty.amazonaws.com`, used by the `AWSServiceRoleForAmazonGuardDuty` service-linked role.
- `malware-protection.guardduty.amazonaws.com`, used by the `AmazonGuardDutyMalwareProtectionServiceRolePolicy` service-linked role.

## Enabling trusted access with

GuardDuty

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only enable trusted access using
Amazon GuardDuty.

Amazon GuardDuty requires trusted access to AWS Organizations before you can designate a member
account to be the GuardDuty administrator for your organization. If you configure a
delegated administrator using the GuardDuty console, then GuardDuty automatically enables trusted
access for you.

However, if you want to configure a delegated administrator account
using the AWS CLI or one of the AWS SDKs, then you must explicitly call the [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md") operation and provide the service principal as a
parameter. Then you can call [EnableOrganizationAdminAccount](../../../guardduty/latest/APIReference/API_EnableOrganizationAdminAccount.md "../../../guardduty/latest/APIReference/API_EnableOrganizationAdminAccount.md") to delegate the GuardDuty administrator
account.

## Disabling trusted access with

GuardDuty

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable Amazon GuardDuty as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal guardduty.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for GuardDuty

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
GuardDuty that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of GuardDuty.

###### Minimum permissions

For information about the permissions required to designate a member account as a
delegated administrator, see [Permissions required to designate a delegated administrator](../../../guardduty/latest/ug/guardduty_organizations.md#organizations_permissions "../../../guardduty/latest/ug/guardduty_organizations.md#organizations_permissions") in the
_Amazon GuardDuty User Guide_

###### To designate a member account as a delegated administrator for

GuardDuty

See [Designate a delegated administrator and add member accounts (console)](../../../guardduty/latest/ug/guardduty_organizations.md#organization_thru_console "../../../guardduty/latest/ug/guardduty_organizations.md#organization_thru_console")
and [Designate a delegated administrator and add member accounts
(API)](../../../guardduty/latest/ug/guardduty_organizations.md#organization_thru_api "../../../guardduty/latest/ug/guardduty_organizations.md#organization_thru_api")
