# AWS Trusted Advisor and

AWS Organizations

AWS Trusted Advisor inspects your AWS environment and makes recommendations when opportunities
exist to save money, to improve system availability and performance, or to help close
security gaps. When integrated with Organizations, you can receive Trusted Advisor check results for all of
the accounts in your organization and download reports to view the summaries of your checks
and any affected resources.

For more information, see [Organizational view for
AWS Trusted Advisor](../../../awssupport/latest/user/organizational-view.md "../../../awssupport/latest/user/organizational-view.md") in the _AWS Support User Guide_.

Use the following information to help you integrate
AWS Trusted Advisor with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Trusted Advisor to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Trusted Advisor and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForTrustedAdvisorReporting`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Trusted Advisor grant access to the following service
principals:

- `reporting.trustedadvisor.amazonaws.com`

## Enabling trusted access with

Trusted Advisor

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can only enable trusted access using
AWS Trusted Advisor.

###### To enable trusted access using the Trusted Advisor console

See [Enable organizational view](../../../awssupport/latest/user/organizational-view.md#enable-organizational-view "../../../awssupport/latest/user/organizational-view.md#enable-organizational-view") in the _AWS Support
User Guide_.

## Disabling trusted access with

Trusted Advisor

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

After you disable this feature, Trusted Advisor stops recording check information for all
other accounts in your organization. You can't view or download existing reports or
create new reports.

You can disable trusted access using either the AWS Trusted Advisor or the AWS Organizations tools.

###### Important

We strongly recommend that whenever possible, you use the AWS Trusted Advisor console or
tools to disable integration with Organizations. This lets AWS Trusted Advisor perform any
clean up that it requires, such as deleting resources or access roles that are no
longer needed by the service. Proceed with these steps only if you can’t disable
integration using the tools provided by AWS Trusted Advisor.

If you disable trusted access by using the AWS Trusted Advisor console or tools then you
don’t need to complete these steps.

###### To disable trusted access using the Trusted Advisor console

See [Disable organizational view](../../../awssupport/latest/user/organizational-view.md#disable-organizational-view "../../../awssupport/latest/user/organizational-view.md#disable-organizational-view") in the _AWS Support
User Guide_.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Trusted Advisor as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal reporting.trustedadvisor.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Trusted Advisor

When you designate a member account to be a delegated administrator for the
organization, users and roles from the designated account can manage the AWS account
metadata for other member accounts in the organization. If you don't enable a delegated
admin account, then these tasks can be performed only by the organization's management
account. This helps you to separate management of the organization from management of
your account details.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for Trusted Advisor in the
organization

For instruction about enabling a delegated administrator account for Trusted Advisor, see
[Register delegated administrators](../../../awssupport/latest/user/trusted-advisor-priority.md#register-delegated-administrators "../../../awssupport/latest/user/trusted-advisor-priority.md#register-delegated-administrators") in the _Support User Guide_.

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$`  `aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal reporting.trustedadvisor.amazonaws.com`
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service principal
  `account.amazonaws.com` as parameters.

## Disabling a delegated administrator

for Trusted Advisor

You can remove the delegated administrator using either the Trusted Advisor console, or by using the the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. For information on how to disable the delegated admin Trusted Advisor account using the Trusted Advisor console,
see [Deregister delegated administrators](../../../awssupport/latest/user/trusted-advisor-priority.md#deregister-delegated-administrators "../../../awssupport/latest/user/trusted-advisor-priority.md#deregister-delegated-administrators") in the _Support user guide_.
