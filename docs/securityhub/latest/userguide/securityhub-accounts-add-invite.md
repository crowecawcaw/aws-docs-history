# Adding and inviting member accounts in Security Hub CSPM

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

Your account becomes the AWS Security Hub CSPM administrator for accounts that accept your
invitation to become a Security Hub CSPM member account.

When you accept an invitation from another account, your account becomes a member
account, and that account becomes your administrator.

If your account is an administrator account, you can't accept an invitation to become
a member account.

Adding a member account consists of the following steps:

1. The administrator account adds the member account to their list of member
   accounts.
2. The administrator account sends an invitation to the member account.
3. The member account accepts the invitation.

## Adding member accounts

From the Security Hub CSPM console, you can add accounts to your list of member accounts. In the Security Hub CSPM console, you
can select accounts individually, or upload a `.csv` file that
contains the account information.

For each account, you must provide the account ID and an email address. The email
address should be the email address to contact about security issues in the account.
It is not used to verify the account.

Choose your preferred method, and follow the steps to add member accounts.

Security Hub CSPM console

###### To add accounts to your list of member accounts

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the administrator account. 2. In the left pane, choose **Settings**. 3. On the **Settings** page, choose
**Accounts** and then choose **Add
accounts**. You can then either add accounts individually or
upload a `.csv` file containing the list of
accounts. 4. To select the accounts, do one of the following:

    * To add the accounts individually, under **Enter
     accounts**, enter the account ID and email address of
     the account to add, and then choose **Add**.


    Repeat this process for each account.
    * To use a comma-separated values (.csv) file to add multiple
     accounts, first create the file. The file must contain the account
     ID and email address for each account to add.


    In your `.csv` list, accounts must appear one
     per line. The first line of the `.csv` file must
     contain the header. In the header, the first column is
     `Account ID` and the second column is
     `Email`.


    Each subsequent line must contain a valid account ID and email
     address for the account to add.


    Here is an example of a `.csv` file when viewed
     in a text editor.



    ```
    Account ID,Email
    111111111111,user@example.com
    ```

    In a spreadsheet program, the fields appear in separate columns.
     The underlying format is still comma-separated. You must format the
     account IDs as non-decimal numbers. For example, the account ID
     444455556666 cannot be formatted as 444455556666.0. Also make sure
     that the number formatting does not remove any leading zeros from
     the account ID.


    To select the file, on the console, choose **Upload list
     (.csv)**. Then choose
     **Browse**.


    After you select the file, choose **Add
     accounts**.

5. After you finish adding accounts, under **Accounts to be
   added**, choose **Next**.

Security Hub CSPM API
**To add accounts to your list of member accounts**

Invoke the [`CreateMembers`](../../1.0/APIReference/API_CreateMembers.md "../../1.0/APIReference/API_CreateMembers.md") API from the administrator account. For each member
account to add, you must provide the AWS account ID.

AWS CLI
**To add accounts to your list of member accounts**

Run the [`create-members`](../../../cli/latest/reference/securityhub/create-members.md "../../../cli/latest/reference/securityhub/create-members.md") command from the administrator account. For each member
account to add, you must provide the AWS account ID.

```
aws securityhub create-members --account-details '[{"AccountId": "`<accountID1>`"}]'
```

**Example**

```
aws securityhub create-members --account-details '[{"AccountId": "123456789111"}, {"AccountId": "123456789222"}]'
```

## Inviting member accounts

After you add the member accounts, you send an invitation to the member account.
You can also resend an invitation to an account that you disassociated from the administrator.

Security Hub CSPM console

###### To invite prospective member accounts

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the administrator account. 2. In the navigation pane, choose **Settings**, and then
choose **Accounts**. 3. For the account to invite, choose **Invite** in the
**Status** column. 4. When prompted to confirm, choose **Invite**.

###### Note

To resend invitations to disassociated accounts, select each disassociated account on the **Accounts**
page. For **Actions**, choose **Resend
invitation**.

Security Hub CSPM API
**To invite prospective member accounts**

Invoke the [`InviteMembers`](../../1.0/APIReference/API_InviteMembers.md "../../1.0/APIReference/API_InviteMembers.md") API from the administrator account. For each account to
invite, you must provide the AWS account ID.

AWS CLI
**To invite prospective member accounts**

Run
the [`invite-members`](../../../cli/latest/reference/securityhub/invite-members.md "../../../cli/latest/reference/securityhub/invite-members.md") command from the administrator account. For each account to
invite, you must provide the AWS account ID.

```
aws securityhub invite-members --account-ids `<accountIDs>`
```

**Example**

```
aws securityhub invite-members --account-ids "123456789111" "123456789222"
```
