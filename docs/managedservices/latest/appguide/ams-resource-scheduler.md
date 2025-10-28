# AWS Managed Services Resource Scheduler

Use AWS Managed Services (AMS) Resource Scheduler to schedule the automatic start and stop of AutoScaling groups, Amazon EC2 instances, and RDS instances in your account.
This helps reduce infrastructure costs where the resources are not meant to be running 24/7. The solution is built on top of
[Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/ "https://aws.amazon.com/solutions/implementations/instance-scheduler/"), but contains additional features
and customizations specific to AMS needs.

###### Note

By default, AMS Resource Scheduler doesn't interact with resources that aren't part of an AWS CloudFormation stack.
The resource must be part of a stack that starts with "stack-" , "sc-" or "SC-". To schedule the resources that
are not part of a CloudFormation stack, you can update the Resource Scheduler stack parameter `ScheduleNonStackResources` to `Yes`.

AMS Resource Scheduler uses periods and schedules:

- _Periods_ define the times when Resource Scheduler runs, such as start time, end time, and days of the month.
- _Schedules_ contain your defined periods, along with additional configurations, such as SSM maintenance window,
  timezone, hibernate setting, and so forth; and specify when resources should run, given the configured period rules.
  You can configure these periods and schedules using AMS Resource Scheduler's automated change types (CTs).

For full details on the settings available for AMS Resource Scheduler, see the corresponding AWS Instance Scheduler documentation at
[Solution components](../../../solutions/latest/instance-scheduler-on-aws/components.md "../../../solutions/latest/instance-scheduler-on-aws/components.md"). For an architectural
view of the solution, see the corresponding AWS Instance Scheduler documentation at
[Architecture overview.html](../../../solutions/latest/instance-scheduler-on-aws/architecture-overview.md "../../../solutions/latest/instance-scheduler-on-aws/architecture-overview.md").
