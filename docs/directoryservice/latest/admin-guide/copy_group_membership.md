

# Copying an AWS Managed Microsoft AD group memberships in the AWS Management Console
<a name="copy_group_membership"></a>

 You can copy group memberships from one AWS Managed Microsoft AD user into another user in the AWS Management Console. Group memberships are the roles and permissions that a user inherits when you add them to a group. 

**Before you begin, complete the following:**
+ [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory).
+ Enable [user and group management for Directory Service Data](ms_ad_users_groups_mgmt_enable_disable.md). You can only enable this feature from the Primary AWS Region for your directory. For more information, see [Primary vs additional Regions](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/multi-region-global-primary-additional.html).
+ You'll need the necessary IAM permissions to use AWS Directory Service Data. To get started, you can use the [AWS managed policy: AWSDirectoryServiceDataFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataFullAccess) or [AWS managed policy: AWSDirectoryServiceDataReadOnlyAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSDirectoryServiceDataReadOnlyAccess). For more information, see [Directory Service API permissions: Actions, resources, and conditions reference](UsingWithDS_IAM_ResourcePermissions.md) and [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-use-aws-defined-policies).
+ [Create an AWS Managed Microsoft AD group](ms_ad_create_group.md).

**To copy AWS Managed Microsoft AD group memberships with the AWS Management Console**

1. Open the Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/).

1.  From the navigation pane, choose **Active Directory**, and then choose **Directories**. You're directed to the **Directories** screen where you can view a list of directories in your AWS Region. 

1.  Choose a directory. You're directed to the **Directory details** screen. 

1.  Choose **Groups**. The tab shows a list of groups in your AWS Region. 

1. Choose the user whose account you want to copy their group membership. To find a user, enter the user logon name in the search box under the **Users** section. You're directed to the **User details** screen.

1.  Choose **Copy all group memberships**. You're directed to a procedure where you can specify which groups you want to copy. 

   1.  For **Verify groups to copy**, under **Groups to copy**, select the groups with roles and permissions you want to copy, and then choose **Next**. 

   1.  For **Select destination account**, under **Account type**, choose **Existing user account** to copy group memberships into an existing user account. Alternatively, choose **New user account** to create a new user and copy group memberships into the new user account. To find a group, enter the group's name in the search box under the **Selected groups** section. 

      1. *(Optional)* If you choose **Existing user account**, select destination accounts where you want to copy the roles and permissions into, and then choose **Next**. 

      1. *(Optional)* If you choose **New user account**, complete the procedure, and then choose **Next**. For information about creating a user, see [Creating a user](ms_ad_create_user.md). 

   1.  For **Review and copy group memberships**, review your choices, and then choose **Copy group membership**. 