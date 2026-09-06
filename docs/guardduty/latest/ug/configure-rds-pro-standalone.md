

# Enabling RDS Protection for a standalone account
<a name="configure-rds-pro-standalone"></a>

A standalone account owns the decision to enable or disable a protection plan in their AWS account in a specific AWS Region. 

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of invitation, this section doesn't apply to your account. For more information, see [Enabling RDS Protection in multiple-account environments](configure-rds-pro-multi-account.md).

After you enable RDS Protection, GuardDuty will start monitoring [RDS login activity](rds-protection.md#guardduty-rds-login-events) for the supported databases in your account.

Choose your preferred access method to configure RDS Protection for a standalone account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **RDS Protection**, choose **Enable** to enable RDS Protection.

1. Choose **Save all**, then choose **Confirm and save**.

------
#### [ API/CLI ]

Run the [updateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `RDS_LOGIN_EVENTS` and `status` as `ENABLED`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable RDS Protection. 

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --features '[{"Name" : "RDS_LOGIN_EVENTS", "Status" : "ENABLED"}]'
```

------