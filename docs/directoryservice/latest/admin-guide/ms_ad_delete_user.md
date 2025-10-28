# Deleting an AWS Managed Microsoft AD user

Use the following procedure to delete an AWS Managed Microsoft AD user with user and group management or
AWS Directory Service Data in either the AWS Management Console, AWS CLI, AWS Tools for PowerShell.

###### Important

When you delete a user's account from a directory, all information about the user is
removed, including any permissions the user has to access their account and applications.

###### Before you begin either procedure, you need to complete the following:

- [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- To use user and group management or AWS Directory Service Data CLI, it must be enabled. For more information, see
  [Enable user and group management or
  Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md "ms_ad_users_groups_mgmt_enable_disable.md").
- You can only enable this feature from the Primary AWS Region for your directory. For
  more information, see [Primary vs additional Regions](multi-region-global-primary-additional.md "multi-region-global-primary-additional.md").
- You'll need the necessary IAM permissions to use AWS Directory Service Data. For more
  information, see [AWS Directory Service API permissions: Actions,
  resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md "UsingWithDS_IAM_ResourcePermissions.md"). To get started granting permissions
  to your users and workloads, you can use AWS managed policies like [AWS managed
  policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess") or [AWS
  managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess"). For more
  information, see [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies "../../../IAM/latest/UserGuide/best-practices.md#bp-use-aws-defined-policies").
- [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md "ms_ad_create_user.md").

AWS Management Console
You can delete an AWS Managed Microsoft AD user account in the AWS Management Console.

###### To delete an AWS Managed Microsoft AD user account with the AWS Management Console

1. Open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Users**. The tab shows a list of users in your
   directory.
5. Choose the user whose account you want to delete. To find a user, enter the
   user logon name in the search box under the **Users** section.
   You're directed to the **User details** screen.
6. Choose **Actions**. Then choose **Delete user
   account** and **Delete user account** again.

AWS CLI
The following describes how to format a request that deletes an AWS Managed Microsoft AD user's
account with the AWS Directory Service Data CLI.

###### To delete an AWS Managed Microsoft AD user account with AWS CLI

- Open the AWS CLI, and run the following command, replacing the Directory ID and
  username with your AWS Managed Microsoft AD Directory ID and username:

```
aws ds-data delete-user --directory-id `d-1234567890` --sam-account-name "`jane.doe`"
```

AWS Tools for PowerShell
The following describes how to format a request that deletes an AWS Managed Microsoft AD user's
account with AWS Tools for PowerShell.

###### To delete an AWS Managed Microsoft AD user account with AWS Tools for PowerShell

- Open PowerShell, and run the following command, replacing the
  Directory ID and username with your AWS Managed Microsoft AD Directory ID and username:

```
Remove-DSDUser -DirectoryId `d-1234567890` -SAMAccountName "`jane.doe`"
```
