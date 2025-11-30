# Closing a member account in an

organization with AWS Organizations

If you no longer need a member account in your organization, you can close it from the
[AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2") following the instructions in this topic. You can only close a member
account using the AWS Organizations console if your organization is in [All features](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all") mode.

You can also close an AWS account directly from the [**Account** page](https://console.aws.amazon.com/billing/home#/account "https://console.aws.amazon.com/billing/home#/account") in
the AWS Management Console after signing in as the root user. For step-by-step instructions, see [Close an
AWS account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the _AWS Account Management Guide_.

To close a management account, see [Closing a management account in your
organization](orgs_manage_accounts_close_management.md "orgs_manage_accounts_close_management.md").

## Close a member account

When you sign in to the organization's management account, you can close member
accounts that are part of your organization. To do this, complete the following
steps.

###### Important

Before you close your member account, we highly recommend that you review
considerations and understand the impact for closing an account. For more
information, see [What you need to know before closing your account](../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations "../../../accounts/latest/reference/manage-acct-closing.md#close-account-considerations") and [What to expect after you close your account](../../../accounts/latest/reference/manage-acct-closing.md#what-to-expect-after-closure "../../../accounts/latest/reference/manage-acct-closing.md#what-to-expect-after-closure") in the _AWS
Account Management Guide_.

AWS Management Console

###### To close a member account from the AWS Organizations console

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2 "https://console.aws.amazon.com/organizations/v2"). You must sign in as an IAM user, or
   sign in as the root user ([not
   recommended](../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials "../../../IAM/latest/UserGuide/best-practices.md#lock-away-credentials")) in the organization’s management
   account.
2. On the **[AWS accounts](https://console.aws.amazon.com/organizations/v2/home/accounts "https://console.aws.amazon.com/organizations/v2/home/accounts")** page, find and choose the name of the member
   account you want to close. You can navigate the OU hierarchy, or
   look at a flat list of accounts without the OU structure.
3. Choose **Close** next to the account name at the
   top of the page. This option is only available when an AWS
   organization is in [All features](orgs_getting-started_concepts.md#feature-set-all "orgs_getting-started_concepts.md#feature-set-all") mode.

###### Note

If your organization is using [Consolidated billing](orgs_getting-started_concepts.md#feature-set-cb-only "orgs_getting-started_concepts.md#feature-set-cb-only") mode, you won't be able to see
the **Close** button in the console. To close
an account in consolidated billing mode, sign in to the account
you want to close as the root user. On the
**Accounts** page, choose the
**Close account** button, enter your
account ID, and then choose the **Close
account** button. 4. Read and ensure that you understand the account closure guidance. 5. Enter the member account ID, and then choose **Close
account**.

###### Note

Any member account that you close will display a
`CLOSED` label next to its account name in the
AWS Organizations console for up to 90 days after the original closure date.
After 90 days, the member account will be permanently closed and will no longer be displayed in the AWS Organizations console. Please note that it may take a few days for the account to be removed from the organization after permanent closure.

**To close a member account from the Accounts
page**

Optionally, you can close an AWS member account directly from the
**Accounts** page in the AWS Management Console. For step-by-step
guidance, follow the instructions in [Close an
AWS account](../../../accounts/latest/reference/manage-acct-closing.md "../../../accounts/latest/reference/manage-acct-closing.md") in the _AWS Account Management
Guide_.

AWS CLI & AWS SDKs

###### To close an AWS account

You can use one of the following commands to close an AWS
account:

- AWS CLI: [close-account](../../../cli/latest/reference/organizations/close-account.md "../../../cli/latest/reference/organizations/close-account.md")

```
`$` **aws organizations close-account \
 --account-id 123456789012**
```

This command produces no output when successful.

- AWS SDKs: [CloseAccount](../APIReference/API_CloseAccount.md "../APIReference/API_CloseAccount.md")
