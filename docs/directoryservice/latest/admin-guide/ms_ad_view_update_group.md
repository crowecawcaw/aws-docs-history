

# Viewing and updating an AWS Managed Microsoft AD group's details
<a name="ms_ad_view_update_group"></a>

Use the following procedure to view or update an AWS Managed Microsoft AD group's details with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

## Viewing an AWS Managed Microsoft AD group's detail
<a name="ms_ad_view_group"></a>

You can view or update a group's details in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ [Creating an AWS Managed Microsoft AD group](ms_ad_create_group.md).

------
#### [ AWS Management Console ]

 You can view an AWS Managed Microsoft AD group's details in the AWS Management Console.

**To view AWS Managed Microsoft AD group's details with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1. From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Group**. The tab shows a list of groups in your AWS Region. 

1.  Choose a group. To find groups, enter the group name in the search box under the **Groups** section. You're directed to the **Group details** screen. The **Group details** screen shows the following information: 
   +  **Member** tab lists the users and child groups that are members of your group.
   +  **Parent groups** tab lists the parent groups that your group is a member of.
   +  **Properties** tab lists the group properties (such as primary information like group name, group display name, etc.).

------
#### [ AWS CLI ]

 You can view an AWS Managed Microsoft AD group's details with the AWS Directory Service Data CLI. 
+  To view a group's details, open the AWS CLI, and run the following command with your Directory ID and group name: 

```
aws ds-data describe-group --directory-id {{d-1234567890}} --sam-account-name "{{your-group-name}}"
```

For more information, see [`describe-group`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/describe-group.html).
+  To view a group's members, open the AWS CLI, and run the following command with your Directory ID and group name: 

```
aws ds-data list-group-members --directory-id {{d-1234567890}} --sam-account-name "{{your-group-name}}"
```

For more information, see [`list-group-members`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/list-group-members.html).

------
#### [ PowerShell ]

 You can view an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell. 
+ To view a group's details, open PowerShell, and run the following command with your Directory ID and group name: 

```
Get-DSDGroup -DirectoryId {{d-1234567890}} -SAMAccountName "{{your-group-name}}"
```

For more information, see [`Get-DSDGroup`](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-DSDGroup.html).
+  To view a group's members, open PowerShell, and run the following command with your Directory ID and group name: 

```
(Get-DSDGroupMemberList -DirectoryId {{d-1234567890}} -SAMAccountName "{{your-group-name}}").Members
```

For more information, see [`Get-DSDGroupMemberList`](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-DSDGroupMemberList.html).

------

## Updating an AWS Managed Microsoft AD group's details
<a name="ms_ad_update_group"></a>

Use the following procedure to update an AWS Managed Microsoft AD group's details with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

------
#### [ AWS Management Console ]

You can update a group's details with the AWS Management Console. For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Group type and group scope](ad_group_type_and_scope.md)

**To update an AWS Managed Microsoft AD group's details with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Group**. The tab shows a list of groups in your AWS Region. 

1.  Choose a group. To find groups, enter the group name in the search box under the **Groups** section. You're directed to the **Group details** screen. 

1.  To edit users and child groups that are members of your group, choose **Members**. From this tab, you can add and remove users and child groups from your group. For more information, see [Adding and removing members to groups and groups to groups](ms_ad_add_remove_user_group.md). 

1.  To edit parent groups that your group is a member of, choose **Parent groups**. From this tab, you can add and remove your group from parent groups. For more information, see [Adding and removing members to groups and groups to groups](ms_ad_add_remove_user_group.md).

1.  To edit your group properties, choose **Properties**, and then choose **Edit**. Or choose **Actions**, and then choose **Edit group**. Make and review your updates, and then choose **Save**. 

------
#### [ AWS CLI ]

 The following describes how to format a request that updates an AWS Managed Microsoft AD group's details with the AWS Directory Service Data CLI. 

 When you update a group, you must include your directory ID number and group name. You also must include the update type and attribute you want to update in your request, such as a group email address with the `EmailAddress` parameter. For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Group type and group scope](ad_group_type_and_scope.md). 
+ 

**To update an AWS Managed Microsoft AD group's details with the AWS CLI**

   To update a group's details, open the AWS CLI, and run the following command with your Directory ID, group name, update type, and attribute: 

```
aws ds-data update-group \
  --directory-id {{d-1234567890}} \
  --sam-account-name "{{your-group-name}}" \
  --update-type "{{REPLACE}}" \
  --group-scope {{"global"}}
```

For more information, see [`update-group`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/update-group.html).

------
#### [ PowerShell ]

 The following describes how to format a request that updates an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell. 

 When you update a group, you must include your directory ID number and group name. You also must include the update type and attribute you want to update in your request, such as a group email address with the `EmailAddress` parameter. For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Group type and group scope](ad_group_type_and_scope.md). 
+ 

**To update an AWS Managed Microsoft AD group's details with AWS Tools for PowerShell**

   To update a group's details, open PowerShell, and run the following command with your Directory ID, group name, update type, and attribute: 

```
Update-DSDGroup `
    -DirectoryId {{d-1234567890}} `
    -SAMAccountName "{{your-group-name}}" `
    -UpdateType "{{REPLACE}}" `
    -GroupScope "{{global}}"
```

For more information, see [`Update-DSDGroup`](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-DSDGroup.html).

------