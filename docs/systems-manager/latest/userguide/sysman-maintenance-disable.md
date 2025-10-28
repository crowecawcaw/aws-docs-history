# Disable or enable a maintenance window

using the console

You can disable or enable a maintenance window in Maintenance Windows, a tool in AWS Systems Manager.
You can choose one maintenance window at a time to either disable or enable the
maintenance window from running. You can also select multiple or all maintenance
windows to enable and disable.

This section describes how to disable or enable a maintenance window by using the
Systems Manager console. For examples of how to do this by using the AWS Command Line Interface (AWS CLI), see
[Tutorial: Update a
maintenance window using the AWS CLI](maintenance-windows-cli-tutorials-update.md "maintenance-windows-cli-tutorials-update.md").

###### Topics

- [Disable a maintenance window
  using the console](#sysman-maintenance-disable-mw "#sysman-maintenance-disable-mw")
- [Enable a maintenance window using
  the console](#sysman-maintenance-enable-mw "#sysman-maintenance-enable-mw")

## Disable a maintenance window

using the console

You can disable a maintenance window to pause a task for a specified period,
and it will remain available to enable again later.

###### To disable a maintenance window

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Maintenance Windows**.
3. Using the check box next to the maintenance window that you want to
   disable, select one or more maintenance windows.
4. Choose **Disable maintenance window** in the
   **Actions** menu. The system prompts you to confirm
   your actions.

## Enable a maintenance window using

the console

You can enable a maintenance window to resume a task.

###### Note

If the maintenance window uses a rate schedule and the start date is
currently set to a past date and time, the current date and time is used as
the start date for the maintenance window. You can change the start date of
the maintenance window before or after enabling it. For
information, see [Update or delete maintenance window
resources using the console](sysman-maintenance-update.md "sysman-maintenance-update.md").

###### To enable a maintenance window

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Maintenance Windows**.
3. Select the check box next to the maintenance window to enable.
4. Choose **Actions, Enable maintenance window**. The
   system prompts you to confirm your actions.
