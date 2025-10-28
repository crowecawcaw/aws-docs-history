**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Amazon Pinpoint channels

A _channel_ represents the platform through which you engage your
audience segment with messages. For example, to send push notifications to users of your
apps, you must have an Amazon Pinpoint project in which the _push notifications_
channel is enabled. Amazon Pinpoint supports the following channels:

- [Push notifications](channels-push.md "channels-push.md")
- [Email](channels-email.md "channels-email.md")
- [SMS](channels-sms.md "channels-sms.md")
- [Voice](channels-voice.md "channels-voice.md")
- In-app messages
  In addition to these channels, you can also extend the capabilities to meet your specific
  use case by creating [custom channels](channels-custom.md "channels-custom.md").

Before you can use Amazon Pinpoint to engage your audience, you have to create an Amazon Pinpoint project.
After you create a project, you can use it to send campaigns. To engage your customers using
campaigns, start by [defining the audience segment](segments.md "segments.md") that you
want to engage. Next, [define that campaign](campaigns.md "campaigns.md") that you want to
send to the segment.

###### Topics in this section

- [Amazon Pinpoint push notifications](channels-push.md "channels-push.md")
- [Amazon Pinpoint email channel](channels-email.md "channels-email.md")
- [Amazon Pinpoint SMS channel](channels-sms.md "channels-sms.md")
- [Amazon Pinpoint voice channel](channels-voice.md "channels-voice.md")
- [Amazon Pinpoint in-app messaging channel](channels-inapp.md "channels-inapp.md")
- [Custom channels in Amazon Pinpoint](channels-custom.md "channels-custom.md")
