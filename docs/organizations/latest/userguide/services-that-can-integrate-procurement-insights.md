# AWS Marketplace procurement insights dashboard and

AWS Organizations

You use the AWS Marketplace procurement insights dashboard to view agreements and cost-analysis data for all of the AWS accounts in your organization.
When integrated with Organizations, AWS Marketplace procurement insights dashboard listens to organization changes,
such as an account joining the organization, and aggregates data for their corresponding agreements to build their dashboards.

For more information, see [Procurement insights](../../../marketplace/latest/buyerguide/procurement-insights.md "../../../marketplace/latest/buyerguide/procurement-insights.md")  
 in the _AWS Marketplace Buyer Guide_.

Use the following information to help you integrate
AWS Marketplace procurement insights dashboard with AWS Organizations.

## Service-linked roles and managed policies created when

you enable integration

When you activate the AWS Marketplace procurement insights dashboard dashboard the [`AWSServiceRoleForProcurementInsightsPolicy`](../../../marketplace/latest/buyerguide/buyer-service-linked-role-procurement.md "../../../marketplace/latest/buyerguide/buyer-service-linked-role-procurement.md") service-linked role and the [`AWSServiceRoleForProcurementInsightsPolicy`](../../../marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.md#aws-procurement-insights "../../../marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.md#aws-procurement-insights") AWS managed policy are created.

## Enabling trusted access with

AWS Marketplace procurement insights

Enabling trusted access grants the AWS Marketplace procurement insights dashboard the ability to integrate with the customer's Organizations service. AWS Marketplace procurement insights dashboard listens to organization changes, such as an account joining the organization, and aggregates data for their corresponding agreements to build their dashboards.

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Marketplace procurement insights dashboard console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Marketplace procurement insights dashboard console or
tools to enable integration with Organizations. This lets AWS Marketplace procurement insights dashboard perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Marketplace procurement insights dashboard. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Marketplace procurement insights dashboard console or tools then you
don’t need to complete these steps.

###### To enable trusted access by enabling the AWS Marketplace procurement insights dashboard

See [Enabling the AWS Marketplace procurement insights dashboard](../../../marketplace/latest/buyerguide/enabling-procurement-insights.md "../../../marketplace/latest/buyerguide/enabling-procurement-insights.md") in the
_AWS Marketplace Buyer Guide_.

**To enable trusted access using Organizations tools**

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Marketplace procurement insights dashboard** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Marketplace procurement insights dashboard** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Marketplace procurement insights dashboard that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Marketplace procurement insights dashboard as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal procurement-insights.marketplace.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS Marketplace procurement insights

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

Run the following command to disable AWS Marketplace procurement insights dashboard as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal procurement-insights.marketplace.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for AWS Marketplace procurement insights

To configure a delegated administrator in the AWS Marketplace procurement insights console, see See [Registering delegated administrators>](../../../marketplace/latest/buyerguide/management-delegates.md#management-register-delegate "../../../marketplace/latest/buyerguide/management-delegates.md#management-register-delegate") in the
_AWS Marketplace Buyer Guide_.

You can also configure a delegated administrator by using
the Organizations `RegisterDelegatedAdministrator` API. For more information, see [RegisterDelegatedAdministrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md") in the _Organizations
Command Reference_.

## Disabling a delegated administrator

for AWS Marketplace procurement insights

Only an administrator in the organization management account can configure a delegated
administrator for AWS Marketplace procurement insights.

To remove a delegated administrator through the AWS Marketplace procurement insights console, see [Deregistering delegated administrators](../../../marketplace/latest/buyerguide/management-delegates.md#management-deregister-delegate "../../../marketplace/latest/buyerguide/management-delegates.md#management-deregister-delegate") in the
_AWS Marketplace Buyer Guide_.

You can also remove the delegated administrator by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation.
