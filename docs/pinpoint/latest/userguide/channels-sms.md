**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint SMS channel

###### Note

Amazon Pinpoint has updated their User Guide documentation. To get the latest information
regarding how to create, configure, and manage your SMS and voice resources, see the new
[AWS End User Messaging SMS User Guide](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md").

The following topic have been moved to the new [AWS End User Messaging SMS
User Guide](../../../sms-voice/latest/userguide/what-is-service.md "../../../sms-voice/latest/userguide/what-is-service.md").

- [About the SMS/MMS
  and Voice sandbox](../../../sms-voice/latest/userguide/sandbox.md "../../../sms-voice/latest/userguide/sandbox.md")
- [Choosing
  a phone number or sender ID](../../../sms-voice/latest/userguide/phone-number-types.md "../../../sms-voice/latest/userguide/phone-number-types.md")
- [SMS and MMS
  limits and restrictions](../../../sms-voice/latest/userguide/sms-limitations.md "../../../sms-voice/latest/userguide/sms-limitations.md")
- [Requesting
  support for SMS, MMS, and voice messaging](../../../sms-voice/latest/userguide/awssupport.md "../../../sms-voice/latest/userguide/awssupport.md")
- [Monitoring
  SMS, MMS, and voice spending activity with AWS End User Messaging SMS](../../../sms-voice/latest/userguide/monitor-spending.md "../../../sms-voice/latest/userguide/monitor-spending.md")
- [First time user tutorial](../../../sms-voice/latest/userguide/getting-started-tutorial.md "../../../sms-voice/latest/userguide/getting-started-tutorial.md")
- [Keywords](../../../sms-voice/latest/userguide/phone-numbers-keywords.md "../../../sms-voice/latest/userguide/phone-numbers-keywords.md")
- [Two-way SMS messaging](../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md "../../../sms-voice/latest/userguide/phone-numbers-two-way-sms.md")
- [SMS and MMS country capabilities and limitations](../../../sms-voice/latest/userguide/phone-numbers-sms-support-by-country.md "../../../sms-voice/latest/userguide/phone-numbers-sms-support-by-country.md")
- [Phone
  pools](../../../sms-voice/latest/userguide/phone-pool.md "../../../sms-voice/latest/userguide/phone-pool.md")
- [Best practices](../../../sms-voice/latest/userguide/best-practices.md "../../../sms-voice/latest/userguide/best-practices.md")
- [Understanding
  SMS billing and usage reports](../../../sms-voice/latest/userguide/sms-billing.md "../../../sms-voice/latest/userguide/sms-billing.md")
  You can use the SMS channel in Amazon Pinpoint to send SMS messages (text messages) to your
  customers' mobile devices. Amazon Pinpoint can send SMS messages to recipients in over 200 countries and regions. In some
  countries and regions, you can also receive messages from your customers by using the
  two-way SMS feature. When you create a new Amazon Pinpoint account, your account is placed in an SMS
  sandbox. This initially limits your monthly spending and who you can send messages to. For
  more information, see [SMS sandbox](../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms "../../../sms-voice/latest/userguide/sandbox.md#sandbox-sms") in the _AWS End User Messaging SMS User Guide_.

To send text messages using Amazon Pinpoint, you must [enable the
SMS channel in your project](channels-sms-setup.md "channels-sms-setup.md"). Depending on how you use Amazon Pinpoint to send SMS messages,
you might also need to initiate a request with
Support to enable or modify certain SMS options for your account. For example, you
can request to increase your SMS spending quota, to move from the sandbox to production, or
you can request a short code to use when sending and receiving messages.

To receive text messages using Amazon Pinpoint, you should first obtain a dedicated short code or long code. When you have a dedicated
number, you can enable two-way SMS for it.
Finally, you can specify the messages that Amazon Pinpoint sends to
customers when it receives incoming messages.

In the SMS and voice settings section of the Amazon Pinpoint
console, you can manage SMS channel settings for your use case and budget. For example, you
can set your monthly SMS spending quota, or change your default message type.

###### Note

When you configure SMS channel settings in Amazon Pinpoint, your changes apply to other
AWS services that send SMS messages, such as Amazon SNS.

###### Topics

- [Setting up the Amazon Pinpoint SMS channel](channels-sms-setup.md "channels-sms-setup.md")
- [Managing the Amazon Pinpoint SMS channel](channels-sms-manage.md "channels-sms-manage.md")
- [Message routes](channels-sms-limitations-routes.md "channels-sms-limitations-routes.md")
- [Message fallback](channels-sms-limitations-fallback.md "channels-sms-limitations-fallback.md")
- [Troubleshooting the SMS channel](channels-sms-troubleshooting.md "channels-sms-troubleshooting.md")
