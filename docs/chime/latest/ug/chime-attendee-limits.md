# Meeting size limits

A maximum of 250 attendees can join Amazon Chime meetings scheduled by users with Amazon Chime Pro permissions. If you want to use auto-call, you must include
`meet@chime.aws` in the meeting invite.

However, meeting invitations can include a maximum of 300 attendees. Amazon Chime supports that number because some attendees decline
the meeting, some don't join the meeting, and some drop out of the meeting.

Auto-call doesn't count as an attendee. Distribution lists count as single attendees unless you expand them. Also, you must expand distribution lists if you want to use auto-call.

If you invite more than 300 individual users:

- Amazon Chime disables auto-call and notifies the meeting organizer.
- Attendees must join the meeting manually at the scheduled time.
- Attendess do not see the meeting name or scheduled ending time.
- The **Attendees** panel and its subsections, such as **Invited** and **dropped**, can
  display a combined maximum of 300 items. If the panel reaches the 300-item limit, or 250 attendees connect to the meeting, new attendees receive a "meeting
  full" notice and can't join the meeting.
  For more information about running large meetings, see
  [Conducting large meetings using Amazon Chime](https://answers.chime.aws/articles/1062/conducting-large-meetings-using-amazon-chime.html "https://answers.chime.aws/articles/1062/conducting-large-meetings-using-amazon-chime.html"), on the **Amazon Chime Help Center**.
  For more information about using auto-call, see [Using auto-call](chime-scheduling-best-practices.md#autocall "chime-scheduling-best-practices.md#autocall"), later in this section. For more information about the
  various Amazon Chime permissions, see the [Amazon Chime pricing page](https://aws.amazon.com/chime/pricing "https://aws.amazon.com/chime/pricing").
