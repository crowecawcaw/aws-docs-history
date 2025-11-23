# Removing the delegated administrator in Amazon Inspector

You might need to remove the Amazon Inspector delegated administrator account.
You can do this from the AWS Organizations management account.
When you remove the Amazon Inspector delegated administrator account, Amazon Inspector is still activated in the account and in all of its member accounts.
The delegated administrator account and all of its member accounts become standalone accounts and retain their original scan settings.

###### Note

If AWS Organizations policies are managing Amazon Inspector enablement, removing the delegated administrator does not affect policy enforcement.
Accounts will remain enabled according to the organization policy settings, though member account findings will no longer be visible in a central delegated administrator console until a new delegated administrator is designated.

This section describes how to remove the delegated administrator account.

## Remove the Amazon Inspector delegated administrator

The following procedures describe how to remove the Amazon Inspector delegated administrator and how to associate member accounts from the delegated administrator account.

For information about how to assign an Amazon Inspector delegated admninistrator, see [Designating a delegated administrator account for Amazon Inspector](designating-admin.md "designating-admin.md").

###### Note

After you assign an Amazon Inspector delegated administrator, the Amazon Inspector delegated administrator must associate member accounts manually.

###### To remove the delegated administrator

1. Sign in to the AWS Management Console using the AWS Organizations management account.
2. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
3. Use the region selector to choose the AWS Region where you want to remove the delegated administrator.
4. From the navigation pane, choose **General settings**.
5. Under **Delegated administrator**, choose **Remove**, and then confirm your action.

###### To associate members with a new delegated administrator

1. Sign in using the delegated administrator account credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Use the region selector to choose the AWS Region where you want to associate members.
3. From the navigation pane, choose **Account management**.
4. Under **Organization**, select the box next to **Account number**.
5. Choose **Actions**, and then choose **Add member**.
