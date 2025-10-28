# Stop and start EC2 instances automatically

on a schedule using Quick Setup

With Quick Setup, a tool in AWS Systems Manager, you can configure Resource Scheduler to
automate the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) instances.

This Quick Setup configuration helps you reduce operational costs by starting and
stopping instances according to the schedule that you specify. This tool helps you
avoid incurring unnecessary costs for running instances when they’re not needed.

For example, you currently might leave your instances running constantly, even
though they’re only used 10 hours a day, 5 days a week. Instead, you can schedule
your instances to stop every day after business hours. As a result, there would be
70 percent savings for those instances because the running time is reduced from 168
hours to 50 hours. There is no cost to use Quick Setup. However, costs can be incurred
by the resources you set up and the usage limits with no fees for the services used
to set up your configuration.

Using Resource Scheduler, you can choose to automatically stop and start instances
across multiple AWS Regions and AWS accounts according to a schedule you define.
The Quick Setup configuration targets Amazon EC2 instances using the tag key and value that
you specify. Only the instances with a tag matching the value that you specify in
your configuration are stopped or started by Resource Scheduler. Note that if the
Amazon EBS volumes attached to the instance are encrypted, you must add the required
permissions for the AWS KMS key to the IAM role for Resource Scheduler to start the
instance.

###### Maximum instances per configuration

An individual configuration supports scheduling up to 5,000 instances per
Region. If your case requires more than 5,000 instances to be scheduled in a
given Region, you must create multiple configurations. Tag your instances
accordingly so each configuration is managing up to 5,000 instances. When
creating multiple Resource Scheduler Quick Setup configurations, you must specify
different tag key values. For example, one configuration can use the tag key
`Environment` with the value `Production`, while
another uses `Environment` and `Development`.

###### Scheduling behaviors

The following points describe certain behaviors of schedule
configurations:

- Resource Scheduler starts the tagged instances only if they are in the
  `Stopped` state. Similarly, instances are only stopped if
  they are in the `running` state. Resource Scheduler operates on
  an event driven model and only starts or stops instances at the times that
  you specify. For example, you create a schedule that starts instances at 9
  AM. Resource Scheduler starts all instances associated with the tag you
  specify that are in the `Stopped` state at 9 AM. If the instances
  are manually stopped at a later time, Resource Scheduler will not start them
  again to maintain the `Running` state. Similarly, if an instance
  is started manually after it was stopped according to your schedule,
  Resource Scheduler will not stop the instance again.
- If you create a schedule with a start time that is later in a 24-hour day
  than the stop time, Resource Scheduler assumes your instances are to run
  overnight. For example, you create a schedule that starts instances at 9 PM,
  and stops instances at 7 AM. Resource Scheduler starts all instances
  associated with the tag you specify that are in the `Stopped`
  state at 9 PM, and stops them at 7 AM the following day. For overnight
  schedules, the start time applies to the days you select for your schedule.
  However, the stop time applies to the following day in your schedule.
- When you create a schedule configuration, the current state of your
  instances might be changed to match the requirements of the schedule.

For example, say that today is a Wednesday, and you specify a schedule for
your managed instances to start at 9 AM and stop at 5 PM on Tuesdays and
Thursdays _only_. Because your current time
is outside of the prescribed hours for the instances to be running, they
will be stopped after the configuration is created. The instances won't run
again until the next prescribed hour, 9 AM on Thursday.

If your instances are currently in a `Stopped` state, and you
specify a schedule in which they would be running at the current time,
Resource Scheduler starts them after the configuration is created.
If you delete your configuration, instances are no longer stopped and started
according to the previously defined schedule. In rare cases, instances might not
successfully stop or start due to API operation failures.

To set up scheduling for Amazon EC2 instances, perform the following tasks in the
AWS Systems Manager Quick Setup console.

###### To set up instance scheduling with Quick Setup

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. On the **Resource Scheduler** card, choose
   **Create**.

###### Tip

If you already have one or more configurations in your account, first
choose the **Library** tab or the
**Create** button in the
**Configurations** section to view the
cards. 4. In the **Instance tag** section, specify the tag key and
value applied to the instances you want to associate with your
schedule. 5. In the **Schedule options** section, specify the time
zone, days, and times you want to start and stop your instances. 6. In the **Targets** section, choose whether to set
scheduling for a **Custom** group of organizational units
(OUs), or the **Current account** you're signed in
to:

    * **Custom** – In the **Target
     OUs** section, select the OUs where you want to set up
     scheduling. Next, in the **Target Regions**
     section, select the Regions where you want to set up
     scheduling.
    * **Current account** – Select
     **Current Region** or **Choose
     Regions**. If you selected **Choose
     Regions**, choose the **Target
     Regions** where you want to set up scheduling.

7. Verify the schedule information in the **Summary**
   section.
8. Choose **Create**.
