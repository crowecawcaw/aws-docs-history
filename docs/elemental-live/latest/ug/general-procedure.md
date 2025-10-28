# General procedure

###### Topics

- [Step A: Design the dynamic
  playlist](#step-design "#step-design")
- [Step B: Create and start the
  event](#step-create "#step-create")
- [Step C: Add more
  inputs](#step-add-more-inputs "#step-add-more-inputs")
- [Step D: Prepare
  inputs](#step-prepare "#step-prepare")
- [Step E: Activate
  inputs](#step-active "#step-active")
- [Step F: Continue adding to
  the dynamic playlist](#step-add-more "#step-add-more")
- [Step G: Interrupt the
  currently active input](#step-interrupt "#step-interrupt")
- [Step H: Clean up the
  playlist](#step-clean "#step-clean")
- [Step I:
  Troubleshoot](#step-troubleshoot "#step-troubleshoot")

## Step A: Design the dynamic

playlist

### Identify

inputs

1. Identify the inputs and the order in which they are
   to play.

- The first input can be a live asset or a file
  asset.
- The inputs can be all live assets, all file
  assets, or a mix of live and file assets.
- The same input can be repeated as many times
  as you want in the dynamic playlist.

Generally, it is a good idea to add the inputs to the
event in the order in which they will be played. You
should do this even if you plan to specify a start time
for some or all inputs (below).

### Identify inputs to prepare manually

2. Identify inputs that must first be prepared:

- Live streaming inputs: You must manually
  prepare each live input before it is due to be
  played.
- File inputs: There is no need to manually
  prepare file inputs, but you may do so if you
  prefer. Perhaps a reason to prepare is that you
  know you have to prepare live inputs and you
  want to follow the same steps for both live and
  file inputs.

### Identify inputs to activate manually

3. Identify inputs that must start at a specific time,
   rather than simply starting after the previous input
   ends.

If you follow the recommended procedure (Step E:
below), you will need a placeholder input. Read the
procedure in Step E: so that you can prepare this input
now.

## Step B: Create and start the

event

4. Create the event with only the first input. (If the
   event contains more than one input, the others will be
   deleted when you create the dynamic playlist.)

Use the REST API Create Event command or use the web
interface. See below for tips on setting up the event for
the different use cases.

5. Start the event. Use the REST API or the web interface.
   Processing starts on that single input.

## Step C: Add more

inputs

6. Once the event has been started, you can create the
   dynamic playlist in order to add more inputs to the event.

There are two ways to add inputs to the dynamic
playlist:

- Use the Add Dynamic Playlist Inputs command to
  create an array of inputs that are appended to the
  inputs currently in the event. Up to 29 inputs can
  be added in this way. For more information, see
  [Add dynamic
  playlist inputs](add-dynamic-playlist-inputs.md "add-dynamic-playlist-inputs.md").
- Use the Replace Dynamic List command to create an
  array of inputs that replaces the existing dynamic
  playlist (except for the currently running input).
  You can add any number of inputs this way. For more
  information, see [Replace dynamic
  playlist](replace-dynamic-playlist.md "replace-dynamic-playlist.md").

## Step D: Prepare

inputs

7. If you have identified inputs that must be manually
   prepared, then as soon as one of those inputs becomes “next
   in line”, you prepare it by calling [Prepare dynamic
   playlist input](prepare-dynamic-playlist-input.md "prepare-dynamic-playlist-input.md").

- Time the preparation correctly: For a live input,
  you must prepare enough time in advance to allow
  Elemental Live to inspect the entire next-in-line
  input and decode at least one frame. But you should
  not prepare it too far in advance because once
  preparation starts, this is what happens:

Elemental Live inspects the entire input then
decodes the first frame in the pipeline. If this
input is still not due to run, it discards that
frame and decodes the frame that is now first in the
pipeline. It discards that frame and decodes the
frame that is now first in the pipeline, on and on
until the input is due to run. This decoding
obviously uses processing resources.

- This timing rule does not apply to file inputs.
- You can optionally specify a prepare time. The
  input will transition to the Prepare state but no
  preparing will actually occur until the specified
  time.
- Keep in mind that you can only manually prepare
  one input at a time: if you prepare input A, do not
  prepare the next input until input A is active. If
  you do, input A may not start as expected.

For more information about the rules around preparation, see [Details on
preparing inputs](details-on-preparing-inputs.md "details-on-preparing-inputs.md").

## Step E: Activate

inputs

8. For each input that must start at a specific time, set
   the activate time when the input is next in line.

### Activating using placeholders

Scheduling inputs is a bit tricky because an
Elemental Live event must always be encoding: there is no
concept of waiting for a frame to arrive. Therefore, if
you do not time input B to start immediately after input
A ends, then Elemental Live will move to the next input
that does not have an activate time (perhaps the input
that appears after input B in the XML). But it is very
difficult to get this timing between inputs exact
enough.

The workaround is to use a “placeholder” input between
inputs A and B, as follows:

- Estimate the expected end time of input A.
- Assign an activate time for input B that is as
  close to the end time without being before it.
  (In this way, input A is not
  interrupted.)
- Between input A and input B insert a
  “placeholder” file input (this input could be a
  blackout slate, for example). Do not assign a
  start to this placeholder but do set the
  loop_source tag to true for this input in order
  to play the content repeatedly until it is time
  to return to the live input.

This will be the result: if input A end time does not
exactly match the activate time for input B, then the
placeholder will play. When the activate time for input
B arrives, the placeholder will be interrupted by input
B. Input B will start at the scheduled time.

## Step F: Continue adding to

the dynamic playlist

9. As inputs are run, add more inputs to the event.

- So long as the event is still running, you can
  continue to add inputs to it; the event will not
  end.
- Add inputs using either the [Add
  Dynamic Playlist Inputs](add-dynamic-playlist-inputs.md "add-dynamic-playlist-inputs.md") command or the
  [Replace
  Dynamic List](replace-dynamic-playlist.md "replace-dynamic-playlist.md") command.

## Step G: Interrupt the

currently active input

Occasionally, you may need to interrupt the current active
input and start a different input (input B). See [Implementing use
case 3](sample-implementations.md#implementing-use-case-3 "sample-implementations.md#implementing-use-case-3") for an example
of an unanticipated interruption.

- If necessary, add input B to the dynamic playlist.
  There are two ways to add:
  - Rebuild the entire playlist, with input B
    inserted at the top, using the Replace
    Dynamic Playlist command. The currently
    active input will not be removed when you do
    this. For more information, see [Replace dynamic
    playlist](replace-dynamic-playlist.md "replace-dynamic-playlist.md").
  - Append input B to the end of the playlist,
    using the Add Dynamic Playlist Inputs
    command. The drawback to this method is that
    the input appears at the end of the playlist
    on the web interface, but then gets
    activated, which may confuse your operators.
    For more information, see [Add dynamic
    playlist inputs](add-dynamic-playlist-inputs.md "add-dynamic-playlist-inputs.md").

- If input B is a live input, prepare it using the
  Prepare Dynamic Playlist command. For more
  information, see [Prepare dynamic
  playlist input](prepare-dynamic-playlist-input.md "prepare-dynamic-playlist-input.md").
- Use the Activate Dynamic List Input command
  (without an activate time) to immediately activate
  the input. For more information, see [Activate
  dynamic playlist input](activate-dynamic-playlist-input.md "activate-dynamic-playlist-input.md").

## Step H: Clean up the

playlist

10. The dynamic playlist is never automatically cleaned
    up; even after an input has been processed, it remains on
    the dynamic playlist.

- If you use the Replace Dynamic Playlist command,
  the entire playlist is replaced, which effectively
  cleans up old inputs. Fore more information, see
  [Replace dynamic
  playlist](replace-dynamic-playlist.md "replace-dynamic-playlist.md").
- If you use the Add Dynamic Playlist Inputs
  command, then you may want to occasionally use the
  Delete Dynamic Playlist Input command. For more
  information, see [Delete dynamic
  playlist input](delete-dynamic-playlist-input.md "delete-dynamic-playlist-input.md").

## Step I:

Troubleshoot

If the dynamic playlist is not behaving as expected, see the information about
preparation and activation, starting [here](details-on-preparing-inputs.md "details-on-preparing-inputs.md"). You may have broken a preparation or activation rule.
