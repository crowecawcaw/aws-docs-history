# Disabling automated sensitive data discovery

You can disable automated sensitive data discovery for an account or organization at any time. If you do this,
Amazon Macie stops performing all automated discovery activities for the account or organization before a
subsequent evaluation and analysis cycle starts, typically within 48 hours. Additional effects
vary:

- If you're a Macie administrator and you disable it for an individual account in your organization,
  you and the account can continue to access to all statistical data, inventory data, and other
  information that Macie produced and directly provided while performing automated discovery for the account.
  You can enable automated discovery for the account again. Macie then resumes all automated discovery activities for the
  account.
- If you're a Macie administrator and you disable it for your organization, you and the accounts in
  your organization lose access to all statistical data, inventory data, and other information
  that Macie produced and directly provided while performing automated discovery for your organization. For
  example, your S3 bucket inventory no longer includes sensitivity visualizations or analyses
  statistics. You can subsequently enable automated discovery for your organization again. Macie then resumes
  all automated discovery activities for accounts in your organization. If you re-enable it within 30 days,
  you and the accounts regain access to data and information that Macie previously produced and
  directly provided while performing automated discovery. If you don't re-enable it within 30 days, Macie
  permanently deletes this data and information.
- If you disable it for your standalone Macie account, you lose access to all statistical
  data, inventory data, and other information that Macie produced and directly provided while
  performing automated discovery for your account. If you don't re-enable it within 30 days, Macie permanently
  deletes this data and information.
  You can continue to access sensitive data findings that Macie produced while performing
  automated sensitive data discovery for the account or organization. Macie stores findings for 90 days. Macie also retains
  your configuration settings for automated discovery. In addition, data that you stored or published to other
  AWS services remains intact and isn't affected, such as sensitive data discovery results in
  Amazon S3 and finding events in Amazon EventBridge.

###### To disable automated sensitive data discovery

If you're the Macie administrator for an organization or you have a standalone Macie account, you
can disable automated sensitive data discovery by using the Amazon Macie console or the Amazon Macie API. If you have a member
account in an organization, work with your Macie administrator to disable automated discovery for your account. Only
your Macie administrator can disable automated discovery for your account.

Console
Follow these steps to disable automated sensitive data discovery by using the Amazon Macie console.

###### To disable automated sensitive data discovery

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to disable automated sensitive data discovery.
3. In the navigation pane, under **Settings**, choose **Automated
   sensitive data discovery**.
4. If you're the Macie administrator for an organization, choose an option in the
   **Status** section to specify the accounts to disable automated sensitive data discovery
   for:
   - To disable it for only particular member accounts, choose **Manage
     accounts**. Then, in the table on the **Accounts** page, select
     the checkbox for each account to disable it for. When you finish, choose **Disable
     automated sensitive data discovery** on the **Actions** menu.
   - To disable it for only your Macie administrator account, choose **Disable**. In
     the dialog box that appears, choose **My account**, and then choose
     **Disable**.
   - To disable it for all the accounts in your organization and your organization
     overall, choose **Disable**. In the dialog box that appears, choose
     **My organization**, and then choose
     **Disable**.

5. If you have a standalone Macie account, choose **Disable** in the
   **Status** section.

If you use Macie in multiple Regions and want to disable automated sensitive data discovery in additional
Regions, repeat the preceding steps in each additional Region.

API
With the Amazon Macie API, you can disable automated sensitive data discovery in two ways. How you disable it
depends partly on the type of account that you have. If you're the Macie administrator for an
organization, it also depends on whether you want to disable automated discovery for only particular member
accounts or your organization overall. If you disable it for your organization, you disable it
for all the accounts that are currently part of your organization. If additional accounts
subsequently join your organization, automated discovery is also disabled for those accounts.

To disable automated sensitive data discovery for an organization or a standalone Macie account, use the [UpdateAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. Or, if you're using the AWS Command Line Interface
(AWS CLI), run the [update-automated-discovery-configuration](../../../cli/latest/reference/macie2/update-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/update-automated-discovery-configuration.md") command. In your request, specify
`DISABLED` for the `status` parameter.

To disable automated sensitive data discovery for only particular member accounts in an organization, use the
[BatchUpdateAutomatedDiscoveryAccounts](../APIReference/automated-discovery-accounts.md "../APIReference/automated-discovery-accounts.md") operation. Or, if you're using the AWS CLI, run
the [batch-update-automated-discovery-accounts](../../../cli/latest/reference/macie2/batch-update-automated-discovery-accounts.md "../../../cli/latest/reference/macie2/batch-update-automated-discovery-accounts.md") command. In your request, use the
`accountId` parameter to specify the account ID for an account that you want to
disable automated discovery for. For the `status` parameter, specify `DISABLED`. To
disable automated discovery for an account, Macie must currently be enabled for the account.

The following examples show how to use the AWS CLI to disable automated sensitive data discovery for one or more
accounts in an organization. This first example disables automated discovery for an organization. It
disables automated discovery for the Macie administrator account and all member accounts in the organization.

```
`$` `aws macie2 update-automated-discovery-configuration --status DISABLED --region `us-east-1``
```

Where `us-east-1` is the Region in which to disable
automated sensitive data discovery for the organization, the US East (N. Virginia) Region. If the request succeeds, Macie disables
automated discovery for the organization and returns an empty response.

These next examples disable automated sensitive data discovery for two member accounts in an organization.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 batch-update-automated-discovery-accounts \
--region `us-east-1` \
--accounts '[{"accountId":"`123456789012`","status":"DISABLED"},{"accountId":"`111122223333`","status":"DISABLED"}]'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 batch-update-automated-discovery-accounts ^
--region `us-east-1` ^
--accounts=[{\"accountId\":\"`123456789012`\",\"status\":\"DISABLED\"},{\"accountId\":\"`111122223333`\",\"status\":\"DISABLED\"}]`
```

Where:

- `us-east-1` is the Region in which to disable
  automated sensitive data discovery for the specified accounts, the US East (N. Virginia) Region.
- `123456789012` and
  `111122223333` are the account IDs for the accounts to
  disable automated sensitive data discovery for.

If the request succeeds for all specified accounts, Macie returns an empty
`errors` array. If the request fails for some accounts, the array specifies the
error that occurred for each affected account. For example:

```
`"errors": [
 {
 "accountId": "123456789012",
 "errorCode": "ACCOUNT_PAUSED"
 }
]`
```

In the preceding response, the request failed for the specified account
(`123456789012`) because Macie is currently suspended for the
account.

If the request fails for all accounts, you receive a message that describes the error
that occurred. For example:

```
`An error occurred (ConflictException) when calling the BatchUpdateAutomatedDiscoveryAccounts operation: Cannot modify account states
while auto-enable is set to ALL.`
```

In the preceding response, the request failed because the member enablement setting for
the organization is currently configured to enable automated sensitive data discovery for all accounts
(`ALL`). To address the error, the Macie administrator must first change this setting to
`NONE` or `NEW`. For information about this setting, see [Enabling automated sensitive data discovery](discovery-asdd-account-enable.md "discovery-asdd-account-enable.md").
