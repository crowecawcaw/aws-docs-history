# How epoch locking works

You can set up to use the epoch locking variation of output locking.
Or you can set up to use [standard output locking](opl-standard-how-it-works.md "opl-standard-how-it-works.md").

Epoch locking requires that all of the inputs have a timecode that is in the source. The
timecode must show the epoch time in UTC.

###### Note

We recommend against using epoch locking, for the following
reasons:

- Epoch locking requires that the sources have an epoch timecode.
  It might be difficult to arrange for this timecode to be inserted in
  the source.

- Epoch locking doesn't work well with ad insertion
  workflows.
  **How the initial lock occurs**

- When each event starts, the event uses its own source timecode to
  determine the sequence number and timecode to assign to the first
  segment and to every following segment:
  - The first sequence number is the number that would be assigned
    if the event had been running since the start of epoch time. For
    example, if the event output has segment lengths of 2.02 seconds,
    the first sequence number is the current epoch time divided by
    2.02.
  - The timecode for that sequence number is the current epoch
    time.

- The event can now predict the sequence numbers and timecodes for
  each segment:
  - The expected sequence numbers are predictable. They always
    increment by 1.
  - The expected timecode is predictable. It should increment by
    2.02 seconds in each segment.

- The event now locks to that expectation. As the event continues
  encoding, it continually compares the timecode of each sequence to the
  expected timecode.
- Every event locks in this way. They all lock to the epoch
  timecode, which means that in effect they are locked to each other.
  **How resynchronization works**

Each event checks the timecode for the current segment to the expected timecode. If it is
different, a drift has occurred. The event will resynchronize by inserting a short segment and
a presentation timestamp (PTS) discontinuity tag.

Keep this detect-and-correct behavior in mind. Output locking doesn't
guarantee that output never becomes out of sync. Rather, the guarantee is
that when a drift occurs, Elemental Live resynchronizes.

**Inability to detect and
correct**

As the event runs, there might be times when the event can't detect
and correct. For example, if the current source doesn't include a
timecode, perhaps because it is slate content.

Even in this case, Elemental Live continues to attempt to synchronize. For example, if the
content changes so that a timecode is present again in the source, then Elemental Live will
resync again.
