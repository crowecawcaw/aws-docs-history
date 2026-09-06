

# Definition of a metric for MediaConnect datapoints
<a name="monitor-with-cloudwatch-metric-info"></a>

AWS Elemental MediaConnect collects data that is the basis for metrics. It collects these *datapoints* every second and sends them immediately to Amazon CloudWatch. You can use CloudWatch to generate *metrics* for these datapoints.

A metric is a collection of datapoints that has had an aggregation (a *statistic*) applied and that has a *period* and a *time range*. For example, you can request the Dropped packets metric as an average (the statistic) for a 1 minute period over 10 minutes (the time range). This result of this request is 10 metrics (because the range divided by the period is 10). 

## Period
<a name="emx-metrics-about-period"></a>

Most MediaConnect metrics have a *high resolution period*, which means that the minimum period is one second. MediaConnect Gateway metrics are the only metrics not available in a high resolution period. 

## Time range
<a name="emx-metrics-about-time-range"></a>

Each period has a *maximum time range*. For example, if you specify 1 day as the time range, you won't be able to retrieve metrics with a 10 second period.


<table>
<thead>
  <tr><th>Period</th><th>Maximum time range</th></tr>
</thead>
<tbody>
  <tr><td>1 second</td><td rowspan="4">The last 3 hours</td></tr>
  <tr><td>5 seconds</td></tr>
  <tr><td>10 seconds</td></tr>
  <tr><td>30 seconds</td></tr>
  <tr><td>60 seconds</td><td>The last 360 hours (15 days)</td></tr>
  <tr><td>300 seconds (5 minutes)</td><td rowspan="2">The last 1512 hours (63 days)</td></tr>
  <tr><td>900 seconds (15 minutes)</td></tr>
  <tr><td>3600 seconds (1 hour) or longer</td><td>The last 455 days (15 months)</td></tr>
</tbody>
</table>


Periods don't have a *minimum time range*. But there is a point where the statistic you apply becomes meaningless if you have a low period. For example, assume that you set the period to one second. This means that CloudWatch retrieves one datapoint. You can't obtain an average, a minimum or a maximum on one datapoint. However, this doesn't mean that the metric is meaningless. Instead, the metric is for the raw datapoint, with no statistic.

## Maximum storage time
<a name="emx-metrics-about-storage"></a>

Metrics are available for the last 15 months. Make sure that you specify a period that allows the time range that you want.