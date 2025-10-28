# Creating an AWS Elemental MediaLive

schedule

In AWS Elemental MediaLive, you can manipulate the processing of a channel while it
is running. You perform this manipulation by adding actions to the
schedule that is associated with the channel. The schedule holds each
action until the start time for the action, at which point MediaLive passes
the action to the channel, and the channel performs the action.

We recommend that you read this schedule chapter before you start the
channel. A key schedule action is input switching, which you must
implement if you have a multiple-input channel (if you have attached
more than one input to the channel). But there are other actions that
might be relevant to your workflow.

Typically, you set up the schedule before you start the channel. At
the least, you create schedule actions that you know must occur soon.
After you start the channel, you can continue to add schedule actions.
You can add actions you already have planned and ad-hoc actions.

###### Topics

- [Types of actions in the
  schedule](x-actions-in-schedule.md "x-actions-in-schedule.md")
- [Types of timing for
  actions](sched-timing-types.md "sched-timing-types.md")
- [How schedule actions work](sched-how-actions-work.md "sched-how-actions-work.md")
- [Working with the schedule
  (console)](schedule-using-console.md "schedule-using-console.md")
- [Working with the schedule
  (AWS CLI)](schedule-using-cli.md "schedule-using-cli.md")
