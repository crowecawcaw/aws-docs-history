# AWS IP address ranges notifications

AWS publishes its current IP address ranges in JSON format. Whenever there is a change
to the AWS IP address ranges, we send notifications to subscribers of the Amazon SNS topic named
`AmazonIpSpaceChanged`. For more information about the syntax of the JSON file,
see [Syntax for AWS IP address range JSON](aws-ip-syntax.md "aws-ip-syntax.md").

The payload of the notification contains information in the following format.

```
{
  "create-time":"`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`+00:00",
  "synctoken":"`0123456789`",
  "md5":"`6a45316e8bc9463c9e926d5d37836d33`",
  "url":"https://ip-ranges.amazonaws.com/ip-ranges.json"
}
```

**create-time**

The creation date and time.

Notifications could be delivered out of order. Therefore, we recommend
that you check the timestamps to ensure the correct order.

**synctoken**

The publication time, in Unix epoch time format.

**md5**

The cryptographic hash value of the `ip-ranges.json`
file. You can use this value to check whether the downloaded file is
corrupted.

**url**

The location of the `ip-ranges.json` file. For
more information, see [Download the JSON file](aws-ip-ranges.md#aws-ip-download "aws-ip-ranges.md#aws-ip-download").

You can subscribe to receive notifications as follows.

###### To subscribe to AWS IP address range notifications

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, change the Region to
   **US East (N. Virginia)**, if necessary. You must select this
   Region because the SNS notifications that you are subscribing to were created in
   this Region.
3. In the navigation pane, choose **Subscriptions**.
4. Choose **Create subscription**.
5. In the **Create subscription** dialog box, do the
   following:
   1. For **Topic ARN**, copy the following Amazon Resource
      Name (ARN):

   ```
   arn:aws:sns:us-east-1:806199016981:AmazonIpSpaceChanged
   ```

   2. For **Protocol**, choose the protocol to use (for
      example, `Email`).
   3. For **Endpoint**, type the endpoint to receive the
      notification (for example, your email address).
   4. Choose **Create subscription**.

6. You'll be contacted on the endpoint that you specified and asked to confirm
   your subscription. For example, if you specified an email address, you'll
   receive an email message with the subject line `AWS Notification -
 Subscription Confirmation`. Follow the directions to confirm your
   subscription.
   Notifications are subject to the availability of the endpoint. Therefore, you might
   want to check the JSON file periodically to ensure that you've got the latest ranges.
   For more information about Amazon SNS reliability, see [https://aws.amazon.com/sns/faqs/#Reliability](https://aws.amazon.com/sns/faqs/#Reliability "https://aws.amazon.com/sns/faqs/#Reliability").

If you no longer want to receive these notifications, use the following procedure to
unsubscribe.

###### To unsubscribe from AWS IP address ranges notifications

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Select the check box for the subscription.
4. Choose **Actions**, **Delete
   subscriptions**.
5. When prompted for confirmation, choose **Delete**.
   For more information about Amazon SNS, see the _[Amazon Simple Notification Service Developer Guide](../../../sns/latest/dg.md "../../../sns/latest/dg.md")_.
