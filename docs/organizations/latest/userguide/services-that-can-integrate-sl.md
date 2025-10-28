# Amazon Security Lake and

AWS Organizations

Amazon Security Lake centralizes security data from cloud, on-premises, and custom sources into a data lake that's stored in your account.
By integrating with Organizations, you can create a data lake that collects logs and events across your accounts. For more information see [Managing multiple accounts with AWS Organizations](../../../security-lake/latest/userguide/multi-account-management.md "../../../security-lake/latest/userguide/multi-account-management.md") in the _Amazon Security Lake user guide_.

Use the following information to help you integrate
Amazon Security Lake with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../aws-backup/latest/devguide/manage-cross-account.md#backup-delegatedadmin "../../../aws-backup/latest/devguide/manage-cross-account.md#backup-delegatedadmin") is automatically created
in your organization's management account when you call the [RegisterDataLakeDelegatedAdministrator](../../../security-lake/latest/APIReference/API_RegisterDataLakeDelegatedAdministrator.md "../../../security-lake/latest/APIReference/API_RegisterDataLakeDelegatedAdministrator.md") API.
This role allows Amazon Security Lake to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Amazon Security Lake and Organizations,
or if you remove the member account from the organization.

- `AWSServiceRoleForSecurityLake`

###### Recommendation: Use Security Lake's RegisterDataLakeDelegatedAdministrator

API to allow Security Lake access to your Organization and to register Organizations's delegated administrator

If you use Organizations' APIs to register a delegated administrator, service-linked roles for the Organizations might not be created successfully.
To ensure full functionality, use the Security Lake APIs.

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon Security Lake grant access to the following service
principals:

- `securitylake.amazonaws.com`

## Enabling trusted access with

Amazon Security Lake

When you enable trusted access with Security Lake,
Security Lake can react automatically to changes in the organization membership. The delegated administrator
can enable AWS logs collection from supported services in any organization account.
For more information, see [Service-linked role for Amazon Security Lake](../../../security-lake/latest/userguide/service-linked-roles.md "../../../security-lake/latest/userguide/service-linked-roles.md") in the _Amazon Security Lake user guide_.

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
3. Choose **Amazon Security Lake** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for Amazon Security Lake** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon Security Lake that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable Amazon Security Lake as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal securitylake.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Amazon Security Lake

Only an administrator in the Organizations management account can disable trusted access with Amazon Security Lake.

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
3. Choose **Amazon Security Lake** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for Amazon Security Lake** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon Security Lake that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable Amazon Security Lake as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal securitylake.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Amazon Security Lake

The Amazon Security Lake delegated administrator adds other accounts in the organization as member accounts.
The delegated administrator can enable Amazon Security Lake and configure Amazon Security Lake settings for the member accounts.
The delegated administrator can collect logs across an organization in all AWS Regions where Amazon Security Lake is enabled
(regardless of which Regional endpoint you're currently using).

You can also set up the delegated administrator to automatically add new accounts in the organization as members.
The Amazon Security Lake delegated administrator has access to the logs and events in associated member accounts.
Accordingly, you can set up Amazon Security Lake to collect data owned by associated member accounts. You can also grant subscribers permission
to consume data owned by associated member accounts.

For more information see [Managing multiple accounts with AWS Organizations](../../../security-lake/latest/userguide/multi-account-management.md "../../../security-lake/latest/userguide/multi-account-management.md") in the _Amazon Security Lake user guide_.

###### Minimum permissions

Only an administrator in the Organizations management account can configure a member
account as a delegated administrator for Amazon Security Lake in the
organization

You can specify a delegated administrator account by using the Amazon Security Lake console, the Amazon Security Lake
`CreateDatalakeDelegatedAdmin` API operation, or the `create-datalake-delegated-admin` CLI command.
Alternatively, you can use the Organizations `RegisterDelegatedAdministrator` CLI or SDK operation. For instructions about
enabling a delegated administrator account for Amazon Security Lake, see
[Designating the delegated Security Lake administrator and adding member accounts](../../../security-lake/latest/userguide/multi-account-management.md#designated-admin "../../../security-lake/latest/userguide/multi-account-management.md#designated-admin") in the _Amazon Security Lake user guide_.

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$`  `aws organizations register-delegated-administrator \
 --account-id 123456789012 \ --service-principal securitylake.amazonaws.com`
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service principal
  `account.amazonaws.com` as parameters.

## Disabling a delegated administrator

for Amazon Security Lake

Only an administrator in either the Organizations management account or the Amazon Security Lake
delegated administrator account can remove a delegated administrator account from the
organization.

You can remove the delegated administrator account by using the Amazon Security Lake
`DeregisterDataLakeDelegatedAdministrator` API operation, the
`deregister-data-lake-delegated-administrator` CLI command, or by using the Organizations
`DeregisterDelegatedAdministrator` CLI or SDK operation. To remove a
delegated administrator using Amazon Security Lake, see [Removing the
Amazon Security Lake delegated administrator](../../../security-lake/latest/userguide/multi-account-management.md#remove-delegated-admin "../../../security-lake/latest/userguide/multi-account-management.md#remove-delegated-admin") in the
_Amazon Security Lake user guide_.
