

# Deleting an AWS Managed Microsoft AD user
<a name="ms_ad_delete_user"></a>

Use the following procedure to delete an AWS Managed Microsoft AD user with AWS Directory Service Data in the AWS Management Console, AWS CLI, or AWS Tools for PowerShell.

**Important**  
When you delete a user's account from a directory, all information about the user is removed, including any permissions the user has to access their account and applications. 

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ [Creating an AWS Managed Microsoft AD user](ms_ad_create_user.md).

------
#### [ AWS Management Console ]

 You can delete an AWS Managed Microsoft AD user account in the AWS Management Console. 

**To delete an AWS Managed Microsoft AD user account with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Users**. The tab shows a list of users in your directory. 

1.  Choose the user whose account you want to delete. To find a user, enter the user logon name in the search box under the **Users** section. You're directed to the **User details** screen. 

1.  Choose **Actions**. Then choose **Delete user account** and **Delete user account** again. 

------
#### [ AWS CLI ]

 The following describes how to format a request that deletes an AWS Managed Microsoft AD user's account with the AWS Directory Service Data CLI.

**To delete an AWS Managed Microsoft AD user account with AWS CLI**
+  Open the AWS CLI, and run the following command with your Directory ID and username: 

```
aws ds-data delete-user --directory-id {{d-1234567890}} --sam-account-name "{{jane.doe}}"
```

For more information, see [`delete-user`](https://docs.aws.amazon.com/cli/latest/reference/ds-data/delete-user.html).

------
#### [ PowerShell ]

 The following describes how to format a request that deletes an AWS Managed Microsoft AD user's account with AWS Tools for PowerShell.

**To delete an AWS Managed Microsoft AD user account with AWS Tools for PowerShell**
+  Open PowerShell, and run the following command with your Directory ID and username: 

```
Remove-DSDUser -DirectoryId {{d-1234567890}} -SAMAccountName "{{jane.doe}}"
```

For more information, see [`Remove-DSDUser`](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-DSDUser.html).

------