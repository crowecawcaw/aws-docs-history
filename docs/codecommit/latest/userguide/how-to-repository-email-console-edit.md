AWS CodeCommit is no longer available to new customers. Existing customers of
AWS CodeCommit can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider")

# Change or disable notifications

You can use the AWS CodeCommit console to change how notifications created
before November 5, 2019 are configured, including the event types that send emails to users
and the Amazon SNS topic used to send emails about the repository. You can also use the CodeCommit
console to manage the list of email addresses and endpoints subscribed to the topic or to
disable notifications.

###### To change notification

settings

1. Open the CodeCommit console at [https://console.aws.amazon.com/codesuite/codecommit/home](https://console.aws.amazon.com/codesuite/codecommit/home "https://console.aws.amazon.com/codesuite/codecommit/home").
2. In **Repositories**, choose the name of the repository where you want
   to configure notifications created before November 5, 2019.
3. In the navigation pane, choose **Settings**, and then choose
   **Notifications**. If you see a banner informing you that you have
   notifications instead of notification rules, choose **Manage existing
   notifications**.
4. Choose **Edit**.
5. Make your changes, and then choose **Save**.
   Disabling notifications is an easy way to temporarily prevent users from receiving emails
   about repository events.

To permanently delete a notification created before November 5, 2019, follow the steps in
[Delete notifications](how-to-repository-email-delete.md "how-to-repository-email-delete.md").

###### To disable notifications

1. Open the CodeCommit console at [https://console.aws.amazon.com/codesuite/codecommit/home](https://console.aws.amazon.com/codesuite/codecommit/home "https://console.aws.amazon.com/codesuite/codecommit/home").
2. In **Repositories**, choose the name of the repository where you want
   to disable notifications.
3. In the navigation pane, choose **Settings**, and then choose
   **Notifications**. Choose **Manage existing
   notifications**.
4. Choose **Edit**, and in **Event status**, use the
   slider to turn off **Enable notifications**. Choose
   **Save**.
5. The event status changes to **Disabled**. No emails about events are
   sent. When you disable notifications, the CloudWatch Events rule for the repository is disabled
   automatically. Do not manually change its status in the CloudWatch Events console.
