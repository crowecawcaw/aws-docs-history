# Setting Amazon S3 Storage Lens permissions

Amazon S3 Storage Lens requires new permissions in AWS Identity and Access Management (IAM) to authorize access to S3 Storage Lens
actions. To grant these permissions, you can use an identity-based IAM policy. You can
attach this policy to IAM users, groups, or roles to grant them permissions. Such
permissions can include the ability to enable or disable S3 Storage Lens, or to access any S3 Storage Lens
dashboard or configuration.

The IAM user or role must belong to the account that created or owns the dashboard or
configuration, unless both of the following conditions are true:

- Your account is a member of AWS Organizations.
- You were given access to create organization-level dashboards by your management
  account as a delegated administrator.

###### Note

- You can't use your account's root user credentials to view Amazon S3 Storage Lens dashboards. To
  access S3 Storage Lens dashboards, you must grant the required IAM permissions to a new or
  existing IAM user. Then, sign in with those user credentials to access S3 Storage Lens
  dashboards. For more information, see [Security best practices in
  IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.
- Using S3 Storage Lens on the Amazon S3 console can require multiple permissions. For example, to
  edit a dashboard on the console, you need the following permissions:
  - `s3:ListStorageLensConfigurations`
  - `s3:GetStorageLensConfiguration`
  - `s3:PutStorageLensConfiguration`

###### Topics

- [Setting account permissions to use S3 Storage Lens](#storage_lens_iam_permissions_account "#storage_lens_iam_permissions_account")
- [Setting account permissions to use S3 Storage Lens groups](#storage_lens_groups_permissions "#storage_lens_groups_permissions")
- [Setting permissions to use S3 Storage Lens with AWS Organizations](#storage_lens_iam_permissions_organizations "#storage_lens_iam_permissions_organizations")

## Setting account permissions to use S3 Storage Lens

To create and manage S3 Storage Lens dashboards and Storage Lens dashboard configurations, you
must have the following permissions, depending on which actions you want to perform:

The following table shows Amazon S3 Storage Lens related IAM permissions.

| Action                                                                                   | IAM permissions                                                                                                                                                                                  |
| ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create or update an S3 Storage Lens dashboard in the Amazon S3 console.                  | `s3:ListStorageLensConfigurations`<br>`s3:GetStorageLensConfiguration`<br>`s3:GetStorageLensConfigurationTagging`<br>`s3:PutStorageLensConfiguration`<br>`s3:PutStorageLensConfigurationTagging` |
| Get the tags of an S3 Storage Lens dashboard on the Amazon S3 console.                   | `s3:ListStorageLensConfigurations`<br>`s3:GetStorageLensConfigurationTagging`                                                                                                                    |
| View an S3 Storage Lens dashboard on the Amazon S3 console.                              | `s3:ListStorageLensConfigurations`<br>`s3:GetStorageLensConfiguration`<br>`s3:GetStorageLensDashboard`                                                                                           |
| Delete an S3 Storage Lens dashboard on Amazon S3 console.                                | `s3:ListStorageLensConfigurations`<br>`s3:GetStorageLensConfiguration`<br>`s3:DeleteStorageLensConfiguration`                                                                                    |
| Create or update an S3 Storage Lens configuration by using the AWS CLI or an AWS<br>SDK. | `s3:PutStorageLensConfiguration`<br>`s3:PutStorageLensConfigurationTagging`                                                                                                                      |
| Get the tags of an S3 Storage Lens configuration by using the AWS CLI or an AWS<br>SDK.  | `s3:GetStorageLensConfigurationTagging`                                                                                                                                                          |
| View an S3 Storage Lens configuration by using the AWS CLI or an AWS SDK.                | `s3:GetStorageLensConfiguration`                                                                                                                                                                 |
| Delete an S3 Storage Lens configuration by using the AWS CLI or AWS SDK.                 | `s3:DeleteStorageLensConfiguration`                                                                                                                                                              |

###### Note

- You can use resource tags in an IAM policy to manage permissions.
- An IAM user or role with these permissions can see metrics from buckets and
  prefixes that they might not have direct permission to read or list objects
  from.
- For S3 Storage Lens dashboards with prefix-level metrics enabled, if a selected prefix
  path matches with an object key, the dashboard might display the object key as another
  prefix.
- For metrics exports, which are stored in a bucket in your account, permissions are
  granted by using the existing `s3:GetObject` permission in the IAM
  policy. Similarly, for an AWS Organizations entity, the organization's management account or
  delegated administrator accounts can use IAM policies to manage access permissions
  for organization-level dashboard and configurations.

## Setting account permissions to use S3 Storage Lens groups

You can use S3 Storage Lens groups to understand the distribution of your storage within
buckets based on prefix, suffix, object tag, object size, or object age. You can attach
Storage Lens groups to your dashboards to view their aggregated metrics.

To work with Storage Lens groups, you need certain permissions. For more information,
see [Storage Lens groups permissions](storage-lens-groups.md#storage-lens-group-permissions "storage-lens-groups.md#storage-lens-group-permissions").

## Setting permissions to use S3 Storage Lens with AWS Organizations

You can use Amazon S3 Storage Lens to collect storage metrics and usage data for all accounts that
are part of your AWS Organizations hierarchy. The following table shows the actions and permissions related
to using S3 Storage Lens with Organizations.

| Action                                                                                                                                        | IAM Permissions                                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Enable trusted access for S3 Storage Lens for your organization.                                                                              | `organizations:EnableAWSServiceAccess`                                                                                                                                                                      |
| Disable trusted access for S3 Storage Lens for your organization.                                                                             | `organizations:DisableAWSServiceAccess`                                                                                                                                                                     |
| Register a delegated administrator to create S3 Storage Lens dashboards or<br>configurations for your organization.                           | `organizations:RegisterDelegatedAdministrator`                                                                                                                                                              |
| Deregister a delegated administrator so that they can no longer create S3 Storage Lens<br>dashboards or configurations for your organization. | `organizations:DeregisterDelegatedAdministrator`                                                                                                                                                            |
| Additional permissions to create S3 Storage Lens organization-wide<br>configurations.                                                         | `organizations:DescribeOrganization`<br>`organizations:ListAccounts`<br>`organizations:ListAWSServiceAccessForOrganization`<br>`organizations:ListDelegatedAdministrators`<br>`iam:CreateServiceLinkedRole` |
