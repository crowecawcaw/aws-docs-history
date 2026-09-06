

# Canceling meetings
<a name="cancel-meeting"></a>

If you schedule meetings for yourself, or you schedule them as a delegate for someone else, you can cancel your meetings. You can cancel individual and recurring meetings, including meetings that continue to auto call after you cancel them.

**Topics**
+ [Canceling individual meetings](#cancel-individual-meeting)
+ [Canceling recurring meetings](#cancel-recurring-meeting)
+ [Removing yourself from a recurring meeting that you don't own](#remove-self-not-organizer)

## Canceling individual meetings
<a name="cancel-individual-meeting"></a>

If you use a calendar application to create an individual meeting, you use that same app to cancel the meeting. If your calendar app prompts you, send the cancellation to all attendees.

We assume that you know how to use your calendar app to do that task.

## Canceling recurring meetings
<a name="cancel-recurring-meeting"></a>

If you use a calendar app to create a recurring meeting, you use that app to cancel the meeting. Make sure you send the cancellation to **meet@chime.aws**. If your calendar app prompts you to do so, send the cancellation to all attendees.

**Note**  
Your calendar app needs to send an iCalendar (.ics) file to **meet@chime.aws** to cancel the meeting. However, some calendar apps don't send ICS files. As a result, Amazon Chime may auto-call attendees even though the meeting doesn't appear on their calendars. When that happens, you must cancel the meetings during a specific timeframe. You can cancel meetings from 30 minutes before they start until they reach their scheduled end time or someone ends the meeting. You must wait for that timeframe.

**To cancel a recurring meeting during the window**

1. In the desktop client or web app, choose **Home**.

1. A list of **In progress meetings** and **Upcoming meetings**—meetings starting in the next 30 minutes—appears.

1. Select a meeting that you host, then choose **Delete meeting series**.

1. When prompted, confirm the deletion.

1. Amazon Chime ends the meeting for all attendees, if it has already started. The host and invited attendees won’t receive auto-calls for that meeting.

## Removing yourself from a recurring meeting that you don't own
<a name="remove-self-not-organizer"></a>

You own a meeting when you create and host that meeting, or when you have a delegate create the meeting for you. To remove yourself from a recurring meeting that you don't own, follow the steps in [ Removing yourself from a recurring meeting ](https://docs.aws.amazon.com/chime/latest/ug/remove-recurring.html). 