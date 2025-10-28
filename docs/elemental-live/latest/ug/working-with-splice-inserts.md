# Working with splice

inserts

Splice inserts inserted by the REST API are always of type “ad avail.”

You can:

- Insert a SCTE-35 ad avail of type splice_insert. See [Insert a new
  splice insert message](insert-a-new-splice-insert-message.md "insert-a-new-splice-insert-message.md").
- Get the timecode of the content that is currently being
  processed. This data
  can
  be useful
  to
  determine the start time you need to enter
  in the command. See [Get current time](get-current-time.md "get-current-time.md").
- Insert an end time in an ad avail. See [Insert an end time in an existing ad avail](insert-an-end-time-in-an-existing-ad-avail.md "insert-an-end-time-in-an-existing-ad-avail.md").
- Cancel a SCTE-35 ad avail that is pending (the start time has not yet been
  reached). See [Cancel a pending ad
  avail](cancel-a-pending-ad-avail.md "cancel-a-pending-ad-avail.md").

###### Effect of these commands

These commands modify the data stream as it is being encoded.

Their precise effect on other parts of the content depends on how
the event is set up, as described in earlier chapters of this guide.
So it depends on the Ad Avail mode, whether manifest decoration is
enabled, blanking and blackout are enabled, and whether passthrough
is enabled.

###### Topics

- [Insert a new
  splice insert message](insert-a-new-splice-insert-message.md "insert-a-new-splice-insert-message.md")
- [Get current time](get-current-time.md "get-current-time.md")
- [Insert an end time in an existing ad avail](insert-an-end-time-in-an-existing-ad-avail.md "insert-an-end-time-in-an-existing-ad-avail.md")
- [Cancel a pending ad
  avail](cancel-a-pending-ad-avail.md "cancel-a-pending-ad-avail.md")
