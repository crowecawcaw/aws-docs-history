

# ADVSUS03-BP04 Carry only the OpenRTB fields the bidding logic uses to reduce bytes on the wire
<a name="advsus03-bp04"></a>

 Excess payload adds network bandwidth and energy consumption at scale. Many requests exceed 2 kibibytes (KiB), especially rich video and connected-TV (CTV) bids. The objective is to carry only the fields the bidding logic uses and to reduce payload above the per-transaction allowance. 

 **Desired outcome:** 
+  Real-time bidding (RTB) payloads carry only the fields the bidding logic consumes, so average transaction size is minimized and payload above the 2 KiB no-charge allowance is reduced wherever the use case allows. 
+  Payload size is treated as a tracked sustainability indicator. 
+  Excess payload above the per-transaction no-charge allowance is minimized across partner links. Rich video and CTV payloads may legitimately exceed it. 
+  OpenRTB payloads exclude fields that are not used by bidding logic. 
+  Average payload size is monitored continuously as a sustainability metric. 
+  Reductions in data transfer produce measurable data-transfer-cost savings and a proxied reduction in transfer energy and emissions. 

 **Common anti-patterns:** 
+  Sending verbose OpenRTB payloads that include fields no downstream system reads. 
+  Using full text representations (for example, full country names) where compact codes would suffice. 
+  Treating payload size as a one-time tuning task rather than a continuously monitored metric. 
+  Optimizing transaction volume while ignoring the per-transaction data footprint. 

 **Benefits of establishing this best practice:** 
+  Lower network bandwidth consumption across high-volume RTB traffic, which reduces the energy associated with moving that data. 
+  Reduced data transfer cost that scales with transaction volume. 
+  Improved visibility into the sustainability impact of the bidding workload. 
+  Leaner payloads that can reduce processing overhead on both sides of the exchange. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 RTB Fabric carries a steady stream of small, repetitive requests between exchange and bidder. At high request volumes, transaction size drives the workload's data-transfer footprint. Every byte that crosses a partner link consumes network capacity and the energy to move it. The workload's transfer energy therefore tracks average payload multiplied by transaction volume. Video and connected-TV inventory has a higher baseline, because a CTV bid request carries more device and context signaling than a display request. This is why the size of each transaction is the variable that matters most for the sustainability of a bidding workload. 

 The 2 KiB no-charge allowance is a pricing construct rather than an energy threshold. AWS publishes no energy or carbon guidance for RTB Fabric, and its documented rationale for smaller transactions is cost and data-transfer efficiency. The resource-reduction case rests on the Well-Architected Sustainability Pillar's general principle of minimizing data transferred and stored, applied to this workload. RTB Fabric includes the first 2 KiB of each transaction at no charge and bills the excess per gibibyte. Above that threshold, cost and bytes transferred move together, so reducing spend also reduces transfer energy. Energy scales continuously with bytes on the wire, so a payload below 2 KiB still consumes transfer energy even where it incurs no excess-payload charge. 

 The reduction opportunity is in the OpenRTB message itself: fields accumulate over time, and some are never read by the bidding logic on either side of the exchange. Rich video and CTV payloads often exceed 2 KiB for legitimate reasons. Stripping fields that targeting or measurement depend on is a false economy: it can depress win rates or break downstream systems while saving negligible bandwidth. Carry only what the bidding logic consumes, using the most compact representation the schema allows. 

 Treat payload size as an ongoing sustainability signal, because schemas drift and new fields reintroduce weight. Bytes transferred is the practical proxy: a sustained fall in average payload stands in for the reduction in transfer energy and emissions. Read that figure against transaction volume to distinguish a real efficiency gain from a workload that has grown. \#\#\# Implementation steps 

1.  **Audit current payload sizes:** Measure average bid request and response sizes across all partner links to establish a baseline against the 2 KiB no-charge allowance. 

1.  **Identify trimmable fields:** Where average sizes exceed 2 KiB, review the OpenRTB schema in use and identify fields that can be trimmed or removed. 

1.  **Remove unused fields:** Remove fields that your bidding logic doesn't consume from outgoing and incoming payloads. 

1.  **Adopt compact representations:** Use compact encodings for data where possible, such as country codes instead of full country names. 

1.  **Monitor payload size as a KPI:** Track average payload size as a sustainability KPI alongside transaction volume so regressions are caught early. 

1.  **Track data-transfer reduction:** Track the reduction in bytes transferred attributable to payload optimization, and read it against transaction volume so growth isn't mistaken for regression. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP05 Minimize bid response payload sizes](advsus02-bp05.md) 
+  [ADVSUS02-BP06 Reduce per-auction network overhead by consolidating bid request fan-out and reusing transport connections](advsus02-bp06.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 

 **Related documents:** 
+  [AWS RTB Fabric pricing](https://aws.amazon.com/rtb-fabric/pricing/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 