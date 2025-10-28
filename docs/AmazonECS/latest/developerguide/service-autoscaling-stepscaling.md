# Use predefined increments based on CloudWatch alarms to scale Amazon ECS services

With step scaling policies, you create and manage the CloudWatch alarms that invoke
the scaling process. When an alarm is breached, Amazon ECS initiates the scaling policy
associated with that alarm. The step scaling policy scales tasks using a set of
adjustments, known as step adjustments. The size of the adjustment varies based on the
magnitude of the alarm breach.

- If the breach exceeds the first threshold, Amazon ECS applies the first step
  adjustment.
- If the breach exceeds the second threshold, Amazon ECS applies the second step
  adjustment, and so on.
  We strongly recommend that you use target tracking scaling policies to scale on metrics
  like average CPU utilization or average request count per target. Metrics that decrease
  when capacity increases and increase when capacity decreases can be used to
  proportionally scale out or in the number of tasks using target tracking. This helps
  ensure that Amazon ECS follows the demand curve for your applications
  closely.
