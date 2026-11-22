

# Media delivery and creative cost

 FAST channels combine channel assembly from a VOD library with SSAI and SGAI monetization to stream continual linear content. Two cost areas dominate these workloads: delivering the content and serving the ad creative. On the delivery side, the largest saving comes from programmatic channel assembly rather than continual live encoding infrastructure, and VOD storage costs scale with how much of the library each channel actually serves. Balance these costs against ad revenue to maximize revenue per dollar of infrastructure spend. Creative serving has its own costs. Interactive, rich-media, and shoppable formats have larger payloads, render in more complex ways, and cost more to serve than standard display or video ads. When they are not designed with cost in mind, they erode the CPM premium they command. Pre-cache creative assets at the CDN edge and serve formats only to devices that can render them to avoid wasted serving costs. 


|  ADVCOST06: How do you optimize media delivery and creative costs for your FAST channel and rich-media advertising workloads?  | 
| --- | 
| [ADVCOST06-BP01 Use programmatic channel assembly to remove dedicated encoding infrastructure](advcost06-bp01.md) | 
| [ADVCOST06-BP02 Optimize VOD storage costs for FAST channel source content](advcost06-bp02.md) | 
| [ADVCOST06-BP03 Pre-cache creative assets at the CDN edge to avoid redundant origin fetches](advcost06-bp03.md) | 
| [ADVCOST06-BP04 Use device capability filtering to avoid wasted spend on unsupported formats](advcost06-bp04.md) | 

## Capability intent
<a name="advcost06-capability-intent"></a>
+  FAST channels use programmatic channel assembly from existing VOD assets instead of around-the-clock live encoding infrastructure, removing the largest infrastructure cost component. 
+  VOD storage costs are automatically optimized based on actual content access patterns using S3 Intelligent-Tiering. 
+  Rich-media creative assets are cached at CDN edge locations, avoiding redundant origin fetches. 
+  Innovative ad formats are served only to devices that can render them, with graceful fallback to standard formats for incompatible devices. 

## Common issues to watch for
<a name="advcost06-common-issues-to-watch-for"></a>
+  Running continual live encoding infrastructure for FAST channels assembled entirely from pre-encoded VOD assets. 
+  Storing all VOD renditions regardless of which ones FAST channels actually serve, paying for unused encoding outputs. 
+  Fetching rich-media creative assets from origin on every impression without CDN caching, paying redundant origin egress at scale. 
+  Serving innovative format instructions to devices that can't render them, wasting bandwidth and ad spend with zero viewer engagement. 