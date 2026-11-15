

# ADVREL09-BP03 Design graceful auction degradation when demand partners become unavailable
<a name="advrel09-bp03"></a>

 When multiple adapters become unavailable, the auction executes with the remaining healthy demand partners. Dynamic floor price adjustments maintain publisher yield during reduced competition, and cached fallback creatives fill zero-bid auctions. 

 **Desired outcome:** 
+  The auction consistently completes within its timeout budget and returns the best available bids to the publisher's ad server, even if only a subset of adapters responded. 
+  Fill rate remains above 85% during partial demand partner failures. 
+  Dynamic floor prices protect yield when competition is temporarily reduced. 

 **Common anti-patterns:** 
+  Blocking the entire auction waiting for a single slow adapter to respond or timeout. 
+  Returning empty ad slots to the publisher when all adapters fail, with no fallback mechanism. 
+  Static floor prices that don't adapt to reduced competition, so the publisher accepts bids below the going rate during partner outages. 

 **Benefits of establishing this best practice:** 
+  Graceful degradation helps publishers maintain monetization even during demand partner outages. 
+  Fill rate remains above 85% during partial failures, and dynamic floor prices reduce the risk of yield erosion when competition is temporarily reduced. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Publisher revenue depends on fill rate and CPM. Fill rate measures how often a slot receives a paying bid, and CPM measures what each thousand impressions earns. An adapter outage pushes on both metrics at once. Fewer partners bid, fill rate falls, competition thins among the survivors, and clearing prices fall. 

 A floor above the going rate rejects the remaining bids and drops fill rate. Adapters flap between healthy and unhealthy as they recover, and a floor that shifts on every change makes bidding unstable. Buyers see erratic pricing and pull back. Adjust the floor gradually against trailing CPM to keep it near the going rate. 

 A cached creative works for a display slot but not for premium video, where buyers expect fresh targeting and a stale creative can misrepresent the audience. Programmatic guaranteed deals are stricter still. They are contracted commitments to a specific buyer, and a cached substitute breaks the contract. Exclude premium video and programmatic guaranteed inventory from the cache. 

 Yield and revenue teams set the commercial thresholds, engineering wires them into the auction, and brand safety teams decide which creatives may be cached. When these groups disagree, the fallback serves unsafe creatives or blocks safe ones. Emit a stream of degraded auction events so that the revenue team can measure the outage's cost. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure Prebid Server to return best-available bids on timeout:** Confirm Prebid Server auction configuration doesn't block on any single adapter. Set the overall auction timeout and execute the auction with whatever bid responses arrive before the deadline. Return the best bids from available adapters to the publisher's ad server on time. 

1.  **Implement dynamic floor price adjustment based on adapter count:** Monitor the count of active adapters in each auction. When active adapter count drops below threshold (configurable per publisher, typically 3), apply a floor price multiplier (1.2–1.5x) based on trailing CPM data. Reset floor price when adapter count recovers. 

1.  **Deploy ElastiCache fallback creative cache:** Implement a cache-aside pattern that stores the last successful bid response per ad unit (publisher \+ placement combination). On zero-bid auctions, retrieve the cached creative. Set appropriate TTLs (1 hour display, 30 minutes video) and configure the cache to store only creatives from demand partners that have met brand safety requirements. 

1.  **Monitor fill rate and CPM during adapter degradation:** Publish real-time fill rate and CPM metrics to CloudWatch dimensioned by adapter health state. Configure alarms when fill rate drops below 85% sustained for 5 minutes during adapter outages. Use these metrics to evaluate the effectiveness of graceful degradation configurations. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 

 **Related documents:** 
+  [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/) 

 **Related services:** 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 