# Amazon VPC Reachability Analyzer and AWS Organizations

Reachability Analyzer is a configuration analysis tool that enables you to perform connectivity testing between a source resource and a destination resource in your virtual private clouds (VPCs).

Using AWS Organizations with Reachability Analyzer allows you to trace paths across accounts in your organizations.

For more information, see [Manage delegated administrator accounts in Reachability Analyzer](../../../vpc/latest/reachability/manage-delegated-administrators.md "../../../vpc/latest/reachability/manage-delegated-administrators.md") in the _Reachability Analyzer user guide_.

Use the following information to help you integrate Reachability Analyzer with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Reachability Analyzer to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Reachability Analyzer and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForReachabilityAnalyzer`

For more information, see [Cross-account analyses for Reachability Analyzer](../../../vpc/latest/reachability/multi-account.md "../../../vpc/latest/reachability/multi-account.md") in the _Reachability Analyzer user guide_.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Reachability Analyzer grant access to the following service
principals:

- `reachabilityanalyzer.networkinsights.amazonaws.com`

## To enable trusted access with

Reachability Analyzer

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

When you designate a delegated administrator for Reachability Analyzer it automatically enables
trusted access for Reachability Analyzer for your organization.

Reachability Analyzer requires trusted access to AWS Organizations before you can designate a member
account to be the delegated administrator for this service for your
organization.

###### Important

- You can enable trusted access using either the Reachability Analyzer console or the Organizations console. However, we strongly recommend that you use the Reachability Analyzer console or the `EnableMultiAccountAnalysisForAwsOrganization` API to enable integration with Organizations.
  This lets Reachability Analyzer perform any configuration that it requires, such as creating resources needed by the service.
- Granting trusted access creates the service-linked role
  `AWSServiceRoleForReachabilityAnalyzer` in the management account and in
  all of the member accounts in the organization. Reachability Analyzer uses the service-linked role to
  allow management, and the delegated administrator to run connectivity analyses between
  any resources in the organization. Reachability Analyzer is able to take snapshots of the networking
  elements of the accounts in an organization in order to answer connectivity queries.
- For
  more information, and for instructions on enabling trusted access through Reachability Analyzer, see [Cross-account analyses for Reachability Analyzer](../../../vpc/latest/reachability/multi-account.md "../../../vpc/latest/reachability/multi-account.md") in the _Reachability Analyzer user guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. On the **[Services](https://console.aws.amazon.com/organizations/v2/home/services "https://console.aws.amazon.com/organizations/v2/home/services")** page, find the row for
   **VPC Reachability Analyzer**, choose the service’s name, and
   then choose **Enable trusted access**.
3. In the confirmation dialog box, enable **Show the option to
   enable trusted access**, enter `enable`
   in the box, and then choose **Enable trusted
   access**.
4. If you are the administrator of only AWS Organizations, tell the
   administrator of Reachability Analyzer that they can now enable that service
   using its console to work with AWS Organizations.

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

You can use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

You can run the following command to enable Reachability Analyzer as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal reachabilityanalyzer.networkinsights.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## To disable trusted access with

Reachability Analyzer

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can disable trusted access using either the Reachability Analyzer console (recommended), or the Organizations console. To disable trusted access using the Reachability Analyzer console, see [Cross-account analyses for Reachability Analyzer](../../../vpc/latest/reachability/multi-account.md "../../../vpc/latest/reachability/multi-account.md") in the _Reachability Analyzer user guide_.

## Enabling a delegated administrator

account for Reachability Analyzer

The delegated administrator account is able to run connectivity analyses across any of the resources in the organization.
For more information, see [Integrate Reachability Analyzer
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Reachability Analyzer user guide_.

Only an administrator in the organization management account can configure a delegated
administrator for Reachability Analyzer.

You can specify a delegated administrator account from the Reachability Analyzer console, or by using
the `RegisterDelegatedAdministrator` API. For more information, see [RegisterDelegatedAdministrator](../../../cli/latest/reference/organizations/register-delegated-administrator.md "../../../cli/latest/reference/organizations/register-delegated-administrator.md") in the _Organizations
Command Reference_.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for Reachability Analyzer in the organization

To configure a delegated administrator using the Reachability Analyzer console, see [Integrate Reachability Analyzer
with AWS Organizations](../../../vpc/latest/ipam/enable-integ-ipam.md "../../../vpc/latest/ipam/enable-integ-ipam.md") in the _Reachability Analyzer user guide_.

## Disabling a delegated administrator

for Reachability Analyzer

Only an administrator in the organization management account can configure a delegated
administrator for Reachability Analyzer.

You can remove the delegated administrator using either the Reachability Analyzer console or API, or
by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK
operation.

To disable the delegated admin Reachability Analyzer account using the Reachability Analyzer console, see [Cross-account analyses for Reachability Analyzer](../../../vpc/latest/reachability/multi-account.md "../../../vpc/latest/reachability/multi-account.md") in the _Reachability Analyzer user guide_.
