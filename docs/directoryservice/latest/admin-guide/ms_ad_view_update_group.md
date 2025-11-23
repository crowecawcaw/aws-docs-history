# Viewing and updating an AWS Managed Microsoft AD group's

details

Use the following procedure to view or update an AWS Managed Microsoft AD group's details with
user and group management or AWS Directory Service Data in either the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

## Viewing an AWS Managed Microsoft AD group's detail

You can view or update a group's details in the AWS Management Console, AWS CLI, or
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
- [Creating an AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").

AWS Management Console
You can view an AWS Managed Microsoft AD group's details in the AWS Management Console.

###### To view AWS Managed Microsoft AD group's details with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Group**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. To find groups, enter the group name in the search box under
   the **Groups** section. You're directed to the **Group
   details** screen. The **Group details** screen shows
   the following information:
   - **Member** tab lists the users and child groups that are
     members of your group.
   - **Parent groups** tab lists the parent groups that your group
     is a member of.
   - **Properties** tab lists the group properties (such as
     primary information like group name, group display name, etc.).

AWS CLI
You can view an AWS Managed Microsoft AD group's details with the AWS Directory Service Data CLI.

###### To view an AWS Managed Microsoft AD group's details with the AWS CLI

The following describes how to view an AWS Managed Microsoft AD group's details with the
AWS CLI.

- To view a group's details, open the AWS CLI, and run the following command,
  replacing the Directory ID and group name with your AWS Managed Microsoft AD Directory ID and
  group name:

```
aws ds-data describe-group --directory-id `d-1234567890` --sam-account-name "`your-group-name`"
```

###### To view an AWS Managed Microsoft AD group's group members with the AWS CLI

The following describes how to view an AWS Managed Microsoft AD group's members with the
AWS CLI.

- To view a group's details, open the AWS CLI, and run the following command,
  replacing the Directory ID and group name with your AWS Managed Microsoft AD Directory ID and
  group name:

```
aws ds-data list-group-members --directory-id `d-1234567890` --sam-account-name "`your-group-name`"
```

AWS Tools for PowerShell
You can view an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell.

###### To view an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell

The following describes how to view an AWS Managed Microsoft AD group's details with the
Tools for PowerShell.

- To view a group's details, open the PowerShell, and run the
  following command, replacing the Directory ID and group name with your
  AWS Managed Microsoft AD Directory ID and group name:

```
Get-DSDGroup -DirectoryId `d-1234567890` -SAMAccountName "`your-group-name`"
```

###### To view an AWS Managed Microsoft AD group's group members with AWS Tools for PowerShell

The following describes how to view an AWS Managed Microsoft AD group's members with the
Tools for PowerShell.

- To view a group's details, open the PowerShell, and run the
  following command, replacing the Directory ID and group name with your
  AWS Managed Microsoft AD Directory ID and group name:

```
(Get-DSDGroupMemberList -DirectoryId `d-1234567890` -SAMAccountName "`your-group-name`").Members
```

## Updating an AWS Managed Microsoft AD group's details

Use the following procedure to update an AWS Managed Microsoft AD group's details with
user and group management or AWS Directory Service Data in either the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

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
- [Creating an AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").

AWS Management Console
You can update a group's details with the AWS Management Console. For more information,
see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md")

###### To update an AWS Managed Microsoft AD group's details with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and
   then choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Group**. The tab shows a list of groups in your
   AWS Region.
5. Choose a group. To find groups, enter the group name in the search box under
   the **Groups** section. You're directed to the **Group
   details** screen.
6. To edit users and child groups that are members of your group, choose
   **Members**. From this tab, you can add and remove users and
   child groups from your group. For more information, see [Adding and removing members to
   groups and groups to groups](ms_ad_add_remove_user_group.md "ms_ad_add_remove_user_group.md").
7. To edit parent groups that your group is a member of, choose **Parent
   groups**. From this tab, you can add and remove your group from parent
   groups. For more information, see [Adding and removing members to
   groups and groups to groups](ms_ad_add_remove_user_group.md "ms_ad_add_remove_user_group.md").
8. To edit your group properties, choose **Properties**, and
   then choose **Edit**. Or choose **Actions**, and
   then choose **Edit group**. Make and review your updates, and
   then choose **Save**.

AWS CLI
The following describes how to format a request that updates an AWS Managed Microsoft AD
group's details with the AWS Directory Service Data CLI.

When you update a group, you must include your directory ID number and group
name. You also must include the update type and attribute you want to update in your
request, such as a group email address with the `EmailAddress` parameter.
For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md").

- ###### To update an AWS Managed Microsoft AD group's details with the AWS CLI

To update a group's details, open the AWS CLI, and run the following command,
replacing the Directory ID, group name, update type, and attribute with your
AWS Managed Microsoft AD Directory ID, group name, and desired update type and attribute:

```
aws ds-data update-group --directory-id `d-1234567890` --sam-account-name "`your-group-name`" --update-type "`REPLACE`" --group-scope `"global"`
```

AWS Tools for PowerShell
The following describes how to format a request that updates an AWS Managed Microsoft AD
group's details with AWS Tools for PowerShell.

When you update a group, you must include your directory ID number and group
name. You also must include the update type and attribute you want to update in your
request, such as a group email address with the `EmailAddress` parameter.
For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md").

- ###### To update an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell

To update a group's details, open the PowerShell, and run the
following command, replacing the Directory ID, group name, update type, and
attribute with your AWS Managed Microsoft AD Directory ID, group name, and desired update type
and attribute:

```
Update-DSDGroup -DirectoryId `d-1234567890` -SAMAccountName "`your-group-name`" -UpdateType "`REPLACE`" -GroupScope "`global`"
```
