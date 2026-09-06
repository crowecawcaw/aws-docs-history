

# Pipeline locking metrics
<a name="eml-metrics-output-lock"></a>

Pipeline locking metrics relate to the synchronization of MediaLive pipelines.

**Topics**
+ [Pipelines locked](#eml-metrics-pipelines-locked)
+ [Input video aligned](#eml-metrics-input-video-aligned)

## Pipelines locked
<a name="eml-metrics-pipelines-locked"></a>

An indicator of whether the two pipelines are synchronized with each other. MediaLive uses [pipeline locking](pipeline-lock.md) to ensure that the two pipelines are synchronized with each other. 

The metric applies only to [output types that support pipeline locking](pipeline-lock.md). 

In addition, the metric applies only to the following channel configurations:
+ Standard channels that are configured for standard pipeline locking.
+ Standard channels and single-pipeline channels that are configured for epoch locking.
+ Single-pipeline channels using linked channels.



If the metric applies, then  a value of 1 means that all the eligible pairs of pipelines are synchronized. A value of 0 means that at least one pair of eligible pipelines is not synchronized.

**Note**  
This metric also applies when you have enabled [video aligned locking](pipeline-locking-verify-input.md#pipeline-locking-video-alignment-inputs). Video aligned locking is an advanced configuration option that uses visual signature comparison instead of embedded timecodes for synchronization. The PipelinesLocked metric reports the same synchronization status regardless of whether standard pipeline locking or video aligned locking is in use.

If the metric doesn't apply, the metric is always 0.

**Details:**
+ Name: PipelinesLocked
+ Units: Not applicable.
+ Meaning of zero: False (the eligible pipelines are not synchronized).
+ Meaning of no data points: The channel is not running. 
+ Supported dimension sets: ChannelId, Pipeline
+ Recommended statistic: Minimum (Value is 0).

## Input video aligned
<a name="eml-metrics-input-video-aligned"></a>

Indicates whether video aligned locking has successfully aligned the input video content between pipelines in the same pipeline locking pool.

In a video aligned locking pool, one pipeline serves as the reference and will always show a value of 1 for this metric. All other pipelines will only show 1 when they are successfully aligned with the reference pipeline.

Here are some guidelines on interpreting this metric:
+ A value of 1 means that pipeline is successfully aligned with the reference pipeline.

  If the metric shows a value of 0, this indicates that video alignment could not be established with the reference pipeline in the pipeline locking pool. This may be due to: 
  + Content mismatch between input sources
  + Input loss
  + Content that frequently loops
+ If the metric frequently transitions between 0 and 1, this suggests intermittent alignment issues that should be investigated.

**Details:**
+ Name: InputVideoAligned
+ Units: Not applicable.
+ Meaning of zero: False (Video alignment cannot be established or has been lost).
+ Meaning of no datapoints: Video aligned locking is not configured, or the pipeline has not processed any video frames since the channel started.
+ Supported dimension sets: ChannelId, Pipeline
+ Recommended statistic: Minimum