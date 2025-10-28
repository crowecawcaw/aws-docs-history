# Amazon Detective and AWS Organizations

Amazon Detective uses your log data to generate visualizations that allow you to analyze,
investigate, and identify the root cause of security findings or suspicious activity.

Using AWS Organizations allows you to ensure that your Detective behavior graph provides visibility
into the activity for all of your organization accounts.

When you grant trusted access to Detective, the Detective service can react automatically to
changes in the organization membership. The delegated administrator can enable any
organization account as a member account in the behavior graph. Detective also can automatically
enable new organization accounts as member accounts. Organization accounts cannot
disassociate themselves from the behavior graph.

For more information, see [Using Amazon Detective in your
organization](../../../detective/latest/adminguide/accounts-orgs-transition.md "../../../detective/latest/adminguide/accounts-orgs-transition.md") in the _Amazon Detective Administration Guide_.

Use the following information to help you integrate Amazon Detective with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Detective to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Detective and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForDetective`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Detective grant access to the following service
principals:

- `detective.amazonaws.com`

## To enable trusted access with

Detective

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

###### Note

When you designate a delegated administrator for Amazon Detective, Detective automatically
enables trusted access for Detective for your organization.

Detective requires trusted access to AWS Organizations before you can designate a member
account to be the delegated administrator for this service for your
organization.

You can only enable trusted access using the Organizations
tools.

You can enable trusted access by using the AWS Organizations console.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **Amazon Detective** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for Amazon Detective** dialog
   box, type **enable** to confirm it, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon Detective that they can now enable that service
   to work with AWS Organizations from the service console .

## To disable trusted access with

Detective

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Only an administrator in the AWS Organizations management account can disable trusted access
with Amazon Detective.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by using the AWS Organizations console.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **Amazon Detective** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for Amazon Detective** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon Detective that they can now disable that service from working with AWS Organizations
   using tthe service console or tools;.

## Enabling a delegated administrator

account for Detective

The delegated administrator account for Detective is the administrator account for a Detective
behavior graph. The delegated administrator determines which organization accounts to
enable and disable as member accounts in that behavior graph. The delegated
administrator can configure Detective to automatically enable new organization accounts as
member accounts as they are added to the organization. For information on how a
delegated administrator manages organization accounts, see [Managing organization
accounts as member accounts](../../../detective/latest/adminguide/accounts-orgs-members.md "../../../detective/latest/adminguide/accounts-orgs-members.md") in the _Amazon Detective Administration
Guide_.

Only an administrator in the organization management account can configure a delegated
administrator for Detective.

You can specify a delegated administrator account from the Detective console or API, or by
using the Organizations CLI or SDK operation.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for Detective in the organization

To configure a delegated administrator using the Detective console or API, see [Designating a
Detective administrator account for an organization](../../../detective/latest/adminguide/accounts-designate-admin.md "../../../detective/latest/adminguide/accounts-designate-admin.md") in the
_Amazon Detective Administration Guide_.

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$` **aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal detective.amazonaws.com**
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service principal
  `account.amazonaws.com` as parameters.

## Disabling a delegated administrator

for Detective

You can remove the delegated administrator using either the Detective console or API, or
by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation. For information on how to remove a delegated administrator using the Detective
console or API, or the Organizations API, see [Designating a
Detective administrator account for an organization](../../../detective/latest/adminguide/accounts-designate-admin.md "../../../detective/latest/adminguide/accounts-designate-admin.md") in the
_Amazon Detective Administration Guide_.
