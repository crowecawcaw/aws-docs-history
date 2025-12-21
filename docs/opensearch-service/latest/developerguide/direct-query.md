# Working with Amazon OpenSearch Service direct queries

Use Amazon OpenSearch Service direct query to analyze data in Amazon CloudWatch Logs, Amazon S3, and Amazon Security Lake without
building ingestion pipelines. This zero-ETL integration lets you query data in place using
OpenSearch SQL or PPL, and explore it in **Discover**.

To get started, configure your data source in the OpenSearch Service console. For Amazon S3, use domain
connections and create tables with SQL in Query Workbench. CloudWatch Logs and Security Lake use preconfigured
sources and AWS Glue Data Catalog tables.

## Direct query quotas

Your account has the following quotas related to OpenSearch Service direct queries.

### Quotas for Amazon S3

Each time you initiate a query to an Amazon S3 data source, OpenSearch Service opens a
_session_ and keeps it alive for at least three minutes. This
reduces query latency by removing session start-up time in subsequent
queries.

| Description                            | Maximum | Can override |
| -------------------------------------- | ------- | ------------ |
| Connections per domain                 | 10      | Yes          |
| Data sources per domain                | 20      | Yes          |
| Indexes per domain                     | 5       | Yes          |
| Concurrent sessions per data source    | 10      | Yes          |
| Maximum OCU per query                  | 60      | Yes          |
| Maximum query execution time (minutes) | 30      | Yes          |
| Maximum OCUs per acceleration          | 20      | Yes          |
| Maximum ephemeral storage              | 20      | Yes          |

### Quotas for CloudWatch Logs

###### Note

If you're looking to perform direct queries using CloudWatch Logs Insights, make sure
that you refer to [Additional information for
CloudWatch Logs Insights users using OpenSearch SQL](supported-directquery-sql.md#supported-sql-for-multi-log-queries "supported-directquery-sql.md#supported-sql-for-multi-log-queries").

| Description                                           | Value   | Soft limit? | Notes                                                                                                                                                                                                                         |
| ----------------------------------------------------- | ------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account-level TPS limit across direct query APIs      | 3 TPS   | Yes         |                                                                                                                                                                                                                               |
| Maximum number of data sources                        | 20      | Yes         | Limit is per AWS account.                                                                                                                                                                                                     |
| Maximum auto-refreshing indexes or materialized views | 30      | Yes         | Limit is per data source.                                                                                                                                                                                                     |
| Maximum concurrent queries                            | 15      | Yes         | Limit applies to queries in pending or running state.<br>Includes interactive queries (for example, data retrieval<br>commands like `SELECT`) and index queries (for<br>example, operations like<br>`CREATE`/`ALTER`/`DROP`). |
| Maximum concurrent OCU per query                      | 512     | Yes         | OpenSearch Compute Units (OCU). Limit based on 15 executors<br>and 1 driver, each with 16 vCPU and 32 GB memory. Represents<br>concurrent processing power.                                                                   |
| Maximum query execution time in minutes               | 60      | No          | Limit applies to OpenSearch PPL/SQL queries in CloudWatch Logs<br>Insights.                                                                                                                                                   |
| Period for purging stale query IDs                    | 90 days | Yes         | This is the time period after which OpenSearch Service purges query metadata<br>for older entries. For example, calling GetDirectQuery or<br>GetDirectQueryResult fails for queries older than 90 days.                       |

### Quotas for Security Lake

| Description                                           | Value   | Soft limit? | Notes                                                                                                                                                                                                                         |
| ----------------------------------------------------- | ------- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Account-level TPS limit across direct query APIs      | 3 TPS   | Yes         |                                                                                                                                                                                                                               |
| Maximum number of data sources                        | 20      | Yes         | Limit is per AWS account.                                                                                                                                                                                                     |
| Maximum auto-refreshing indexes or materialized views | 30      | Yes         | Limit applies per data source.<br>Only includes indices and materialized views (MVs) with<br>auto-refresh set to true.                                                                                                        |
| Maximum concurrent queries                            | 30      | Yes         | Limit applies to queries in pending or running state.<br>Includes interactive queries (for example, data retrieval<br>commands like `SELECT`) and index queries (for<br>example, operations like<br>`CREATE`/`ALTER`/`DROP`). |
| Maximum concurrent OCU per query                      | 512     | Yes         | OpenSearch Compute Units (OCU). Limit based on 15 executors<br>and 1 driver, each with 16 vCPU and 32 GB memory. Represents<br>concurrent processing power.                                                                   |
| Maximum query execution time in minutes               | 30      | No          | Applies only to interactive queries (for example, data retrieval<br>commands like `SELECT`). For `REFRESH`<br>queries, the limit is 6 hours.                                                                                  |
| Period for purging stale query IDs                    | 90 days | Yes         | This is the time period after which OpenSearch Service purges query<br>metadata for older entries. For example, calling GetDirectQuery<br>or GetDirectQueryResult fails for queries older than 90<br>days.                    |

## Supported AWS Regions

The following AWS Regions are supported for OpenSearch Service direct queries in Amazon S3, CloudWatch Logs, and
Security Lake:

### Available AWS Regions for Amazon

S3

- Asia Pacific (Hong Kong)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (Stockholm)
- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)

### Available AWS Regions

for CloudWatch Logs

- Asia Pacific (Mumbai)
- Asia Pacific (Hong Kong)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (Stockholm)
- Europe (Milan)
- Europe (Spain)
- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- US West (N. California)
- Europe (Paris)
- Europe (London)
- South America (Sao Paulo)

### Available AWS Regions

for Security Lake

- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (Stockholm)
- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Europe (Paris)
- Europe (London)
- South America (Sao Paulo)
