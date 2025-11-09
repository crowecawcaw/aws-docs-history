# Explore

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

In a Grafana workspace, the dashboard UI provides tools for building dashboards for
visualization. _Explore_ strips away all the dashboard and panel options
so that you can focus on the query. Iterate until you have a working query, and then plan
and build a dashboard.

For infrastructure monitoring and incident response, you no longer need to switch to
other tools to debug what went wrong. You can use Explore to dig deeper into your metrics
and logs to find the cause.

Explore makes it easier to view your data without creating a dashboard. If your data
source supports graph and table data, Explore shows the results both as a graph and as a
table. This helps you to see trends in the data and more details at the same time.

## Start exploring

###### Note

By default, users with the Viewer role cannot edit and do not have access to
Explore.

The **Explore** icon on the left side menu opens an empty Explore
tab.

To start with an existing query in a panel, choose the **Explore**
option from the **Panel** menu. This opens an Explore tab that contains
the query from the panel. You can then to tweak or iterate in the query outside of your
dashboard.

Choose your data source from the dropdown list in the top left. Prometheus has a
custom Explore implementation. The other data sources use their standard query editor.

In the query field, you can write your query and explore your data. There are three
buttons beside the query field, a clear button (X), an add query button (+) and the
remove query button (-). As in the panel query editor, you can add and remove multiple
queries.

## Splitting and comparing

The split view feature is a way to compare graphs and tables side-by-side or to look
at related data together on one page. Choose **Split** to duplicate the
current query and split the page into two side-by-side queries. You have the option of
selecting a different data source for the new query. This gives you the opportunity to
compare the same query for two different servers or to compare the staging environment
to the production environment.

In split view, time pickers for both panels can be linked (if you change one, the
other gets changed as well) by choosing one of the time-sync buttons attached to the
time pickers. Linking the time pickers helps keep the start and end times of the split
view queries in sync, so that you’re looking at the same time interval in both split
panels.

You can close the newly created query by choosing **Close
Split**.

## Sharing a shortened link

Use the **Share shortened link** capability to create smaller and
simpler URLs of the format `/goto/:uid` instead of sharing longer URLs that
contain complex query parameters. You can create a shortened link by choosing the
**Share** option in the Explore toolbar. Any shortened
links that are never used are automatically deleted after 7 days.

## Query history

Query history is a list of queries that you have used in Explore. The history is
local to your browser and is not shared. To open and interact with your history, choose
**Query history** in Explore.

### Viewing the query history

FIn the query history, you can do the following:

- Run a query.
- Create or edit a comment.
- Copy a query to the clipboard.
- Copy a shortened link with the query to the clipboard.
- Star a query.

### Managing favorite queries

All queries that have been starred in the Query history tab are displayed on the
Starred tab. You can access your favorite queries faster and reuse those queries
without retyping them from.

### Sort query history

By default, query history shows you the most recent queries. You can sort your
history by date or by data source name in ascending or descending order.

On the right side of the query history, in the dropdown list, choose one of the
following options: field.

- Newest first
- Oldest first
- Data source A-Z
- Data source Z-A

###### Note

If you are in split view, the sorting mode applies only to the active panel.

### Filter query history

On the **Query history** and **Starred** tabs,
you can filter the query history by data source name.

1. Choose **Filter queries for specific data
   source(s)**.
2. Select the data source that you want to use to filter your history. You
   can select multiple data sources.

On the **Query history** tab, you can use the
vertical slider to filter queries by date:

- Drag the lower handle to adjust the start date.
- Drag the upper handle to adjust the end date.

###### Note

If you are in split view, filters are applied only to the active panel.

### Searching in the query history

You can search in your history across queries and your comments. Search is
possible for queries in the **Query history** and
**Starred** tabs.

1. Choose the **Search queries** field.
2. In the search field, enter your search term.

### Query history settings

You can customize the query history in the **Settings** tab. The
following table lists the available options.

| Setting                                                                       | Default value                                                                      |
| ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Specify how long Grafana will save your query history.                        | 1 week                                                                             |
| Change the default active tab.                                                | Query history tab                                                                  |
| Show queries only for the data source that is currently active<br>in Explore. | True                                                                               |
| Clear query history.                                                          | (Choose \*_Clear query history_<br>• to permanently<br>delete all stored queries.) |

###### Note

Query history settings are global, and they are applied to both panels in
split mode.

## Prometheus-specific features

The first version of Explore features a custom querying experience for Prometheus.
When you run a query, Grafana actually runs two queries: a normal Prometheus query for
the graph and an Instant Query for the table. An Instant Query returns the last value
for each time series, which shows a good summary of the data shown in the graph.

### Metrics explorer

On the left side of the query field, choose **Metrics** to open the Metric Explorer. This shows a hierarchical menu
with metrics grouped by their prefix. For example, all Alertmanager metrics are
grouped under the `alertmanager` prefix. This is a good starting point
for exploring which metrics are available.

### Query field

The Query field supports automatic completion for metric names, function and
works mostly the same way as the standard Prometheus query editor. Press **Enter** to run a query.

The Autocomplete menu can be accessed by pressing **Ctrl+Space**. The Autocomplete menu contains a new History section
with a list of recently run queries.

Suggestions can appear under the Query field. Choose a suggestion to update your
query with the suggested change.

- For counters (monotonically increasing metrics), a rate function is
  suggested.
- For buckets, a histogram function is suggested.
- For recording rules, possible to expand the rules.

### Table filters

Choose the **Filter** button in the **label**
column of a table panel to add filters to the query expression. You can add filters
for multiple queries as well. The filter is added for all the queries.

## Logs integration

You can also use Explore to investigate your logs with the following data sources:

- InfluxDB
- Elasticsearch

### Logs visualization

Results of log queries are shown as histograms in the graph, and individual logs
are displayed below. If the data source does not send histogram data for the
requested time range, the logs model computes a time series based on the log row
counts bucketed by an automatically calculated time interval. The start of the
histogram is then anchored by the first log row’s timestamp from the result. The end
of the time series is anchored to the time picker’s **To** range.

#### Log level

For logs where a **level** label is specified,
Grafana uses the value of the label to determine the log level and update the
color accordingly. If the log doesn’t have a level label specified, Grafana
parses the log to find out whether its content matches any of the supported
expressions. The log level is always determined by the first match. If Grafana
is not able to determine a log level, it will be visualized with the **unknown** log level. The following table lists log
levels and the mapping of log level abbreviations and expressions.

| Supported expressions | Log level | Color      |
| --------------------- | --------- | ---------- |
| emerg                 | critical  | purple     |
| fatal                 | critical  | purple     |
| alert                 | critical  | purple     |
| crit                  | critical  | purple     |
| critical              | critical  | purple     |
| err                   | error     | red        |
| eror                  | error     | red        |
| error                 | error     | red        |
| warn                  | warning   | yellow     |
| warning               | warning   | yellow     |
| info                  | info      | green      |
| information           | info      | green      |
| notice                | info      | green      |
| dbug                  | debug     | blue       |
| debug                 | debug     | blue       |
| trace                 | trace     | light blue |
| \*                    | unknown   | grey       |

### Visualization options

You can customize how logs are displayed and select which columns are shown.

#### Time

This option shows or hides the time column. This is the timestamp that is
associated with the log line as reported from the data source.

#### Unique labels

This option shows or hides the unique labels column, which includes only
non-common labels. All common labels are displayed above.

#### Wrap lines

To use line wrapping in the display, set this to **True**.
Setting this option to **False** results in horizontal
scrolling.

#### Deduping

Log data can be very repetitive. Explore can help by hiding duplicate log
lines. You can choose from different deduplication algorithms:

- Exact – Exact matches are done on
  the whole line except for date fields.
- Numbers – Matches are done on the
  line after stripping out numbers such as durations, IP addresses, and so
  on.
- Signature – The most aggressive
  deduping, this strips all letters and numbers. Matches are done on the
  remaining whitespace and punctuation.

#### Flip results

order

You can change the order of received logs from the default descending order
(newest first) to ascending order (oldest first).

### Labels and detected fields

Each log row has an extendable area with its labels and detected fields, for more
robust interaction. For all labels, you can filter for (positive filter) and filter
out (negative filter) selected labels. Each field or label also has a stats icon to
display one-time statistics in relation to all displayed logs.

### Toggle detected fields

If your logs are structured in JSON or logfmt, you can show or hide detected
fields. Expand a log line, and then choose the eye icon to show or hide fields.

{{< docs-imagebox img="/img/docs/explore/parsed-fields-7-2.gif"
 max-width="800px" caption="Toggling detected fields in
 Explore" >}}

## Tracing integration

You can visualize traces from tracing data sources in Explore. Data sources currently
supported:

- [Connect to a Jaeger data source](jaeger-data-source.md "jaeger-data-source.md")
- [Connect to a Tempo data source](tempo-data-source.md "tempo-data-source.md")
- [Connect to an AWS X-Ray data source](x-ray-data-source.md "x-ray-data-source.md")
- [Connect to a Zipkin data source](zipkin-data-source.md "zipkin-data-source.md")

For information on using the query editor, see the documentation for the specific
data source.

### Header

The header includes the following items:

- Header title, which shows the name of the root span and trace ID
- Search, which highlights spans that contain the searched text
- Metadata about the trace

### Minimap

Minimap shows a condensed view or the trace timeline. Drag your mouse over the
minimap to zoom into a smaller time range. Zooming will also update the main
timeline, so it's easy to see shorter spans. If you pause on the minimap, when
zoomed, you can see the **Reset Selection** button, which resets
the zoom.

### Timeline

The timeline shows a list of spans within the trace. Each span row consists of
the following components:

- **Expand children** button: Expands or collapses all the
  children spans of selected span
- Service name: Name of the service that logged the span
- Operation name: Name of the operation that this span represents
- Span duration bar: Visual representation of the operation duration within
  the trace

Choosing anywhere on the span row shows span details.

### Span details

The span details include the following items:

- Operation name
- Span metadata
- Tags (any tags associated with this span)
- Process metadata (metadata about the process that logged this span)
- Logs: List of logs logged by this span and associated key values. In case
  of Zipkin logs section shows Zipkin annotations.

## Navigating between Explore

and a dashboard

To help accelerate workflows that involve regularly switching from Explore to a
dashboard and vice-versa, we’ve added the ability to return to the origin dashboard
after navigating to Explore from the panel’s dropdown.

After you’ve navigated to Explore, you should notice a "Back" button in
the Explore toolbar.

Simply choosing the button will return you to the origin dashboard, or, if you’d like
to bring changes you make in Explore back to the dashboard, simply choose the arrow next
to the button to reveal a "Return to panel with changes" menu item.

## Query inspector

To help with debugging queries, Explore allows you to investigate query requests and
responses, as well as query statistics, via the Query inspector. This functionality is
similar to the panel inspector **Stats** tab and
**Query** tab. For more information, see [Inspect query performance](inspect-a-panel.md#inspect-query-performance "inspect-a-panel.md#inspect-query-performance") and
[View raw request
and response to data source](inspect-a-panel.md#view-raw-request-and-response-to-data-source "inspect-a-panel.md#view-raw-request-and-response-to-data-source").
