

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# Supported Amazon Pinpoint SMS and voice API version 1 actions in CloudTrail log files
<a name="pinpoint-sms-voice-cloudtrail-actions"></a>

The Amazon Pinpoint SMS and Voice version 1 API supports logging the following actions as events in CloudTrail log files:
+ [CreateConfigurationSet](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.html#v1-sms-voice-configuration-setspost)
+ [CreateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.html#v1-sms-voice-configuration-sets-configurationsetname-event-destinationspost)
+ [DeleteConfigurationSet](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname.html#v1-sms-voice-configuration-sets-configurationsetnamedelete)
+ [DeleteConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.html#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnamedelete)
+ [GetConfigurationSetEventDestinations](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.html#v1-sms-voice-configuration-sets-configurationsetname-event-destinationsget)
+ [UpdateConfigurationSetEventDestination](https://docs.aws.amazon.com/pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.html#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnameput)

The following Amazon Pinpoint SMS and Voice version 1 API action **isn't** logged in CloudTrail:
+ SendVoiceMessage