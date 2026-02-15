# Viewing your account events in the

AWS Health Dashboard

You can sign in to your account to get personalized events and recommendations.

###### To view account events in your AWS Health Dashboard

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. In the navigation pane, for **Your account health**, you can
   choose the following options:
   1. **[Open and recent
      issues](#dashboard "#dashboard")** – View recently opened and closed
      events.
   2. **[Scheduled
      changes](#scheduled-changes-account-events "#scheduled-changes-account-events")** – View upcoming events that
      might affect your services and resources.
   3. **[Other
      notifications](#notification-account-events "#notification-account-events")** – View all other
      notifications and ongoing events from the past seven days that might
      affect your account.
   4. **[Event log](#event-log "#event-log")**
      – View all events from the past 90 days.

## Open and recent issues

Use the **Open and recent issues** tab to view all ongoing events
from the past seven days that might affect your account.

When you choose an event from the dashboard, the **Details** pane
appears with information about the event and a list of affected resources. For more
information, see [Event details](#event-details "#event-details").

You can filter the events that appear in any tab by choosing options from the
filter list. For example, you can narrow the results by Availability Zone, Region,
event end time or last update time, AWS service, and so on.

To see all the events, rather than the recent ones that appear in the dashboard,
choose the **[Event log](#event-log "#event-log")** tab.

###### Note

Currently, you can’t delete notifications for events that appear in your
AWS Health Dashboard. After an AWS service resolves an event, the notification is removed
from your dashboard view.

###### Example: Operational issue event for Amazon Elastic Compute Cloud (Amazon EC2)

The following image shows an event for launch failures and connectivity issues
for Amazon EC2 instances.

![Screenshot of your account events in the AWS Health console.](images/health-dashboard-your-account-events.png)

## Scheduled changes

Use the **Scheduled changes** tab to view upcoming events that
might affect your account. These events can include scheduled maintenance activities
for services and planned lifecycle events that require action to resolve. To help
you plan for these activities, a calendar view is provided so that you can map these
scheduled changes into a monthly calendar. Filters are available. For more
information about planned lifecycle events, see [Planned lifecycle events for
AWS Health](aws-health-planned-lifecycle-events.md "aws-health-planned-lifecycle-events.md").

## Other notifications

Use the **Notifications** tab to view all other notifications and
ongoing events from the past seven days that might affect your account. This can
include events, such as certificate rotations, billing notifications, and security
vulnerabilities.

## Event log

Use the **Event log** tab to view all AWS Health events. The log
table includes additional columns so that you can filter by
**Status** and **Start time**.

When you choose an event in the **Event log** table, the
**Details** pane appears with information about the event and
the list of affected resources. For more information, see [Event details](#event-details "#event-details").

You can choose the following filter options to narrow your results:

- Availability Zone
- End time
- Event
- Event ARN
- Event category
- Last update time
- Region
- Resource ID / ARN
- Service
- Start time
- Status

###### Example: Event log

The following image shows recent events for the US East (N. Virginia) and
US East (Ohio) Regions.

![Screenshot of the event log tab in the AWS Health console.](images/event-log-aws-health-console.png)

## Event details

When you choose an event, two tabs appear about the event. The
**Details** tab shows the following information:

- Service
- Status
- Region / Availability Zone
- Whether or not the event is account specific
- Start and end time
- Category
- Number of affected resources
- Description and a timeline of updates about the event

The **Affected resources** tab shows the following information
about any AWS resources that are affected by the event:

- The resource ID (for example, an Amazon EBS volume ID such as
  `vol-a1b2c34f`) or Amazon Resource Name (ARN), if available
  or relevant.
- For planned lifecycle events, this affected resources list also contains
  the latest status of the resources (**Pending**,
  **Unknown**, or **Resolved**). This
  list usually refreshes once every 24 hours, but might take up to 72 hours to reflect the current status.

You can filter the items that appear in the resources. You can narrow your results
by resource ID or ARN.

###### Example: AWS Health event for AWS Lambda

The following screenshot shows an example event for Lambda.

![Screenshot of the details pane for an event in the AWS Health console.](images/event-log-details-pane-aws-health-console.png)

## Events types

There are two types of AWS Health events:

- _Public events_ are service events that
  aren't specific to an account. For example, if there is an issue with Amazon EC2
  in an AWS Region, AWS Health provides information about the event, even
  if you don't use services or resources in that Region.
- _Account-specific_ events are specific to
  your account or an account in your organization. For example, if there's an

issue with an Amazon EC2 instance in an AWS Region that you use, AWS Health provides

information about the event and the list of affected Amazon EC2 instances.

You can use the following options to identify if an event is public or
account-specific:

- In the AWS Health Dashboard, choose the **Affected resources** tab for
  an event. Events with resources are specific
  to your account. Events without resources are public and are not specific to
  your account. For more information, see [Getting started with your
  AWS Health Dashboard](getting-started-health-dashboard.md "getting-started-health-dashboard.md").
- Use the AWS Health API to return the `eventScopeCode`
  parameter. Events can have the `PUBLIC`,
  `ACCOUNT_SPECIFIC`, or `NONE` value. For more
  information, see the [DescribeEventDetails](../APIReference/API_DescribeEventDetails.md "../APIReference/API_DescribeEventDetails.md") operation in the
  _AWS Health API Reference_.

## Calendar view

**Calendar view** is available in the **scheduled
changes** tab to project AWS Health events into a monthly calendar.
This view allows you to see scheduled changes up to 3 months into the past and a
year into the future.

AWS Health events are displayed by date. Select a date to display a side panel
that contains further details on the AWS Health event.
**Upcoming** and **ongoing** events are
displayed in black. **Completed** events are displayed in grey. If
there are more than two events in a date, only the number of black and grey events
are shown. Select a date to display a list of AWS Health events in the side panel.
You can select an event in the side panel to display information about the event.
The side panel has breadcrumbs to navigate to an earlier view.

![Scheduled changes calendar view](images/calendar-view2.png)

## Affected resources view

AWS Health events might specify the precise resources that are affected. You can
view affected resources in the **Affected Resources** tab of the
AWS Health event. To view the status, select the AWS Health event. The status
displays in the affected resources tab in the side panel. For planned lifecycle
events, AWS Health events provide daily updates of the affected resources' status.

Account-level AWS Health events display a summary of affected resources statuses
at the top of the **Affected Resources** tab. A list of affected
resources is displayed in a table along with the corresponding status. Planned
lifecycle events are an example of event types that use the resource status field.
To learn more about planned lifecycle events, see [Planned lifecycle events for
AWS Health](aws-health-planned-lifecycle-events.md "aws-health-planned-lifecycle-events.md").

When you access the organization view, AWS Health events display a summary of the
status of all affected resources for all included accounts. After the summary is a
list of affected accounts and the number of pending resources for that account.
Select the account number or the number of pending resources to display the account
view summary. The account view summary has breadcrumbs to navigate back to the
organizational list of affected accounts. A summary of affected resource statuses is
displayed at the top of the split panel.

You can download the list of affected resources in the affected resources tab in
CSV or JSON format. In organizational view, the downloaded file includes all
resources in the accounts listed. Navigate to the account level in organizational
view to include only resources for that account in the downloaded file. Each
affected resource in the downloaded file includes the AWS account ID, the
eventARN, the entity name, the entityARN, status, and the last updated time of the
resource. If filters are activated, the downloaded file only includes the filtered
results.

You can download only one file at a time. The files are automatically downloaded
into the default download folder of your browser and have a preset file name based
on the AWS Region, the event title, the event start date, and the download date.

![Affected resources view](images/affected-resources.png)

## Time zone settings

You can view the events in the AWS Health Dashboard in your local time zone or in UTC. If you
change the time zone in your AWS Health Dashboard, all timestamps in the dashboard and public
events update to the time zone that you specify.

###### To update your time zone settings

1. Open your AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/ "https://health.aws.amazon.com/health/").
2. At the bottom of the page, choose **Cookie
   preferences**.
3. Select **Allowed** for Functional cookies. Then choose
   **Save preferences**.
4. In the navigation pane of your AWS Health Dashboard, choose **Time zone
   settings**.
5. Select a time zone for your AWS Health Dashboard sessions. Then choose **Save
   changes**.

## Your organization health

AWS Health integrates with AWS Organizations so that you can view events for all accounts
that are part of your organization. This provides you a centralized view for events
that appear in your organization. You can use these events to monitor for changes in
your resources, services, and applications.

For more information, see [Aggregating AWS Health events across accounts](aggregate-events.md "aggregate-events.md").

![Screenshot of the Enable organizational view page in the AWS Health console.](images/organizational-view-aws-health-console.png)

## Alerts for AWS Health events

Your AWS Health Dashboard has a bell icon in the console navigation bar with an alert menu. This
feature displays the number of recent AWS Health events that appear on the
dashboard in each category. This bell icon appears on several AWS consoles, such
as those for Amazon EC2, Amazon Relational Database Service (Amazon RDS), AWS Identity and Access Management (IAM), and AWS Trusted Advisor.

Choose the bell icon to see if recent events affect your account. You can then
choose an event to navigate to your AWS Health Dashboard for more information.

###### Example: Open events

The following image shows open and notification events for an account.

![Screenshot of the notification bell icon in the AWS Health console.](images/aws-health-dashboard-bell-icon.png)
