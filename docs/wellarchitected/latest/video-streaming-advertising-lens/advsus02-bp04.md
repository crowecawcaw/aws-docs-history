

# ADVSUS02-BP04 Reduce no-bid response volume to lower infrastructure demand and energy draw
<a name="advsus02-bp04"></a>

 Real-time bidding produces both winning bids and no-bid responses. Reducing unnecessary no-bid traffic lowers DSP infrastructure demand and energy draw without compromising win rates. 

 **Desired outcome:** 
+  No-bid traffic is treated as a measurable, reducible cost rather than an inevitable byproduct of bidding. 
+  You understand where requests you cannot act on originate, you work with supply partners to suppress them at the source, and you handle the remaining no-bid responses as efficiently as possible. 
+  Energy consumed per no-bid response trends downward over time while win rates are preserved. 
+  No-bid rate is measured per SSP link and reviewed as a recurring sustainability metric. 
+  The volume of requests you cannot act on is reduced through targeting agreements with supply partners. 
+  Remaining no-bid responses are handled at the most efficient layer available, minimizing compute per response. 
+  Energy consumption attributable to no-bid handling is visible and decreasing. 

 **Common anti-patterns:** 
+  Accepting all incoming bid requests indiscriminately and absorbing the full cost of responding "no-bid" to traffic that could never be won. 
+  Tracking only win rate and revenue, with no visibility into the volume or energy cost of no-bid responses. 
+  Treating no-bid handling as a fixed infrastructure cost rather than a metric that can be optimized in partnership with SSPs. 
+  Scaling bidding compute to absorb growing no-bid traffic instead of suppressing the unnecessary traffic upstream. 

 **Benefits of establishing this best practice:** 
+  Lower energy draw and infrastructure demand from processing fewer requests you cannot act on. 
+  Reduced operating cost per bid opportunity without sacrificing win rate. 
+  Mutual efficiency gains with SSP partners who also reduce request-overhead on their side. 
+  Clearer sustainability reporting through a directly attributable no-bid energy metric. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 No-bid responses are the majority of what a demand-side platform emits into a real-time bidding exchange, because a DSP wins only a fraction of the impression opportunities it is offered. Every declined request travels the network, is deserialized, evaluated against targeting and budget, and answered, work that consumes compute and bandwidth without producing an ad. In connected-television and streaming video, each ad break across a large audience fans out into an enormous request volume. Across billions of requests, small per-no-bid savings add up. You can reason about the resource footprint of each no-bid: compute cycles, connection state, and bytes on the wire. 

 At the response level, an HTTP 204 with no content is the lightest way to signal a no-bid, cheaper to serialize and transmit than an HTTP 200 that carries an empty body or a no-bid reason code. HTTP 204 also withholds the diagnostic signal an exchange uses to stop sending inventory the DSP cannot win. Upstream suppression produces the larger and more durable savings. Targeting agreements or filters tuned too aggressively can drop the occasional request that would have converted, trading a small immediate energy saving for lost revenue and reach that is harder to observe. 

 At real-time bidding request rates, opening and tearing down a fresh TCP and TLS connection for each exchange would let handshake overhead, the asymmetric cryptography and extra round trips, dominate the energy of a response that carries almost no data. Persistent connections and pooling amortize that setup cost across many requests, so per-no-bid energy depends heavily on connection reuse. The layer at which a no-bid is resolved has the same effect. Resolving a no-bid near the network edge, before promoting the request into full bidding evaluation, skips the deserialization and application logic that runs on responses handled deep in the stack. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze no-bid rate per SSP link:** Measure your no-bid rate for each SSP connection to identify which partners send you the most traffic you cannot act on. 

1.  **Coordinate targeting with SSP partners:** Work with supply partners to improve request targeting. This is a mutual benefit: the SSP reduces request overhead while the DSP reduces no-bid response overhead. 

1.  **Handle no-bid scenarios efficiently:** Configure RTB Fabric modules to process no-bid scenarios at the network layer where possible, reducing the compute required per response. 

1.  **Track no-bid volume as a sustainability metric:** Report no-bid response volume alongside win rate so the efficiency of your bidding is visible over time. 

1.  **Monitor energy consumption per SSP link:** Track energy use per link to expose optimization opportunities and confirm that suppression and efficient handling are reducing draw. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) 
+  [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) (responder gateway metrics, modules) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (no-bid rate monitoring per link, resource utilization) 
+  [AWS Graviton](https://aws.amazon.com/ec2/graviton/) (for energy-efficient bidding compute) 