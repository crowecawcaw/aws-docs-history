

# Get ready
<a name="smart-crop-get-ready"></a>

## Pricing
<a name="smart-crop-pricing"></a>

There is a charge for running a channel that has the smart crop feature enabled. The charge is applied to each pipeline, which means that it applies once in single-pipeline channels and twice in standard channels. The charge isn't applied to each output in the channel, it is applied only to the pipelines.

To stop this charge, you must disable the feature [in all outputs in the channel](smart-crop-disable-console.md). For information about the current rates for using this feature, see [https://aws.amazon.com/elemental-inference/pricing/](https://aws.amazon.com/elemental-inference/pricing/).

## Source requirements
<a name="smart-crop-source-requirements"></a>
+ Input type: All supported types. The input must be live input, not a file input.
+ Input codec: All supported codecs 
+ Input resolution: All supported resolutions.
+ Aspect ratio: Any aspect ratio 
+ Dynamic image overlays: We recommend that the source doesn’t include image overlays because movement in the overlay might include movement that Elemental Inference will incorrectly start to track. 
+ Static image overlays and burned-in captions: We recommend that the source doesn’t include static image overlays or burned-in captions because the smart crop might cut them off awkwardly. 
+ Smart crop is supported in channels that implement input switching and/or input failover. 
+ Smart crop isn't supported in MediaLive Anywhere channels. 

## Output specifications
<a name="smart-crop-output-requirements"></a>
+ Output types: All supported types.
+ Output codec: All supported codecs.
+ Aspect ratio: Any aspect ratio, and any orientation (portrait or landscape).
+ Resolution: All supported resolutions.
+ Shared encodes: You might choose not to share encodes in a channel that you set up for smart crop because if you enable smart crop in one of the outputs that shares an encode, MediaLive automatically enables it in the other output that shares the encode. If you are setting up smart crop in an existing channel with shared encodes, see [Sharing a video encode](create-video-share.md) for information about how to uncouple the outputs.
+ You can't enable AFD in any video outputs where smart crop is enabled.
+ You can't insert dynamic image overlays in a channel where smart crop is enabled.