

# Creating OrganizationAccountAccessRole for an invited account with AWS Organizations
<a name="orgs_manage_accounts_create-cross-account-role"></a>

By default, if you create a member account as part of your organization, AWS automatically creates a role in the account that grants administrator permissions to IAM users in the management account who can assume the role. By default, that role is named `OrganizationAccountAccessRole`. For more information, see [Accessing a member account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md).

However, member accounts that you *invite* to join your organization ***do not*** automatically get an administrator role created. You have to do this manually, as shown in the following procedure. This essentially duplicates the role automatically set up for created accounts. We recommend that you use the same name, `OrganizationAccountAccessRole`, for your manually created roles for consistency and ease of remembering.

------
#### [ AWS Management Console ]

**To create an AWS Organizations administrator role in a member account**

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the member account. The user or role must have permission to create IAM roles and policies.

1. In the IAM console, navigate to **Roles** and then choose **Create role**.

1. Choose **AWS account**, and then select **Another AWS account**.

1. Enter the 12-digit account ID number of the management account that you want to grant administrator access to. Under **Options**, please note the following:
   + For this role, because the accounts are internal to your company, you should **not** choose **Require external ID**. For more information about the external ID option, see [When should I use an external ID?](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html#external-id-use) in the *IAM User Guide*. 
   + If you have MFA enabled and configured, you can optionally choose to require authentication using an MFA device. For more information about MFA, see [Using multi-factor authentication (MFA) in AWS](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) in the *IAM User Guide*. 

1. Choose **Next**.

1. On the **Add permissions** page, choose the AWS managed policy named `AdministratorAccess` and then choose **Next**.

1. On the **Name, review, and create** page, specify a role name and an optional description. We recommend that you use `OrganizationAccountAccessRole`, for consistency with the default name assigned to the role in new accounts. To commit your changes, choose **Create role**.

1. Your new role appears on the list of available roles. Choose the new role's name to view its details, paying special note to the link URL that is provided. Give this URL to users in the member account who need to access the role. Also, note the **Role ARN** because you need it in step 15.

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/). This time, sign in as a user in the management account who has permissions to create policies and assign the policies to users or groups.

1. Navigate to **Policies** and then choose **Create policy**.

1. For **Service**, choose **STS**.

1. For **Actions**, start typing **AssumeRole** in the **Filter** box and then select the check box next to it when it appears.

1. Under **Resources**, ensure that **Specific** is selected and then choose **Add ARNs**.

1. Enter the AWS member account ID number and then enter the name of the role that you previously created in steps 1–8. Choose **Add ARNs**.

1. If you're granting permission to assume the role in multiple member accounts, repeats steps 14 and 15 for each account.

1. Choose **Next**.

1. On the **Review and create** page, enter a name for the new policy and then choose **Create policy** to save your changes.

1. Choose **IAM user groups** in the navigation pane and then choose the name of the group (not the check box) that you want to use to delegate administration of the member account.

1. Choose the **Permissions** tab.

1. Choose **Add permissions**, choose **Attach policies**, and then select the policy that you created in steps 11–18.

------

The users who are members of the selected group now can use the URLs that you captured in step 9 to access each member account's role. They can access these member accounts the same way as they would if accessing an account that you create in the organization. For more information about using the role to administer a member account, see [Accessing a member account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md). 