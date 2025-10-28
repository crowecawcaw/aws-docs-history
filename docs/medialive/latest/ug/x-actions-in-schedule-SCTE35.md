# How SCTE 35

actions work

You can set up an action to insert a SCTE 35 message in the
channel. There are three types of actions:

- Action to insert a splice_insert into the channel: a
  SCTE 35 message with splice_command_type set to
  splice_insert.
- Action to insert a time_signal into the channel: a
  SCTE 35 message with splice_command_type set to
  time_signal.
- Action to insert a SCTE 35 return-to-network message
  into the schedule in order to end a splice_insert that
  either has a duration or has no duration.
  Before you add SCTE 35 actions to the schedule, read [Processing SCTE 35 messages](scte-35-message-processing.md "scte-35-message-processing.md").

###### Insert SCTE 35 message with fixed start

When you create the action, you include a start time. The
start time for the action must be at least 15 seconds in the
future but not more than 14 days in the future. After that
cutoff, MediaLive rejects the request to create the action.

After you have created the action, the action sits in the
schedule. Approximately 15 seconds before the start time, the
schedule passes the action to the channel. At the start time,
the channel inserts the SCTE 35 message into the stream.

After the channel inserts the message, MediaLive processes the
inserted message in the same way as it processes messages that
were already in the source content.

###### Insert SCTE 35 message with immediate start

When you create the action, you set the start type to
_immediate_.

The schedule immediately passes the action to the channel. The
channel immediately inserts the SCTE 35 message into the
stream.

After the channel inserts the message, MediaLive processes the
inserted message in the same way as it processes messages that
were already in the source content.

###### Insert SCTE 35 message with follow start

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
has finished, the channel inserts the SCTE 35 message into the
stream.

After the channel inserts the message, MediaLive processes the
inserted message in the same way as it processes messages that
were already in the source content.
