

# Encoding and adaptive bit rate
<a name="smperf05"></a>

Encoding settings and the ABR ladder determine the balance between quality, bandwidth, and device compatibility. These decisions affect both viewer experience and delivery cost at scale.


| SMPERF05: What tradeoffs have you made in media processing to improve client experience and lower bandwidth costs? | 
| --- | 
| [SMPERF05-BP01 Optimize the number of adaptive bit rate renditions for your workload](smperf05-bp01.md) | 
| [SMPERF05-BP02 Select appropriate encoding settings for your content type and quality targets](smperf05-bp02.md) | 

## Capability intent
<a name="smperf05-intent"></a>
+ The ABR ladder is sized to the actual device and network distribution of the audience.
+ Renditions are spaced appropriately (1.5-2x between rungs) to avoid switching oscillation.
+ Encoding settings are chosen per content type and validated with objective quality metrics.
+ The ladder is reviewed regularly as audience devices and codecs evolve.

## Common issues to watch for
<a name="smperf05-issues"></a>
+ Copying a default ladder without validating it against the actual audience.
+ Too many renditions causing switching oscillation.
+ Uniform encoding presets across all content regardless of complexity.
+ Measuring only bit rate without objective quality metrics (VMAF, PSNR).