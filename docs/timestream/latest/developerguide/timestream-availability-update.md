For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Amazon Timestream for LiveAnalytics availability change

Since time-series applications have unique requirements and characteristics, we offer a broad framework to help you evaluate various alternatives before diving into specific implementation details. This high-level guidance serves as a foundation for your decision-making process, with more detailed steps and practical implementations to be covered in subsequent sections.

## Alternative services evaluation

**Large-scale analytics, high cardinality, or new workloads (recommended)**

We recommend [Amazon Timestream for InfluxDB 3 Enterprise](influxdb3.md "influxdb3.md") for most LiveAnalytics migrations. InfluxDB 3 is built on Apache Arrow, DataFusion, and Parquet with Amazon S3 object storage, supporting unlimited cardinality, standard SQL and InfluxQL queries, multi-node clusters (up to 15 nodes), and a built-in Python processing engine. It is the recommended target for workloads with more than 1 million series, complex analytical queries, or any new greenfield deployment.

**Low-latency operational monitoring (less than 1 million series)**

We recommend [Amazon Timestream for InfluxDB 2](timestream-for-influxdb.md "timestream-for-influxdb.md"), if your Timestream for LiveAnalytics table has less than 10 million cardinality ([series keys](https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/#series "https://docs.influxdata.com/influxdb/v2/reference/key-concepts/data-elements/#series")), meaning the unique combinations of [Amazon Timestream for LiveAnalytics concepts](concepts.md "concepts.md") or if you can reduce your table's cardinality under 10 million. Amazon Timestream for InfluxDB 2 provides single-instance or Multi-AZ deployments with single-digit millisecond query response times, [Flux](https://docs.influxdata.com/influxdb/v2/query-data/flux/ "https://docs.influxdata.com/influxdb/v2/query-data/flux/") and [InfluxQL](https://docs.influxdata.com/influxdb/v2/query-data/influxql/ "https://docs.influxdata.com/influxdb/v2/query-data/influxql/") query support, and tasks (equivalent to [Scheduled queries](scheduled-query.md "scheduled-query.md")).

**Prefer using SQL instead of InfluxQL**

Amazon Timestream for InfluxDB 3 supports native SQL (standard SQL via Apache DataFusion) as well as InfluxQL.
If your LiveAnalytics workloads use SQL, Amazon Timestream for InfluxDB 3 is the direct migration path—there
is no need to move to any other SQL based engine. InfluxDB 3's SQL implementation
is purpose-built for time-series data with optimized time-based functions, GROUP BY time intervals,
and columnar storage that outperforms general-purpose relational databases for time-series
analytics.

**Require high-scale data ingestion (exceeding 1 million records per second)**

While Amazon Timestream for InfluxDB 3 Enterprise is built for large-scale time-series workloads, a single
cluster cannot currently support more than 1 million records per second. For workloads exceeding
this threshold, data would need to be sharded across multiple InfluxDB 3 clusters. If sharding
is not an option, NoSQL engines like Amazon DynamoDB could be a good alternative for use cases
that involve low complexity analytics.

Before beginning your data migration to the chosen alternate AWS service, it is crucial to assess several key factors that will significantly influence your migration strategy and its ultimate success. These evaluations will help shape your approach, identify potential challenges, and ensure a smoother transition during the migration process.

**Data selection and retention considerations**

Assess your data migration scope by defining exact retention requirements. Consider whether you need to migrate the complete historical dataset, recent data only (such as the last 30, 60, or 90 days), or specific time-series data segments. This decision should be guided by three key factors: regulatory compliance requirements, analytical needs of your business, and practical considerations around migration complexity and costs.

**Query pattern compatibility analysis**

While Amazon Timestream for InfluxDB 3 supports SQL, the SQL dialect does not match LiveAnalytics 1:1. Thorough
testing of all business-critical queries is required before migration. We recommend running
your existing query set against InfluxDB 3 in a dev cluster to identify syntax differences
and validate performance meets your requirements.

**Data transformation planning**

Before migrating, pay close attention to schema mapping to ensure proper data alignment and structural consistency between source and target systems, and accurate data type conversions specifically tailored for time-series data. These components work together to ensure data quality, optimize performance, and maintain functionality across different system architectures. In addition, consider any specialized indexing patterns and system-specific optimizations to guarantee efficient data access and retrieval.

**Continuity and downtime management**

Since data migration inherently causes operational disruption, developing a comprehensive switchover strategy is crucial for success. Few best practices to consider in the migration plan to minimize downtime are:

- Implement temporary parallel processing systems where possible to maintain business continuity.
- Schedule migrations during low-traffic periods such as weekends or overnight hours.
- Establish well-tested rollback procedures for quick recovery in case of unexpected issues.
