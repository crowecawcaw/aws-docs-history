# Scheduled events for Amazon EC2

instances

To ensure infrastructure reliability and performance, AWS can schedule events to
reboot, stop, and retire your instances. These events do not occur frequently.

If one of your instances will be affected by a scheduled event, AWS notifies you in
advance by email, using the email address that's associated with your AWS account. The
email provides details about the event, such as the start and end dates. Depending on
the event type, you might be able to take action to control the timing of the event.
AWS also sends an AWS Health event, which you can monitor and manage by using
Amazon EventBridge. For more information, see [Monitoring events in
AWS Health with Amazon EventBridge](../../../health/latest/ug/cloudwatch-events-health.md "../../../health/latest/ug/cloudwatch-events-health.md").

Scheduled events are managed by AWS. You can't schedule events for your instances.
However, you can:

- View scheduled events for your instances.
- Customize scheduled event notifications to include or remove tags from the
  email notification.
- Reschedule certain scheduled events.
- Create custom event windows for scheduled events.
- Take action when an instance is scheduled to reboot, stop, or retire.
  To ensure that you receive notifications of scheduled events, verify your contact
  information on the [Account](https://console.aws.amazon.com/billing/home?#/account "https://console.aws.amazon.com/billing/home?#/account") page.

###### Note

When
an instance is affected by a scheduled event, and it is part of an Auto Scaling group,
Amazon EC2 Auto Scaling eventually replaces it as part of its health checks, with no further action
necessary on your part. For more information about the health checks performed by
Amazon EC2 Auto Scaling, see [Health
checks for instances in an Auto Scaling group](../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-health-checks.md") in the
_Amazon EC2 Auto Scaling User Guide_.

## Types of scheduled events

Amazon EC2 can create the following types of scheduled events for your instances, where
the event occurs at a scheduled time:

| Event type          | Event code            | Event action                                                                                                                                                                       |
| ------------------- | --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance stop       | `instance-stop`       | At the scheduled time, the instance is stopped. When you start it<br>again, it's migrated to a new host. Applies only to instances with<br>an Amazon EBS root volume.              |
| Instance retirement | `instance-retirement` | At the scheduled time, the instance is stopped if it has an Amazon EBS<br>root volume, or terminated if it has an instance store root<br>volume.                                   |
| Instance reboot     | `instance-reboot`     | At the scheduled time, the instance is rebooted. The instance<br>stays on the host, and during the reboot, the host undergoes<br>maintenance. This is known as an in-place reboot. |
| System reboot       | `system-reboot`       | At the scheduled time, the instance is rebooted and migrated to a<br>new host. This is known as a reboot migration.                                                                |
| System maintenance  | `system-maintenance`  | At the scheduled time, the instance might be temporarily affected<br>by network maintenance or power maintenance.                                                                  |

## Determine the event type

You can check what type of event is scheduled for your instance.

Console

###### To determine the event type

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. In the table, the event code appears in the **Event
   type** column.
4. To filter the table to show only the events for instances, in
   the search field choose **Resource type:
   instance** from the filter list.

AWS CLI

###### To determine the event type for an instance

Use the [describe-instance-status](../../../cli/latest/reference/ec2/describe-instance-status.md "../../../cli/latest/reference/ec2/describe-instance-status.md") command. If the instance
has an associated scheduled event, the output provides
information about the scheduled event.

```
aws ec2 describe-instance-status \
    --instance-id `i-1234567890abcdef0` \
    --query InstanceStatuses[].Events
```

The following is example output. The scheduled event
code is `system-reboot`.

```
[
    "Events": [
        {
            "InstanceEventId": "instance-event-0d59937288b749b32",
            **"Code": "system-reboot"**,
            "Description": "The instance is scheduled for a reboot",
            "NotAfter": "2020-03-14T22:00:00.000Z",
            "NotBefore": "2020-03-14T20:00:00.000Z",
            "NotBeforeDeadline": "2020-04-05T11:00:00.000Z"
        }
    ]
]
```

PowerShell

###### To determine the event type for an instance

Use the [Get-EC2InstanceStatus](../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md "../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md")
cmdlet. If the instance has an associated scheduled event, the
output provides information about the scheduled event.

```
(Get-EC2InstanceStatus `
    -InstanceId `i-1234567890abcdef0`).Events
```

The following is example output. The scheduled event
code is `system-reboot`.

```
Code              : system-reboot
Description       : The instance is scheduled for a reboot
InstanceEventId   : instance-event-0d59937288b749b32
NotAfter          : 2020-03-14T22:00:00.000Z
NotBefore         : 2020-03-14T20:00:00.000Z
NotBeforeDeadline : 2020-04-05T11:00:00.000Z
```

###### Contents

- [Manage Amazon EC2 instances scheduled to
  stop or retire](schedevents_actions_retire.md "schedevents_actions_retire.md")
- [Manage Amazon EC2 instances scheduled for
  reboot](schedevents_actions_reboot.md "schedevents_actions_reboot.md")
- [Manage Amazon EC2 instances scheduled
  for maintenance](schedevents_actions_maintenance.md "schedevents_actions_maintenance.md")
- [View scheduled events that affect your
  Amazon EC2 instances](viewing_scheduled_events.md "viewing_scheduled_events.md")
- [Customize scheduled
  event notifications for your EC2 instances](customizing_scheduled_event_notifications.md "customizing_scheduled_event_notifications.md")
- [Reschedule a scheduled event for an EC2 instance](reschedule-event.md "reschedule-event.md")
- [Create custom event windows for scheduled events
  that affect your Amazon EC2 instances](event-windows.md "event-windows.md")
