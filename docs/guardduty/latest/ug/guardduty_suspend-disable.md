# Suspending or disabling GuardDuty

You can use the GuardDuty console to suspend or disable the GuardDuty service. You don't get
charged for using GuardDuty when the service is suspended.

- All member accounts must be disassociated or deleted before you can suspend or
  disable GuardDuty.
- If you suspend GuardDuty, it no longer monitors the security of your AWS environment
  or generates new findings. Your existing findings remain intact and are not affected
  by the GuardDuty suspension. You can choose to re-enable GuardDuty later.
- When you disable GuardDuty in an account, it will be disabled only for the currently
  selected AWS Region. If you want to completely disable GuardDuty, you must disable it
  in each Region where it is enabled.
- If you disable GuardDuty, your existing findings and the GuardDuty configuration are lost
  and can't be recovered. If you want to save your existing findings, you must export
  them before you confirm to disable GuardDuty. For information on how to export findings,
  see [Exporting generated findings to
  Amazon S3](guardduty_exportfindings.md "guardduty_exportfindings.md").
- If you have enabled Malware Protection for S3 for one or more protected buckets in your account,
  then suspending or disabling GuardDuty doesn't impact the status of a protected
  bucket under Malware Protection for S3. Even after suspending or disabling GuardDuty, your account will
  continue incurring the usage costs associated with the Malware Protection for S3 feature. For
  information about disabling Malware Protection for S3, see [Disabling Malware Protection for S3 for a protected
  bucket](disable-malware-s3-protected-bucket.md "disable-malware-s3-protected-bucket.md").

###### To suspend or disable GuardDuty

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Settings**.
3. In the **Suspend GuardDuty** section, choose **Suspend
   GuardDuty** or **Disable GuardDuty**, then
   **Confirm** your action.

###### To re-enable GuardDuty after suspending

1. Open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/ "https://console.aws.amazon.com/guardduty/").
2. In the navigation pane, choose **Settings**.
3. Choose **Re-enable GuardDuty**.
