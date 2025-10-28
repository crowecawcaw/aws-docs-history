**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Troubleshooting the voice channel

For logging of Amazon Pinpoint voice messages, see [How do I set up logging for Amazon Pinpoint voice messages for Amazon Pinpoint SMS
and Voice v1 API?](https://repost.aws/knowledge-center/pinpoint-voice-message-logging-setup "https://repost.aws/knowledge-center/pinpoint-voice-message-logging-setup").

## Voice

###### **Issues and solutions**

- By default, the voice channel of an Amazon Pinpoint project is turned off. To see if
  voice is turned on for your project, select the
  **Settings** page under the project. Under
  **Features** for SMS and voice, you will see whether
  each of the two are turned off or turned on. While you can turn on SMS under
  the **Manage** option, you can turn on the voice channel by
  running the following command:

```
aws pinpoint update-voice-channel --application-id AppId --voice-channel-request Enabled=true
```

- TooManyRequests exception
  - If your account is in a sandbox, there's a 20-message limit over a 24 hour period. This
    limit can be increased by [Voice sandbox](../../../sms-voice/latest/userguide/sandbox.md#sandbox-voice "../../../sms-voice/latest/userguide/sandbox.md#sandbox-voice") in the _AWS End User Messaging SMS User Guide_.
  - Amazon Pinpoint voice channel has a hard limit of five messages per single recipient over a 24
    hour period. This limit is a hard limit that can't be increased.
