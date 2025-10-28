# Pipeline locking

metrics

Pipeline locking metrics relate to the synchronization of MediaLive
pipelines.

###### Topics

- [Pipelines locked](#eml-metrics-pipelines-locked "#eml-metrics-pipelines-locked")

## Pipelines locked

An indicator of whether the two pipelines are
synchronized with each other.
MediaLive uses [pipeline locking](pipeline-lock.md "pipeline-lock.md") to ensure that the two pipelines
are synchronized with each other.

The metric applies only to [output types that support
pipeline locking](pipeline-lock.md "pipeline-lock.md").

In addition, the metric applies only to the following channel
configurations:

- Standard channels that are configured for standard pipeline
  locking.
- Standard channels and single-pipeline channels that are configured for
  epoch locking.

If the metric
applies, then

a value of 1 means that all the eligible pairs of pipelines are synchronized. A
value of 0 means that at least one pair of eligible pipelines is not
synchronized.

If
the metric doesn't apply, the metric is always 0.

**Details:**

- Name: PipelinesLocked
- Units: Not applicable.
- Meaning of zero: False (the eligible pipelines are not
  synchronized).
- Meaning of no data points: The channel is not running.
- Supported dimension sets: ChannelId, Pipeline
- Recommended statistic: Minimum (Value is 0).
