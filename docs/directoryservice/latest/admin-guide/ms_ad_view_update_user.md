# Viewing and updating an AWS Managed Microsoft AD user

Use the following procedure to view or update an AWS Managed Microsoft AD user's details with
user and group management or AWS Directory Service Data in either the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

## Viewing an AWS Managed Microsoft AD user's details

You can view a user's details in the AWS Management Console or AWS CLI. The user's details
includes profile and account information and group membership.

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
You can view an AWS Managed Microsoft AD user's details in the AWS Management Console.

###### To view an AWS Managed Microsoft AD user's details and account details with the

AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Users**. The tab shows a list of users in your
   directory.
5. Select a user. You're directed to the **User details**
   screen. The **User details** screen shows the following
   information:
   - Groups the user is a member of (group memberships)
   - Profile details (such as primary information like user logon name, first
     name, last name, etc.)
   - Account settings (such as account information like user principal name,
     service principal name, distinguished name, etc.)
   - Account status

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

AWS CLI
With the AWS CLI, you can view a user's details, which includes profile and account
information and group memberships.

###### To view an AWS Managed Microsoft AD user's profile and account details with the

AWS CLI

The following describes how to view an AWS Managed Microsoft AD user's details with the
AWS Directory Service Data CLI.

- To view a user's details, open the AWS CLI, and run the following command,
  replacing the Directory ID and username with your AWS Managed Microsoft AD Directory ID and
  username:

```
aws ds-data describe-user --directory-id `d-1234567890` --sam-account-name "`jane.doe`"
```

###### To view a user's group memberships

The following describes how to view an AWS Managed Microsoft AD user's group membership
with the AWS Directory Service Data CLI.

- To view a user's group memberships, open the AWS CLI, and run the following
  command, replacing the Directory ID and username with your AWS Managed Microsoft AD Directory
  ID and username:

```
aws ds-data list-groups-for-member --directory-id `d-1234567890` --sam-account-name "`jane.doe`"
```

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

AWS Tools for PowerShell
With Tools for PowerShell, you can view a user's details, which includes profile and account
information and group memberships.

###### To view an AWS Managed Microsoft AD user's profile and account details with

Tools for PowerShell

The following describes how to view an AWS Managed Microsoft AD user's details with the
Tools for PowerShell.

- To view a user's details, open the PowerShell, and run the following
  command, replacing the Directory ID and username with your AWS Managed Microsoft AD Directory
  ID and username:

```
Get-DSDUser -DirectoryId `d-1234567890` -SAMAccountName "`jane.doe`"
```

###### To view a user's group memberships

The following describes how to view an AWS Managed Microsoft AD user's group membership
with the Tools for PowerShell.

- To view a user's group memberships, open the PowerShell, and run the
  following command, replacing the Directory ID and username with your AWS Managed Microsoft AD
  Directory ID and username:

```
(Get-DSDGroupsForMemberList -DirectoryId `d-1234567890` -SAMAccountName "`jane.doe`").Groups
```

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

## Updating an AWS Managed Microsoft AD user's details

Use the following procedure to update an AWS Managed Microsoft AD user with user and group management or
AWS Directory Service Data in either the AWS Management Console, AWS CLI, AWS Tools for PowerShell.

###### Note

The minimum attribute length is 1.

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
You can update an AWS Managed Microsoft AD user's details in the AWS Management Console.

###### To update an AWS Managed Microsoft AD user's details with the AWS Management Console

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. Choose **Users**. The tab shows a list of users in your
   directory.
5. Select a user. To find a user, enter the user logon name in the search box
   under the **Users** section. You're directed to the
   **User details** screen.
6. To edit groups the user is a member of, choose **Groups**.
   From this tab, you can add and remove the user from groups. For more information,
   see [Add an AWS Managed Microsoft AD member to a
   group](ms_ad_add_remove_user_group.md "ms_ad_add_remove_user_group.md").
7. To edit the user's profile details, choose **Profile**, and
   then choose **Edit**. Or choose **Actions**, and
   then choose **Edit user**. Make and review your updates, and then
   choose **Save**.

###### Warning

The user logon name cannot be changed after the user is created. 8. To edit the user's account settings, choose **User account
settings**. Or choose **Actions**, and then choose
**Edit user**. Make and review your updates, and then choose
**Save**.

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

AWS CLI
The following describes how to format a request that updates an AWS Managed Microsoft AD
user's details with AWS Directory Service Data CLI.

When you update a user's account, you must include your directory ID number and
user logon name. You also must include the update type and attribute you want to
update in your request, such as a user last name with the `Surname`
parameter. For more information, see [AWS Directory Service Data
attributes](ad_data_attributes.md "ad_data_attributes.md").

- To update a user's details, open the AWS CLI, and run the following command,
  replacing the Directory ID, username, user type, and attribute value with your
  AWS Managed Microsoft AD Directory ID, username, and desired user type and attribute value:

```
aws ds-data update-user --directory-id `d-1234567890` --sam-account-name "`jane.doe`" --update-type "`REPLACE`" --surname "`Doe`"
```

###### Note

When removing user attributes with [update-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/update-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/update-user.html") CLI command, you must specify the attribute and the exact
value to be removed. To determine user attributes, use [describe-user](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/describe-user.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/describe-user.html") command.

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

AWS Tools for PowerShell
The following describes how to format a request that updates an AWS Managed Microsoft AD
user's details with AWS Tools for PowerShell.

When you update a user's account, you must include your directory ID number and
user logon name. You also must include the update type and attribute you want to
update in your request, such as a user last name with the `Surname`
parameter. For more information, see [AWS Directory Service Data
attributes](ad_data_attributes.md "ad_data_attributes.md").

- To update a user's details, open the PowerShell, and run the
  following command, replacing the Directory ID, username, user type, and attribute
  value with your AWS Managed Microsoft AD Directory ID, username, and desired user type and
  attribute value:

```
Update-DSDUser -DirectoryId `d-1234567890` -SAMAccountName "`jane.doe`" -UpdateType "`REPLACE`" -Surname "`Doe`"
```

For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").
