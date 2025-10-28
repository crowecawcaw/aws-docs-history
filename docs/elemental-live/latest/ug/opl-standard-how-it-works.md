# How output locking

works

This section shows how Elemental Live locks outputs when an event first
starts, and how resync works when an event is running.

Output locking has these key requirements:

- All inputs must have a timecode in the source. You can't set up output locking in
  events that use the system clock.
- The events must be able to communicate with each other over
  multicast or unicast.
  **How the initial lock occurs**

When you start or restart all of the events, one event is designated as the leader.
Subsequent events are followers. At the first segment boundary, each follower uses its own
timecode and the leader's timecode to align the frame that it emits with the frame that the
leader is emitting. The events are now all locked together.

**How resynchronization works**

Elemental Live continually checks the timecode for the same segment in all the locked
events. If the segment in one event has a different timecode, then it is considered to be out
sync.

Elemental Live resynchronizes the output of an event by inserting a short segment and a
presentation timestamp (PTS) discontinuity tag.

Keep this detect-and-correct behavior in mind. Output locking doesn't
guarantee that output always staty in sync. Rather, the guarantee is that
when a drift occurs, Elemental Live resynchronizes.

**Inability to detect and
correct**

As the event runs, there might be times when the event can't detect and correct. For
example, if the current source doesn't include a timecode because it is slate content.

Even in this case, Elemental Live continues to attempt to synchronize. For example, if the
content changes so that a timecode is present again in the source, then Elemental Live will
resync again.
