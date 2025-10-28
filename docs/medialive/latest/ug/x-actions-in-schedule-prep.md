# How input prepare

actions work

You can set up an action to prepare an input that is
associated with an immediate input switch, in order to reduce
the delay that occurs when MediaLive performs the switch.

The input must already be attached to the channel. However,
there is no requirement for the input switch for this input to
already exist in the schedule. For example, input X must be
_attached_ to the channel.
You can create action A to prepare input X and later on you can
create action B to switch to input X. Or you can create action B
and then create action A.

Before you add input prepare actions to the schedule, read
[Preparing inputs in
AWS Elemental MediaLive](feature-prepare-input.md "feature-prepare-input.md").

###### Input prepare with fixed start

When you create the action, include a start time. The
start time for the action must be at least 15 seconds before
the start time of the associated input switch, but not more
than 14 days in the future. After that cutoff, MediaLive rejects
the request to create the action.

After you have created the action, the action sits in the
schedule. Approximately 15 seconds before the start time of the
prepare action, the schedule passes the action to the channel.
The channel starts preparing the input.

###### Input prepare with immediate start

When you create the action, you set the start type to
_immediate_.

The schedule immediately passes the action to the channel. The
channel immediately starts the prepare.

###### Input prepare with follow start

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
passes the action to the channel. As soon as the current input
has finished, the channel switches to the new input.
