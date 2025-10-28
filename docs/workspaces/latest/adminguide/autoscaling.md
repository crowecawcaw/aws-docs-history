# Auto scaling for WorkSpaces Pools

Auto Scaling lets you change the size of your pools automatically to match the supply
of available instances to user demand. The size of your pool determines the number of
users who can stream concurrently. One instance is required for each user session. You
can specify your pool capacity in terms of instances. Based on your pool configurations
and auto scaling policies, the required number of instances will be made available. You
can define scaling policies that adjust the size of your pool automatically based on a
variety of utilization metrics, and optimize the number of available instances to match
user demand. You can also choose to turn off automatic scaling and make the pool run at
a fixed size.

###### Note

- As you develop your plan for WorkSpaces Pools scaling, make sure that your network
  configuration meets your requirements.
- When you use scaling, you work with the Application Auto Scaling API. For Auto Scaling to work correctly with
  WorkSpaces Pools, Application Auto Scaling requires permission to describe and update your pools
  and describe your Amazon CloudWatch alarms, and permissions to modify your pool
  capacity on your behalf.
  The following topics provide information to help you understand and use Auto Scaling
  for WorkSpaces Pools.

###### Contents

- [Scaling concepts](#autoscaling-concepts "#autoscaling-concepts")
- [Managing pool scaling using the
  console](#autoscaling-console "#autoscaling-console")
- [Managing pool scaling using the AWS CLI](#autoscaling-cli "#autoscaling-cli")
- [Additional resources](#autoscaling-additional-resources "#autoscaling-additional-resources")

## Scaling concepts

WorkSpaces Pools scaling is provided by Application Auto Scaling. For more information, see the [Application Auto Scaling API Reference](../../../autoscaling/application/APIReference.md "../../../autoscaling/application/APIReference.md").

To use Auto Scaling with WorkSpaces Pools effectively, you must understand the following
terms and concepts.

**Minimum capacity/minimum user sessions for the pool**

The minimum number of instances. The number of instances can't be
below this value, and scaling policies will not scale your pool below
this value. For example, if you set the
minimum capacity for a pool to 2, your pool will never have less than
2 instances.

**Maximum capacity/maximum user sessions for the pool**

The maximum number of instances. The number of instances can't be
above this value, and scaling policies will not scale your pool above
this value. For example, if you set the
maximum capacity for a pool to 10, your pool will never have more than
10 instances.

**Desired user session capacity**

The total number of sessions that are either running or pending. This
represents the total number of concurrent streaming sessions your pool
can support in a steady state.

**Scaling policy action**

The action that scaling policies perform on your pool when the
**Scaling Policy Condition** is met. You can choose
an action based on **% capacity** or **number
of instance(s)**. For example, if **Desired user
session capacity** is 4 and **Scaling Policy
Action** is set to "Add 25% capacity", **Desired
user session capacity** is increased by 25% to 5 when
**Scaling Policy Condition** is met.

**Scaling policy condition**

The condition that triggers the action set in **Scaling Policy
Action**. This condition includes a scaling policy metric,
a comparison operator, and a threshold. For example, to scale a pool if
the utilization of the pool is greater than 50%, your scaling policy
condition should be "If Capacity Utilization > 50%".

**Scaling policy metric**

Your scaling policy is based on this metric. The following metrics are
available for scaling policies:

**Capacity Utilization**

The percentage of instances in a pool that are being
used. You can use this metric to scale your pool based on
usage of the pool. For example, **Scaling Policy
Condition**: "If Capacity Utilization < 25%"
perform **Scaling Policy Action**: "Remove
25 % capacity".

**Available capacity**

The number of instances in your pool that
are available for users. You can use this metric to maintain
a buffer in your capacity available for users to start
streaming sessions. For example, **Scaling Policy
Condition**: "If Available Capacity < 5"
perform **Scaling Policy Action**: "Add 5
instance(s)".

**Insufficient capacity error**

The number of session requests rejected due to lack of
capacity. You can use this metric to provision new instances
for users who can't start streaming sessions due to lack of
capacity. For example, **Scaling Policy
Condition**: "If Insufficient Capacity Error

> 0" perform **Scaling Policy Action**:
> "Add 1 instance(s)".

## Managing pool scaling using the

console

You can set up and manage scaling by using the WorkSpaces console in either of the
following two ways: During pool creation, or any time, by using the
**Pools** tab. After you create pools, go to the
**Scaling Policies** tab to add new scaling policies for your
pool. For more information, see [Create a WorkSpaces Pool](set-up-pools-create.md "set-up-pools-create.md").

For user environments that vary in number, define scaling policies to control how
scaling responds to demand. If you expect a fixed number of users or have other
reasons for disabling scaling, you can set your pool with a fixed number of
instances for user sessions.

To do this, set the minimum capacity to your desired number of instances. Adjust
the maximum capacity to be at least the value of the minimum capacity. This avoids
validation errors, but the maximum capacity will ultimately be ignored since the
pool will not be scaled. Then, delete all scaling policies for that pool.

###### To set a pool scaling policy using the console

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **Pools**.
3. Select the pool.
4. On that pool's page, scroll down to capacity and scaling.
5. Choose **Edit**.
6. Edit existing policies and set the desired values in their field and choose **Save**.
   The policy changes go into effect within a few minutes.
7. You can also add new capacity and scaling policies by choosing **Add new schedule capacity**,
   **Add new scale out policy**, or **Add new scale in policy**.

The following is an example usage graph of scaling
activity when five users connect to the pool and then disconnect. This example is
from a pool using the following scaling policy values:

- Minimum capacity = 10
- Maximum capacity = 50
- Scale out = If my pool Capacity Utilization is Greater than 75% then add 5
  instances
- Scale in = If my pool Capacity Utilization is Less than 25% then remove 6 instances

###### Note

During the session, 5 new instances will be launched during a scale
out event. During a scale in event, 6 instances will be reclaimed, if
there are enough instances without active user sessions, and the total
number of instances does not drop below the minimum capacity of 10
instances. Instances with running user sessions will not be reclaimed.
Only instances with no user sessions running will be reclaimed.

## Managing pool scaling using the AWS CLI

You can set up and manage pool scaling by using the AWS Command Line Interface (AWS CLI). For
more advanced features such as setting scale-in and scale-out cooldown times, use
the AWS CLI. Before running scaling policy commands, you must register your pool
as a scalable target. To do so, use the following [register-scalable-target](../../../cli/latest/reference/application-autoscaling/register-scalable-target.md "../../../cli/latest/reference/application-autoscaling/register-scalable-target.md") command:

```
`aws application-autoscaling register-scalable-target
 --service-namespace workspaces \
 --resource-id workspacespool/`PoolId` \
 --scalable-dimension workspaces:workspacespool:DesiredUserSessions \
 --min-capacity 1 --max-capacity 5`
```

###### Examples

- [Example 1: Applying a scaling
  policy based on capacity utilization](#autoscaling-cli-utilization "#autoscaling-cli-utilization")
- [Example 2: Applying a scaling policy
  based on insufficient capacity errors](#autoscaling-cli-capacity "#autoscaling-cli-capacity")
- [Example 3: Applying a scaling policy
  based on low capacity utilization](#autoscaling-cli-scale-in "#autoscaling-cli-scale-in")
- [Example 4: Change the pool capacity
  based on a schedule](#autoscaling-cli-schedule "#autoscaling-cli-schedule")
- [Example 5: Applying a target
  tracking scaling policy](#autoscaling-target-tracking "#autoscaling-target-tracking")

### Example 1: Applying a scaling

policy based on capacity utilization

This AWS CLI example sets up a scaling policy that scales out a pool by 25%
if Utilization >= 75%.

The following [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command defines a utilization-based scaling
policy:

```
aws application-autoscaling put-scaling-policy -- cli-input-json file://scale-out-utilization.json
```

The contents of the file `scale-out-utilization.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "workspaces",
    "ResourceId": "workspacespool/`PoolId`",
    "ScalableDimension": "workspaces:workspacespool:DesiredUserSessions",
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
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:e3425d21-16f0-d701-89fb-12f98dac64af:resource/workspaces/workspacespool/PoolId:policyName/scale-out-utilization-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account
number, and policy identifier that apply to you. You can use the policy ARN
returned by the previous command for the `-- alarm-actions`
parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when Available User Session Capacity exceeds 75 percent" \
--metric-name AvailableUserSessionCapacity \
--namespace AWS/WorkSpaces \
--statistic Average \
--period 300 \
--threshold 75 \
--comparison-operator GreaterThanOrEqualToThreshold \
--dimensions "Name=WorkSpaces pool ID,Value=`PoolId`" \
--evaluation-periods 1 --unit Percent \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/workspaces/workspacespool/`PoolId`:policyName/`policyname`"`
```

### Example 2: Applying a scaling policy

based on insufficient capacity errors

This AWS CLI example sets up a scaling policy that scales out the pool by 1
if the pool returns an `InsufficientCapacityError` error.

The following command defines a insufficient capacity-based scaling
policy:

```
`aws application-autoscaling put-scaling-policy -- cli-input-json file://scale-out-capacity.json`
```

The contents of the file `scale-out-capacity.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "workspaces",
    "ResourceId": "workspacespool/`PoolId`",
    "ScalableDimension": "workspaces:workspacespool:DesiredUserSessions",
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
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:f4495f21-0650-470c-88e6-0f393adb64fc:resource/workspaces/workspacespool/PoolId:policyName/scale-out-insufficient-capacity-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account
number, and policy identifier that apply to you. You can use the policy ARN
returned by the previous command for the `--alarm-actions`
parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when out of capacity is > 0" \
--metric-name InsufficientCapacityError \
--namespace AWS/WorkSpaces \
--statistic Maximum \
--period 300 \
--threshold 0 \
--comparison-operator GreaterThanThreshold \
--dimensions "Name=Pool,Value=`PoolId`" \
--evaluation-periods 1 --unit Count \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/workspaces/workspacespool/`PoolId`:policyName/`policyname`"`
```

### Example 3: Applying a scaling policy

based on low capacity utilization

This AWS CLI example sets up a scaling policy that scales in the pool to reduce
actual capacity when `UserSessionsCapacityUtilization` is low.

The following command defines an excess capacity-based scaling policy:

```
`aws application-autoscaling put-scaling-policy -- cli-input-json file://scale-in-capacity.json`
```

The contents of the file `scale-in-capacity.json` are as
follows:

```
{
    "PolicyName": "`policyname`",
    "ServiceNamespace": "workspaces",
    "ResourceId": "workspacespool/`PoolId`",
    "ScalableDimension": "workspaces:workspacespool:DesiredUserSessions",
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
{"PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:12ab3c4d-56789-0ef1-2345-6ghi7jk8lm90:resource/workspaces/workspacespool/PoolId:policyName/scale-in-utilization-policy"}
```

Now, set up a CloudWatch alarm for this policy. Use the names, Region, account
number, and policy identifier that apply to you. You can use the policy ARN
returned by the previous command for the `--alarm-actions`
parameter.

```
`aws cloudwatch put-metric-alarm
--alarm-name `alarmname` \
--alarm-description "Alarm when Capacity Utilization is less than or equal to 25 percent" \
--metric-name UserSessionsCapacityUtilization \
--namespace AWS/WorkSpaces \
--statistic Average \
--period 120 \
--threshold 25 \
--comparison-operator LessThanOrEqualToThreshold \
--dimensions "Name=Pool,Value=`PoolId`" \
--evaluation-periods 10 --unit Percent \
--alarm-actions "arn:aws:autoscaling:`your-region-code`:`account-number-without-hyphens`:scalingPolicy:`policyid`:resource/workspaces/workspacespool/`PoolId`:policyName/`policyname`"`
```

### Example 4: Change the pool capacity

based on a schedule

Changing your pool capacity based on a schedule lets you scale your pool
capacity in response to predictable changes in demand. For example, at the start
of a work day, you might expect a certain number of users to request streaming
connections at one time. To change your pool capacity based on a schedule, you
can use the Application Auto Scaling [PutScheduledAction](../../../autoscaling/application/APIReference/API_PutScheduledAction.md "../../../autoscaling/application/APIReference/API_PutScheduledAction.md") API action or the [put-scheduled-action](../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md "../../../cli/latest/reference/application-autoscaling/put-scheduled-action.md") AWS CLI command.

Before changing your pool capacity, you can list your current pool capacity by
using the WorkSpaces [describe-workspaces-pools](../../../cli/latest/reference/workspaces/describe-workspaces-pools.md "../../../cli/latest/reference/workspaces/describe-workspaces-pools.md") AWS CLI command.

```
aws workspaces describe-workspaces-pools --name `PoolId`
```

The current pool capacity will appear similar to the following output (shown
in JSON format):

```
{
    "CapacityStatus": {
        "AvailableUserSessions": 1,
        "DesiredUserSessions": 1,
        "ActualUserSessions": 1,
        "ActiveUserSessions": 0
    },
}
```

Then, use the `put-scheduled-action` command to create a scheduled
action to change your pool capacity. For example, the following command changes
the minimum capacity to 3 and the maximum capacity to 5 every day at 9:00 AM
UTC.

###### Note

For cron expressions, specify when to perform the action in UTC. For more
information, see [Cron
Expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md#CronExpressions").

```
`aws application-autoscaling put-scheduled-action --service-namespace workspaces \
--resource-id workspacespool/`PoolId` \
--schedule="cron(0 9 * * ? *)" \
--scalable-target-action MinCapacity=3,MaxCapacity=5 \
--scheduled-action-name ExampleScheduledAction \
--scalable-dimension workspaces:workspacespool:DesiredUserSessions`
```

To confirm that the scheduled action to change your pool capacity was
successfully created, run the [describe-scheduled-actions](../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md "../../../cli/latest/reference/application-autoscaling/describe-scheduled-actions.md") command.

```
aws application-autoscaling describe-scheduled-actions --service-namespace workspaces --resource-id workspacespool/`PoolId`
```

If the scheduled action was successfully created, the output appears similar
to the following.

```
{
    "ScheduledActions": [
        {
            "ScalableDimension": "workspaces:workspacespool:DesiredUserSessions",
            "Schedule": "cron(0 9 * * ? *)",
            "ResourceId": "workspacespool/ExamplePool",
            "CreationTime": 1518651232.886,
            "ScheduledActionARN": "<arn>",
            "ScalableTargetAction": {
                "MinCapacity": 3,
                "MaxCapacity": 5
            },
            "ScheduledActionName": "ExampleScheduledAction",
            "ServiceNamespace": "workspaces"
        }
    ]
}
```

For more information, see [Scheduled Scaling](../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-scheduled-scaling.md") in the _Application Auto Scaling User
Guide_.

### Example 5: Applying a target

tracking scaling policy

With target tracking scaling, you can specify a capacity utilization level for
your pool.

When you create a target tracking scaling policy, Application Auto Scaling automatically
creates and manages CloudWatch alarms that trigger the scaling policy. The scaling
policy adds or removes capacity as required to keep capacity utilization at, or
close to, the specified target value. To ensure application availability, your
pool scales out proportionally to the metric as fast as it can but scales in
more gradually.

The following [put-scaling-policy](../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md "../../../cli/latest/reference/application-autoscaling/put-scaling-policy.md") command defines a target tracking scaling policy
that attempts to maintain 75% capacity utilization for a WorkSpaces pool.

```
aws application-autoscaling put-scaling-policy -- cli-input-json file://config.json
```

The contents of the file `config.json` are as follows:

```
{
  "PolicyName":"target-tracking-scaling-policy",
  "ServiceNamespace":"workspaces",
  "ResourceId":"workspacespool/`PoolId`",
  "ScalableDimension":"workspaces:workspacespool:DesiredUserSessions",
  "PolicyType":"TargetTrackingScaling",
  "TargetTrackingScalingPolicyConfiguration":{
    "TargetValue":75.0,
    "PredefinedMetricSpecification":{
      "PredefinedMetricType":"WorkSpacesAverageUserSessionsCapacityUtilization"
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
    "PolicyARN": "arn:aws:autoscaling:us-west-2:123456789012:scalingPolicy:6d8972f3-efc8-437c-92d1-6270f29a66e7:resource/workspaces/workspacespool/PoolId:policyName/target-tracking-scaling-policy",
    "Alarms": [
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-workspacespool/PoolId-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca",
            "AlarmName": "TargetTracking-workspacespool/PoolId-AlarmHigh-d4f0770c-b46e-434a-a60f-3b36d653feca"
        },
        {
            "AlarmARN": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:TargetTracking-workspacespool/PoolId-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d",
            "AlarmName": "TargetTracking-workspacespool/PoolId-AlarmLow-1b437334-d19b-4a63-a812-6c67aaf2910d"
        }
    ]
}
```

For more information, see [Target
Tracking Scaling Policies](../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md "../../../autoscaling/application/userguide/application-auto-scaling-target-tracking.md") in the _Application Auto Scaling User
Guide_.

## Additional resources

To learn more about using the Application Auto Scaling AWS CLI commands or API actions, see the
following resources:

- [application-autoscaling](../../../cli/latest/reference/application-autoscaling.md "../../../cli/latest/reference/application-autoscaling.md") section of the
  _AWS CLI Command Reference_
- [Application Auto Scaling API Reference](../../../autoscaling/application/APIReference.md "../../../autoscaling/application/APIReference.md")
- [Application Auto Scaling User Guide](../../../autoscaling/application/userguide.md "../../../autoscaling/application/userguide.md")
