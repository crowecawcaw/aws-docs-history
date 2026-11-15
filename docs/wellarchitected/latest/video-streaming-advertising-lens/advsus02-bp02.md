

# ADVSUS02-BP02 Apply rate limiting to control inbound request volume per partner
<a name="advsus02-bp02"></a>

 Without rate limits, partner spikes drive unplanned infrastructure scaling and energy draw. Rate limiting caps queries per second per partner connection, which stabilizes resource demand and reduces energy consumption in downstream systems. 

 **Desired outcome:** Inbound request volume from each advertising partner is bounded by an agreed queries-per-second (QPS) limit enforced before traffic reaches your core infrastructure. Aggregate demand stays within provisioned capacity, scaling events become predictable, and per-partner resource and energy consumption is observable and attributable. 
+  Each partner connection has an explicit QPS cap derived from historical traffic and contractual terms. 
+  Limits are enforced before traffic reaches your core infrastructure (at the network edge), so excess traffic is shed before it consumes downstream compute. 
+  Aggregate demand stays within provisioned capacity and scaling events are predictable. 
+  Operators receive early-warning signals before a partner reaches its hard cap. 
+  Per-partner resource and utilization metrics are observable and attributable, and are a proxy for energy consumption to inform ongoing tuning. 

 **Common anti-patterns:** 
+  Accepting unbounded inbound request volume and relying solely on automatic scaling to absorb partner spikes, which drives unplanned capacity and energy growth. 
+  Applying a single global rate limit instead of per-partner limits, so one partner's burst starves others and obscures attribution. 
+  Setting limits once and never revisiting them as partner traffic patterns and business value shift. 
+  Enforcing limits deep in the application stack after traffic has already consumed network and compute resources. 

 **Benefits of establishing this best practice:** 
+  Reduces wasted energy and capacity by limiting demand to provisioned, right-sized resources. 
+  Makes scaling behavior predictable, lowering the carbon cost of over-provisioning headroom for unmanaged spikes. 
+  Improves fairness and stability across partners by isolating the impact of any single partner's traffic. 
+  Provides per-partner visibility that exposes optimization and renegotiation opportunities. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In video-streaming advertising, inbound request volume originates outside your control. External bidding partners send traffic in bursts tied to audience and campaign activity. Automatic scaling can absorb those spikes, but the headroom provisioned for the largest spike stays mostly idle. Idle but powered infrastructure still draws energy. Rate limiting bounds the volume of work you accept so intake stays aligned with provisioned capacity. Queries per second (QPS) is the unit for bounding each partner's demand. 

 A single global limit treats all inbound traffic as interchangeable. Requests arrive from distinct partners with distinct contracts, traffic profiles, and business value. A global ceiling sheds those requests without distinction when total volume is high. The ceiling couples partners, so one partner's burst consumes the shared allowance and starves well-behaved ones. It also destroys attribution because a spike observed only in aggregate can't be traced to its source. Per-partner boundaries contain each burst to its own allocation and make resource consumption attributable by connection. The usable signal is a proxy inferred from per-connection resource and utilization metrics. Without per-partner segmentation, that proxy has no source to attribute to and no defensible basis for tuning a limit or renegotiating a contract. 

 Set each partner's cap high enough to accept legitimate, revenue-bearing bid requests and low enough to keep automatic scaling from absorbing spikes. Reassess caps as campaigns, audiences, and commercial relationships evolve. A cap left in place drifts out of alignment, either throttling legitimate growth or reintroducing the over-provisioning this practice exists to remove. Enforce the limit at the network edge, because a request that traverses the stack before rejection has already consumed its network and compute energy. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set per-partner QPS limits:** Analyze historical traffic and contractual agreements for each partner to derive a defensible queries-per-second cap, rather than applying a single global limit. 

1.  **Enforce limits at the network layer:** Deploy rate limiting in the AWS RTB Fabric Rate Limiter module so that limits are applied before traffic reaches your downstream infrastructure. 

1.  **Configure graduated thresholds:** Set a warning threshold far enough below the hard cap that operators can act before rejection begins, and derive that gap from how long your own remediation takes. 

1.  **Review and adjust limits monthly:** Reassess each partner's limit on a monthly cadence using observed traffic trends and the business value of the partner relationship. 

1.  **Monitor energy consumption per partner link:** Track resource and energy metrics for each partner connection to identify optimization opportunities and inform limit tuning. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) 
+  [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 

 **Related documents:** 
+  [AWS RTB Fabric modules, including the rate limiter](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) (Rate Limiter module) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) (QPS monitoring per link, resource metrics) 