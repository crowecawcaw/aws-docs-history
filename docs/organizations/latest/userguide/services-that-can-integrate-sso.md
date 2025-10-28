# AWS IAM Identity Center and

AWS Organizations

AWS IAM Identity Center provides single sign-on access for all of your AWS accounts and
cloud applications. It connects with Microsoft Active Directory through AWS Directory Service to allow
users in that directory to sign in to a personalized AWS access portal using their existing Active
Directory user names and passwords. From the AWS access portal, users have access to all the AWS accounts and cloud applications that they have permissions for.

For more information about IAM Identity Center, see the [AWS IAM Identity Center User Guide](../../../singlesignon/latest/userguide.md "../../../singlesignon/latest/userguide.md").

Use the following information to help you integrate
AWS IAM Identity Center with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows IAM Identity Center to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
IAM Identity Center and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForSSO`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by IAM Identity Center grant access to the following service
principals:

- `sso.amazonaws.com`

## Enabling trusted access with

IAM Identity Center

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS IAM Identity Center console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS IAM Identity Center console or
tools to enable integration with Organizations. This lets AWS IAM Identity Center perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS IAM Identity Center. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS IAM Identity Center console or tools then you
don’t need to complete these steps.

IAM Identity Center requires trusted access with AWS Organizations to function. Trusted access is enabled
when you set up IAM Identity Center. For more information, see [Getting Started - Step 1: Enable AWS IAM Identity Center](../../../singlesignon/latest/userguide/step1.md "../../../singlesignon/latest/userguide/step1.md")
in the _AWS IAM Identity Center User Guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS IAM Identity Center** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS IAM Identity Center** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS IAM Identity Center that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS IAM Identity Center as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal sso.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

IAM Identity Center

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

IAM Identity Center requires trusted access with AWS Organizations to operate. If you disable trusted access
using AWS Organizations while you are using IAM Identity Center, it stops functioning because it can't access
the organization. Users can't use IAM Identity Center to access accounts. Any roles that IAM Identity Center creates
remain, but the IAM Identity Center service can't access them. The IAM Identity Center service-linked roles remain.
If you reenable trusted access, IAM Identity Center continues to operate as before, without the need
for you to reconfigure the service.

If you remove an account from your organization, IAM Identity Center automatically cleans up any
metadata and resources, such as its service-linked role. A standalone account that is
removed from an organization no longer works with IAM Identity Center.

You can only disable trusted access using the Organizations
tools.

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS IAM Identity Center** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS IAM Identity Center** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS IAM Identity Center that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS IAM Identity Center as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal sso.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for IAM Identity Center

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
IAM Identity Center that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of IAM Identity Center.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for IAM Identity Center in the
organization.

For instructions about how to enable a delegated administrator account for IAM Identity Center, see
[Delegated
administration](../../../singlesignon/latest/userguide/delegated-admin.md "../../../singlesignon/latest/userguide/delegated-admin.md") in the _AWS IAM Identity Center User Guide_.
