# Enabling automated sensitive data discovery

When you enable automated sensitive data discovery, Amazon Macie begins evaluating your Amazon Simple Storage Service (Amazon S3) inventory data
and performing other automated discovery activities for your account in the current AWS Region. If you're
the Macie administrator for an organization, by default the evaluation and activities include S3 buckets
that your member accounts own. Depending on the size of your Amazon S3 data estate, statistics and
other results can begin to appear within 48 hours.

After you enable automated sensitive data discovery, you can configure settings that refine the scope and nature of
the analyses that Macie performs. These settings specify any S3 buckets to exclude from analyses.
They also specify the managed data identifiers, custom data identifiers, and allow lists that you
want Macie to use when it analyzes S3 objects. For information about these settings, see [Configuring settings for automated sensitive data discovery](discovery-asdd-account-configure.md "discovery-asdd-account-configure.md").
If you're the Macie administrator for an organization, you can also refine the scope of the analyses by
enabling or disabling automated sensitive data discovery for individual accounts in your organization on a case-by-case
basis.

To enable automated sensitive data discovery, you must be the Macie administrator for an organization or have a standalone
Macie account. If you have a member account in an organization, work with your Macie administrator to
enable automated sensitive data discovery for your account.

###### To enable automated sensitive data discovery

If you're the Macie administrator for an organization or you have a standalone Macie account, you
can enable automated sensitive data discovery by using the Amazon Macie console or the Amazon Macie API. If you're enabling it
for the first time, start by [completing
the prerequisite tasks](discovery-asdd-account-configure-prereqs.md "discovery-asdd-account-configure-prereqs.md"). This helps ensure that you have the resources and permissions
that you need.

Console
Follow these steps to enable automated sensitive data discovery by using the Amazon Macie console.

###### To enable automated sensitive data discovery

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to enable automated sensitive data discovery.
3. In the navigation pane, under **Settings**, choose **Automated
   sensitive data discovery**.
4. If you have a standalone Macie account, choose **Enable** in the
   **Status** section.
5. If you're the Macie administrator for an organization, choose an option in the
   **Status** section to specify the accounts to enable automated sensitive data discovery
   for:
   - To enable it for all the accounts in your organization, choose
     **Enable**. In the dialog box that appears, choose **My
     organization**. For an organization in AWS Organizations, select **Enable
     automatically for new accounts** to also enable it automatically for accounts
     that subsequently join your organization. When you finish, choose
     **Enable**.
   - To enable it for only particular member accounts, choose **Manage
     accounts**. Then, in the table on the **Accounts** page, select
     the checkbox for each account to enable it for. When you finish, choose **Enable
     automated sensitive data discovery** on the **Actions** menu.
   - To enable it for only your Macie administrator account, choose **Enable**. In
     the dialog box that appears, choose **My account** and clear
     **Enable automatically for new accounts**. When you finish, choose
     **Enable**.

If you use Macie in multiple Regions and want to enable automated sensitive data discovery in additional Regions,
repeat the preceding steps in each additional Region.

To subsequently check or change the status of automated sensitive data discovery for individual accounts in an
organization, choose **Accounts** in the navigation pane. On the
**Accounts** page, the **Automated sensitive data
discovery** field in the table indicates the current status of automated discovery for an
account. To change the status for an account, select the checkbox for the account. Then use
the **Actions** menu to enable or disable automated discovery for the account.

API
To enable automated sensitive data discovery programmatically, you have several options:

- To enable it for a Macie administrator account, an organization, or a standalone Macie account,
  use the [UpdateAutomatedDiscoveryConfiguration](../APIReference/automated-discovery-configuration.md "../APIReference/automated-discovery-configuration.md") operation. Or, if you're using the AWS Command Line Interface
  (AWS CLI), run the [update-automated-discovery-configuration](../../../cli/latest/reference/macie2/update-automated-discovery-configuration.md "../../../cli/latest/reference/macie2/update-automated-discovery-configuration.md") command.
- To enable it for only particular member accounts in an organization, use the [BatchUpdateAutomatedDiscoveryAccounts](../APIReference/automated-discovery-accounts.md "../APIReference/automated-discovery-accounts.md") operation. Or, if you're using the AWS CLI,
  run the [batch-update-automated-discovery-accounts](../../../cli/latest/reference/macie2/batch-update-automated-discovery-accounts.md "../../../cli/latest/reference/macie2/batch-update-automated-discovery-accounts.md") command. To enable automated discovery for a member
  account, you must first enable it for your administrator account or organization.

Additional options and details vary depending on the type of account that you
have.

If you're a Macie administrator, use the **UpdateAutomatedDiscoveryConfiguration**
operation or run the **update-automated-discovery-configuration** command to
enable automated sensitive data discovery for your account or organization. In your request, specify
`ENABLED` for the `status` parameter. For the
`autoEnableOrganizationMembers` parameter, specify the accounts to enable it for.
If you're using the AWS CLI, specify the accounts by using the
`auto-enable-organization-members` parameter. Valid values are:

- `ALL` (default) – Enable it for all the accounts in your
  organization. This includes your administrator account, existing member accounts, and
  accounts that subsequently join your organization.
- `NEW` – Enable it for your administrator account. Also enable it
  automatically for accounts that subsequently join your organization. If you previously
  enabled automated discovery for your organization and you specify this value, automated discovery will continue to be
  enabled for existing member accounts that it's currently enabled for.
- `NONE` – Enable it for only your administrator account. Don't
  enable it automatically for accounts that subsequently join your organization. If you
  previously enabled automated discovery for your organization and you specify this value, automated discovery will
  continue to be enabled for existing member accounts that it's currently enabled for.

If you want to selectively enable automated sensitive data discovery for only particular member accounts, specify
`NEW` or `NONE`. You can then use the
**BatchUpdateAutomatedDiscoveryAccounts** operation or run the
**batch-update-automated-discovery-accounts** command to enable automated discovery for the
accounts.

If you have a standalone Macie account, use the
**UpdateAutomatedDiscoveryConfiguration** operation or run the
**update-automated-discovery-configuration** command to enable automated sensitive data discovery for
your account. In your request, specify `ENABLED` for the `status`
parameter. For the `autoEnableOrganizationMembers` parameter, consider whether you
plan to become the Macie administrator for other accounts, and specify the appropriate value. If you
specify `NONE`, automated discovery isn't enabled automatically for an account when you become
the Macie administrator for the account. If you specify `ALL` or `NEW`, automated discovery
is enabled automatically for the account. If you're using the AWS CLI, use the
`auto-enable-organization-members` parameter to specify the appropriate value for
this setting.

The following examples show how to use the AWS CLI to enable automated sensitive data discovery for one or more
accounts in an organization. This first example enables automated discovery for all the accounts in an
organization for the first time. It enables automated discovery for the Macie administrator account, all existing
member accounts, and any accounts that subsequently join the organization.

```
`$` `aws macie2 update-automated-discovery-configuration --status ENABLED --auto-enable-organization-members ALL --region `us-east-1``
```

Where `us-east-1` is the Region in which to enable
automated sensitive data discovery for the accounts, the US East (N. Virginia) Region. If the request succeeds, Macie enables automated discovery
for the accounts and returns an empty response.

The next example changes the member enablement setting for an organization to
`NONE`. With this change, automated sensitive data discovery isn't enabled automatically for accounts that
subsequently join the organization. Instead, it's enabled only for the Macie administrator account, and
any existing member accounts that it's currently enabled for.

```
`$` `aws macie2 update-automated-discovery-configuration --status ENABLED --auto-enable-organization-members NONE --region `us-east-1``
```

Where `us-east-1` is the Region in which to change
the setting, the US East (N. Virginia) Region. If the request succeeds, Macie updates the setting and
returns an empty response.

The following examples enable automated sensitive data discovery for two member accounts in an organization. The
Macie administrator has already enabled automated discovery for the organization. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws macie2 batch-update-automated-discovery-accounts \
--region `us-east-1` \
--accounts '[{"accountId":"`123456789012`","status":"ENABLED"},{"accountId":"`111122223333`","status":"ENABLED"}]'`
```

This example is formatted for Microsoft Windows and it uses the caret (^) line-continuation character to improve readability.

```
`C:\>` `aws macie2 batch-update-automated-discovery-accounts ^
--region `us-east-1` ^
--accounts=[{\"accountId\":\"`123456789012`\",\"status\":\"ENABLED\"},{\"accountId\":\"`111122223333`\",\"status\":\"ENABLED\"}]`
```

Where:

- `us-east-1` is the Region in which to enable
  automated sensitive data discovery for the specified accounts, the US East (N. Virginia) Region.
- `123456789012` and
  `111122223333` are the account IDs for the accounts to
  enable automated sensitive data discovery for.

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
(`123456789012`) because Macie is currently suspended for the account. To
address this error, the Macie administrator must first enable Macie for the account.

If the request fails for all accounts, you receive a message that describes the error
that occurred.
