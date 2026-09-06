

# Enabling AI Protection for a standalone account
<a name="ai-protection-enable-standalone-account"></a>

A standalone account owns the decision to enable or disable a protection plan in its AWS account in a specific Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations or by invitation, this section doesn't apply to you. For information about managing multiple accounts, see [Enabling AI Protection in multiple-account environments](ai-protection-enable-multiple-accounts.md).

After you enable AI Protection, GuardDuty starts monitoring the Amazon Bedrock and Amazon SageMaker AI model invocation activity that it collects from CloudTrail for your account.

Choose your preferred access method to enable AI Protection in your standalone account.

------
#### [ Console ]

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).

1. From the **Region** selector in the upper-right corner, select a Region where you want to enable AI Protection.

1. In the navigation pane, choose **Protection Plans**.

1. Choose **Configure all enablements**. Under **AI Protection**, choose **Enable** to enable AI Protection.

1. Choose **Save all**, then choose **Confirm and save**.

------
#### [ API/CLI ]

Run the [UpdateDetector](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_UpdateDetector.html) API operation using your own regional detector ID and passing the `features` object `name` as `AI_PROTECTION` and `status` as `ENABLED`.

Alternatively, you can use the AWS CLI to enable AI Protection. Run the following command, and replace {{12abc34d567e8fa901bc2d34e56789f0}} with your account's detector ID and {{us-east-1}} with the Region where you want to enable AI Protection.

To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

```
aws guardduty update-detector --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --region {{us-east-1}} --features '[{"Name": "AI_PROTECTION", "Status": "ENABLED"}]'
```

To disable AI Protection, replace `ENABLED` with `DISABLED`.

------