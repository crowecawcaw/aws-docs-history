# Closing a management account in your

organization

To close the management account in your organization, you must first either [close](orgs_manage_accounts_close.md "orgs_manage_accounts_close.md") or [remove](orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account "orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account") all member accounts
in the organization. The act of closing the management account also deletes the instance of
AWS Organizations and any policies that you created inside of that organization after the [post-closure period](../../../accounts/latest/reference/manage-acct-closing.md#post-closure-period "../../../accounts/latest/reference/manage-acct-closing.md#post-closure-period") has expired.

## Close the management account

Use the following procedure to close a management account.

###### Important

Before you close your management account, we highly recommend that you review
considerations and understand the impact for closing an account. For more
information, see [What you need to know before closing your account](../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations "../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations") and [What to expect after you close your account](../../../accounts/latest/reference/manage-acct-closing.md#what-to-expect-after-closure "../../../accounts/latest/reference/manage-acct-closing.md#what-to-expect-after-closure") in the _AWS
Account Management Guide_.

AWS Management Console

###### To close a management account from the Accounts page

###### Note

You cannot close a management account directly from the AWS Organizations
console.

1. [Sign in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") for the
   management account that you want to close. You can't close an
   account while signed in as an IAM user or role.
2. Verify that there are no active member accounts remaining in your
   organization. To do this, go to the [AWS Organizations
   console](https://console.aws.amazon.com/organizations "https://console.aws.amazon.com/organizations"). If you have a member account that is still
   active, you will need to follow the guidance provided in [Closing a member account in an
   organization with AWS Organizations](orgs_manage_accounts_close.md "orgs_manage_accounts_close.md") or [Remove a member account
   from an organization](orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account "orgs_manage_accounts_remove.md#orgs_manage_accounts_remove-member-account") before you can move
   to the next step.
3. On the navigation bar in the upper-right corner, choose your
   account name or number, and then choose
   **Account**.
4. On the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account"), choose the
   **Close account** button. Read and ensure that
   you understand the account closure guidance.
5. Choose the **Close account** button to initiate
   the account closure process.
6. Within a few minutes, you should receive an email confirmation
   that your account has been closed.

AWS CLI & AWS SDKsThis task isn't supported in the AWS CLI or by an API operation from
one of the AWS SDKs. You can perform this task only by using the AWS Management Console.
