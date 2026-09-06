

# Components of a metric
<a name="eml-metrics-gen-info"></a>

AWS Elemental MediaLive collects data that is the basis for metrics. It collects these *datapoints* every second and sends them immediately to Amazon CloudWatch. You can use CloudWatch to generate *metrics* for these datapoints.

A metric is a collection of datapoints that has had an aggregation (a *statistic*) applied and that has a *period* and a *time range*. For example, you can request the Dropped frames metric as an average (the statistic) for a 1-minute period over 10 minutes (the time range). This result of this request is 10 metrics (because the range divided by the period is 10). 

## Statistics
<a name="eml-metrics-about-statistics"></a>

MediaLive supports all the statistics offered by CloudWatch. However, some statistics aren't useful for MediaLive metrics. In the description of metrics later in this chapter, we include the recommended statistics for each metric.

## Period
<a name="eml-metrics-about-period"></a>

All MediaLive metrics have a *high resolution period*, which means that the minimum period is 1 second.

## Time range
<a name="eml-metrics-about-time-range"></a>

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


Periods don't have a *minimum time range*. But there is a point where the statistic you apply becomes meaningless if you have a low period. For example, assume that you set the period to 1 second. This means that CloudWatch retrieves one datapoint. You can't obtain an average, a minimum or a maximum on one datapoint. However, this doesn't mean that the metric is meaningless. Instead, the metric is for the raw datapoint, with no statistic.

## Maximum storage time
<a name="eml-metrics-about-storage"></a>

Metrics are available for the last 15 months. Make sure that you specify a period that allows the time range that you want.

## Dimensions for MediaLive
<a name="eml-metrics-dimensions"></a>

Each MediaLive metric includes one or two specific sets of dimensions. MediaLive metrics include the following dimensions, from the dimension with the widest scope to the dimension with the narrowest scope.
+ ChannelID – Identifies a specific channel.
+ Pipeline – Identifies a specific pipeline. Standard channels have two pipelines (pipeline 0 or pipeline 1). Single-pipeline channels only have pipeline 0.
+ ActiveInputFailoverLabel – This dimension identifies the currently active input in a failover pair (part of the[ automatic input failover feature](automatic-input-failover.md)). Choose a dimension set that includes this dimension only if your channel implements automatic input failover.

  If you use this dimension, then the metric shows data only for the active input in the channel. If you don't use this dimension, the metric shows data for both inputs.
+ OutputGroupName – Identifies a specific output group.
+ AudioDescriptionName – Identifies a specific audio description (audio encode) among all the outputs of a channel.

## Definition of a running channel
<a name="eml-metrics-running-channel"></a>

Many metrics collect data only when a channel is running.

*Running *means that the channel has started. It could be both ingesting and producing output. Or it could be paused, meaning that it is still ingesting but not producing output.

Keep in mind that you can view or retrieve metrics when the channel isn't running. The only requirement is that the channel has run in the last 15 months.