# Enabling Lambda Protection for a

standalone account

A standalone account owns the decision to enable or disable a protection plan in their
AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method of
invitation, this section doesn't apply to your account. For more information, see [Enabling Lambda Protection in
multiple-account environments](configure-lambda-protection-multi-acc-env.md "configure-lambda-protection-multi-acc-env.md").

After you enable Lambda Protection, GuardDuty will start monitoring [Lambda Network Activity Monitoring](lambda-protection.md#gdu-lambda-flow-logs "lambda-protection.md#gdu-lambda-flow-logs") in your
account.

Choose your preferred access method to configure Lambda Protection for a standalone account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, under **Settings**, choose
   **Lambda Protection**.
3. The Lambda Protection page shows the current status for your account. Choose
   **Enable** to enable Lambda Protection in your account.
4. Choose **Confirm** to save your selection.

API/CLI
Run the [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") API operation using your own regional
detector ID and passing the `features` object `name` as
`LAMBDA_NETWORK_LOGS` and `status` as
`ENABLED`.

Alternatively, you can use AWS CLI to enable Lambda Protection. Run the following command, and
replace `12abc34d567e8fa901bc2d34e56789f0` with your account's
detector ID and `us-east-1` with the Region where you want to
enable Lambda Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features [{"Name" : "LAMBDA_NETWORK_LOGS", "Status" : "ENABLED"}]'
```
