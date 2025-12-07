# Create a multi-step and multi-channel journey

On the Outbound Campaigns page, you will have two options to create an outbound campaigns:
Visual Journey Builder for multi-channel and multi-steps using an intuitive drag-and-drop canvas,
or Guided Campaign Builder to create a single-channel with step-by-step guidance.

1. From the **Outbound Campaigns** page, choose **Create Journey**.
2. Enter a journey **Name**.
3. Select a Customer Segment or Customer event to use for this journey. Recipients for the
   journey will be determined at the journey's scheduled start time using the chosen segment or
   customer event.
4. To connect with a journey, first create a **journey flow** that supports multi-step
   experiences triggered by events or audience segments, then select the flow you want to connect
   to this journey.
5. If you haven’t created a journey flow yet, you can click “create journey flow” and
   will take you to the flow canvas. Please refer to **Journey flow blocks definition** for details.
6. If the selected journey flow has voice channel, you will use the
   **Voice setup** option to define the details.
7. You can choose Agent assisted voice or automated voice and complete the channel
   configuration. Please refer to details on
   [Outbound campaigns channel
   configurations](how-to-create-campaigns.md#create-campaigns-channel-configurations "how-to-create-campaigns.md#create-campaigns-channel-configurations").

## Delivery guardrails

###

You can control how often each recipient is contacted by setting communication limits for
the Journey. Simply specify the maximum number of messages a recipient can receive within a
defined time frame (e.g., per day, week, or month). If a recipient has already received the
maximum number of communications within any of the time frames you set, Amazon Connect Outbound
Campaigns will automatically skip that recipient and they won’t receive additional messages
from the Journey.

**Example:**

If you set a limit of 4 communications per 2 days and 6 communications per 2 weeks (14
days), any recipient who has already received 4 messages in the last 2 days or 6 messages in
the last 14 days will not be contacted again by this Journey.

Amazon Connect Outbound Campaigns
considers any time a recipient has been contacted, regardless of the recipients interaction
with the message, as a communication. For example, a phone call ending in a voicemail is still
considered a communication. Amazon Connect Outbound Campaigns will adjust the count of
communications if it can determine that the message never reached the end user, and will always
err on the side of over-counting. In addition to setting communication limits for individual
journeys, you can also define **Total Communication Limits** at the instance level. These limits
control how many messages a recipient can receive across all journeys running within your
Amazon Connect instance over a specific time frame. If a recipient reaches the specified
limit—for example, 10 communications per week—they will be excluded from further messaging
across **all journeys** until the time window resets. This helps ensure that overall message volume
stays within acceptable boundaries.

For **critical journeys**, you have the option to
**opt out** of
total communication limits by enabling the **Ignore total limits** setting. This allows these
journeys to bypass the instance-wide limits, ensuring important messages are delivered without
being blocked by other ongoing journeys.

###### Note

The total count of messages across journeys will not necessarily be incremented
immediately, but will eventually be accurate. For example, if two journeys target the same
user at the same moment in time, the first journey's communication may not be reflected in the
total communication count by the time the second campaign checks.

All communications across
all journeys in the active state are considered when determining if a recipient has breached
their total limits.

Amazon Connect Outbound Campaigns measures a day as a rolling 24 hour
window from the current moment.

Any communications sent from a journey that
**ignores total limits** will not count toward the instance's total communication limits. These journeys are
treated as **outside the scope** of instance-level limits.

### Communication time

You can specify valid times to attempt to contact your users. The **Active communication time**
specifies those valid times, based on the day of the week.
**Exceptions to communication**
time, an optional setting, specifies specific days of the year during which you want no
communications sent, even if that day happens to fall in an active communication time.

#### Time zone

In order for the Journey to determine appropriate time to attempt communication with a
particular recipient, you need to provide a
**Time Zone**. You may either select a **Standard time
zone**, which will be used for all recipients, or you may specify the
**Recipient's local time zone**. Recipients with no time zone specified are excluded from message deliveries.

- Standard
  time zone: The time zone selected will be used for all recipients. Select this option if you
  know the time zone of all recipients in your segment or if you want all communications sent at
  the same moment in time.
- Recipient's local time zone: Amazon Connect Outbound Campaigns use the provided Address
  and/or the area code from the Phone Number to infer the recipients time zone. If the time
  zone cannot be determined (for example, if either the [Address](../APIReference/API_connect-customer-profiles_CreateProfile.md#connect-connect-customer-profiles_CreateProfile-request-Address "../APIReference/API_connect-customer-profiles_CreateProfile.md#connect-connect-customer-profiles_CreateProfile-request-Address") and/or [Phone Number](../APIReference/API_connect-customer-profiles_CreateProfile.md#connect-connect-customer-profiles_CreateProfile-request-PhoneNumber "../APIReference/API_connect-customer-profiles_CreateProfile.md#connect-connect-customer-profiles_CreateProfile-request-PhoneNumber") is missing
  or is invalid), the recipient will be dropped from the Journey. Select this option if it's
  important to send communications to recipients only during their specific local
  times.

#### Active communication time (optional)

The **Active communication time** represents the times during which
Amazon Connect Outbound campaigns may send communications for this journey. To add active
communication times: Select the channel. Alternatively, select Apply to all channels to apply
the active communication times to each channel. Select the day of the week to configure. You
can add multiple active communication times for each day, if desired. Select the time frame
during which Amazon Connect Outbound campaigns can send communications on the given day.

#### Exceptions to communication time

(optional)

**Exceptions to communication time** is an optional set of specific calendar days for which
you do not want communications sent. If exceptions are included in the Journey, then active
communication times must also be specified. To add exceptions to communication time:

Select
the channel. Add a **Name** for the exception. This name is only for informational purposes and
does not affect the running of the journey. Select the
**Date range** for the exception.

### Review and publish

Take a moment to review your journey prior to publishing.

###### Important

These settings cannot be changed once your journey has been published.
Once you have reviewed you journey, choose
**Publish to Schedule** your journey.

#### Schedule journey

Specify when you want your journey to begin:

- **Start now**: Start the journey right away.
- **Start later**: Select the specific day and time for the journey to
  begin.
- **Expiry Date and Time**: The date and time at which Amazon Connect
  Outbound campaigns should end the journey. An expired journey appears with a
  **Completed**
  status a few moments after expiry time. The start and end times of a journey that starts now
  or a journey that starts later are based on your local time zone.

#### Repeats

If you want your journey to repeat running, select the **Repeats** radio
button and choose a **Frequency**. Amazon Connect Outbound campaigns will then refresh
profiles in the segment specified for this journey at the same frequency you select. For
example, if you schedule your journey to start at 7:03AM EST and use a Daily Frequency, then
profiles will be refreshed in the segment daily at 7:03AM EST.

###### Important

A recipient may be active only in a journey once at any given time. So if they are still
waiting to exit the journey when the next Segment Snapshot is created, and are a member of
that Snapshot, they are **NOT** allowed to enter the journey as a part of the second Snapshot. If
a recipient is a part of a segment Snapshot and is not currently in the journey, they are
allowed to enter, regardless of whether they have previously gone through the journey.

Choose **Publish** to schedule your journey.
