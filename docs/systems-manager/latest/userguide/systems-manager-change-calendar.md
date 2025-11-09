AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# AWS Systems Manager Change Calendar

Change Calendar, a tool in AWS Systems Manager, allows you to set up date and time ranges when actions you
specify (for example, in [Systems Manager Automation](systems-manager-automation.md "systems-manager-automation.md")
runbooks) might or might not be performed in your AWS account. In Change Calendar, these ranges
are called _events_. When you create a Change Calendar entry, you're creating a
[Systems Manager document](documents.md "documents.md") of the type `ChangeCalendar`.
In Change Calendar, the document stores [iCalendar 2.0](https://icalendar.org/ "https://icalendar.org/")
data in plaintext format. Events that you add to the Change Calendar entry become part of the
document. To get started with Change Calendar, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/change-calendar "https://console.aws.amazon.com/systems-manager/change-calendar"). In the navigation pane,
choose **Change Calendar**.

You can create a calendar and its events in the Systems Manager console. You can also import an
iCalendar (`.ics`) file that you have exported from a supported
third-party calendar provider to add its events to your calendar. Supported providers
include Google Calendar, Microsoft Outlook, and iCloud Calendar.

A Change Calendar entry can be one of two types:

**`DEFAULT_OPEN`**, or Open by
default

All actions can run by default, except during calendar events. During events,
the state of a `DEFAULT_OPEN` calendar is `CLOSED` and
events are blocked from running.

**`DEFAULT_CLOSED`**, or Closed by
default

All actions are blocked by default, except during calendar events. During
events, the state of a `DEFAULT_CLOSED` calendar is `OPEN`
and actions are permitted to run.

You can choose to have all scheduled Automation workflows, maintenance windows, and
State Manager associations added automatically to a calendar. You can also remove any of those
individual types from the calendar display.

## Who should use Change Calendar?

###### Change Manager availability change

AWS Systems Manager Change Manager will no longer be open to new customers
starting November 7, 2025. If you would like to use Change Manager, sign up prior to that
date. Existing customers can continue to use the service as normal. For more
information, see [AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

- AWS customers who perform the following action types:

      + Create or run Automation runbooks.
      + Create change requests in Change Manager.
      + Run maintenance windows.
      + Create associations in State Manager.

  Automation, Change Manager, Maintenance Windows, and State Manager are all tools AWS Systems Manager. By
  integrating these tools with Change Calendar, you can allow or block these action types
  depending on the current state of the change calendar you associate with each
  one.

- Administrators who are responsible for keeping the configurations of Systems Manager
  managed nodes consistent, stable, and functional.

## Benefits of Change Calendar

The following are some benefits of Change Calendar.

- **Review changes before they're applied**

A Change Calendar entry can help ensure that potentially destructive changes to your
environment are reviewed before they're applied.

- **Apply changes only during appropriate
  times**

Change Calendar entries help keep your environment stable during event times. For
example, you can create a Change Calendar entry to block changes when you expect high
demand on your resources, such as during a conference or public marketing
promotion. A calendar entry can also block changes when you expect limited
administrator support, such as during vacations or holidays. You can use a
calendar entry to allow changes except for certain times of the day or week when
there is limited administrator support to troubleshoot failed actions or
deployments.

- **Get the current or upcoming state of the
  calendar**

You can run the Systems Manager `GetCalendarState` API operation to show you
the current state of the calendar, the state at a specified time, or the next
time that the calendar state is scheduled to change.

###### Note

The `GetCalendarState` API has a quota of 10 requests per
second. For more information about Systems Manager quotas, see [Systems Manager service quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm") in the
_Amazon Web Services General Reference_.

- ###### EventBridge support

This Systems Manager tool is supported as an _event_ type in Amazon EventBridge rules.
For information, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md") and [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

###### Topics

- [Setting up Change Calendar](systems-manager-change-calendar-prereqs.md "systems-manager-change-calendar-prereqs.md")
- [Working with Change Calendar](systems-manager-change-calendar-working.md "systems-manager-change-calendar-working.md")
- [Adding Change Calendar
  dependencies to Automation runbooks](systems-manager-change-calendar-automations.md "systems-manager-change-calendar-automations.md")
- [Troubleshooting Change Calendar](change-calendar-troubleshooting.md "change-calendar-troubleshooting.md")
