

# ADVPERF06-BP06 Architect real-time bid stream processing pipeline for publisher yield analytics

 Make bid-level yield data, such as win rate, CPM by SSP, and fill rate, available for query within 60 seconds of auction completion, so teams can adjust floor prices dynamically. Dedicate a streaming pipeline to yield analytics that runs independently of the auction hot path so analytics compute doesn't compete with bid evaluation for resources. 

 **Desired outcome:** 
+  Bid-level yield data is available for query within 60 seconds of auction completion, enabling dynamic floor price adjustments. 
+  The analytics pipeline is decoupled from the auction hot path, so analytics compute doesn't introduce latency or resource competition into bid evaluation. 
+  Floor prices are refreshed based on trailing yield data every 5 minutes, enabling responsive yield optimization. 

 **Common anti-patterns:** 
+  Batch-processing bid logs hourly, which limits intra-day floor price responses to demand changes. 
+  Storing raw bid events without pre-aggregation. 
+  Running analytics queries against the same datastore serving live auction lookups, where they compete for read capacity with latency-sensitive bid evaluation. 

 **Benefits of establishing this best practice:** 
+  A dedicated streaming pipeline decouples analytics compute from the auction hot path, enabling sub-minute yield visibility without affecting bid response latency. 
+  Real-time floor price adjustments based on trailing yield data optimize publisher revenue by responding to demand changes within minutes rather than hours. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Yield analytics and bid evaluation have different latency and compute requirements. Bid evaluation requires sub-millisecond to single-digit-millisecond response times with deterministic resource access. Yield analytics requires data freshness measured in seconds to minutes with complex aggregations across millions of bid events. Running both on the same infrastructure creates interference: analytics queries consume read capacity needed for bid evaluation, and analytics compute latency introduces variability into the auction path. 

 Separating the two workloads means one write path feeding independent readers, and it works only when neither reader can affect the other's capacity. A single ingestion point keeps both views derived from the same events, which is why a real-time yield figure and a historical report agree. Independent consumption keeps a heavy historical query from competing with the pipeline the auction depends on. 

 The events describing one auction don't arrive together. A bid response and its outcome are separated in time, arrival order doesn't match occurrence order, and aggregation grouped by arrival time attributes activity to the wrong interval. When you group by when an event occurred rather than when it was received, the win rate becomes trustworthy, but you also have to decide how long to wait for stragglers. Waiting longer produces a more complete window while delaying every downstream decision by that same interval. 

 Duplicate delivery is another correctness hazard, and it's important because the aggregate feeds a pricing decision. A double-counted win inflates a win rate, which raises a floor and suppresses demand. Configure exactly-once semantics through the aggregation stage. 

 Serving the result back to the auction is a separate problem from computing it. Treating them as one puts analytics infrastructure on the critical path. Don't read from the store optimized for aggregation and history during bid evaluation, because the auction can afford neither its latency nor its variability. Instead, populate a tier the auction can read cheaply, asynchronously from the pipeline, so bid evaluation doesn't pay pipeline latency on every request. This adds one more place the value can go stale, so include the propagation delay in your freshness budget. 

 The pipeline can also fall behind without signaling a problem. Floor prices keep being read and keep looking valid while they describe conditions that have already changed, and the auction reports no error. Monitor pipeline lag as a health signal in this case. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Stream bid events from Prebid Server to [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/):** Configure Prebid Server to publish bid events (bid request metadata, response, and outcome) to a Kinesis Data Stream using per-SSP partition keys to preserve ordering and parallelize processing. Set the shard count based on your peak bid QPS (each shard handles approximately 1,000 records/second). Use the Kinesis Producer Library (KPL) for efficient batching and retry. 

1.  **Process with Amazon Managed Service for Apache Flink for rolling aggregations:** Deploy a Flink application that consumes the Kinesis stream and computes rolling 5-minute aggregates of win rate, average CPM, fill rate, and timeout rate per SSP adapter. Use Flink's event-time processing with watermarks to handle out-of-order bid events. Configure exactly-once processing semantics to avoid double-counting of bid events during recovery. Configure the watermark strategy with a bounded out-of-orderness buffer AND with idleness detection, because a quiet Kinesis shard stalls watermark advancement for the whole application and silently holds every window open. 

1.  **Write aggregated metrics to DynamoDB (hot path) and S3 (cold path):** From the Flink application, write aggregated yield metrics to DynamoDB (keyed by SSP adapter \+ time window) for the floor price read path, and to [Amazon S3](https://aws.amazon.com/s3/) in Parquet format for historical analysis through [Amazon Athena](https://aws.amazon.com/athena/). DynamoDB provides sub-millisecond reads for real-time floor price lookups. S3/Athena provides cost-effective historical analysis. 

1.  **Feed aggregated signals back to Prebid Server floor price module through ElastiCache:** Deploy a Lambda function triggered by DynamoDB Streams that propagates updated floor price signals to [Amazon ElastiCache](https://aws.amazon.com/elasticache/). Configure Prebid Server's floor price module to read floor prices from ElastiCache (sub-millisecond reads) rather than DynamoDB directly. Update floor prices every 5 minutes based on trailing win-rate and CPM trends from the Flink aggregations. 

1.  **Monitor pipeline freshness and lag:** Publish Flink pipeline lag (difference between event time and processing time) as a CloudWatch custom metric. Set alarms when pipeline lag exceeds 60 seconds. This indicates the pipeline isn't meeting the freshness target for dynamic floor price adjustments. Also monitor Kinesis GetRecords.IteratorAgeMilliseconds to detect consumer processing falling behind the stream. 

## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Maintain best practices for Managed Service for Apache Flink applications](https://docs.aws.amazon.com/managed-flink/latest/java/best-practices.html) 
+  [Implement fault tolerance in Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/how-fault.html) 
+  [Build a Real-time Stream Processing Pipeline with Apache Flink on AWS](https://aws.amazon.com/blogs/big-data/build-a-real-time-stream-processing-pipeline-with-apache-flink-on-aws/) 
+  [Amazon Managed Service for Apache Flink FAQs: ad tech use cases](https://aws.amazon.com/managed-service-apache-flink/faqs/) 
+  [Querying data in Amazon S3 with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying.html) 

 **Related services:** 
+  [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) 
+  [Amazon Managed Service for Apache Flink](https://aws.amazon.com/managed-service-apache-flink/) 
+  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) 
+  [Amazon Athena](https://aws.amazon.com/athena/) 