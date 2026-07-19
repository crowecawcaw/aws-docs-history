# Enabling AI Protection for a standalone account

A standalone account owns the decision to enable or disable a protection plan in its
AWS account in a specific Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations or by invitation, this
section doesn't apply to you. For information about managing multiple
accounts, see [Enabling AI Protection in multiple-account environments](ai-protection-enable-multiple-accounts.md "ai-protection-enable-multiple-accounts.md").

After you enable AI Protection, GuardDuty starts monitoring the Amazon Bedrock and Amazon SageMaker AI model
invocation activity that it collects from CloudTrail for your account.

Choose your preferred access method to enable AI Protection in your standalone
account.

Console

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. From the **Region** selector in the upper-right
   corner, select a Region where you want to enable AI Protection.
3. In the navigation pane, choose **Protection Plans**.
4. Choose **Configure all enablements**. Under **AI
   Protection**, choose **Enable** to enable AI
   Protection.
5. Choose **Save all**, then choose **Confirm and
   save**.

API/CLI
Run the [UpdateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") API operation using your own regional
detector ID and passing the `features` object `name` as
`AI_PROTECTION` and `status` as
`ENABLED`.

Alternatively, you can use the AWS CLI to enable AI Protection. Run the following
command, and replace `12abc34d567e8fa901bc2d34e56789f0`
with your account's detector ID and `us-east-1` with the
Region where you want to enable AI Protection.

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features '[{"Name": "AI_PROTECTION", "Status": "ENABLED"}]'
```

To disable AI Protection, replace `ENABLED` with
`DISABLED`.
