# Creating a configuration for AWS Artifact notification settings

###### Note

The content of this page is only applicable to commercial AWS [Regions](../../../glossary/latest/reference/glos-chap.md#region "../../../glossary/latest/reference/glos-chap.md#region"), and does not currently apply to AWS GovCloud (US) Regions.

After you [select your User Notifications notification hubs](managing-notifications.md#notifications-hubs "managing-notifications.md#notifications-hubs"), you
can create a configuration for notification settings in the AWS Artifact console. In the
configuration that you create, you specify the recipient email addresses that you want
to receive AWS Artifact notifications. You also specify which updates those recipients should
receive notifications about, such as updates for AWS Artifact agreements, and updates for all
(or a subset of) AWS Artifact reports.

###### To create a configuration

1. Open the [Notification settings](https://console.aws.amazon.com/artifact/notification "https://console.aws.amazon.com/artifact/notification") page of the AWS Artifact console.
2. Choose **Create configuration**.
3. On the **Create configuration** page, do the following:
   - To receive notifications for agreements, under **Agreements**,
     keep **Updates on AWS Agreements** selected.
   - To receive notifications for reports, under **Reports**,
     keep **Updates on AWS Reports** selected.
     1. To receive notifications for all reports, choose **All reports**.
     2. To receive notifications only for reports under specific categories and series,
        choose **A subset of reports**. Then, select the categories and series
        that you're interested in.

   - Under **Configuration name**, enter a **Name** for your configuration.
   - Under **Email**, for **Recipients**, enter a comma-separated list of email addresses that you want to receive AWS Artifact notification emails.
   - (Optional) To add tags to the notification configuration, expand **Tags**, choose **Add new tag**,
     and then enter tags as key-value pairs. For more information about tagging User Notifications resources, see [Tagging your AWS User Notifications resources](../../../notifications/latest/userguide/tagging-resources.md "../../../notifications/latest/userguide/tagging-resources.md") in the _AWS User Notifications User Guide_.
   - Choose **Create configuration**.

   User Notifications sends a verification email to each of the recipient email addresses that you provided. To verify the email address,
   in the verification email, the recipient must choose **Verify email**. Only verified email addresses will receive AWS Artifact notifications.
