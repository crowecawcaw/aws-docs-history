# Enabling RDS Protection for a standalone

account

A standalone account owns the decision to enable or disable a protection plan in their
AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of
invitation, this section doesn't apply to your account. For more information, see [Enabling RDS Protection in multiple-account
environments](configure-rds-pro-multi-account.md "configure-rds-pro-multi-account.md").

After you enable RDS Protection, GuardDuty will start monitoring [RDS login activity](rds-protection.md#guardduty-rds-login-events "rds-protection.md#guardduty-rds-login-events") for the
supported databases in your account.

Choose your preferred access method to configure RDS Protection for a standalone account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **RDS Protection**.
3. The **RDS Protection** page shows the current status for your
   account. Choose **Enable** to enable RDS Protection.
4. Choose **Confirm** to save your selection.

API/CLI
Run the [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") API operation using your own regional
detector ID and passing the `features` object `name` as
`RDS_LOGIN_EVENTS` and `status` as `ENABLED`.

Alternatively, you can use AWS CLI to enable RDS Protection. Run the following command, and
replace `12abc34d567e8fa901bc2d34e56789f0` with your account's
detector ID and `us-east-1` with the Region where you want to
enable RDS Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features '[{"Name" : "RDS_LOGIN_EVENTS", "Status" : "ENABLED"}]'
```
