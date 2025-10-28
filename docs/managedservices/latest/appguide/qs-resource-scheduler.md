# AMS Resource Scheduler quick start

Use this quick start guide to implement
[AMS Resource Scheduler](../userguide/resource-scheduler.md "../userguide/resource-scheduler.md"),
a tag-based instance scheduler to save cost in AMS Advanced.

The AMS Resource Scheduler is based on the
[AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/ "https://aws.amazon.com/solutions/implementations/instance-scheduler/").

## AMS Resource Scheduler terminology

Before you begin, it's good to be familiar with the AMS Resource Scheduler terminology:

- **period**: Each schedule must contain at least one period that defines
  the time(s) the instance should run. A schedule can contain more than one period. When more than one period is used in a
  schedule, the Resource Scheduler applies the appropriate start action when at least one of the period rules is
  true.
- **timezone**: For a list of acceptable time zone values to be used in the
  **DefaultTimezone** parameter referenced later, see the
  **TZ** column of the [List of TZ Database Time Zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones "https://en.wikipedia.org/wiki/List_of_tz_database_time_zones").
- **hibernate**: When set to **true** EC2 instances that are enabled for
  hibernation and meet hibernation requirements are hibernated (suspend-to-disk). Check the EC2 console to find out if your
  instances are enabled for hibernation. Use hibernation for stopped Amazon EC2 instances running Amazon Linux.
- **enforced**: When set to **true**, based on the schedule defined,
  the Resource Scheduler stops a running resource if it's manually started outside of the running period, and it
  starts a resource if it's stopped manually during the running period.
- **retain_running**: When set to **true**, prevents the Resource Scheduler from
  stopping an instance at the end of a running period if the instance was manually started before the beginning of the period.
  For example, if an instance with a configured **period** that runs from 9 am to 5 pm is manually started before
  9 am, the Resource Scheduler does not stop the instance at 5 pm.
- **ssm-maintenance-window**: Add an AWS Systems Manager maintenance window as a
  running period to a schedule. When you specify the name of a maintenance window that exists in the same account and AWS Region
  as your deployed stack to schedule your Amazon EC2 instances, the Resource Scheduler will start the instance before the
  start of the maintenance window and stop the instance at the end of the maintenance window, if no other running period
  specifies that the instance should run, and if the maintenance event is completed.

The Resource Scheduler uses the AWS Lambda frequency you specified during initial configuration to determine
how long before the maintenance window to start your instance. If you set the **Frequency**
AWS CloudFormation parameter to 10 minutes or less, the Resource Scheduler starts the instance 10 minutes before the maintenance
window. If you set the frequency to greater than 10 minutes, the Resource Scheduler starts the instance the same number of
minutes as the frequency you specified. For example, if you set the Systems Manager maintenance window frequency to 30 minutes, the
Resource Schedulers starts the instance 30 minutes before the maintenance window.

For more information, see
[AWS Systems Manager Maintenance Windows](../../../systems-manager/latest/userguide/systems-manager-maintenance.md "../../../systems-manager/latest/userguide/systems-manager-maintenance.md").

- **override-status**: Temporarily override the Resource Scheduler's configured
  **Schedule** start and stop actions. If you set the field to **running**, the
  Resource Scheduler starts, but not stops, the applicable instance. The instance runs until you stop it manually. If you set
  the **override-status** to **stopped**, the Resource Scheduler stops but not starts the
  applicable instance. The instance does not run until you manually start it.

## AMS Resource Scheduler implementation

To deploy an AMS Resource scheduler solution, follow these steps.

1. Submit a
   [Deployment | AMS Resource Scheduler | Solution | Deploy](../ctref/deployment-ams-solution-deploy.md "../ctref/deployment-ams-solution-deploy.md")
   ([ct-0ywnhc8e5k9z5](../ctref/schemas.md#ct-0ywnhc8e5k9z5-schema-section "../ctref/schemas.md#ct-0ywnhc8e5k9z5-schema-section"))
   RFC and provide the following parameters:
   - **SchedulingActive**: **Yes** to enable resource scheduling,
     **No** to disable. Default is **Yes**.
   - **ScheduledServices**: Enter a comma-separated list of services to schedule resources
     for. Valid values include a combination of **autoscaling**, **ec2**, and
     **rds**. Default is **autoscaling,ec2,rds**.
   - **TagName**: The name of the Tag Key that associates resource schedule
     schemas with service resources. Default is **Schedule**.

   ###### Note

   Your Resource Scheduler deployment will only operate on resources that have this tag.
   - **DefaultTimezone**: The name of the time zone, in the form US/Pacific, to be used as
     the default time zone. Default is **UTC**.

2. After you receive a confirmation that the RFC in step one executed successfully, you can
   submit the [Period | Add](../ctref/management-ams-period-add.md "../ctref/management-ams-period-add.md") change type.
3. Finally, submit an RFC to add a schedule to the period that was created in step two. Use the
   [Schedule
   | Add](../ctref/management-ams-schedule-add.md "../ctref/management-ams-schedule-add.md") change type. ### AMS Resource Scheduler implementation and usage FAQs Frequently asked questions about AMS Resource Scheduler. **Q**: What happens if I enable hibernation but the EC2 instance does not support it? **A**: Hibernation saves the contents from the instance memory (RAM) to your Amazon Elastic Block Store (Amazon EBS) root volume. If this field is set to **true**, instances are hibernated when Resource Scheduler stops them. If you set Resource Scheduler to use hibernation but your instances are not [enabled for hibernation](../../../AWSEC2/latest/UserGuide/Hibernate.md#enabling-hibernation "../../../AWSEC2/latest/UserGuide/Hibernate.md#enabling-hibernation") or they do not meet the [hibernation prerequisites](../../../AWSEC2/latest/UserGuide/Hibernate.md#hibernating-prerequisites "../../../AWSEC2/latest/UserGuide/Hibernate.md#hibernating-prerequisites"), Resource Scheduler logs a warning and the instances are stopped without hibernation. For more information, see [Hibernate Your Instance](../../../AWSEC2/latest/UserGuide/Hibernate.md "../../../AWSEC2/latest/UserGuide/Hibernate.md"). **Q**: What happens if I set both **override_status** and **enforced**? **A**: If you set **override_status** to **running**  and set **enforced** to **true** (prevents an instance from being manually started outside of a running period), Resource Scheduler stops the instance. If you set **override_status** to **stopped**, and set **enforced** to **true** (prevents an instance from being manually stopped during a running period), the Resource Scheduler restarts the instance. ###### Note If **enforced** is **false**, the configured **override** behavior is applied. **Q**: After the AMS Resource Scheduler is deployed, how do I disable or enable the resource scheduler in my account? **A**: To disable or enable AMS Resource Scheduler: <br>• To **disable**: Create an RFC using [State | Disable](../ctref/management-ams-state-disable.md "../ctref/management-ams-state-disable.md"). Be sure to set the **SchedulerState** to **DISABLE** <br>• To **enable**: Create an RFC using [State | Enable](../ctref/management-ams-state-enable.md "../ctref/management-ams-state-enable.md"). Be sure to set the **SchedulerState** to **ENABLE** **Q**What happens if the AMS Resource Scheduler period falls within my patching maintenance window? **A**: Resource Scheduler works based on its configured schedules. If it is configured to stop an instance while patching is in flight, then it stops the instance unless the patching window is added as a period to the schedule before patching begins. In other words, Resource Scheduler does not auto-start any stopped instances for patching unless a designated period is configured. To avoid conflicts with your patching maintenance window, add the time window allocated for patching to the Resource Scheduler schedule as a period. To add a period to existing schedule, create an RFC using [Period | Add](../ctref/management-ams-period-add.md "../ctref/management-ams-period-add.md"). **Q** If I need to have a different schedule for different EC2 instances, can I have more than one schedule setup inside of my account? **A**: Yes, you can create multiple schedules. Each schedule can have multiple periods based on the requirement. When AMS Resource Scheduler is enabled in the account, a **Tag Key** is configured. As an example, if the Tag Key is "Schedule", the Tag Value can differ based on different schedules which corresponds to AMS Resource Scheduler’s schedule name. To add a new schedule, you can create an RFC using the Management | AMS Resource Scheduler | Schedule | Add (ct-2bxelbn765ive) change type, see [Schedule | Add](../ctref/management-ams-schedule-add.md "../ctref/management-ams-schedule-add.md"). **Q**: Where can I find all the different change types that are supported for AMS Resource Scheduler? **A**: AMS has Resource Scheduler change types to deploy the AMS Resource Scheduler to your account; enable or disable it; define, add, update, and delete schedules and periods to use with it; and describe (get a detailed description of) the schedules and periods.
