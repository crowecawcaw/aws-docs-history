

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# AWS Managed Services Resource Scheduler
<a name="ams-resource-scheduler"></a>

Use AWS Managed Services (AMS) Resource Scheduler to schedule the automatic start and stop of AutoScaling groups, Amazon EC2 instances, and RDS instances in your account. This helps reduce infrastructure costs where the resources are not meant to be running 24/7. The solution is built on top of [Instance Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/), but contains additional features and customizations specific to AMS needs.

**Note**  
By default, AMS Resource Scheduler doesn't interact with resources that aren't part of an AWS CloudFormation stack. The resource must be part of a stack that starts with "stack-" , "sc-" or "SC-". To schedule the resources that are not part of a CloudFormation stack, you can update the Resource Scheduler stack parameter `ScheduleNonStackResources` to `Yes`.

AMS Resource Scheduler uses periods and schedules:
+ *Periods* define the times when Resource Scheduler runs, such as start time, end time, and days of the month.
+ *Schedules* contain your defined periods, along with additional configurations, such as SSM maintenance window, timezone, hibernate setting, and so forth; and specify when resources should run, given the configured period rules. 

You can configure these periods and schedules using AMS Resource Scheduler's automated change types (CTs).

For full details on the settings available for AMS Resource Scheduler, see the corresponding AWS Instance Scheduler documentation at [Solution components](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/components.html). For an architectural view of the solution, see the corresponding AWS Instance Scheduler documentation at [Architecture overview.html](https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/architecture-overview.html).