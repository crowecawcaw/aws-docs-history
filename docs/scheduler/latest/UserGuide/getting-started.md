# Getting started with EventBridge Scheduler

This topic describes creating a new EventBridge Scheduler schedule. You use the EventBridge Scheduler console, AWS Command Line Interface
(AWS CLI), or AWS SDKs to create a schedule with a templated Amazon SQS target. Then, you'll set
up logging, configure retries, and set a maximum retention time for failed tasks. After you
create the schedule, you'll verify that your schedule successfully invokes the target
and sends a message to the target queue.

###### Note

To follow this guide, we recommend that you set up IAM users with the minimum
required permissions described in [Using identity-based policies in EventBridge Scheduler](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). After you create and configure a user, run the following command to set your access
credentials. You'll need your access key ID and secret access key to configure the
AWS CLI.

```
`$` `aws configure`
AWS Access Key ID [None]: `AKIAIOSFODNN7EXAMPLE`
AWS Secret Access Key [None]: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
Default region name [None]: `us-west-2`
Default output format [None]: `json`
```

For more information about different ways you can set your credentials, see
[Configuration settings and precedence](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-precedence "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-precedence") in the
_AWS Command Line Interface User Guide for Version 2_.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Create a schedule using the EventBridge Scheduler console](#getting-started-console "#getting-started-console")
- [Create a schedule using the AWS CLI](#getting-started-cli "#getting-started-cli")
- [Create a schedule using the EventBridge Scheduler SDKs](#getting-started-sdk "#getting-started-sdk")
- [What's next?](#working-with-cli-sdk-whats-next "#working-with-cli-sdk-whats-next")

## Prerequisites

Before attempting the steps in this section, you must do the following:

- Complete the tasks described in [Setting up Amazon EventBridge Scheduler](setting-up.md "setting-up.md")

## Create a schedule using the EventBridge Scheduler console

###### To create a new schedule using the console

1. Sign in to the AWS Management Console, then choose the following link to open the EventBridge Scheduler
   section of the EventBridge console: [https://us-west-2.console.aws.amazon.com/scheduler/home?region=us-west-2#home](https://us-west-2.console.aws.amazon.com/scheduler/home?region=us-west-2#home "https://us-west-2.console.aws.amazon.com/scheduler/home?region=us-west-2#home")

###### Note

You can switch your AWS Region by using the AWS Management Console's Region
selector. 2. On the **Schedules** page, choose **Create schedule**. 3. On the **Specify schedule detail** page, in the **Schedule name and description** section, do the following:

    1. For **Schedule name**, enter a name for your
     schedule. For example, `MyTestSchedule`
    2. For **Description - *optional***,
     enter a description for your schedule. For example, `My first
     schedule`.
    3. For **Schedule group**, choose a schedule group from
     the drop down options. If you haven't previously made any schedule
     groups, you can choose the `default` group for your schedule.
     To create a new schedule group, choose the **create your own
     schedule** link in the console description. You use
     schedule groups to add tags to groups of schedules.

4.  In the **Schedule pattern** section, do the following:
    1.  For **Occurrence**, choose one of the following
        pattern options. The configuration options change depending on which
        pattern that you select.

            * One-time schedule – A
             one-time schedule invokes a target only once at the date and
             time that you specify.


            For **Date and time**, enter a valid date in
             `YYYY/MM/DD` format. Then, specify a timestamp in
             24-hour `hh:mm` format. Finally, choose a timezone
             from the drop down options.
            * Recurring schedule – A
             recurring schedule invokes a target at a rate that you specify
             using a **cron** expression or rate expression.


            Choose **Cron-based schedule** to configure a
             schedule by using a **cron** expression. To use a
             rate expression, choose **Rate-based schedule**
             and enter a positive number for **Value**, then
             choose a **Unit** from the drop down options.

        For more information on using cron and rate expressions, see [Schedule types in EventBridge Scheduler](schedule-types.md "schedule-types.md").

    2.  For **Flexible time window**, choose
        **Off** to turn off the option, or choose one of
        the pre-defined time windows from the drop down list. For example, if
        you choose **15 minutes** and you set a recurring
        schedule to invoke its target once every hour, the schedule runs within
        15 minutes after the start of every hour.

5.  If you chose **Recurring schedule** in the previous step, in
    the **Timeframe** section, specify a timezone, and optionally set a start date and time, and an end date and time for the schedule.
    A recurring schedule without a start date will begin as soon as it is created and available. A recurring schedules without an end date will
    continue to invoke it's target indefinitely.
6.  Choose **Next**.
7.  On the **Select target** page, do the following:
    1. Select **Templated targets** and choose a target API. For this
       example, we'll choose the **Amazon SQS
       `SendMessage`** templated target.
    2. On the **SendMessage** section, for **SQS
       queue**, choose an existing Amazon SQS queue ARN such as
       `arn:aws:sqs:`us-west-2`:`123456789012`:`TestQueue``
       from the drop down list. To create a new queue, choose **Create
       new SQS queue** to navigate to the Amazon SQS console. After
       finish creating a queue, return to the EventBridge Scheduler console and refresh the
       drop down. Your new queue ARN appears and can be selected.
    3. For **Target**, enter the payload you want EventBridge Scheduler to
       deliver to the target. For this example, we'll send the following
       message to the target queue: `Hello, it's
EventBridge Scheduler.`

8.  Choose **Next**, then on the **Settings - _optional_** page, do the following:
9.  1. In the **Schedule state** section, for
       **Enable schedule**, toggle feature on or off
       using the switch. By default, the EventBridge Scheduler enables your schedule.
    2. In the **Action after schedule completion** section, configure the action EventBridge Scheduler takes after the schedule completes:
       - Choose **DELETE** if you want the schedule to be automatically deleted. For one-time schedules, this occurs after the schedule invokes the target once.
         For recurring schedules, this occurs after the schedule's last planned invocation. For more information about automatic deletion, see [Deletion after schedule completion](managing-schedule-delete.md#managing-schedule-automatic-deletion "managing-schedule-delete.md#managing-schedule-automatic-deletion").
       - Choose **NONE**, or do not choose a value, if you do not want EventBridge Scheduler to take any action after the schedule completes.

    3. In the **Retry policy and dead-letter queue (DLQ)**
       section, for **Retry policy**, turn
       **Retry** on to configure a retry policy for your
       schedule. With retry policies, if a schedule fails to invoke its target,
       EventBridge Scheduler re-runs the schedule. If configured, you must set the maximum
       retention time and retries for the schedule.
    4. For **Maximum age of event - _optional_**, enter the maximum **hour(s)** and **min(s)** that EventBridge Scheduler must keep an unprocessed event.

    ###### Note

    The maximum value is 24 hours. 5. For **Maximum retries**, enter the maximum number of
    times EventBridge Scheduler retries the schedule if the target returns an error.

    ###### Note

    The maximum value is 185 retries. 6. For **Dead-letter queue (DLQ)**, choose from the
    following options:

        * **None** – Choose this
         option if you do not want to configure a DLQ.
        * **Select an Amazon SQS queue in my AWS
         account as DLQ** – Choose this option, then
         select a queue ARN from the drop down list, configure a DLQ
         the same AWS account as the one where you're creating the
         schedule.
        * **Specify an Amazon SQS queue in other AWS
         account as DLQ** – Choose this option, then
         enter the ARN of the queue configure as the DLQ, if the queue
         is in another AWS account. You must enter the exact ARN for the
         queue in order to use this option.

    7. In the **Encryption** section, choose
       **Customize encryption settings (advanced)** to use
       a customer managed KMS key to encrypt your target input. If you choose
       this option, enter an existing KMS key ARN or choose **Create
       an AWS KMS key** to navigate to the AWS KMS console. For
       more information on how EventBridge Scheduler encrypts your data at rest, see [Encryption at rest in EventBridge Scheduler](encryption-rest.md "encryption-rest.md").
    8. For **Permissions**, choose **Use existing
       role**, then select the role you created during the [setup](setting-up.md#setting-up-execution-role "setting-up.md#setting-up-execution-role") procedure from the
       drop down list. You can also choose **Go to IAM
       console** to create a new role.

    If you would like EventBridge Scheduler to create a new execution role for you, choose
    **Create new role for this schedule** instead.
    Then, enter a name for **Role name**. If you choose
    this option, EventBridge Scheduler adds the required permissions necessary for your
    templated target to the role.

10. Choose **Next**.
11. In the **Review and create schedule** page, review the
    details of your schedule. In each section, choose **Edit** to
    go back to that step and edit its details.
12. Choose **Create schedule** to finish creating your new
    schedule. You can view a list of your new and existing schedules on the
    **Schedules** page. Under the **Status**
    column, verify that your new schedule is **Enabled**.
13. To verify that your schedule invokes the Amazon SQS target, open the Amazon SQS console
    and do the following:
    1. Choose the target queue from the **Queues** list.
    2. Choose **Send and receive messages**.
    3. On the **Send and receive messages** page, under
       **Receive messages**, choose **Poll for
       messages** to retrieve the test messages your schedule sent
       to the target queue.

## Create a schedule using the AWS CLI

The following example shows how to use the AWS CLI command
[`create-schedule`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html")
to create a EventBridge Scheduler schedule with a templated Amazon SQS target. Replace the placeholder values for the following parameters with your information:

- **--name** – Enter a name for the schedule.
- **RoleArn** – Enter the ARN for the execution role you want to associate with the schedule.
- **Arn** – Enter the ARN for the target. In this case, the target is an Amazon SQS queue.
- **Input** – Enter a message that EventBridge Scheduler delivers to the target queue.

```
`$` `aws scheduler create-schedule --name `sqs-templated-schedule` --schedule-expression 'rate(5 minutes)' \
--target '{"RoleArn": "`ROLE_ARN`", "Arn": "`QUEUE_ARN`", "Input": "`TEST_PAYLOAD`" }' \
--flexible-time-window '{ "Mode": "OFF"}'`
```

## Create a schedule using the EventBridge Scheduler SDKs

In the following example, you use the EventBridge Scheduler SDKs to create a EventBridge Scheduler schedule with a
templated Amazon SQS target.

###### Example Python SDK

```
import boto3
scheduler = boto3.client('scheduler')

flex_window = { "Mode": "OFF" }

sqs_templated = {
    "RoleArn": "<ROLE_ARN>",
    "Arn": "<QUEUE_ARN>",
    "Input": "Message for scheduleArn: '<aws.scheduler.schedule-arn>', scheduledTime: '<aws.scheduler.scheduled-time>'"
}

scheduler.create_schedule(
    Name="sqs-python-templated",
    ScheduleExpression="rate(5 minutes)",
    Target=sqs_templated,
    FlexibleTimeWindow=flex_window)
```

###### Example Java SDK

```
package com.example;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.scheduler.SchedulerClient;
import software.amazon.awssdk.services.scheduler.model.*;


public class MySchedulerApp {

    public static void main(String[] args) {

        final SchedulerClient client = SchedulerClient.builder()
                .region(Region.US_WEST_2)
                .build();

        Target sqsTarget = Target.builder()
                .roleArn("<ROLE_ARN>")
                .arn("<QUEUE_ARN>")
                .input("Message for scheduleArn: '<aws.scheduler.schedule-arn>', scheduledTime: '<aws.scheduler.scheduled-time>'")
                .build();

        CreateScheduleRequest createScheduleRequest = CreateScheduleRequest.builder()
                .name("<SCHEDULE NAME>")
                .scheduleExpression("rate(10 minutes)")
                .target(sqsTarget)
                .flexibleTimeWindow(FlexibleTimeWindow.builder()
                        .mode(FlexibleTimeWindowMode.OFF)
                        .build())
                .build();

        client.createSchedule(createScheduleRequest);
        System.out.println("Created schedule with rate expression and an Amazon SQS templated target");
    }
}
```

## What's next?

- For more information about managing your schedule using the console, AWS CLI,
  or the EventBridge Scheduler SDK, see [Managing a schedule in EventBridge Scheduler](managing-schedule.md "managing-schedule.md").
- For more information about how to configure templated targets and learn about
  using the universal target parameter, see [Managing targets in EventBridge Scheduler](managing-targets.md "managing-targets.md").
- For more information about the EventBridge Scheduler data types and API operations, see the [EventBridge Scheduler API Reference](../APIReference.md "../APIReference.md").
