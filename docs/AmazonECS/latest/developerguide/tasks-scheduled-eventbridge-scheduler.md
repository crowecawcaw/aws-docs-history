# Using Amazon EventBridge Scheduler to schedule Amazon ECS tasks

EventBridge Scheduler is a serverless scheduler that allows you to create, run, and manage tasks from one
central, managed service. It provides one-time and recurring scheduling functionality
independent of event buses and rules. EventBridge Scheduler is highly customizable, and offers improved
scalability over EventBridge scheduled rules, with a wider set of target API operations and AWS
services. EventBridge Scheduler provides the following schedules which you can configure for your tasks in
the EventBridge Scheduler console:

- Rate-based
- Cron-based

You can configure cron-based schedules in any time zone.

- One-time schedules

You can configure one-time schedules in any time zone.
You can schedule your Amazon ECS using Amazon EventBridge Scheduler.

Although you can create a scheduled task in the Amazon ECS console, currently the EventBridge Scheduler
console provides more functionality.

Complete the following steps before you schedule a task:

1. Use the VPC console to get the subnet IDs where the tasks run and the security
   group IDs for the subnets. For more information, see [Subnets for your VPC](../../../vpc/latest/userguide/configure-subnets.md "../../../vpc/latest/userguide/configure-subnets.md"), and [Control traffic to your AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md") in the _Amazon VPC User Guide_.
2. Configure the EventBridge Scheduler execution role. For more information, see [Set
   up the execution role](../../../scheduler/latest/UserGuide/setting-up.md#setting-up-execution-role "../../../scheduler/latest/UserGuide/setting-up.md#setting-up-execution-role") in the _Amazon EventBridge Scheduler User
   Guide_.
3. If you want to use a capacity provider strategy to run the task, you must have a
   capacity provider associated with the cluster.

###### To create a new schedule using the console

1. Open the Amazon EventBridge Scheduler console at [https://console.aws.amazon.com/scheduler/home](https://console.aws.amazon.com/scheduler/home/ "https://console.aws.amazon.com/scheduler/home/").
2. On the **Schedules** page, choose **Create schedule**.
3. On the **Specify schedule detail** page, in the **Schedule name and description** section, do the following:
   1. For **Schedule name**, enter a name for your
      schedule. For example, `MyTestSchedule`.
   2. (Optional) For **Description**, enter a
      description for your schedule. For example, `TestSchedule`.
   3. For **Schedule group**, choose a schedule group. If you don't have a group, choose
      **default**. To create a schedule group, choose
      **create your own schedule**.

   You use schedule groups to add tags to groups of schedules.

4. Choose your schedule options.

| Occurrence                                                                                                                                               | Do this...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **One-time schedule**<br>A one-time schedule invokes a target only once<br>at the date and time that you specify.                                        | For **Date and time**, do the<br>following:<br>• Enter a valid date in<br>`YYYY/MM/DD` format.<br>• Enter a timestamp in 24-hour<br>`hh:mm` format.<br>• For **Timezone**, choose<br>the timezone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Recurring schedule**<br>A recurring schedule invokes a target at a<br>rate that you specify using a<br>\*_cron_<br>• expression or rate<br>expression. | 1. For **Schedule type**, do<br>one of the following:<br>• To use a cron expression to define the<br>schedule, choose **Cron-based<br>schedule\*<br>• and enter the cron<br>expression.<br>• To use a rate expression to define the<br>schedule, choose **Rate-based<br>schedule*<br>• and enter the rate<br>expression.<br>For more information about cron and rate<br>expressions, see [Schedule types on EventBridge Scheduler](../../../scheduler/latest/UserGuide/schedule-types.md#cron-based "../../../scheduler/latest/UserGuide/schedule-types.md#cron-based") in the *Amazon EventBridge Scheduler User Guide*.<br>2. For **Flexible time<br>window**, choose **Off**<br>to turn off the option, or choose one of the<br>pre-defined time windows.<br>For example, if you choose \*\*15<br>minutes*<br>• and you set a recurring<br>schedule to invoke its target once every hour, the<br>schedule runs within 15 minutes after the start of<br>every hour. |

5.  (Optional) If you chose **Recurring schedule** in the previous step,
    in the **Timeframe** section, do the following:
    1. For **Timezone**,
       choose a timezone.
    2. For **Start date and time**, enter a valid date in
       `YYYY/MM/DD` format, and then specify a timestamp in
       24-hour `hh:mm` format.
    3. For **End date and time**, enter a valid date in
       `YYYY/MM/DD` format, and then specify a timestamp in
       24-hour `hh:mm` format.

6.  Choose **Next**.
7.  On the **Select target** page, do the following:
    1. Choose **All APIs**, and then in the search box
       enter **ECS**.
    2. Select **Amazon ECS**.
    3. In the search box, enter **RunTask**, and then
       choose **RunTask**.
    4. For **ECS cluster**, choose the cluster.
    5. For **ECS task**, choose the task definition to use for the task.
    6. Choose how your tasks are distributed across your cluster
       infrastructure. Expand **Compute options**, and then choose one of the following options

    | Compute option             | Steps                                                                                                                                                                                                                                                                                                                                                                         |
    | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Capacity provider strategy | 1. Choose<br>**Capacity provider<br>strategy**.<br>2. Choose a strategy:<br>• To use the default capacity<br>provider strategy, choose **Use cluster<br>default**.<br>• To use a custom<br>strategy, choose **Use custom**. Then, enter the **Base**, **Capacity<br>provider**, and<br>**Weight**.<br>For EC2, the Capacity<br>provider is the Amazon EC2 Auto Scaling group. |
    | Launch type                | 1. Choose **Launch<br>type**.<br>2. For **Launch type**, choose a<br>launch type.<br>3. When the Fargate is<br>specified, for **Platform<br>version**, specify the platform version to<br>use.                                                                                                                                                                                |
    7. For **Subnets**, enter the subnet IDs to run the task in.
    8. For **Security groups**, enter the security group IDs for the subnet.
    9. (Optional) To use a task placement strategy other than the
       default, expand **Placement constraint**, and then enter the constraints.

    For more information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md"). 10. (Optional) To help identify your tasks, under
    **Tags** configure your tags.

    To have Amazon ECS automatically tag all newly launched tasks with the task definition tags, select **Enable Amazon ECS managed
    tags**.

8.  Choose **Next**.
9.  On the **Settings** page, do the following:
    1.  To turn on the schedule, under **Schedule
        state**, toggle **Enable schedule**.
    2.  To configure a retry policy for your schedule, under
        **Retry policy and dead-letter queue (DLQ)**,
        do the following:

            * Toggle **Retry**.
            * For **Maximum retention time of event**,
             enter the maximum **hour(s)** and
             **min(s)** that EventBridge Scheduler must keep an
             unprocessed event.
            * The maximum time is 24 hours.
            * For **Maximum retries**, enter the
             maximum number of times EventBridge Scheduler retries the schedule if the
             target returns an error.


             The maximum value is 185 retries.

        With retry policies, if a schedule fails to invoke its target,
        EventBridge Scheduler re-runs the schedule. If configured, you must set the maximum
        retention time and retries for the schedule.

    3.  Choose where EventBridge Scheduler stores undelivered events.

    | **Dead-letter queue (DLQ)**<br>option                                                 | Do this...                                                                                                                                          |
    | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Don't store                                                                           | Choose **None**.                                                                                                                                    |
    | Store the event in the same AWS account where<br>you're creating the schedule         | 1. Choose **Select an Amazon SQS queue in<br>my AWS account as a DLQ**.<br>2. Choose the Amazon Resource Name (ARN) of<br>the Amazon SQS queue.     |
    | Store the event in a different AWS account from<br>where you're creating the schedule | 1. Choose **Specify an Amazon SQS queue in<br>other AWS accounts as a DLQ**.<br>2. Enter the Amazon Resource Name (ARN) of<br>the Amazon SQS queue. |
    4. To use a customer managed key to encrypt your target input, under
       **Encryption**, choose **Customize
       encryption settings (advanced)**.

    If you choose this option, enter an existing KMS key ARN or choose
    **Create an AWS KMS key** to navigate to the
    AWS KMS console. For more information about how EventBridge Scheduler encrypts your data
    at rest, see [Encryption at
    rest](../../../scheduler/latest/UserGuide/encryption-rest.md "../../../scheduler/latest/UserGuide/encryption-rest.md") in the _Amazon EventBridge Scheduler User
    Guide_. 5. For **Permissions**, choose **Use existing
    role**, then select the role.

    To have EventBridge Scheduler create a new execution role for you, choose
    **Create new role for this schedule**.
    Then, enter a name for **Role name**. If you choose
    this option, EventBridge Scheduler attaches the required permissions necessary for
    your templated target to the role.

10. Choose **Next**.
11. In the **Review and create schedule** page, review the
    details of your schedule. In each section, choose **Edit** to
    go back to that step and edit its details.
12. Choose **Create schedule**.

You can view a list of your new and existing schedules on the
**Schedules** page. Under the
**Status** column, verify that your new schedule is
**Enabled**.

## Next steps

You can use the EventBridge Scheduler console or the AWS CLI to manage the schedule. For more
information, see [Managing a schedule](../../../scheduler/latest/UserGuide/managing-schedule.md "../../../scheduler/latest/UserGuide/managing-schedule.md")
in the _Amazon EventBridge Scheduler User Guide_.
