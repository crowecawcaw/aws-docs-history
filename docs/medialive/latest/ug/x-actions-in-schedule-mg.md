# How motion graphics

overlay works

You can set up an action to insert and remove a motion
graphics overlay on the video:

- The activate motion graphics action inserts a motion
  graphic and activates it so that it is superimposed on
  the underlying video. If the image overlay information
  includes a duration, then at the appropriate time the
  motion graphic is removed.
- The deactivate motion graphics action removes an image
  overlay. You therefore use this action to remove a
  currently running motion graphics before the specified
  duration, or remove it when no duration is
  specified.
  For information about preparing the motion graphics asset that
  the action inserts, see [Working with motion graphics
  overlays](feature-mgi.md "feature-mgi.md").

###### Activate or deactivate with fixed start

When you create the action, you include a start time. The
start time for the action must be at least 15 seconds in the
future but not more than 14 days in the future. After that
cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the
schedule. Approximately 15 seconds before the start time, the
schedule passes the action to the channel. At the start time,
the channel inserts the motion graphic or removes the motion
graphic from the video.

###### Activate or deactivate with immediate start

When you create the action, you set the start type to
_immediate_.

The schedule immediately passes the action to the channel. The
channel immediately inserts the motion graphic or removes the
motion graphic.
