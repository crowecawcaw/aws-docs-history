

# Scheduling your Amazon Quick Flows
<a name="schedules-in-quick-flows"></a>

Schedules let you automate recurring flow runs without manual intervention. You can schedule flows you have created or flows that have been shared with you. All schedules are private to you and cannot be shared with other users.

Common uses include generating recurring reports, summarizing open items from external services, or preparing daily meeting briefings.

## Creating a schedule
<a name="creating-schedules"></a>

1. Open your flow in Run mode.

1. Choose the scheduling icon.

1. Choose **Create schedule**.

1. Configure your schedule:
   + **Schedule name** — A unique name for the schedule.
   + **Description** — Optional. Details about the schedule's purpose.
   + **Repeat configuration** — Choose from suggestions or configure custom recurrence (daily, weekly, or monthly) with start date, optional end date, and time zone.

1. Choose **Next**.

1. Provide default inputs for each scheduled run.

1. Choose **Next**.

1. Configure action permissions:
   + Turn on **Run with no confirmation** to automatically submit action forms during scheduled runs.
   + Turn off to review and confirm each action manually.

1. Choose **Save**.

**Note**  
Action permissions only appear if the flow contains action steps. Automatic form submission is enabled by default for write actions. User confirmation is recommended to help avoid AI prediction errors.

## Managing schedules
<a name="managing-schedules"></a>

You can manage schedules from two places:
+ **From the flow** — Open the flow, choose the scheduling icon, and edit, pause, duplicate, view runs, or delete a schedule.
+ **From the Flows library** — Choose the **My schedules** tab to see all your schedules across all flows with their status, frequency, last run, and associated flow name.

## Schedule history
<a name="schedule-history-and-auditing"></a>

All manual and scheduled runs appear in the flow run history. You can filter by all runs, scheduled runs, or failed runs. History is retained for 30 days.

Visual indicators help distinguish run types:
+ Schedule run tag for scheduled runs
+ Orange dot for un-viewed completed runs
+ Running tag for in-progress runs
+ Failed tag for failed runs

**Note**  
You cannot view an ongoing scheduled run until it completes.

## Notifications
<a name="notifications-for-schedule-runs"></a>

You receive email notifications when:
+ A scheduled run completes successfully (with a link to the results)
+ A run requires your input to continue
+ A run requires authentication for a third-party application
+ A flow with your schedules is unshared from you (schedules are archived)
+ A flow with your schedules is deleted
+ A flow with your schedules is updated with a new version (schedules continue with the updated version)

## Authentication for connectors
<a name="authentication-for-action-connectors"></a>

Ensure your authentication for connectors is current before scheduling. If authentication expires before a scheduled run, you receive an email notification. To verify, run the flow manually or visit the connector page in Quick to sign in.