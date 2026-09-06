

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Amazon Pinpoint voice channel
<a name="channels-voice"></a>

**Note**  
Amazon Pinpoint has updated their user guide documentation. To get the latest information regarding how to create, configure, and manage your AWS End User Messaging SMS and voice resources, see the new [*AWS End User Messaging SMS User Guide*](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html).   
The following topics have been moved to the new [*AWS End User Messaging SMS User Guide*](https://docs.aws.amazon.com/sms-voice/latest/userguide/what-is-service.html).  
[Amazon Pinpoint voice sandbox](https://docs.aws.amazon.com/sms-voice/latest/userguide/sandbox.html#sandbox-voice)
[Supported countries and regions (voice channel)](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-numbers-voice-support-by-country.html)
[Managing Pools in Amazon Pinpoint](https://docs.aws.amazon.com/sms-voice/latest/userguide/phone-pool.html)
[Best practices for the voice channel](https://docs.aws.amazon.com/sms-voice/latest/userguide/best-practices.html#voice-best-practices)

You can use the voice channel to create voice messages from a text script, and then send those messages to your customers over the phone. The voice channel is a great way to reach customers whose phone numbers aren't able to receive SMS messages—for example, customers who use landlines or VoIP services.

To send voice messages using Amazon Pinpoint, you must first enable the voice channel in your project and lease a dedicated phone number for sending the messages. Depending on how you use Amazon Pinpoint to send voice messages, you might also want to change certain settings for your account. For example, you might want to request production access to increase the number of voice messages that you can send.

**Topics**
+ [Setting up the Amazon Pinpoint voice channel](channels-voice-setup.md)
+ [Managing the Amazon Pinpoint voice channel](channels-voice-manage.md)
+ [Troubleshooting the voice channel](channels-voice-troubleshooting.md)