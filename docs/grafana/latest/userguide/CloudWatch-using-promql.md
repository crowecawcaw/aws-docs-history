

# Using the PromQL query option
<a name="CloudWatch-using-promql"></a>

**Note**  
The **PromQL** query type is only available with Grafana workspaces that are running Grafana version 13 and later.

The **PromQL** query type lets you query metrics that Amazon CloudWatch has ingested through its OpenTelemetry (OTLP) endpoint, using [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/). CloudWatch stores these OTLP-ingested metrics in a high-cardinality metrics store and exposes them through a Prometheus-compatible query API. This query type targets your OTLP-ingested metrics. It does not query standard CloudWatch metrics. For more information about availability and CloudWatch's PromQL implementation, see [Introducing OpenTelemetry PromQL support in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/introducing-opentelemetry-promql-support-in-amazon-cloudwatch/).

To use this query type, select **PromQL** from the query type drop-down in the upper middle of the query editor. No data source configuration changes are required. The plugin sends signed requests to the CloudWatch endpoint for the selected **Region**, so PromQL queries use the same authentication and Region settings as your other CloudWatch queries.

**Note**  
Querying with PromQL requires OTLP metrics ingestion and OTel enrichment to be enabled on your account. This feature must be available in the selected AWS Region.

The **PromQL** query type has two editing modes. Use the **Builder**/**Code** toggle in the query editor header to switch between them. Grafana keeps the query in sync when you switch modes. If a raw query written in **Code** mode can't be represented visually, Grafana prompts you before switching to **Builder** mode, because parts of the query might be lost.

You can augment PromQL queries with template variables. Grafana interpolates template variables in the expression before sending the query to CloudWatch. For more information, see [Variables](v13-dash-variables.md).

## Builder mode
<a name="CloudWatch-promql-builder-mode"></a>

**Builder** mode provides a visual interface for constructing a PromQL query without writing it by hand.

**To create a query in `Builder` mode**

1. Select a metric.

1. Add label filters to narrow the results. Choose a label key and value from the drop-downs.

1. (Optional) Chain operations, such as aggregations and functions, to transform the query.

Grafana constructs the PromQL expression from your selections. You can switch to **Code** mode at any time to view or refine the generated expression.

## Code mode
<a name="CloudWatch-promql-code-mode"></a>

**Code** mode provides a code editor for writing raw PromQL expressions. The editor includes autocomplete support:
+ **Metric name autocomplete** - As you type, the editor suggests CloudWatch metrics available in the current Region.
+ **Label key autocomplete** - Inside `{}`, the editor suggests the available label keys for the selected metric.
+ **Label value autocomplete** - After `key="`, the editor suggests values for that label.

Choose **Metrics browser** to open a visual browser that lists CloudWatch metrics for the current Region. Select a metric to list its labels, choose labels and values to build a selector, and then choose **Use query** to write the selector into the editor.

Enable the **Explain** toggle in the query editor header to display a human-readable, step-by-step explanation of the current PromQL expression.

## PromQL query options
<a name="CloudWatch-promql-query-options"></a>

The following options are available for PromQL queries in both **Builder** and **Code** modes.


|  Option  |  Description  | 
| --- | --- | 
|  Legend  |  Controls the time series name. Auto shows only the labels that distinguish each series. Verbose shows the full set of labels. Custom lets you provide a template using label names, such as {{InstanceId}}.  | 
|  Min step  |  The lower bound on the interval between data points. For example, set 1m to lock data points to one-minute boundaries. Supports duration strings such as 15s, 1m, and 1h.  | 
|  Format  |  The format of the returned data. Choose Time series to render a graph, or Table to render tabular data.  | 
|  Type  |  The query type. Choose Range to return data over the selected time range, or Instant to return a single value at the end of the time range.  | 