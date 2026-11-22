

# Latency-sensitive advertising

 Consider strategies for managing latency-sensitive advertising workloads through throttling and rate-limiting implementations. Avoid traditional retry mechanisms for fast-failing services, implement effective caching strategies, and proportionally scale across all system components to maintain consistent performance. In real-time bidding, the workload must handle failures in latency-sensitive services within the 100 ms bid response window. There is no room for exponential backoff or deep retry queues. 


|  ADVREL02: How do you manage reliability for your latency-sensitive advertising services within strict auction deadlines?  | 
| --- | 
| [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry](advrel02-bp01.md) | 
| [ADVREL02-BP02 Implement a caching strategy](advrel02-bp02.md) | 
| [ADVREL02-BP03 Avoid scale mismatch of both internal services and external partners](advrel02-bp03.md) | 

## Capability intent
<a name="advrel02-capability-intent"></a>
+  Failures in latency-sensitive services are handled with fast-fail approaches and appropriate rate-limiting rather than traditional exponential backoff and retry. 
+  Caching strategies are applied at multiple levels (client-side, server-side, CDN) to reduce response latency and the load on database clusters. 
+  All system components (application servers, load balancers, databases) scale proportionally to avoid scale mismatch bottlenecks at the boundaries between components. 

## Common issues to watch for
<a name="advrel02-common-issues-to-watch-for"></a>
+  Using exponential backoff on bid path services, where a 5-second retry delay results in many failed bids and potentially insurmountable retry queues. 
+  Applying the same rate limit to all clients regardless of their traffic volume agreements, under-serving high-value partners while over-allocating capacity to low-value connections. 
+  Not considering the latency impact of cache misses during peak traffic. If a cache cold-starts during a spike, all requests hit the database simultaneously. 