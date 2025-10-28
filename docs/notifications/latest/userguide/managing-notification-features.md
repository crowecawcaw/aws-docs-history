# Disabling or re-enabling AWS managed notifications for AWS Health in AWS User Notifications

###### Note

As of September 15, 2025, AWS managed notifications are enabled by default in AWS accounts.
Your existing notification preferences remain unchanged if you previously disabled AWS managed notifications.

###### Important

Starting December 15, 2025, AWS managed notifications will be enabled for all AWS accounts, including accounts where they were previously disabled.
After this date, you can't disable AWS managed notifications.

You can view and manage
notifications for AWS Health with User Notifications. If you no longer wish to receive these notifications, you can disable them at any time.

## Prerequisites

Attach the following policy to your IAM roles or users to grant them the requisite permissions to enable AWS managed notifications in User Notifications.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "notifications:GetFeatureOptInStatus",
 "notifications:PutFeatureOptInStatus"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Disabling or re-enabling AWS managed notifications for AWS Health

If you no longer wish to receive AWS managed notifications, you can disable them.
If you disable AWS managed notifications, previously subscribed delivery channels won't receive managed notifications. You can re-enable AWS managed notifications at any time.
Configured delivery channels will persist if notifications are enabled again.

To receive AWS managed notifications, ensure they're enabled. The prefix for emails about AWS managed notifications always reflect the originating service.
For example, notifications about AWS Health are sent from the email `health@aws.com`.

###### Note

Any AWS managed notifications that were previously delivered through User Notifications continue to appear up to 90 days, but new AWS managed notifications aren't accessible using User Notifications and are available directly in the AWS Health dashboard.

###### To disable or re-enable AWS managed notifications

1. Open User Notifications in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/").
2. In the navigation pane, choose **AWS managed notifications subscriptions**.
3. Choose **Disable AWS Health notifications** or **Enable AWS Health notifications**.
