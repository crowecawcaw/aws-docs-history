**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Editing a project's default settings

On the **General settings** page, you can configure default settings
and quotas that you want to apply to campaigns and journeys in a project. When you
change these settings, Amazon Pinpoint automatically applies them to all new campaigns and
journeys that you create for the project. The settings aren't applied to any campaigns
or journeys that you previously created. You can also configure these same settings for
individual campaigns and journeys. If you configure settings for an individual campaign
or journey, those settings override the settings that you choose on the
**General settings** page.

###### To configure default settings for a project

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose the project that you
   want to change the default settings for.
3. In the navigation pane, under **Settings**, choose
   **General settings**.
4. Choose **Edit**.
5. On the **Edit general settings** page, change any of the
   following settings:
   1. _Campaign settings_

   **Quiet time hours**

   Use these settings to prevent Amazon Pinpoint from sending messages
   during specific hours. When you configure these settings,
   you provide a **Start time** and an
   **End time**. If a message would be
   sent between the start and end times in an endpoint's local
   time zone, Amazon Pinpoint doesn't attempt to send the message to that
   endpoint.

   ###### Note

   In order for this setting to observe local time zones,
   the endpoint definition for a recipient has to include a
   properly-formatted `Demographic.Timezone`
   attribute.

   The times that you specify must use 24-hour notation and
   be in _HH:MM_ format. For example, for
   9:30 PM, enter `21:30`.

   **Maximum number of daily messages per
   endpoint**

   Use this setting to specify the maximum number of messages
   that can be sent to a single endpoint during a 24-hour
   period by all the campaigns in the project. The value that
   you specify can't be larger than 100.

   ###### Note

   In certain situations, it's possible for an endpoint
   to receive a number of messages that exceed the value
   that you specify in this setting. For example, assume
   that this setting is configured to send a maximum of
   five messages per day. If you have 10 campaigns that
   target the endpoint, and all 10 are launched at the same
   time, then the endpoint receives 10 messages. However,
   if there are 10 campaigns that target the endpoint, and
   the start times for the campaigns are separated by
   several minutes, then the recipient only receives five
   messages.

   **Maximum number of messages per
   endpoint**

   Use this setting to specify the maximum number of messages
   that can be sent to a single endpoint by each campaign. If a
   campaign recurs, this setting applies to all runs of the
   campaign. The value that you specify can't be larger than 100.

   ###### Note

   This setting considers the number of messages that
   _target_ an endpoint, as opposed
   to the number of messages that are actually
   _delivered_ to an endpoint. For
   example, if a campaign is configured to automatically
   send a message when a customer creates a new account,
   but the endpoint isn't able to receive the message (for
   example, if the quiet time setting applies to the
   endpoint), then the endpoint is still counted as having
   been targeted. In this situation, the endpoint would be
   removed from subsequent runs of the campaign.

   **Maximum number of messages per
   second**

   Use this setting to specify the maximum number of messages
   that can be sent each second by a campaign. The value that
   you specify has to be a number between 1 and 20,000. If you
   define a messages per second parameter, we try to match it.
   Otherwise, if this isn't defined, we attempt to deliver the
   message as fast as possible. Note that delivery speed,
   however, is dependent on channel latency at any given
   time.

   **Maximum amount of time for a campaign
   run**

   Use this setting to specify the maximum amount of time, in
   seconds, that a campaign can attempt to deliver a message
   after the scheduled start time. The minimum value for this
   setting is 60 seconds. 2. _Journey settings_

   **Maximum daily messages per endpoint across all
   journeys**

   Use this setting to specify the maximum number of times in
   a 24 hour period that an endpoint can be messaged across all
   journeys. The default value is zero and means that there is
   no limit on the number of times an endpoint can be messaged
   in a 24 hour period.

   **Maximum number of messages across all journeys
   within a time frame**

   Use this setting to specify the maximum number of times a
   message can be sent to a single endpoint within the
   specified **Timeframe**. For example, if
   you want to send a maximum of three messages within a
   **Timeframe** of seven days to each
   endpoint. The default setting is 0, which means that there
   is no limit on the number of messages that endpoints in the
   journey can receive.

   **Timeframe**

   The number of days applied to the **Maximum number
   of messages across all journeys within a time
   frame** if not set to 0. The default setting is
   0, which means that there is no limit on the number of days
   that endpoints in the journey can receive.

6. When you finish, choose **Save**.
