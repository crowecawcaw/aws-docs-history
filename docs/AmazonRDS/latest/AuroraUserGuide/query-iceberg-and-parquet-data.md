

# Querying Apache Iceberg and Parquet data directly in Aurora PostgreSQL
<a name="query-iceberg-and-parquet-data"></a>

Amazon Aurora PostgreSQL-Compatible Edition enables you to directly query Apache Iceberg and Parquet data in your data lake alongside your operational data in Aurora, using the same PostgreSQL endpoint, drivers, and SQL that your applications already use.

Applications increasingly need access to structured data in data lakes to make more informed decisions, deliver richer user experiences, and power AI agents that reason across operational and historical context. Traditionally, providing this access has required reverse extract, transform, and load (ETL) pipelines that copy data from your data lake into Aurora. These pipelines duplicate data, add infrastructure costs, and require ongoing engineering effort to keep copies in sync as source schemas and business requirements evolve.Aurora PostgreSQL eliminates this complexity. You create a PostgreSQL foreign table that points to your Iceberg or Parquet data in Amazon S3, Amazon S3 Tables, or the AWS Glue Data Catalog, and query it with standard SQL, without data movement or duplication. You can join foreign tables with your Aurora PostgreSQL tables in a single query, and write query results into a PostgreSQL table or materialized view. Through AWS Glue Data Catalog federation, you can also query Iceberg tables managed in external Iceberg REST Catalog (IRC)-compatible catalogs, without building custom integrations.

This capability is available on Aurora PostgreSQL 17.11 or higher, and 18.6 or higher, including Aurora Serverless v2.

**Topics**
+ [Benefits](#aurora-analytics-benefits)
+ [Use cases](#aurora-analytics-use-cases)
+ [How it works](aurora-analytics-how-it-works.md)
+ [Getting started](aurora-analytics-getting-started.md)
+ [Working with foreign tables](aurora-analytics-foreign-tables.md)
+ [Resource management](aurora-analytics-resource-management.md)
+ [Best practices](aurora-analytics-best-practices.md)
+ [Monitoring and troubleshooting](aurora-analytics-monitoring-troubleshooting.md)
+ [Using foreign tables with Aurora Global Database](aurora-analytics-global-database.md)
+ [Limitations](aurora-analytics-limitations.md)
+ [Technical reference](aurora-analytics-reference.md)
+ [Tutorial: Querying Amazon S3 data](aurora-analytics-tutorial.md)

## Benefits
<a name="aurora-analytics-benefits"></a>

Direct querying of Iceberg and Parquet data in Aurora PostgreSQL provides the following benefits.
+ **Unified access to operational and data lake data**: Query Apache Iceberg and Apache Parquet data alongside your Aurora PostgreSQL tables through the same PostgreSQL endpoint, using the drivers, ORMs, and BI tools your applications already use.
+ **No ETL pipelines to build or maintain**: Read data lake data directly from Aurora, no data to duplicate, no infrastructure to operate, and no ongoing engineering effort as schemas evolve.
+ **Improved analytical performance**: Aurora PostgreSQL embeds DuckDB, an open-source columnar analytical engine, directly in the PostgreSQL server. Analytical queries over data lake data run through an engine built for them. In addition, automatic caching on local instance storage, predicate pushdown, and column pruning keep queries fast, with no additional infrastructure to provision, size, or tune.
+ **Access to data across multiple sources**: Query Iceberg and Parquet data in Amazon S3, Amazon S3 Tables, and AWS Glue Data Catalog. For Iceberg tables managed outside AWS, AWS Glue Data Catalog federation extends this reach to any IRC-compatible catalog, so a single Aurora query can span operational data, AWS-managed data lakes, and third-party catalogs.
+ **Consistent security and governance**: Data lake access flows through PostgreSQL, so the roles, permissions, audit logs, and network controls you already use for Aurora extend automatically to foreign table queries. You manage access to operational and data lake data through one governance model, not two.
+ **No additional charge**: There is no additional charge to enable this capability. You pay only for the incremental Aurora compute and Amazon S3 requests that your queries consume.

## Use cases
<a name="aurora-analytics-use-cases"></a>

You can use direct querying of Iceberg and Parquet data anywhere reading data lake data alongside your operational data adds value to a PostgreSQL application. Common use cases include the following.
+ **Enrich operational queries with data lake data**: Join Iceberg or Parquet data in your data lake directly with your Aurora PostgreSQL tables in a single query. For example, combine an active support case in Aurora with a customer's purchase history and past interactions from your data lake, without data movement or duplication.
+ **Building agentic AI applications**: AI agents need reliable, structured access to both operational and historical data to reason and act. Aurora PostgreSQL provides this through a single PostgreSQL endpoint, with standard SQL as the tool interface. For example, a sales assistant agent can pull an open opportunity from Aurora and the account's full engagement history from your data lake in a single query, then use the result to draft the next outreach or recommend the next best action.
+ **Architecture simplification**: When workloads need data resident in Aurora PostgreSQL for low-latency access, you can load Iceberg or Parquet data from your data lake directly into Aurora tables using standard PostgreSQL statements such as `CREATE TABLE AS SELECT`, `INSERT INTO ... SELECT`, and `MERGE INTO`. This replaces separate bulk-load pipelines with a single SQL command, with no additional ingestion infrastructure to build or operate.
+ **Data tiering**: Keep hot operational data in Aurora PostgreSQL and move cold historical data into Iceberg or Parquet in your data lake using your existing data pipeline. Aurora continues to query the cold data through a foreign table, reducing your operational database size, storage cost, and backup footprint without losing query access to history.