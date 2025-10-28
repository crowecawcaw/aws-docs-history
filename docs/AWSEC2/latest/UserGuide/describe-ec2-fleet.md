# Describe an EC2 Fleet, its instances, and its events

You can describe your EC2 Fleet configuration, the instances in your EC2 Fleet, and the event
history of your EC2 Fleet.

###### Tasks

- [Describe your EC2 Fleet](#describe-all-ec2-fleets "#describe-all-ec2-fleets")
- [Describe all instances in your EC2 Fleet](#describe-instances-in-ec2-fleet "#describe-instances-in-ec2-fleet")
- [Describe the event history for your EC2 Fleet](#describe-ec2-fleet-event-history "#describe-ec2-fleet-event-history")

## Describe your EC2 Fleet

AWS CLI

###### To describe your EC2 Fleet

Use the [describe-fleets](../../../cli/latest/reference/ec2/describe-fleets.md "../../../cli/latest/reference/ec2/describe-fleets.md")
command.

```
aws ec2 describe-fleets \
    --fleet-ids `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

The following is example output.

```
{
    "Fleets": [
        {
            "ActivityStatus": "fulfilled",
            "CreateTime": "2022-02-09T03:35:52+00:00",
            "FleetId": "fleet-364457cd-3a7a-4ed9-83d0-7b63e51bb1b7",
            "FleetState": "active",
            "ExcessCapacityTerminationPolicy": "termination",
            "FulfilledCapacity": 2.0,
            "FulfilledOnDemandCapacity": 0.0,
            "LaunchTemplateConfigs": [
                {
                    "LaunchTemplateSpecification": {
                        "LaunchTemplateName": "my-launch-template",
                        "Version": "$Latest"
                    }
                }
            ],
            "TargetCapacitySpecification": {
                "TotalTargetCapacity": 2,
                "OnDemandTargetCapacity": 0,
                "SpotTargetCapacity": 2,
                "DefaultTargetCapacityType": "spot"
            },
            "TerminateInstancesWithExpiration": false,
            "Type": "maintain",
            "ReplaceUnhealthyInstances": false,
            "SpotOptions": {
                "AllocationStrategy": "capacity-optimized",
                "InstanceInterruptionBehavior": "terminate"
            },
            "OnDemandOptions": {
                "AllocationStrategy": "lowestPrice"
            }
        }
    ]
}
```

PowerShell

###### To describe your EC2 Fleet

Use the [Get-EC2FleetList](../../../powershell/latest/reference/items/Get-EC2FleetList.md "../../../powershell/latest/reference/items/Get-EC2FleetList.md")
cmdlet.

```
Get-EC2FleetList `
    -FleetId `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

## Describe all instances in your EC2 Fleet

The returned list of running instances is refreshed periodically and
might be out of date.

AWS CLI

###### To describe the instances for the specified EC2 Fleet

Use the [describe-fleet-instances](../../../cli/latest/reference/ec2/describe-fleet-instances.md "../../../cli/latest/reference/ec2/describe-fleet-instances.md") command.

```
aws ec2 describe-fleet-instances \
    --fleet-id `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

The following is example output.

```
{
    "ActiveInstances": [
        {
            "InstanceId": "i-09cd595998cb3765e",
            "InstanceHealth": "healthy",
            "InstanceType": "m4.large",
            "SpotInstanceRequestId": "sir-86k84j6p"
        },
        {
            "InstanceId": "i-09cf95167ca219f17",
            "InstanceHealth": "healthy",
            "InstanceType": "m4.large",
            "SpotInstanceRequestId": "sir-dvxi7fsm"
        }
    ],
    "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE"
}
```

PowerShell

###### To describe the instances for the specified EC2 Fleet

Use the [Get-EC2FleetInstanceList](../../../powershell/latest/reference/items/Get-EC2FleetInstanceList.md "../../../powershell/latest/reference/items/Get-EC2FleetInstanceList.md") cmdlet.

```
Get-EC2FleetInstanceList `
    -FleetId `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`
```

## Describe the event history for your EC2 Fleet

For more information about the events in the event history, see [EC2 Fleet event types](monitor-ec2-fleet-using-eventbridge.md#ec2-fleet-event-types "monitor-ec2-fleet-using-eventbridge.md#ec2-fleet-event-types").

AWS CLI

###### To describe the events for the specified EC2 Fleet

Use the [describe-fleet-history](../../../cli/latest/reference/ec2/describe-fleet-history.md "../../../cli/latest/reference/ec2/describe-fleet-history.md") command.

```
aws ec2 describe-fleet-history \
    --fleet-id `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` \
    --start-time `2020-06-01T00:00:00Z`
```

The following is example output.

```
{
    "HistoryRecords": [
        {
            "EventInformation": {
                "EventSubType": "submitted"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:05.000Z"
        },
        {
            "EventInformation": {
                "EventSubType": "active"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:15.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "t2.small, ami-07c8bc5c1ce9598c3, ...",
                "EventSubType": "progress"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "{\"instanceType\":\"t2.small\", ...}",
                "EventSubType": "launched",
                "InstanceId": "i-083a1c446e66085d2"
            },
            "EventType": "instanceChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "{\"instanceType\":\"t2.small\", ...}",
                "EventSubType": "launched",
                "InstanceId": "i-090db02406cc3c2d6"
            },
            "EventType": "instanceChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        }
    ],
    "FleetId": "fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE",
    "LastEvaluatedTime": "1970-01-01T00:00:00.000Z",
    "StartTime": "2020-06-01T00:00:00.000Z"
}
```

PowerShell

###### To describe the events for the specified EC2 Fleet

Use the [Get-EC2FleetHistory](../../../powershell/latest/reference/items/Get-EC2FleetHistory.md "../../../powershell/latest/reference/items/Get-EC2FleetHistory.md")
cmdlet.

```
Get-EC2FleetHistory `
    -FleetId `fleet-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE` `
    -UtcStartTime `2020-06-01T00:00:00Z`
```
