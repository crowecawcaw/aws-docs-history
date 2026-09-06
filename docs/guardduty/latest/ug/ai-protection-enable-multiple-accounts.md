

# Enabling AI Protection in multiple-account environments
<a name="ai-protection-enable-multiple-accounts"></a>

In a multiple-account environment, only the delegated GuardDuty administrator account can enable or disable AI Protection for the member accounts in the organization. Member accounts can't modify this configuration from their own accounts. The delegated GuardDuty administrator account manages member accounts using AWS Organizations, and can choose to auto-enable AI Protection for all new accounts as they join the organization. For more information about multiple-account environments, see [Managing multiple accounts in Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_accounts.html).

## Enabling AI Protection for the delegated GuardDuty administrator account
<a name="configure-ai-protection-delegatedadmin"></a>

Choose your preferred access method to enable AI Protection for the delegated GuardDuty administrator account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **AI Protection**, you can view the current configuration status of AI Protection.

1. Do one of the following:

**Using **Enable for all accounts****
   + Choose **Enable for all accounts**. This will enable the protection plan for all the active GuardDuty accounts in your AWS organization, including the new accounts that join the organization.
   + Choose **Save**.

**Using **Configure accounts manually****
   + To enable the protection plan only for the delegated GuardDuty administrator account account, choose **Configure accounts manually**.
   + Choose **Enable** under the **delegated GuardDuty administrator account (this account)** section.
   + Choose **Save**.

------
#### [ API/CLI ]

Run the [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `AI_PROTECTION` and `status` as `ENABLED` or `DISABLED`.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables AI Protection for the delegated GuardDuty administrator account. Replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable AI Protection.

```
aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --features '[{"Name": "AI_PROTECTION", "Status": "ENABLED"}]'
```

To disable AI Protection, replace `ENABLED` with `DISABLED`.

------

## Enabling AI Protection for all existing active member accounts
<a name="enable-ai-protection-all-existing-members"></a>

Choose your preferred access method to enable AI Protection for all the existing active member accounts in the organization.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **AI Protection**, in the **Active member accounts** section, choose **Actions**.

1. From the **Actions** dropdown menu, choose **Enable for all existing active member accounts**.

1. Choose **Save**.

------
#### [ API/CLI ]

To selectively enable or disable AI Protection for your member accounts, run the [UpdateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables AI Protection for a single member account. To disable it, replace `ENABLED` with `DISABLED`. You can also pass a list of account IDs separated by a space.

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --account-ids {{111122223333}} --region {{us-east-1}} --features '[{"Name": "AI_PROTECTION", "Status": "ENABLED"}]'
```

When the command runs successfully, it returns an empty list of `UnprocessedAccounts`. If there are any problems changing the detector settings for an account, the response lists that account ID along with a summary of the issue.

------

## Auto-enable AI Protection for new member accounts
<a name="auto-enable-ai-protection-new-members"></a>

Choose your preferred access method to enable AI Protection for new accounts that join your organization.

In the console, the delegated GuardDuty administrator account can auto-enable AI Protection for new member accounts by using either the **Protection Plans** page or the **Accounts** page.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. Do one of the following:
   + Using the **Protection Plans** page:

     1. In the navigation pane, choose **Protection Plans**.

     1. Choose **Configure all enablements**.

     1. Under **AI Protection**, choose **Configure accounts manually**, and then select **Automatically enable for new member accounts**. This step ensures that whenever a new account joins your organization, GuardDuty automatically enables AI Protection for that account. Only the organization delegated GuardDuty administrator account can modify this configuration.

     1. Choose **Save**.
   + Using the **Accounts** page:

     1. In the navigation pane, choose **Accounts**.

     1. On the **Accounts** page, choose **Auto-enable** preferences.

     1. In the **Manage auto-enable preferences** window, select **Enable for new accounts** under **AI Protection**.

     1. Choose **Save**.

------
#### [ API/CLI ]

To enable AI Protection for new member accounts, run the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API operation using your own {{detector ID}}.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables AI Protection for new accounts that join your organization. If you don't want to enable it for all new accounts, set `AutoEnable` to `NONE`.

```
aws guardduty update-organization-configuration --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --auto-enable --features '[{"Name": "AI_PROTECTION", "AutoEnable": "NEW"}]'
```

------