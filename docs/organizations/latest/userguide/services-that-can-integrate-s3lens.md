# Amazon S3 Storage Lens and

AWS Organizations

By giving Amazon S3 Storage Lens trusted access to your organization, you allow it to collect
and aggregate metrics across all of the AWS accounts in your organization. S3 Storage Lens
does this by accessing the list of accounts that belong to your organization and collects
and analyzes the storage and usage and activity metrics for all of them.

For more information, see the [Using
service-linked roles for Amazon S3 Storage Lens](../../../AmazonS3/latest/dev/using-service-linked-roles.md "../../../AmazonS3/latest/dev/using-service-linked-roles.md") in the _Amazon S3 Storage Lens User
Guide_.

Use the following information to help you integrate
Amazon S3 Storage Lens with AWS Organizations.

## Service-linked role created when

you enable integration

The following [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md") is
automatically created in your organization's delegated administrator account when you enable trusted
access and the Storage Lens configuration has been applied to your organization. This role allows Amazon S3 Storage Lens to perform supported operations within your
organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between
Amazon S3 Storage Lens and Organizations, or if you remove the member account from the organization.

- `AWSServiceRoleForS3StorageLens`

## Service principals used by the

service-linked roles

The service-linked role in the previous section can be
assumed only by the service principals authorized by the trust relationships defined for the
role. The service-linked roles used by Amazon S3 Storage Lens grant access to the following service
principals:

- `storage-lens.s3.amazonaws.com`

## Enabling trusted access with

Amazon S3 Storage Lens

For information about the permissions needed to enable trusted
access, see [Permissions required to enable trusted
access](orgs_integrate_services.md#orgs_trusted_access_perms "orgs_integrate_services.md#orgs_trusted_access_perms").

You can enable trusted access using either the Amazon S3 Storage Lens console or the AWS Organizations
console.

###### Important

We strongly recommend that whenever possible, you use the Amazon S3 Storage Lens console or
tools to enable integration with Organizations. This lets Amazon S3 Storage Lens perform any
configuration that it requires, such as creating resources needed by the service.
Proceed with these steps only if you can’t enable integration using the tools
provided by Amazon S3 Storage Lens. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration "orgs_integrate_services.md#important-note-about-integration").

If you enable trusted access by using the Amazon S3 Storage Lens console or tools then you
don’t need to complete these steps.

###### To enable trusted access using the Amazon S3 console

See [Enabling trusted access for S3 Storage Lens](../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_enabling_trusted_access "../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_enabling_trusted_access") in the _Amazon Simple Storage Service User Guide_.

You can enable trusted access by using either
the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in
one of the AWS SDKs.

AWS Management Console

###### To enable trusted service access using the Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, assume an IAM role, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management account.
2. In the navigation pane, choose **Services**.
3. Choose **Amazon S3 Storage Lens** in the list of services.
4. Choose **Enable trusted access**.
5. In the **Enable trusted access for Amazon S3 Storage Lens** dialog
   box, type **enable** to confirm, and then choose **Enable trusted
   access**.
6. If you are the administrator of only AWS Organizations, tell the
   administrator of Amazon S3 Storage Lens that they can now enable that service to work with AWS Organizations
   from the service console .

AWS CLI, AWS API

###### To enable trusted service access using the OrganizationsCLI/SDK

Use the following AWS CLI commands or API operations to enable
trusted service access:

- AWS CLI: [enable-aws-service-access](../../../cli/latest/reference/organizations/enable-aws-service-access.md "../../../cli/latest/reference/organizations/enable-aws-service-access.md")

Run the following command to enable Amazon S3 Storage Lens as a
trusted service with Organizations.

```
`$` **aws organizations enable-aws-service-access \
 --service-principal storage-lens.s3.amazonaws.com**
```

This command produces no output when successful.

- AWS API: [EnableAWSServiceAccess](../APIReference/API_EnableAWSServiceAccess.md "../APIReference/API_EnableAWSServiceAccess.md")

## Disabling trusted access with

Amazon S3 Storage Lens

For information about the permissions needed to disable trusted
access, see [Permissions required to disable
trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms "orgs_integrate_services.md#orgs_trusted_access_disable_perms").

You can only disable trusted access using the
Amazon S3 Storage Lens tools.

You can disable trusted access using the Amazon S3 console, the AWS CLI or any of
the AWS SDKs.

###### To disable trusted access using the Amazon S3 console

See [Disabling trusted access for S3 Storage Lens](../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_disabling_trusted_access "../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_disabling_trusted_access") in the _Amazon Simple Storage Service User Guide_.

## Enabling a delegated administrator

account for Amazon S3 Storage Lens

When you designate a member account as a delegated administrator for the organization,
users and roles from that account can perform administrative actions for
Amazon S3 Storage Lens that otherwise can be performed only by users or roles in the
organization's management account. This helps you to separate management of the
organization from management of Amazon S3 Storage Lens.

###### Minimum permissions

Only a user or role in the Organizations management account with the following
permission can configure a member account as a delegated administrator for
Amazon S3 Storage Lens in the organization:

`organizations:RegisterDelegatedAdministrator`

`organizations:DeregisterDelegatedAdministrator`

Amazon S3 Storage Lens supports a maximum of 5 delegated administrator accounts in your
organization.

###### To designate a member account as a delegated administrator for

Amazon S3 Storage Lens

You can register a delegated administrator using the Amazon S3 console, the AWS CLI or any of the AWS SDKs. To register a member account as a delegated
administrator account for your organization using the Amazon S3 console, see [Registering a delegated administrator for S3 Storage Lens](../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_registering_delegated_admins "../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_registering_delegated_admins") in the
_Amazon Simple Storage Service User Guide_.

###### To deregister a delegated administrator for Amazon S3 Storage Lens

You can deregister a delegated administrator using the Amazon S3 console, the
AWS CLI or any of the AWS SDKs. To deregister a delegated administrator using
the Amazon S3 console, see [Deregistering a delegated administrator for S3 Storage Lens](../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_deregistering_delegated_admins "../../../AmazonS3/latest/user-guide/storage_lens_with_organizations.md#storage_lens_with_organizations_deregistering_delegated_admins") in the
_Amazon Simple Storage Service User Guide_.
