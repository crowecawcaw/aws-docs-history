For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Migration Guide

This guide presents approaches for migrating time-series data from Amazon Timestream for LiveAnalytics to Amazon Timestream for InfluxDB 3 (recommended for most workloads), Amazon Timestream for InfluxDB 2 (for low-latency operational workloads), and to [Aurora](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.md") or [RDS PostgreSQL](../../../AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.md "../../../AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.md") (for non-time-series use cases) with an intermediate layer for [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/").

In this guide, we walk through following steps:

1. Export your data from Timestream for LiveAnalytics to Amazon S3.
2. Migrating to Amazon Timestream for InfluxDB 3 (recommended for most workloads).
3. Ingesting data to Amazon Timestream for InfluxDB 2.
4. Ingesting data to PostgreSQL.

###### Topics

- [Exporting Timestream data to Amazon S3](export-timestream-data.md "export-timestream-data.md")
- [Timestream for InfluxDB as a Target](timestream-influxdb-target.md "timestream-influxdb-target.md")
- [Aurora/RDS Postgres as a target](aurora-postgres-target.md "aurora-postgres-target.md")
