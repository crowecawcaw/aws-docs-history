# Remove user and group access to an
 AWS account

Use this procedure to remove single sign-on access to an AWS account for one or
 more users and groups in your connected directory. Alternatively, you can use the
 [delete-account-assignment](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/delete-account-assignment.html "https://docs.aws.amazon.com/cli/latest/reference/sso-admin/delete-account-assignment.html") AWS CLI.

###### Note

When you need to deprovision IAM Identity Center users or groups, you should first [remove any assignments of permission
 sets](howtoremovepermissionset.md "howtoremovepermissionset.md") from your users and groups before deleting the users and
 groups.

###### To remove user and group access to an AWS account

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. In the navigation pane, under **Multi-account
 permissions**, choose
 **AWS accounts**.
3. On the **AWS accounts** page, a tree view list of your
 organization appears. Select the name of the AWS account that contains the
 users and groups for whom you want to remove single sign-on access.
4. On the **Overview** page for the AWS account, under
 **Assigned users and groups**, select the name of one
 or more users or groups, and choose **Remove
 access**.
5. In the **Remove access** dialog box, confirm that the
 names of the users or groups are correct, and choose **Remove
 access**.
