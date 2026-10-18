

# Schedule a penetration test
<a name="schedule-penetration-test"></a>

In AWS Security Agent, you can schedule a penetration test to run automatically, either once at a date and time that you choose or on a repeating schedule. For example, you can run a penetration test every Monday at 09:00 to retest an application after each weekly release. AWS Security Agent uses [Amazon EventBridge Scheduler](https://docs.aws.amazon.com/scheduler/latest/UserGuide/what-is-scheduler.html) to start each run.

Before you can schedule a penetration test, an administrator must enable scheduling for the Agent Space in the AWS Management Console. For information about how to enable it, see [(Optional) Enable penetration test scheduling](enable-penetration-test.md#enable-penetration-test-scheduling).

A scheduled run uses the configuration that the penetration test has when the run starts. For more information, see [Create a penetration test](perform-penetration-test.md).

## Prerequisites
<a name="_prerequisites"></a>

Before you begin, make sure that you have the following:
+ Access to the AWS Security Agent web application
+ A penetration test that you have created. You can’t schedule a draft penetration test.
+ Scheduling enabled for the Agent Space. If it isn’t, the schedule page shows the message **Scheduling isn’t enabled for this agent space**.

## Create a schedule
<a name="schedule-penetration-test-create"></a>

Each penetration test can have one schedule, either a one-time schedule or a repeating schedule. The time zone defaults to the time zone of your browser.

1. Sign in to the AWS Security Agent web application.

1. Choose **Penetration tests**.

1. Choose the penetration test that you want to schedule.

1. On the penetration test details page, choose **Schedule**, next to **Start run**.

1. On the **Schedule pentest** page, in the **Occurrence** section, choose **Repeating schedule** or **One-time schedule**, and then enter the settings. For descriptions of the settings, see [Schedule settings](#schedule-penetration-test-settings).

1. In the **Next runs** section, review when the penetration test runs next.

1. Choose **Save**.

The penetration test details page opens, and the **Scheduled runs** table lists the upcoming runs.

### Schedule settings
<a name="schedule-penetration-test-settings"></a>

For a repeating schedule, the penetration test runs repeatedly until you remove the schedule. Enter the following settings:
+  **Frequency** – Choose **Daily**, **Weekly**, or **Monthly**.
+  **Days of the week** – For a weekly schedule, select one or more days.
+  **Days of the month** – For a monthly schedule, select one or more days.
+  **Time** – Enter the start time in 24-hour `hh:mm` format, and select the time zone.
+  **Advanced** – (Optional) To run the schedule only in certain months, expand this section and select the months.

For a one-time schedule, the penetration test runs once, and AWS Security Agent removes the schedule after the run starts. Enter the **Date and time** for the run, and select the time zone. The date and time must be in the future.

## View scheduled runs
<a name="schedule-penetration-test-view"></a>

After you save a schedule, the **Scheduled runs** table appears on the penetration test details page. The table lists each upcoming run with its scheduled start time, the time remaining until it starts, and whether it comes from a one-time or a repeating schedule.

A run appears in the **Penetration test runs** list only after it starts. You can review its progress and findings in the same way as a run that you start yourself. For more information, see [Review findings from a penetration test](review-penetration-findings.md).

## Edit or remove a schedule
<a name="schedule-penetration-test-edit"></a>

1. Sign in to the AWS Security Agent web application.

1. Choose **Penetration tests**.

1. Choose the penetration test.

1. On the penetration test details page, choose **Edit schedule**.

1. In the **Occurrence** section, do one of the following:
   + To change the schedule, update the settings. To switch between a one-time schedule and a repeating schedule, choose the other option.
   + To remove the schedule, choose **No schedule**.

1. Choose **Save**.

Removing a schedule doesn’t stop a run that has already started.