# Monitoring ad insertion performance with the analytics dashboard

The MediaTailor analytics dashboard is a console page that gives you a single view of the
CloudWatch metrics that MediaTailor publishes for server-side ad insertion (SSAI). Use it to
monitor monetization health across every AWS region you use, spot regressions early, and
compare performance between AWS regions without building your own CloudWatch dashboards. The
dashboard shows key monetization metrics, trend graphs, and metric tables for playback
configurations and ad tracking domains.

The dashboard queries CloudWatch on your behalf, so you can answer questions such as:

- What is my overall weighted fill rate this week, and how does it compare to
  last week?
- Which ad tracking domains are causing the most impression beacon
  retries?
- How does ad insertion performance in one AWS region compare to another?
  For definitions of the underlying CloudWatch metrics used on the analytics dashboard as
  specified on this page, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md"). To build custom alarms or your own
  CloudWatch dashboards on these metrics, use the CloudWatch console directly.

###### Note

The metric tables on the analytics dashboard call the CloudWatch
`ListMetrics` API, which counts toward your account's CloudWatch API request
usage. The key monetization metrics and trend graphs do not call
`ListMetrics`. For pricing, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Using the analytics dashboard

The analytics dashboard is a top-level page in the MediaTailor console. To open it, sign
in and choose it from the navigation pane.

###### To open the analytics dashboard

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. In the navigation pane, under **Ad insertion**, choose
   **Analytics dashboard**.

When the page opens, the dashboard loads metrics for the last 1 day in the AWS
region you are currently signed in to. You can change the time range and region
selection at any time, and each section on the page reloads against the new
selection.

To use the analytics dashboard, your IAM principal must be permitted to list
MediaTailor playback configurations and to read CloudWatch metrics. At minimum, it needs the
following actions:

- `mediatailor:ListPlaybackConfigurations`
- `cloudwatch:ListMetrics`
- `cloudwatch:GetMetricData`

These actions are included in the AWS managed policies that grant read access to
MediaTailor and CloudWatch. For general information about MediaTailor permissions, see [Identity and Access Management for AWS Elemental MediaTailor](security-iam.md "security-iam.md").

## Choosing AWS regions

MediaTailor publishes CloudWatch metrics in each AWS region where you run playback
configurations. The region selector at the top of the dashboard controls which
regions the page queries and how it combines the results.

When you first open the dashboard, MediaTailor checks each AWS region in which
MediaTailor is available and offers you the regions where your account has at least one
playback configuration. Regions in which the check could not complete are noted on
the page and can be retried. If the check fails in every AWS region, the dashboard
falls back to the AWS region you are currently signed in to.

The dashboard supports two view modes, chosen with the **Aggregate
regions** / **Compare regions** selector above the
region selector:

**Aggregate regions**

Combines metrics from every selected region into a single set of
values. Use this mode when you want to see totals and weighted averages
for your entire ad insertion footprint.

**Compare regions**

Splits the selected regions into two named groups,
**Group A** and **Group B**, and
shows each group's values side by side. For each key monetization metric,
each group's tile also displays the percentage difference from the other
group. Use this mode to compare, for example, your primary regions with
your failover regions.

For the key monetization metrics and trend graphs, how the dashboard combines
values across the selected regions depends on the metric type:

- For count metrics, the values from each selected region are summed.
- For rate metrics, the numerator and denominator from each selected region
  are summed and divided once. This produces a weighted average, so a region
  with more traffic contributes proportionally more to the result.

The metric tables display values by playback configuration or by ad tracking
domain, and each table combines region values differently depending on the view. See
the table sections later on this page for details.

## Key monetization metrics

The **Key monetization metrics** section at the top of the
dashboard shows a set of summary tiles that summarize ad insertion performance across
all of your playback configurations in the selected regions, over the selected time
range. In **Compare regions** view, each tile shows a value for each
region group, and each group's tile displays the percentage difference from the other
group.

The dashboard shows the following key monetization metrics. For definitions of
the underlying CloudWatch metrics, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").

- **Weighted fill rate** —
  `SUM(Avail.FilledDuration) / SUM(Avail.Duration) × 100`
- **Ad insertion rate** — `SUM(AdsBilled) /
 SUM(AdDecisionServer.Ads) × 100`
- **Ad impression rate** — `SUM(Avail.Impression) /
 SUM(AdsBilled) × 100`
- **Video completion rate** —
  `SUM(Avail.Complete) / SUM(Avail.Impression) × 100`
- **Ad insertions** — `SUM(AdsBilled)`

## Trend graphs

The **Trends** section shows the key monetization metrics as
time-series line charts over the selected time range. Use the trend graphs to see
how each metric moves over time and to spot regressions that a single summary value
can hide.

In **Aggregate regions** view, each chart shows a single line
representing all selected regions combined. In **Compare regions**
view, each chart shows one line per region group, with a legend identifying
**Group A** and **Group B**.

## Monetization performance by configuration table

The **Monetization performance by configuration** table shows the
key rate metrics for each of your playback configurations in the selected regions,
over the selected time range. Use this table to find configurations that are
underperforming compared to your other configurations.

Playback configurations are scoped to a specific AWS region. If the same
configuration name exists in more than one selected region, the table shows a
separate row for each region. The **Configuration name** column
links to the details page for that configuration in its region.

The table has the following columns:

- **Configuration name** — The name of the playback
  configuration.
- **Region** — The AWS region where the configuration
  exists.
- **Group** — In **Compare regions**
  view only, the region group (**Group A** or
  **Group B**) that the row's region belongs to.
- **Weighted fill rate**, **Ad insertion
  rate**, **Ad impression rate**, and
  **Video completion rate** — The rate metrics
  described in [Key monetization metrics](#analytics-dashboard-kpis "#analytics-dashboard-kpis"), computed for that
  configuration in that region over the selected time range.

Use the property filter above the table to narrow the rows shown. You can filter
by **Configuration name** or **Region**. In
**Compare regions** view, you can also filter by
**Group** to show one comparison group at a time. Each
property supports the operators **=** (equals),
**!=** (does not equal), **:** (contains), and
**!:** (does not contain).

To limit CloudWatch API usage, the table makes up to 10 `ListMetrics` calls
per selected region on each load. If any selected region has more configurations
than these calls return, the table shows an info banner listing the affected
regions and a **Load more** button. Choose **Load
more** to retrieve additional configurations from those
regions.

## Beacon firing performance table

The **Beacon firing performance** table shows CloudWatch fire,
retry, and recovery metrics for impression and complete beacons, per ad tracking
domain, in the selected regions over the selected time range. For definitions of
these metrics, see [Monitoring AWS Elemental MediaTailor with Amazon CloudWatch metrics](monitoring-cloudwatch-metrics.md "monitoring-cloudwatch-metrics.md").

Use the **Impression** and **Complete**
selector above the table to choose which beacon type the table shows. The selector
applies to both **Browse** view and **Ranked**
view.

The table supports two view modes, chosen with the **Browse**
and **Ranked** selector above the table.

### Browse view

**Browse** view lists each ad tracking domain observed in
the selected regions, with beacon counts summed across those regions. In
**Compare regions** view, an ad tracking domain that
appears in both groups is shown as one row per group.

The Browse view shows the following columns:

- **Ad tracking domain**
- **Group** — In **Compare regions**
  view only.
- **Fired**, **Retried**,
  **Recovered**, and **Retry success
  rate**

Use the property filter above the table to narrow the rows shown. You can
filter by **Ad tracking domain**, and in **Compare
regions** view by **Group**. The property filter
supports the operators **=** (equals),
**!=** (does not equal), **:**
(contains), and **!:** (does not contain).

To limit CloudWatch API usage, Browse view makes up to 10
`ListMetrics` calls per selected region on each load. If any
selected region has more ad tracking domains than these calls return, the
table shows an info banner listing the affected regions and a
**Load more** button. Choose **Load
more** to retrieve additional domains from those regions.

### Ranked view

**Ranked** view lists the top or bottom ad tracking domains
for the selected beacon count metric, with one row per (domain, region) pair.
In **Compare regions** view, ranking runs independently per
group so each group contributes its own top or bottom domains.

Use the two controls above the table to configure the ranking:

- **Metric** — The beacon count metric to rank by:
  **Fired**, **Retried**, or
  **Recovered**. **Retry success
  rate** is a computed ratio and cannot be used to rank
  rows.
- **Order** — **Ascending** or
  **Descending**.

The Ranked view shows the same columns as Browse view, plus a
**Rank** column at the start and a
**Region** column that identifies the region each (domain,
region) row belongs to. You can filter by **Ad tracking
domain**, **Region**, and (in **Compare
regions** view) **Group**.

Ranked view uses CloudWatch Metrics Insights to sort the underlying beacon
metrics. Metrics Insights only supports queries that read the last 14 days of
data. If your selected time range extends beyond 14 days, the table displays
data from the most recent 14 days instead.

## Exporting dashboard data

You can export data from the metric tables and from the trend graphs as CSV
files.

###### To export data from a metric table

1. Select the check boxes next to the rows you want to include. You can
   move between pages of the table and continue selecting rows.
2. Choose **Export CSV** above the table.

The exported file includes one column per column shown in the table. For metric
values to appear in the exported file, the page of the table that contains each
selected row must be viewed so the dashboard has loaded the row's metric
values.

To export the data from a trend graph, choose the actions menu on the graph and
then choose **Download as .csv**.
