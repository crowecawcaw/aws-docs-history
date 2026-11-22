

# Scenario 2: Data pipelines architecture

 Advertising analytics systems ingest, transform, and analyze petabytes of bid events, impressions, clicks, and conversion data. They support campaign measurement, audience intelligence, attribution modeling, and real-time reporting across multiple downstream consumers with different latency requirements. 

## Characteristics
<a name="s02-characteristics"></a>
+  Massive data volumes of up to 100 petabytes, with high throughput up to 1 trillion events per week. 
+  Mixed latency tiers: real-time pacing (sub-second), audience segmentation (minutes), attribution (hours), historical analytics (batch). 
+  Multiple downstream consumers (data warehouse, reporting, ML training, and real-time decisioning), each with different latency and consistency requirements. 
+  Data privacy regulations require geographic data residency and strict retention policies (event-level data retained less than 30 days). 
+  Need for high availability in data pipelines to support critical advertising workloads. 
+  Enabling advanced use cases like machine learning for advertising performance measurement and attribution modeling. 
+  Maintaining operational efficiency with managed services as engineering team sizes may not keep up with data growth. 

## Reference architecture
<a name="s02-reference-architecture"></a><a name="scenario-02-fig1"></a>

![Analytics logical architecture showing ingestion, data processing, lakehouse storage, data warehouse, and reporting layers for an advertising analytics platform](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-02a-analytics-logical-architecture.jpg)

*Advertising analytics logical architecture*


 The architecture consists of the following components: 

1.  **Ingestion module**: Web servers ingest clickstream and event data from ad servers, DSPs, SSPs, and measurement SDKs. Amazon Kinesis Data Streams captures high-throughput real-time events. Amazon Data Firehose de-aggregates and delivers to Amazon S3. 

1.  **Data processing module**: Amazon EMR Serverless runs Apache Spark applications that transform ingested data into the solution data model. Amazon Managed Service for Apache Flink handles real-time stream processing (rolling aggregations, frequency cap updates, real-time yield analytics). 

1.  **Landing zone (Amazon S3)**: Raw data in Apache Parquet format with Snappy compression, partitioned by date, campaign ID, and geography. AWS Glue Data Catalog maintains the schema registry. S3 Intelligent-Tiering automatically optimizes storage costs based on access patterns. 

1.  **Data lake with lakehouse**: AWS Glue ETL transforms raw data into the lakehouse using Apache Iceberg tables. Supports both batch processing and real-time incremental updates. Amazon Athena provides ad-hoc SQL querying. 

1.  **Data warehouse (Amazon Redshift)**: Serves structured campaign metrics queries, pre-computed aggregations, and BI workloads requiring fast response times. Supports both provisioned and Redshift Serverless deployment modes. 

1.  **Reporting module (Quick)**: Provides out-of-the-box dashboards for campaign performance, audience analytics, and attribution reporting. Connects to both Redshift (structured metrics) and Athena (ad-hoc analysis). 

1.  **Attribution and event-level store (Amazon DynamoDB)**: Near-real-time store for event-level data requiring fast lookups. Used for active campaign frequency capping and in-flight pacing. DynamoDB TTL expires bid event records after 30 days. 

1.  **AWS Key Management Service (AWS KMS)**: Encrypts data at rest in Kinesis, S3, DynamoDB, and Redshift. Maintains encryption key audit trails for compliance. <a name="scenario-02-fig2"></a>

![Advertising data pipeline architecture on AWS showing the flow from data ingestion through processing, lakehouse storage, and analytics consumption layers](https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/images/scenario-02b-data-pipeline-architecture.jpg)

*Advertising data pipeline architecture on AWS*


## Configuration notes
<a name="s02-configuration-notes"></a>

### Ingestion
<a name="ingestion"></a>

 Configure Amazon Kinesis Data Streams with the Kinesis Producer Library (KPL) for batching and retry. Route events through VPC interface endpoints to avoid internet egress charges. Configure Amazon Data Firehose with dynamic partitioning to route events to the correct S3 prefix by date, campaign, and data type without custom Lambda transformation. 

### Processing
<a name="processing"></a>

 Use Amazon EMR Serverless for Spark-based batch processing. It requires no cluster management and scales to zero between jobs, which reduces costs significantly. For micro-batch processing (5-minute intervals for audience segmentation), use Amazon Managed Service for Apache Flink with at-least-once processing guarantees and DynamoDB deduplication. 

### Storage
<a name="storage"></a>

 Convert all data to Apache Parquet with Snappy compression before writing to S3. This typically achieves 5–10x size reduction compared to raw JSON, which directly reduces both storage costs and Athena query scan costs. Partition by year=YYYY/month=MM/day=DD/campaign\_id=XXX to enable partition pruning in Athena queries. Enable S3 Object Lock in governance mode on raw event archives to guard against tampering. 

### Data classification and retention
<a name="data-classification-and-retention"></a>

 Aggregate analytics data in the primary region before cross-region transfer when business requirements demand centralization. Apply DynamoDB TTL and S3 lifecycle policies to enforce 30-day retention for event-level data containing user signals. Use Amazon Macie for ongoing PII discovery across all data stores. Retain only aggregated, anonymized data beyond the 30-day window. 

### Clickstream analytics reference
<a name="clickstream-analytics-reference"></a>

 For detailed clickstream analytics pipeline guidance including specific component configuration, see the [Guidance for Clickstream Analytics on AWS](https://aws.amazon.com/solutions/guidance/clickstream-analytics-on-aws/). 