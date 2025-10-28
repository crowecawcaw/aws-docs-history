For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Core and Enterprise versions in Timestream for InfluxDB 3

Amazon Timestream for InfluxDB 3 is available in two versions: Core and Enterprise. Both versions
are built to collect, process, transform, and store event and time-series data, and are ideal for
use cases that require real-time ingest and fast query response times to build user interfaces,
monitoring, and automation solutions.

## Common use cases

Both Core and Enterprise versions are optimized for scenarios where near real-time data
monitoring is essential and queries need to return quickly to support user experiences such as
dashboards and interactive user interfaces. Common use cases include:

- Monitoring sensor data
- Server monitoring
- Application performance monitoring
- Network monitoring
- Financial market and trading analytics
- Behavioral analytics

## Core version

InfluxDB 3 Core is based on the InfluxDB 3 open source release and provides a
cost-effective solution for real-time time-series data processing.

Core feature highlights:

- Diskless architecture with Amazon S3 object storage support.
- Fast query response times (under 10ms for last-value queries, or 30ms for distinct
  metadata queries).
- Embedded Python VM for plugins and triggers .
- Parquet file persistence for efficient storage and querying.
- Full compatibility with InfluxDB 1.x and 2.x write APIs.
- Limited to single-node deployments.

Limitations:

- Lacks compaction capabilities, which impacts performance over time.
- Best suited for workloads focused on recent data (typically a few days old).
- Not recommended for use cases involving long-term storage and analysis.

## Enterprise version

InfluxDB 3 Enterprise builds upon Core with additional features designed for demanding
production workloads, high availability, and long-term data retention.

Enterprise adds the following features to Core:

- **Historical query capability and single series indexing** for
  optimized long-term data analysis.
- **High availability** through multi-node cluster configurations.
- **Read replicas** for scaling read-heavy workloads.
- **Compaction capabilities** essential for maintaining performance
  over time.
- Support for **multi-node deployments** (up to 3 nodes
  initially, with future expansion capabilities).
- **Enhanced security** (coming soon).
- **Row-level delete support** (coming soon).
- **Integrated admin UI** (coming soon) - Note: Currently, you can
  use the InfluxDB Explorer downloaded from [https://docs.influxdata.com/influxdb3/explorer/](https://docs.influxdata.com/influxdb3/explorer/ "https://docs.influxdata.com/influxdb3/explorer/").

## Choosing between Core and

Enterprise

Choose Core when:

- Your workload focuses on near real-time monitoring of recent data.
- Single-node deployment meets your availability needs.
- Cost optimization is a primary concern.
- You don't require long-term data retention.
- Doing development, testing, or proof-of-concept work to explore engine capabilities.

Choose Enterprise when:

- You need to store and analyze historical data beyond a few days.
- High availability and read scaling are requirements.
- You need compaction to maintain long-term performance.
- Production workloads demand enhanced reliability and scalability.
- You require multi-node deployments for better performance distribution.

Both versions leverage Amazon Timestream for InfluxDB's managed service benefits, including
automated backups, software updates, and integration with AWS services, while providing the
flexibility to choose the feature set that best matches your workload requirements.
