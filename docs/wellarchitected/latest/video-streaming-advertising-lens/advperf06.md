

# Real-time bidding and media delivery performance
<a name="advperf06"></a>

 When architecting advertising workloads, there are principles and practices that help you run efficient, high-performing cloud workloads. This capability focuses on optimizing real-time bidding systems and media delivery infrastructure where sub-millisecond to single-digit-millisecond latency determines competitive advantage. It covers chipset-agnostic design for Spot cost optimization, network protocol optimization, ARTF agent container performance, Prebid Server auction tuning, SGAI ad break latency optimization, real-time bid stream analytics pipelines, and contextual pre-classification at ingest time. 


|  ADVPERF06: How do you optimize real-time bidding and media delivery for sub-millisecond to single-digit-millisecond auction latency?  | 
| --- | 
| [ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost](advperf06-bp01.md) | 
| [ADVPERF06-BP02 Optimize your intake request format (HTTP/2 or HTTP/3) for faster processing](advperf06-bp02.md) | 
| [ADVPERF06-BP03 Optimize Agentic RTB Framework (ARTF) agent container performance for sub-millisecond to single-digit-millisecond latency](advperf06-bp03.md) | 
| [ADVPERF06-BP04 Optimize Prebid Server adapter concurrency and timeout budgets](advperf06-bp04.md) | 
| [ADVPERF06-BP05 Minimize SGAI ad break latency with CDN-cached manifests, pre-transcoded creatives, and scaled ADS](advperf06-bp05.md) | 
| [ADVPERF06-BP06 Architect real-time bid stream processing pipeline for publisher yield analytics](advperf06-bp06.md) | 
| [ADVPERF06-BP07 Pre-classify publisher content for contextual targeting at ingest time](advperf06-bp07.md) | 

## Capability intent
<a name="advperf06-capability-intent"></a>
+  Your advertising workloads use chipset-agnostic design (AMD and Intel x86 compatibility) to consistently select the lowest-cost Spot Instance option available. 
+  Ad creative assets and VAST XML responses are delivered over HTTP/3 with QUIC, avoiding TCP head-of-line blocking during parallel asset fetches. 
+  ARTF agent containers complete bid processing within sub-millisecond to single-digit-millisecond budgets through pre-allocated memory pools, compiled model formats, and optimized gRPC connections. 
+  Prebid Server runs with per-adapter circuit breakers, parallel fan-out, and per-adapter timeout budgets that maximize bid density within the auction window. 
+  SGAI ad break latency is minimized through CDN-cached manifests, pre-transcoded creatives, and colocate ad decision servers with VAST response caching. 
+  Bid-level yield data is available for query within 60 seconds of auction completion through a dedicated streaming analytics pipeline that runs independently of the auction hot path. 
+  Publisher content is classified for contextual targeting at ingest time, removing classification latency from the auction path entirely. 

## Common issues to watch for
<a name="advperf06-common-issues-to-watch-for"></a>
+  Hard-coding a specific x86 chipset (AMD or Intel) in launch templates, locking the workload into a single Spot pricing pool. 
+  Serving ad creatives over HTTP/2 without HTTP/3, missing the head-of-line blocking removal that QUIC provides for parallel VAST asset delivery. 
+  Running ARTF agents that allocate memory per bid request and load ML models on first invocation, incurring heap allocation and cold model loading overhead on the auction deadline path. 
+  Running Prebid Server with all adapters sharing a single connection pool, allowing one slow adapter to starve healthy adapters of connections. 
+  Generating viewer-specific SSAI manifests for FAST channels instead of CDN-cacheable SGAI manifests, forcing origin-level manifest generation for every viewer. 
+  Running contextual classification synchronously during bid evaluation, adding 50–200 ms to the auction path for content that could have been pre-classified at ingest. 