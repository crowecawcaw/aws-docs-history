# AWS Resource Access Manager and

AWS Organizations

AWS Resource Access Manager (AWS RAM) enables you to share specified AWS resources that you own with other
AWS accounts. It's a centralized service that provides a consistent experience for sharing
different types of AWS resources across multiple accounts.

For more information about AWS RAM, see the [_AWS RAM User Guide_](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md").

Use the following information to help you integrate
AWS Resource Access Manager with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows AWS RAM to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
AWS RAM and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForResourceAccessManager`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by AWS RAM grant access to the following service
principals:

- `ram.amazonaws.com`

## Enabling trusted access with

AWS RAM

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Resource Access Manager console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Resource Access Manager console or
tools to enable integration with Organizations. This lets AWS Resource Access Manager perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Resource Access Manager. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Resource Access Manager console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the AWS RAM console or CLI

See [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
_AWS RAM User Guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Resource Access Manager** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Resource Access Manager** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Resource Access Manager that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Resource Access Manager as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal ram.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

AWS RAM

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can disable trusted access using either the AWS Resource Access Manager or the AWS Organizations tools.

###### Important

We strongly recommend that whenever possible, you use the AWS Resource Access Manager console or
tools to disable integration with Organizations. This lets AWS Resource Access Manager perform any
clean up that it requires, such as deleting resources or access roles that are no
longer needed by the service. Proceed with these steps only if you can’t disable
integration using the tools provided by AWS Resource Access Manager.

If you disable trusted access by using the AWS Resource Access Manager console or tools then you
don’t need to complete these steps.

###### To disable trusted access using the AWS Resource Access Manager console or CLI

See [Enable Sharing with AWS Organizations](../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs "../../../ram/latest/userguide/getting-started-sharing.md#getting-started-sharing-orgs") in the
_AWS RAM User Guide_.

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Resource Access Manager** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Resource Access Manager** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Resource Access Manager that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Resource Access Manager as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal ram.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")
