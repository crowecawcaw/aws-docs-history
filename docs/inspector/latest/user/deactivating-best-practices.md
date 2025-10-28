# Deactivating Amazon Inspector

You can deactivate Amazon Inspector in the Amazon Inspector console or with the Amazon Inspector API.
If you deactivate all scan types for an account;, Amazon Inspector is deactivated for that account automatically.

If you deactivate Amazon Inspector for an account, all scan types are deactivated for that account.
Additionally, all Amazon Inspector scan settings, inclduing filters, suppression rules, and findings are deleted for the account.

When you deactivate Amazon Inspector Amazon EC2 scanning,Amazon Inspector deletes the following SSM associations:

- `InspectorDistributor-do-not-delete`
- `InspectorInventoryCollection-do-not-delete`
- `InvokeInspectorSsmPlugin-do-not-delete`.
  Additionally, the Amazon Inspector SSM plugin installed through this association is removed from all of your Windows hosts.
  For more information, see [Scanning Windows EC2 instance](windows-scanning.md "windows-scanning.md").

###### Note

Once you deactivate Amazon Inspector, you no longer incur service charges.
However, you can reactivate Amazon Inspector at any time.

For information about how to deactivate scan types for different resources, see [Deactivating a scan type](deactivate-scans.md "deactivate-scans.md").

###### Prerequisites

Depending on the account type, consider the following:

- If your account is a standalone Amazon Inspector account, you can deactivate Amazon Inspector at any time.
- If your account is a member account in a multi-account environment, you cannot deactivate Amazon Inspector.
  You must contact the delegated administrator for your organization to deactivate Amazon Inspector.
- If you're the delegated administrator for an organization, you must [disassociate all of your member accounts](disassociating-member-accounts.md "disassociating-member-accounts.md") before you deactivate Amazon Inspector.

###### Note

When you deactivate Amazon Inspector as the delegated administrator, you deactivate the auto-activate feature for your organization.

## Deactivate Amazon Inspector

###### Note

Before you deactivate Amazon Inspector, consider [exporting your findings](findings-managing-exporting-reports.md "findings-managing-exporting-reports.md").

Console

###### To deactivate Amazon Inspector

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to
   deactivate Amazon Inspector.
3. In the navigation pane, choose **General settings**.
4. Choose **Deactivate Inspector**.
5. When prompted for confirmation, enter
   **deactivate** in the text box, and then choose
   **Deactivate Inspector**.
6. (Recommended) Repeat these steps in each Region for which
   you want to deactivate Amazon Inspector.

API
Run the [Disable](../../v2/APIReference/API_Disable.md "../../v2/APIReference/API_Disable.md") API operation. In the request, provide the account IDs you are deactivating, and `EC2, ECR, LAMBDA` for `resourceTypes` to deactivate all scans, which will deactivate the account.
