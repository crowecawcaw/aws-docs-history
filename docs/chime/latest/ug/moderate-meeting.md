# Scheduling moderated meetings

Meeting hosts and delegates with Pro permissions can schedule moderated meetings,
which only start when a moderator joins. Until a moderator joins, moderated meeting
attendees cannot interact with each other. The audio, video, screen sharing, meeting
chat, and visual roster remain unavailable. After moderated meetings start, those
features become available until the meeting ends, even if the moderators leave the
meeting.

By default, meeting hosts and delegates have moderator permission, and a meeting can have more than one moderator. Hosts and delegates can share the moderator passcode with other attendees,
and they can also join the meeting as moderators. When they do, they can lock, record, and end meetings, and mute all other attendees. For more information, see
[Moderator actions using the Amazon Chime app](#actions-app "#actions-app") and [Moderator actions using phone or in-room video systems](#actions-phone-vid "#actions-phone-vid").

###### Topics

- [Joining a meeting as a moderator](#mod-join "#mod-join")
- [Scheduling a moderated meeting](#schedule-mod-mtg "#schedule-mod-mtg")
- [Moderator actions using the Amazon Chime app](#actions-app "#actions-app")
- [Moderator actions using phone or in-room video systems](#actions-phone-vid "#actions-phone-vid")

## Joining a meeting as a moderator

To join a meeting, moderators enter the moderator passcode. Moderators can enter the
passcode via phone, supported in-room video systems, or the Amazon Chime desktop client, web app, or mobile app.
When meeting hosts or delegates join while signed in to the desktop client, they automatically connect to the meeting as moderators without having to enter
the moderator passcode.

###### Note

Alexa for Business doesn't support joining a meeting as a moderator.

## Scheduling a moderated meeting

Schedule moderated meetings from the Amazon Chime app.

###### To schedule a moderated meeting

1. From the Amazon Chime app, choose **Meetings**, **Schedule a meeting**.
2. In the **Meeting scheduling assistant**, select **Generate a new ID and require moderator to start**.
3. Enter a 4-8 digit moderator passcode.
4. Finish selecting your other meeting options.
5. Choose **Copy moderator info** to copy and paste the moderator information for your moderated meeting.
6. Send the moderator information to the attendees who will moderate the meeting. To protect the moderator passcode, the Amazon Chime meeting invite doesn't contain moderator information.
   You must send that information to moderators separately.

###### Note

You can't add or change the moderator passcodes for an existing meeting. If you forget the moderator passcode, reschedule the meeting with a new meeting ID and passcode.

If you use one of the Amazon Chime Outlook Add-Ins, to schedule a moderated meeting,
select **Generate a new ID and require moderator to start** and
enter a moderator passcode. Send the moderator passcode to one or more attendees who
will act as moderators.

Attendees who have the moderator passcode can become moderators by entering the
passcode after they join the meeting. To enter the moderator passcode during a
meeting in progress, choose **More** from the Amazon Chime app, then
choose **Enter moderator passcode**.

## Moderator actions using the Amazon Chime app

If moderators sign in to a moderated meeting using any of the Amazon Chime apps, those
moderators can perform the same actions as meeting hosts and delegates. For a list
of available actions, see [Hosting meetings](chime-organizer-call-controls.md "chime-organizer-call-controls.md").

If a moderator joins a moderated meeting without signing in, they can use the
following subset of host actions:

- Mute all other attendees.
- Start and stop recording the meeting.
- Lock and unlock the meeting.
- End the meeting for all attendees.

## Moderator actions using phone or in-room video systems

When joining a moderated meeting over the phone or an in-room video
system, moderators can perform the following additional meeting actions from the
dial pad:

- Mute all other attendees – \*97
- Start and stop meeting recording – \*2

###### Note

If you use a phone or in-room conferencing system to start recording, the host receives the recording by default.

- Lock and unlock meeting – \*4
- End meeting for all – ##
- See menu (in-room video system only) – \*0

Any meeting attendee, including moderators, can press \*7 to mute and unmute themselves.
