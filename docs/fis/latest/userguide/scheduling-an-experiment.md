# Create an experiment schedule

Before you schedule an experiment, you need one or more [Experiment template components](experiment-templates.md "experiment-templates.md") for
your schedule to invoke. You can use an existing AWS resource, or create a new one.

Once experiment template is created, click on **Actions** and select **Schedule
experiment**. You will be redirected to schedule experiment page. The name of
the schedule will be filled in for you.

Follow to the schedule pattern section and choose either one-time schedule or recurring.
Fill in required input fields and navigate to permissions.

![Schedule pattern interface with options for one-time or recurring schedules and date/time settings](images/schedule-pattern.png)
Schedule state will be enabled by default. Note: if you disable **schedule
state**, the experiment will not be scheduled even if you create a schedule.

AWS FIS Experiment Scheduler is built on top of [EventBridge Scheduler](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md").
You can refer the documentation for the various [schedule
types
supported](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md").

## To update schedule using the console

1. Open the [AWS FIS console](https://console.aws.amazon.com/fis "https://console.aws.amazon.com/fis").
2. In the left navigation pane, choose **Experiment Templates**
   .
3. Choose **Experiment Template** for which you want to create
   the schedule.
4. Click **Actions**, and select **Schedule Experiment**
   from the dropdown.
   1. Under **Schedule name**, name is auto populated.
   2. Under **Schedule pattern**, select **Recurring
      schedule**.
   3. Under **Schedule type**, you can select a **Rate-based
      schedule**, see [schedule types](../../../scheduler/latest/UserGuide/schedule-types.md "../../../scheduler/latest/UserGuide/schedule-types.md")
      .
   4. Under **Rate expression**, choose a rate that is
      slower than the execution time of your experiment, e.g. **5
      minutes**.
   5. Under **Timeframe**, select your **Time Zone**
      .
   6. Under **Start Date and Time**, specify a start date
      and time.
   7. Under **End Date and Time**, specify an end date and
      time
   8. Under **Schedule State**, toggle the **Enable
      Schedule Option**.
   9. Under **Permissions**, select **Use
      existing role**, and then search for `FisSchedulerExecutionRole`.
   10. Choose **Next**.

5. Select **Review and create schedule**, review your scheduler
   details, and then choose **Create schedule**.
