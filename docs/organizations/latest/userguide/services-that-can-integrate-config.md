# AWS Config and

AWS Organizations

Multi-account, multi-region data aggregation in AWS Config enables you to aggregate AWS Config data
from multiple accounts and AWS Regions into a single account. Multi-account, multi-region
data aggregation is useful for central IT administrators to monitor compliance for multiple
AWS accounts in the enterprise. An aggregator is a resource type in AWS Config that collects
AWS Config data from multiple source accounts and Regions. Create an aggregator in the Region
where you want to see the aggregated AWS Config data. While creating an aggregator, you can choose
to add either individual account IDs or your organization. For more information about AWS Config,
see the [AWS Config Developer Guide](../../../config/latest/developerguide.md "../../../config/latest/developerguide.md").

You can also use [AWS Config APIs](../../../config/latest/APIReference/welcome.md "../../../config/latest/APIReference/welcome.md") to manage AWS Config
rules across all AWS accounts in your organization. For more information, see [Enabling AWS Config Rules Across
All Accounts in Your Organization](../../../config/latest/developerguide/config-rule-multi-account-deployment.md "../../../config/latest/developerguide/config-rule-multi-account-deployment.md") in the _AWS Config Developer Guide_.

Use the following information to help you integrate
AWS Config with AWS Organizations.

## Service-linked roles

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md")
allows AWS Config to perform supported operations within the accounts in your
organization.

- `AWSServiceRoleForConfig`

Learn more about creating this role in [Permissions for the IAM Role Assigned to AWS Config](../../../config/latest/developerguide/iamrole-permissions.md "../../../config/latest/developerguide/iamrole-permissions.md") in the _AWS Config Developer Guide_

Learn more about how AWS Config uses service-linked roles in [Using Service-Linked Roles for AWS Config](../../../config/latest/developerguide/using-service-linked-roles.md "../../../config/latest/developerguide/using-service-linked-roles.md") in the _AWS Config Developer Guide_

You can delete or modify this role only if you disable trusted access between
AWS Config and Organizations, or if you remove the member account from the
organization.

## Enabling trusted access with

AWS Config

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Config console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Config console or
tools to enable integration with Organizations. This lets AWS Config perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Config. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Config console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the AWS Config console

To enable trusted access to AWS Organizations using AWS Config, create a multi-account aggregator
and add the organization. For information on how to configure a multi-account
aggregator, see [Creating Aggregators](../../../config/latest/developerguide/aggregated-create.md "../../../config/latest/developerguide/aggregated-create.md") in the _AWS Config Developer Guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Config** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Config** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Config that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Config as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal config.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS Config

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

Run the following command to disable AWS Config as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal config.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
