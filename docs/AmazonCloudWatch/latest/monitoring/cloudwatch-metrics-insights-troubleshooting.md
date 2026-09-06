

# Troubleshooting Metrics Insights
<a name="cloudwatch-metrics-insights-troubleshooting"></a>

## The results include "Other," but I don't have this as a dimension
<a name="cloudwatch-metrics-insights-troubleshooting-other"></a>

This means that the query includes a **GROUP BY** clause that specifies a label key that is not used in some of the metrics that are returned by the query. In this case, a null group named `Other` is returned. The metrics that do not include that label key are probably aggregated metrics that return values aggregated across all values of that label key.

 For example, suppose you have the following query:

```
SELECT AVG(Faults) 
FROM MyCustomNamespace 
GROUP BY Operation, ServiceName
```

If some of the returned metrics don't include `ServiceName` as a dimension, then those metrics are displayed as having `Other` as the value for `ServiceName`.

To prevent seeing "Other" in your results, use **SCHEMA** in your **FROM** clause, as in the following example:

```
SELECT AVG(Faults) 
FROM SCHEMA(MyCustomNamespace, Operation)
GROUP BY Operation, ServiceName
```

This limits the returned results to only the metrics that have both the `Operation` and `ServiceName` dimensions.

## The oldest timestamp in my graph has a lower metric value than the others
<a name="cloudwatch-metrics-insights-troubleshooting-oldest"></a>

CloudWatch Metrics Insights supports up to two weeks of historical data. When you graph with a period larger than one minute, there could be cases where the oldest data point differs from the expected value. This is because the CloudWatch Metrics Insights queries return only data within the two-week retention period. In this case, the oldest data point in the query returns only the observations that have been measured within the two-week boundary, instead of returning all the observations within the period of that data point.

## Inconsistent metric values across different time periods when using tag-based queries
<a name="cloudwatch-metrics-insights-troubleshooting-tag-mutations"></a>

When you use `WHERE` or `GROUP BY` clauses with tags in CloudWatch Metrics Insights queries, you might see different metric values depending on the selected time period. For example, a 6-hour period might show a peak value of 20, while a 1-hour period shows only 2 for the same time window.

This occurs because tag timestamps are stored with second-level resolution, while metric data points are aligned to period boundaries (for example, the start of each minute or hour). To determine which data points match a tag time range, CloudWatch adjusts the start of the range by subtracting one period. With larger periods, this adjustment creates a wider gap between the tag timestamp and the earliest included data point, which can cause data points near the start of the range to be excluded.

The following example shows how this affects query results. A metric has two tag values: `env=beta` (from 00:00 to 01:30) and `env=gamma` (from 01:30 to 03:00). Each tag covers 90 minutes of data with a SUM of 270.

![Two CloudWatch metric graphs comparing tag-based query results with 1-minute and 3-hour periods.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/metrics-insights-tag-alignment.png)



<table>
<thead>
  <tr><th colspan="4"><b>env=beta with 1-minute period</b></th></tr>
  <tr><th>Statistic</th><th>Expected</th><th>Returned</th><th>Difference</th></tr>
</thead>
<tbody>
  <tr><td>SUM</td><td>270</td><td>271</td><td>+1</td></tr>
  <tr><td>AVG</td><td>3.0</td><td>3.0</td><td>0</td></tr>
  <tr><td>MIN</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>MAX</td><td>5</td><td>5</td><td>0</td></tr>
  <tr><td>SAMPLE_COUNT</td><td>90</td><td>91</td><td>+1</td></tr>
</tbody>
</table>



<table>
<thead>
  <tr><th colspan="4"><b>env=gamma with 1-minute period</b></th></tr>
  <tr><th>Statistic</th><th>Expected</th><th>Returned</th><th>Difference</th></tr>
</thead>
<tbody>
  <tr><td>SUM</td><td>270</td><td>275</td><td>+5</td></tr>
  <tr><td>AVG</td><td>3.0</td><td>3.0</td><td>0</td></tr>
  <tr><td>MIN</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>MAX</td><td>5</td><td>5</td><td>0</td></tr>
  <tr><td>SAMPLE_COUNT</td><td>90</td><td>91</td><td>+1</td></tr>
</tbody>
</table>


With a 1-minute period, the alignment adjustment is small (1 minute), so only 1 extra data point is included per tag. With a 3-hour period, the adjustment spans the entire query range:


<table>
<thead>
  <tr><th colspan="4"><b>env=beta with 3-hour period</b></th></tr>
  <tr><th>Statistic</th><th>Expected</th><th>Returned</th><th>Difference</th></tr>
</thead>
<tbody>
  <tr><td>SUM</td><td>270</td><td>540</td><td>+270</td></tr>
  <tr><td>AVG</td><td>3.0</td><td>3.0</td><td>0</td></tr>
  <tr><td>MIN</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>MAX</td><td>5</td><td>5</td><td>0</td></tr>
  <tr><td>SAMPLE_COUNT</td><td>90</td><td>180</td><td>+90</td></tr>
</tbody>
</table>



<table>
<thead>
  <tr><th colspan="4"><b>env=gamma with 3-hour period</b></th></tr>
  <tr><th>Statistic</th><th>Expected</th><th>Returned</th><th>Difference</th></tr>
</thead>
<tbody>
  <tr><td>SUM</td><td>270</td><td>540</td><td>+270</td></tr>
  <tr><td>AVG</td><td>3.0</td><td>3.0</td><td>0</td></tr>
  <tr><td>MIN</td><td>1</td><td>1</td><td>0</td></tr>
  <tr><td>MAX</td><td>5</td><td>5</td><td>0</td></tr>
  <tr><td>SAMPLE_COUNT</td><td>90</td><td>180</td><td>+90</td></tr>
</tbody>
</table>


With the 3-hour period, both tags return the entire dataset (SUM=540, SAMPLE\_COUNT=180) because the single aggregated data point's timestamp falls within both adjusted ranges. The tag boundary is effectively erased.

To reduce the impact of this behaviour, try the following approaches:
+ **Use smaller aggregation periods.** Smaller periods (such as 1 minute or 5 minutes) more closely match the second-level resolution of tag timestamps, which minimizes the alignment gap and makes it more likely that all relevant data points are included.
+ **Use dimension-based filtering instead of tags.** If your use case allows it, filter by dimensions rather than tags. Dimension-based queries are not affected by this behaviour. For example, use `WHERE InstanceId = 'i-1234567890abcdef0'` instead of `WHERE tag."my-tag" = 'my-value'`.
+ **Query at a consistent granularity.** When comparing metric data across different time windows, use the same period to avoid unexpected differences caused by the alignment adjustment.