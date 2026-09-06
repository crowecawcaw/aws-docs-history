

# Components of a metric
<a name="inference-metrics-gen-info"></a>

AWS Elemental Inference collects data that is the basis for metrics. It collects these *datapoints* every second and sends them immediately to Amazon CloudWatch. You can use CloudWatch to generate *metrics* for these datapoints.

A metric is a collection of datapoints that has had an aggregation (a *statistic*) applied and that has a *period* and a *time range*. For example, you can request the Dropped frames metric as a sum (the statistic) for a 1-minute period over 10 minutes (the time range). This result of this request is 10 metrics (because the range divided by the period is 10). 

Elemental Inference supports all the statistics offered by CloudWatch. However, some statistics aren't useful for Elemental Inference metrics. In the description of metrics later in this chapter, we include the recommended statistics for each metric.

Each Elemental Inference metric includes one or two specific sets of dimensions.