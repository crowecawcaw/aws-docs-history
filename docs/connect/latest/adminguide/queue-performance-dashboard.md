# Queue and agent performance dashboard in Connect Customer

The **Queue and agent performance** dashboard helps you understand
the performance of your queues and agents compared over configurable periods of time. It
uses key metrics such as contacts handled, service level, and average handle time.

This dashboard includes:

- Real-time statistics such as number of agents online and current agent
  activity. It has the capabilities and metrics that are available on the
  **Real-time metrics** page.
- [Customer first callback
  mode](customer-first-cb.md#customer-first-callback-metrics "customer-first-cb.md#customer-first-callback-metrics") metrics. These metrics are only available on the dashboard and
  by calling the [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API. They're not available on the Historical
  metrics report.

###### Contents

- [Enable access to the dashboard](#queue-performance-dashboard-enable-access "#queue-performance-dashboard-enable-access")
- [Performance overview chart](#queue-performance-dashboard-performance-overview "#queue-performance-dashboard-performance-overview")
- [Current queue overview](#current-queue-overview "#current-queue-overview")
- [Current agent performance](#current-agent-perf-overview "#current-agent-perf-overview")
- [One-click drill-down](#one-click-drilldown "#one-click-drilldown")
- [Toggle between table and bar chart](#toggle-table-bar-chart "#toggle-table-bar-chart")
- [Current agent adherence](#current-agent-adherence-dashboard "#current-agent-adherence-dashboard")
- [Trailing agent adherence](#trailing-agent-adherence-dashboard "#trailing-agent-adherence-dashboard")
- [Trailing agent performance](#trailing-agent-performance "#trailing-agent-performance")
- [Average queue answer time and contacts queued trend](#avg-queue-answer "#avg-queue-answer")
- [Contacts handled and average handle time trend](#queue-performance-dashboard-contacts-handled "#queue-performance-dashboard-contacts-handled")
- [Agent status drill down](#agent-status-drill-down "#agent-status-drill-down")
- [Dashboard functionality limitations](#queue-performance-dashboard-functionality-limitations "#queue-performance-dashboard-functionality-limitations")

## Enable access to the dashboard

Ensure users are assigned the appropriate security profile permissions:

- **Access metrics - Access permission** or the
  **Dashboard - Access permission**. For information
  about the difference in behavior, see [Assign permissions to view dashboards and reports in Connect Customer](dashboard-required-permissions.md "dashboard-required-permissions.md").

## Performance overview chart

The **Performance overview** chart that provides aggregated
metrics based on your filters. Each metric within the chart is compared to your
"compare to" benchmark time range filter.

The following image shows an example **Performance overview**
chart:

![An example Performance overview chart in the dashboard.](images/queue-performance-dashboards-performance-overview-chart.png)

- **Contacts handled** during your time range selection was
  126,306, which is down ~13% compared to your benchmark number of contacts
  handled, 144,647 contacts.
- The percentages are rounded up or down.
- The colors that appear for the metrics indicate positive (green) or
  negative (red) compared to your benchmark.
- There are no colors for **Contacts handled**.

## Current queue overview

The **Current queue overview** widget provides real-time snapshot
metrics that display what is happening right now in your queues. You can configure
this widget in multiple ways including changing the metrics (but only to real-time
queue metrics), configuring the queues that are included, and re-ordering the
metrics.

The following image shows an example **Current queue
overview**.

![An example Current queue overview in the dashboard.](images/dashboard-current-queue.png)

## Current agent performance

The **Current agent performance** widget provides a real-time
view of what agents are doing (equivalent to the real-time metrics page agent
widget) including time in status, current active contacts, and the next activity.

By default, this widget collapses the rows to give you an at a glance view of what
agents are doing. Choose **Expand all** to automatically expand all
the rows for a complete view of agent performance.

With the appropriate security profile permissions, from this widget you can listen
in to contacts and change agent statuses within this widget (similar to the
real-time metrics page).

###### Note

You can't change the grouping of this widget.

The following image shows an example **Current agent
performance**.

![An example of Current agent performance in the dashboard.](images/dashboard-current-agent-performance.png)

### Thresholds

You can also set thresholds on this widget, but several of the metrics behave
slightly differently. For agent activity you need to select two
conditions:

- What the activity type is (for example, rejected)
- The duration of that activity

You configure custom thresholds based on the state. For example, you can
define a cell that should flip to red if an agent is in missed call state for
more than 5 seconds but also only flip to red if an agent is on hold for more
than 5 minutes.

The following image shows an example of thresholds set on the
**Activity** metric.

![An example of thresholds set for the Activity metric.](images/dashboard-thresholds-3.png)

### Contact state filtering

You can filter by contact states to identify specific agents who have a
contact within a specific state. For example, if you want to quickly identify
agents who have a contact in error and can't be routed additional contacts, you
can filter for "Missed" and "Rejected" to identify those agents and change their
status.

The following image shows a list of some of the filters available for contact
states.

![An example of the filters you can apply to Contact state.](images/dashboard-contact-state-filtering.png)

## One-click drill-down

Use the one-click drill-down feature to quickly create a new widget filtered
by a specific queue or routing profile. This can help you investigate performance
details without manually configuring a new widget.

When viewing a real-time widget grouped by queue or routing profile, a
drill-down menu appears next to each resource name. Choose the drill-down menu
to select the type of widget you want to create.

![A Current queue performance widget showing the drill-down menu button next to a queue name.](images/drilldown-more-options-button.png)

### When grouped by queue

The following options are available when your widget is grouped by queue:

- **View agents** – Creates a
  **Current agent performance** widget filtered by the
  selected queue.
- **View routing profile** – Creates a
  **Current routing profile performance** widget
  filtered by the selected queue.

![The drill-down menu for a queue, showing View agents and View routing profile options.](images/drilldown-grouped-by-queue.png)

### When grouped by routing profile

The following options are available when your widget is grouped by routing
profile:

- **View agents** – Creates a
  **Current agent performance** widget filtered by the
  selected routing profile.
- **View queue** – Creates a
  **Current queue performance** widget filtered by the
  selected routing profile.

![The drill-down menu for a routing profile, showing View agents and View queue options.](images/drilldown-grouped-by-routing-profile.png)

The new widget is automatically filtered by the selected resource and inserted
after the current widget on your dashboard.

![A new widget created by one-click drill-down, filtered by the selected routing profile.](images/drilldown-new-widget-result.png)

### Limitations

The one-click drill-down feature has the following limitations:

- One-click drill-down is not available when the dashboard has
  reached the maximum of 11 widgets.
- One-click drill-down is not available when using the
  [Filter by queue type](dashboard-customize-widgets.md#filter-by-queue-type "dashboard-customize-widgets.md#filter-by-queue-type").
- One-click drill-down is only available on real-time widgets. It is
  not available on historical widgets.

## Toggle between table and bar chart

You can switch chart widgets to a table view to see exact metric values.

To switch between chart and table views:

1. Choose **Actions** in the widget header.
2. Choose **Show as table**.

![A chart widget with the Actions menu open, showing the Show as table option.](images/show-as-table-actions-menu.png)

A checkmark appears next to the option when table view is active. To return to
the chart view, choose **Show as table** again.

![A widget displaying data in table view, with a checkmark next to Show as table in the Actions menu.](images/show-as-table-result.png)

## Current agent adherence

The **Current agent adherence** widget provides a real-time view of agent
adherence metrics, including adherence status, duration, and percentage, enabling
supervisors to monitor and manage agent adherence. This widget supports filtering on
adherence status, duration, and percentage, sorting by duration or percentage, and
conditional formatting on duration and percentage to quickly identify adherence
breaches and take prompt action to address issues.

For example, you can filter for agents with a **Non-adherent**
status, sort by adherence duration, and highlight duration greater than 5 minutes to
quickly identify breaches and send reminders to bring agents back on task.

The following image shows an example of the **Current agent adherence**
widget. The red highlight is conditional formatting applied on the
**Adherence status duration** (Adherence status duration >= 3
hours). The breach in the agent adherence is indicated by the **Non-adherent
status**.

![The Current agent adherence widget with conditional formatting.](images/dashboard-adherence-widget.png)

The following image shows an example of how to set up conditional formatting.

![How to set up conditional formatting.](images/agent-adherence-status.png)

The following image shows an example of filtering the **Adherence status
duration**. In this case, Connect Customer will display only those agents who are
not adherent for longer than 10 minutes.

![A filter set for Adherence status duration.](images/dashboard-agent-adherence-status-duration1.png)

## Trailing agent adherence

The **Trailing agent adherence** widget provides
a historical view of agent adherence over a configurable time period.
Use this widget to review adherence trends and identify patterns over time.

By default, you see adherence metrics grouped by agent, including scheduled time,
adherent time, non-adherent time, and adherence percentage.

You can group data by agent, queue, channel, routing profile, agent hierarchy levels,
and shift activity. You can filter by agent, queue, routing profile, channel, and
agent hierarchy levels. You can sort by any metric, such as adherence percentage,
to quickly identify agents who need attention.

###### Note

Historical adherence metrics data is available from May 6, 2026. Queries for dates
before May 6, 2026 return no results.

The following image shows an example of the **Trailing agent
adherence** widget.

![The Trailing agent adherence widget showing adherence metrics grouped by agent.](images/dashboard-trailing-agent-adherence.png)

## Trailing agent performance

This table provides a historical view of performance over time.

![An example of Trailing agent performance.](images/dashboard-trailing-agent-performance.png)

To see how your performance compares to the previous time range, choose
**Actions**, **Edit**. On the
**Edit** pane, choose **Show comparison**, as
shown in the following image.

![The Show comparison option in the Edit pane, the Prior information on the chart.](images/dashboard-add-comparisons.png)

You can also change the metrics, configure thresholds, or re-order
metrics.

## Average queue answer time and contacts queued trend

The **Average queue answer time and contacts queued trend** is a
time-series chart that displays the count of contacts queued (blue bars) and the
average queue answer time (red line) over a given time period broken down by
intervals (15min, daily, weekly, monthly). You can also change the metrics and add
up to four different metrics as line graphs.

###### Note

This widget can support a maximum of two metric types (count, time,
percentage).

The following image shows the Contacts queued (blue bars) and Avg queue answer
time (red line), for four months.

![An example of Average queue answer time and contacts queued.](images/dashboard-average-queue-answer-time-trend.png)

This next image shows the same data, but with the addition of the
**Contacts abandoned** (green) filter.

![An example of Average queue answer time with Contacts abandoned.](images/dashboard-contacts-abandoned.png)

## Contacts handled and average handle time trend

The **Contacts handled and average handle time trend** is a
time-series chart that displays the count of contacts handled (blue bars) and the
average handle time (red line) over a given time period broken down by intervals
(15min, daily, weekly, monthly).

To configure different time range intervals, choose **Interval**,
as shown in the following image.

![Contacts handled and average handle time trend chart.](images/queue-performance-dashboards-contacts-handled-average-handle-time.png)

The available intervals depend on the page-level time range filter. For example:

- If you have a "Today" time range filter on your dashboard, you
  can only see an interval of 15min for the last 24 hours.
- If you have a "Day" time range filter on your dashboard, you
  can see a trailing 8 day interval trend, or a 15min interval trend for the
  trailing 24 hours.

## Agent status drill down

The **Agent status drill down** widget displays the number of
agents logged into the Contact Control Panel (CCP), and their status. By default,
the widget groups data by queue. For more detail, you can add **Agent
status** as a secondary grouping to view agent count by their CCP
status within each queue.

The following image shows an example of the **Agent status drill
down** widget. It shows **Agent status** (for example,
Training, Lunch) as a secondary grouping.

![The Agent status drill down widget.](images/agent-status-drill-down.png)

## Dashboard functionality limitations

The following limitations apply to the Queue performance dashboard:

- Tag-based access controls are not supported on the dashboard.
