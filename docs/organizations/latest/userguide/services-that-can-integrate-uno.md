# AWS User Notifications and

AWS Organizations

[AWS User Notifications](https://aws.amazon.com/notifications "https://aws.amazon.com/notifications") is a central location for your AWS notifications.

After you integrate with AWS Organizations, you can configure and view notifications centrally across accounts in your organization.

Use the following information to help you integrate
AWS User Notifications with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows User Notifications to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
User Notifications and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForAWSUserNotifications`

For more information, see [Using Service-Linked Roles](../../../notifications/latest/userguide/using-service-linked-roles.md "../../../notifications/latest/userguide/using-service-linked-roles.md") in the _AWS User Notifications User Guide_.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by User Notifications grant access to the following service
principals:

- `notifications.amazon.com`

## Enabling trusted access with

User Notifications

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only enable trusted access using
AWS User Notifications.

To enable trusted access using the User Notifications console, see [Enabling AWS Organizations in AWS User Notifications](../../../notifications/latest/userguide/uno-orgs.md "../../../notifications/latest/userguide/uno-orgs.md") in the
_User Notifications User Guide_.

## Disabling trusted access with

User Notifications

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can only enable trusted access using
AWS User Notifications.

To disable trusted access using the User Notifications console, see [Enabling AWS Organizations in AWS User Notifications](../../../notifications/latest/userguide/uno-orgs.md "../../../notifications/latest/userguide/uno-orgs.md") in the
_User Notifications User Guide_.

## Enabling a delegated administrator

account for User Notifications

The management account administrator can delegate User Notifications administrative permissions
to a designated member account known as delegated administrator. To register an account as a delegated administrator
for the private marketplace, the management account administrator must ensure that trusted access and the service-linked role are enabled,
choose **Register a new administrator**, provide the 12-digit AWS account number, and choose **Submit**.

Management accounts and delegated administrator accounts can perform User Notifications administrative tasks,
such as creating experiences, updating branding settings, associating or disassociating audiences,
adding or removing products, and approving or declining pending requests.

To configure a delegated administrator using the User Notifications console, see [Registering delegated administrators in AWS User Notifications](../../../notifications/latest/userguide/uno-orgs.md#register-admins "../../../notifications/latest/userguide/uno-orgs.md#register-admins") in the
_User Notifications User Guide_.

You can also configure a delegated administrator by using
the Organizations `RegisterDelegatedAdministrator` API. For more information, see [RegisterDelegatedAdministrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md") in the _Organizations
Command Reference_.

## Disabling a delegated administrator

for User Notifications

Only an administrator in the organization management account can configure a delegated
administrator for User Notifications.

You can remove the delegated administrator using either the User Notifications console or API, or
by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation.

To disable the delegated admin User Notifications account using the User Notifications console, see [Removing delegated administrators in in AWS User Notifications](../../../notifications/latest/userguide/uno-orgs.md#deregister-admins "../../../notifications/latest/userguide/uno-orgs.md#deregister-admins") in the
_User Notifications User Guide_.
