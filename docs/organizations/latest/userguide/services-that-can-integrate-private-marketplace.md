# AWS Marketplace Private Marketplace and

AWS Organizations

AWS Marketplace is a curated digital catalog that you can use to find, buy, deploy, and manage
third-party software, data, and services that you need to build solutions and run your
businesses. A private marketplace provides you with a broad catalog of products available in AWS Marketplace, along with ﬁne-grained control of those products.

AWS Marketplace Private Marketplace enables you to create multiple private marketplace experiences that are associated with your
entire organization, one or more OUs, or one or more accounts in your organization, each with its own set of
approved products. Your AWS administrators can also apply company branding to each private marketplace experience
with your company or team’s logo, messaging, and color scheme.

For more information, see [Using roles to configure Private Marketplace in AWS Marketplace](../../../marketplace/latest/buyerguide/using-service-linked-roles-private-marketplace.md "../../../marketplace/latest/buyerguide/using-service-linked-roles-private-marketplace.md")
in the _AWS Marketplace Buyer Guide_.

Use the following information to help you integrate
AWS Marketplace Private Marketplace with AWS Organizations.

## Service-linked roles created when

you enable integration

The following service-linked role is automatically created in your organization's
management account when you enable trusted access using the AWS Marketplace Private Marketplace console. This
role allows Private Marketplace to perform supported operations within your
organization's accounts in your organization. You can delete or modify this role only if
you disable trusted access between AWS Marketplace Private Marketplace and Organizations and disassociate all private
marketplace experiences in your organization.

If you enable trusted access directly from the Organizations console, CLI or SDK, the service-linked role is not created automatically.

- `AWSServiceRoleForPrivateMarketplaceAdmin`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Private Marketplace grant access to the following service
principals:

- `private-marketplace.marketplace.amazonaws.com`

## Enabling trusted access with

Private Marketplace

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Marketplace Private Marketplace console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Marketplace Private Marketplace console or
tools to enable integration with Organizations. This lets AWS Marketplace Private Marketplace perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Marketplace Private Marketplace. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Marketplace Private Marketplace console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the Private Marketplace console

See [Getting started with Private Marketplace](../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-getting-started "../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-getting-started") in the
_AWS Marketplace Buyer Guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Marketplace Private Marketplace** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Marketplace Private Marketplace** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Marketplace Private Marketplace that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Marketplace Private Marketplace as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal private-marketplace.marketplace.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Private Marketplace

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Marketplace Private Marketplace as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal private-marketplace.marketplace.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Private Marketplace

The management account administrator can delegate Private Marketplace administrative permissions
to a designated member account known as delegated administrator. To register an account as a delegated administrator
for the private marketplace, the management account administrator must ensure that trusted access and the service-linked role are enabled,
choose **Register a new administrator**, provide the 12-digit AWS account number, and choose **Submit**.

Management accounts and delegated administrator accounts can perform Private Marketplace administrative tasks,
such as creating experiences, updating branding settings, associating or disassociating audiences,
adding or removing products, and approving or declining pending requests.

To configure a delegated administrator using the Private Marketplace console, see [Creating and managing a private marketplace](../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-managing "../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-managing") in the
_AWS Marketplace Buyer Guide_.

You can also configure a delegated administrator by using
the Organizations `RegisterDelegatedAdministrator` API. For more information, see [RegisterDelegatedAdministrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md") in the _Organizations
Command Reference_.

## Disabling a delegated administrator

for Private Marketplace

Only an administrator in the organization management account can configure a delegated
administrator for Private Marketplace.

You can remove the delegated administrator using either the Private Marketplace console or API, or
by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation.

To disable the delegated admin Private Marketplace account using the Private Marketplace console, see [Creating and managing a private marketplace](../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-managing "../../../marketplace/latest/buyerguide/private-catalog-administration.md#private-marketplace-managing") in the
_AWS Marketplace Buyer Guide_
