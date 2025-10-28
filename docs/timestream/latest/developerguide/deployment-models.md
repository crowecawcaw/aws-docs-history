For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Deployment models in Timestream for InfluxDB 3

## Single-node deployment

In a single-node deployment (available for both Core and Enterprise versions), a single
instance handles all database operations. This configuration features:

- One node performing multiple critical roles:
  - Writer role: Handles all write operations to the database.
  - Reader role: Processes read queries and data retrieval operations.
  - Compactor role: Optimizes storage by compacting data files (Enterprise version only).

- Core version: Single node operates with writer and reader roles only.
- Enterprise version: Single node operates with writer, reader, and compactor roles for
  complete functionality.
- Simplified management with all operations consolidated on a single instance.
- Lower cost compared to multi-node deployments.
- Suitable for development, testing, or smaller production workloads.

Single-node deployments are ideal for getting started with Timestream for InfluxDB 3 or for
workloads with moderate performance requirements.

## Multi-node deployment

Multi-node deployments (available only for Enterprise version) distribute workloads across
multiple instances for improved performance, scalability, and availability. This configuration
offers:

- Flexible node allocation based on workload requirements:
  - 2 nodes that can handle both write and read operations.
  - 1 dedicated compactor node for optimizing storage.

- Horizontal scaling capabilities to accommodate growing workloads.
- Enhanced fault tolerance with workload distribution across multiple nodes in different
  Availability Zones.
- Improved query performance.
- Better handling of concurrent operations.

Multi-node deployments are recommended for production environments with high throughput
requirements, large data volumes, or the need for enhanced availability.
