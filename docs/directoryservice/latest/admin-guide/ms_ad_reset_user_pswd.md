# Resetting and enabling an AWS Managed Microsoft AD user's

password

Use the following procedure to reset an AWS Managed Microsoft AD user's password to enable their
account with user and group management or AWS Directory Service Data in either the AWS Management Console, AWS CLI,
AWS Tools for PowerShell.

###### Before you begin either procedure, you need to complete the following:

- [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- To use user and group management or AWS Directory Service Data CLI, it must be enabled. For more information, see
  [Enable user and group management or
  Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md "ms_ad_users_groups_mgmt_enable_disable.md").
- You can only enable this feature from the Primary AWS Region for your directory. For
  more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
- You'll need the necessary IAM permissions to use AWS Directory Service Data. For more
  information, see [Directory Service API permissions: Actions,
  resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md"). To get started granting permissions
  to your users and workloads, you can use AWS managed policies like [AWS managed
  policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess") or [AWS
  managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess"). For more
  information, see [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies").
- [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md "ms_ad_create_user.md").

AWS Management Console
You can reset an AWS Managed Microsoft AD user's password to enable their account in the
AWS Management Console. You can perform this task from either the **Directories**
screen or **Directory details** screen.

###### Directories

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose **Actions**, and then choose **Reset user
   password and enable account**.
   1. Under **User logon name**, enter the user logon name for
      the user whose password you want to reset.
   2. Under **New password**, enter the user's new password.
   3. Under **Confirm password**, enter user's new password
      again.

4. After you confirm the user's new password, choose **Reset password and
   enable account**.

###### Directory details

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Users**. The tab shows a list of users in your
   directory.
5. Select the user whose password you want to reset.
6. Choose **Actions**, and then choose **Reset user
   password and enable account**.
   1. Under **New password**, enter the user's new password.
   2. Under **Confirm password**, enter user's new password
      again.

7. After you confirm the user's new password, choose **Reset password and
   enable account**.

AWS CLI
You can reset an AWS Managed Microsoft AD use's password to enable their account with the
AWS Directory Service Data CLI.

###### Note

The reset user's password command uses `aws ds`.

###### To reset an AWS Managed Microsoft AD user's password with the AWS CLI

- To reset a user's password, open the AWS CLI, and run the following command,
  replacing the Directory ID, username, and password with your AWS Managed Microsoft AD Directory
  ID, username, and desired credentials:

```
aws ds reset-user-password --directory-id `d-1234567890` --user-name "`jane.doe`" --new-password "`your-password`"
```

AWS Tools for PowerShell
You can reset an AWS Managed Microsoft AD use's password to enable their account with
AWS Tools for PowerShell.

###### To reset an AWS Managed Microsoft AD user's password with AWS Tools for PowerShell

- To reset a user's password, open the PowerShell, and run the
  following command, replacing the Directory ID, username, and password with your
  AWS Managed Microsoft AD Directory ID, username, and desired credentials:

```
Reset-DSUserPassword -DirectoryId `d-1234567890` -UserName "`jane.doe`" -NewPassword "`your-password`"
```
