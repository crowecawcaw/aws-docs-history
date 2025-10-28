**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Pause, resume, or stop a journey

## Pausing a journey

After publishing a journey, you can pause that journey. During a paused journey, messages
aren't sent and analytics data isn't generated. You can pause a journey during holidays,
or if you need to re-evaluate the journey itself for changes. Any endpoints that entered
the journey before the pause will complete the journey and are then paused. Any
endpoints waiting to enter the journey don't enter the journey during the pause. If a
journey is in a **Wait** activity, the timer on the
**Wait** activity is paused. After the journey is resumed, the
**Wait** activity continues from the point at which it was paused.
A paused journey cannot be edited.

###### To pause a journey

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. For **All Projects**, choose an existing project.
3. In the navigation pane, choose **Journeys**.
4. Choose a currently published journey.
5. In the upper-right corner of the published journey's workspace, choose
   **Actions**.
6. Choose **Pause**.
7. When prompted to confirm pausing the journey, choose
   **Pause**.

A paused journey stays paused indefinitely until you resume it.

## Resuming a journey

A paused journey can only be resumed after five minutes have passed. When you resume a
paused journey, participants resume traveling through the journey from the point they
were at when the journey was paused. If any journeys were in a **Wait**
activity, the **Wait** activity countdown resumes from the point at
which the journey was paused.

###### To resume a journey

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. For **All Projects**, choose an existing project.
3. In the navigation pane, choose **Journeys**.
4. Choose a currently paused journey.
5. In the upper-right corner of the paused journey's workspace, choose
   **Actions**.
6. Choose **Resume**.
7. When prompted to confirm resuming the journey, choose
   **Resume**.

The journey resumes.

## Stopping a journey

Stopping a journey permanently ends the journey and all activities associated with it. Any
activities that are currently in-process are ended. However, you will still be able to
view analytics data.

###### Tip

If you are unsure whether to stop a journey, consider pausing instead. Because a stopped
journey is stopped permanently, you must recreate the journey to use it
again.

###### To stop a journey

1. Sign in to the AWS Management Console and open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. For **All Projects**, choose an existing project.
3. In the navigation pane, choose **Journeys**.
4. Choose a currently published journey.
5. In the upper-right corner of the journey workspace, choose
   **Actions**.
6. Choose **Stop**.
7. When prompted to confirm stopping the journey, choose **Stop
   journey**.

The journey permanently stops.

**Next**: [View journey metrics](journeys-metrics.md "journeys-metrics.md")
