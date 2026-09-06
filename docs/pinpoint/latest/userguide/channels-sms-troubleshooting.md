

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Troubleshooting the SMS channel
<a name="channels-sms-troubleshooting"></a>

Verify that logging is turned on to assist in identifying the cause of failure. For more information, see [Monitoring and logging](troubleshooting.md#troubleshooting-logging). To turn on logging for AWS End User Messaging SMS and Voice v2 API, see [How do I set up logging for Amazon Pinpoint voice messages for Amazon Pinpoint SMS and Voice v2 API?](https://repost.aws/knowledge-center/pinpoint-voice-message-logging-setup-v2). 

## SMS delivery failures
<a name="troubleshooting-sms-delivery-failures"></a>

****Issues and solutions****
+ Confirm that the number is valid using the [Amazon Pinpoint number validator](https://docs.aws.amazon.com/pinpoint/latest/developerguide/validate-phone-numbers.html). SMS delivery is only supported for ‘MOBILE’ phoneType. SMS delivery to ‘VOIP’ numbers is attempted on a best effort.
+ Confirm that your monthly SMS spend quota isn't depleted. For more information see [Monitoring SMS, MMS, and voice spending activity](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitor-spending.html) in the *AWS End User Messaging SMS User Guide*.
+ If the delivery issue is limited to one or two devices, then rule out device-related issues. Verify that the number(s) can receive SMS outside of Amazon Pinpoint at the time of the failure. 
+ Turn on SMS event logging to assist in identifying the cause of the failure.
  + Review the [message status](https://docs.aws.amazon.com/pinpoint/latest/developerguide/event-streams-data-sms.html#event-streams-data-sms-attributes-attrs).
  + Review how to resolve [Unknown error attempting to reach phone](https://repost.aws/knowledge-center/sns-unknown-error-phone-sms).
+ Take note of the special requirements and regulations. See [Supported countries and regions (SMS channel)](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) in the *AWS End User Messaging SMS User Guide*, and confirm that these requirements are being met.

## Two-way SMS troubleshooting
<a name="troubleshooting-sms-two-way"></a>

Two-way SMS responses are not received on either the SNS topic, subscribers, or both.

****Issues and solutions****
+ Verify that you have a number with two-way SMS enabled for a country where the feature is supported. See [Supported countries and regions (SMS channel)](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-by-country.html) and [Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-two-way-sms.html) in the *AWS End User Messaging SMS User Guide*. 
+ Verify that the sender number is from the same country as the two-way SMS-enabled number in Amazon Pinpoint. 
+ Verify that the users' number is a valid mobile number and not a virtual number by using the [Amazon Pinpoint Phone Number validator API](https://docs.aws.amazon.com/pinpoint/latest/developerguide/validate-phone-numbers.html). Communication between two virtual numbers, like the ones in Amazon Pinpoint, will be attempted at a maximum effort. 
+ Review [Amazon SNS CloudWatch metrics](https://docs.aws.amazon.com/sns/latest/dg/sns-monitoring-using-cloudwatch.html#sns-metrics) for `NumberOfMessagesPublished`, `NumberOfNotificationsDelivered`, and `NumberOfNotificationsFailed` to verify if the Amazon SNS topic is able to receive the inbound SMS. 
  + If there are data points for `NumberOfMessagesPublished` at the time of the inbound SMS timestamps, then the recipient response was successfully received from downstream. Enable logging on the Amazon SNS topic for the delivery protocol being used. See [Amazon SNS message delivery status](https://docs.aws.amazon.com/sns/latest/dg/sns-topic-attributes.html). 
  + If there are no data points for the `NumberOfMessagesPublished` metric at the time of the inbound SMS timestamps:
    + Review the Amazon SNS topic policy to confirm that it allows the Amazon Pinpoint service to publish to the Amazon SNS topic. For an example policy, see [Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-two-way-sms.html) in the *AWS End User Messaging SMS User Guide*. 
    + If the Amazon SNS topic linked to the two-way SMS number is encrypted:
      + Verify that the key used is symmetric. 
      + Verify that the key policy is modified to allow Amazon Pinpoint to use the key, see [Amazon SNS topic policies for Amazon SNS topics](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-two-way-sms.html#phone-number-two-way-sms-iam-policy-auto) in the *AWS End User Messaging SMS User Guide*. 