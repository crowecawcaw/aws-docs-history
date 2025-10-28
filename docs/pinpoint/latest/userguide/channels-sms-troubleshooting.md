**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Troubleshooting the SMS channel

Verify that logging is turned on to assist in identifying the cause of failure. For more
information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging "troubleshooting.md#troubleshooting-logging"). To
turn on logging for AWS End User Messaging SMS and Voice v2 API, see [How do
I set up logging for Amazon Pinpoint voice messages for Amazon Pinpoint SMS and Voice v2 API?](https://repost.aws/knowledge-center/pinpoint-voice-message-logging-setup-v2 "https://repost.aws/knowledge-center/pinpoint-voice-message-logging-setup-v2").

## SMS delivery failures

###### **Issues and solutions**

- Confirm that the number is valid using the [Amazon Pinpoint number validator](../developerguide/validate-phone-numbers.md "../developerguide/validate-phone-numbers.md"). SMS delivery is
  only supported for ‘MOBILE’ phoneType. SMS delivery to ‘VOIP’ numbers is attempted on a best effort.
- Confirm that your monthly SMS spend quota isn't depleted.
  For more information see [Monitoring SMS, MMS, and voice spending activity](../../../sms-voice/latest/userguide/monitor-spending.md "../../../sms-voice/latest/userguide/monitor-spending.md") in the _AWS End User Messaging SMS User Guide_.
- If the delivery issue is limited to one or two devices, then rule out device-related
  issues. Verify that the number(s) can receive SMS outside of Amazon Pinpoint at the time
  of the failure.
- Turn on SMS event logging to assist in identifying the cause of the failure.
  - Review the [message status](../developerguide/event-streams-data-sms.md#event-streams-data-sms-attributes-attrs "../developerguide/event-streams-data-sms.md#event-streams-data-sms-attributes-attrs").
  - Review how to resolve [Unknown error attempting to reach phone](https://repost.aws/knowledge-center/sns-unknown-error-phone-sms "https://repost.aws/knowledge-center/sns-unknown-error-phone-sms").

- Take note of the special requirements and regulations. See [Supported countries and regions (SMS channel)](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") in the _AWS End User Messaging SMS User Guide_, and
  confirm that these requirements are being met.

## Two-way SMS troubleshooting

Two-way SMS responses are not received on either the SNS topic, subscribers, or both.

###### **Issues and solutions**

- Verify that you have a number with two-way SMS enabled for a country where the feature is
  supported. See [Supported countries and regions (SMS channel)](../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-by-country.md") and [Two-way SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md") in the _AWS End User Messaging SMS User Guide_.
- Verify that the sender number is from the same country as the two-way SMS-enabled number
  in Amazon Pinpoint.
- Verify that the users' number is a valid mobile number and not a virtual number by using
  the [Amazon Pinpoint Phone Number validator API](../developerguide/validate-phone-numbers.md "../developerguide/validate-phone-numbers.md"). Communication
  between two virtual numbers, like the ones in Amazon Pinpoint, will be attempted at a
  maximum effort.
- Review [Amazon SNS CloudWatch metrics](../../../sns/latest/dg/sns-monitoring-using-cloudwatch.md#sns-metrics "../../../sns/latest/dg/sns-monitoring-using-cloudwatch.md#sns-metrics") for
  `NumberOfMessagesPublished`,
  `NumberOfNotificationsDelivered`, and
  `NumberOfNotificationsFailed` to verify if the Amazon SNS topic is
  able to receive the inbound SMS.
  - If there are data points for `NumberOfMessagesPublished` at the time of the
    inbound SMS timestamps, then the recipient response was successfully
    received from downstream. Enable logging on
    the Amazon SNS topic for the delivery protocol being used. See [Amazon SNS message delivery status](../../../sns/latest/dg/sns-topic-attributes.md "../../../sns/latest/dg/sns-topic-attributes.md").
  - If there are no data points for the `NumberOfMessagesPublished` metric at the
    time of the inbound SMS timestamps:
    - Review the Amazon SNS topic policy to confirm that it allows the Amazon Pinpoint service to publish
      to the Amazon SNS topic. For an example policy, see [Two-way SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md") in the _AWS End User Messaging SMS User Guide_.
    - If the Amazon SNS topic linked to the two-way SMS number is
      encrypted:
      - Verify that the key used is symmetric.
      - Verify that the key policy is modified to allow Amazon Pinpoint to use the key, see [Amazon SNS topic policies for Amazon SNS topics](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md#phone-number-two-way-sms-iam-policy-auto "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md#phone-number-two-way-sms-iam-policy-auto") in the _AWS End User Messaging SMS User Guide_.
