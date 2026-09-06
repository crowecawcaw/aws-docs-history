

# Manage AWS Managed Microsoft AD users and groups with the AWS Management Console, AWS CLI, or AWS Tools for PowerShell
<a name="ms_ad_manage_users_groups_procedures"></a>

You can use the AWS Management Console, AWS CLI, or AWS Tools for PowerShell to manage your AWS Managed Microsoft AD users and groups with [AWS Directory Service Data](ms_ad_getting_started_directory_service_data.md). The AWS CLI commands use the `ds-data` namespace. The PowerShell commands use the `AWS.Tools.DirectoryServiceData` module. For more information, see [Getting started with AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [Getting started with AWS Tools for PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html).

See the following procedures for more information on creating, viewing, updating, and deleting AWS Managed Microsoft AD users and groups.

**Topics**
+ [Enabling or disabling user and group management or AWS Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md)
+ [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md)
+ [Viewing and updating an AWS Managed Microsoft AD user](ms_ad_view_update_user.md)
+ [Deleting an AWS Managed Microsoft AD user](ms_ad_delete_user.md)
+ [Disabling an AWS Managed Microsoft AD user](ms_ad_disable_user.md)
+ [Resetting and enabling an AWS Managed Microsoft AD user's password](ms_ad_reset_user_pswd.md)
+ [Creating an AWS Managed Microsoft AD group](ms_ad_create_group.md)
+ [Viewing and updating an AWS Managed Microsoft AD group's details](ms_ad_view_update_group.md)
+ [Deleting an AWS Managed Microsoft AD group](ms_ad_delete_group.md)
+ [Adding and removing AWS Managed Microsoft AD members to groups and groups to groups](ms_ad_add_remove_user_group.md)
+ [Copying an AWS Managed Microsoft AD group memberships in the AWS Management Console](copy_group_membership.md)

**AWS CloudShell**  
You can run the AWS CLI and PowerShell examples from [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/welcome.html), which comes with the [AWS CLI](https://aws.amazon.com/cli/), PowerShell, and [AWS.Tools for PowerShell](https://aws.amazon.com/powershell/) pre-installed, and credentials are automatically configured.

1. Sign in to the AWS Management Console.

1. Open [AWS CloudShell](https://console.aws.amazon.com/cloudshell/home). Run `pwsh` to use the PowerShell commands.