

# Creating an AWS Managed Microsoft AD group
<a name="ms_ad_create_group"></a>

Use the following procedure to create an AWS Managed Microsoft AD group with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).

------
#### [ AWS Management Console ]

 You can create a new AWS Managed Microsoft AD group in the AWS Management Console. When you create a new group, you specify the group's details and determine the [group's type and scope](ad_group_type_and_scope.md). You also have the option to add users and child groups to your new group or add your new group to a parent group.

**To create an AWS Managed Microsoft AD group with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Group**. The tab shows a list of groups in your AWS Region. 

1.  Choose **Create group**. You're directed to a procedure where you finish creating your new group. 

1. The **Specify group details** page opens. Enter a **Group name**. Group names must meet the following conditions:
   + Must be unique group name
   + Can be up to 64 characters long
   + Can only contain alphanumeric characters
   + \~\!@\#$%^&\*\_-\+=`\|\\(){}[]:;"'<>,.?/
**Warning**  
The group name cannot be changed after the group is created.

1. Choose the **Group type** from one of the following:
   + **Security**
   + **Distribution**
     + To learn more, see [Group type](ad_group_type_and_scope.md#ad_group_type).

1. Choose the **Group scope** from one of the following:
   + **Domain local**
   + **Universal**
   + **Global**
     + You can turn on **Compare scopes** to display a chart of the similarities and differences between group scopes. To learn more, see [Group scope](ad_group_type_and_scope.md#ad_group_scope).

1. After providing the primary information and contact methods, choose **Next**.

1. The **Add users to group - *Optional*** page opens and you can add users to the new group. To find a user to add to the group, enter the user logon name in the search box under the **Users** section. Select the users you want to add to the group and choose **Next**.

1. The **Add child groups - *Optional*** page opens and you can add existing groups to the new group. The existing groups becomes child groups of the newly created group. When you add a child group to your group, your group becomes the parent group, and the child group inherits all of your group's roles and permissions. To find groups to add, enter the group name in the search box under the **Add child groups** section. Select the children groups you want to add to the new group and choose **Next**.

1. The **Add parent groups - *Optional*** page opens and you can add the new group to existing groups. The new group becomes the parent group of the existing groups. When you add your group to a parent group, your group becomes the child group and inherits all of the parent group's roles and permissions. To find groups to add, enter the group name in the search box under the **Add parent groups** section. Select the parent groups you want to add to the new group and choose **Next**.

1. On the **Review and create group** page, review your choices, and then choose **Create group**.

------
#### [ AWS CLI ]

 The following describes how to format a request that creates an AWS Managed Microsoft AD group with the AWS Directory Service Data CLI. When you create a new group, you must include your Directory ID number and a group name. You can also add other attributes, such as a group display name with the `DisplayName` attribute. For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Group type and group scope](ad_group_type_and_scope.md). 

**To create an AWS Managed Microsoft AD group with the AWS CLI**
+  Open the AWS CLI, and run the following command with your Directory ID, group name, and display name: 

```
aws ds-data create-group \
    --directory-id {{d-1234567890}} \
    --sam-account-name "{{your-group-name}}" \
    --other-attributes '{
        "DisplayName": { "S": "{{myGroupDisplayName}}"},
        "Description":{ "S": "{{myGroupDescription}}"}
    }'
```

For more information, see [`create-group`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/create-group.html).

------
#### [ PowerShell ]

 The following describes how to format a request that creates an AWS Managed Microsoft AD group with AWS Tools for PowerShell. When you create a new group, you must include your Directory ID number and a group name. You can also add other attributes, such as a group display name with the `DisplayName` attribute. For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Group type and group scope](ad_group_type_and_scope.md). 

**To create an AWS Managed Microsoft AD group with AWS Tools for PowerShell**
+  Open PowerShell, and run the following command with your Directory ID, group name, and display name:

```
New-DSDGroup `
    -DirectoryId {{d-1234567890}} `
    -SAMAccountName "{{your-group-name}}" `
    -OtherAttribute @{
        DisplayName = [Amazon.DirectoryServiceData.Model.AttributeValue]@{S = '{{myGroupDisplayName}}' }
        Description = [Amazon.DirectoryServiceData.Model.AttributeValue]@{S = '{{myGroupDescription}}' }
    }
```

For more information, see [`New-DSDGroup`](https://docs.aws.amazon.com/powershell/latest/reference/items/New-DSDGroup.html).

------