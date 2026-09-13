

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

## Maturity levels
<a name="smcost03-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | A single bit rate ladder and CBR profile are applied to all content. No objective quality measurement exists. | 
| 2 | Emerging | VMAF or PSNR scores are collected for some content but don't influence encoding decisions. VBR is used selectively. | 
| 3 | Defined | Encoding profiles are differentiated by content type. Quality metrics are measured alongside cost for every encoding change. | 
| 4 | Proactive | Content-aware encoding adjusts settings per title or scene complexity. VBR is the default, with bit rate caps informed by quality targets. | 
| 5 | Optimized | Per-title or per-shot encoding runs automatically, continuously tuning bit rate ladders against quality thresholds and delivery cost data. | 

## Common issues to watch for
<a name="smcost03-issues"></a>
+ Fixed high bit rate without measuring whether the quality justifies the cost.
+ Identical encoding settings for all content regardless of complexity (static compared to fast motion).
+ CBR used everywhere instead of variable bit rate modes that reduce average bandwidth.
+ Encoding changes made without measuring the impact on both quality and cost.