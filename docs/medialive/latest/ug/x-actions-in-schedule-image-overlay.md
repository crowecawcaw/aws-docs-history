# How image overlay actions

work

You can set up an action to insert and remove an image overlay on the
video:

- The activate action inserts an image overlay and activates it so that it
  is superimposed on the underlying video. If the image overlay information
  includes a duration, then at the appropriate time the image overlay is
  removed.
- The deactivate action removes an image overlay. You therefore use this
  action to remove a currently running image overlay before the specified
  duration, or remove it when no duration is specified.
  Before you add image overlay actions to the schedule, read [Working with image overlays](working-with-image-overlay.md "working-with-image-overlay.md").

**Global or per-outputs insertion**

There are two ways to insert image overlays:

- Use the **Static image activate** feature to
  insert globally: You can create an action to insert an image overlay in
  every output in every output group in a channel.

- Use the **Static image output activate**
  feature to insert per-output: You can create an action to insert an image
  overlay in specific outputs in specific output groups in a channel.
  **Activate or deactivate with fixed start**

When you create the action, you include a start time. The start time for the
action must be at least 15 seconds in the future but not more than 14 days in the
future. After that cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the schedule. Approximately
15 seconds before the start time, the schedule passes the action to the channel. At
the start time, the channel inserts the image overlay or removes the image overlay
from the video.

**Activate or deactivate with immediate
start**

When you create the action, you set the start type to _immediate_.

The schedule immediately passes the action to the channel. The channel immediately
inserts the image overlay or removes the image overlay.
