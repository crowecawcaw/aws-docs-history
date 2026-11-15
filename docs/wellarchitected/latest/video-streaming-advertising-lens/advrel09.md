

# Prebid Server resilience
<a name="advrel09"></a>

 Prebid Server acts as the server-side header bidding orchestrator, sending bid requests to multiple SSPs and DSPs simultaneously. A failure in one adapter should not cascade to other demand partners or halt publisher monetization. Design Prebid Server deployments to maintain auction capability even when individual adapters, Availability Zones, or demand partners become unavailable. 


|  ADVREL09: How do you keep your Prebid Server implementation available when individual demand partner adapters or auction components fail?  | 
| --- | 
| [ADVREL09-BP01 Deploy Prebid Server across multiple Availability Zones with health-checked load balancing](advrel09-bp01.md) | 
| [ADVREL09-BP02 Implement per-adapter circuit breakers and bulkhead isolation](advrel09-bp02.md) | 
| [ADVREL09-BP03 Design graceful auction degradation when demand partners become unavailable](advrel09-bp03.md) | 

## Capability intent
<a name="advrel09-capability-intent"></a>
+  Prebid Server instances are distributed across at least two Availability Zones with active health checks for automatic traffic redistribution. 
+  Per-adapter circuit breakers and bulkhead isolation keep a degraded adapter from starving healthy adapters of resources. 
+  The auction consistently completes within its timeout budget and returns the best available bids even when multiple adapters are unavailable. 

## Common issues to watch for
<a name="advrel09-common-issues-to-watch-for"></a>
+  Health checks that only validate HTTP 200 (container alive) rather than auction engine responsiveness. 
+  Single HTTP connection pool shared across all adapters. One slow adapter can exhaust connections for all others. 
+  No fallback creative when all adapters fail, resulting in empty ad slots. 