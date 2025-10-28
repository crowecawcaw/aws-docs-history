# AWS Health and

AWS Organizations

AWS Health provides ongoing visibility into your resource performance and the
availability of your AWS services and accounts. AWS Health delivers events when your
AWS resources and services are impacted by an issue or will be affected by upcoming
changes. After you enable organizational view, a user in the organization’s management
account can aggregate AWS Health events across all accounts in the organization.
Organizational view only shows AWS Health events delivered after the feature is enabled and
retains them for 90 days.

You can enable organizational view by using the AWS Health console, the AWS Command Line Interface
(AWS CLI), or the AWS Health API.

For more information, see [Aggregating AWS Health events](../../../health/latest/ug/aggregate-events.md "../../../health/latest/ug/aggregate-events.md") in
the _AWS Health User Guide_.

Use the following information to help you integrate
AWS Health with AWS Organizations.

## Service-linked roles for integration

The `AWSServiceRoleForHealth_Organizations` service-linked role allows AWS Health to perform supported operations within
your organization's accounts in your organization.

This role is created automatically in your organization's management account when you enable trusted access
by calling the [EnableHealthServiceAccessForOrganization](../../../health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.md "../../../health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.md") API operation.
Otherwise, create the role using the AWS Health console, API, or CLI, as described in [Creating a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#create-service-linked-role") in the [IAM User Guide](../../../IAM/latest/UserGuide.md "../../../IAM/latest/UserGuide.md").

You can delete or modify this role only if you disable trusted access between AWS Health and Organizations, or if you remove the member account from the organization.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by AWS Health grant access to the following service
principals:

- `health.amazonaws.com`

## Enabling trusted access with

AWS Health

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

When you the enable organizational view feature for AWS Health, trusted access is
also enabled for you automatically.

You can enable trusted access using either the AWS Health console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Health console or
tools to enable integration with Organizations. This lets AWS Health perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Health. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Health console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the AWS Health console

You can enable trusted access by using AWS Health and one of the following
options:

- Use the AWS Health console. For more information, see [Organizational view (console)](../../../health/latest/ug/enable-organizational-view-in-health-console.md "../../../health/latest/ug/enable-organizational-view-in-health-console.md") in the _AWS Health User
  Guide_.
- Use the AWS CLI. For more information, see [Organizational view (CLI)](../../../health/latest/ug/enable-organizational-view-from-aws-command-line.md "../../../health/latest/ug/enable-organizational-view-from-aws-command-line.md") in the _AWS Health User
  Guide_.
- Call the [EnableHealthServiceAccessForOrganization](../../../health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.md "../../../health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.md") API operation.

You can enable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To enable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Health as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal health.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS Health

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

After you disable the organizational view feature, AWS Health stops aggregating
events for all other accounts in your organization. This also disables trusted access
for you automatically.

You can disable trusted access using either the AWS Health or the AWS Organizations tools.

###### Important

We strongly recommend that whenever possible, you use the AWS Health console or
tools to disable integration with Organizations. This lets AWS Health perform any
clean up that it requires, such as deleting resources or access roles that are no
longer needed by the service. Proceed with these steps only if you can’t disable
integration using the tools provided by AWS Health.

If you disable trusted access by using the AWS Health console or tools then you
don’t need to complete these steps.

###### To disable trusted access using the AWS Health console

You can disable trusted access with one of the following options:

- Use the AWS Health console. For more information, see [Disabling organizational view (console)](../../../health/latest/ug/enable-organizational-view-in-health-console.md#disabling-organizational-view-console "../../../health/latest/ug/enable-organizational-view-in-health-console.md#disabling-organizational-view-console") in the
  _AWS Health User Guide_.
- Use the AWS CLI. For more information, see [Disabling organizational view (CLI)](../../../health/latest/ug/enable-organizational-view-from-aws-command-line.md#disabling-organizational-view "../../../health/latest/ug/enable-organizational-view-from-aws-command-line.md#disabling-organizational-view") in the _AWS Health
  User Guide_.
- Call the [DisableHealthServiceAccessForOrganization](../../../health/latest/APIReference/API_DisableHealthServiceAccessForOrganization.md "../../../health/latest/APIReference/API_DisableHealthServiceAccessForOrganization.md") API operation.

You can disable trusted access by running a Organizations AWS CLI command, or by
calling an Organizations API operation in one of the AWS SDKs.

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

Use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Health as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal health.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for AWS Health

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
AWS Health that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of AWS Health.

###### To designate a member account as a delegated administrator for

AWS Health

See [Register a delegated administrator for your organizational view](../../../health/latest/ug/delegated-administrator-organizational-view.md#register-a-delegated-administrator "../../../health/latest/ug/delegated-administrator-organizational-view.md#register-a-delegated-administrator")

###### To remove a delegated administrator for

AWS Health

See [Remove a delegated administrator from your organizational view](../../../health/latest/ug/delegated-administrator-organizational-view.md#remove-a-delegated-administrator "../../../health/latest/ug/delegated-administrator-organizational-view.md#remove-a-delegated-administrator")
