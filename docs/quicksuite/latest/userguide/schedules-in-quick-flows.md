# Scheduling your Amazon Quick Flows

Schedules in Amazon Quick Flows enables users to automate recurring, unattended flow executions. This feature allows business users to set up workflows that run automatically at specified times without manual intervention. This capability is great for automating routine and administrative tasks such as generating recurring reports from dashboards, summarizing open items assigned to you in external services, or generating daily meeting briefings before you head out to work. Users can configure schedules to flow that are created by them or to flows that are shared with them.

To create a schedule, open your flow and choose the scheduling icon. You configure the schedule by providing a name and description, defining the frequency, adding default inputs for the schedule run, and setting action permissions for any action steps. After you create a schedule, you can edit, pause, duplicate, or view runs directly from the schedule interface. All schedules you configure are private to you and cannot be shared with other users.

You can view schedules for a specific flow from the flow run page, or view all your schedules across all flows from the My schedules tab in the flows library. When a scheduled flow completes successfully, you receive an email notification with a link to the completed run. You also receive notifications when a schedule run requires your input to continue, when a run fails, or when a flow with your schedules is unshared from you. The flow run history displays all runs—both scheduled and manual—for your review.

## Creating schedules

Users can create schedules directly in the flows runtime.

###### To create a schedule

1. Sign in to the Amazon Quick Suite console.
2. In the navigation pane, choose **Flows**.
3. Choose the flow name to open it in runtime mode.
4. Choose the scheduling icon.
5. Choose **Create schedule**.
6. Configure your schedule settings:
   - **Schedule name** - Enter a unique name for your schedule.
   - **Description** - (Optional) Provide details about the schedule's purpose.
   - **Repeat configuration** - Choose from system-generated suggestions or configure custom recurrence.

7. For custom recurrence, specify the following:
   - **Frequency** - Choose **Daily**, **Weekly**, or **Monthly**.
   - **Start date** - Select when the schedule begins.
   - **End date** - (Optional) Select when the schedule ends.
   - **Time zone** - Choose the time zone for schedule execution.

8. Choose **Next**.
9. Provide default inputs that the schedule uses during each run.

###### Note

Depending on the flow, you will be required to add multiple files or provide multiple text inputs. 10. Choose **Next**. 11. Configure action permissions:

    * Turn on **Run with no confirmation** to automatically submit action forms during scheduled runs.
    * Turn off this option if you want to review and confirm each action manually.

###### Note

Action permissions only appear if there are read action steps set up in the flow. 12. Choose **Save**.

### Schedule frequency options

- **Daily**: Run every X day(s) with start date, end date and time zone configurable.
- **Weekly**: Run every week on selected day(s) of the week with start date, end date and time zone configurable.
- **Monthly**: Run on a specific day of the month with start date, end date and time zone configurable.

## Managing schedules

### Managing schedules from the flow runtime page

From the flow runtime page, you can access schedules associated with that specific flow.

###### To manage schedules for a flow

1. Open your flow in runtime mode.
2. Choose the scheduling icon.
3. Choose one of the following actions:
   - **Create schedule** - Create a new schedule for the flow.
   - **Edit** - Modify an existing schedule's configuration.
   - **Pause** - Temporarily stop a schedule from running.
   - **Duplicate** - Create a copy of an existing schedule.
   - **View runs** - Opens the run history for the schedule.
   - **Delete** - Permanently remove the schedule.

### Managing schedules from the flows library

The **Schedules** tab in the flows library provides a centralized view of all your schedules across all flows.

###### To access all your schedules

1. In the navigation pane, choose **Flows**.
2. Choose the **Schedules** tab.

The Schedules tab displays the following information:

- **Status** - Whether the schedule is active or paused.
- **Schedule name** - The name you assigned to the schedule.
- **Repeat configuration** - The frequency and timing settings.
- **Last run status** - The time of the most recent execution.
- **Flow name** - The flow associated with the schedule.

From this view, you can edit, pause, duplicate, view run history, or delete any schedule.

### Schedule history and auditing

All manual and scheduled runs are available for users in the flow run history. For completed scheduled run, the history highlights the name of the schedule, status of the schedule (completed, running, unread) and schedule run time. Users get filters to view all runs, scheduled runs, and failed runs. Users can open any completed run through history and follow up.

**Visual indicators:**

- Schedule run tag differentiates scheduled runs from manual runs.
- Orange dot indicator for un-viewed completed scheduled runs.
- Running tag for schedules that are currently running.
- Failed tag for scheduled runs that failed.

###### Note

Users cannot view ongoing scheduled runs till the run is complete.

**Filtering and search:**

- Filter by completed scheduled runs, all runs, failed runs.
- Search through your history. History persists for 30 days.

## Notifications for schedule runs

Users receive email notifications for:

1. **Successful completion:** On successful schedule run complete, users get an email notification. The email notification contains a link that takes users view the completed flow run.
2. **Schedule run requires human input:** If the flow run requires human input to continue, users receive an email notification asking for input. The email notification contains flow link that takes user to the paused flow run where they can enter their inputs.
3. **Schedule run requires authentication for third-party applications:** When a schedule flow run requires user to authorize their third-party apps, users receive an email notification asking for authentication to complete. The email notification contains flow link that takes user to the paused flow run where they can enter their inputs.
4. **Flow unshared:** When a flow that has schedules configured by the user is unshared from them, the user receives an email notification on the same. The schedules associated with the flow are archived. Users have to reach out to flow owners to get access to the flow again and revive their schedules.
5. **Flow deleted:** When the underlying flow that has schedules configured by the user is deleted, users receive an email notification on the same.
6. **Flow version updates affecting schedules:** When the underlying flow that has schedules configured by the user gets a new version publish from owner of the flow, users get an email notification on the update. Schedules will continue to run with the updated version.

## Authentication and action handling in flow schedules

### Authentication for action connectors

While setting your schedules, ensure your authentication for actions used in the flow is up to date. You can run the flow to confirm the authentication or directly visit the [action connector](action-integrations.md "action-integrations.md") page in your Amazon Quick Suite to sign in. If your authentication expires before the scheduled run, you will receive an email notification to complete your authentication for your action connector.

###### To verify action connector authentication

1. Run the flow manually to confirm authentication is current.
2. Alternatively, in the navigation pane, choose **Integrations** and navigate to **Actions**.
3. Locate the action connector used in your flow.
4. Choose **Sign in** if authentication has expired.

### Action form submission

**Automatic form submit - Run flow with no action confirmation**

- Users get an option to auto-submit forms while configuring their schedules. Doing so, all actions will be automatically submitted during the schedule run.
- Automatic form submit option is only shown for write actions.
- This configuration is enabled by default. If you opt out, for each scheduled run, you will be notified by email to review and confirm each action.

###### Note

User confirmation is recommended to help avoid AI prediction errors and security threats.
