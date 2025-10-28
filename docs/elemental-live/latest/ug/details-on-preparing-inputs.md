# Details on

preparing inputs

Read this section if your inputs are not being prepared as
expected.

## File inputs vs

live streaming inputs

- Preparing a live input involves a one-time
  inspection of the stream to determine what audio,
  video, and data tracks it holds and then continually
  decoding the frames. So: frame X gets decoded; the
  input does not become Active so frame X is
  discarded; frame Y gets decoded; the input does not
  become Active so frame Y is discarded; and so on
  decoding and discarding until finally the input does
  become Active.

As you can see, this preparation may be expensive
in terms of processing power.

- File inputs are automatically prepared just before
  they are Due-to-be-processed. Preparation of a file
  input involves decoding the first frame; after that,
  processing pauses until the input becomes
  Due-to-be-processed. Preparation of file inputs is
  not expensive.

## Rules for

preparing

- The input must not be currently Active.
- Only one input can be in the Prepared state at a
  time. If you manually prepare input A and then
  manually prepare input B before A becomes Active,
  input A will become unprepared.
- An input is put in the Prepared state only when
  the Prepare command is called on that input. So if a
  file input that is unprepared is
  Due-to-be-processed, it transitions directly to the
  Active state, where it gets both prepared and
  Active. This means that you can safely prepare a
  live input several inputs ahead of time, if you
  want.
- Timing of the manual prepare is important:
  - You should probably prepare a live input
    only when it is the Next-in-line.
  - You must prepare enough time in advance to
    allow Elemental Live to inspect the entire
    third input and decode at least one frame.
  - If the current input is quite long, you
    may want to wait until it is close to
    completion before preparing the Next-in-line
    input.

- If you prepare an input and specify a prepare
  time, note that the input will transition to the
  Prepare state but no preparing will occur until the
  specified time.
- If you both manually prepare an input with a
  prepare time and manually activate it with an
  activate time, make sure the prepare time is before
  the activate time; Elemental Live does not
  check.
- When you call Prepare Immediately on an input that
  has previously been set up to be prepared at a time
  that is still in the future, the input will prepare
  immediately and the future preparation will be
  cleared. It will not be prepared both immediately
  and in the future.

For example, you prepare with a prepare time of
2:00 p.m., then you prepare it immediately, then the
input becomes Active and completes at 1:45 p.m. The
input will not get prepared again at 2:00
p.m.

- If you prepare input X with a prepare time, any
  previously prepared input will immediately become
  unprepared, even though the preparation of input x
  is still in the future. although input x is not
  being prepared, it is still considered to be in the
  Prepared state; only one input can be Prepared at a
  time, so the previous input becomes
  unprepared.
