# Disassociating member accounts in Security Hub CSPM

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

An AWS Security Hub CSPM administrator account can disassociate a member
account to stop receiving and viewing findings from that account. You must disassociate
a member account before you can delete it.

When you disassociate a member account, it remains in your list of member accounts
with a status of **Removed (Disassociated)**. Your account is removed
from the administrator account information for the member account.

To resume receiving findings for the account, you can resend the invitation. To remove
the member account entirely, you can delete the member account.

Choose your preferred method, and follow the steps to disassociate a manually-invited member account from the administrator account.

Security Hub CSPM console

###### To disassociate a manually-invited member account

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the administrator account. 2. In the navigation pane, under **Settings**, choose **Configuration**. 3. In the **Accounts** section, select the accounts that you want to disassociate. 4. Choose **Actions**, and then choose
**Disassociate account**.

Security Hub CSPM API
**To disassociate a manually-invited member account**

Invoke the [`DisassociateMembers`](../../1.0/APIReference/API_DisassociateMembers.md "../../1.0/APIReference/API_DisassociateMembers.md") API from the administrator account. You must
provide the AWS account IDs of the member accounts that you want to disassociate. To
view a list of member accounts, use the [`ListMembers`](../../1.0/APIReference/API_ListMembers.md "../../1.0/APIReference/API_ListMembers.md") operation.

AWS CLI
**To disassociate a manually-invited member account**

Run the [`disassociate-members`](../../../cli/latest/reference/securityhub/disassociate-members.md "../../../cli/latest/reference/securityhub/disassociate-members.md") command from the administrator account. You must
provide the AWS account IDs of the member accounts that you want to disassociate. To
view a list of member accounts, run the [`list-members`](../../../cli/latest/reference/securityhub/list-members.md "../../../cli/latest/reference/securityhub/list-members.md") command.

```
aws securityhub disassociate-members --account-ids `<accountIds>`
```

**Example**

```
aws securityhub disassociate-members --account-ids "123456789111" "123456789222"
```
