# Queries

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

Grafana workspace panels use _Queries_ to communicate with data
sources to get data for the visualization. A query is a question written in the query
language that is used by the data source. If the query is properly formed, the data
source responds. In the panel data source options, you can adjust how often the query is
sent to the data source and how many data points are collected.

Grafana workspaces supports up to 26 queries per panel.

## Query editors

Query editors are forms that help you write queries. Depending on your data
source, the query editor might provide automatic completion, metric names, or
variable suggestion.

Because of differences between query languages, data sources might have query
editors that look different.

## Query syntax

Data sources have different query languages and syntaxes to ask for the data.
Here are two query examples.

**PostgreSQL**

```

SELECT hostname FROM host WHERE region IN($region)

```

**PromQL**

```

query_result(max_over_time(<metric>[${__range_s}s]) != <state>)

```

For more information about writing a query for your data source, see the
documentation for that data source. Data sources are listed in [Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").

## Query tab UI

The **Query** tab consists of the following elements:

- Data source selector
- Query options
- Query inspector button
- Query editor list

### Data source selector

The data source selector is a dropdown list. Choose it to select a data
source that you have added. When you create a panel, Amazon Managed Grafana automatically
selects your default data source. For more information about data sources, see
[Connect to data sources](AMG-data-sources.md "AMG-data-sources.md").

In addition to the data sources that you have configured in your Grafana
workspace, three special data sources are available.

- TestDataDB – A built-in data
  source that generates random walk data. The Grafana data source is
  useful for testing visualizations and running experiments.
- Mixed – A data source for querying
  multiple data sources in the same panel. When this data source is
  selected, you can select a data source for every new query that you
  add.
  - The first query will use the data source that was selected
    before you selected **Mixed**.
  - You cannot change an existing query to use the Mixed data
    source.

- Dashboard –A data source for
  using a result set from another panel in the same dashboard.

### Query options

To see settings for your selected data source, choose **Query
options** next to the data source selector. Changes you make here
affect only the queries made in this panel.

Amazon Managed Grafana sets defaults that are shown in dark gray text. Changes are
displayed in white text. To return a field to the default setting, delete the
white text from the field.

You can use the following panel data source query options:

- Max data points – If the data
  source supports it, sets the maximum numbers of data points for each
  series returned. If the query returns more data points than the max data
  points setting, the data source consolidates them (reduces the number of
  points returned by aggregating them together by average or max or other
  function).

There are two main reasons for limiting the number of points:
performance and smoothing the line. The default value is the width (or
number of pixels) of the graph, which avoids having more data points
than the graph panel can display.

With streaming data, the max data points value is used for the
rolling buffer. (Streaming is a continuous flow of data, and buffering
is a way to divide the stream into chunks).

- Min interval – Sets a minimum limit
  for the automatically calculated interval, typically the minimum scrape
  interval. If a data point is saved every 15 seconds, you don't need to
  have an interval lower than that. Another use case is to set it to a
  higher minimum than the scrape interval to get more coarse-grained,
  well-functioning queries.
- Interval – A time span that you can
  use when aggregating or grouping data points by time.

Amazon Managed Grafana automatically calculates an appropriate interval that can
be used as a variable in templated queries. The variable is either in
seconds: `$__interval`; or in milliseconds:
`$__interval_ms`. It is typically used in aggregation
functions like `sum` or `average`. For example,
this is a Prometheus query using the interval variable:
`rate(http_requests_total[$__interval])`.

This automatic interval is calculated based on the width of the
graph. If the user zooms out a lot, the interval becomes greater
resulting in a more coarse-grained aggregation. If the user zooms in,
the interval decreases resulting in a more fine-grained aggregation.

For more information, see [Global variables](variables-types.md#global-variables "variables-types.md#global-variables").

- Relative time – Override of the
  relative time range for individual panels causing them to be different
  from what is selected in the dashboard time picker in the top-right
  corner of the dashboard. This
  enables
  you to show metrics from different time periods or days on the same
  dashboard.
- Time shift – Provides another way
  to override the time range for individual panels. This function works
  only with relative time ranges, and you can adjust the time range.

For example, you can shift the time range for the panel to be 2 hours
earlier than the dashboard time picker. For more information, see [Time range controls](dashboard-time-range-controls.md "dashboard-time-range-controls.md").

- Cache timeout – (This field is
  visible only if it is available in your data source.) Overrides the
  default cache timeout if your time series store has a query cache. It is
  specified as a numeric value in seconds.

### Query inspector button

You can choose **Query inspector** to open the
**Query** tab of the panel inspector. On the
**Query** tab, you can see the query request sent by the
panel and the response.

Choose **Refresh** to see the full text of the request sent
by this panel to the server.

###### Note

You need to add at least one query before the Query inspector can return
results.

For more information about the panel inspector, see [Inspect a panel](inspect-a-panel.md "inspect-a-panel.md").

### Query editor list

In the UI, queries are organized in collapsible query rows. Each query row
contains a query editor and is identified with a letter (A, B, C, and so on).

## Sharing query results between

panels

With Amazon Managed Grafana, you can use the query result from one panel for any other panel
in the dashboard. Sharing query results across panels reduces the number of queries
made to your data source, which can improve the performance of your dashboard.

The Dashboard data source lets you select a panel in your dashboard that contains
the queries that you want to share the results for. Instead of sending a separate
query for each panel, Amazon Managed Grafana sends one query, and other panels use the query
results to construct visualizations.

This strategy can drastically reduce the number of queries being made when, for
example, you have several panels visualizing the same data.

###### To share data source queries with another panel

1. Create a dashboard. For more information, see [Creating a dashboard](getting-started-grafanaui.md#create-a-dashboard "getting-started-grafanaui.md#create-a-dashboard").
2. Add a panel. For more information, see [Adding a panel](add-a-panel-to-a-dashboard.md "add-a-panel-to-a-dashboard.md").
3. Change the title to `Source panel`. You’ll use this
   panel as a source for the other panels. Define the query or queries that
   will be shared. If you don’t have a data source available at the moment, you
   can use the **Grafana** data source, which returns a random
   time series that you can use for testing.
4. Add a second panel, and then select the **Dashboard**
   data source in the query editor.
5. In **Use results from panel list**, select the first
   panel that you created.

All queries defined in the source panel are now available to the new panel.
Queries made in the source panel can be shared with multiple panels.

To go to a panel where a query is defined, choose that query.
