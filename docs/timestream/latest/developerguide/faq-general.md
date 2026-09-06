

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# General FAQ for Amazon Timestream for InfluxDB 3
<a name="faq-general"></a>

Common questions about Amazon Timestream for InfluxDB 3, its architecture, editions, and regional availability. For a full overview, see [What is Timestream for InfluxDB 3?](influxdb3.md#what-is-timestream-for-influxdb-3).

**What is Amazon Timestream for InfluxDB 3?**  
Amazon Timestream for InfluxDB 3 is a managed time-series database service that runs InfluxDB 3 on AWS. It is designed for large-scale time-series analytics using open-source APIs. The service handles provisioning, patching, backups, and software updates so you can focus on your applications.

**How is InfluxDB 3 different from InfluxDB v2?**  
InfluxDB 3 is a complete architectural redesign. It replaces the TSM (Time-Structured Merge tree) storage engine with Apache Arrow for in-memory processing, Apache DataFusion for query execution, and Apache Parquet for columnar storage on Amazon S3. This enables better performance for high-cardinality data and more efficient scaling for analytical workloads.

**What is the difference between Core and Enterprise editions?**  
Core is a cost-effective, single-node edition optimized for real-time monitoring of recent data, typically around 3 days. It does not include compaction or multi-node deployments, which means query performance degrades as data ages. Core is best suited for dashboards, real-time alerting, and development or proof-of-concept workloads.  
Enterprise is designed for production workloads that require high availability and long-term data retention. Key differences include:  
+ **Compaction** – Enterprise includes compaction capabilities that maintain query performance over time by optimizing Parquet file organization. Without compaction, Core accumulates small files that slow down queries on older data.
+ **Multi-node clusters** – Enterprise supports multi-node deployments across multiple Availability Zones with dedicated ingest, query, and compactor nodes. Core is limited to a single node.
+ **Read replicas** – Enterprise supports query-only nodes to scale read-heavy workloads independently from ingest.
+ **Historical queries** – Enterprise includes single series indexing for optimized long-term data analysis, making it suitable for months or years of data retention.
Choose Core for near real-time monitoring where cost is a priority. Choose Enterprise when you need high availability, compaction, or long-term data analysis.    
**Core vs Enterprise Feature Comparison**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/timestream/latest/developerguide/faq-general.html)

**Which AWS Regions support Amazon Timestream for InfluxDB 3?**  
For the current list of supported AWS Regions and endpoints, see [Amazon Timestream endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/timestream.html) in the AWS General Reference.

**Does Amazon Timestream for InfluxDB 3 support event notifications?**  
Yes. Amazon Timestream for InfluxDB publishes events to Amazon EventBridge when clusters undergo state changes, including creation, scaling, parameter group updates, and maintenance. You can create EventBridge rules to route events to targets such as Lambda, Amazon SNS, Amazon SQS, or Amazon CloudWatch Logs. Events use source `aws.timestream-influxdb`. For details, see [Amazon EventBridge event notifications](influxdb3-eventbridge-events.md).

**Is there an additional charge for event notifications?**  
No. Publishing events to Amazon EventBridge is included at no additional Amazon Timestream for InfluxDB charge. Standard Amazon EventBridge pricing applies for rule evaluation and target delivery, and downstream target costs (such as Lambda invocations or Amazon SNS deliveries) follow their respective service pricing.

**In which Regions are event notifications available?**  
Event notifications are available in all AWS Regions where Amazon Timestream for InfluxDB is available. Events are published in the same Region as your database resource.

**Do I need to enable event notifications?**  
No. Events are published automatically for all Amazon Timestream for InfluxDB resources. You do not need to opt in or configure anything on the database side. To receive events, create an Amazon EventBridge rule that matches the events you want and routes them to a target.

**What types of operations generate events?**  
Events are generated for creation, deletion, compute scaling, storage scaling, port changes, parameter group updates, log delivery changes, maintenance window updates, reboots, node addition/removal, engine type conversion, and Multi-AZ/Single-AZ changes. Both successful completions and failures emit events.

**Can I filter events by cluster name or event type?**  
Yes. Amazon EventBridge supports content-based filtering on any event field. You can filter by `detail.SourceIdentifier` (cluster name), `detail.EventCategories` (creation, notification, maintenance, failure), `detail.EventID` (specific event type), or `detail-type` (instance vs. cluster events).

**How quickly are events delivered after an operation completes?**  
Amazon EventBridge provides at-least-once delivery with a 24-hour retry window. Events are emitted only when a workflow reaches a terminal state (success or failure), not when the operation starts. Under normal conditions events are delivered shortly after completion, but delivery timing depends on target availability and is not guaranteed within a specific timeframe.

**Can I send events to another AWS account?**  
Yes. You can configure Amazon EventBridge rules to forward events to an event bus in another account for centralized observability. Configure the target event bus to accept events from your source account.