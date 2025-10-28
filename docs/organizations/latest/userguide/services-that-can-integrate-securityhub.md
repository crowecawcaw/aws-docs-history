# AWS Security Hub and

AWS Organizations

AWS Security Hub provides you with a comprehensive view of your security state in AWS and helps
you check your environment against security industry standards and best practices.

Security Hub collects security data from across your AWS accounts, the AWS services you use,
and supported third-party partner products. It helps you to analyze your security trends and
identify the highest priority security issues.

When you use both Security Hub and AWS Organizations together, you can automatically enable Security Hub for all
of your accounts, including new accounts as they are added. This increases the coverage for
Security Hub checks and findings, which provides a more comprehensive and accurate picture of your
overall security posture.

For more information about Security Hub, see the _[AWS Security Hub User Guide](../../../securityhub/latest/userguide.md "../../../securityhub/latest/userguide.md")_.

Use the following information to help you integrate
AWS Security Hub with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Security Hub to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Security Hub and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForSecurityHub`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Security Hub grant access to the following service
principals:

- `securityhub.amazonaws.com`

## Enabling trusted access with

Security Hub

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

When you designate a delegated administrator for Security Hub, Security Hub automatically enables
trusted access for Security Hub in your organization.

## Disabling trusted access with

Security Hub

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms") in the _AWS Organizations User Guide_.

Before you disable trusted access, we recommend working with the delegated administrator for your organization to disable Security Hub in member accounts and to clean up Security Hub resources in those accounts.

You can disable trusted access by using the AWS Organizations console, Organizations API, or the AWS CLI.
Only an administrator of the Organizations management account can disable trusted access with Security Hub.

For instructions on disabling trusted access with Security Hub, see [Disabling Security Hub integration with AWS Organizations](../../../securityhub/latest/userguide/designate-orgs-admin-account.md#disable-orgs-integration "../../../securityhub/latest/userguide/designate-orgs-admin-account.md#disable-orgs-integration").

## Enabling a delegated administrator

for Security Hub

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
Security Hub that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of Security Hub.

For information, see [Designating a Security Hub administrator account](../../../securityhub/latest/userguide/designate-orgs-admin-account.md "../../../securityhub/latest/userguide/designate-orgs-admin-account.md") in the
_AWS Security Hub User Guide_.

###### To designate a member account as a delegated administrator for

Security Hub

1. Sign in with your Organizations management account.
2. Perform one of the following:
   - If your management account does not have Security Hub enabled, then on the
     Security Hub console, choose **Go to Security Hub**.
   - If your management account does have Security Hub enabled, then on the Security Hub
     console, under **General** choose **Settings**.

3. Under **Delegated Administrator**, enter the account
   ID.

## Disabling a delegated administrator

for Security Hub

Only the organization management account can remove the delegated Security Hub administrator account.

To change the delegated Security Hub administrator, you must first remove the current delegated administrator account and then designate a new one.

If you use the Security Hub console to remove the
delegated administrator in one Region, it is automatically removed in all Regions.

The Security Hub API only removes the delegated Security Hub administrator account from the Region where
the API call or command is issued. You must repeat the action in other Regions.

If you use the Organizations API to remove the delegated Security Hub administrator account, it is automatically
removed in all Regions.

For instructions on disabling the delegated Security Hub administrator, see [Removing or changing the delegated administrator](../../../securityhub/latest/userguide/designate-orgs-admin-account.md#remove-admin-overview "../../../securityhub/latest/userguide/designate-orgs-admin-account.md#remove-admin-overview").
