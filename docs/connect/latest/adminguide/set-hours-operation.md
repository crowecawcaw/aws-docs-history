# Set the hours of operation and time zone for a

queue using Amazon Connect

This topic explains how to set hours of operating by using the Amazon Connect admin website. To set hours
programmatically, see [Hours of operations actions](../APIReference/hours-of-operation-api.md "../APIReference/hours-of-operation-api.md").

The first thing you need to do when you set up a queue is to specify the hours of
operation and timezone. The hours may be referenced in flows. For example, when routing
contacts to agents, you might use the [Check hours of
operation](check-hours-of-operation.md "check-hours-of-operation.md") block first, and then route the
contact to the appropriate queue.

![An Hours of operation page with overrides.](images/hoop-listpage.png)

###### Contents

- [How many hours of operation and
  overrides can I create?](#howmany-hours "#howmany-hours")
- [Set the hours of operation](#set-hoop "#set-hoop")
- [How to specify midnight](#set-hours-operation-midnight "#set-hours-operation-midnight")
- [Examples](#set-hours-operation-examples "#set-hours-operation-examples")
- [Add lunch and other breaks](#add-lunch-breaks "#add-lunch-breaks")
- [Daylight saving
  time](#daylight-savings-time "#daylight-savings-time")
- [How flows leverage hours of operation](#use-check-hours-of-operation-block "#use-check-hours-of-operation-block")
- [Set overrides for extended, reduced, and holiday hours](hours-of-operation-overrides.md "hours-of-operation-overrides.md")
- [View calendar that illustrates effective hours of operation](view-hours-of-operation-calendar.md "view-hours-of-operation-calendar.md")

## How many hours of operation and overrides can I

create?

To view your quota of **Hours of operation per
instance**, open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").

## Set the hours of operation

1. Log in to the Amazon Connect admin website with an Admin account or an account that has
   **Routing - Hours of operation - Create** security
   profile permission.
2. On the navigation menu, choose **Routing**,
   **Hours of operation**.
3. To create a set of operating hours, choose **Add new set of hours** and
   enter a name and a description.
4. Choose **Time zone** and select a value.
5. Choose **Operational hours** to set new hours.
6. Optionally, in the **Tags** section, add tags to
   identify, organize, search for, or filter who can access this hours of
   operation record. For more information, see [Add tags to resources in Amazon Connect](tagging.md "tagging.md").
7. Choose **Save**.
8. Now you can specify these the hours of operation when you [create a queue](create-queue.md "create-queue.md"), and check them in the
   [Check hours of
   operation](check-hours-of-operation.md "check-hours-of-operation.md") block.

## How to specify midnight

To specify midnight, enter 12:00AM.

For example, if you want to set your hours to 10:00AM to midnight, you would
enter: 10:00AM to 12:00AM. Your call center would be open for 14 hours. Here's the
math:

- 10:00AM-12:00PM = 2 hours
- 12:00PM-12:00AM = 12 hours
- Total = 14 hours

## Examples

**Schedule for 24x7**

![An example of a weekly, 24-hour contact center schedule.](images/set-hours-of-operation-24x7.png)

**Schedule for Monday to Friday 9:00 AM to 5:00
PM**

Select the button to **Expand to individual days**.

Remove Sunday and Saturday from the schedule.

![An example of removing days from a contact center schedule.](images/set-hours-of-operation-closed-weekends-remove.png)

## Add lunch and other breaks

Select **+ Add more time** at the bottom of the Operational
hours section to create more rows, then set the hour ranges within each day. For
example, if Saturday the hours are 8-11 then 1-5:

![A diagram showing lunch breaks in a contact center schedule.](images/hours-of-operation-lunch.png)

In most contact centers breaks are staggered. While some agents are at lunch, for
example, others are still available to handle contacts. Instead of specifying this
in the hours of operation, you [add custom agent
statuses](agent-custom.md "agent-custom.md") that appear in the agent's Contact Control Panel (CCP).

For example, you might create a custom status named **Lunch**.
When the agent goes to lunch, they change their status in the CCP from
**Available** to **Lunch**. During this time,
no contacts are routed to them. When they return from lunch and are ready to take
contacts again, they change their status back to **Available**.

Supervisors can change an agent's status using the real-time metrics
report.

For more information, see these topics:

- [Add a custom agent status to the Amazon Connect Contact Control
  Panel (CCP)](agent-custom.md "agent-custom.md")
- [Agent status in the Contact Control Panel
  (CCP)](metrics-agent-status.md "metrics-agent-status.md")
- [Change the "Agent activity" status
  in a metrics report in the Contact Control Panel (CCP)](rtm-change-agent-activity-state.md "rtm-change-agent-activity-state.md")

## What happens during daylight saving

time

Amazon Connect uses the timezone to determine whether daylight saving time is in effect for
the queues, and **adjusts automatically** for all
timezones that observe daylight saving time. When a contact comes in, Amazon Connect looks at
the hours and timezone of your contact center to determine whether the contact can
be routed to the given queue.

###### Important

Amazon Connect provides options for EST5EDT, PST8PDT, CST6CDT, and more.
For example, EST5EDT is defined as:

[Eastern Standard
Time (EST)](https://en.wikipedia.org/wiki/Eastern_Time_Zone "https://en.wikipedia.org/wiki/Eastern_Time_Zone") is used when observing standard time. It is five hours
behind Coordinated Universal Time (UTC).

[Eastern Daylight
Time (EDT)](https://en.wikipedia.org/wiki/Eastern_Time_Zone "https://en.wikipedia.org/wiki/Eastern_Time_Zone") is used when observing daylight saving time. It is four
hours behind Coordinated Universal Time (UTC).

We recommend researching your choice of timezone to ensure you understand
it.

### Example

1. A person initiates a call or chat with your contact center.
2. Amazon Connect looks at the hours of operation for your call center right
   now.
   - The contact is from timezone A.
   - Your call center's hours are 9 AM - 5 PM in timezone B.
   - If the current time in timezone B is 2 PM then the call or
     chat is queued.
   - If the current time in timezone B is 7 AM then the call or
     chat is not queued.

## How flows leverage hours of operation

Flows can be configured to check whether a contact is within or outside the
hours of operation defined by the block. The flow can then branch to follow a
different path based on the results, for example, so a message plays after hours
that offers a callback when operations resume. To learn more, go to
[Check hours of
operation](check-hours-of-operation.md "check-hours-of-operation.md").
