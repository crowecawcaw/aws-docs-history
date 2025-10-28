# How pause and

unpause actions work

You can insert an action to pause and unpause one or both
pipelines in the channel. The action pauses the specified
pipelines and unpauses any unspecified pipelines:

- Action with _one_
  pipeline specified–The action pauses the specified
  pipeline and unpauses the other pipeline.
- Action with _both_
  pipelines specified–The action pauses both
  pipelines.
- Action with _no_
  pipelines specified–The action unpauses both
  pipelines.

###### Note

The pipelines that you don't specify are not left in their
current state. They are always set to unpaused.

**Pause or unpause with fixed start**

When you create the action, you include a start time. The
start time for the action must be at least 15 seconds in the
future but not more than 14 days in the future. After that
cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the
schedule. Approximately 15 seconds before the start time, the
schedule passes the action to the channel. At the start time,
the channel pauses or unpauses the pipelines in the
channel.

**Pause or unpause with immediate start**

When you create the action, you set the start type to
_immediate_.

The schedule immediately passes the action to the channel. The
channel immediately pauses or unpauses the pipelines in the
channel.
