

# ADVCOST03-BP07 Optimize bid request and response payload sizes to reduce data transfer costs

 Each RTB transaction includes 2 KiB (2,048 bytes) of data at no charge. Excess payload charges apply only for bytes above this threshold and can be significant at scale. Keeping payloads under 2 KiB avoids excess data transfer charges entirely. 

 **Desired outcome:** 
+  Average bid request and response sizes stay within or near the 2 KiB no-charge data threshold per transaction. 
+  OpenRTB fields unused by your bidding logic are removed from requests to reduce payload sizes. 
+  Payload compression (gzip or Brotli) is enabled where both parties support it. 

 **Common anti-patterns:** 
+  Accepting default OpenRTB bid request payloads from partners without negotiating field removal, which brings in dozens of unused fields per request that push payload sizes above the no-charge threshold and trigger excess charges on every transaction. 
+  Never measuring average payload sizes across partner links, so excess data charges accumulate at scale until they appear as unexplained cost increases in monthly billing. 
+  Sending full bid responses with optional fields that the receiving party doesn't consume, which inflates response sizes above the no-charge threshold unnecessarily. 
+  Neglecting to enable payload compression (gzip or Brotli) when both parties support it, so a 60-80% size reduction that could bring payloads within the no-charge allowance is left on the table. 
+  Optimizing payload size once and never revisiting as new OpenRTB fields are added by partners over time. 

 **Benefits of establishing this best practice:** 
+  Avoid excess data transfer charges on billions of monthly transactions. 
+  Reduced serialization and deserialization overhead improves auction latency. 
+  Smaller payloads reduce compute time for bid evaluation. 
+  Compression (60-80% size reduction) further decreases transfer costs. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 [RTB Fabric pricing](https://aws.amazon.com/rtb-fabric/pricing/) includes 2 KiB (2,048 bytes) of data per transaction at no extra charge. Bytes above this threshold incur excess data transfer fees on every transaction. At billions of monthly transactions, even a few hundred excess bytes per request compounds into significant cost. Any request or response that stays within the 2 KiB threshold costs nothing beyond the rate for each transaction. 

 OpenRTB bid requests contain dozens of fields defined by the IAB specification, but most bidders evaluate only a subset during decisioning. Fields like extended user segments, full device fingerprints, or multi-level content categorization arrays add hundreds of bytes per request without contributing to bid logic. Partners must agree to field removal bilaterally because the sender controls which fields go in the request template. 

 Payload compression (gzip or Brotli) reduces OpenRTB JSON size by 60 to 80% without requiring field removal. Compression adds CPU overhead on both ends for encoding and decoding, and at high QPS that cost is measurable. Both parties must support the same algorithm. Some legacy partners lack compression support entirely, so field removal is the only option for those links. 

 Payload sizes vary widely by partner, so measure each link separately. One SSP might send lean 1.5 KiB requests while another sends 4 KiB requests packed with video-specific fields. Link-level [CloudWatch](https://aws.amazon.com/cloudwatch/) metrics for average request and response size identify the partners to optimize first. 

 Payload sizes drift upward over time as partners add new OpenRTB fields to their request templates. A link optimized to stay under 2 KiB today might exceed the threshold in six months when a partner adds supply chain transparency fields or seller-defined audience attributes. Without ongoing monitoring, excess charges accumulate unnoticed until they appear as unexplained increases in monthly billing. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Enable RTB Fabric link-level metrics for payload size monitoring:** Monitor average request and response payload sizes per partner link. Identify links where average size exceeds 2 KiB. Alert when average size exceeds 80% of the 2 KiB no-charge threshold. 

1.  **Audit OpenRTB bid request fields:** Review all fields in outgoing bid requests against your bidding logic. Remove fields your bidder never evaluates. Work with SSP partners to remove fields from their bid request templates that you've confirmed are unused. 

1.  **Enable payload compression where supported:** Enable gzip or Brotli compression on RTB Fabric links where both parties support it. Test compression effectiveness: OpenRTB JSON typically compresses 60-80%, potentially bringing payloads below the 2 KiB threshold even if above it. 

1.  **Monitor and optimize payload sizes monthly:** Track average payload size per link as a monthly KPI. Set improvement targets. Review with partners when payloads consistently exceed thresholds. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP05 Replace per-gigabyte egress with transaction-priced partner connectivity](advcost03-bp05.md) 

 **Related documents:** 
+  [AWS RTB Fabric Pricing](https://aws.amazon.com/rtb-fabric/pricing/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 