**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Supported Amazon Pinpoint SMS and voice API version

1 actions in CloudTrail log files

The Amazon Pinpoint SMS and Voice version 1 API supports logging the following actions as events
in CloudTrail log files:

- [CreateConfigurationSet](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.md#v1-sms-voice-configuration-setspost "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets.md#v1-sms-voice-configuration-setspost")
- [CreateConfigurationSetEventDestination](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinationspost "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinationspost")
- [DeleteConfigurationSet](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname.md#v1-sms-voice-configuration-sets-configurationsetnamedelete "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname.md#v1-sms-voice-configuration-sets-configurationsetnamedelete")
- [DeleteConfigurationSetEventDestination](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnamedelete "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnamedelete")
- [GetConfigurationSetEventDestinations](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinationsget "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinationsget")
- [UpdateConfigurationSetEventDestination](../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnameput "../../../pinpoint-sms-voice/latest/APIReference/v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationname.md#v1-sms-voice-configuration-sets-configurationsetname-event-destinations-eventdestinationnameput")
  The following Amazon Pinpoint SMS and Voice version 1 API action **isn't** logged in CloudTrail:

- SendVoiceMessage
