

# Viewing and updating an AWS Managed Microsoft AD user
<a name="ms_ad_view_update_user"></a>

Use the following procedure to view or update an AWS Managed Microsoft AD user's details with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

## Viewing an AWS Managed Microsoft AD user's details
<a name="ms_ad_view_user"></a>

You can view a user's details in the AWS Management Console or AWS CLI. The user's details include profile and account information and group membership.

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md).

------
#### [ AWS Management Console ]

 You can view an AWS Managed Microsoft AD user's details in the AWS Management Console.

**To view an AWS Managed Microsoft AD user's details and account details with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Users**. The tab shows a list of users in your directory. 

1.  Select a user. You're directed to the **User details** screen. The **User details** screen shows the following information: 
   +  Groups the user is a member of (group memberships) 
   +  Profile details (such as primary information like user logon name, first name, last name, etc.) 
   +  Account settings (such as account information like user principal name, service principal name, distinguished name, etc.) 
   + Account status

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------
#### [ AWS CLI ]

 With the AWS CLI, you can view a user's details, which includes profile and account information and group memberships. 

**To view an AWS Managed Microsoft AD user's profile and account details with the AWS CLI**  
 The following describes how to view an AWS Managed Microsoft AD user's details with the AWS Directory Service Data CLI. 
+  To view a user's details, open the AWS CLI, and run the following command with your Directory ID and username: 

```
aws ds-data describe-user --directory-id {{d-1234567890}} --sam-account-name "{{jane.doe}}"
```

For more information, see [`describe-user`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/describe-user.html).

**To view a user's group memberships**  
 The following describes how to view an AWS Managed Microsoft AD user's group membership with the AWS Directory Service Data CLI. 
+  To view a user's group memberships, open the AWS CLI, and run the following command with your Directory ID and username: 

```
aws ds-data list-groups-for-member --directory-id {{d-1234567890}} --sam-account-name "{{jane.doe}}"
```

For more information, see [`list-groups-for-member`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/list-groups-for-member.html).

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------
#### [ PowerShell ]

 With Tools for PowerShell, you can view a user's details, which includes profile and account information and group memberships. 

**To view an AWS Managed Microsoft AD user's profile and account details with Tools for PowerShell**  
 The following describes how to view an AWS Managed Microsoft AD user's details with the Tools for PowerShell. 
+ To view a user's details, open PowerShell, and run the following command with your Directory ID and username: 

```
Get-DSDUser -DirectoryId {{d-1234567890}} -SAMAccountName "{{jane.doe}}"
```

For more information, see [`Get-DSDUser`](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-DSDUser.html).

**To view a user's group memberships**  
 The following describes how to view an AWS Managed Microsoft AD user's group membership with the Tools for PowerShell. 
+ To view a user's group memberships, open PowerShell, and run the following command with your Directory ID and username: 

```
(Get-DSDGroupsForMemberList -DirectoryId {{d-1234567890}} -SAMAccountName "{{jane.doe}}").Groups
```

For more information, see [`Get-DSDGroupsForMemberList`](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-DSDGroupsForMemberList.html).

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------

## Updating an AWS Managed Microsoft AD user's details
<a name="ms_ad_update_user"></a>

Use the following procedure to update an AWS Managed Microsoft AD user with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

**Note**  
The minimum attribute length is 1.

------
#### [ AWS Management Console ]

 You can update an AWS Managed Microsoft AD user's details in the AWS Management Console.

**To update an AWS Managed Microsoft AD user's details with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Users**. The tab shows a list of users in your directory. 

1.  Select a user. To find a user, enter the user logon name in the search box under the **Users** section. You're directed to the **User details** screen. 

1.  To edit groups the user is a member of, choose **Groups**. From this tab, you can add and remove the user from groups. For more information, see [Add an AWS Managed Microsoft AD member to a group](ms_ad_add_remove_user_group.md). 

1. To edit the user's profile details, choose **Profile**, and then choose **Edit**. Or choose **Actions**, and then choose **Edit user**. Make and review your updates, and then choose **Save**. 
**Warning**  
The user logon name cannot be changed after the user is created.

1.  To edit the user's account settings, choose **User account settings**. Or choose **Actions**, and then choose **Edit user**. Make and review your updates, and then choose **Save**. 

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------
#### [ AWS CLI ]

 The following describes how to format a request that updates an AWS Managed Microsoft AD user's details with AWS Directory Service Data CLI.

 When you update a user's account, you must include your directory ID number and user logon name. You also must include the update type and attribute you want to update in your request, such as a user last name with the `Surname` parameter. For more information, see [AWS Directory Service Data attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html). 
+  To update a user's details, open the AWS CLI, and run the following command with your Directory ID, username, update type, and attribute value: 

```
aws ds-data update-user \
  --directory-id {{d-1234567890}} \
  --sam-account-name "{{jane.doe}}" \
  --update-type "{{REPLACE}}" \
  --surname "{{Doe}}"
```

For more information, see [`update-user`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/update-user.html).

**Note**  
When removing user attributes with [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/update-user.html) CLI command, you must specify the attribute and the exact value to be removed. To determine user attributes, use [describe-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/describe-user.html) command.

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------
#### [ PowerShell ]

 The following describes how to format a request that updates an AWS Managed Microsoft AD user's details with AWS Tools for PowerShell.

 When you update a user's account, you must include your directory ID number and user logon name. You also must include the update type and attribute you want to update in your request, such as a user last name with the `Surname` parameter. For more information, see [AWS Directory Service Data attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html). 
+  To update a user's details, open PowerShell, and run the following command with your Directory ID, username, update type, and attribute value: 

```
Update-DSDUser `
    -DirectoryId {{d-1234567890}} `
    -SAMAccountName "{{jane.doe}}" `
    -UpdateType "{{REPLACE}}" `
    -Surname "{{Doe}}"
```

For more information, see [`Update-DSDUser`](https://docs.aws.amazon.com/powershell/latest/reference/items/Update-DSDUser.html).

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md) and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes).

------