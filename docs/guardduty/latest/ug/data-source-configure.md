# Enabling S3 Protection for a standalone

account

A standalone account owns the decision to enable or disable a protection plan in their
AWS account in a specific AWS Region.

If your account is associated with a GuardDuty administrator account through AWS Organizations, or by the method
of invitation, this section doesn't apply to your account. For more information,
see [Enabling S3 Protection in multiple-account
environments](s3-multiaccount.md "s3-multiaccount.md").

After you enable S3 Protection, GuardDuty will start monitoring AWS CloudTrail data events for the S3
buckets in your account.

Choose your preferred access method to configure S3 Protection for a standalone
account.

Console

1. Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. From the **Region** selector in the upper-right
   corner, select a Region where you want to enable S3 Protection.
3. In the navigation pane, choose
   **S3 Protection**.
4. The **S3 Protection** page provides the current status
   of S3 Protection for your account. Choose **Enable** or
   **Disable** to enable or disable S3 Protection at any
   point in time.
5. Choose **Confirm** to confirm your
   selection.

API/CLI
Run [updateDetector](../APIReference/API_UpdateDetector.md "../APIReference/API_UpdateDetector.md") by using your valid detector
ID for the current Region and passing the `features` object
`name` as `S3_DATA_EVENTS` set to
`ENABLED` to enable S3 Protection, respectively.

###### Note

To find the `detectorId` for your account and current Region, see the
**Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/") console,
or run the [ListDetectors](../APIReference/API_ListDetectors.md "../APIReference/API_ListDetectors.md") API.

Alternatively, you can use AWS Command Line Interface. To enable S3 Protection, run the following
command, and replace
`12abc34d567e8fa901bc2d34e56789f0` with your
account's detector ID and `us-east-1` with the
Region where you want to enable S3 Protection.

```
aws guardduty update-detector --detector-id `12abc34d567e8fa901bc2d34e56789f0` --region `us-east-1` --features '[{"Name" : "S3_DATA_EVENTS", "Status" : "ENABLED"}]'
```
