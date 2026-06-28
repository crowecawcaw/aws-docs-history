For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# General FAQ for Amazon Timestream for InfluxDB 3

Common questions about Amazon Timestream for InfluxDB 3, its architecture, editions, and regional availability. For a full overview, see [What is Timestream for InfluxDB 3?](influxdb3.md#what-is-timestream-for-influxdb-3 "influxdb3.md#what-is-timestream-for-influxdb-3").

**What is Amazon Timestream for InfluxDB 3?**

Amazon Timestream for InfluxDB 3 is a managed time-series database service that runs InfluxDB 3 on AWS. It is designed for large-scale time-series analytics using open-source APIs. The service handles provisioning, patching, backups, and software updates so you can focus on your applications.

**How is InfluxDB 3 different from InfluxDB v2?**

InfluxDB 3 is a complete architectural redesign. It replaces the TSM (Time-Structured Merge tree) storage engine with Apache Arrow for in-memory processing, Apache DataFusion for query execution, and Apache Parquet for columnar storage on Amazon S3. This enables better performance for high-cardinality data and more efficient scaling for analytical workloads.

**What is the difference between Core and Enterprise editions?**

Core is a cost-effective, single-node edition optimized for real-time monitoring of recent data, typically around 3 days. It does not include compaction or multi-node deployments, which means query performance degrades as data ages. Core is best suited for dashboards, real-time alerting, and development or proof-of-concept workloads.

Enterprise is designed for production workloads that require high availability and long-term data retention. Key differences include:

- **Compaction** – Enterprise includes compaction capabilities that maintain query performance over time by optimizing Parquet file organization. Without compaction, Core accumulates small files that slow down queries on older data.
- **Multi-node clusters** – Enterprise supports multi-node deployments across multiple Availability Zones with dedicated ingest, query, and compactor nodes. Core is limited to a single node.
- **Read replicas** – Enterprise supports query-only nodes to scale read-heavy workloads independently from ingest.
- **Historical queries** – Enterprise includes single series indexing for optimized long-term data analysis, making it suitable for months or years of data retention.

Choose Core for near real-time monitoring where cost is a priority. Choose Enterprise when you need high availability, compaction, or long-term data analysis.

Core vs Enterprise Feature Comparison| Feature | Core | Enterprise |
| --- | --- | --- |
| Deployment | Single-node | Multi-node across AZs |
| Compaction | Not included | Included |
| Read replicas | Not available | Query-only node scaling |
| Historical queries | Limited (~3 days) | Months/years with indexing |
| High availability | Single node | Multi-AZ |
| Best for | Dev/test, real-time dashboards | Production, long-term analytics |

**Which AWS Regions support Amazon Timestream for InfluxDB 3?**

For the current list of supported AWS Regions and endpoints, see [Amazon Timestream endpoints and quotas](../../../general/latest/gr/timestream.md "../../../general/latest/gr/timestream.md") in the AWS General Reference.
