# Disassociating from a Security Hub CSPM administrator account

###### Note

We recommend using AWS Organizations instead of Security Hub CSPM invitations to manage your member accounts. For information, see
[Managing Security Hub CSPM for multiple accounts with
AWS Organizations](securityhub-accounts-orgs.md "securityhub-accounts-orgs.md").

If your account was added as an AWS Security Hub CSPM member account by invitation, you can disassociate the
member account from the administrator account. After you disassociate a member account,
Security Hub CSPM doesn't send findings from the account to the administrator account.

Member
accounts that are managed using the integration with AWS Organizations can't disassociate their accounts from the
administrator account. Only the Security Hub CSPM delegated administrator can disassociate member accounts that are managed
with Organizations.

When you disassociate from your administrator account, your account remains in the
administrator account's member list with a status of **Resigned**.
However, the administrator account does not receive any findings for your
account.

After you disassociate yourself from the administrator account, the invitation to be a member still remains. You can accept the
invitation again in the future.

Security Hub CSPM console

###### To disassociate from your administrator account

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").
2. In the navigation pane, choose **Settings**, and then
   choose **Accounts**.
3. In the **Administrator account** section, turn off
   **Accept**, and then choose
   **Update**.

Security Hub CSPM API
**To disassociate from your administrator account**

Invoke the [`DisassociateFromAdministratorAccount`](../../1.0/APIReference/API_DisassociateFromAdministratorAccount.md "../../1.0/APIReference/API_DisassociateFromAdministratorAccount.md") API.

AWS CLI
**To disassociate from your administrator account**

Run
the [`disassociate-from-administrator-account`](../../../cli/latest/reference/securityhub/disassociate-from-administrator-account.md "../../../cli/latest/reference/securityhub/disassociate-from-administrator-account.md")
command.

```
aws securityhub disassociate-from-administrator-account
```

###### Note

The Security Hub CSPM console continues to use `DisassociateFromMasterAccount`.
It will eventually change to use
`DisassociateFromAdministratorAccount`. Any IAM policies that
specifically control access to this function must continue to use
`DisassociateFromMasterAccount`. You should also add
`DisassociateFromAdministratorAccount` to your policies to ensure
that the correct permissions are in place after the console begins to use
`DisassociateFromAdministratorAccount`.
