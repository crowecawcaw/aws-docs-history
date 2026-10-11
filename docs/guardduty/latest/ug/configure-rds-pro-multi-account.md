

# Enabling RDS Protection in multiple-account environments
<a name="configure-rds-pro-multi-account"></a>

In a multiple-account environment, only the delegated GuardDuty administrator account has the option to enable or disable the RDS Protection feature, including the RDS data activity monitoring additional configuration, for the member accounts in their organization. The GuardDuty member accounts can't modify this configuration from their accounts. The delegated GuardDuty administrator account manages their member accounts using AWS Organizations. This delegated GuardDuty administrator account can choose to auto-enable RDS login activity monitoring and RDS data activity monitoring for all the new accounts as they join the organization. For more information about multiple-account environments, see [Managing multiple accounts](guardduty_accounts.md).

## Enabling RDS Protection for delegated GuardDuty administrator account
<a name="configure-rds-pro-delegatedadmin"></a>

Choose your preferred access method to enable RDS Protection, including the RDS data activity monitoring additional configuration, for the delegated GuardDuty administrator account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**.

1. Under **RDS Protection**, locate the **RDS Login Activity Monitoring** and **RDS Data Activity Monitoring** entries.

1. In the **This account** column, choose **Enabled** for each entry that you want to turn on, or **Not enabled** to leave it off.
**Note**  
RDS Login Activity Monitoring must be enabled before you can enable RDS Data Activity Monitoring.

------
#### [ API/CLI ]

Run the [updateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `RDS_LOGIN_EVENTS` and `status` as `ENABLED`. To also enable RDS data activity monitoring, pass `RDS_DATA_RISK` as the `name` under `AdditionalConfiguration` with `status` set to `ENABLED`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables RDS login activity monitoring on the delegated administrator account, and uses `AdditionalConfiguration` to also enable RDS data activity monitoring:

```
aws guardduty update-detector \
    --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
    --region {{us-east-1}} \
    --features '[
        {
            "Name": "RDS_LOGIN_EVENTS",
            "Status": "ENABLED",
            "AdditionalConfiguration": [
                {
                    "Name": "RDS_DATA_RISK",
                    "Status": "ENABLED"
                }
            ]
        }
    ]'
```

------

## Auto-enable RDS Protection for all member accounts
<a name="auto-enable-rds-pro-existing-memberaccounts"></a>

Choose your preferred access method to enable the RDS Protection feature, including the RDS data activity monitoring additional configuration, for all member accounts. This includes existing member accounts and the new accounts that join the organization.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**.

1. Under **RDS Protection**, choose **Enable for all accounts**. This action automatically enables RDS Protection for both existing and new accounts in the organization.

1. To also turn on RDS data activity monitoring for every account, expand **Additional configuration** and choose **Enable for all accounts** for **RDS Data Activity Monitoring**.

1. Choose **Save all**, then choose **Confirm and save**.
**Note**  
It may take up to 24 hours to update the configuration for the member accounts.

------
#### [ API/CLI ]

To enable RDS Protection for all member accounts in your organization, including existing members and new accounts that join later, invoke the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API operation using your own {{detector ID}}. Set `AutoEnable` to `ALL` for the `RDS_LOGIN_EVENTS` feature, and pass `RDS_DATA_RISK` under `AdditionalConfiguration` with `AutoEnable` set to `ALL` to also auto-enable RDS data activity monitoring.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example auto-enables both `RDS_LOGIN_EVENTS` and `RDS_DATA_RISK` for every member account in the organization:

```
aws guardduty update-organization-configuration \
    --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
    --region {{us-east-1}} \
    --auto-enable-organization-members ALL \
    --features '[
        {
            "Name": "RDS_LOGIN_EVENTS",
            "AutoEnable": "ALL",
            "AdditionalConfiguration": [
                {
                    "Name": "RDS_DATA_RISK",
                    "AutoEnable": "ALL"
                }
            ]
        }
    ]'
```

**Note**  
It may take up to 24 hours to update the configuration for the member accounts.

------

## Enable RDS Protection for all existing active member accounts
<a name="enable-for-all-existing-members-rds-pro"></a>

Choose your preferred access method to enable RDS Protection, including the RDS data activity monitoring additional configuration, for all the existing active member accounts in your organization. The member accounts that already have GuardDuty enabled, are referred to as existing active members.

**Note**  
RDS Login Activity Monitoring must be enabled on a member account before you can enable RDS Data Activity Monitoring on that account.

------
#### [ Console ]

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Sign in using the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

1. On the **Accounts** page, select the existing active member accounts you want to enable. To select every account, use the checkbox in the table header.

1. From the **Edit Protection Plans** dropdown menu, choose **RDS Login Activity**, and then choose **Enable**.

1. To also enable RDS data activity monitoring on the selected accounts, open the **Edit Protection Plans** dropdown menu again, choose **RDS Data Activity**, and then choose **Enable**. RDS Login Activity Monitoring must already be enabled on each selected account.

------
#### [ API/CLI ]

Run the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. Pass `RDS_DATA_RISK` under `AdditionalConfiguration` on the `RDS_LOGIN_EVENTS` feature to also control RDS data activity monitoring. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables RDS login activity monitoring on an existing active member account, and uses `AdditionalConfiguration` to also enable RDS data activity monitoring:

```
aws guardduty update-member-detectors \
    --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
    --region {{us-east-1}} \
    --account-ids {{111122223333}} \
    --features '[
        {
            "Name": "RDS_LOGIN_EVENTS",
            "Status": "ENABLED",
            "AdditionalConfiguration": [
                {
                    "Name": "RDS_DATA_RISK",
                    "Status": "ENABLED"
                }
            ]
        }
    ]'
```

You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------

## Auto-enable RDS Protection for new member accounts
<a name="auto-enable-rds-pro-new-members"></a>

Choose your preferred access method to enable RDS login activity monitoring and RDS data activity monitoring for new accounts that join your organization.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**.

1. Choose **Configure accounts manually**.

1. Under **RDS Protection**, select **Automatically enable for new member accounts**. This step ensures that whenever a new account joins your organization, RDS Protection will be automatically enabled for their account. Only the organization delegated GuardDuty administrator account can modify this configuration.

1. To also auto-enable RDS data activity monitoring for new accounts, expand **Additional configuration** and select **Automatically enable for new member accounts** for **RDS Data Activity Monitoring**.

1. Choose **Save**.

------
#### [ API/CLI ]

To auto-enable RDS Protection for new accounts that join your organization, invoke the [UpdateOrganizationConfiguration](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateOrganizationConfiguration.html) API operation using your own {{detector ID}}. Set `AutoEnable` to `NEW` for the `RDS_LOGIN_EVENTS` feature, and pass `RDS_DATA_RISK` under `AdditionalConfiguration` with `AutoEnable` set to `NEW` to also auto-enable RDS data activity monitoring. To stop auto-enabling a feature for new accounts, set its `AutoEnable` value to `NONE`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example auto-enables both `RDS_LOGIN_EVENTS` and `RDS_DATA_RISK` for new accounts that join the organization:

```
aws guardduty update-organization-configuration \
    --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} \
    --region {{us-east-1}} \
    --auto-enable-organization-members NEW \
    --features '[
        {
            "Name": "RDS_LOGIN_EVENTS",
            "AutoEnable": "NEW",
            "AdditionalConfiguration": [
                {
                    "Name": "RDS_DATA_RISK",
                    "AutoEnable": "NEW"
                }
            ]
        }
    ]'
```

------

## Selectively enable RDS Protection for member accounts
<a name="enable-disable-rds-pro-selectively"></a>

Choose your preferred access method to selectively enable monitoring RDS login activity and RDS data activity for member accounts.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

   Make sure to use the delegated GuardDuty administrator account credentials.

1. In the navigation pane, choose **Accounts**.

   On the **Accounts** page, review the **RDS login activity** and **RDS data activity** columns for the status of your member account. 

1. 

**To selectively enable or disable RDS login activity**

   Select the account for which you want to configure RDS Protection. You can select multiple accounts at a time. In the **Edit Protection Plans** dropdown menu, choose **RDS Login Activity**, and then choose the appropriate option.

1. 

**To selectively enable or disable RDS data activity**

   Select the account for which you want to configure RDS data activity monitoring. You can select multiple accounts at a time. In the **Edit Protection Plans** dropdown menu, choose **RDS Data Activity**, and then choose the appropriate option.

------
#### [ API/CLI ]

To selectively enable or disable RDS Protection for your member accounts, invoke the [updateMemberDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateMemberDetectors.html) API operation using your own {{detector ID}}. Pass `RDS_DATA_RISK` under `AdditionalConfiguration` on the `RDS_LOGIN_EVENTS` feature to control RDS data activity monitoring independently. 

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

The following example enables both `RDS_LOGIN_EVENTS` and `RDS_DATA_RISK`:

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --account-ids {{111122223333}} --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "{{ENABLED}}", "AdditionalConfiguration": [{"Name": "RDS_DATA_RISK", "Status": "{{ENABLED}}"}]}]'
```

To keep RDS login activity monitoring on while turning off RDS data activity monitoring, set `RDS_LOGIN_EVENTS` `Status` to `ENABLED` and `RDS_DATA_RISK` `Status` to `DISABLED`:

```
aws guardduty update-member-detectors --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --account-ids {{111122223333}} --features '[{"Name": "RDS_LOGIN_EVENTS", "Status": "ENABLED", "AdditionalConfiguration": [{"Name": "RDS_DATA_RISK", "Status": "DISABLED"}]}]'
```

**Note**  
You can also pass a list of account IDs separated by a space.

When the code has successfully executed, it returns an empty list of `UnprocessedAccounts`. If there were any problems changing the detector settings for an account, that account ID is listed along with a summary of the issue.

------