# How input switch

actions work

You can set up an action to switch the input that the running
channel is ingesting. The channel stops ingesting the current
input and starts ingesting the specified input.

The input must already be attached to the channel.

Before you add input switching actions to the schedule, read
[Setting up for input switching](scheduled-input-switching.md "scheduled-input-switching.md").

###### Input switch with fixed start

When you create the action, you include a start time. The
start time for the action must be at least 15 seconds in the
future but not more than 14 days in the future. After that
cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the
schedule. Approximately 15 seconds before the start time, the
schedule passes the action to the channel. The channel sets up
so that the input switches at the specified time.

###### Input switch with immediate start

When you create the action, you set the start type to
_immediate_.

For an input switch in a standard channel (a channel with two
pipelines), MediaLive internally sets the start time to 10 seconds
in the future. This delay ensures that the switch occurs at
exactly the same time for the two pipelines.

The schedule immediately passes the action to the channel. The
channel immediately starts to switch the input (for a
single-pipeline channel), or sets up to switch at the specified
time (for a standard channel).

###### Input switch with follow start

When you create the action, you specify the input switch
action that you want this action to follow. That _reference action_ must be an
input switch.

The input for the reference action must have a source end
behavior of _Continue_. To find
the **Source end behavior** field, go to the
**Create channel** page, find the input in
the **Input attachment** list, and then find
**General input settings**.

After you create the action, the action waits in the schedule.
Just before the reference action is due to finish, the schedule
passes the action to the channel so that the channel can switch
to the new input as soon as the current input has
finished.
