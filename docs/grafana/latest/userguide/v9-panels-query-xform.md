

# Query and transform data
<a name="v9-panels-query-xform"></a>

****  
This documentation topic is designed for Grafana workspaces that support **Grafana version 9.x**.  
For Grafana workspaces that support Grafana version 12.x, see [Working in Grafana version 12](using-grafana-v12.md).  
For Grafana workspaces that support Grafana version 10.x, see [Working in Grafana version 10](using-grafana-v10.md).  
For Grafana workspaces that support Grafana version 8.x, see [Working in Grafana version 8](using-grafana-v8.md).

Grafana supports many types of [data sources](AMG-data-sources.md). Data source *queries* return data that Grafana can *transform* and visualize. Each data source uses its own query language, and data source plugins each implement a query-building user interface called a query editor.

## About queries
<a name="v9-panels-query-xform-about"></a>

Grafana panels communicate with data sources via queries, which retrieve data for the visualization. A query is a question written in the query language used by the data source.

You can configure query frequency and data collection limits in the panel’s data source options. Grafana supports up to 26 queries per panel.

You can find more information about each data source’s query language in the [Data sources](AMG-data-sources.md) section.

**Query editors**

Each data source’s *query editor* provides a customized user interface that helps you write queries that take advantage of its unique capabilities.

Because of the differences between query languages, each data source query editor looks and functions differently. Depending on your data source, the query editor might provide auto-completion features, metric names, variable suggestions, or a visual query-building interface.

For details on a specific data source’s unique query editor features, refer to its documentation:
+ For data sources included with Grafana, see [Built-in data sources](AMG-data-sources-builtin.md).
+ For data sources included with Grafana Enterprise editiion, see [Connect to Enterprise data sources](AMG-data-sources-enterprise.md).

**Query syntax**

Data sources use different query languages to request data. For details on a specific data source’s unique query language, refer to its documentation.

**PostgreSQL example:**

```
SELECT hostname FROM host WHERE region IN($region)
```

**PromQL example:**

```
query_result(max_over_time(<metric>[${__range_s}s]) != <state>)
```

**Special data sources**

Grafana also includes three special data sources: **Grafana**, **Mixed**, and **Dashboard**. For details, refer to Data sources

## Navigate the query tab
<a name="v9-panels-query-xform-navigate"></a>

A panel’s **Query** tab consists of the following elements:
+ **Data source selector** – Selects the data source to query.
+ **Query options:** – Sets maximum data retrieval parameters and query run time intervals.
+ **Query inspector button:** – Opens the query inspector panel, where you can view and optimize your query.
+ **Query editor list:** – Lists the queries you’ve written.
+ **Expressions:** – Uses the expression builder to create alert expressions. For more information about expressions, see [Write expression queries](v9-panels-query-xform-expressions.md).

## Add a query
<a name="v9-panels-query-xform-add"></a>

A query returns data that Grafana visualizes in dashboard panels. When you create a panel, Grafana automatically selects the default data source.

**To add a query**

1. Edit the panel to which you’re adding a query.

1. Choose the **Query** tab.

1. Choose the **Data source** dropdown menu and select a data source.

1. Choose **Query options** to configure the maximum number of data points you need. For more information about query options, see [Query options](#v9-panels-query-xform-options).

1. Write the query using the query editor.

1. Choose **Apply**.

Grafana queries the data source and visualizes the data.

## Manage queries
<a name="v9-panels-query-xform-manage"></a>

Grafana organizes queries in collapsible query rows. Each query row contains a query editor and is identified with a letter (A, B, C, and so on).

To manage your queries, you can copy queries, hide queries, remove a query, reorder queries, and toggle help for the query editor.

## Query options
<a name="v9-panels-query-xform-options"></a>

Choose **Query options** next to the data source selector to see settings for the selected data source. Changes you make here affect only queries made in this panel.

Grafana sets defaults that are shown in dark gray text. Changes are displayed in white text. To return a field to the default setting, delete the white text from the field.

Panel data source query options include:
+ **Max data points** – If the data source supports it, this sets the maximum number of data points for each series returned. If the query returns more data points than the max data points setting, then the data source reduces the number of points returned by aggregating them together by average, max, or another function.

  You can limit the number of points to improve query performance or smooth the visualized line. The default value is the width (or number of pixels) of the graph, because you can only visualize as many data points as the graph panel has room to display.
+ **Min interval** – Sets a minimum limit for the automatically calculated interval, which is typically the minimum scrape interval. If a data point is saved every 15 seconds, you don’t benefit from having an interval lower than that. You can also set this to a higher minimum than the scrape interval to retrieve queries that are more coarse-grained and well-functioning.
+ **Interval** – Sets a time span that you can use when aggregating or grouping data points by time.

  Grafana automatically calculates an appropriate interval that you can use as a variable in templated queries. The variable is measured in either seconds (`$__interval`) or milliseconds (`$__interval_ms`).

  Intervals are typically used in aggregation functions like sum or average. For example, this is a Prometheus query that uses the interval variable: `rate(http_requests_total[$__interval])`.

  This automatic interval is calculated based on the width of the graph. As the user zooms out on a visualization, the interval grows, resulting in a more coarse-grained aggregation. Likewise, if the user zooms in, the interval decreases, resulting in a more fine-grained aggregation.

  For more information, see [Global variables](v9-dash-variable-add.md#v9-dash-variable-add-global).
+ **Relative time** – Overrides the relative time range for individual panels, which causes them to be different than what is selected in the dashboard time picker in the top-right corner of the dashboard. You can use this to show metrics from different time periods or days on the same dashboard.
**Note**  
Panel time overrides have no effect when the dashboard’s time range is absolute.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-xform.html)
+ **Time shift** – Overrides the time range for individual panels by shifting its start and end relative to the time picker. For example, you can shift the time range for the panel to be two hours earlier than the dashboard time picker.
**Note**  
Panel time overrides have no effect when the dashboard's time range is absolute.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/grafana/latest/userguide/v9-panels-query-xform.html)
+ **Cache timeout** – *(Visible only if available in the data source)* Overrides the default cache timeout if your time series store has a query cache. Specify this value as a numeric value in seconds.