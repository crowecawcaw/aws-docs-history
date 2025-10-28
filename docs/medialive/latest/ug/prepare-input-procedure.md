# Setting up input prepare actions in the

schedule

Follow this procedure to add input prepare actions to the channel schedule, in order to
prepare any input ahead of the switch action to that input.

###### To include input prepare actions in a channel schedule

1. As a one-time action, enable the input prepare feature in the channel. You must enable the
   feature while the channel is idle. See [Enabling and disabling the input prepare feature](input-prep-enable.md "input-prep-enable.md").
2. Plan the input switches and input prepares for the channel. See [Planning the start type for an input prepare](input-prep-plan-start.md "input-prep-plan-start.md").
3. If the associated input switch includes input clipping, see [Clipping the content of a file input](input-clipping.md "input-clipping.md").

If the associated input switch is an input failover pair, see [Setting up dynamic inputs](dynamic-inputs.md "dynamic-inputs.md"). 4. Create the actions in the schedule. Typically, you create some prepare actions and switch
actions before you start the channel for the first time. Then you add more actions over time.
You add fixed switch actions, and follow switch actions. You add prepare actions as soon as you
know that you will have an immediate switch some time in the future. Typically, you add all
these actions while the channel is running, but you can also add them when the channel is
idle.

For detailed information on adding an input prepare action to the schedule, see [Creating an AWS Elemental MediaLive
schedule](working-with-schedule.md "working-with-schedule.md").

###### Topics

- [Enabling and disabling the input prepare feature](input-prep-enable.md "input-prep-enable.md")
- [Planning the start type for an input prepare](input-prep-plan-start.md "input-prep-plan-start.md")
- [Input prepare and dynamic inputs](input-prep-dynamic.md "input-prep-dynamic.md")
- [Input prepare with clipping](input-prep-clip.md "input-prep-clip.md")
- [Input prepare and automatic input failover](input-prep-aif.md "input-prep-aif.md")
