

# ADVCOST06-BP04 Use device capability filtering to avoid wasted spend on unsupported formats
<a name="advcost06-bp04"></a>

 Sending rich-media creatives to devices that can't render them wastes bandwidth, compute, and ad spend with zero viewer engagement. Capability detection and graceful fallback runs every impression with the best format the device can render. 

 **Desired outcome:** 
+  Rich-media ad formats are served only to devices capable of rendering them, with automatic fallback to standard formats for incompatible devices. 
+  Every ad slot is monetized. Incompatible device impressions receive standard video or display fallback, not blank slots. 

 **Common anti-patterns:** 
+  Serving interactive overlays, shoppable ads, or 360 video creatives to all devices without checking capability signals. 
+  Omitting device capability signals (interactive support, MRAID version, and rendering engine) from OpenRTB bid requests. 
+  Failing to implement graceful degradation for incompatible devices. 
+  Detecting format incompatibility only at the player level, after the creative has already been fetched, transcoded, and delivered. 
+  Never tracking creative rendering success rates by device type and format combination. 

 **Benefits of establishing this best practice:** 
+  Reduce wasted bandwidth and compute on unsupported format deliveries 
+  Improve measured engagement rates by serving only to capable devices 
+  Graceful degradation maintains monetization on incompatible devices 
+  Network-layer filtering limits waste before it reaches application compute 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Rich-media creatives require specific rendering capabilities that vary across device populations. Interactive overlays need JavaScript execution or MRAID support. Shoppable ads require click-through handling and overlay rendering. 360-degree video needs gyroscope APIs or WebGL. Legacy CTV devices, older set-top boxes, and basic mobile players often lack one or more of these capabilities. When you send a creative to a device that can't render it, you waste bandwidth, ad-selection compute, transcoding, and CDN delivery costs, and the impression produces no viewer engagement and no measurable campaign performance. 

 Device capability detection happens through signals in the OpenRTB bid request. Fields like device.js (JavaScript support), MRAID version, rendering engine, and interactive support flags tell DSPs what the device can handle. When these signals are missing or inaccurate, DSPs can't decide on the right format and return creative that fails to render on the device. 

 Graceful degradation preserves monetization on incompatible devices. The system substitutes a standard video or display creative that the device can render. Every impression stays monetized at some value. The fallback creative commands a lower CPM than the premium innovative format, but lower CPM is an improvement over zero CPM from a blank slot. 

 Filter as early in the delivery chain as possible. Player-level detection catches incompatibility only after the creative has been fetched, transcoded, and delivered through the CDN, wasting the full delivery cost. Network-layer filtering on device attributes (using [RTB Fabric](https://aws.amazon.com/rtb-fabric/) attribute modules or equivalent) tags or drops requests before they reach application compute. 

 Track creative rendering success rates by device type and format combination to refine capability rules. Without this data, wasted impressions go undetected. A high fallback activation rate for a device-format pair might mean capability signals are inaccurate for that device population. Correct the signal at the SSP level, or add that device to the exclusion list. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Audit OpenRTB bid request fields for capability signals:** Verify that device capability signals (device.js, MRAID version, rendering engine, interactive support) are populated for all supply paths. Work with SSP partners to add missing capability signals. 

1.  **Implement creative format selection based on device capability tiers:** Configure ad decisioning logic that maps device capability tiers to eligible creative formats. Serve innovative formats to capable devices, and serve standard formats to all others. This helps avoid wasted delivery of unsupported format instructions. 

1.  **Build capability success rate dashboards:** Track creative rendering success rates segmented by device type and format combination. Identify device-format pairs with high failure rates for exclusion or fallback configuration. 

1.  **Configure graceful degradation rules:** When a device is flagged as incompatible with a selected rich-media creative, automatically substitute a pre-transcoded standard video fallback. Measure the fallback activation rate. A high rate may indicate device capability signals are inaccurate. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST06-BP03 Pre-cache creative assets at the CDN edge to avoid redundant origin fetches](advcost06-bp03.md) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 