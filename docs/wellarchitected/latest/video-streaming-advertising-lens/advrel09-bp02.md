

# ADVREL09-BP02 Implement per-adapter circuit breakers and bulkhead isolation
<a name="advrel09-bp02"></a>

 Prebid Server communicates with multiple SSP and DSP adapters concurrently. A slow or failing adapter can consume shared thread pool resources and starve healthy adapters, causing cascading auction failures. Isolate each demand partner adapter into its own failure domain. 

 **Desired outcome:** 
+  Each demand partner adapter draws from its own bounded connection pool, so one partner's slow responses can't exhaust the resources the others need. 
+  A degraded adapter is removed from the active auction within a bounded detection window you have chosen and measured, while the remaining healthy adapters continue processing. 
+  Losing a subset of adapters costs you their demand while auctions still complete and return a winner from the adapters that remain. 
+  Per-adapter timeout budgets reflect each partner's observed latency profile rather than a single uniform value, and the sum of them leaves room for response aggregation inside the auction deadline. 

 **Common anti-patterns:** 
+  Sharing a single HTTP connection pool across all adapters, which allows one slow adapter to exhaust connections for all. 
+  No circuit breaker, so continuing to send requests to a failing adapter wastes the auction timeout budget. 
+  Uniform timeout for all adapters regardless of historical latency profiles. 

 **Benefits of establishing this best practice:** 
+  Adapter failures stay contained to the failing partner instead of consuming the auction's shared resources. 
+  A partial partner outage degrades demand density rather than auction availability, so publisher fill rate falls by the missing partners' contribution instead of collapsing. 
+  Fail-fast on a tripped adapter returns its share of the timeout budget to the auction, so the remaining partners are not squeezed by a partner that will not answer. 
+  Alarm patterns become diagnostic. Many adapters opening at once points upstream at something shared, while one opening points at that partner. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Every adapter draws from the same thread pool by default, so one slow demand partner holds its connections open and healthy adapters wait behind it. The bulkhead pattern breaks that coupling by giving each adapter its own resource boundary. A circuit breaker adds a second boundary in time, stopping calls to a partner once failures exceed the threshold. 

 Set each threshold from the partner's own error and latency distribution, measured over a window long enough that normal jitter does not trip the breaker. One threshold rarely suits partners with different latency profiles. Treat any starting value as a hypothesis to calibrate against observed behavior. 

 Keep each adapter's budget inside the auction's aggregate deadline. The gap between budget and deadline is not spare capacity, because response aggregation, bid validation, and the ad server's own response consume time after the last adapter answers. A budget set too close to the aggregate starves those steps, and the auction misses its deadline while a straggler is still pending. Size each budget from the partner's observed response distribution, then confirm the sum of concurrent budgets plus aggregation still fits the deadline the ad server enforces. 

 Infrastructure teams own the shared infrastructure while partner managers hold each demand source's reliability history. Tuning these thresholds requires input from both teams. With isolation for each adapter, many adapters opening at once points to something shared upstream, while a lone adapter opening points only at that partner. Inject failures deliberately to verify the isolation. Production traffic alone does not prove it. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Implement circuit breakers with per-adapter thresholds:** Configure a circuit breaker per adapter, setting the failure-rate threshold, sliding-window size, open-state wait duration, and half-open trial-call count from that partner's measured error and latency distribution. Start from your library's defaults, then calibrate each value against the partner's history rather than applying one profile across adapters. Record the rationale for each setting so a later operator can tell a tuned value from an inherited one. 

1.  **Assign per-adapter HTTP connection pools:** Give each adapter its own client instance with its own pool, so pool exhaustion is bounded to the partner that caused it. Size each pool from that adapter's share of bid request volume and its observed response time, since a slower partner needs more concurrent connections to carry the same throughput. Verify the isolation holds by saturating one adapter's pool and confirming the others are unaffected. 

1.  **Publish circuit breaker metrics to CloudWatch:** Emit CircuitBreakerState (OPEN/CLOSED/HALF\_OPEN) and AdapterTimeoutCount as CloudWatch custom metrics per adapter. Create CloudWatch alarms when 3\+ adapters enter OPEN state simultaneously, which indicates a systemic issue rather than isolated adapter failures. 

1.  **Validate isolation with fault injection:** Use [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to fail and to slow individual adapter endpoints, then confirm that auctions still complete and return a winner from the remaining partners, that the failing adapter's breaker opens, and that healthy adapters hold their latency profile. Measure your own baseline completion rate first so the degraded number has something to be compared against. Run the experiments during low-traffic windows and treat any auction-wide failure, or a healthy adapter slowing in sympathy, as a blocker. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry](advrel02-bp01.md) 

 **Related documents:** 
+  [Implementing health checks - Amazon Builders Library](https://aws.amazon.com/builders-library/implementing-health-checks/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 