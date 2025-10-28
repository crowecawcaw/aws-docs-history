# AWS Artifact and

AWS Organizations

AWS Artifact is a service that allows you to download AWS security compliance reports such
as ISO and PCI reports. Using AWS Artifact, a user in the organization's management account can
automatically accept agreements on behalf of all member accounts in an organization, even as
new reports and accounts are added. Member account users can view and download agreements.
For more information, see [Managing an agreement for multiple
accounts in AWS Artifact](../../../artifact/latest/ug/manage-org-agreement.md "../../../artifact/latest/ug/manage-org-agreement.md") in the _AWS Artifact User Guide_.

Use the following information to help you integrate
AWS Artifact with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows AWS Artifact to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
AWS Artifact and Organizations, or if you remove the member account from the organization.

Although you can delete or modify this role if you remove the member account from the
organization, we do not recommend it.

Modifying the role is discouraged because it can lead to security issues such as the
cross-service confused deputy. To learn more about protection against confused deputy,
see [Cross-service deputy
prevention](../../../artifact/latest/ug/security-iam.md#confused-deputy "../../../artifact/latest/ug/security-iam.md#confused-deputy") in the _AWS Artifact User Guide_.

- `AWSServiceRoleForArtifact`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by AWS Artifact grant access to the following service
principals:

- `artifact.amazonaws.com`

## Enabling trusted access with

AWS Artifact

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

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
3. Choose **AWS Artifact** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Artifact** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Artifact that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Artifact as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal artifact.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS Artifact

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Only an administrator in the AWS Organizations management account can disable trusted access
with AWS Artifact.

You can only disable trusted access using the Organizations
tools.

AWS Artifact requires trusted access with AWS Organizations to work with organization agreements. If
you disable trusted access using AWS Organizations while you are using AWS Artifact for organization
agreements, it stops functioning because it cannot access the organization. Any
organization agreements that you accept in AWS Artifact remain, but can't be accessed by AWS Artifact.
The AWS Artifact role that AWS Artifact creates remains. If you then re-enable trusted access, AWS Artifact
continues to operate as before, without the need for you to reconfigure the service.

A standalone account that is removed from an organization no longer has access to any
organization agreements.

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Artifact** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Artifact** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Artifact that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Artifact as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal artifact.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
