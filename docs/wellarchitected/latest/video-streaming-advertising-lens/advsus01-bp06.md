

# ADVSUS01-BP06 Keep yield analytics off the auction path so its compute scales with events, not traffic
<a name="advsus01-bp06"></a>

 Decouple yield analytics from the auction hot path so that analytics compute does not run synchronously in the bid evaluation path. A dedicated streaming pipeline makes bid-level yield data available within a minute of auction completion. 

 **Desired outcome:** 
+  Bid-level yield data is available for query within 60 seconds of auction completion through a dedicated streaming analytics pipeline. 
+  The analytics pipeline is fully decoupled from the auction hot path, so analytics compute failures never affect bid processing. 
+  Running analytics queries against the same datastore serving live auction lookups is avoided, so each store can be optimized for its specific workload. 

 **Common anti-patterns:** 
+  Yield analytics queries run against the same datastore that serves live auction floor-price lookups, which creates resource contention that inflates both auction latency and compute use. 
+  Batch-processing bid logs on an hourly cadence blocks intra-day floor-price response and forces publishers to react to yield shifts a full day late. 
+  Analytics compute runs continuously on clusters provisioned for peak query load, which consumes resources around the clock for queries that arrive intermittently. 
+  Over-provisioning a single datastore to satisfy both sub-millisecond auction reads and infrequent historical analysis wastes capacity on the access pattern it isn't optimized for. 

 **Benefits of establishing this best practice:** 
+  Streaming compute scales with event volume rather than running continuously, reducing the resources consumed when query demand is low. 
+  Separate hot and cold tiers let each store be right-sized for its workload, avoiding the resource overhead of over-provisioning one store for two access patterns. 
+  Analytics failures are isolated from the auction path, so a problem in the reporting pipeline never degrades live bidding. 
+  Publishers see bid-level yield metrics within a minute of auction completion, enabling intra-day floor-price adjustments. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A real-time auction runs under a hard response deadline, typically a few hundred milliseconds, and every component on that path competes for the same budget. On the auction path, run only what must complete before a bid returns. Route everything else to a separate pipeline that can fail, scale, or lag without affecting live bidding. A dedicated streaming pipeline applies this to yield analytics with little resource overhead: streaming compute scales with event volume and idles when no events arrive. Event latency is not a proxy for energy use. Track compute and memory utilization as the resource proxy. 

 Yield data has two access patterns. The floor-price module needs the freshest aggregates at single-digit-millisecond latency on every auction. Analysts read the same data infrequently and tolerate seconds of latency. Serving both patterns from one store over-provisions it for the more demanding pattern and leaves capacity idle for the other. Split the data by access pattern so each tier is sized for its real workload. The trade-off is added pipeline complexity and eventual consistency between tiers, acceptable here because floor-price decisions tolerate a few minutes of aggregation lag. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Stream bid events from Prebid Server to Kinesis with per-SSP partition keys:** Configure Prebid Server to publish bid events to Amazon Kinesis Data Streams using per-SSP partition keys. Size shards for peak bid QPS. This is the shared source for both real-time analytics and cold storage: write once, consume multiple times. 

1.  **Compute rolling 5-minute aggregates using Apache Flink:** Deploy a Managed Service for Apache Flink application that computes rolling 5-minute aggregates of win rate, average CPM, and fill rate per SSP adapter. Flink's event-time processing handles out-of-order events without over-processing. 

1.  **Use a hot-cold data split for different access patterns:** Write aggregated metrics to Amazon DynamoDB (hot path, single-digit-millisecond reads) and Amazon S3 (cold path, historical analysis through Amazon Athena). This right-sizes each store for its actual access pattern, avoiding the resource waste of over-provisioning a single store for peak query patterns. 

1.  **Feed floor price signals through ElastiCache:** Propagate floor price updates from DynamoDB to ElastiCache on a 5-minute cadence. Prebid Server reads floor prices from ElastiCache (sub-millisecond reads) rather than DynamoDB, reducing per-auction read latency and DynamoDB read unit consumption. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP08 Identify and remove redundant data across advertising storage infrastructure](advsus01-bp08.md) 

 **Related documents:** 
+  [Amazon Managed Service for Apache Flink documentation](https://docs.aws.amazon.com/managed-flink/latest/java/what-is.html) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 