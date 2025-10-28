# AWS Account Management and

AWS Organizations

AWS Account Management helps you manage the account information and metadata for all of the
AWS accounts in your organization. You can set, modify, or delete the alternate contact
information for each of your organization's member accounts. For more information, see
[Using
AWS Account Management in your organization](../../../accounts/latest/reference/using-orgs.md "../../../accounts/latest/reference/using-orgs.md") in the _AWS Account Management User
Guide_.

Use the following information to help you integrate
AWS Account Management with AWS Organizations.

## To enable trusted access with

Account Management

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

Account Management requires trusted access to AWS Organizations before you can designate a
member account to be the delegated administrator for this service for your
organization.

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
3. Choose **AWS Account Management** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Account Management** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Account Management that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Account Management as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal account.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## To disable trusted access with

Account Management

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

Only an administrator in the AWS Organizations management account can disable trusted access
with AWS Account Management.

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
3. Choose **AWS Account Management** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Account Management** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Account Management that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Account Management as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal account.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Account Management

When you designate a member account to be a delegated administrator for the
organization, users and roles from the designated account can manage the AWS account
metadata for other member accounts in the organization. If you don't enable a delegated
admin account, then these tasks can be performed only by the organization's management
account. This helps you to separate management of the organization from management of
your account details.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member account
as a delegated administrator for Account Management in the organization

For general instructions on how to configure a delegation policy, see [Create a resource-based delegation
policy with AWS Organizations](orgs-policy-delegate.md "orgs-policy-delegate.md").

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$`  `aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal account.amazonaws.com`
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service
  principal `account.amazonaws.com` as parameters.
