# Managing Fleet Scaling Using the AWS CLI for Amazon WorkSpaces Applications

You can set up and manage fleet scaling by using the AWS Command Line Interface (AWS CLI). For more
advanced features such as setting up multiple scaling policies or setting scale-in and
scale-out cooldown times, use the AWS CLI. Before running scaling policy commands, you
must register your fleet as a scalable target. To do so, use the following [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command:

```
`aws application-autoscaling register-scalable-target
 --service-namespace appstream \
 --resource-id fleet/`fleetname` \
 --scalable-dimension appstream:fleet:DesiredCapacity \
 --min-capacity 1 --max-capacity 5`
```

###### Examples

- [Example 1: Applying a Scaling Policy Based on Capacity Utilization](#autoscaling-cli-utilization "#autoscaling-cli-utilization")
- [Example 2: Applying a Scaling Policy Based on Insufficient Capacity Errors](#autoscaling-cli-capacity "#autoscaling-cli-capacity")
- [Example 3: Applying a Scaling Policy Based on Low Capacity Utilization](#autoscaling-cli-scale-in "#autoscaling-cli-scale-in")
- [Example 4: Change the Fleet Capacity Based on a Schedule](#autoscaling-cli-schedule "#autoscaling-cli-schedule")
- [Example 5: Applying a Target Tracking Scaling Policy](#autoscaling-target-tracking "#autoscaling-target-tracking")

## Example 1: Applying a Scaling Policy Based on Capacity Utilization

This AWS CLI example sets up a scaling policy that scales out a fleet by 25% if
Utilization >= 75%.

The following [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command defines a utilization-based scaling
policy:

```
aws application-autoscaling put-scaling-policy --cli-input-json file://scale-out-utilization.json
```

The contents of the file `scale-out-utilization.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "appstream",
    "ResourceId": "fleet/`fleetname`",
    "ScalableDimension": "appstream:fleet:DesiredCapacity",
    "PolicyType": "StepScaling",
    "StepScalingPolicyConfiguration": {
        "AdjustmentType": "PercentChangeInCapacity",
        "StepAdjustments": [
            {
                "MetricIntervalLowerBound": 0,
                "ScalingAdjustment": 25
            }
        ],
        "Cooldown": 120
    }
}
```

If the command is successful, the output is similar to the following, although
some details are unique to your account and Region. In this example, the policy
identifier is `e3425d21-16f0-d701-89fb-12f98dac64af`.

```
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:e3425d21-16f0-d701-89fb-12f98dac64af:resource/appstream/fleet/SampleFleetName:policyName/scale-out-utilization-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account number,
and policy identifier that apply to you. You can use the policy ARN returned by the
previous command for the `--alarm-actions` parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when Capacity Utilization exceeds 75 percent" \
--metric-name CapacityUtilization \
--namespace AWS/AppStream \
--statistic Average \
--period 300 \
--threshold 75 \
--comparison-operator GreaterThanOrEqualToThreshold \
--dimensions "Name=Fleet,Value=`fleetname`" \
--evaluation-periods 1 --unit Percent \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/appstream/fleet/`fleetname`:policyName/`policyname`"`
```

## Example 2: Applying a Scaling Policy Based on Insufficient Capacity Errors

This AWS CLI example sets up a scaling policy that scales out the fleet by 1 if
the fleet returns an `InsufficientCapacityError` error.

The following command defines a insufficient capacity-based scaling policy:

```
`aws application-autoscaling put-scaling-policy --cli-input-json file://scale-out-capacity.json`
```

The contents of the file `scale-out-capacity.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "appstream",
    "ResourceId": "fleet/`fleetname`",
    "ScalableDimension": "appstream:fleet:DesiredCapacity",
    "PolicyType": "StepScaling",
    "StepScalingPolicyConfiguration": {
        "AdjustmentType": "ChangeInCapacity",
        "StepAdjustments": [
            {
                "MetricIntervalLowerBound": 0,
                "ScalingAdjustment": 1
            }
        ],
        "Cooldown": 120
    }
}
```

If the command is successful, the output is similar to the following, although
some details are unique to your account and Region. In this example, the policy
identifier is `f4495f21-0650-470c-88e6-0f393adb64fc`.

```
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:f4495f21-0650-470c-88e6-0f393adb64fc:resource/appstream/fleet/SampleFleetName:policyName/scale-out-insufficient-capacity-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account number,
and policy identifier that apply to you. You can use the policy ARN returned by the
previous command for the `--alarm-actions` parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when out of capacity is > 0" \
--metric-name InsufficientCapacityError \
--namespace AWS/AppStream \
--statistic Maximum \
--period 300 \
--threshold 0 \
--comparison-operator GreaterThanThreshold \
--dimensions "Name=Fleet,Value=`fleetname`" \
--evaluation-periods 1 --unit Count \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/appstream/fleet/`fleetname`:policyName/`policyname`"`
```

## Example 3: Applying a Scaling Policy Based on Low Capacity Utilization

This AWS CLI example sets up a scaling policy that scales in the fleet to reduce
actual capacity when `CapacityUtilization` is low.

The following command defines an excess capacity-based scaling policy:

```
`aws application-autoscaling put-scaling-policy --cli-input-json file://scale-in-capacity.json`
```

The contents of the file `scale-in-capacity.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "appstream",
    "ResourceId": "fleet/`fleetname`",
    "ScalableDimension": "appstream:fleet:DesiredCapacity",
    "PolicyType": "StepScaling",
    "StepScalingPolicyConfiguration": {
        "AdjustmentType": "PercentChangeInCapacity",
        "StepAdjustments": [
            {
                "MetricIntervalUpperBound": 0,
                "ScalingAdjustment": -25
            }
        ],
        "Cooldown": 360
    }
}
```

If the command is successful, the output is similar to the following, although
some details are unique to your account and Region. In this example, the policy
identifier is `12ab3c4d-56789-0ef1-2345-6ghi7jk8lm90`.

```
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:12ab3c4d-56789-0ef1-2345-6ghi7jk8lm90:resource/appstream/fleet/SampleFleetName:policyName/scale-in-utilization-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account number,
and policy identifier that apply to you. You can use the policy ARN returned by the
previous command for the `--alarm-actions` parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when Capacity Utilization is less than or equal to 25 percent" \
--metric-name CapacityUtilization \
--namespace AWS/AppStream \
--statistic Average \
--period 120 \
--threshold 25 \
--comparison-operator LessThanOrEqualToThreshold \
--dimensions "Name=Fleet,Value=`fleetname`" \
--evaluation-periods 10 --unit Percent \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/appstream/fleet/`fleetname`:policyName/`policyname`"`
```

## Example 4: Change the Fleet Capacity Based on a Schedule

Changing your fleet capacity based on a schedule lets you scale your fleet
capacity in response to predictable changes in demand. For example, at the start of
a work day, you might expect a certain number of users to request streaming
connections at one time. To change your fleet capacity based on a schedule, you can
use the Application Auto Scaling [PutScheduledAction](../../../autoscaling/application/APIReference/API_PutScheduledAction.md "../../../autoscaling/application/APIReference/API_PutScheduledAction.md") API action or the [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md") AWS CLI command.

Before changing your fleet capacity, you can list your current fleet capacity by
using the WorkSpaces Applications [describe-fleets](../../../cli/latest/reference/appstream/describe-fleets.md "../../../cli/latest/reference/appstream/describe-fleets.md") AWS CLI command.

```
aws appstream describe-fleets --name `fleetname`
```

The current fleet capacity will appear similar to the following output (shown in
JSON format):

```
{
    {
            "ComputeCapacityStatus": {
                "Available": 1,
                "Desired": 1,
                "Running": 1,
                "InUse": 0
            },
}
```

Then, use the `put-scheduled-action` command to create a scheduled
action to change your fleet capacity. For example, the following command changes the
minimum capacity to 3 and the maximum capacity to 5 every day at 9:00 AM UTC.

###### Note

For cron expressions, specify when to perform the action in UTC. For more
information, see [Cron Expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions").

```
`aws application-autoscaling put-scheduled-action --service-namespace appstream \
--resource-id fleet/`fleetname` \
--schedule="cron(0 9 * * ? *)" \
--scalable-target-action MinCapacity=3,MaxCapacity=5 \
--scheduled-action-name ExampleScheduledAction \
--scalable-dimension appstream:fleet:DesiredCapacity`
```

To confirm that the scheduled action to change your fleet capacity was
successfully created, run the [describe-scheduled-actions](../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md "../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md") command.

```
aws application-autoscaling describe-scheduled-actions --service-namespace appstream --resource-id fleet/`fleetname`
```

If the scheduled action was successfully created, the output appears similar to
the following.

```
{
    "ScheduledActions": [
        {
            "ScalableDimension": "appstream:fleet:DesiredCapacity",
            "Schedule": "cron(0 9 * * ? *)",
            "ResourceId": "fleet/ExampleFleet",
            "CreationTime": 1518651232.886,
            "ScheduledActionARN": "<arn>",
            "ScalableTargetAction": {
                "MinCapacity": 3,
                "MaxCapacity": 5
            },
            "ScheduledActionName": "ExampleScheduledAction",
            "ServiceNamespace": "appstream"
        }
    ]
}
```

For more information, see [Scheduled
Scaling](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md") in the _Application Auto Scaling User Guide_.

## Example 5: Applying a Target Tracking Scaling Policy

With target tracking scaling, you can specify a capacity utilization level for
your fleet.

When you create a target tracking scaling policy, Application Auto Scaling automatically creates
and manages CloudWatch alarms that trigger the scaling policy. The scaling policy adds or
removes capacity as required to keep capacity utilization at, or close to, the
specified target value. To ensure application availability, your fleet scales out
proportionally to the metric as fast as it can but scales in more gradually.

The following [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command defines a target tracking scaling policy
that attempts to maintain 75% capacity utilization for an WorkSpaces Applications fleet.

```
aws application-autoscaling put-scaling-policy --cli-input-json file://config.json
```

The contents of the file `config.json` are as follows:

```
{
  "PolicyName":"target-tracking-scaling-policy",
  "ServiceNamespace":"appstream",
  "ResourceId":"fleet/`fleetname`",
  "ScalableDimension":"appstream:fleet:DesiredCapacity",
  "PolicyType":"TargetTrackingScaling",
  "TargetTrackingScalingPolicyConfiguration":{
    "TargetValue":75.0,
    "PredefinedMetricSpecification":{
      "PredefinedMetricType":"AppStreamAverageCapacityUtilization"
    },
    "ScaleOutCooldown":300,
    "ScaleInCooldown":300
  }
}
```

If the command is successful, the output is similar to the following, although
some details are unique to your account and Region. In this example, the policy
identifier is 6d8972f3-efc8-437c-92d1-6270f29a66e7.

```
{
    "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/appstream/fleet/fleetname:policyName/target-tracking-scaling-policy",
    "Alarms": [
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-fleet/fleetname-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
            "AlarmName": "TargetTracking-fleet/fleetname-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
        },
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-fleet/fleetname-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
            "AlarmName": "TargetTracking-fleet/fleetname-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
        }
    ]
}
```

For more information, see [Target
Tracking Scaling Policies](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md") in the _Application Auto Scaling User
Guide_.
