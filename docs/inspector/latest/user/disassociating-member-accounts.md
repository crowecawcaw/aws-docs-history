# Disassociating member accounts in Amazon Inspector

As the delegated administrator, you might need to disassociate a member account from your account.
When you disassociate a member account, Amazon Inspector is still activated in the account, and the account becomes a standalone account.
You also don't have permission to manage Amazon Inspector for the account anymore.
However, you can associate previously disassociated member accounts with your account at any time.
This section describes how to disassociate member accounts as the delegated administrator.

###### Note

To disassociate policy-managed accounts, there should be no Amazon Inspector organization policy attached to that account for the scan type.

Console

###### To disassociate member accounts using the console

1. Sign in using the delegated administrator account credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home")
2. Use the region selector to choose the AWS Region where you want to disassociate member accounts.
3. From the navigation pane, choose **Account management**.
4. Under **Organization**, select the box next to each account number you want to disassociate.
5. Choose **Actions** menu, and then choose **Disassociate account**.

API
**To disassociate member
accounts using the API**

Run the [DisassociateMember](../../v2/APIReference/API_DisassociateMember.md "../../v2/APIReference/API_DisassociateMember.md") API
operation. In the request, provide the account IDs you're
disassociating.
