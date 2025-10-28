# Creating an AWS Managed Microsoft AD user

Use the following procedure to create a new AWS Managed Microsoft AD user with user and group management or
AWS Directory Service Data in either the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

###### Before you begin either procedure, you need to complete the following:

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

AWS Management Console
You can create a new AWS Managed Microsoft AD user account in the AWS Management Console. When you create a
new user account, you specify the new user's details and determine whether to add the
new user to a group or copy another user's group memberships into the new user.

For more information, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md").

###### To create an AWS Managed Microsoft AD user with the AWS Management Console

1. Open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then choose
   **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories
   in your AWS Region.
3. Choose a directory. You're directed to the **Directory
   details** screen.
4. On the **Directory details** page, under the
   **Users** section, choose **Create users
   account**.
5. The **Specify user details** page opens. Under the
   **Required information** section, enter a user logon name and
   password. User logon names must meet the following conditions:
   - Must be a unique logon name
   - Can be up to 20 characters long
   - Can only contain alphanumeric characters
   - ~!@#$%^&\*\_-+=`|\(){}[]:;"'<>,.?/
   - The password must adhere to your password policy requirements. Check with
     your AWS administrator for more information.

###### Warning

The user logon name cannot be changed after the user is created.

    1. *(Optional)* Under the **Primary
     information** section, you can enter a first and last name for the
     user. You can also enter a display name and description for the user.
    2. *(Optional)* Under the **Contact
     methods** section, you can enter an email address and telephone
     numbers for the user.
    3. *(Optional)* Under the **Job-related
     information** section, you can enter a department, manager, office,
     and company for the user.
    4. *(Optional)* Under the **Address**
     section, you can enter an address for the user.
    5. *(Optional)* Under the **Account
     settings** section, you can enter notes, a preferred language, and
     service principal name for the user.


    For more information on user attributes, see [AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md")
    and [Microsoft documentation](https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes "https://learn.microsoft.com/en-us/windows/win32/ad/user-object-attributes").

6. Choose **Next** once you've provided the user account
   details.
7. On the **Add users to groups - _optional_**
   page, you can add the user to a new group or to an existing group. You can also copy
   the group membership of an existing user to the new user. If you don't want to add a
   user to a group, choose **Next**. Move to Step 12 to continue this
   procedure.
8. _(Optional)_ To create a new group, see [Create a AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").
9. _(Optional)_ To add a new user to an existing group:
   1. Select the group you want to add the new user to in the
      **Groups** section. To find groups, enter the group name in
      the search box.

10. _(Optional)_ To copy the group membership of an existing user
    to a new user:
    1. Choose the **Copy group membership from user** tab. To find
       a user with a group membership you want to copy, enter the user logon name in
       the search box under the **Users** section.
    2. In the **Selected groups** section, select the groups the
       new user should become a member of.

11. Choose **Next** when you're ready to create the new user
    account.
12. On the **Review and create user** page, review all the choices
    you made. Choose **Create user**.
13. After the user is configured, you've taken to the new user's details page. A
    banner appears stating the user was successfully created.

###### Important

If you receive an error message telling you that you don't have permission to
create a user, follow the instructions in the error message to request that your
administrator grant you access.

AWS CLI
The following describes how to format a request that creates a new AWS Managed Microsoft AD
user account with the AWS Directory Service Data CLI. You must include your directory ID number and a user
logon name in your request. You can also include other attributes, such as a user
display name with the `DisplayName` attribute. For more information, see
[AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md").

###### To create an AWS Managed Microsoft AD user with AWS CLI

- Open the AWS CLI, and run the following command, replacing the Directory ID,
  username, and display name with your AWS Managed Microsoft AD Directory ID and desired
  credentials:

```
aws ds-data create-user \
  --directory-id `d-1234567890` \
  --sam-account-name "`jane.doe`" \
  --other-attributes '{
    "DisplayName" : { "S": "`jane.doe`"},
    "Department":{ "S": "`Legal`"}
    }‘
```

AWS Tools for PowerShell
The following describes how to format a request that creates a new AWS Managed Microsoft AD
user account with AWS Tools for PowerShell. You must include your directory ID number and a user
logon name in your request. You can also include other attributes, such as a user
display name with the `DisplayName` attribute. For more information, see
[AWS Directory Service Data attributes](ad_data_attributes.md "ad_data_attributes.md") and [Group type and group scope](ad_group_type_and_scope.md "ad_group_type_and_scope.md").

###### To create an AWS Managed Microsoft AD user with Tools for PowerShell

- Open PowerShell, and run the following command, replacing the
  Directory ID, username, and display name with your AWS Managed Microsoft AD Directory ID and
  desired credentials:

```
New-DSDUser `
    -DirectoryId `d-1234567890` `
    -SAMAccountName "`jane.doe`" `
    -OtherAttribute @{
        DisplayName = [Amazon.DirectoryServiceData.Model.AttributeValue]@{S = '`jane.doe`' }
        Department = [Amazon.DirectoryServiceData.Model.AttributeValue]@{S = 'Legal' }
    }
```
