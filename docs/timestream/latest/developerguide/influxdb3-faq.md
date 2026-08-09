For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Amazon Timestream for InfluxDB 3 frequently asked questions

Amazon Timestream for InfluxDB 3 is a fully managed time-series database service on AWS built on Apache Arrow, Apache DataFusion, and Apache Parquet. It supports SQL and InfluxQL queries, line protocol writes, and is available in Core (single-node, real-time monitoring) and Enterprise (multi-node, compaction, high availability) editions. This section answers the most common questions organized by topic.

**General**
What Amazon Timestream for InfluxDB 3 is, how it differs from v2, Core vs Enterprise editions, regional availability, and event notifications.

**Clusters and instances**
Instance types from db.influx.medium to db.influx.24xlarge, creating clusters, multi-node Enterprise deployments, scaling, cluster endpoints, and maintenance windows.

**Writing and querying data**
Write APIs (v3, v2, v1 compatibility), SQL and InfluxQL query support, token-based authentication, line protocol format, and data plane administration.

**Configuration and parameter groups**
Creating and managing parameter groups, immutable parameters, cloning best practices, and instance-size tuning guidelines.

**Schema design**
Tags vs fields, high-cardinality handling, and schema design best practices for InfluxDB 3.

**Processing engine**
Running Python plugins inside your cluster with write, schedule, and request triggers.

**Custom plugins**
Running your own Python plugins from public and private repositories: parameter group setup, repository access secrets, multi-repository configurations, and troubleshooting.

**Storage and billing**
Decoupled compute/storage architecture on Amazon S3, billing components, automatic backups, and customer-managed backup and restore.

**Security and access**
VPC deployment, AWS Identity and Access Management access control, customer managed encryption keys (CMK), and managed security policies.

###### Topics

- [General](faq-general.md "faq-general.md")
- [Clusters and instances](faq-clusters.md "faq-clusters.md")
- [Writing and querying data](faq-data-operations.md "faq-data-operations.md")
- [Configuration and parameter groups](faq-configuration.md "faq-configuration.md")
- [Schema design](faq-schema-design.md "faq-schema-design.md")
- [Processing engine](faq-processing-engine.md "faq-processing-engine.md")
- [Custom plugins](faq-custom-plugins.md "faq-custom-plugins.md")
- [Storage and billing](faq-storage-billing.md "faq-storage-billing.md")
- [Security and access](faq-security.md "faq-security.md")
