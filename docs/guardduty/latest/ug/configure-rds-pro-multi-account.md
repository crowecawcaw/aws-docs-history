

# Enabling RDS Protection in multiple-account environments
<a name="configure-rds-pro-multi-account"></a>

In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable the RDS Protection feature for the member accounts in their organization. The GuardDuty member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account manages their member accounts using AWS Organizations. This delegated GuardDuty administrator account can choose to auto-enable RDS login activity monitoring for all the new accounts as they join the organization. For more information about multiple-account environments, see [Multiple accounts in GuardDuty](guardduty_accounts.md).

## Enabling RDS Protection for delegated GuardDuty administrator account
<a name="configure-rds-pro-delegatedadmin"></a>

Choose your preferred access method to configure RDS Login Activity Monitoring for the delegated GuardDuty administrator account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**.

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

Run the [updateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `RDS_LOGIN_EVENTS` and `status` as `ENABLED`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "ENABLED"}]'
```

------

## Auto-enable RDS Protection for all member accounts
<a name="auto-enable-rds-pro-existing-memberaccounts"></a>

Choose your preferred access method to enable the RDS Protection feature for all member accounts. This includes existing member accounts and the new accounts that join the organization.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. Do one of the following:

**Using the **Protection Plans** page**

   1. In the navigation pane, choose **Protection Plans**.

   1. Choose **Configure all enablements**.

   1. Under **RDS Protection**, choose **Enable for all accounts**. This action automatically enables RDS Protection for both existing and new accounts in the organization.

   1. Choose **Save all**, then choose **Confirm and save**.
**Note**  
It may take up to 24 hours to update the configuration for the member accounts.

**Using the **Accounts** page**

   1. In the navigation pane, choose **Accounts**.

   1. On the **Accounts** page, choose **Auto-enable** preferences before **Add accounts by invitation**.

   1. In the **Manage auto-enable preferences** window, choose **Enable for all accounts** under **RDS Login Activity Monitoring**.

   1. Choose **Save**.

   If you can't use the **Enable for all accounts** option, see [Selectively enable RDS Protection for member accounts](#enable-disable-rds-pro-selectively).

------
#### [ API/CLI ]

To selectively enable or disable RDS Protection for your member accounts, invoke the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --account-ids {{111122223333}} --features '[{"name": "RDS_LOGIN_EVENTS", "status": "{{ENABLED}}"}]'
```

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Enable RDS Protection for all existing active member accounts
<a name="enable-for-all-existing-members-rds-pro"></a>

Choose your preferred access method to enable RDS Protection for all the existing active member accounts in your organization. The member accounts that already have GuardDuty enabled, are referred to as existing active members.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **RDS Protection**, you can view the current status of the configuration. Under the **Active member accounts** section, choose **Actions**.

1. From the **Actions** dropdown menu, choose **Enable for all existing active member accounts**.

1. Choose **Confirm**.

------
#### [ API/CLI ]

Run the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --account-ids {{111122223333}} --features '[{"name": "RDS_LOGIN_EVENTS", "status": "{{ENABLED}}"}]'
```

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Auto-enable RDS Protection for new member accounts
<a name="auto-enable-rds-pro-new-members"></a>

Choose your preferred access method to enable RDS login activity for new accounts that join your organization.

------
#### [ Console ]

The delegated GuardDuty administrator account can enable for new member accounts in an organization through the console, using either the **RDS Protection** or **Accounts** page.

**To auto-enable RDS Protection for new member accounts**

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. Do one of the following:
   + Using the **Protection Plans** page:

     1. In the navigation pane, choose **Protection Plans**.

     1. Choose **Configure all enablements**.

     1. Choose **Configure accounts manually**.

     1. Select **Automatically enable for new member accounts**. This step ensures that whenever a new account joins your organization, RDS Protection will be automatically enabled for their account. Only the organization delegated GuardDuty administrator account can modify this configuration.

     1. Choose **Save**.
   + Using the **Accounts** page:

     1. In the navigation pane, choose **Accounts**.

     1. On the **Accounts** page, choose **Auto-enable** preferences.

     1. In the **Manage auto-enable preferences** window, select **Enable for new accounts** under **RDS Login Activity Monitoring**.

     1. Choose **Save**.

------
#### [ API/CLI ]

To selectively enable or disable RDS Protection for your member accounts, invoke the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API operation using your own {{detector ID}}. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. If you don't want to enable it for all the new accounts joining the organization, set `autoEnable` to `NONE`.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-organization-configuration --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --auto-enable --features '[{"Name": "RDS_LOGIN_EVENTS", "AutoEnable": "NEW"}]'
```

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Selectively enable RDS Protection for member accounts
<a name="enable-disable-rds-pro-selectively"></a>

Choose your preferred access method to selectively enable monitoring RDS login activity for member accounts.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

   On the **Accounts** page, review the **RDS login activity** column for the status of your member account. 

1. 

**To selectively enable or disable RDS login activity**

   Select the account for which you want to configure RDS Protection. You can select multiple accounts at a time. In the **Edit Protection Plans** dropdown menu, choose **RDS Login Activity**, and then choose the appropriate option.

------
#### [ API/CLI ]

To selectively enable or disable RDS Protection for your member accounts, invoke the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --account-ids {{111122223333}} --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "{{ENABLED}}"}]'
```

**Note**  
You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------