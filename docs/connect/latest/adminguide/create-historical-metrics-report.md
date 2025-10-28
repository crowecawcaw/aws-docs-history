# Create a custom historical

metrics report in Amazon Connect

Create your own customized historical metrics reports to look at specific data.

###### Requirement

- You must have permission to access metric data. The following security
  profiles include this permission: **CallCenterManager** and
  **QualityAnalyst**. For more information, see [Security profiles for Amazon Connect and Contact Control
  Panel (CCP) access](connect-security-profiles.md "connect-security-profiles.md").

## Grouping options

You can group the metrics included in your reports in different ways to
provide greater insight into how your contact center is performing.

You can group reports by queue, agent, agent hierarchy, routing profile, phone
number, email address, channel, Amazon Q, or subtype. Some options are limited to
instances using [service linked roles](connect-slr.md "connect-slr.md"). The
metric calculations, and therefore metrics values displayed in the report, are
different when reports are grouped differently. For example, if you group a
report by queue, the value of a metric includes all contacts associated with the
queue. If you group a report by agent, the values for the metrics associated
with queues might not provide much insight.

When you create a report, the values for calculated metrics are displayed as
rows in the report. The rows in the report are grouped by the grouping options
you select. Grouping the data enables you to generate global data for your
contact center, or more specific data for queues, agents, routing profiles, or
agent hierarchy defined in your contact center.

For example, consider the **Contacts handled** metric. This
metric is a count of the contacts handled during the time range defined for the
report. Here are the results based on the grouping:

- **Queue** - The metric is the total number of
  contacts handled during the time range from that queue by all agents in
  your contact center.
- **Agent** - The metric is the total number of
  contacts handled by that agent during the time range across all queues
  and routing profiles.
- **Routing Profile** - The metric is the total number
  of contacts handled during the time range by agents assigned that
  routing profile.
- **Queue**, then **Agent**, then
  **Routing Profile** - The metric is the total
  number of contacts that agent assigned that routing profile handled from
  that queue.

Agent activity can be included in one routing profile at a time, but agents
can switch between routing profiles over the reporting time interval. If agents
are assigned multiple routing profiles and handle contacts from multiple queues,
there are multiple rows in the report for each routing profile assigned to the
agent and the queue that the agent handled contacts from.

## Filters

When you customize a report, you can add filters to control which data is
included in the report. Some options are limited to instances using [service linked roles](connect-slr.md "connect-slr.md"). You can filter on the
following:

- **Amazon Q**—Includes data only for the
  specified Amazon Q status. If you don’t specify any Amazon Q status, data
  for all statuses are included.
- **Agent hierarchy**—Includes data only for the
  contacts handled by agents in the specified hierarchies. If you don't
  specify a hierarchy, data for all contacts handled by agents in all
  hierarchies is included. When only one hierarchy is specified, you can
  specify a more granular filter within the hierarchy.
- **Agent Queues**—Includes data only for the
  specified agent queues. If you don’t specify any agent queues, data for
  all agent queues are included. This option is only available when the
  [show agent queues](show-agent-queues.md "show-agent-queues.md") checkbox
  is selected.
- **Channel**—Includes data only for the
  specified channels. If you don't specify any channels, data for all
  channels are included.
- **Phone number**—Includes data only for the
  contacts associated with the specified phone numbers. If you don't
  specify a phone number, data for all contacts associated with any or no
  phone numbers is included.
- **Email address**—Includes data only for the
  contacts associated with the specified email address. If you don't
  specify an email address, data for all contacts associated with any or
  no email address is included.
- **Queue**—Includes data only for the specified
  queues. If you don't specify any queues, data for all queues are
  included.
- **Routing profile**—Includes data only for the
  agents assigned to the specified routing profiles. If you don't specify
  any routing profiles, data for all agents for all routing profiles is
  included.
- **Subtype**—Includes data only for the
  specified subtypes. If you don’t specify any subtypes, data for all
  subtypes are included.

## How to create a historical

metrics report

1. Log in to the Amazon Connect admin website at https://`instance name`.my.connect.aws/.
2. Choose **Analytics and optimization**,
   **Historical metrics**.
3. Choose one of the following report types, which group and order the
   data in different ways, and include different metrics:
   - **Queues**
     - **Contact metrics**
     - **Agent metrics**

   - **Agents**
     - **Agent performance**
     - [Agent activity audit report in
       Amazon Connect](agent-activity-audit-report.md "agent-activity-audit-report.md")

   - **Phone numbers**
     - **Contact metrics**

   - **Email addresses**
     - **Email contact metrics**

4. To customize your report, choose the gear icon.
5. On the **Interval & Time range** tab, do the
   following:
   1. For **Interval**, choose **30
      minutes** to get a row for each 30-minute period in
      the time range, **Daily** to get a row for each
      day in the time range, or **Total** to get all
      data for the time range in a single row.
   2. For **Time Zone**, select a time zone, which
      determines the hour at which a day starts. For example, to align
      the report with your calendar days, select the time zone for
      your location.

   You should use the same time zone for reports over time to get
   accurate and consistent metrics data for your contact center.
   Using different time zones for different reports may result in
   different data for the same time range selection. 3. The possible values for **Time range** depend
   on the value that you select for **Interval**.
   Alternatively, you can specify a custom time range.

   For **Last _x_ days** and
   **Month to date**, the current day is not
   included in the report. **Yesterday** specifies
   the previous calendar day while **Last 24
   hours** specifies the 24 hours prior to the current
   time.

6. (Optional) On the **Groupings** tab, choose up to
   five groupings. If you choose one grouping option, the data is grouped
   by that option. If you choose multiple grouping options, the data is
   group by the first grouping option and then by the subsequent grouping
   options. For more information, see [Grouping options](#historical-metrics-groupings "#historical-metrics-groupings").
7. (Optional) On the **Filters** tab, specify filters to
   scope the data to be included in the report. The available filters
   depend on the groupings that you select. For more information, see [Filters](#historical-metrics-filters "#historical-metrics-filters").
8. On the **Metrics** tab, choose the metrics and fields
   to include in the report. An exclamation point (!) is displayed next to
   any metrics that are not available based on the groupings that you
   selected. For more information, see [Metric definitions in Amazon Connect](metrics-definitions.md "metrics-definitions.md").
9. When you are finished customizing your report, choose
   **Apply**.
10. (Optional) To save your report for future use, choose
    **Save**, provide a name for the report, and then
    choose **Save**.
