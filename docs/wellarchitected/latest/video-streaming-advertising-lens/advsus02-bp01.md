

# ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy
<a name="advsus02-bp01"></a>

 Invalid or incompatible requests waste energy when they reach application compute. You can reduce that waste by rejecting them at the network layer, upstream of compute, which also improves response times. 

 **Desired outcome:** 
+  Malformed, unsupported, or economically incompatible bid requests are rejected before they consume bidder compute, at the cheapest tier that can make each decision. 
+  The proportion of inbound traffic discarded by filters, and the reasons for rejection, are observable and trend toward fewer wasted invocations over time. 
+  Filter rules evolve from real no-bid analysis so the workload spends energy only on requests it can act on. 

 **Common anti-patterns:** 
+  Accepting every inbound bid request into application compute and deciding to no-bid only after deserialization and business-logic evaluation. 
+  Hard-coding filter rules once and never revisiting them as traffic patterns, partners, and floor prices change. 
+  Treating rejected-request volume as an operational afterthought with no visibility into how much traffic is filtered or why. 
+  Filtering only on coarse signals (such as source IP) while letting structurally invalid OpenRTB payloads reach the bidder. 

 **Benefits of establishing this best practice:** 
+  Compute and the energy it draws are reserved for requests the workload can actually bid on, lowering the carbon intensity of each useful response. 
+  Removing doomed requests early reduces queueing and contention, improving latency for legitimate traffic. 
+  Rejection metrics expose partner and inventory quality problems sooner, enabling targeted remediation. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In a real-time bidding workload, a large share of inbound requests are never winnable: they are malformed, use unsupported protocol versions, omit required fields, or sit below the bidder's floor price. When these requests reach application compute, the workload still pays the full cost of connection handling, deserialization, and business-logic evaluation before it can decide to no-bid. That work consumes CPU cycles and the energy behind them with no useful output, because the request was going to be rejected regardless. 

 Pushing rejection earlier changes where that decision is made, and how cheaply it can be made. A check expressible as an attribute value match, such as a country, a device type, or a regulatory flag, can run in the connectivity layer. AWS RTB Fabric's OpenRTB Attribute Module matches JSON paths against value sets and returns a no-bid without the request reaching the bidder. A check that requires parsing and validating the bid request payload itself, such as rejecting malformed JSON, enforcing required fields, checking a protocol version, or comparing a numeric floor price, isn't attribute matching and no built-in module performs it. That work needs a lightweight validation tier in front of the bidder, or the bidder's own entry point, kept cheap so a rejected request never reaches full business-logic evaluation. This also reduces queueing and resource contention on the bidder fleet, which improves response times for the legitimate requests that remain. Requirements, supported protocols, partner behavior, and floor prices all change, so a rule set that is accurate today gradually admits more waste. 

 Rules that are set once and never revisited drift away from current traffic, and without visibility into how much traffic is rejected and why, that drift first shows up as inflated compute cost. To keep the energy savings durable, measure filter effectiveness and refine the rules using your bidder's no-bid analysis. Filters that are too aggressive can discard winnable requests, so validate changes against no-bid data before tightening them. 

 The defensible evidence is the compute and network the rejected requests would have consumed, read from utilization and filtered-request volume. 

 This best practice's scope covers rejecting requests whose rejection is deterministic (structurally invalid, malformed, protocol-unsupported, missing required fields, or below the floor price). Shedding valid requests that are merely unlikely to win, based on attributes such as geo, device type, COPPA flags, or domain, belongs to [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md). Per-partner rate limiting belongs to [ADVSUS02-BP02 Apply rate limiting to control inbound request volume per partner](advsus02-bp02.md). Response-side efficiency belongs to [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md). 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Push attribute-based rejection into the connectivity layer:** Configure the [OpenRTB Attribute Module](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) to match JSON paths against value sets and return a no-bid for requests you can never act on, so they never reach bidder compute. Roll each new filter out behind a high holdback percentage and lower it as you confirm the filter rejects only what you intended. 

1.  **Validate bid request structure in a cheap tier ahead of business logic:** Structural checks, required-field presence, protocol-version support, and numeric floor-price comparison are not attribute matching, so implement them in a lightweight validation tier in front of the bidder or at the bidder's entry point. Keep that tier clear of campaign lookups and model inference so a rejected request costs parsing only. 

1.  **Observe filter behavior:** Monitor filter hit rates to understand what percentage of inbound traffic is being rejected and the reasons behind each rejection. 

1.  **Iterate on rules:** Review no-bid analysis from your bidding application on a regular cadence and refine filter rules so they stay aligned with current traffic patterns. 

1.  **Track sustainability impact:** Quantify the compute and network the rejected traffic would have consumed, using CloudWatch utilization and filtered-request volume, and report it as a sustainability KPI. Read the filtered share against total inbound volume so the figure reflects filter effectiveness rather than a change in traffic. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) 
+  [ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw](advsus02-bp04.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 

 **Related documents:** 
+  [AWS RTB Fabric modules](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) (OpenRTB Attribute Module, inline execution) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (filter metrics, rejection rates, resource utilization) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 