

# Get Ready
<a name="event-clip-getready"></a>

## Pricing
<a name="event-clip-pricing"></a>

There is a charge for running a channel that has the event clipping feature enabled. The charge is applied to each pipeline, which means that it applies once in single-pipeline channels and twice in standard channels. The charge isn't applied to each output in the channel, it is applied only to the pipelines.

To stop this charge, you must [disable the feature](event-clip-disable.md). For information about the current rates for using this feature, see [https://aws.amazon.com/elemental-inference/pricing/](https://aws.amazon.com/elemental-inference/pricing/).

## Source requirements
<a name="event-clip-source-requirements"></a>
+ Input type: All supported types. The *input* must be live input, not a file input.
+ Input codec: All supported codecs 
+ Input resolution: All supported resolutions.
+ Aspect ratio: Any aspect ratio 
+ Static image overlays and burned-in captions: We recommend that the source doesn’t include static image overlays or burned-in captions because the event clipping might cut them off awkwardly. 
+ Event clipping is supported in channels that implement input switching and/or input failover. 
+ Event clipping isn't supported in MediaLive Anywhere channels. 