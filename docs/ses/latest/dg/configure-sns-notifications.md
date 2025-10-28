# Configuring Amazon SNS notifications for

Amazon SES

Amazon SES can notify you of your bounces, complaints, and deliveries through [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns "https://aws.amazon.com/sns").

You can configure notifications in the Amazon SES console, or by using the Amazon SES API.

###### Topics in this section:

- [Prerequisites](#configure-feedback-notifications-prerequisites "#configure-feedback-notifications-prerequisites")
- [Configuring notifications
  using the Amazon SES console](#configure-feedback-notifications-console "#configure-feedback-notifications-console")
- [Configuring notifications using
  the Amazon SES API](#configure-feedback-notifications-api "#configure-feedback-notifications-api")
- [Troubleshooting
  feedback notifications](#configure-feedback-notifications-troubleshooting "#configure-feedback-notifications-troubleshooting")

## Prerequisites

Complete the following steps before you set up Amazon SNS notifications in Amazon SES:

1. Create a topic in Amazon SNS. For more information, see [Create a Topic](../../../sns/latest/dg/CreateTopic.md "../../../sns/latest/dg/CreateTopic.md") in the
   _Amazon Simple Notification Service Developer Guide_.

###### Important

When you create your topic using Amazon SNS, for **Type**,
only choose **Standard**. (SES does not support FIFO
type topics.)

Whether you create a new SNS topic or select an existing one, you need
to give access to SES to publish notifications to the topic.

To give Amazon SES permission to publish notifications to the topic, on the
**Edit topic** screen in the SNS console, expand
**Access policy** and in the **JSON
editor**, add the following permission policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "notification-policy",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": "sns:Publish",
 "Resource": "arn:aws:sns:`us-east-1`:`111122223333`:`topic_name`",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "`111122223333`",
 "AWS:SourceArn": "arn:aws:ses:`topic_region`:`111122223333`:identity/`identity_name`"
 }
 }
 }
 ]
}`

```

Make the following changes to the preceding policy example:

    * Replace `topic_region` with the AWS Region
     where you created the SNS topic.
    * Replace `111122223333` with your
     AWS account ID.
    * Replace `topic_name` with the name of your
     SNS topic.
    * Replace `identity_name` with the verified
     identity (email address or domain) that you're subscribing to the
     SNS topic.

2. Subscribe at least one endpoint to the topic. For example, if you want to
   receive notifications by text message, subscribe an SMS endpoint (that is, a
   mobile phone number) to the topic. To receive notifications by email, subscribe
   an email endpoint (an email address) to the topic.

For more information, see [Getting Started](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the _Amazon Simple Notification Service Developer Guide_. 3. (Optional) If your Amazon SNS topic uses AWS Key Management Service (AWS KMS) for server-side
encryption, you have to add permissions to the AWS KMS key policy. You can add
permissions by attaching the following policy to the AWS KMS key policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowSESToUseKMSKey",
 "Effect": "Allow",
 "Principal": {
 "Service": "ses.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Configuring notifications

using the Amazon SES console

###### To configure notifications using the Amazon SES console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Identities**.
3. In the **Identities** container, select the verified identity
   you want to receive feedback notifications for when a message sent from this
   identity results in either a bounce, complaint, or delivery.

###### Important

Verified domain notification settings apply to all mail sent from email
addresses in that domain _except_ for email addresses
that are also verified. 4. In the details screen of the verified identity you selected, choose the
**Notifications** tab and select **Edit**
in the **Feedback notifications** container. 5. Expand the SNS topic list box of each feedback type you want to receive
notifications for, and select either an SNS topic you own, **No SNS
topic**, or **SNS topic you don’t own**.

    1. If you chose **SNS topic you don’t own**, the
     **SNS topic ARN** field will be presented where you
     must enter the SNS topic ARN shared with you by your delegate sender.
     (Only your delegate sender will get these notifications because they own
     the SNS topic. To learn more about delegate sending, see [Overview of sending
     authorization](sending-authorization-overview.md "sending-authorization-overview.md").)###### Important

The Amazon SNS topics that you use for bounce, complaint, and delivery
notifications have to be in the same AWS Region that in which you use
Amazon SES.

Additionally, you have to subscribe one or more endpoints to the topic in
order to receive notifications. For example, if you want to have
notifications sent to an email address, you have to subscribe an email
endpoint to the topic. For more information, see [Getting Started](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in
the _Amazon Simple Notification Service Developer Guide_. 6. (Optional) If you want your topic notification to include the headers from the
original email, check the **Include original email headers**
box directly underneath the SNS topic name of each feedback type. This option is
only available if you've assigned an Amazon SNS topic to the associated notification
type. For information about the contents of the original email headers, see the
`mail` object in [Notification contents](notification-contents.md "notification-contents.md"). 7. Choose **Save changes**. The changes you made to your
notification settings might take a few minutes to take effect. 8. (Optional) If you chose Amazon SNS topic notifications for both bounces and
complaints, you can disable email notifications entirely so that you don't
receive double notifications through email and SNS notifications. To disable
email notifications for bounces and complaints, under the
**Notifications** tab on the details screen of the verified
identity, in the **Email Feedback Forwarding** container,
choose **Edit**, uncheck the **Enabled** box,
and choose **Save changes**.
.

After you configure your settings, you will start receiving bounce, complaint, and
delivery notifications to your Amazon SNS topics. These notifications are in JavaScript
Object Notation (JSON) format and follow the structure described in [Notification contents](notification-contents.md "notification-contents.md").

You will be charged standard Amazon SNS rates for bounce, complaint, and delivery
notifications. For more information, see the [Amazon SNS pricing page](https://aws.amazon.com/sns/pricing "https://aws.amazon.com/sns/pricing").

###### Note

If an attempt to publish to your Amazon SNS topic fails because the topic has been
deleted or your AWS account no longer has permissions to publish to it, Amazon SES
removes the configuration for that topic if it's been configured for bounces or
complaints (not deliveries - for delivery notifications, SES won't delete the
SNS topic configuration setting). Additionally, Amazon SES re-enables bounce and
complaint email notifications for the identity, and you receive a notification of
the change by email. If multiple identities are configured to use the topic, the
topic configuration for each identity is changed when each identity experiences a
failure to publish to the topic.

## Configuring notifications using

the Amazon SES API

You can also configure bounce, complaint, and delivery notifications by using the
Amazon SES API. Use the following operations to configure notifications:

- [SetIdentityNotificationTopic](../APIReference/API_SetIdentityNotificationTopic.md "../APIReference/API_SetIdentityNotificationTopic.md")
- [SetIdentityFeedbackForwardingEnabled](../APIReference/API_SetIdentityFeedbackForwardingEnabled.md "../APIReference/API_SetIdentityFeedbackForwardingEnabled.md")
- [GetIdentityNotificationAttributes](../APIReference/API_GetIdentityNotificationAttributes.md "../APIReference/API_GetIdentityNotificationAttributes.md")
- [SetIdentityHeadersInNotificationsEnabled](../APIReference/API_SetIdentityHeadersInNotificationsEnabled.md "../APIReference/API_SetIdentityHeadersInNotificationsEnabled.md")

You can use these API actions to write a customized front-end application for
notifications. For a complete description of the API actions related to notifications,
see the [Amazon Simple Email Service API Reference](../APIReference.md "../APIReference.md").

## Troubleshooting

feedback notifications

###### Not receiving notifications

If you aren't receiving notifications, make sure that you subscribed an endpoint
to the topic that the notifications are sent through. When you subscribe an email
endpoint to a topic, you receive an email asking you to confirm your subscription.
You have to confirm your subscription before you start receiving email
notifications. For more information, see [Getting Started](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the
_Amazon Simple Notification Service Developer Guide_.

###### `InvalidParameterValue` error when choosing a topic

If you receive an error stating that an `InvalidParameterValue` error
occurred, check the Amazon SNS topic to see if it's encrypted using AWS KMS. If it is, you
have to modify the policy for the AWS KMS key. See [Prerequisites](#configure-feedback-notifications-prerequisites "#configure-feedback-notifications-prerequisites") for a sample
policy.
