# View scheduled events that affect your

Amazon EC2 instances

In addition to receiving notification of scheduled events in email, you can check
for scheduled events.

Console

###### To view scheduled events for your instances

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. The dashboard displays any resources with an associated event
   under **Scheduled events**.

![Viewing events using the dashboard.](images/dashboard-scheduled-events.png) 3. For more detail, choose **Events** in the
navigation pane. Any resources with an associated event are
displayed. You can filter by characteristics such as event type,
resource type, and Availability Zone.

![Viewing events using the Events page.](images/events-instance-scheduled-stop.png)

AWS CLI

###### To view scheduled events for your instances

Use the [describe-instance-status](../../../cli/latest/reference/ec2/describe-instance-status.md "../../../cli/latest/reference/ec2/describe-instance-status.md") command.

```
aws ec2 describe-instance-status \
    --instance-id `i-1234567890abcdef0` \
    --query "InstanceStatuses[].Events"
```

The following example output shows a reboot event.

```
[
    "Events": [
        {
            "InstanceEventId": "instance-event-0d59937288b749b32",
            "Code": "system-reboot",
            "Description": "The instance is scheduled for a reboot",
            "NotAfter": "2019-03-15T22:00:00.000Z",
            "NotBefore": "2019-03-14T20:00:00.000Z",
            "NotBeforeDeadline": "2019-04-05T11:00:00.000Z"
         }

    ]
]
```

The following example output shows an instance retirement
event.

```
[
    "Events": [
        {
            "InstanceEventId": "instance-event-0e439355b779n26",
            "Code": "instance-stop",
            "Description": "The instance is running on degraded hardware",
            "NotBefore": "2015-05-23T00:00:00.000Z"
        }
    ]
]
```

PowerShell

###### To view scheduled events for your instances

Use the following [Get-EC2InstanceStatus](../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md "../../../powershell/latest/reference/items/Get-EC2InstanceStatus.md") command.

```
(Get-EC2InstanceStatus -InstanceId `i-1234567890abcdef0`).Events
```

The following example output shows an instance retirement
event.

```
Code         : instance-stop
Description  : The instance is running on degraded hardware
NotBefore    : 5/23/2015 12:00:00 AM
```

Instance metadata

###### To view scheduled events for your instances using instance

metadata

You can retrieve information about active maintenance events for
your instances from the [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") by using Instance Metadata Service Version 2 or
Instance Metadata Service Version 1.

**IMDSv2**

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/events/maintenance/scheduled`
```

**IMDSv1**

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/events/maintenance/scheduled`
```

The following is example output with information about a scheduled
system reboot event, in JSON format.

```
[
  {
    "NotBefore" : "21 Jan 2019 09:00:43 GMT",
    "Code" : "system-reboot",
    "Description" : "scheduled reboot",
    "EventId" : "instance-event-0d59937288b749b32",
    "NotAfter" : "21 Jan 2019 09:17:23 GMT",
    "State" : "active"
  }
]
```

###### To view event history about completed or canceled events for your

instances using instance metadata

You can retrieve information about completed or canceled events
for your instances from [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") by using Instance Metadata Service Version 2 or
Instance Metadata Service Version 1.

**IMDSv2**

```
`[ec2-user ~]$` `TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/events/maintenance/history`
```

**IMDSv1**

```
`[ec2-user ~]$` `curl http://169.254.169.254/latest/meta-data/events/maintenance/history`
```

The following is example output with information about a system reboot
event that was canceled, and a system reboot event that was completed,
in JSON format.

```
[
  {
    "NotBefore" : "21 Jan 2019 09:00:43 GMT",
    "Code" : "system-reboot",
    "Description" : "[Canceled] scheduled reboot",
    "EventId" : "instance-event-0d59937288b749b32",
    "NotAfter" : "21 Jan 2019 09:17:23 GMT",
    "State" : "canceled"
  },
  {
    "NotBefore" : "29 Jan 2019 09:00:43 GMT",
    "Code" : "system-reboot",
    "Description" : "[Completed] scheduled reboot",
    "EventId" : "instance-event-0d59937288b749b32",
    "NotAfter" : "29 Jan 2019 09:17:23 GMT",
    "State" : "completed"
  }
]
```

AWS Health
You can use the AWS Health Dashboard to learn about events that can affect your
instance. The Health Dashboard organizes issues in three groups: open issues,
scheduled changes, and other notifications. The scheduled changes group
contains items that are ongoing or upcoming.

For more information, see [Getting
started with your AWS Health Dashboard](../../../health/latest/ug/getting-started-health-dashboard.md "../../../health/latest/ug/getting-started-health-dashboard.md") in the
_AWS Health User Guide_.
