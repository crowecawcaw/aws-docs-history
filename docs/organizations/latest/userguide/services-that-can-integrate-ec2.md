# Amazon Elastic Compute Cloud and

AWS Organizations

Amazon Elastic Compute Cloud provides on-demand, scalable computing capacity in the AWS Cloud.
When you use Amazon EC2 with Organizations; you enable the Organizations admin to create a report of what the existing configuration is for accounts across their organization
after using Amazon EC2's [Declarative Policies](orgs_manage_policies_declarative.md "orgs_manage_policies_declarative.md") feature.

Use the following information to help you integrate
Amazon Elastic Compute Cloud with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Amazon EC2 to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Amazon EC2 and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForDeclarativePoliciesEC2Report`

## Service principals used by Amazon EC2

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon EC2 grant access to the following service
principals:

- `ec2.amazonaws.com`

## Enabling trusted access with

Amazon EC2

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

To enable the Organizations admin to create a report of what the existing configuration is for accounts across their organization, you must enable trusted access.

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
3. Choose **Declarative Policy for EC2** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for Declarative Policy for EC2** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon Elastic Compute Cloud that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable Amazon Elastic Compute Cloud as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal ec2.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access

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

Run the following command to disable Amazon Elastic Compute Cloud as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal ec2.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
