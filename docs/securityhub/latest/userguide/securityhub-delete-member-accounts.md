# Deleting member accounts in Security Hub CSPM

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

As an AWS Security Hub CSPM administrator account, you can delete member accounts that were added by
invitation. Before you can delete an enabled account, you must disassociate it.

When you delete a member account, it is completely removed from the list. To restore
the account's membership, you must add and invite it again as if it were a completely new
member account.

You can't delete accounts that belong to an organization and that are managed using the integration with AWS Organizations.

Choose your preferred method, and follow the steps to delete manually-invited member accounts.

Security Hub CSPM console

###### To delete a manually-invited member account

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the administrator account. 2. In the navigation pane, choose **Settings**, and then
choose **Configuration**. 3. Choose the **Invitation accounts** tab. Then, select the accounts to
delete. 4. Choose **Actions**, and then choose **Delete**. This option is available only if you have disassociated the account. You
must disassociate a member account before it can be deleted.

Security Hub CSPM API
**To delete a manually-invited member account**

Invoke the [`DeleteMembers`](../../1.0/APIReference/API_DeleteMembers.md "../../1.0/APIReference/API_DeleteMembers.md") API from the administrator account. You must provide the
AWS account IDs of the member accounts that you want to delete. To retrieve the list of
member accounts, invoke the [`ListMembers`](../../1.0/APIReference/API_ListMembers.md "../../1.0/APIReference/API_ListMembers.md") API.

AWS CLI
**To delete a manually-invited member account**

Run
the [`delete-members`](../../../cli/latest/reference/securityhub/delete-members.md "../../../cli/latest/reference/securityhub/delete-members.md") command from the administrator account. You must provide the
AWS account IDs of the member accounts that you want to delete. To retrieve the list of
member accounts, run the [`list-members`](../../../cli/latest/reference/securityhub/list-members.md "../../../cli/latest/reference/securityhub/list-members.md") command.

```
aws securityhub delete-members --account-ids `<memberAccountIDs>`
```

**Example**

```
aws securityhub delete-members --account-ids "123456789111" "123456789222"
```
