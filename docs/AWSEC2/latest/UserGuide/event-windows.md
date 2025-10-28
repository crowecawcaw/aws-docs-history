# Create custom event windows for scheduled events

that affect your Amazon EC2 instances

You can define custom event windows that recur weekly for scheduled events that
reboot, stop, or terminate your Amazon EC2 instances. You can associate one or more
instances with an event window. If a scheduled event for those instances is planned,
AWS will schedule the events within the associated event window.

You can use event windows to maximize workload availability by specifying event
windows that occur during off-peak periods for your workload. You can also align the
event windows with your internal maintenance schedules.

You define an event window by specifying a set of time ranges. The minimum time
range is 2 hours. The combined time ranges must total at least 4 hours.

You can associate one or more instances with an event window by using either
instance IDs or instance tags. You can also associate Dedicated Hosts with an event window by
using the host ID.

###### Warning

Event windows are applicable only for scheduled events that stop, reboot, or
terminate instances.

Event windows are not applicable for:

- Expedited scheduled events and network maintenance events.
- Unscheduled maintenance such as [automatic instance recovery](ec2-instance-recover.md "ec2-instance-recover.md") and unplanned reboots.

###### Work with event windows

- [Considerations](#event-windows-considerations "#event-windows-considerations")
- [Create an event window](#create-event-windows "#create-event-windows")
- [Associate a target with an event window](#associate-target-event-window "#associate-target-event-window")
- [Disassociate a target from an event window](#disassociate-target-event-window "#disassociate-target-event-window")
- [Modify an event window](#modify-event-windows "#modify-event-windows")
- [Delete an event window](#delete-event-windows "#delete-event-windows")

## Considerations

- All event window times are in UTC.
- An event window can contain multiple time ranges. While each
  individual range must be at least 2 hours, the total duration across all
  ranges must be at least 4 hours.
- Only one target type (instance ID, Dedicated Host ID, or instance tag) can be
  associated with an event window.
- A target (instance ID, Dedicated Host ID, or instance tag) can only be
  associated with one event window.
- A maximum of 100 instance IDs, or 50 Dedicated Host IDs, or 50 instance tags can
  be associated with an event window. The instance tags can be associated
  with any number of instances.
- A maximum of 200 event windows can be created per AWS Region.
- Multiple instances that are associated with event windows can
  potentially have scheduled events occur at the same
  time.
- If AWS has already scheduled an event, modifying an event window
  won't change the time of the scheduled event. If the event has a
  deadline date, you can [reschedule the
  event](reschedule-event.md "reschedule-event.md").
- You can stop and start an instance before the scheduled event. This
  migrates the instance to a new host and clears the event.

## Create an event window

You can create one or more event windows. For each event window, you specify
one or more blocks of time. For example, you can create an event window with
blocks of time that occur every day at 4 AM for 2 hours. Or you can create an
event window with blocks of time that occur on Sundays from 2 AM to 4 AM and on
Wednesdays from 3 AM to 5 AM.

Event windows recur weekly until you delete them.

Console

###### To create an event window

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event windows**.
4. Choose **Create instance event
   window**.
5. For **Event window name**, enter a
   descriptive name for the event window.
6. For **Event window schedule**, choose to
   specify the blocks of time in the event window by using the
   cron schedule builder or by specifying time ranges.
   - If you choose **Cron schedule
     builder**, specify the following:
     1. For **Days (UTC)**, specify
        the days of the week on which the event window
        occurs.
     2. For **Start time (UTC)**,
        specify the time when the event window
        begins.
     3. For **Duration**, specify
        the duration of the blocks of time in the event
        window. The minimum duration per block of time is
        2 hours. The minimum duration of the event window
        must equal or exceed 4 hours in total. All times
        are in UTC.

   - If you choose **Time ranges**,
     choose **Add new time range** and
     specify the start day and time and the end day and
     time. Repeat for each time range. The minimum
     duration per time range is 2 hours. The minimum
     duration for all time ranges combined must equal or
     exceed 4 hours in total.

7. (Optional) For **Target details**,
   associate one or more instances with the event window. Use
   instance IDs or instance tags to associate instances. Use
   host IDs to associate Dedicated Hosts. When these targets
   are scheduled for maintenance, the event will occur during
   this event window.

Note that you can create the event window without
associating a target with the window. Later, you can modify
the window to associate one or more targets. 8. (Optional) For **Event window tags**,
choose **Add tag**, and enter the key and
value for the tag. Repeat for each tag. 9. Choose **Create event window**.

AWS CLI

###### To create an event window with a time range

Use the [create-instance-event-window](../../../cli/latest/reference/ec2/create-instance-event-window.md "../../../cli/latest/reference/ec2/create-instance-event-window.md") command.

```
aws ec2 create-instance-event-window \
    --time-range StartWeekDay=`monday`,StartHour=`2`,EndWeekDay=`wednesday`,EndHour=`8` \
    --tag-specifications "ResourceType=instance-event-window,Tags=[{Key=`K1`,Value=`V1`}]" \
    --name `myEventWindowName`
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "TimeRanges": [
            {
                "StartWeekDay": "monday",
                "StartHour": 2,
                "EndWeekDay": "wednesday",
                "EndHour": 8
            }
        ],
        "Name": "myEventWindowName",
        "State": "creating",
        "Tags": [
            {
                "Key": "K1",
                "Value": "V1"
            }
        ]
    }
}
```

###### To create an event window with a cron expression

Use the [create-instance-event-window](../../../cli/latest/reference/ec2/create-instance-event-window.md "../../../cli/latest/reference/ec2/create-instance-event-window.md") command.

```
aws ec2 create-instance-event-window \
    --cron-expression "`* 21-23 * * 2,3`" \
    --tag-specifications "ResourceType=instance-event-window,Tags=[{Key=`K1`,Value=`V1`}]" \
    --name `myEventWindowName`
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "State": "creating",
        "Tags": [
            {
                "Key": "K1",
                "Value": "V1"
            }
        ]
    }
}
```

PowerShell

###### To create an event window with a time range

Use the [New-EC2InstanceEventWindow](../../../powershell/latest/reference/items/New-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/New-EC2InstanceEventWindow.md")
cmdlet.

```
$timeRange = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest
$timeRange.StartWeekDay = "monday"
$timeRange.EndWeekDay = "wednesday"
$timeRange.StartHour = 2
$timeRange.EndHour = 8
$tag = @{Key="`key1`"; Value="`value1`"}
$tagspec = New-Object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "instance-event-window"
$tagspec.Tags.Add($tag)
New-EC2InstanceEventWindow `
    -Name `my-event-window` `
    -TagSpecification $tagspec `
    -TimeRange @($timeRange)
```

The following is example output.

```
AssociationTarget     :
CronExpression        :
InstanceEventWindowId : iew-0abcdef1234567890
Name                  : my-event-window
State                 : creating
Tags                  : {key1}
TimeRanges            : {Amazon.EC2.Model.InstanceEventWindowTimeRange}
```

###### To create an event window with a cron expression

Use the [New-EC2InstanceEventWindow](../../../powershell/latest/reference/items/New-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/New-EC2InstanceEventWindow.md")
cmdlet.

```
$tag = @{Key="`key1`"; Value="`value1`"}
$tagspec = New-Object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "instance-event-window"
$tagspec.Tags.Add($tag)
New-EC2InstanceEventWindow `
    -Name `my-event-window` `
    -TagSpecification $tagspec`
    -CronExpression "`* 21-23 * * 2,3`"
```

The following is example output.

```
AssociationTarget     :
CronExpression        : * 21-23 * * 2,3
InstanceEventWindowId : iew-0abcdef1234567890
Name                  : my-event-window
State                 : creating
Tags                  : {key1}
TimeRanges            : {}
```

## Associate a target with an event window

After you create an event window, you can associate targets with the
event window. You can associate only one type of target with an event window.
You can specify instance IDs, Dedicated Host IDs, or instance tags.

Console

###### To associate targets with an event window

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Events**.
3. Select the event window to modify.
4. Choose **Actions**, **Modify instance event window**.

AWS CLI

###### To associate instance tags with an event window

Use the [associate-instance-event-window](../../../cli/latest/reference/ec2/associate-instance-event-window.md "../../../cli/latest/reference/ec2/associate-instance-event-window.md") command.

```
aws ec2 associate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target "InstanceTags=[{Key=`k2`,Value=`v2`},{Key=`k1`,Value=`v1`}]"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [],
            "Tags": [
                {
                    "Key": "k2",
                    "Value": "v2"
                },
                {
                    "Key": "k1",
                    "Value": "v1"
                }
            ],
            "DedicatedHostIds": []
        },
        "State": "creating"
    }
}
```

###### To associate instance IDs with an event window

Use the [associate-instance-event-window](../../../cli/latest/reference/ec2/associate-instance-event-window.md "../../../cli/latest/reference/ec2/associate-instance-event-window.md") command.

```
aws ec2 associate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target "InstanceIds=`i-1234567890abcdef0`,`i-0598c7d356eba48d7`"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [
                "i-1234567890abcdef0",
                "i-0598c7d356eba48d7"
            ],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating"
    }
}
```

###### To associate a Dedicated Host with an event window

Use the [associate-instance-event-window](../../../cli/latest/reference/ec2/associate-instance-event-window.md "../../../cli/latest/reference/ec2/associate-instance-event-window.md") command.

```
aws ec2 associate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target "DedicatedHostIds=`h-029fa35a02b99801d`"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [],
            "Tags": [],
            "DedicatedHostIds": [
                "h-029fa35a02b99801d"
            ]
        },
        "State": "creating"
    }
}
```

PowerShell

###### To associate instance tags with an event window

Use the [Register-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md")
cmdlet.

```
$tag1 = @{Key="key1"; Value="value1"}
$tag2 = @{Key="key2"; Value="value2"}
Register-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_InstanceTag @($tag1,$tag2)
```

###### To associate instance IDs with an event window

Use the [Register-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md")
cmdlet.

```
Register-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_InstanceId `i-1234567890abcdef0`, `i-0598c7d356eba48d7`
```

###### To associate a Dedicated Host with an event window

Use the [Register-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Register-EC2InstanceEventWindow.md")
cmdlet.

```
Register-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_DedicatedHostId `h-029fa35a02b99801d`
```

## Disassociate a target from an event window

Console

###### To disassociate targets with an event window

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Events**.
3. Select the event window to modify.
4. Choose **Actions**, **Modify instance event window**.

AWS CLI

###### To disassociate instance tags from an event window

Use the [disassociate-instance-event-window](../../../cli/latest/reference/ec2/disassociate-instance-event-window.md "../../../cli/latest/reference/ec2/disassociate-instance-event-window.md") command.

```
aws ec2 disassociate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target "InstanceTags=[{Key=`k2`,Value=`v2`},{Key=`k1`,Value=`v1`}]"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating"
    }
}
```

###### To disassociate instance IDs from an event window

Use the [disassociate-instance-event-window](../../../cli/latest/reference/ec2/disassociate-instance-event-window.md "../../../cli/latest/reference/ec2/disassociate-instance-event-window.md") command.

```
aws ec2 disassociate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target "InstanceIds=`i-1234567890abcdef0`,`i-0598c7d356eba48d7`"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating"
    }
}
```

###### To disassociate a Dedicated Host from an event window

Use the [disassociate-instance-event-window](../../../cli/latest/reference/ec2/disassociate-instance-event-window.md "../../../cli/latest/reference/ec2/disassociate-instance-event-window.md") command.

```
aws ec2 disassociate-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --association-target DedicatedHostIds=`h-029fa35a02b99801d`
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating"
    }
}
```

PowerShell

###### To disassociate instance tags from an event window

Use the [Unregister-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md")
cmdlet.

```
$tag1 = @{Key="key1"; Value="value1"}
$tag2 = @{Key="key2"; Value="value2"}
Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_InstanceTag @($tag1, $tag2)
```

###### To disassociate instance IDs from an event window

Use the [Unregister-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md")
cmdlet.

```
Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_InstanceId `i-1234567890abcdef0`, `i-0598c7d356eba48d7`
```

###### To disassociate a Dedicated Host from an event window

Use the [Unregister-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Unregister-EC2InstanceEventWindow.md")
cmdlet.

```
Unregister-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -AssociationTarget_DedicatedHostId `h-029fa35a02b99801d`
```

## Modify an event window

You can modify all of the fields of an event window except its ID. For
example, when daylight savings begin, you might want to modify the event window
schedule. For existing event windows, you might want to add or remove
targets.

You can modify either a time range or a cron expression when
modifying the event window, but not both.

Console

###### To modify an event window

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event windows**.
4. Select the event window to modify, and then choose
   **Actions**, **Modify instance
   event window**.
5. Modify the fields in the event window, and then choose
   **Modify event window**.

AWS CLI

###### To modify the time range of an event window

Use the [modify-instance-event-window](../../../cli/latest/reference/ec2/modify-instance-event-window.md "../../../cli/latest/reference/ec2/modify-instance-event-window.md") command.

```
aws ec2 modify-instance-event-window
    --instance-event-window-id `iew-0abcdef1234567890` \
    --time-range StartWeekDay=`monday`,StartHour=`2`,EndWeekDay=`wednesday`,EndHour=`8`
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "TimeRanges": [
            {
                "StartWeekDay": "monday",
                "StartHour": 2,
                "EndWeekDay": "wednesday",
                "EndHour": 8
            }
        ],
        "Name": "myEventWindowName",
        "AssociationTarget": {
            "InstanceIds": [
                "i-0abcdef1234567890",
                "i-0be35f9acb8ba01f0"
            ],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating",
        "Tags": [
            {
                "Key": "K1",
                "Value": "V1"
            }
        ]
    }
}
```

###### To modify a set of time ranges for an event window

Use the [modify-instance-event-window](../../../cli/latest/reference/ec2/modify-instance-event-window.md "../../../cli/latest/reference/ec2/modify-instance-event-window.md") command.

```
aws ec2 modify-instance-event-window
    --instance-event-window-id `iew-0abcdef1234567890` \
    --time-range '[{"StartWeekDay": "`monday`", "StartHour": `2`, "EndWeekDay": "`wednesday`", "EndHour": `8`},
	  {"StartWeekDay": "`thursday`", "StartHour": `2`, "EndWeekDay": "`friday`", "EndHour": `8`}]'
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "TimeRanges": [
            {
                "StartWeekDay": "monday",
                "StartHour": 2,
                "EndWeekDay": "wednesday",
                "EndHour": 8
            },
            {
                "StartWeekDay": "thursday",
                "StartHour": 2,
                "EndWeekDay": "friday",
                "EndHour": 8
            }
        ],
        "Name": "myEventWindowName",
        "AssociationTarget": {
            "InstanceIds": [
                "i-0abcdef1234567890",
                "i-0be35f9acb8ba01f0"
            ],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating",
        "Tags": [
            {
                "Key": "K1",
                "Value": "V1"
            }
        ]
    }
}
```

###### To modify the cron expression of an event window

Use the [modify-instance-event-window](../../../cli/latest/reference/ec2/modify-instance-event-window.md "../../../cli/latest/reference/ec2/modify-instance-event-window.md") command.

```
aws ec2 modify-instance-event-window
    --instance-event-window-id `iew-0abcdef1234567890` \
    --cron-expression "`* 21-23 * * 2,3`"
```

The following is example output.

```
{
    "InstanceEventWindow": {
        "InstanceEventWindowId": "iew-0abcdef1234567890",
        "Name": "myEventWindowName",
        "CronExpression": "* 21-23 * * 2,3",
        "AssociationTarget": {
            "InstanceIds": [
                "i-0abcdef1234567890",
                "i-0be35f9acb8ba01f0"
            ],
            "Tags": [],
            "DedicatedHostIds": []
        },
        "State": "creating",
        "Tags": [
            {
                "Key": "K1",
                "Value": "V1"
            }
        ]
    }
}
```

PowerShell

###### To modify the time range of an event window

Use the [Edit-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Edit-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Edit-EC2InstanceEventWindow.md")
cmdlet.

```
$timeRange1 = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest
$timeRange1.StartWeekDay = "monday"
$timeRange1.EndWeekDay = "wednesday"
$timeRange1.StartHour = 2
$timeRange1.EndHour = 8
$timeRange2 = New-Object Amazon.EC2.Model.InstanceEventWindowTimeRangeRequest
$timeRange2.StartWeekDay = "thursday"
$timeRange2.EndWeekDay = "friday"
$timeRange2.StartHour = 1
$timeRange2.EndHour = 6
Edit-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -TimeRange @($timeRange1, $timeRange2)
```

###### To modify the cron expression of an event window

Use the [Edit-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Edit-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Edit-EC2InstanceEventWindow.md")
cmdlet.

```
Edit-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -CronExpression "`* 21-23 * * 2,3`"
```

## Delete an event window

You can delete one event window at a time.

Console

###### To delete an event window

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Events**.
3. Choose **Actions**, **Manage
   event windows**.
4. Select the event window to delete, and then choose
   **Actions**, **Delete instance
   event window**.
5. When prompted, enter `delete`, and
   then choose **Delete**.

AWS CLI

###### To delete an event window

Use the [delete-instance-event-window](../../../cli/latest/reference/ec2/delete-instance-event-window.md "../../../cli/latest/reference/ec2/delete-instance-event-window.md") command and specify
the event window to delete.

```
aws ec2 delete-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890`
```

###### To force-delete an event window

Use the `--force-delete` parameter if the event
window is currently associated with targets.

```
aws ec2 delete-instance-event-window \
    --instance-event-window-id `iew-0abcdef1234567890` \
    --force-delete
```

PowerShell

###### To delete an event window

Use the [Remove-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Remove-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Remove-EC2InstanceEventWindow.md")
cmdlet.

```
Remove-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890`
```

###### To force-delete an event window

Use the [Remove-EC2InstanceEventWindow](../../../powershell/latest/reference/items/Remove-EC2InstanceEventWindow.md "../../../powershell/latest/reference/items/Remove-EC2InstanceEventWindow.md")
cmdlet.

```
Remove-EC2InstanceEventWindow `
    -InstanceEventWindowId `iew-0abcdef1234567890` `
    -ForceDelete $true
```
