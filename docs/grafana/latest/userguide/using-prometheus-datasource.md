# Using the Prometheus data

source

## Prometheus settings

| Name                      | Description                                                                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Name`                    | The data source name. This is how you see the data<br>source in panels and queries.                                                                                                                                |
| `Default`                 | Default data source means that it will be pre-selected<br>for new panels.                                                                                                                                          |
| `Url`                     | The URL of your Prometheus server; for<br>example, `https://prometheus.example.org:9090`.                                                                                                                          |
| `Access`                  | Server (default) = URL must be accessible from the<br>Grafana backend/server.                                                                                                                                      |
| `Basic Auth`              | Enable basic authentication to the Prometheus data<br>source.                                                                                                                                                      |
| `User`                    | User name for basic authentication.                                                                                                                                                                                |
| `Password`                | Password for basic authentication.                                                                                                                                                                                 |
| `Scrape interval`         | Set this to the typical scrape and evaluation interval<br>configured in Prometheus. Defaults to 15s.                                                                                                               |
| `Disable metrics lookup`  | Checking this option will disable the metrics chooser<br>and metric/label support in the query field’s autocomplete.<br>This helps if you have performance issues with bigger<br>Prometheus instances.             |
| `Custom Query Parameters` | Add custom parameters to the Prometheus query URL. For<br>example `timeout`, `partial_response`,<br>`dedup`, or<br>`max_source_resolution`. Multiple parameters<br>should be concatenated together with an<br>"&". |

## Prometheus query editor

The following sections provide information and options for Prometheus
query editor in the dashboard and in Explore.

### Query editor in

dashboards

Open a graph in edit mode by choosing the title and then choosing
**Edit** (or by pressing **e** key while pausing on the panel).

| Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Query expression`  | For more information about Prometheus query<br>expressions, see the [Prometheus documentation](https://prometheus.io/docs/querying/basics/ "https://prometheus.io/docs/querying/basics/").                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `Legend format`     | Controls the name of the time series, using name or<br>pattern. For example `{{hostname}}` is<br>replaced with the label value for the label<br>`hostname`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `Min step`          | An additional lower limit for the [`step` parameter of Prometheus range<br>queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries "https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries") and for the `$__interval`<br>and `$__rate_interval` variables. The limit<br>is absolute and not modified by the<br>\*Resolution<br>• setting.                                                                                                                                                                                                                        |
| `Resolution`        | `1/1` sets both the `$__interval`<br>variable and the [`step` parameter of Prometheus range<br>queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries "https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries") such that each pixel corresponds to<br>one data point. For better performance, use lower<br>resolutions. `1/2` only retrieves a data<br>point for every other pixel, and `1/10`<br>retrieves one data point per 10 pixels. Note that both<br>*Min time interval<br>• and<br>*Min step<br>• limit the final value<br>of `$__interval` and `step`. |
| `Metric lookup`     | Search for metric names in this input field.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `Format as`         | Switch between `Table`, `Time<br>series`, or `Heatmap`.<br>`Table` works only in the table panel.<br>`Heatmap` is suitable for displaying<br>metrics of the histogram type on a heatmap panel. It<br>converts cumulative histograms to regular ones and sorts<br>series by the bucket bound.                                                                                                                                                                                                                                                                                                                  |
| `Instant`           | Perform an "instant" query, to return<br>only the latest value that Prometheus has scraped for<br>the requested time series. Instant queries return<br>results much faster than normal range queries. Use them<br>to look up label sets.                                                                                                                                                                                                                                                                                                                                                                      |
| `Min time interval` | This value multiplied by the denominator from the<br>*Resolution<br>• setting sets a lower<br>limit to both the `$__interval` variable and<br>the [`step` parameter of Prometheus range<br>queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries "https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries"). Defaults to *Scrape<br>interval<br>• as set in the data source<br>options.                                                                                                                                                                          |

###### Note

Amazon Managed Grafana modifies the request dates for queries to align them
with the dynamically calculated step. This ensures consistent
display of metrics data, but it can result in a small gap of data at
the right edge of a graph.

#### Instant

queries in dashboards

The Prometheus data source allows you to run instant queries,
which query only the latest value. You can visualize the results in
a table panel to see all available labels of a time series.

Instant query results are made up of only one data point per
series. They can be shown in the graph panel with the help of series
overrides. To show them in the graph as a latest value point, add a
series override and select `Points > true`. To show a
horizontal line across the whole graph, add a series override and
select `Transform > constant` For more information
about series overrides, see [Series overrides](graph-panel.md#graph-panel-series-overrides "graph-panel.md#graph-panel-series-overrides").

### Query editor in

Explore

| Name               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Query expression` | For more information about Prometheus query<br>expression, see the [Prometheus documentation](https://prometheus.io/docs/querying/basics/ "https://prometheus.io/docs/querying/basics/").                                                                                                                                                                                                                                                                               |
| `Step`             | [`Step` parameter of Prometheus range<br>queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries "https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries"). Time units can be used here, for<br>example: 5s, 1m, 3h, 1d, 1y. Default unit if no unit<br>specified is `s` (seconds).                                                                                                                                         |
| `Query type`       | `Range`, `Instant`, or<br>`Both`. When running **Range query**, the result of<br>the query is displayed in graph and table. Instant query<br>returns only the latest value that Prometheus has<br>scraped for the requested time series and it is<br>displayed in the table. When \*_Both_<br>• is selected, both instant query and<br>range query is run. Result of range query is displayed<br>in graph and the result of instant query is displayed in<br>the table. |

## Metrics browser

The metrics browser allows you to quickly find metrics and select relevant
labels to build basic queries. When you open the browser you will see all
available metrics and labels. If supported by your Prometheus instance, each
metric will show its HELP and TYPE as a tooltip.

When you select a metric, the browser narrows down the available labels to
show only the ones applicable to the metric. You can then select one or more
labels for which the available label values are shown in lists in the bottom
section. Select one or more values for each label to tighten your query
scope.

###### Note

If you do not remember a metric name to start with, you can also
select a few labels first, to narrow down the list and then find
relevant label values.

All lists in the metrics browser have a search field above them to quickly
filter for metrics or labels that match a certain string. The values section
only has one search field. Its filtering applies to all labels to help you
find values across labels once they have been selected, for example, among
your labels app, job, job_name only one might with the value you are looking
for.

Once you are satisfied with your query, click “Use query” to run the
query. The **Use as rate query** button adds a
rate(...)[$\_\_interval] around your query to help write queries for counter
metrics. The “Validate selector” button will check with Prometheus how many
time series are available for that selector.

### Limitations

The metrics browser has a hard limit of 10,000 labels (keys) and
50,000 label values (including metric names). If your Prometheus
instance returns more results, the browser will continue functioning.
However, the result sets will be cut off above those maximum
limits.

## Templating

Instead of hardcoding things such as server, application and sensor name
in your metric queries, you can use variables in their place. Variables are
shown as dropdown select boxes at the top of the dashboard. You can use
these dropdown boxes to change the data being displayed in your dashboard.

For more information about templating and template variables, see [Templates and variables](templates-and-variables.md "templates-and-variables.md").

### Query variable

Variable of the type _Query_ allows you to query
Prometheus for a list of metrics, labels, or label values. The
Prometheus data source plugin provides the following functions you can
use in the **Query** input field.

| Name                          | Description                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| `label_names()`               | Returns a list of label names.                                             |
| `label_values(label)`         | Returns a list of label values for the<br>`label` in every metric.         |
| `label_values(metric, label)` | Returns a list of label values for the<br>`label` in the specified metric. |
| `metrics(metric)`             | Returns a list of metrics matching the specified<br>`metric` regex.        |
| `query_result(query)`         | Returns a list of Prometheus query result for the<br>`query`.              |

For information about what _metric names_,
_label names_ and _label
values_ are, see the [Prometheus documentation](https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels "https://prometheus.io/docs/concepts/data_model/#metric-names-and-labels").

#### Using

interval and range variables

###### Note

Support for `$__range`, `$__range_s`,
and `$__range_ms` are available only from Grafana
v5.3.

You can use some global variables in query variables:
`$__interval`, `$__interval_ms`,
`$__range`, `$__range_s`, and
`$__range_ms`. For more information, see [Global variables](variables-types.md#global-variables "variables-types.md#global-variables").
These can be convenient to use with the `query_result`
function when you must filter variable queries because the
`label_values` function doesn’t support queries.

To get the correct instances when changing the time range on the
dashboard, make sure to set the variable’s `refresh`
trigger to be `On Time Range Change`.

The following code example shows how to populate a variable with
the busiest five request instances based on average QPS over the
time range shown in the dashboard.

```

Query: query_result(topk(5, sum(rate(http_requests_total[$__range])) by (instance)))
Regex: /"([^"]+)"/

```

The following code example shows how to populate a variable with
the instances having a certain state over the time range shown in
the dashboard, using `$__range_s`.

```

Query: query_result(max_over_time(<metric>[${__range_s}s]) != <state>)
Regex:

```

### Using

`$__rate_interval` variable

The `$__rate_interval` variable is meant to be used in the
rate function. It is defined as max( `$__interval` +
_Scrape interval_, 4 \* _Scrape
interval_). _Scrape interval_ is the
Min step setting (AKA query_interval, a setting per PromQL query), if
any is set, and otherwise the _Scrape interval_ as
set in the Prometheus data source (but ignoring any Min interval setting
in the panel, because the latter is modified by the resolution setting).

### Using variables in

queries

There are two syntaxes:

- `$<varname>` Example:
  rate(http_requests_total{job=~"$job"}[5m])
- `[[varname]]` Example:
  rate(http_requests_total{job=~"[[job]]"}[5m])

Why two ways? The first syntax is easier to read and write but does
not allow you to use a variable in the middle of a word. When the
_Multi-value_ or _Include all
value_ options are enabled, Grafana converts the labels
from plaintext to a regex compatible string. Which means you have to use
`=~` instead of `=`.

## Annotations

You can use annotations to overlay rich event information on top of
graphs. You add annotation queries using the Dashboard menu or Annotations
view. For more information, see [Annotations](dashboard-annotations.md "dashboard-annotations.md").

Prometheus supports two ways to query annotations.

- A regular metric query
- A Prometheus query for pending and firing alerts. For more
  information, see [Inspecting alerts during runtime](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/#inspecting-alerts-during-runtime "https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/#inspecting-alerts-during-runtime")).

The step option is useful to limit the number of events returned from
your query.
