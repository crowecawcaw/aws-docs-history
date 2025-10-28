# Receive Notifications on New Updates

###### Note

AWS Deep Learning AMIs have a weekly release cadence for security patches. Release notifications will be sent for these incremental security patches though they may not be included in official release notes.

You can receive notifications whenever a new DLAMI is released. Notifications are published with [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") using the following topic.

```
arn:aws:sns:us-west-2:767397762724:dlami-updates
```

Messages are posted here when a new DLAMI is published. The version, metadata, and regional AMI ID’s of the AMI will be included in the message.

These messages can be received using several different methods. We recommend that you use the following method.

1. Open the [Amazon SNS console](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, change the AWS Region to **US West (Oregon)**,
   if necessary. You must select the region where the SNS notification that you're subscribing to
   was created.
3. In the navigation pane, choose **Subscriptions, Create
   subscription**.
4. For the **Create subscription** dialog box, do
   the following:
   1. For **Topic ARN**, copy and paste the following Amazon
      Resource Name (ARN): `arn:aws:sns:us-west-2:767397762724:dlami-updates`
   2. For **Protocol**, choose one from
      **[Amazon SQS, AWS Lamda, Email, Email-JSON]**
   3. For **Endpoint**, enter the email address or
      **Amazon Resource Name (ARN)** of resource that you will
      use to receive the notifications.
   4. Choose **Create subscription**.

5. You receive a confirmation email with the subject line
   _AWS Notification - Subscription Confirmation_.
   Open the email and choose **Confirm subscription** to complete your subscription.
