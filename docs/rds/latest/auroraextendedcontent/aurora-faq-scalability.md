

# Scalability
<a name="aurora-faq-scalability"></a>

How does Amazon Aurora scale?

**Topics**
+ [What are the ways to scale compute resources in Amazon Aurora?](#aurora-faq-what-are-the-ways-to-scale-compute-resources-in-amazon-auror)
+ [What is Amazon Aurora serverless?](#aurora-faq-what-is-amazon-aurora-serverless)
+ [How is Aurora serverless priced?](#aurora-faq-how-is-aurora-serverless-priced)
+ [What is Aurora PostgreSQL Limitless Database?](#aurora-faq-what-is-aurora-postgresql-limitless-database)
+ [When should I use Aurora PostgreSQL Limitless Database?](#aurora-faq-when-should-i-use-aurora-postgresql-limitless-database)
+ [How does Limitless Database differ from Aurora serverless and replicas?](#aurora-faq-how-does-limitless-database-differ-from-aurora-serverless-an)
+ [What table types does Aurora PostgreSQL Limitless Database support?](#aurora-faq-what-table-types-does-aurora-postgresql-limitless-database-s)
+ [Are there any PostgreSQL compatibility considerations when using Aurora PostgreSQL Limitless Database?](#aurora-faq-are-there-any-postgresql-compatibility-considerations-when-u)
+ [How do I get started and connected to Aurora PostgreSQL Limitless Database?](#aurora-faq-how-do-i-get-started-and-connected-to-aurora-postgresql-limi)
+ [Do I need to change my existing database schema or application to use Aurora PostgreSQL Limitless Database?](#aurora-faq-do-i-need-to-change-my-existing-database-schema-or-applicati)
+ [Does Aurora PostgreSQL Limitless Database have support for high availability?](#aurora-faq-does-aurora-postgresql-limitless-database-have-support-for-h)
+ [What versions does Aurora PostgreSQL Limitless Database support?](#aurora-faq-what-versions-does-aurora-postgresql-limitless-database-supp)
+ [How is Aurora PostgreSQL Limitless Database priced?](#aurora-faq-how-is-aurora-postgresql-limitless-database-priced)

Aurora storage starts at a minimum of 10 GiB and automatically grows up to 256 TiB in 10 GiB increments with no impact to database performance. There is [no need to provision storage in advance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability). For workloads that need to scale beyond 256 TiB, [Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) provides automated horizontal scaling.

## What are the ways to scale compute resources in Amazon Aurora?
<a name="aurora-faq-what-are-the-ways-to-scale-compute-resources-in-amazon-auror"></a>

There are three ways to scale compute resources:
+ Aurora serverless: An on-demand, autoscaling configuration that adjusts database compute based on application demand. You specify a capacity range and Aurora scales automatically. Learn more in the [Aurora serverless user guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-2.html).
+ Aurora PostgreSQL Limitless Database: Automatically scales compute horizontally to support high-scale applications that need more write throughput or storage than a single instance provides. Learn more in the [Limitless Database User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html).
+ Manual scaling: Select the desired DB instance type in the [Amazon RDS console](https://console.aws.amazon.com/rds/). Changes apply during your maintenance window or immediately with the Apply Immediately flag.

## What is Amazon Aurora serverless?
<a name="aurora-faq-what-is-amazon-aurora-serverless"></a>

[Aurora serverless](https://aws.amazon.com/rds/aurora/serverless/) is an on-demand, autoscaling configuration for Amazon Aurora. It automatically adjusts database compute capacity based on your application's needs — you specify a desired capacity range in Aurora Capacity Units (ACUs) and Aurora scales within that range in fine-grained increments. It's especially well-suited for agentic AI applications, which typically have bursts of activity, long idle windows, and unpredictable patterns. You pay per-second for ACU usage.

Aurora serverless scales down to zero ACUs when your database has no active connections, automatically pausing the instance to eliminate compute costs during idle periods. When a new connection arrives, the instance automatically resumes — typically faster than starting a stopped cluster. This [automatic pause and resume](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2-auto-pause.html) capability is available for both Aurora PostgreSQL and Aurora MySQL, and is especially useful for development, test, and SaaS multi-tenant environments where databases may have extended periods of inactivity.

[Aurora serverless](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-2.how-it-works.html) supports all features of provisioned Aurora, including [read replica](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication), [Multi-AZ configuration](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability), [Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database), [RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy), and [CloudWatch Database Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Database-Insights.html). If capacity cannot scale fast enough for a sudden workload change, you can set it explicitly via the console, CLI, or API.

How do I connect to Aurora serverless?

You access Aurora serverless from within a client application running in the same VPC. You can't give a public IP address to Aurora serverless.

Can I use Aurora serverless with my existing Aurora cluster?

Yes, you can add Aurora serverless instances to your existing Aurora DB cluster , creating a mixed-configuration cluster with any combination of provisioned and serverless instances. To test it, add a serverless reader, validate it with read-only workloads, then initiate a failover to use it for both reads and writes with minimal downtime. You can also restore snapshots between provisioned and serverless clusters in either direction.

## How is Aurora serverless priced?
<a name="aurora-faq-how-is-aurora-serverless-priced"></a>

In Aurora serverless, database capacity is measured in Aurora Capacity Units (ACUs). You pay a flat rate per second of ACU usage. Compute costs depend on the database cluster configuration you choose: Aurora Standard or Aurora I/O-Optimized. Visit the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/) for information about pricing and Regional availability.

## What is Aurora PostgreSQL Limitless Database?
<a name="aurora-faq-what-is-aurora-postgresql-limitless-database"></a>

[Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) provides automated horizontal scaling while maintaining the simplicity of operating inside a single database. It splits data across database instances using customer-specified shard keys and automatically scales compute and storage as your workload grows. Your application connects using the standard cluster endpoint — no special drivers required.

Limitless Database supports three table types: sharded tables distributed across shards for scaling your largest tables, reference tables copied in full on every shard for faster joins, and standard tables placed on a single shard. You may need to adjust your schema to add shard keys to tables and queries. For high availability, set compute redundancy greater than zero to achieve 99.99% availability with automatic failover. Available with Aurora I/O-Optimized (see [documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) for supported versions and pricing).

## When should I use Aurora PostgreSQL Limitless Database?
<a name="aurora-faq-when-should-i-use-aurora-postgresql-limitless-database"></a>

You should use Limitless Database for applications that need to scale horizontally and require more write throughput or data storage capacity than a single Aurora database instance supports. For example, an accounting application can be horizontally partitioned by user since each user's accounting data is independent from the others.

## How does Limitless Database differ from Aurora serverless and replicas?
<a name="aurora-faq-how-does-limitless-database-differ-from-aurora-serverless-an"></a>

Aurora offers three scaling mechanisms, each designed for different needs:

How does Aurora PostgreSQL Limitless Database work?

Aurora PostgreSQL Limitless Database is a distributed, horizontally scalable PostgreSQL database that automatically splits data across multiple serverless compute instances based on customer-defined shard key.

Architecture:

Shard key — A designated table column (e.g., User-ID) that determines how data is distributed across instances.

Routers — Serverless nodes that analyze incoming queries and route them to the correct shard or orchestrate cross-shard queries.

Shards — Serverless nodes that each store a subset of data, enabling parallel processing for high write throughput.

Auto-scaling:

Aurora automatically scales up individual instances (compute and storage) first, then scales out by adding shards to handle growing workloads. Each shard key value is owned by a single serverless instance at any point in time.

Transaction semantics:

Multiple compute instances serve requests simultaneously while maintaining the same ACID transaction guarantees as single-writer Aurora PostgreSQL — no application-level transaction domain management required.

## What table types does Aurora PostgreSQL Limitless Database support?
<a name="aurora-faq-what-table-types-does-aurora-postgresql-limitless-database-s"></a>

Aurora PostgreSQL Limitless Database supports three table types: sharded, reference, and standard. Sharded tables: Distributed across multiple shards based on the values of designated columns in the table, called shard keys. Use these for scaling out the largest, most I/O-intensive tables in your application. Reference tables: Fully replicated to every shard.. Ideal for infrequently modified lookup data, such as product catalogs and zip codes. Standard tables: Standard Aurora PostgreSQL tables stored together on a single shard. You can create sharded and reference tables from standard tables.

## Are there any PostgreSQL compatibility considerations when using Aurora PostgreSQL Limitless Database?
<a name="aurora-faq-are-there-any-postgresql-compatibility-considerations-when-u"></a>

To learn more about PostgreSQL compatibility considerations, visit

## How do I get started and connected to Aurora PostgreSQL Limitless Database?
<a name="aurora-faq-how-do-i-get-started-and-connected-to-aurora-postgresql-limi"></a>

You can create a new Aurora PostgreSQL cluster with the supported engine version using the [Amazon RDS console](https://console.aws.amazon.com/rds/home) or Amazon APIs. Then connect to the cluster endpoint — the same way you connect to any standard Aurora PostgreSQL cluster.

To learn more, visit [Aurora PostgreSQL Limitless Database User Guide](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html).

## Do I need to change my existing database schema or application to use Aurora PostgreSQL Limitless Database?
<a name="aurora-faq-do-i-need-to-change-my-existing-database-schema-or-applicati"></a>

Yes, you might need to adjust your database schema to use Aurora PostgreSQL Limitless Database.

Schema changes:
+ All sharded tables must include the shard key column. If a table doesn’t naturally contain it, you’ll need to add and backfill it.
+ Column names are flexible, but the shard key column definition must match across collocated tables.
+ For example, an accounting application sharded by User-ID would need to add a User-ID column to the invoice line items to collocate related items.

Query changes:

Include the shard key in application queries – which may require adjusting your queries and transactions for optimal performance.

For example, a query specifying both Invoice-ID and User-ID routes to a single shard; omitting User-ID forces execution across all shards, increasing latency.

PostgreSQL compatibility:

Some PostgreSQL features have specific requirements or limitations in Limitless Database. For more details, go to [Aurora PostgreSQL Limitless Database requirements and considerations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reqs-limits.html).

## Does Aurora PostgreSQL Limitless Database have support for high availability?
<a name="aurora-faq-does-aurora-postgresql-limitless-database-have-support-for-h"></a>

Yes. Aurora PostgreSQL Limitless Database supports up to 99.99% availability with configurable compute redundancy. Set compute redundancy to be greater than zero to enable high availability.. Each compute instance that stores and accesses data from your Aurora PostgreSQL Limitless Database can have one or two standbys that can take over requests if the primary is unavailable. The routers will automatically redirect the traffic for minimal impact on your application.

## What versions does Aurora PostgreSQL Limitless Database support?
<a name="aurora-faq-what-versions-does-aurora-postgresql-limitless-database-supp"></a>

Aurora PostgreSQL Limitless Database is available for the Aurora I/O-Optimized cluster configuration starting with PostgreSQL 16.4 compatibility. Additional information is available in the [Aurora release notes](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/limitless-updates.html).

## How is Aurora PostgreSQL Limitless Database priced?
<a name="aurora-faq-how-is-aurora-postgresql-limitless-database-priced"></a>

In Aurora PostgreSQL Limitless Database, database capacity is measured in ACUs. You pay a flat rate per second of ACU usage. Aurora I/O-Optimized configuration storage rates apply. For more information, visit the [Aurora pricing page](https://aws.amazon.com/rds/aurora/pricing/).