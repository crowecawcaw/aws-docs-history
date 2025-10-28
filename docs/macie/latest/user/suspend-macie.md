# Suspending Macie for your AWS account

You can temporarily pause Amazon Macie for your AWS account in an AWS Region. You can do
this by suspending Macie in the Region. Macie then stops performing all activities for your
account in that Region. The activities include: monitoring your Amazon Simple Storage Service (Amazon S3) data,
performing automated sensitive data discovery, and running sensitive data discovery jobs that are currently in progress. Macie
also cancels all of your sensitive data discovery jobs in the Region. You aren't charged for using Macie
in the Region while it's suspended.

If you suspend Macie in a Region, Macie retains the session identifier, settings, and
resources that it stores or maintains for your account in the Region. Macie also retains
certain data that it stores or maintains for your account in the Region. For example, your
existing findings remain intact and are retained for up to 90 days. If automated sensitive data discovery was
enabled for your account, your existing results also remain intact and are retained for up
to 30 days.

###### Note

If your account is part of an organization that centrally manages multiple Macie
accounts, note the following requirements for suspending Macie:

- If you have a member account in an AWS Organizations organization, you must contact the
  Macie administrator for your organization. Only your Macie administrator can suspend Macie for
  your account.
- If you're the Macie administrator for the organization, you must remove all member
  accounts that are associated with your account before you suspend Macie for your
  account. How you do this depends on whether your account is associated with the
  accounts through AWS Organizations or by invitation. For more information, see [Managing multiple accounts](macie-accounts.md "macie-accounts.md").
  After you suspend Macie in a Region, you can enable it again later. You then regain access
  to your Macie settings, resources, and data in the Region. In addition, Macie resumes its
  activities for your account in the Region. This includes updating and maintaining
  information about your S3 buckets, and monitoring the buckets for security and access
  control. This doesn't include resuming or restarting your sensitive data discovery jobs. Sensitive data
  discovery jobs can't be resumed or restarted after they're cancelled.

###### To suspend Macie for your account

To suspend Macie for your account, you can use the Amazon Macie console or the Amazon Macie
API. Follow these steps to suspend it by using the console. To suspend it
programmatically, use the [UpdateMacieSession](../APIReference/macie.md "../APIReference/macie.md") operation of
the Amazon Macie API.

1. Open the Amazon Macie console at [https://console.aws.amazon.com/macie/](https://console.aws.amazon.com/macie/ "https://console.aws.amazon.com/macie/").
2. By using the AWS Region selector in the upper-right corner of the page, choose the Region in which you want to suspend Macie.
3. In the navigation pane, choose **Settings**.
4. In the **Suspend Macie** section, choose **Suspend
   Macie**.
5. When prompted for confirmation, enter `Suspend`, and then
   choose **Suspend**.
6. To suspend Macie in additional Regions, repeat steps 2 through 5 in each
   additional Region.
   To subsequently re-enable Macie in a Region, open the Amazon Macie console and choose the Region
   by using the AWS Region selector. Then choose **Settings** in the
   navigation pane. In the **Suspend Macie** section, choose
   **Re-enable Macie**. You can also re-enable Macie programmatically. To
   do this, use the [UpdateMacieSession](../APIReference/macie.md "../APIReference/macie.md") operation of the Amazon Macie API.
