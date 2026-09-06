

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint SMS channel
<a name="channels-sms"></a>

**Note**  
Amazon Pinpoint has updated their User Guide documentation. To get the latest information regarding how to create, configure, and manage your SMS and voice resources, see the new [AWS End User Messaging SMS User Guide](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html).   
The following topic have been moved to the new [AWS End User Messaging SMS User Guide](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html).  
[About the SMS/MMS and Voice sandbox](https://docs.aws.amazon.com/sms-voice/latest/userguide/sandbox.html)
[Choosing a phone number or sender ID](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-number-types.html)
[SMS and MMS limits and restrictions](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-limitations.html)
[Requesting support for SMS, MMS, and voice messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/awssupport.html)
[Monitoring SMS, MMS, and voice spending activity with AWS End User Messaging SMS](https://docs.aws.amazon.com/sms-voice/latest/userguide/monitor-spending.html)
[First time user tutorial](https://docs.aws.amazon.com/sms-voice/latest/userguide/getting-started-tutorial.html)
[Keywords](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-keywords.html)
[Two-way SMS messaging](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-two-way-sms.html)
[SMS and MMS country capabilities and limitations](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-sms-support-by-country.html)
[Phone pools](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool.html)
[Best practices](https://docs.aws.amazon.com/sms-voice/latest/userguide/best-practices.html)
[Understanding SMS billing and usage reports](https://docs.aws.amazon.com/sms-voice/latest/userguide/sms-billing.html)

You can use the SMS channel in Amazon Pinpoint to send SMS messages (text messages) to your customers' mobile devices. Amazon Pinpoint can send SMS messages to recipients in over 200 countries and regions. In some countries and regions, you can also receive messages from your customers by using the two-way SMS feature. When you create a new Amazon Pinpoint account, your account is placed in an SMS sandbox. This initially limits your monthly spending and who you can send messages to. For more information, see [SMS sandbox](https://docs.aws.amazon.com/sms-voice/latest/userguide/sandbox.html#sandbox-sms) in the *AWS End User Messaging SMS User Guide*. 

To send text messages using Amazon Pinpoint, you must [enable the SMS channel in your project](channels-sms-setup.md). Depending on how you use Amazon Pinpoint to send SMS messages, you might also need to initiate a request with Support to enable or modify certain SMS options for your account. For example, you can request to increase your SMS spending quota, to move from the sandbox to production, or you can request a short code to use when sending and receiving messages. 

To receive text messages using Amazon Pinpoint, you should first obtain a dedicated short code or long code. When you have a dedicated number, you can enable two-way SMS for it. Finally, you can specify the messages that Amazon Pinpoint sends to customers when it receives incoming messages. 

In the SMS and voice settings section of the Amazon Pinpoint console, you can manage SMS channel settings for your use case and budget. For example, you can set your monthly SMS spending quota, or change your default message type.

**Note**  
When you configure SMS channel settings in Amazon Pinpoint, your changes apply to other AWS services that send SMS messages, such as Amazon SNS.

**Topics**
+ [Setting up the Amazon Pinpoint SMS channel](channels-sms-setup.md)
+ [Managing the Amazon Pinpoint SMS channel](channels-sms-manage.md)
+ [Message routes](channels-sms-limitations-routes.md)
+ [Message fallback](channels-sms-limitations-fallback.md)
+ [Troubleshooting the SMS channel](channels-sms-troubleshooting.md)