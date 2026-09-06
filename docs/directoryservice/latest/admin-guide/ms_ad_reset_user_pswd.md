

# Resetting and enabling an AWS Managed Microsoft AD user's password
<a name="ms_ad_reset_user_pswd"></a>

Use the following procedure to reset an AWS Managed Microsoft AD user's password to enable their account with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md).

------
#### [ AWS Management Console ]

 You can reset an AWS Managed Microsoft AD user's password to enable their account in the AWS Management Console. You can perform this task from either the **Directories** screen or **Directory details** screen.

**Directories**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose **Actions**, and then choose **Reset user password and enable account**. 

   1.  Under **User logon name**, enter the user logon name for the user whose password you want to reset. 

   1.  Under **New password**, enter the user's new password. 

   1.  Under **Confirm password**, enter user's new password again. 

1.  After you confirm the user's new password, choose **Reset password and enable account**. 

**Directory details**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Users**. The tab shows a list of users in your directory. 

1.  Select the user whose password you want to reset. 

1.  Choose **Actions**, and then choose **Reset user password and enable account**. 

   1.  Under **New password**, enter the user's new password. 

   1.  Under **Confirm password**, enter user's new password again. 

1.  After you confirm the user's new password, choose **Reset password and enable account**. 

------
#### [ AWS CLI ]

 You can reset an AWS Managed Microsoft AD user's password to enable their account with the AWS Directory Service Data CLI.

**Note**  
This command uses the [`aws ds`](https://docs.aws.amazon.com/cli/latest/reference/ds/) namespace.

**To reset an AWS Managed Microsoft AD user's password with the AWS CLI**
+  To reset a user's password, open the AWS CLI, and run the following command with your Directory ID, username, and password: 

```
aws ds reset-user-password \
  --directory-id {{d-1234567890}} \
  --user-name "{{jane.doe}}" \
  --new-password "{{your-password}}"
```

For more information, see [`reset-user-password`](https://docs.aws.amazon.com/cli/latest/reference/ds/reset-user-password.html).

------
#### [ PowerShell ]

 You can reset an AWS Managed Microsoft AD user's password to enable their account with AWS Tools for PowerShell.

**Note**  
This command uses the [`AWS.Tools.DirectoryService`](https://docs.aws.amazon.com/powershell/latest/reference/items/DirectoryService_cmdlets.html) module.

**To reset an AWS Managed Microsoft AD user's password with AWS Tools for PowerShell**
+  To reset a user's password, open PowerShell, and run the following command with your Directory ID, username, and password: 

```
Reset-DSUserPassword `
    -DirectoryId {{d-1234567890}} `
    -UserName "{{jane.doe}}" `
    -NewPassword "{{your-password}}"
```

For more information, see [`Reset-DSUserPassword`](https://docs.aws.amazon.com/powershell/latest/reference/items/Reset-DSUserPassword.html).

------