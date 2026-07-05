# Optimized for log analytics

Amazon OpenSearch Service optimized for log analytics is a new engine option that combines columnar
analytical storage with full-text search in a single managed service. With the Optimized engine, you get significantly better price-performance
for log analytics workloads. You also retain full-text search for incident
investigation.

## Overview

The Optimized engine is a new engine mode in Amazon OpenSearch Service. You
use the same console, APIs, security model, and networking configuration that you
already use with the general-purpose engine.

With the Optimized engine, you get the following improvements for log
analytics workloads:

- **Improved price-performance** – Columnar
  compression and efficient instance utilization reduce the cost of running log
  analytics at scale.
- **Reduced storage** – Apache Parquet
  columnar format compresses log data significantly compared to traditional
  indexing structures.
- **Faster ingestion** – A vectorized,
  columnar write path increases ingestion throughput.
- **Faster analytical queries** –
  Vectorized execution on columnar data accelerates aggregations, filters, and
  trend analysis.
- **Unified search and analytics** –
  Full-text search predicates run inside analytical queries on the same data,
  in a single service.

The following table compares the two engine modes.

| Engine mode                               | Best for                                                                                                      |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| General Purpose                           | Search-heavy and mixed workloads with frequent updates<br>(e-commerce, content discovery, application search) |
| Optimized (Recommended for log analytics) | Append-only logs and log analytics at multi-terabyte scale                                                    |

## When to use each engine mode

Use the Optimized engine when your workload is dominated by aggregations, filters,
and trend analysis over logs, and you also need full-text search during incidents.
Examples include application, infrastructure, and security log analytics at
multi-terabyte-per-day scale.

Use the General Purpose engine when your workload depends on relevance ranking,
nested-object queries, Painless scripting, geo queries, vector/semantic search, or
frequent in-place document updates. Examples include e-commerce search, content
discovery, and application search.

## How it works

The Optimized engine uses the best data structure for each operation. The engine stores log data in columnar format for analytics. It retains a
search index for full-text search and routes each query to the best-suited
component.

The following table describes the components of the Optimized engine.

| Component             | Role                                                                                                                                                  |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Apache Parquet        | Open columnar storage format. Primary storage for log data.<br>Delivers significant storage reduction compared to traditional<br>indexing structures. |
| Lucene inverted index | Retained for full-text search on log content (phrase, fuzzy,<br>wildcard matching).                                                                   |
| Apache Calcite        | SQL parser, planner, and optimizer. Runs on the coordinator node<br>as a single front end for all query languages.                                    |
| DataFusion            | Vectorized execution engine (Rust-based). Executes analytical<br>operations (aggregations, filters, range scans) on columnar<br>data.                 |
| Apache Arrow          | In-memory columnar format. Enables zero-copy data transfer and<br>vectorized processing.                                                              |
| Amazon S3             | Durable backing store for both Parquet files and inverted-index<br>segments.                                                                          |
| OpenSearch UI         | Query and visualization interface for Optimized domains (PPL query<br>bar, natural-language query assistance).                                        |

Data enters through existing REST APIs and client libraries (no new agents or
pipelines required). The engine writes data to columnar Parquet for analytics. For
fields configured as searchable, it also writes to a Lucene inverted index. PPL and
SQL execute natively through the vectorized engine. Full-text search predicates
execute on the inverted index and can be combined with analytics in a single
statement.

Queries flow through a coordinator node (plan and merge) and data nodes (execute
and store). The coordinator parses and optimizes the query, then schedules fragments
to data nodes. On each data node, analytical operations run on the DataFusion engine
while search operations run on the Lucene engine. The two can hand off mid-query, so
a query that searches log content and aggregates the results runs without additional
round-trips.

## Region availability

Amazon OpenSearch Service optimized for log analytics is available in the following
AWS Regions:

- US East (N. Virginia) – `us-east-1`
- US East (Ohio) – `us-east-2`
- US West (Oregon) – `us-west-2`
- Canada (Central) – `ca-central-1`
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Spain)
