

# ADVSUS01-BP04 Tune adapter concurrency and timeouts to stop spending compute on unusable bids

 Prebid Server completes each header bidding auction within the publisher's timeout and keeps bid density high. When an adapter continually misses the deadline, disable it. This stops the server from spending compute on responses that arrive too late to win. 

 **Desired outcome:** 
+  Prebid Server uses parallel adapter fan-out with per-adapter timeouts to maximize bid competition within the auction window without wasting compute on slow adapters. 
+  Adapters that consistently exceed their timeout budget are automatically disabled, reducing wasted CPU cycles. 
+  Bid response caching reduces redundant auction calls for identical impression contexts. 

 **Common anti-patterns:** 
+  Fanning out every auction to a large roster of demand adapters regardless of each adapter's historical contribution, which consumes compute on calls that rarely return a winning bid. 
+  Keeping adapters enabled even when they routinely miss the auction timeout, so the server spends its time budget waiting for responses the auction will discard. 
+  Setting a single global timeout with no per-adapter budget lets one slow adapter consume the window that faster adapters needed. 
+  Re-running a full adapter fan-out for impression contexts that repeat within seconds, instead of reusing a recent bid response. 
+  Treating adapter onboarding as additive only, with no process to measure marginal yield or retire underperforming partners. 

 **Benefits of establishing this best practice:** 
+  Less compute consumed per auction by avoiding calls to adapters that contribute little or miss deadlines, which lowers the resource and carbon proxy for the bidding tier. 
+  Faster, more predictable auctions because the time budget is spent on adapters that respond within it. 
+  Lower infrastructure cost from a smaller, higher-yield adapter set and from cache hits that avoid redundant fan-out. 
+  Clear operational signals from per-adapter latency and yield that make adapter retirement and re-testing a routine, data-driven decision. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The publisher sets one deadline for the whole auction. Prebid Server sends the bid request to many adapters at once, collects the responses that arrive before the deadline, and discards the rest. Every adapter you call consumes compute, whether it returns a usable bid or not. The auction's cost tracks the size of your adapter roster, so an adapter that keeps missing the deadline continues to cost you. 

 The deadline you grant each adapter and the set of adapters you invite both drive this cost. Latency and yield differ widely across partners and drift over time. Measure each adapter's latency and yield before you tune the deadline or trim the roster. 

 Measure each adapter's latency and yield before changing deadlines or disabling adapters. Set the deadline to balance compute cost against bid capture, and retain baselines for disabled adapters so you can re-test them when their performance recovers. 

 Many impression contexts repeat within a short window: the same page, viewer segment, and device type appear again before bid prices move much. For these contexts, a full fan-out reproduces almost the same result at full compute cost. Return a recent result instead, but only while it remains representative of current bid prices. Set the cache TTL based on how quickly prices for that inventory change. 

 Use compute signals such as adapter CPU time, adapters per auction, latency percentiles, and cache hit ratio for measuring this sustainability impact. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure parallel adapter fan-out with a per-adapter timeout budget:** Set each adapter's timeout to leave headroom for auction logic and response assembly within the publisher's auction window (for example, reserve roughly 10 ms of a 100 ms budget). A per-adapter budget guards against any single slow adapter consuming the window that faster adapters need. 

1.  **Instrument per-adapter p99 latency using CloudWatch custom metrics:** Publish per-adapter response latency percentiles as custom Amazon CloudWatch metrics. Set alarms that automatically disable adapters whose p99 latency consistently approaches their timeout budget, setting the trigger point from the headroom your auction deadline actually leaves. Track disabled adapters and periodically re-test them for recovery. 

1.  **Measure incremental yield per demand adapter:** Track bid win rate and CPM contribution per adapter. Disable adapters whose marginal revenue contribution falls below a threshold you set from your own yield data. In practice a relatively small core of adapters captures most of the realizable yield, so concentrate the auction on that set and disable the lowest-contributing adapters. 

1.  **Cache repeated bid responses in Amazon ElastiCache Serverless:** Implement a bid response cache with a short TTL (on the order of a few seconds) for identical impression contexts, tuned to balance bid freshness against compute saved. Measure the cache hit ratio for recurring ad pods and raise the TTL only while bid prices remain stable across the window. Each cache hit removes the need for a complete adapter fan-out, reducing compute proportionally. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP03 Reduce CPU time per bid in agent containers to lower fleet energy intensity](advsus01-bp03.md) 
+  [ADVSUS02-BP03 Suppress low-probability outbound bid requests to avoid needless compute and network draw](advsus02-bp03.md) 
+  [ADVSUS02-BP01 Reject non-actionable bid requests before they draw compute energy](advsus02-bp01.md) 

 **Related documents:** 
+  [Guidance for Deploying a Prebid Server on AWS](https://docs.aws.amazon.com/solutions/deploying-a-prebid-server-on-aws/) 

 **Related services:** 
+  [Amazon ElastiCache Serverless](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/WhatIs.html) 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 