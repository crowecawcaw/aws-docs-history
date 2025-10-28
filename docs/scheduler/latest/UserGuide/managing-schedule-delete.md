# Deleting a schedule in EventBridge Scheduler

You can delete a schedule by either configuring automatic deletion, or by manually deleting an individual schedule. Use following topics
to learn how you to delete a schedule using both methods, and why you might choose one method over the other.

###### Topics

- [Deletion after schedule completion](#managing-schedule-automatic-deletion "#managing-schedule-automatic-deletion")
- [Manual deletion](#managing-schedule-manual-deletion "#managing-schedule-manual-deletion")

## Deletion after schedule completion

Configure automatic deletion after schedule completion if you want to avoid having to individually manage your schedule resources on EventBridge Scheduler. In applications where you create thousands of schedules at a time and need flexibility to scale up the number of your schedules on demand,
automatic deletion can ensure that you do not reach your account quota for the [number of schedules](scheduler-quotas.md "scheduler-quotas.md") in a specified Region.

When you configure automatic deletion for a schedule, EventBridge Scheduler deletes the schedule after its last target invocation. For one-time schedules, this occurs after the schedule has invoked its target once. For recurring schedules you set up with rate, or cron, expressions, your schedule is
deleted after its last invocation. A recurring schedule's last invocation is the invocation that occurs closest to the [`EndDate`](../APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-EndDate "../APIReference/API_CreateSchedule.md#scheduler-CreateSchedule-request-EndDate") you specify. If you configure a schedule with
automatic deletion but do not specify a value for `EndDate`, EventBridge Scheduler does not automatically delete the schedule.

You can set up automatic deletion when you first create a schedule, or update preferences for an existing schedule. The following steps describe how to configure automatic deletion for an existing schedule.

AWS Management Console

1. Open the EventBridge Scheduler console at [https://console.aws.amazon.com/scheduler/](https://console.aws.amazon.com/scheduler/ "https://console.aws.amazon.com/scheduler/").
2. From the list of schedules, select the schedule you want to edit, then choose **Edit**.
3. From the navigation list on the left, choose **Settings**.
4. In the **Action after schedule completion** section, select **DELETE** from the drop down list,
   then save your changes.

AWS CLI

1. Open a new prompt window.
2. Use the update-schedule AWS CLI command to update an existing schedule a shown in the following.
   The command sets the `--action-after-completion` to `DELETE`. This example assumes that you have
   defined your target configuration locally in a JSON file. To update a schedule, you must provide the target, as well
   as any other schedule parameters you want to configure for your existing schedule.

This is a recurring schedule with a rate of one invocation per hour. Therefore, you specify an end date when setting the `--action-after-completion` parameter.

```
`$` ``aws scheduler update-schedule --name `schedule-name` \
**--action-after-completion 'DELETE' \**
--schedule-expression '`rate(1 hour)`' \
--end-date '`2024-01-01T00:00:00`'
--target `file://target-configuration.json` \
--flexible-time-window '{ "Mode": "OFF"}' \``
```

## Manual deletion

When you no longer need a schedule, you can delete it using the [`DeleteSchedule`](../APIReference/API_DeleteSchedule.md "../APIReference/API_DeleteSchedule.md")
operation.

###### Example AWS CLI

```
`$` `aws scheduler delete-schedule --name `your-schedule``
```

###### Example Python SDK

```
import boto3
scheduler = boto3.client('scheduler')

scheduler.delete_schedule(Name="your-schedule")
```
