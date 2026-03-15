# Retrieving time-series metrics for Performance Insights

The `GetResourceMetrics` operation retrieves one or more time-series metrics from the Performance Insights
data. `GetResourceMetrics` requires a metric and time period, and returns a response with a
list of data points.

For example, the AWS Management Console uses `GetResourceMetrics` to populate the **Counter
Metrics** chart and the **Database Load** chart, as seen in the following
image.

![Counter Metrics and Database Load charts](images/perf-insights-api-charts.png)
All metrics returned by `GetResourceMetrics` are standard time-series metrics, with the exception of
`db.load`. This metric is displayed in the **Database Load** chart. The
`db.load` metric is different from the other time-series metrics because you can break it into
subcomponents called _dimensions_. In the previous image, `db.load` is broken down
and grouped by the waits states that make up the `db.load`.

###### Note

`GetResourceMetrics` can also return the `db.sampleload` metric, but the
`db.load` metric is appropriate in most cases.

For information about the counter metrics returned by `GetResourceMetrics`, see [Performance Insights counter metrics](USER_PerfInsights_Counters.md "USER_PerfInsights_Counters.md").

The following calculations are supported for the metrics:

- Average – The average value for the metric over a period of time. Append `.avg` to
  the metric name.
- Minimum – The minimum value for the metric over a period of time. Append `.min` to
  the metric name.
- Maximum – The maximum value for the metric over a period of time. Append `.max` to
  the metric name.
- Sum – The sum of the metric values over a period of time. Append `.sum` to the metric
  name.
- Sample count – The number of times the metric was collected over a period of time. Append
  `.sample_count` to the metric name.
  For example, assume that a metric is collected for 300 seconds (5 minutes), and that the metric is collected
  one time each minute. The values for each minute are 1, 2, 3, 4, and 5. In this case, the following calculations
  are returned:

- Average – 3
- Minimum – 1
- Maximum – 5
- Sum – 15
- Sample count – 5
  For information about using the `get-resource-metrics` AWS CLI command, see [`get-resource-metrics`](../../../cli/latest/reference/pi/get-resource-metrics.md "../../../cli/latest/reference/pi/get-resource-metrics.md").

For the `--metric-queries` option, specify one or more queries that you want to get results for.
Each query consists of a mandatory `Metric` and optional `GroupBy` and `Filter`
parameters. The following is an example of a `--metric-queries` option specification.

```
{
   "Metric": "string",
   "GroupBy": {
     "Group": "string",
     "Dimensions": ["string", ...],
     "Limit": integer
   },
   "Filter": {"string": "string"
     ...}
```
