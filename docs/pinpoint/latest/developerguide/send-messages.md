

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Send transactional messages from your app using Amazon Pinpoint
<a name="send-messages"></a>

You can use the Amazon Pinpoint API and the AWS SDKs to send *transactional messages* directly from your app. Transactional messages are messages that you send to specific recipients, as opposed to messages that you send to segments. There are several reasons that you might want to send transactional messages rather than campaign-based messages. For example, you can send an order confirmation by email when a customer places an order. You could also send a one-time password by SMS or voice that a customer can use to complete the process of creating an account for your service.

This section includes example code in several programming languages that you can use to start sending transactional emails, SMS messages, and voice messages.

For more code examples on endpoints, segments, and channels see [Code examples](https://docs.aws.amazon.com/pinpoint/latest/developerguide/service_code_examples.html).

**Topics**
+ [Send transactional emails using Amazon Pinpoint](send-messages-email.md)
+ [Send transactional SMS messages using Amazon Pinpoint](send-messages-sms.md)
+ [Send voice messages using Amazon Pinpoint](send-messages-voice.md)