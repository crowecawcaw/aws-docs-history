# Cost optimization with AMS Resource Scheduler

The AMS Resource Scheduler on AWS solution helps you reduce your AWS and AMS costs by stopping resources that are not in use and starting
resources when capacity is needed. For example, you can use AMS Resource Scheduler on AWS in a development environment to automatically
stop instances outside of business hours every day. If you leave all of your instances running at full utilization, this solution can result in
reducing the instance utilization, which reduces overall cost based on the schedules you configure.

Use AWS Managed Services (AMS) Resource Scheduler to schedule the automatic start and stop of Amazon EC2 Auto Scaling groups, Amazon EC2 instances, and Amazon RDS instances in your account.
This helps reduce infrastructure costs where the resources are not meant to be running 24/7. The solution is
built on top of [AWS Instance Scheduler](https://aws.amazon.com/solutions/instance-scheduler/ "https://aws.amazon.com/solutions/instance-scheduler/") but contains additional
features and customizations specific to AMS customer needs.
The customization includes support for scheduling Amazon EC2 Auto Scaling groups, CloudWatch alarm suppressor for ELB alarms,
support for multiple AWS Systems Manager maintenance windows for Amazon EC2, a cost savings estimator, and operational support from AMS.

AMS Resource Scheduler uses periods and schedules. Periods define the times the
resource should run, such as start time, end time, and days of the month. Schedules contain
your defined periods, along with additional configurations—SSM maintenance window,
timezone, hibernate, etc—and specify when resources should run. You can configure
these periods and schedules using AMS-provided AWS Systems Manager automation runbooks. Each schedule must contain at least one period that
defines the time(s) the instance should run. A schedule can contain more than one period. When more than one period is used in a
schedule, the Instance Scheduler applies the appropriate start action when at least one of the period rules is true.
For more details on schedule and periods, see
[Solutions Components of AWS Instance Scheduler](../../../solutions/latest/instance-scheduler-on-aws/components.md "../../../solutions/latest/instance-scheduler-on-aws/components.md").

AMS Resource Scheduler uses AWS resource tags to associate a schedule to one or more resources in order to target them for
scheduled start and stop actions. You tag your resources with the tag key (default is `Schedule`) configured in the Scheduler
with the schedule name as the value. You configure the same tag key as the cost allocation tag in AWS Cost Explorer for the cost estimator feature of
Scheduler to track and report on cost savings.

AMS Resource Scheduler is an opt in feature that you can enable per account.
