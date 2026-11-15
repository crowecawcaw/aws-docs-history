

# ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backoff and retry
<a name="advrel02-bp01"></a>

 With real-time bidding, your workload must handle failures in latency-sensitive services within the 100 ms bid response window. Avoid exponential backoff and retry. Use fast-fail approaches and rate limiting to keep services responsive. 

 **Desired outcome:** 
+  Latency-sensitive service failures are detected and handled within the bid response time budget rather than accumulating retry queues. 
+  Rate limiting reduces the risk of resource exhaustion while fairly distributing resources among clients. 
+  The auction completes and returns the best available bids even when individual services are degraded. 

 **Common anti-patterns:** 
+  Using exponential backoff with 5-second maximum delays on bid path services. 
+  Not distinguishing between bid path services (must fail fast) and post-bid analytics services (can retry aggressively asynchronously). 
+  Setting rate limits too low, so legitimate requests get rejected or delayed and ad serving effectiveness drops. 

 **Benefits of establishing this best practice:** 
+  Bid response latency stays within SLO even when downstream services are degraded. 
+  Rate limiting helps protect services from being overloaded while maintaining fair resource distribution. 
+  Clear failure handling behavior is predictable and testable. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 In a 100 ms bid response window, a single throttle and 5-second retry can produce many failed bids and retry queues that never drain. Regulate request rates using token buckets, leaky buckets, or fixed window counters, or use a managed service such as Amazon API Gateway request throttling. 

 Rate limiting reduces resource exhaustion and distributes resources fairly among clients or services. Limits set too low reject or delay legitimate requests and reduce availability or responsiveness. 

 For bid path services, attempt the call once. If it fails within the latency budget, proceed with cached data, default values, or omit the bid. For post-bid services such as analytics, billing, and frequency updates, use aggressive retry with Amazon SQS and a dead-letter queue (DLQ). These services run asynchronously outside the bid response window. 

 Amazon API Gateway implements the token bucket algorithm to throttle requests. Amazon SQS and Amazon Kinesis can buffer requests to smooth request rates. AWS WAF can apply rate limiting and throttle specific API consumers. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Distinguish bid-path services from post-bid services:** Create a service inventory that classifies each advertising service as bid-path (must fail fast within the response window) or post-bid (can retry aggressively asynchronously). Apply different error handling strategies to each class: fast-fail with graceful degradation for bid-path, reliable retry with DLQ for post-bid. 

1.  **Implement token bucket rate limiting on bid-path API endpoints:** Configure Amazon API Gateway throttling with per-client rate limits based on traffic volume agreements. Set burst limits conservatively to guard against a single misbehaving client affecting others. Use WAF rate-based rules for IP-level protection. Configure limits to allow 120% of contracted QPS to accommodate burst traffic while blocking clearly anomalous spikes. 

1.  **Add per-service timeout budgets on the bid path:** For each bid-path service call, set a timeout equal to the service's allocated portion of the total bid response budget (typically 5–15 ms for enrichment lookups, 10–20 ms for targeting data retrieval). If the service doesn't respond within its budget, proceed with a cache hit, default value, or empty response. Log all timeout events with service name and elapsed time for capacity planning. 

1.  **Use SQS for reliable post-bid asynchronous processing:** Route all post-bid events (impression beacons, click tracking, frequency cap updates, analytics) through SQS queues with maxReceiveCount and DLQ configured. Use standard queues for high-throughput events that tolerate at-least-once delivery, FIFO queues for ordered events (such as bid events that must be processed in auction sequence). Configure visibility timeout equal to your expected processing time × 2 to allow retries. 

1.  **Monitor queue depths and timeout rates as leading indicators:** Configure CloudWatch alarms on SQS queue depth (growing queue indicates processing backlog), API Gateway throttle count (increasing throttles indicate capacity constraints), and bid-path service timeout rate (increasing timeouts indicate service degradation). Use these metrics to proactively scale services before they become auction-affecting bottlenecks. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) 
+  [ADVREL02-BP03 Avoid scale mismatch of both internal services and external partners](advrel02-bp03.md) 

 **Related documents:** 
+  [Implementing layers of admission control](https://aws.amazon.com/builders-library/implementing-health-checks/) 
+  [API Gateway Request Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) 

 **Related services:** 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 