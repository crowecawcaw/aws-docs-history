# Scheduling best practices

No matter which app you use to schedule your Amazon Chime meeting, these tips
can help you schedule meetings.

## Creating a personalized link

When you create an account with Amazon Chime, you receive a 10-digit Personal Meeting ID.
To make it easier for attendees to join your meetings, you can create a personalized
link. For more information, see [5. (Optional) Set a personalized meeting link](set-link.md "set-link.md").

## Helping mobile users join your meeting

When inviting mobile users to your meeting, copy and paste the **One-click
Mobile Dial-in** into the **Location** field of your
meeting invite. When a calendar reminder appears for a meeting on their mobile
devices, they can choose the string to dial in automatically.

## Using auto-call

When your meeting starts, Amazon Chime can call every attendee automatically on all
registered devices with auto-call. You and your attendees don’t have to watch the
calendar to join the meeting.

To use auto-call, add `meet@chime.aws` to the list of
invitees when you schedule a meeting.

You can remove **meet@chime.aws** from the meeting invite to
avoid having everyone’s devices ring at the same time. For example, when everyone is
in the same office. You can also remove **meet@chime.aws** if your
attendees would rather open the invite and choose the meeting link.

###### Note

- Auto-call doesn't work if the meeting invitation contains a distribution list, such as myteam@amazon.com.
  Make sure to use the email addresses of individual attendees.
- The system mutes auto-calls for users who set their Amazon Chime status to **Do not disturb**.

## Inviting large numbers of attendees quickly

You can invite up to 300 people to an Amazon Chime meeting. To add a large number of people quickly, you invite **meet@chime.aws** and a distribution list, if one exists. You then
expand the distribution list. That adds each attendee separately and enables auto-calling.

###### To invite a distribution list

1. Follow any of the steps listed earlier in this section to create an Amazon Chime meeting. As a best practice, use a unique meeting ID, or an ID with a moderator passcode. Doing so generates a PIN
   that attendees can use to join the meeting.
2. Add the distribution list to the invite.
3. Expand the distribution list.
4. Add or remove attendees as needed.
5. Set the date, time, and any recurrence.
6. Edit the meeting instructions as needed.
7. Send the invitation.

## Inviting a distribution list without auto-calling

If you need to schedule a meeting with a large team, you can invite the team's distribution list. However, doing so prevents Amazon Chime from auto calling when the meeting starts.

###### To invite a distribution list

1. Follow any of the steps listed earlier in this section to create an Amazon Chime meeting. As a best practice, use a unique meeting ID, or an ID with a moderator passcode. Doing so generates a PIN
   that attendees can use to join the meeting.
2. Add the distribution list to the invite.
3. Delete **meet@chime.aws**, but leave the PIN that the system adds.
4. Set the date, time, and any recurrence.
5. Edit the meeting instructions as needed.
6. Send the invitation.

Attendees can choose the meeting link in the instructions, then choose
**Meetings**, **Join a Meeting**, and enter
the PIN manually.

## Changing meeting details

When changing meeting details or adding `meet@chime.aws` to an existing meeting,
remember to choose **Send Updates to All**.
