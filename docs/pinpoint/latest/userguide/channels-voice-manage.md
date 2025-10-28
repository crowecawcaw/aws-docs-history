**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Managing the Amazon Pinpoint voice channel

You can use the Amazon Pinpoint console to enable the voice channel for a project and to manage
settings that apply to the voice channel for your Amazon Pinpoint account. For example, you can
request production access for your account, or request dedicated phone numbers for sending
voice messages.

## Enabling the voice channel

Before you can use Amazon Pinpoint to send voice messages, you must enable the voice channel
for one or more projects. To learn how to create a new project and enable the voice
channel for it, see [Setting up the Amazon Pinpoint voice channel](channels-voice-setup.md "channels-voice-setup.md"). To enable the voice channel for an
existing project, complete the following steps.

Note that the settings that you choose for the voice channel also apply to the SMS
channel for the project. If you want to send both voice and SMS messages from the
project, choose settings that support your goals for both channels. To learn more, see
[Amazon Pinpoint SMS channel](channels-sms.md "channels-sms.md").

###### To enable the voice channel for an existing project

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to enable the voice channel for.
3. In the navigation pane, under **Settings**, choose
   **SMS and voice**.
4. On the **SMS and voice** page, next to **SMS
   settings**, choose **Edit**.
5. Select **Enable the voice channel for this project**.
6. Choose **Save changes**.
7. On the **SMS and voice** page, under **Number
   settings**, refer to the table to determine whether any phone
   numbers that are already associated with your account can be used to send voice
   messages. If there are, the **Voice** column displays
   **Enabled** next to each phone number that you can use to
   send voice messages. If there aren't, [Request a phone number](../../../sms-voice/latest/userguide/phone-numbers-request.md "../../../sms-voice/latest/userguide/phone-numbers-request.md") in the _AWS End User Messaging SMS User Guide_.
