

# Manage workforce members
<a name="manage-workforce-members"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

After you've activated advanced features, you can invite new workforce members or remove existing workforce members. This includes adding your existing workforce to new AWS accounts. The following information is only for AWS organizations that use AWS Builder ID as the identity source. If you use an external identity provider (IdP), you manage your workforce in those identity providers. If you use Identity Center directory, use the documentation described in [Manage users in the Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

## To invite new workforce members
<a name="invite-new-workforce-members"></a>

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. Visit the AWS console for your identity delegated admin account.

1. From AWS console home, search for **IAM Identity Center** and choose it.

1. On the **Users** page of the IAM Identity Center console, choose **Invite new team member**.

1. For **Email**, enter an email address or a list of email addresses. Separate the email addresses with commas (,) or semicolons (;).

1. Choose **Send invitation**.

## To grant a new workforce member access to AWS accounts
<a name="grant-workforce-member-access"></a>

After the workforce member accepts their invitation, you configure which AWS accounts they have access to.

### Grant full permissions to an account you created before activating advanced features
<a name="grant-full-permissions"></a>

1. Identify the account ID of the account to which you want to grant access. To find the account ID, see [View AWS account identifiers](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html).

1. In the main navigation pane, choose **Groups**.

1. Select the group name that begins with the account ID you identified.

1. Choose **Add users to group**.

1. Select the user you want to add.

1. Choose **Add 1 user**.

### Grant custom permissions to a new or existing AWS account
<a name="grant-custom-permissions"></a>

You configure custom access in AWS Account Access Manager. For more information, see [Manage access to AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/aam-manage-access-to-aws-accounts.html).

**Note**  
If you want to create custom roles and grant access to them from AWS Settings, you must set the session length to 12 hours.

## To remove workforce members
<a name="remove-workforce-members"></a>

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. For **Actions**, choose **Manage team**.

   This will open the IAM Identity Center.

1. On the **Users** page of the IAM Identity Center console, select a team member, and then choose **Remove**.

1. Confirm your choice and choose **Remove**.

The team member will immediately lose all access to your AWS organization.

These steps show you how to manage your workforce members by first accessing AWS Settings. However, you can sign into the AWS Management Console with your delegate admin account and access the IAM Identity Center or the IAM console to manage your workforce members.