

# Scenario 9: Implementation of Prebid Server on AWS

 Prebid Server provides server-side header bidding orchestration that solves the traditional programmatic waterfall challenges of yield leakage, demand opacity, and last-look advantages. It sends parallel bid requests to all demand partners concurrently, giving every bidder equal opportunity to compete and maximizing publisher yield. 

## Characteristics
<a name="s09-characteristics"></a>
+  Publisher wants concurrent auctions across 10–20 SSP/DSP demand partners with no sequential waterfall priority. 
+  Auction must complete within a publisher-configured timeout (typically 100–300 ms) regardless of individual adapter performance. 
+  Auction success rate must remain above 95% even when up to 30% of adapters are unavailable. 
+  Yield analytics (win rate, CPM by adapter, fill rate) must be available within 60 seconds for dynamic floor price adjustments. 
+  Identity signal resilience across multiple frameworks (UID2, LiveRamp, and ID5) is needed as the industry transitions away from third-party cookies. 
+  Publisher needs full ownership of auction logic, bidder configuration, and transaction data, with no opaque third-party control. 

## Reference architecture
<a name="s09-reference-architecture"></a><a name="scenario-09-fig1"></a>

![Prebid Server implementation on AWS, part 1, showing the auction orchestration layer on EKS with Karpenter, per-adapter isolation, and bid response caching](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-09-prebid-server-1.jpg)

*Prebid Server implementation on AWS, part 1*


 The architecture consists of the following components: 

1.  **Application Load Balancer**: Distributes incoming publisher ad requests to Prebid Server pods. Configured with auction-engine health checks (validates that the auction engine is responsive, not just that the container is running). Cross-zone load balancing enabled for even distribution across Availability Zones. 

1.  **Amazon EKS (Prebid Server pods)**: Prebid Server containers deployed across at least 2 Availability Zones with pod anti-affinity rules that enforce Availability Zone distribution. Karpenter handles fast node provisioning for traffic spikes (typically under 60 seconds for new nodes). KEDA scales pod count based on bid request queue depth published to Amazon Managed Service for Prometheus. 

1.  **Per-adapter circuit breakers**: Resilience4j CircuitBreaker per adapter with 50% failure rate threshold over 30-second window. Per-adapter bounded HTTP connection pools (50–200 concurrent connections) guard against one degraded adapter starving others. Per-adapter timeout set at 80% of the global auction timeout. 

1.  **Amazon ElastiCache Serverless**: Bid response cache keyed by impression context (content genre, viewer segment, daypart) with 5-second TTL. Cached bids reduce redundant adapter fan-out for recurring ad pod contexts. Also stores dynamic floor prices refreshed every 5 minutes from the yield analytics pipeline. Target 60%\+ cache hit ratio for recurring contexts. 

1.  **Amazon Kinesis Data Streams**: Receives bid events (bid request metadata, response, and outcome) from Prebid Server with per-SSP partition keys for ordered, parallelized processing. Decoupled from the auction hot path, so analytics can't impact bid response latency. 

1.  **Amazon Managed Service for Apache Flink**: Processes Kinesis bid event stream with rolling 5-minute windowed aggregations: win rate, average CPM, fill rate per SSP adapter. Handles out-of-order bid events using event-time processing. Publishes results to both DynamoDB (hot path for floor price reads) and S3 (cold path for historical analysis through Athena). 

1.  **Amazon DynamoDB (floor prices)**: Stores per-SSP floor price signals updated every 5 minutes from Flink aggregations. Prebid Server reads floor prices from DynamoDB (or ElastiCache as a faster caching layer) to apply dynamic floor pricing based on real-time yield data. 

1.  **Amazon S3 \+ Amazon Athena**: Long-term storage for bid event analytics in Parquet format. Athena provides ad-hoc analysis for adapter performance evaluation, yield optimization, and identity-signal effectiveness measurement. <a name="scenario-09-fig2"></a>

![Prebid Server implementation on AWS, part 2, showing the yield analytics streaming path from bid events through Kinesis and Flink to DynamoDB floor prices and S3 historical storage](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-09-prebid-server-2.jpg)

*Prebid Server implementation on AWS, part 2*


## Configuration notes
<a name="s09-configuration-notes"></a>

### Adapter management
<a name="adapter-management"></a><a name="scenario-09-fig3"></a>

![Prebid Server implementation on AWS, part 3, showing per-adapter circuit breakers, bounded HTTP connection pools, and per-adapter CloudWatch dashboards for timeout and eCPM monitoring](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-09-prebid-server-3.jpg)

*Prebid Server implementation on AWS, part 3*


 Configure per-adapter circuit breakers with 50% failure rate threshold, 30-second sliding window, and 15-second half-open probe interval. Build per-adapter CloudWatch dashboards tracking bid response rate, win rate, identity-signal match rate (per UID2/LiveRamp/ID5 framework), and eCPM contribution. Disable adapters where p99 latency consistently exceeds 90% of the timeout budget or marginal revenue falls below 1% of total auction revenue (typically cap active adapters at 10–12). 

### Dynamic floor prices
<a name="dynamic-floor-prices"></a>

 Configure the yield analytics pipeline to compute rolling 5-minute floor price recommendations based on trailing win-rate and CPM trends. When active adapter count drops below a configured threshold (for example, fewer than 3 healthy SSPs), temporarily increase floor prices to help protect publisher yield during reduced competition. Reset floor prices when adapter count recovers. 

### Identity signal resilience
<a name="identity-signal-resilience"></a>

 Publish header bidding timeout rates by adapter, bid request-to-response ratios per SSP, and identity-signal pass-through rates per SSP segmented by framework (UID2, LiveRamp, ID5, publisher first-party, and no-ID). Monitor for shifts in match rates that indicate partner-side integration issues rather than industry-wide signal loss. Use CloudWatch Anomaly Detection for eCPM contribution to detect demand partner degradation. 

### Graceful degradation
<a name="graceful-degradation"></a>

 Configure Prebid Server to execute the auction with whatever bid responses arrive within the timeout window, and never block on a single slow adapter. Maintain an ElastiCache-backed fallback creative cache per ad unit (1-hour TTL for display, 30-minute TTL for video). If the auction returns zero bids, serve the most recent cached creative rather than returning an empty slot. 

### Operational readiness
<a name="operational-readiness"></a>

 Before launching new SSP adapter integrations, validate: adapter timeout threshold configuration, bid response format compliance testing, yield baseline metrics captured over 24\+ hours of staging traffic. Deploy adapters with canary routing (5–10% traffic) before full rollout. Configure CloudWatch alarms for per-adapter timeout rate spikes and eCPM degradation. 