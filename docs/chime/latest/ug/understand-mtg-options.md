# Setting meeting options

When you schedule an Amazon Chime meeting, you can set or change the following options:

- Meeting IDs – You can choose several types of meeting IDs. Your choice can prevent back-to-back meetings from overlapping, block unwanted
  attendees, or set a moderator passcode.
- External users – You can allow or block attendees from outside your company, and control whether they can use video conference systems or phones
  to connect to a meeting.

###### Topics

- [Choosing a meeting ID](#choose-type "#choose-type")
- [Allowing external attendees](#allow-external "#allow-external")

## Choosing a meeting ID

When you schedule an Amazon Chime meeting, you start by choosing a meeting ID. The right type of ID can block unwanted users, prevent back-to-back meetings
from overlapping, and more.

- Generate a new ID – This option generates a unique
  meeting ID that you can use to host individual or recurring meetings. We
  recommend this external, confidential, overlapping, and back-to-back
  meetings. You can use as many unique IDs as needed. Also, a unique ID
  provides instructions for joining a meeting or meeting series. This
  helps prevent back-to-back meetings from merging if one runs overtime.
- Generate a new ID and require moderator to
  start – This option generates a new, unique meeting
  ID for a moderated meeting, and prompts you to assign a 4-8 digit
  moderator passcode to the ID. Moderated meetings start only when a
  moderator joins by entering the passcode. Moderators also have host
  controls. Meeting hosts and delegates who sign in to the Amazon Chime client
  when they join the meeting become moderators by default. When joining
  over a phone or an in-room conference system, hosts and delegates can
  join as moderators by entering their 13-digit meeting ID. For more
  information, see [Scheduling moderated meetings](moderate-meeting.md "moderate-meeting.md").
- My personal meeting ID – This option generates meeting
  instructions using the meeting ID assigned to you when you registered
  for Amazon Chime. We recommend this for internal meetings, and you can use it
  for individual or recurring meetings. If you set up a personalized
  meeting link, it's included in the meeting instructions sent to your
  attendees. For more information, see [5. (Optional) Set a personalized meeting link](set-link.md "set-link.md"). This type of meeting starts as soon as
  anyone joins. Because this meeting type is more open, don't use personal
  meeting IDs for confidential or back-to-back meetings. To limit access
  to your meeting, select one of the other meeting types.

## Allowing external attendees

After you select a meeting ID, you choose whether to allow other external
attendees to join your meetings. Select one or more of the following attendee access
options:

- Attendees outside of my company who are signed in –
  Allows external attendees to join your meeting, but only if they sign in to
  Amazon Chime. These attendees skip the waiting room and join the meeting directly.

If you clear this checkbox, external attendees who sign in will go to the waiting room.

- Anyone with the meeting ID – Allows anyone to join your
  meeting if they have the meeting ID. This option allows attendees without
  registered Amazon Chime accounts to join.
- In-room video systems – Allows any in-room video system to join your meeting if the attendee has the meeting ID.

Clearing this options blocks in-room systems from the meeting.

- Dial-in – Allows anyone with the meeting ID to dial in
  to the meeting.

###### Note

Attendees from your company can always join
your meetings. Invited attendees can also join, but they must sign in to Amazon Chime using the email address in the
meeting invite. Also, you must add `meet@chime.aws` as a meeting attendee. For more information, see
[Using auto-call](chime-scheduling-best-practices.md#autocall "chime-scheduling-best-practices.md#autocall").
