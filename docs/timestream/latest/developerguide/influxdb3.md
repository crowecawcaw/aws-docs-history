For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Amazon Timestream for InfluxDB 3

## What is Timestream for InfluxDB 3?

Amazon Timestream for InfluxDB 3 is a managed time-series database service that makes it easy
for application developers and DevOps teams to run InfluxDB 3 databases on AWS for
large-scale time-series analytics applications using open-source APIs. With Amazon Timestream for
InfluxDB 3, you can easily set up, operate, and scale time-series workloads designed to handle
high-cardinality data and complex analytical queries.

InfluxDB 3 represents a complete architectural reimagining of the InfluxDB database
engine. Unlike versions 1 and 2, which utilized a Time-Structured Merge tree (TSM) storage
engine, InfluxDB 3 is built from the ground up on entirely different technology foundations.
This new version leverages Apache Arrow for in-memory data processing, Apache Data Fusion for
query execution, and a columnar storage format (Parquet) for data persistence in object
storage (Amazon S3). This architectural shift enables InfluxDB 3 to deliver enhanced performance
for high-cardinality data and scale efficiently for large analytical workloads. InfluxDB 3
architecture provides improved query performance and resource utilization for data-intensive
use cases.

Amazon Timestream for InfluxDB 3 gives you access to the capabilities of this next-generation
time-series database engine. The architectural transformation enables large scale time-series
analytics workloads and capitalizes on the compression, partitioning, and query optimization
capabilities inherent to the columnar Parquet storage format. By decoupling compute from
storage, InfluxDB 3 can scale to handle virtually unlimited data volumes while maintaining
cost efficiency.

Amazon Timestream for InfluxDB 3 can automatically back up your database and keep your database
software up to date with the latest version. As with all AWS services, there are no upfront
investments required, and you pay only for the resources you use.

### DB Clusters

A DB cluster is the fundamental building block of Timestream for InfluxDB 3. Unlike
traditional database instances, InfluxDB 3 uses a cluster-based architecture that separates
compute from storage, leveraging Amazon S3 for virtually unlimited, cost-effective data storage.

You can set up your InfluxDB 3 deployments in either Core or Enterprise versions:

#### Core Version

The Core version of InfluxDB 3 is limited to single-node cluster deployments and
lacks compaction capabilities, which impacts its suitability for certain workloads. Due to
these limitations, the Core version is primarily designed for near real-time workloads
focused on recent data (typically a few days old). It is not recommended for use cases
involving long-term storage and analysis, as performance will degrade over time without
compaction processes to optimize storage.

#### Enterprise Version

The Enterprise version of InfluxDB 3 supports multi-node cluster configurations and
includes essential compaction capabilities, enabling horizontal scaling for both read and
write operations. These multi-node deployments provide enhanced availability, improved
performance for concurrent queries, and greater overall system resilience. The compaction
functionality in the Enterprise version makes it suitable for high-cardinality data and
long-term analytics use cases, as it continuously optimizes the underlying storage format.
Enterprise clusters can be scaled by adding nodes to accommodate growing workloads
without disrupting ongoing operations.

Each DB cluster has a DB cluster identifier. This auto-generated name uniquely
identifies the DB cluster when interacting with the Amazon Timestream for InfluxDB API and AWS CLI
commands. The DB cluster identifier is unique for that customer in an AWS Region.

Timestream for InfluxDB allocates a DNS endpoint for your cluster. The service-generated
identifier forms part of the DNS endpoint of the cluster. For example, if the cluster's
service-generated identifier is `xghozx1v79`, then the DNS endpoint is
`xghozx1v79-3ksj4dla5nfjhi.timestream-influxdb3.us-east-1.on.aws`.

Amazon Timestream for InfluxDB 3 allows you to create a master user account and password for
your DB cluster as part of the creation process. This master user has permissions to
create datababses, tables, and to perform read, write, delete and upsert operations on
your data.

To access a visual, web-based user interface, you can use the InfluxDB Explore, which
can be downloaded from [InfluxData](https://docs.influxdata.com/influxdb3/explorer/ "https://docs.influxdata.com/influxdb3/explorer/") and run on your own instances.

#### DB Cluster Classes

The DB cluster class determines the computation and memory capacity of nodes within
your Amazon Timestream for InfluxDB 3 clusters. The appropriate cluster class depends on your
processing power and memory requirements.

##### InfluxDB 3 Cluster Classes

InfluxDB 3 clusters use instance classes specifically optimized for the
Amazon S3-based storage architecture. These classes, designated as
`db.influxIOIncluded`, are designed to balance compute resources with the
I/O requirements of working with object storage. The `db.influxIOIncluded`
compute instances are priced to already include all I/O operations performed against
Amazon S3, providing customers with predictable costs regardless of their specific I/O
patterns.

The following table shows the hardware details for InfluxDB 3 cluster node classes:

| **Instance Class**           | **vCPU** | **Memory (GiB)** | **Storage Type**  | **Network bandwidth (Gbps)** |
| ---------------------------- | -------- | ---------------- | ----------------- | ---------------------------- |
| db.influxIOIncluded.medium   | 1        | 8                | S3 Object Storage | 12                           |
| db.influxIOIncluded.large    | 2        | 16               | S3 Object Storage | 12                           |
| db.influxIOIncluded.xlarge   | 3        | 32               | S3 Object Storage | 15                           |
| db.influxIOIncluded.2xlarge  | 8        | 64               | S3 Object Storage | 20                           |
| db.influxIOIncluded.4xlarge  | 16       | 128              | S3 Object Storage | 25                           |
| db.influxIOIncluded.8xlarge  | 32       | 256              | S3 Object Storage | 30                           |
| db.influxIOIncluded.12xlarge | 48       | 384              | S3 Object Storage | 22.5                         |
| db.influxIOIncluded.16xlarge | 64       | 512              | S3 Object Storage | 30                           |
| db.influxIOIncluded.24xlarge | 96       | 768              | S3 Object Storage | 40                           |

The `db.influxIOIncluded` instance classes are specifically designed to:

1. Efficiently manage the I/O operations between compute nodes and Amazon S3 object
   storage.
2. Provide optimal memory-to-CPU ratios for processing time-series data using the
   Apache Arrow framework.
3. Support the computational requirements of the Data Fusion query engine.

For Enterprise deployments with multi-node clusters, all nodes use the same
instance class to ensure balanced performance across the cluster. As your workload
grows, you can scale up by selecting a larger instance class for all nodes in the
cluster or scale out by adding more nodes of the same class to your cluster.

##### Hardware specifications

for DB cluster classes

The following terminology describes the hardware specifications for DB cluster
classes:

- **vCPU** – The number of virtual central
  processing units (CPUs). A virtual CPU is a unit of capacity that you can use to
  compare DB cluster classes.
- **Memory (GiB)** – The RAM, in gibibytes,
  allocated to the DB cluster node. There is often a consistent ratio between memory
  and vCPU.
- **Storage Type** – InfluxDB 3 uses S3 Object
  Storage, which is separate from the compute nodes.
- **Network bandwidth** – The network speed
  relative to other DB cluster classes.

#### DB Cluster Storage

Amazon Timestream for InfluxDB 3 introduces a different storage architecture that decouples
compute from storage by leveraging Amazon S3 for object storage. This architecture provides
virtually unlimited storage capacity while keeping cost under control in large-scale
deployments.

##### InfluxDB Object Storage

InfluxDB 3 clusters use a single storage class called InfluxDB Object Storage,
which is built on Amazon S3. This storage option offers:

- Virtually unlimited storage capacity
- Cost-efficient storage for large data volumes (up to 75% savings for
  deployments exceeding 16TB compared to InfluxDB 2.x)
- Durability of 99.999999999% (11 nines)
- Data stored in the columnar Parquet format for efficient compression and query
  performance

Unlike traditional database architectures where storage is directly attached to
compute nodes, InfluxDB 3's object storage is shared across all nodes in the cluster.
Each node maintains local in-memory caches for frequently accessed data to optimize
query performance while the underlying data remains in Amazon S3.

The InfluxDB Object Storage pricing is based on:

- Total data volume stored (GB/month), with a minimum monthly charge equivalent
  to 200GB

I/O operations costs are bundled within the compute pricing for the
db.influxIOIncluded instance classes, providing customers with more predictable costs
regardless of their specific I/O patterns.

##### Storage Architecture Benefits

The Amazon S3-based storage architecture in InfluxDB 3 is particularly beneficial for:

- Large-scale time-series analytics workloads
- High-cardinality data requirements
- Long-term data retention scenarios
- Cost-effective storage of large time-series datasets

This storage model is comparable to Timestream for LiveAnalytics' Magnetic Storage
Tier, which is also object store based and optimized for long-term storage and analytics
use cases. InfluxDB 3's storage economics are designed to be competitive with
LiveAnalytics' magnetic store pricing, a model that has proven suitable for customers
who want to run and store large-scale time-series workloads and data for long periods of
time.

#### DB Cluster Sizing

The optimal configuration of a Timestream for InfluxDB 3 cluster depends on various
factors, including ingestion rate, batch sizes, time-series cardinality, concurrent
queries, and query types.

When sizing InfluxDB 3 clusters, consider these additional factors due to its
different architecture:

- **Storage Efficiency**: For deployments with more than
  16TB of data, InfluxDB 3's object storage can provide up to 75% cost savings compared
  to Timestream for InfluxDB 2 deployments.
- **Workload Characteristics**: InfluxDB 3 is optimized for
  high-cardinality data and analytical queries over large datasets while delivering
  comparable performance to versions 1.x and 2.x for shorter time-range queries.
  Additionally, features like the [last-value](https://docs.influxdata.com/influxdb3/enterprise/admin/last-value-cache/ "https://docs.influxdata.com/influxdb3/enterprise/admin/last-value-cache/") and [distinct-value](https://docs.influxdata.com/influxdb3/enterprise/admin/distinct-value-cache/ "https://docs.influxdata.com/influxdb3/enterprise/admin/distinct-value-cache/") caches enable sustained sub-10ms query latencies for
  specific use cases such as retrieving the most recent data points or unique metadata
  values.
- **Query Patterns**: Consider whether your workload is
  continuous (24/7 monitoring) or intermittent (periodic analytics)
- **Compaction Requirements**: Enterprise version includes
  compaction capabilities essential for long-term data storage and high-cardinality
  workloads. For deployments with 3-node clusters and larger, a dedicated compactor
  node is recommended to maximize writer and reader performance on the other individual
  nodes, ensuring that compaction processes don't compete for resources with query and
  ingestion operations.

To provide sizing recommendations, let's consider an exemplary workload with the
following characteristics:

- Data is collected and written by a fleet of Telegraf agents gathering System,
  CPU, Memory, Disk, IO, etc. from a data center.
- Each write request contains 5000 lines.
- The queries executed on the system are categorized as "moderate
  complexity" queries, exhibiting the following characteristics:
  - They have multiple functions and one or two regular expressions.
  - They may include group by clauses or sample a time range of multiple weeks.
  - They typically take a few hundred milliseconds to a couple of thousand
    milliseconds to execute.
  - The CPU favors query performance primarily.
  - All tests were performed with a dataset containing a cardinality of 30
    million time-series.

| **Writes (lines per second)** | **Reads (Queries per second)** | **Instance class**            | **Version** |
| ----------------------------- | ------------------------------ | ----------------------------- | ----------- |
| ~150,000                      | <25                            | db.influxIOIncluded.large     | Core        |
| ~200,000                      | ~25                            | db.influxIOIncluded.xlarge    | Core        |
| ~250,000                      | ~35                            | db.influxIOIncluded.2xlarge   | Enterprise  |
| ~500,000                      | ~50                            | db.influxIOIncluded.4xlarge   | Enterprise  |
| <750,000                      | <100                           | db.influxIOIncluded.8xlarge   | Enterprise  |
| >750,000                      | >100                           | Multi-node Enterprise cluster | Enterprise  |

#### DB Cluster

Billing for Amazon Timestream for InfluxDB 3

Amazon Timestream for InfluxDB 3 clusters are billed based on the following components:

- **DB cluster node hours (per hour)** – Based on
  the DB cluster node class, for example, db.influxIOIncluded.large. Pricing is listed
  on a per-hour basis, but bills are calculated down to the second and show times in
  decimal form. Usage is billed in 1-second increments, with a minimum of 10 minutes.
  For single-node Core deployments or multi-node Enterprise deployments, each node is
  billed separately based on its running time.
- **Object storage (per GB per month)** – Actual
  data volume stored in InfluxDB Object Storage, rather than provisioned capacity. This
  model allows you to pay only for the storage you use, with no need to pre-provision
  storage capacity. **Note: There is a minimum monthly storage
  charge equivalent to 200GB**, even if your actual storage usage is lower.
- **Data transfer out (per GB)** – Data transfer out
  of your DB cluster to the internet or other AWS Regions. Data transfer in or traffic
  within the same VPC or between Availability Zones within the same AWS Region is free
  of charge.
- **InfluxDB 3 Enterprise License (per vCPU per
  hour)** – For InfluxDB 3 Enterprise deployments, there is an
  additional InfluxData license cost charged on a per vCPU per hour basis. This license
  fee is billed directly through AWS Marketplace and appears as a separate line item on your
  AWS bill. The license enables Enterprise features such as multi-node clustering,
  compaction capabilities, and advanced security features.

For InfluxDB 3 Enterprise clusters with multiple nodes, each node is billed
separately based on its instance class and vCPU count (for license fees), while storage
costs are consolidated since all nodes share the same underlying object storage.

##### Billing Components Summary

| **Billing Component**                     | **InfluxDB 3 Core**                         | **InfluxDB 3 Enterprise**                   |
| ----------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| Compute Billing                           | Per node hour (db.influxIOIncluded classes) | Per node hour (db.influxIOIncluded classes) |
| Storage Billing                           | Per GB of data stored (200GB minimum)       | Per GB of data stored (200GB minimum)       |
| I/O Operations                            | Included in compute node pricing            | Included in compute node pricing            |
| Storage Scaling                           | Not necessary,pay only for storage used     | Not necessary, pay only for storage used    |
| Data Transfer In                          | Free                                        | Free                                        |
| Data Transfer Within VPC/AZ               | Free                                        | Free                                        |
| Data Transfer Out (Internet/Cross-Region) | Charged per GB                              | Charged per GB                              |
| Minimum Billing                           | 10 minutes                                  | 10 minutes                                  |
| Billing Granularity                       | 1-second increments                         | 1-second increments                         |
| Multi-Node Support                        | No (single-node only)                       | Yes                                         |
| Additional License                        | None                                        | Per vCPU per hour via AWS Marketplace       |

### Cost Optimization Strategies

- **Right-sizing** – Select the appropriate node class
  based on your workload requirements to avoid over-provisioning. We also recommend
  choosing an instance that maintains an average of approximately 65% CPU and memory
  utilization, ensuring resilience to usage spikes and allowing headroom for healthy
  capacity planning.
- **Storage Efficiency** – For deployments with more
  than 16TB of data, InfluxDB 3's object storage can provide up to 75% cost savings
  compared to traditional EBS-based solutions.
- **Network Traffic Optimization** – Keep data
  transfer within the same VPC or region when possible to avoid data transfer out charges.
- **Scaling Strategy** – For InfluxDB 3 Enterprise,
  consider whether scaling up (larger node class) or scaling out (more nodes) is more
  cost-effective for your specific workload patterns.
- **License Optimization** – For InfluxDB 3
  Enterprise, choose node classes that provide the optimal balance between vCPU count
  (which affects license costs) and performance requirements.

For Amazon Timestream for InfluxDB 3 pricing information, see the [Amazon Timestream for InfluxDB pricing page](https://aws.amazon.com/timestream/pricing/ "https://aws.amazon.com/timestream/pricing/").

### AWS Regions and Availability

Zones

Amazon cloud computing resources are hosted in multiple locations world-wide. These
locations are composed of AWS Regions and Availability Zones. Each AWS Region is a
separate geographic area. Each AWS Region has multiple, isolated locations known as
Availability Zones.

Amazon Timestream for InfluxDB 3 enables you to place resources, such as DB clusters, and
data in multiple locations. For Enterprise deployments with multi-node clusters, nodes are
distributed across multiple Availability Zones to enhance availability.

For information about AWS Regions where Amazon Timestream for InfluxDB 3 is available and
the endpoints for each Region, see [Amazon Timestream endpoints and quotas](../../../general/latest/gr/timestream.md "../../../general/latest/gr/timestream.md").
