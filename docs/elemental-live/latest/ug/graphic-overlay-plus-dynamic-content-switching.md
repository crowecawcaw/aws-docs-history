# Static

overlay plus dynamic content switching

You can combine the static overlays with the dynamic content switching feature. You can
use dynamic content switching to continually add and modify inputs in an event that is
running. As you add inputs, you can insert static or motion overlays, as desired. For
information about dynamic content switching, see [Dynamic input
switching](dynamic-content-switching.md "dynamic-content-switching.md").

## Scheduling inputs

and overlays

The scheduling of the inputs and the overlays is completely
decoupled.

A given input X might be added several times to the dynamic
playlist, for example, so that it plays at 2:00 p.m. and then plays
again at 3:10 p.m.

If you want an overlay to appear the first time that input X
plays, you might set its start time for 2:10 p.m. The next time that
input X plays, there is no logic to play the same overlay again
because 2:10 p.m. has passed. Therefore, if you want the overlay to
appear again on input X, you must send a Modify Overlay call again.

## Behavior with different insertion options for static

overlays

Following are points to remember when using static overlay with
dynamic content switching:

**Playlist input plus overlay at the input
stage**

You specify the overlay in the input section of the event.
Therefore, whenever you include this input in the playlist, the
overlay will be included. If you want to the image the first time
the input appears in the playlist but you don't want to include it
the next time the input appears, you must unless enter an action to
remove it.

- If you want to include the overlay in a given repetition of the input, you
  might need to change the start time of the overlay. See the information about the
  Start Time in the table under [Step B: Initial
  setup](step-b-initial-setup.md "step-b-initial-setup.md").
- If you do not want to include the overlay in a given
  repetition of that input, you must use the REST interface to
  enter a Modify Static Overlay command and delete the overlay.
  See [Static graphic
  overlay commands](static-graphic-overlay-commands.md "static-graphic-overlay-commands.md").

  **Playlist input plus overlay at the global
  processing stage**

The scheduling of the inputs and the overlays is completely
decoupled.

A given input X might be added several times to the dynamic
playlist, for example, so that it plays at 2:00 p.m. and then plays
again at 3:10 p.m.

If you want an overlay to appear the first time that input X
plays, you might set its start time for 2:10 p.m. The next time that
input X plays, there is no logic to play the same overlay again
because 2:10 p.m. has passed.

Therefore, if you want the overlay to appear again on input X,
you must enter the Modify Static Overlay command again.

**Playlist input plus overlay at the output
stage**

The same comments as for global processing stage apply.
