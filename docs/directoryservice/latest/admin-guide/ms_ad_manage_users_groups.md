

# User and group management in AWS Managed Microsoft AD
<a name="ms_ad_manage_users_groups"></a>

 You can manage users and groups in AWS Managed Microsoft AD. You create a user to represent a person or entity that can access your directory. You can also create a group to grant and deny permissions to more than one user at a time. You can add not only users to a group, but also groups to a group. When you add a user to a group, the user inherits the roles and permissions assigned to the group. When you add a group to a group, the groups share a parent-child relationship, where the child group inherits the roles and permissions assigned to the parent group. You can also copy a user's group memberships into another user. 

You can manage users and groups with [AWS Directory Service Data](ms_ad_getting_started_directory_service_data.md) using the following methods:
+ [AWS Management Console](#ms_ad_manage_users_groups_with_console)
+ [AWS CLI](#ms_ad_manage_users_groups_console_cli)
+ [AWS Directory Service Data API](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html)
+ [AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/reference/items/DirectoryServiceData_cmdlets.html)

For a demonstration of the AWS Directory Service Data CLI, see the following YouTube video.

[![AWS Videos](http://img.youtube.com/vi/GJK567cuBu0?si=vb9KNV5JOWDXELSI/0.jpg)](http://www.youtube.com/watch?v=GJK567cuBu0?si=vb9KNV5JOWDXELSI)


Alternatively, you can use a [domain-joined instance](#ms_ad_manage_users_groups_with_instance).

## Manage users and groups with the AWS Management Console
<a name="ms_ad_manage_users_groups_with_console"></a>

 You can manage users and groups with the AWS Management Console with AWS Directory Service Data. Directory Service Data is an extension of Directory Service that provides you with the ability to perform built-in object management tasks. Some of these tasks include creating users and groups and adding users to groups as well as groups to a group.

For more information, see [Manage AWS Managed Microsoft AD users and groups with the AWS Management Console](ms_ad_manage_users_groups_procedures.md).

**Note**  
To use this feature, it must be enabled. For more information, see [Enable user and group management](ms_ad_users_groups_mgmt_enable_disable.md).  
 You can only manage users and groups with the AWS Management Console from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).  
You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).

## Manage users and groups with the AWS CLI
<a name="ms_ad_manage_users_groups_console_cli"></a>

 You can manage users and groups with the AWS CLI through the [AWS Directory Service Data API](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html). Directory Service Data is an extension of Directory Service that provides you with the ability to perform built-in object management tasks using the `ds-data` namespace. Some of these tasks include creating users and groups and adding users to groups as well as groups to a group.

**Create a user with AWS Directory Service Data CLI**  
 The following is an example AWS CLI command that uses the `ds-data` namespace to create a user. 

```
aws ds-data create-user --directory-id {{d-1234567890}} --sam-account-name {{"jane.doe"}} --region {{your-Primary-Region-name}}
```

**Note**  
To use this AWS CLI, it must be enabled. For more information, see [Enabling or disabling user and group management or AWS Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md).  
 You can only manage users and groups with the AWS Directory Service Data CLI from the primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).  
You'll need the necessary IAM permissions to use AWS Directory Service Data. For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md). To get started granting permissions to your users and workloads, you can use AWS managed policies like. [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies)

For more information, see [Manage AWS Managed Microsoft AD users and groups with the AWS CLI](ms_ad_manage_users_groups_procedures.md).

## Manage users and groups with AWS Tools for PowerShell
<a name="ms_ad_manage_users_groups_pwershell"></a>

The [AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-welcome.html) provides two separate modules for managing AWS Directory Service: `AWS.Tools.DirectoryService` (DS) and `AWS.Tools.DirectoryServiceData` (DSD). When working with AWS Directory Service, ensure you're using the appropriate module for your intended operation.
+ The `DirectoryService` module contains cmdlets for managing directory service configuration and administration, including cmdlets like `Enable-DSDirectoryDataAccess`, `Disable-DSDirectoryDataAccess`, and `Reset-DSUserPassword`.
+ The `DirectoryServiceData` module contains cmdlets for performing operations within a directory, specifically focused on user and group management. These DSD cmdlets include user management operations (`New-DSDUser`, `Get-DSDUser`, `Update-DSDUser`, and `Remove-DSDUser`), group management operations (`New-DSDGroup`, `Get-DSDGroup`, and `Update-DSDGroup`, `Remove-DSDGroup`), group membership management (`Add-DSDGroupMember`, and `Remove-DSDGroupMember`), and search functionality (`Search-DSDUser` and `Search-DSDGroup`).

## Manage users and groups with an on-premise instance or Amazon EC2 instance
<a name="ms_ad_manage_users_groups_with_instance"></a>

 If the AWS Directory Service Data doesn't support your use case, we recommend managing users and groups with an on-premise or EC2 instance.

To create users and groups in an AWS Managed Microsoft AD, you can use any instance (from either on-premises or EC2) that has been joined to your AWS Managed Microsoft AD. You need to be logged in as a user that has privileges to create users and groups. You will also need to install the Active Directory Tools on your instance so you can add your users and groups with the Active Directory Users and Computers tool.
+ You can deploy a pre-configured EC2 instance with preinstalled Active Directory administrative tools from Directory Service management console. For more information, see [Launching a directory administration instance in your AWS Managed Microsoft AD Active Directory](console_instance.md).
+ If you need to deploy a self-managed EC2 instance with administrative tools and install the necessary tools, see [Step 3: Deploy an Amazon EC2 instance to manage your AWS Managed Microsoft AD Active Directory](microsoftadbasestep3.md).

**Topics**
+ [Manage users and groups with the AWS Management Console](#ms_ad_manage_users_groups_with_console)
+ [Manage users and groups with the AWS CLI](#ms_ad_manage_users_groups_console_cli)
+ [Manage users and groups with AWS Tools for PowerShell](#ms_ad_manage_users_groups_pwershell)
+ [Manage users and groups with an on-premise instance or Amazon EC2 instance](#ms_ad_manage_users_groups_with_instance)
+ [Manage AWS Managed Microsoft AD users and groups with the AWS Management Console, AWS CLI, or AWS Tools for PowerShell](ms_ad_manage_users_groups_procedures.md)
+ [Manage users and groups with an Amazon EC2 instance](ms_ad_manage_users_groups_ec2.md)