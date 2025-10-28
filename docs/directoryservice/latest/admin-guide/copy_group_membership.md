# Copying an AWS Managed Microsoft AD group memberships in the

AWS Management Console

You can copy group memberships from one AWS Managed Microsoft AD user into another user in the
AWS Management Console. Group memberships are the roles and permissions that a user inherits when you add
them to a group.

###### Before you begin this procedure, you need to complete the following:

- [Creating your AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
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
- [Create an AWS Managed Microsoft AD group](ms_ad_create_group.md "ms_ad_create_group.md").

###### To copy AWS Managed Microsoft AD group memberships with the AWS Management Console

1. Open the AWS Directory Service console at [https://console.aws.amazon.com/directoryservicev2/](https://console.aws.amazon.com/directoryservicev2/ "https://console.aws.amazon.com/directoryservicev2/").
2. From the navigation pane, choose **Active Directory**, and then
   choose **Directories**. You're directed to the
   **Directories** screen where you can view a list of directories in your
   AWS Region.
3. Choose a directory. You're directed to the **Directory details**
   screen.
4. Choose **Groups**. The tab shows a list of groups in your
   AWS Region.
5. Choose the user whose account you want to copy their group membership. To find a user,
   enter the user logon name in the search box under the **Users** section.
   You're directed to the **User details** screen.
6. Choose **Copy all group memberships**. You're directed to a
   procedure where you can specify which groups you want to copy.
   1. For **Verify groups to copy**, under **Groups to
      copy**, select the groups with roles and permissions you want to copy, and
      then choose **Next**.
   2. For **Select destination account**, under **Account
      type**, choose **Existing user account** to copy group
      memberships into an existing user account. Alternatively, choose **New user
      account** to create a new user and copy group memberships into the new user
      account. To find a group, enter the group's name in the search box under the
      **Selected groups** section.
      1. _(Optional)_ If you choose **Existing user
         account**, select destination accounts where you want to copy the roles
         and permissions into, and then choose **Next**.
      2. _(Optional)_ If you choose **New user
         account**, complete the procedure, and then choose
         **Next**. For information about creating a user, see [Creating a user](ms_ad_create_user.md "ms_ad_create_user.md").

   3. For **Review and copy group memberships**, review your choices,
      and then choose **Copy group membership**.
