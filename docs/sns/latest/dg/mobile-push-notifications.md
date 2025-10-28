# Using Amazon SNS for mobile push

notifications

This section describes how to send mobile push notifications.

## Publishing to a topic

You can also use Amazon SNS to send messages to mobile endpoints subscribed to a topic. The
concept is the same as subscribing other endpoint types, such as Amazon SQS, HTTP/S, email, and
SMS, to a topic, as described in [What is Amazon SNS?](welcome.md "welcome.md"). The
difference is that Amazon SNS communicates through notification services like Apple Push
Notification Service (APNS) and Google Firebase Cloud Messaging (FCM). Through the
notifications service, the subscribed mobile endpoints receive notifications sent to the
topic.

## Direct Amazon SNS mobile device messaging

You can send Amazon SNS push notification messages directly to an endpoint which represents an
application on a mobile device.

###### To send a direct message

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Push notifications**.
3. On the **Mobile push notifications** page, in the
   **Platform applications** section, choose the name of the
   application, for example
   `**MyApp**`.
4. On the `**MyApp**` page, in the
   **Endpoints** section, choose an endpoint and then choose
   **Publish message**.
5. On the **Publish message to endpoint** page, enter the message
   that will appear in the application on the mobile device and then choose
   **Publish message**.

Amazon SNS sends the notification message to the platform notification service which,
in turn, sends the message to the application.
