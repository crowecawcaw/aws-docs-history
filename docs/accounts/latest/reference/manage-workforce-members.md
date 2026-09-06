

# Manage workforce members
<a name="manage-workforce-members"></a>

**Warning**  
We're currently releasing our new experience to a limited number of customers. You might not be able to access this experience yet.

After you've activated advanced features, you can invite new workforce members or remove existing workforce members. This includes adding your existing workforce to new AWS accounts. The following information is only for AWS organizations that use AWS Builder ID as the identity source. If you use an external identity provider (IdP), you manage your workforce in those identity providers. If you use Identity Center directory, use the documentation described in [Manage your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-sso.html).

**To invite new workforce members**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. For **Actions**, choose **Manage team**.

   This will open the IAM Identity Center. This is a task that requires root-level permission.

1. On the **Users** page of the IAM Identity Center console, choose **Invite new team member**.

1. For **Email**, enter an email address or a list of email addresses. Separate the email addresses with commas (,) or semicolons (;).

1. Choose **Send invitation**.

After the workforce member accepts their invitation, you configure which AWS accounts they have access to in AWS Account Access Manager. For more information, see [Manage access to AWS accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/aam-manage-access-to-aws-accounts.html).

**To remove workforce members**

1. Open AWS Settings at [https://settings.aws.com](https://settings.aws.com).

1. In the main navigation pane, choose **Projects**.

1. For **Actions**, choose **Manage team**.

   This will open the IAM Identity Center. This is a task that requires root-level permission.

1. On the **Users** page of the IAM Identity Center console, select a team member, and then choose **Remove**.

1. Confirm your choice and choose **Remove**.

The team member will immediately lose all access to your AWS organization.

These steps show you how to manage your workforce members by first accessing AWS Settings. However, you can sign into the AWS Management Console with your delegate admin account and access the IAM Identity Center or the IAM console to manage your workforce members.