# Understand automatic scaling for

Spot Fleet

_Automatic scaling_ enables your Spot Fleet to increase or decrease its
target capacity based on demand. With automatic scaling, a Spot Fleet can either launch
instances (scale out) or terminate instances (scale in) within a specified range, in
response to one or more scaling policies.

Automatic scaling for Spot Fleet is made possible by a combination of the Amazon EC2, Amazon CloudWatch,
and Application Auto Scaling APIs. Spot Fleet requests are created with Amazon EC2, alarms are created with CloudWatch,
and scaling policies are created with Application Auto Scaling.

**Types of automatic scaling**

Spot Fleet supports the following types of automatic scaling:

- [Target tracking scaling](spot-fleet-target-tracking.md "spot-fleet-target-tracking.md")
  – Increase or decrease
  the current capacity of the fleet by targeting a
  value for a specific metric. This is similar to the way that your thermostat
  maintains the temperature of your home—you select the desired temperature
  and the thermostat does the rest.
- [Step scaling](spot-fleet-step-scaling.md "spot-fleet-step-scaling.md") – Increase
  or decrease the current capacity of the fleet based on a set of scaling
  adjustments, known as step adjustments, that vary based on the size of the alarm
  breach.
- [Scheduled scaling](spot-fleet-scheduled-scaling.md "spot-fleet-scheduled-scaling.md") –
  Increase or decrease the current capacity of the fleet based on the date and
  time.

## Considerations

When using automatic scaling for your Spot Fleet, consider the following:

- **Instance weighting** – If you're
  using [instance
  weighting](ec2-fleet-instance-weighting.md "ec2-fleet-instance-weighting.md"), keep in mind that Spot Fleet can exceed the target capacity as
  needed. Fulfilled capacity can be a floating-point number but target
  capacity must be an integer, so Spot Fleet rounds up to the next integer. You must
  take these behaviors into account when you look at the outcome of a scaling
  policy when an alarm is triggered. For example, suppose that the target
  capacity is 30, the fulfilled capacity is 30.1, and the scaling policy
  subtracts 1. When the alarm is triggered, the automatic scaling process
  subtracts 1 from 30.1 to get 29.1 and then rounds it up to 30, so no scaling
  action is taken. As another example, suppose that you selected instance
  weights of 2, 4, and 8, and a target capacity of 10, but no weight 2
  instances were available so Spot Fleet provisioned instances of weights 4 and 8
  for a fulfilled capacity of 12. If the scaling policy decreases target
  capacity by 20% and an alarm is triggered, the automatic scaling process
  subtracts 12\*0.2 from 12 to get 9.6 and then rounds it up to 10, so no
  scaling action is taken.
- **Cooldown period** – The scaling
  policies that you create for Spot Fleet support a cooldown period. This is the
  number of seconds after a scaling activity completes where previous
  trigger-related scaling activities can influence future scaling events. For
  scale-out policies, while the cooldown period is in effect, the capacity
  that has been added by the previous scale-out event that initiated the
  cooldown is calculated as part of the desired capacity for the next scale
  out. The intention is to continuously (but not excessively) scale out. For
  scale in policies, the cooldown period is used to block subsequent scale in
  requests until it has expired. The intention is to scale in conservatively
  to protect your application's availability. However, if another alarm
  triggers a scale-out policy during the cooldown period after a scale-in,
  automatic scaling scales out your scalable target immediately.
- **Use detailed monitoring** – We
  recommend that you scale based on instance metrics with a 1-minute frequency
  because that ensures a faster response to utilization changes. Scaling on
  metrics with a 5-minute frequency can result in slower response time and
  scaling on stale metric data. To send metric data for your instances to CloudWatch
  in 1-minute periods, you must specifically enable detailed monitoring. For
  more information, see [Manage detailed monitoring for your EC2 instances](manage-detailed-monitoring.md "manage-detailed-monitoring.md") and [Create a Spot Fleet request using defined
  parameters](create-spot-fleet.md#create-spot-fleet-advanced "create-spot-fleet.md#create-spot-fleet-advanced").
- **AWS CLI** – If you use the AWS CLI for
  configuring scaling for Spot Fleet, you'll use the [application-autoscaling](../../../cli/latest/reference/application-autoscaling.md "../../../cli/latest/reference/application-autoscaling.md") commands.
