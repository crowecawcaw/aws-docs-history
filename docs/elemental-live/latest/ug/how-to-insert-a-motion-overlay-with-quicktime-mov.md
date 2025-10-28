# How

to insert a motion overlay with QuickTime MOV

You can use a `.mov` file as an asset for the
motion image overlay.

Here are some examples of how motion image overlay works with a MOV
file:

- Example 1: “Coming up” motion overlay – You want to
  insert an asset that will run as a 10-second motion overlay 59
  minutes into the runtime of the event. You want the motion
  overlay to be placed in the lower right corner of the video
  frame.
- Example 2: Animated corporate logo – You want to insert
  an asset and run it every 5 minutes, starting 20 minutes into the
  runtime of the event. You specify the single asset in the event
  and specify the first runtime. You start the event and, after the
  motion overlay has run once, you send a REST API command to
  modify the start time of the asset to a new time. You repeat this
  command (each time with a new start time) as many times as you
  want.
  Typically, you set up the event as follows:

- You prepare a MOV file and store it at a location that is
  accessible to Elemental Live.
- You configure the event with the location URL and start time
  of the first motion overlay you want to run, with position and
  size information, and with an instruction to run the motion
  overlay once or to loop it. You set up the motion overlay to be
  active when the event starts, and you enable control via the REST
  API.
- When you're ready, you start the event. The motion overlay
  configured in the event runs at the specified time. You then
  enter REST API commands to specify different content (a different
  URL), a start time, and a new position and size. After that
  motion overlay plays, you can enter another command to run
  different content, as required, for the duration of the event.
