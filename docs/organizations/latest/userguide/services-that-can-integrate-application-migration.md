# AWS Application Migration Service (Application Migration Service) and

AWS Organizations

AWS Application Migration Service simplifies, expedites, and reduces the cost of migrating applications to AWS.
By integrating with Organizations, you can use the global view feature to manage large-scale migrations across multiple accounts. For more information see [Setting up your AWS Organizations](../../../mgn/latest/ug/setting-up-organizations.md "../../../mgn/latest/ug/setting-up-organizations.md") in the _Application Migration Service user guide_.

Use the following information to help you integrate
AWS Application Migration Service with AWS Organizations.

## Service-linked roles created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's management account when you enable trusted
access. This role allows Application Migration Service to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Application Migration Service and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForApplicationMigrationService`

## Service principals used by Application Migration Service

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Application Migration Service grant access to the following service
principals:

- `mgn.amazonaws.com`

## Enabling trusted access with

Application Migration Service

When you enable trusted access with Application Migration Service you can use the global view feature, which allows you to manage
large-scale migrations across multiple accounts. Global view provides visibility and the ability to perform
specific actions on source servers, apps, and waves in different AWS accounts.
For more information, see [Setting up your AWS Organizations](../../../mgn/latest/ug/setting-up-organizations.md "../../../mgn/latest/ug/setting-up-organizations.md") in the _AWS Application Migration Service user guide_.

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the AWS Application Migration Service console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the AWS Application Migration Service console or
tools to enable integration with Organizations. This lets AWS Application Migration Service perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by AWS Application Migration Service. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the AWS Application Migration Service console or tools then you
don’t need to complete these steps.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Application Migration Service** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for AWS Application Migration Service** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Application Migration Service that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable AWS Application Migration Service as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal mgn.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Application Migration Service

Only an administrator in the Organizations management account can disable trusted access with Application Migration Service.

You can disable trusted access using either the AWS Application Migration Service or the AWS Organizations tools.

###### Important

We strongly recommend that whenever possible, you use the AWS Application Migration Service console or
tools to disable integration with Organizations. This lets AWS Application Migration Service perform any
clean up that it requires, such as deleting resources or access roles that are no
longer needed by the service. Proceed with these steps only if you can’t disable
integration using the tools provided by AWS Application Migration Service.

If you disable trusted access by using the AWS Application Migration Service console or tools then you
don’t need to complete these steps.

You can disable trusted access by using either the AWS Organizations console,
by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

AWS Management Console

###### To disable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **AWS Application Migration Service** in the list of services.
4. Choose **Disable trusted access**.
5. In the **Disable trusted access for AWS Application Migration Service** dialog
   box, type **disable** to confirm, and then choose **Disable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of AWS Application Migration Service that they can now disable that service from working with AWS Organizations
   using the service console or tools .

AWS CLI, AWS API

###### To disable trusted service access using the Organizations CLI/SDK

You can use the following AWS CLI commands or API operations to disable
trusted service access:

- AWS CLI: [disable-aws-service-access](../../../cli/latest/reference/organizations/disable-aws-service-access.md "../../../cli/latest/reference/organizations/disable-aws-service-access.md")

Run the following command to disable AWS Application Migration Service as a
trusted service with Organizations.

```
`$` **aws organizations disable-aws-service-access \
 --service-principal mgn.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [DisableAWSServiceAccess](../APIReference/API_DisableAWSServiceAccess.md "../APIReference/API_DisableAWSServiceAccess.md")

## Enabling a delegated administrator

account for Application Migration Service

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
Application Migration Service that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of Application Migration Service. For more information see [Setting up your AWS Organizations](../../../mgn/latest/ug/setting-up-organizations.md "../../../mgn/latest/ug/setting-up-organizations.md") in the _Application Migration Service user guide_.

###### Minimum permissions

Only a user or role in the Organizations management account can configure a member
account as a delegated administrator for Application Migration Service in the organization

AWS CLI, AWS API
If you want to configure a delegated administrator account using the AWS
CLI or one of the AWS SDKs, you can use the following commands:

- AWS CLI:

```
`$` **aws organizations register-delegated-administrator \
 --account-id 123456789012 \
 --service-principal mgn.amazonaws.com**
```

- AWS SDK: Call the Organizations
  `RegisterDelegatedAdministrator` operation and the
  member account's ID number and identify the account service
  `mgn.amazonaws.com` as parameters.

## Disabling a delegated administrator

for Application Migration Service

Only an administrator in the Organizations management account can remove a delegated
administrator for Application Migration Service. You can remove the delegated administrator using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.
