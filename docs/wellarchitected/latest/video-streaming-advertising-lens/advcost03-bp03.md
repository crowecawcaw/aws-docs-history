

# ADVCOST03-BP03 Filter inbound bid requests at the network layer to reduce compute costs
<a name="advcost03-bp03"></a>

 Most DSP bidders respond with no-bid to 70% or more of incoming requests. Each no-bid still consumes compute. The request traverses the network, gets deserialized, gets evaluated against targeting logic, and produces a response with zero revenue. If you filter predictably non-viable requests at the network layer before they reach application compute, you avoid that cost entirely. The built-in OpenRTB Filter and Rate Limiter modules in RTB Fabric run this filtering at no additional charge. 

 **Desired outcome:** 
+  Invalid, malformed, or predictably non-matching bid requests are rejected at the network layer, so that only commercially viable traffic reaches application compute. 
+  Filter rules based on OpenRTB fields (geography, device type, floor price, ad format) are validated through holdback testing before full deployment. 
+  Rate limiting helps protect downstream systems from traffic spikes that bypass attribute-based filters. 
+  Per-partner rejection rates are monitored and partners with high rejection rates are engaged to improve bid request quality. 
+  Filter rules are recalibrated weekly based on no-bid analysis to maintain accuracy as campaigns and traffic patterns shift. 

 **Common anti-patterns:** 
+  Accepting all inbound bid requests into the application stack before evaluating validity, so full compute costs land on the 70%\+ of requests that produce no-bid responses based on predictable attributes. 
+  Implementing filtering logic only at the application layer rather than at the network layer, which still incurs deserialization and evaluation costs on requests that should never reach the bidder. 
+  Deploying filter rules without holdback testing (holdbackPercentage), so accidental filtering of commercially viable requests goes undetected and revenue loss cannot be traced. 
+  Deploying only attribute-based filters without rate limiting, which leaves downstream systems vulnerable to traffic spikes that bypass filter rules. 
+  Treating filter rules as static configuration rather than a living system, so accuracy drifts as campaigns start, end, and shift targeting. 
+  Never iterating on filter rules based on no-bid analysis. 

 **Benefits of establishing this best practice:** 
+  Reduced compute costs proportional to filtered traffic volume (30-70% of inbound requests removed). 
+  OpenRTB Filter and Rate Limiter are included with RTB Fabric. 
+  Inline network-layer execution adds negligible latency compared to application-level filtering. 
+  Rate limiting helps protect bidder availability during traffic spikes regardless of filter configuration. 
+  Partner engagement on rejection rates improves traffic quality at the source. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every bid request that reaches application compute costs money whether your bidder responds with a bid or a no-bid. In high-volume RTB environments processing millions of requests per second, even a small percentage of non-viable requests wastes a large amount of compute. Typical DSP no-bid rates range from 70% to 95%. When you can predict from attributes visible in the OpenRTB request envelope (geography, device type, COPPA flag, domain, and floor price) that a request will produce a no-bid, filtering it at the network layer turns a per-request compute cost into a near-zero marginal cost. 

 Use both attribute filters and rate limiting for complete protection. Attribute-based filtering (the OpenRTB Filter module) drops or tags requests that match specific field values you define. Rate limiting (the Rate Limiter module) caps total transactions per second flowing through a link regardless of attributes, which helps protect your compute from volume spikes that exceed your bidder's healthy throughput. 

 The [RTB Fabric modules](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) run filtering inline within the request path at the network layer, which adds negligible latency compared to forwarding requests to application compute. Network-layer execution skips the connection handling, deserialization, and business logic evaluation that application-layer processing requires. 

 The primary risk is a false positive, where the filter suppresses a request that would have received a valid bid. The holdbackPercentage parameter controls what fraction of matching traffic passes through the filter unaffected, which sets up an A/B comparison. A holdback of 90 means only 10% of matching traffic gets filtered, so you keep a large control group to confirm that filtered traffic produces no bids. Decrease holdback gradually (90, 50, 10, and 0) over several weeks so you can detect revenue impact at each stage before committing further. 

 Your bidder's behavior changes as campaigns start and end, as new inventory types emerge, and as partner traffic composition shifts. A geo filter that correctly identifies no-bid traffic today might catch viable requests next month after a new campaign targets that geography. Without weekly recalibration against fresh no-bid logs, the gap between network-layer decisions and actual bidder decisions widens. 

 Filtering exists between supply operations (who manage partner relationships) and bidder engineering (who manage compute costs), so ownership needs to be clear. If supply operations change targeting parameters without notifying whoever maintains filter rules, you might see a spike in false positives. A defined owner and a change notification process between these teams keeps filters aligned with the current bidding strategy. 

 When you monitor rejection rates per partner, you can see which supply sources send the most traffic that produces no bids. Partners whose rejection rates exceed 20% are worth a conversation about improving bid request quality at the source, which reduces the network transfer you pay for on requests that will never pass validation. The SSP stops paying to transmit requests that generate no revenue, and the DSP stops paying to process them. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Analyze historical bid logs to identify filterable traffic patterns:** Query your bid event archive to identify the highest-volume no-bid reasons: missing required OpenRTB fields, unsupported protocol versions, floor prices below your minimum threshold, geographies you never target, and device types outside your buying interest. Quantify the traffic volume each category represents. Prioritize patterns with 90%\+ no-bid rates and high request volume. 

1.  **Configure RTB Fabric OpenRTB Filter with holdback testing:** Enable the OpenRTB Filter module targeting the highest-volume no-bid categories. Set initial holdbackPercentage to 90 (only 10% of matching traffic is filtered). Use headerTag to mark filtered requests for A/B analysis without dropping them. This validates filter accuracy before committing to blocking. 

1.  **Reduce holdbackPercentage gradually over 2-4 weeks:** After confirming filter accuracy through holdback comparison, reduce holdbackPercentage in stages: 90 to 50 to 10 to 0. Validate at each stage that bid metrics (win rate and revenue) remain stable for the unfiltered cohort. If revenue drops, investigate which filter rule is producing false positives. 

1.  **Configure Rate Limiter module to protect downstream systems:** Set per-link maximum TPS caps based on your bidder's healthy throughput threshold. This helps protect downstream compute from unfiltered traffic spikes regardless of filter configuration. Size the cap to accommodate peak legitimate traffic without dropping viable requests. 

1.  **Iterate weekly to promote new no-bid patterns to filter rules:** Compare application-level no-bid logs against existing network-layer filter rules weekly. Identify new no-bid patterns that appear consistently (for example, a new inventory type your bidder doesn't support). Promote them to network-layer filter rules with holdback testing. Alert when per-filter bid-rate metrics shift, indicating the pattern may no longer be safe to filter. 

1.  **Engage partners with high per-partner rejection rates:** Track rejection rates per partner link in CloudWatch. Engage partners with rejection rates exceeding 20% to improve bid request quality at the source. Provide specific data: which segments produce zero bids, what volume they represent, and what targeting filters would suppress them. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVCOST03-BP04 Shape outbound traffic and optimize no-bid handling](advcost03-bp04.md) 

 **Related documents:** 
+  [AWS RTB Fabric Modules Documentation](https://docs.aws.amazon.com/rtb-fabric/latest/userguide/modules.html) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 