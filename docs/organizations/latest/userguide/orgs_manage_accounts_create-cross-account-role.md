# Creating

OrganizationAccountAccessRole for an invited account with AWS Organizations

By default, if you create a member account as part of your organization, AWS
automatically creates a role in the account that grants administrator permissions to
IAM users in the management account who can assume the role. By default, that role is
named `OrganizationAccountAccessRole`. For more information, see [Accessing a member
account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md").

However, member accounts that you _invite_ to join
your organization **_do
not_** automatically get an administrator role created. You have
to do this manually, as shown in the following procedure. This essentially duplicates
the role automatically set up for created accounts. We recommend that you use the same
name, `OrganizationAccountAccessRole`, for your manually created roles for
consistency and ease of remembering.

AWS Management Console

###### To create an AWS Organizations administrator role in a member account

1. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). You must sign
   in as an IAM user, assume an IAM role, or sign in as the root
   user ([not recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the member account. The user or
   role must have permission to create IAM roles and policies.
2. In the IAM console, navigate to **Roles** and then choose **Create
   role**.
3. Choose **AWS account**, and then select
   **Another AWS account**.
4. Enter the 12-digit account ID number of the management account
   that you want to grant administrator access to. Under
   **Options**, please note the following:
   - For this role, because the accounts are internal to your
     company, you should **not**
     choose **Require external ID**. For more
     information about the external ID option, see [When should I use an external ID?](../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md#external-id-use "../../../IAM/latest/UserGuide/id_roles_create_for-user_externalid.md#external-id-use") in the
     _IAM User Guide_.
   - If you have MFA enabled and configured, you can optionally
     choose to require authentication using an MFA device. For
     more information about MFA, see [Using
     multi-factor authentication (MFA) in AWS](../../../IAM/latest/UserGuide/id_credentials_mfa.md "../../../IAM/latest/UserGuide/id_credentials_mfa.md") in
     the _IAM User Guide_.

5. Choose **Next**.
6. On the **Add permissions** page, choose the AWS
   managed policy named `AdministratorAccess` and then
   choose **Next**.
7. On the **Name, review, and create** page, specify
   a role name and an optional description. We recommend that you use
   `OrganizationAccountAccessRole`, for consistency with
   the default name assigned to the role in new accounts. To commit
   your changes, choose **Create role**.
8. Your new role appears on the list of available roles. Choose the
   new role's name to view its details, paying special note to the link
   URL that is provided. Give this URL to users in the member account
   who need to access the role. Also, note the **Role
   ARN** because you need it in step 15.
9. Sign in to the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). This time, sign
   in as a user in the management account who has permissions to create
   policies and assign the policies to users or groups.
10. Navigate to **Policies** and then choose
    **Create policy**.
11. For **Service**, choose
    **STS**.
12. For **Actions**, start typing
    `AssumeRole` in the
    **Filter** box and then select the check box
    next to it when it appears.
13. Under **Resources**, ensure that
    **Specific** is selected and then choose
    **Add ARNs**.
14. Enter the AWS member account ID number and then enter the name
    of the role that you previously created in steps 1–8. Choose
    **Add ARNs**.
15. If you're granting permission to assume the role in multiple
    member accounts, repeats steps 14 and 15 for each account.
16. Choose **Next**.
17. On the **Review and create** page, enter a name
    for the new policy and then choose **Create
    policy** to save your changes.
18. Choose **User groups** in the
    navigation pane and then choose the name of the group (not the check
    box) that you want to use to delegate administration of the member
    account.
19. Choose the **Permissions** tab.
20. Choose **Add permissions**, choose
    **Attach policies**, and then select the policy
    that you created in steps 11–18.

The users who are members of the selected group now can use the URLs that you captured
in step 9 to access each member account's role. They can access these member accounts
the same way as they would if accessing an account that you create in the organization.
For more information about using the role to administer a member account, see [Accessing a member
account that has OrganizationAccountAccessRole with AWS Organizations](orgs_manage_accounts_access-cross-account-role.md "orgs_manage_accounts_access-cross-account-role.md").
