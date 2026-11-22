

# ADVSUS02-BP05 Minimize bid response payload sizes

 Oversized bid responses increase network bandwidth demand and processing overhead. Reducing payload sizes lowers data transfer energy consumption and improves system-wide efficiency. 

 **Desired outcome:** 
+  Bid responses carry only the fields required for the transaction, encoded in an efficient serialization format, with creative assets referenced rather than embedded. 
+  Average payload size per supply-side platform (SSP) link is measured, trends downward over time, and the associated network energy savings are tracked. 
+  Bid responses exclude fields that the SSP doesn't consume. 
+  Responses use an efficient serialization format that carries only the required data. 
+  Creative assets are referenced by URL or ID rather than inlined into the response. 
+  Payload size per SSP link is continuously monitored and alarmed on regressions. 

 **Common anti-patterns:** 
+  Returning a fixed response schema that includes optional or rarely used fields on every bid. 
+  Embedding full creative assets inline instead of passing references. 
+  Using verbose text-based serialization without compression for high-volume bid traffic. 
+  Lacking visibility into payload size, so growth from new fields goes unnoticed. 

 **Benefits of establishing this best practice:** 
+  Lower network bandwidth demand and reduced data transfer energy consumption. 
+  Reduced serialization and processing overhead on both bidder and SSP sides. 
+  Lower bid latency, improving win rates without provisioning additional compute. 
+  Measurable sustainability signal that can be tracked and reported per SSP link. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Real-time bidding produces a steady, high-volume stream of bid responses, which expresses the cost of a payload as a rate. A field that adds only a few bytes is inconsequential in isolation. At auction volumes, it becomes a persistent tax on network transfer, serialization, and the compute that moves data through memory on both the bidder and the SSP. That transfer and processing work is the observable sustainability signal. 

 A bid response is a contract between the bidder and the SSP. Its efficient form carries only the data the counterparty acts on. Any additional field costs transfer and parsing time without downstream value. Creative assets deserve particular scrutiny, because they are large relative to bid metadata and reused across many auctions. Reference them by URL or ID so the SSP resolves them separately. This avoids retransmitting the same bytes on each bid, and shared caching and content delivery absorb the load. The cost is an added lookup and a dependency on the asset being available at serve time. 

 Serialization format and compression govern how compactly the remaining data travels. A dense binary encoding gives up the readability and loose interoperability of text formats, which can complicate debugging and partner onboarding. Compression trades bytes on the wire for CPU cycles on the sender that encodes and the receiver that decodes. For the small payloads typical of a single bid, the framing overhead can erode or even exceed the transfer savings. RTB runs under a strict latency budget. Any added encode or decode time competes with the win-rate benefit that a smaller response protects. The right balance depends on the payload size distribution and the CPU headroom on each side. 

 Payload composition isn't static. New targeting signals, experiments, and integration requirements steadily add fields. Without an owner for the response schema per supply-side link, that growth goes unnoticed until rising latency or transfer cost forces an investigation. Assign an owner for each link's response contract, accountable for what the link receives and for retiring fields no longer worth their transfer cost. Ongoing per-link visibility lets you trace drift to the change that caused it and defend the avoided-transfer benefit over time. 

 Field trimming and compact encoding are shared with the request side. Apply the mechanics defined in [ADVSUS03-BP04 Carry only the OpenRTB fields the bidding logic uses to reduce bytes on the wire](advsus03-bp04.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Remove unnecessary fields from bid responses:** Audit the response schema against what each SSP actually consumes and strip optional, redundant, or unused fields from the payload. 

1.  **Implement efficient data serialization formats:** Adopt a compact serialization format and apply compression appropriate to your bid traffic to minimize bytes transferred per response. 

1.  **Reference creative assets instead of embedding them:** Compress creative assets and pass them by reference (URL or ID) wherever possible rather than inlining the full asset into the response. 

1.  **Monitor average response payload size per SSP link:** Instrument payload size metrics per SSP link and alarm on regressions so size growth is detected early. 

1.  **Track network savings from payload optimization:** Track the reduction in bytes transferred per SSP link and report it as a sustainability metric alongside transaction volume, so a genuine efficiency gain is distinguishable from a workload that has grown. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS03-BP04 Carry only the OpenRTB fields the bidding logic uses to reduce bytes on the wire](advsus03-bp04.md) 
+  [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md) 
+  [ADVSUS02-BP06 Reduce per-auction network overhead by consolidating bid request fan-out and reusing transport connections](advsus02-bp06.md) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) (payload monitoring) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (payload size metrics) 