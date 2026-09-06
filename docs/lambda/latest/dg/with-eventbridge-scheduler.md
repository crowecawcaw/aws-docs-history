

# Invoke a Lambda function on a schedule
<a name="with-eventbridge-scheduler"></a>

[Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html) is a serverless scheduler that you can use to create, run, and manage tasks from one central, managed service. With EventBridge Scheduler, you can create schedules using cron and rate expressions for recurring patterns, or configure one-time invocations. You can set up flexible time windows for delivery, define retry limits, and set the maximum retention time for unprocessed events.

When you set up EventBridge Scheduler with Lambda, EventBridge Scheduler invokes your Lambda function asynchronously. You can create a schedule from the Lambda console (using the Add trigger flow), the EventBridge Scheduler console, the AWS CLI, or CloudFormation. This page explains how to use EventBridge Scheduler to invoke a Lambda function on a schedule.

## Set up the execution role
<a name="using-eventbridge-scheduler-execution-role"></a>

 When you create a new schedule, EventBridge Scheduler must have permission to invoke its target API operation on your behalf. You grant these permissions to EventBridge Scheduler using an *execution role*. The permission policy you attach to your schedule's execution role defines the required permissions. These permissions depend on the target API you want EventBridge Scheduler to invoke.

 When you create a schedule using the Lambda console or the EventBridge Scheduler console, EventBridge Scheduler automatically sets up an execution role based on your selected target. If you want to create a schedule using one of the EventBridge Scheduler SDKs, the AWS CLI, or CloudFormation, you must have an existing execution role that grants the permissions EventBridge Scheduler requires to invoke a target. For more information about manually setting up an execution role for your schedule, see [Setting up an execution role](https://docs.aws.amazon.com/scheduler/latest/UserGuide/setting-up.html#setting-up-execution-role) in the *EventBridge Scheduler User Guide*. 

## Create a schedule from the Lambda console
<a name="create-schedule-lambda-console"></a>

Use the **Add trigger** flow in the Lambda console to create an EventBridge Scheduler schedule without leaving the console.

**To create a Scheduler trigger using the Lambda console**

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.

1. Choose the function you want to schedule.

1. In the **Function overview** pane, choose **Add trigger**.

1. From the trigger source dropdown, choose **Scheduler**.

1. Configure the schedule settings:

   1. **Schedule name** – Enter a name for your schedule.

   1. **Schedule group** – Choose a schedule group or use `default`.

   1. **Schedule type** – Choose one of the following:
      + **One-time schedule** – Invokes the function once at the specified date and time.
      + **Recurring schedule** – Invokes the function repeatedly using a cron or rate expression.

   1. (Optional) Enter a JSON payload. If you don't enter a payload, EventBridge Scheduler uses an empty event to invoke the function.

   1. Configure the execution role. To have EventBridge Scheduler create a new execution role for you, choose **Create new role for this schedule**. Then, enter a name for **Role name**. If you choose this option, EventBridge Scheduler creates a policy with the required permissions and attaches it to the role.

1. Choose **Add**.

**Tip**  
You can also search for **schedule**, **cron**, **time**, or **recurring** to find this trigger in the Add trigger flow.

You can also use the [EventBridge Scheduler console](https://console.aws.amazon.com/scheduler/home) to create a schedule. With the EventBridge Scheduler console, you can configure additional options such as flexible time windows and dead-letter queues.

## Viewing EventBridge Scheduler triggers
<a name="viewing-scheduler-triggers"></a>

All EventBridge Scheduler schedules targeting your function appear in the **Triggers** section of the function configuration page under the **Scheduler** label. This includes schedules created from any of the following sources:
+ The Lambda console (Add trigger flow)
+ The EventBridge Scheduler console
+ The AWS CLI, SDK, CloudFormation, AWS SAM (using the `ScheduleV2` event type), or AWS CDK (using the `aws-scheduler` module)

**Note**  
If a schedule uses a customer managed key for encryption with a Universal Target Invocation (UTI) target, it might not appear in the triggers list. To view these schedules, use the [EventBridge Scheduler console](https://console.aws.amazon.com/scheduler/home).

To confirm that EventBridge Scheduler invoked the function, [check the function's Amazon CloudWatch logs](monitoring-cloudwatchlogs-view.md#monitoring-cloudwatchlogs-console).

## Related resources
<a name="using-eventbridge-scheduler-related-resources"></a>

 For more information about EventBridge Scheduler, see the following: 
+ [EventBridge Scheduler User Guide](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html)
+ [EventBridge Scheduler API Reference](https://docs.aws.amazon.com/scheduler/latest/APIReference/Welcome.html)
+ [EventBridge Scheduler Pricing](https://aws.amazon.com/eventbridge/pricing/#Scheduler)