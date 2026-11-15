

# ADVREL04-BP02 Architect defensively against failures
<a name="advrel04-bp02"></a>

 Some system failures come from external partners or dependencies that are outside of your control. Implement circuit breakers, retries, and fallbacks to gracefully handle failures from external dependencies, and avoid cascading failures within your system. 

 **Desired outcome:** 
+  External dependency failures are isolated and don't cascade into auction failures. 
+  Your system continues to serve bids with graceful degradation (default targeting and cached data) when external services are unavailable. 
+  Direct Connect or PrivateLink provides stable, low-latency connectivity for critical partner integrations. 

 **Common anti-patterns:** 
+  Treating external partner dependencies as consistently available, with no circuit breaker, retry, or fallback. 
+  Making control plane calls (e.g., describing available DSPs) on every bid request instead of caching pre-computed state. 
+  Routing high-volume partner traffic over the public internet, accepting high p99 latency variance for critical integrations. 
+  Never exercising fallback paths, so degraded-mode behavior is unverified until a real partner outage. 

 **Benefits of establishing this best practice:** 
+  External dependency failures are isolated and don't cascade into auction failures. 
+  The system keeps serving bids with graceful degradation (default targeting and cached data) when partners are unavailable. 
+  Private connectivity (Direct Connect or PrivateLink) gives stable, low-latency links for critical partner integrations. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Advertising systems depend on external partners: DSPs submitting bids, DMPs supplying audience segments, and measurement providers validating impressions. Each partner is a failure domain you don't control. Outages, latency spikes, and error bursts happen without warning during your auction windows. Every synchronous call to an external dependency couples your auction result to that partner's availability. A single partner outage can then cascade into a system-wide auction failure. 

 Static stability keeps the data plane running when the control plane is impaired. Bid requests that must complete in single-digit milliseconds cannot depend on control plane freshness. If the system asks which partners are active on every request, the control plane is in the critical path of the data plane. Any control plane delay then becomes an auction delay. Refresh configuration on a different cadence than you consume it to insulate the data plane from upstream instability. 

 A fallback path that has never executed under production traffic is unproven. Confirm graceful degradation by exercising failure modes under realistic conditions. When you treat resilience validation as a periodic discipline, you can discover systemic brittleness earlier and more efficiently. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement circuit breakers for all external partner connections:** Deploy Resilience4j or equivalent circuit breakers on all DSP, SSP, DMP, and measurement provider connections. Set open threshold at 50% failure rate over a 30-second window. Configure fallback behavior for each connection: DSP unavailable (skip DSP from auction), DMP unavailable (use cached audience segments), measurement provider unavailable (record locally, sync later). 

1.  **Use Static Stability patterns for partner configuration:** Pre-fetch and cache partner configurations (active DSPs, bid floors, and targeting parameters) at service startup and refresh on a configurable interval (every 5 minutes). During a control plane failure, the service continues operating with the last-known-good configuration rather than blocking on configuration retrieval. 

1.  **Establish Direct Connect or PrivateLink for highest-volume partner connections:** For partners handling more than 10% of your bid volume, establish AWS PrivateLink or Direct Connect for stable, private connectivity. Monitor latency variance on these connections. Internet-based connections show significantly higher p99 latency variability than private connections. 

1.  **Validate fallback paths with regular fault injection:** Quarterly, inject failures into each external dependency category and verify that: the correct circuit breaker activates, fallback behavior produces valid (if degraded) auction results, and the system recovers automatically when the dependency recovers. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry](advrel02-bp01.md) 
+  [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) 
+  [ADVREL04-BP03 Monitor and manage partner SLAs against actuals](advrel04-bp03.md) 

 **Related documents:** 
+  [Static stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/) 
+  [Reducing the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html) 

 **Related services:** 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon ElastiCache](https://aws.amazon.com/elasticache/) 