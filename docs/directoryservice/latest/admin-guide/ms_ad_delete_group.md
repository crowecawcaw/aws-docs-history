# Deleting an AWS Managed Microsoft AD group

Use the following procedure to delete an AWS Managed Microsoft AD group with user and group management or
AWS Directory Service Data in either the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

###### Important

When you delete a group, all information about the group is removed, including any
permissions that group members inherit.

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
- [Create an AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").

AWS Management Console
You can delete an AWS Managed Microsoft AD group in the AWS Management Console.

###### To delete an AWS Managed Microsoft AD group with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Group**. The tab shows a list of groups in your
   AWS Region.
5. Choose the group that you want to delete. To find groups, enter the group name
   in the search box under the **Groups** section. You're directed to
   the **Group details** screen.
6. Choose **Delete group**. A dialog box appears where you can
   choose **Confirm** to delete the group.

AWS CLI
The following describes how to format a request that deletes an AWS Managed Microsoft AD group
with the AWS Directory Service Data CLI.

###### To delete an AWS Managed Microsoft AD group with the AWS CLI

- Open the AWS CLI, and run the following command, replacing the Directory ID and
  group name with your AWS Managed Microsoft AD Directory ID and group name:

```
aws ds-data delete-group --directory-id `d-1234567890` --sam-account-name "`your-group-name`"
```

AWS Tools for PowerShell
The following describes how to format a request that deletes an AWS Managed Microsoft AD group
with the AWS Tools for PowerShell.

###### To delete an AWS Managed Microsoft AD group with the AWS Tools for PowerShell

- Open PowerShell, and run the following command, replacing the
  Directory ID and group name with your AWS Managed Microsoft AD Directory ID and group name:

```
Remove-DSDGroup -DirectoryId `d-1234567890` -SAMAccountName "`your-group-name`"
```
