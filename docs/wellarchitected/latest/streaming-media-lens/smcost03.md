

# Encoding and quality optimization
<a name="smcost03"></a>

Encoding decisions directly determine delivery cost. Lower bit rate at equivalent quality means fewer bytes to store and transfer. Content-aware encoding matches spend to complexity rather than applying uniform high bitrates.


| SMCOST03: How do you optimize distribution costs while maintaining video quality? | 
| --- | 
| [SMCOST03-BP01 Implement thorough video quality assessment](smcost03-bp01.md) | 
| [SMCOST03-BP02 Optimize encoder settings based on content type](smcost03-bp02.md) | 

## Capability intent
<a name="smcost03-intent"></a>
+ Quality is measured objectively (VMAF, PSNR) alongside cost so that encoding changes can be evaluated.
+ Encoder settings vary by content type and viewing context rather than applied uniformly.
+ Variable bit rate modes spend bits where complexity demands them and save where it doesn't.

## Common issues to watch for
<a name="smcost03-issues"></a>
+ Fixed high bit rate without measuring whether the quality justifies the cost.
+ Identical encoding settings for all content regardless of complexity (static compared to fast motion).
+ CBR used everywhere instead of variable bit rate modes that reduce average bandwidth.
+ Encoding changes made without measuring the impact on both quality and cost.