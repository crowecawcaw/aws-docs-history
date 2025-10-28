# Reschedule a scheduled event for an EC2 instance

You can reschedule an event so that it occurs at a specific date and time that
suits you. After you reschedule an event, it might take a minute or two before the
the updated date is displayed.

###### Limitations

- Only events with an event deadline date can be rescheduled. The event
  can be rescheduled up to the event deadline date. The event deadline
  date is indicated in the **Deadline** column (console)
  and the `NotBeforeDeadline` field (AWS CLI).
- Only events that have not yet started can be rescheduled. The start
  time is indicated in the **Start time** column
  (console) and the `NotBefore` field (AWS CLI). Events that are
  scheduled to start in the next 5 minutes can't be rescheduled.
- The new event start time must be at least 60 minutes from the current
  time.
- If you reschedule multiple events using the console, the event
  deadline date is determined by the event with the earliest event
  deadline date.

Console

###### To reschedule an event

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Resource type: instance** from the
   filter list.
4. Select one or more instances, and then choose
   **Actions**, **Schedule
   event**.

Only events that have an event deadline date, indicated by a
value for **Deadline**, can be rescheduled. If
one of the selected events does not have a deadline date,
**Actions**, **Schedule
event** is disabled. 5. For **New start time**, enter a new date and
time for the event. The new date and time must occur before the
**Event deadline**. 6. Choose **Save**.

It might take a minute or two for the updated event start time
to be reflected in the console.

AWS CLI

###### To reschedule an event

Use the [modify-instance-event-start-time](../../../cli/latest/reference/ec2/modify-instance-event-start-time.md "../../../cli/latest/reference/ec2/modify-instance-event-start-time.md") command.

```
aws ec2 modify-instance-event-start-time \
    --instance-id `i-1234567890abcdef0` \
    --instance-event-id `instance-event-0d59937288b749b32` \
    --not-before `2020-03-25T10:00:00.000`
```

PowerShell

###### To reschedule an event

Use the [Edit-EC2InstanceEventStartTime](../../../powershell/latest/reference/items/Edit-EC2InstanceEventStartTime.md "../../../powershell/latest/reference/items/Edit-EC2InstanceEventStartTime.md")
cmdlet.

```
Edit-EC2InstanceEventStartTime `
    -InstanceId `i-1234567890abcdef0` `
    -InstanceEventId `instance-event-0d59937288b749b32` `
    -NotBefore `2020-03-25T10:00:00.000`
```
