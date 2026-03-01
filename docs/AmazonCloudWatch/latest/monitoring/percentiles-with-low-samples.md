# Percentile-based alarms and low data samples

When you set a percentile as the statistic for an alarm, you can specify what to do when
there is not enough data for a good statistical assessment. You can choose to have the alarm
evaluate the statistic anyway and possibly change the alarm state. Or, you can have the alarm
ignore the metric while the sample size is low, and wait to evaluate it until there is enough
data to be statistically significant.

For percentiles between 0.5 (inclusive) and 1.00 (exclusive), this setting is used when
there are fewer than 10/(1-percentile) data points during the evaluation period. For example,
this setting would be used if there were fewer than 1000 samples for an alarm on a p99
percentile. For percentiles between 0 and 0.5 (exclusive), the setting is used when there are
fewer than 10/percentile data points.
