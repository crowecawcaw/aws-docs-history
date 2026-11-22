

# ADVPERF06-BP04 Optimize Prebid Server adapter concurrency and timeout budgets

 Prebid Server completes unified header bidding auctions within the publisher-configured auction timeout while maximizing bid density from connected demand partners. Parallel adapter fan-out with derived per-adapter timeouts and circuit breakers maximizes bid competition within the auction window without penalizing the auction for slow adapters. 

 **Desired outcome:** 
+  Prebid Server completes unified header bidding auctions within the publisher-configured auction timeout while maximizing bid density from connected demand partners. 
+  Parallel fan-out sends bid requests to all adapters simultaneously, with per-adapter timeouts derived from the auction deadline rather than set independently of it. 
+  Circuit breakers automatically remove adapters with persistent latency or error issues, keeping a single degraded adapter from affecting overall auction performance. 
+  The auction timeout is calibrated against measured revenue and render time for your own inventory, not adopted from a published figure. 

 **Common anti-patterns:** 
+  Running adapter calls sequentially rather than in parallel, which burns through the auction timeout with each adapter called in turn. 
+  Setting a single global timeout for all adapters regardless of their historical latency profiles. 
+  No circuit breakers: continuing to send requests to a consistently failing adapter wastes timeout budget and delays auction completion. 
+  Setting an auction timeout so short that additional demand partners can't respond within it, which suppresses the bid competition the fan-out exists to create. 
+  Disabling an adapter on latency percentile alone, without measuring its timeout rate or its incremental revenue contribution. 

 **Benefits of establishing this best practice:** 
+  Parallel fan-out with derived per-adapter timeouts maximizes bid competition within the auction window without penalizing the auction for slow adapters. 
+  Circuit breakers help protect auction completion rate when individual adapters experience degradation, maintaining publisher yield during partial partner outages. 
+  A timeout calibrated to measured outcomes avoids both the revenue loss of timing out demand and the abandonment risk of waiting too long. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 More competing bids within the auction window produce higher winning CPMs for publishers. The auction architecture determines how many bids are received before the timeout expires. Sequential adapter calls waste most of the window waiting for each adapter in turn. To maximize bids, use parallel fan-out, which sends all bid requests at once and collects responses as they arrive. 

 [Prebid's own guidance](https://docs.prebid.org/dev-docs/faq.html) puts the starting point at 1,000 milliseconds or less for the internal auction timeout, with 3,000 milliseconds or less for the overall failsafe. Prebid's [bidder-count study](https://docs.prebid.org/overview/how-many-bidders-for-header-bidding.html) explains why a much tighter window defeats the purpose: below roughly 300 milliseconds, working with 5 bids or 10 bids makes no measurable difference, and below a 500 millisecond threshold a larger bidder pool takes longer to render. Waiting longer has a cost, because revenue drops when a page waits long enough that users abandon it. Prebid recommends reproducing that measurement against your own inventory rather than adopting any published number. 

 Per-adapter timeouts must be shorter than the auction deadline, but Prebid Server derives them rather than applying a flat percentage. In [PBS-Go](https://docs.prebid.org/prebid-server/endpoints/openrtb2/pbs-endpoint-auction.html), the per-bidder allowance is the request tmax minus measured request processing time, a network latency buffer, and a minimum expected response duration. PBS-Java applies a configurable percentage of tmax and then subtracts processing time and an upstream response reserve, with a floor below which calling a bidder isn't worthwhile. Where the computed allowance falls below the reserve Prebid Server needs to assemble its own response, the request isn't sent to that bidder at all. Configure the components rather than hardcoding a millisecond value, so the budget tracks the measured behavior of your deployment. The 50 to 75 percent band Prebid documents applies to the browser-side s2sConfig.timeout that bounds the call into Prebid Server, not to PBS per-bidder derivation. 

 Handle a transient failure with a circuit breaker. Automatically remove a slow or erroring adapter, let it recover, and readmit it, so it stops consuming timeout budget while unhealthy. A chronic yield problem calls for a commercial decision rather than automation. 

 The p99 latency metric alone can't distinguish transient failures from chronic ones. A p99 just below the timeout is normal for a long-tail adapter. It means almost all of that adapter's responses arrive in time, so it justifies neither an open circuit nor removal. Timeout rate distinguishes them, visible as seat non-bid status 101 and bidder error code 1. Read it alongside the adapter's incremental revenue net of the latency it adds. For a chronically slow but revenue-positive partner, Prebid offers options short of removal: a tmax deduction for that bidder, designation as a secondary bidder the auction doesn't wait on, per-geography configuration, or reordering. Reserve removal for adapters that combine a high timeout rate with negligible measured lift. 

 Bid responses can't be reused across impressions, which rules out a whole class of caching. Under OpenRTB, each bid relates to one specific impression through its impid, and the win and billing notice URLs are bound to that impression. Serving a prior impression's bid to a new one breaks win and billing attribution and corrupts buyer frequency capping and pacing. This is a contractual exposure with demand partners rather than a tuning trade-off. [Prebid Cache](https://docs.prebid.org/prebid-server/features/pbs-caching.html) stores the bid or VAST document under a per-object identifier after the bidders have responded, so it can be retrieved at render time for the same impression. To reduce adapter load, use request-level throttling, supply path optimization, or fewer and better-performing partners. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Calibrate the auction timeout against your own inventory:** Start from Prebid's recommended 1,000 milliseconds or less for the auction timeout and 3,000 milliseconds or less for the failsafe, then measure revenue and ad render time across a range of values for your own traffic. Confirm the window is long enough that added demand partners can respond, since below roughly 300 milliseconds additional bidders contribute nothing measurable. 

1.  **Derive per-adapter timeouts from the auction deadline:** Configure the derivation components rather than a fixed millisecond value: tmax\_adjustments in PBS-Go, or auction.biddertmax.percent, auction.biddertmax.min, and auction.tmax-upstream-response-time in PBS-Java. Verify that the computed per-bidder allowance leaves the response-preparation reserve intact, because a bidder whose allowance falls below it receives no request. 

1.  **Deploy Prebid Server on [Amazon EKS](https://aws.amazon.com/eks/) with Karpenter auto scaling:** Deploy Prebid Server containers on EKS with Karpenter for fast node provisioning during traffic spikes. Configure KEDA to scale pod count based on bid request queue depth published to [Amazon Managed Service for Prometheus](https://aws.amazon.com/prometheus/), enabling bid-rate-driven scaling that responds faster than CPU-based scaling. 

1.  **Implement per-adapter circuit breakers:** Use Resilience4j (for JVM-based Prebid Server) or equivalent circuit breaker libraries to implement per-adapter circuit breakers. Configure the open threshold at 50% failure rate over a 30-second sliding window, with half-open probing after 15 seconds. Emit AdapterCircuitOpen custom metrics to CloudWatch and set alarms when multiple adapters enter open state simultaneously, which indicates a systemic issue. 

1.  **Configure Prebid Cache for render-time retrieval:** Where the deployment serves video or AMP inventory, run [Prebid Cache](https://docs.prebid.org/prebid-server/features/pbs-caching.html) so Prebid Server stores the winning bid or VAST document after the auction completes and the player retrieves it by identifier at render time. Treat this as a delivery mechanism for a completed auction, and don't use it to skip adapter calls for a new impression. 

1.  **Measure incremental yield per adapter before removing any:** Track per-adapter win rate, eCPM contribution, and timeout rate using CloudWatch custom metrics, reading per-bidder latency from response.ext.responsetimemillis. For adapters with a high timeout rate and negligible revenue lift, apply a tmax deduction, mark them secondary, or vary them by geography before disabling them outright. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF06-BP05 Minimize SGAI ad break latency with CDN-cached manifests, pre-transcoded creatives, and scaled ADS](advperf06-bp05.md) 

 **Related documents:** 
+  [Prebid FAQ: What should my timeouts be?](https://docs.prebid.org/dev-docs/faq.html) 
+  [How many bidders should I work with?](https://docs.prebid.org/overview/how-many-bidders-for-header-bidding.html) 
+  [Prebid Server auction endpoint and timeout configuration](https://docs.prebid.org/prebid-server/endpoints/openrtb2/pbs-endpoint-auction.html) 
+  [Prebid Server Deployment on AWS Solutions Library](https://aws.amazon.com/solutions/implementations/prebid-server-deployment-on-aws/) 
+  [Optimizing your Kubernetes compute costs with Karpenter consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/) 

 **Related services:** 
+  [Amazon ElastiCache Serverless](https://aws.amazon.com/elasticache/features/) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 