# Amazon Aurora FAQ

## What is Amazon Aurora?

[Amazon Aurora](https://aws.amazon.com/rds/aurora/ "https://aws.amazon.com/rds/aurora/") is a fully managed [relational database](https://aws.amazon.com/rds/what-is-a-relational-database/ "https://aws.amazon.com/rds/what-is-a-relational-database/") service designed for high performance and availability at global scale for PostgreSQL, MySQL, and [DSQL](https://aws.amazon.com/rds/aurora/dsql/ "https://aws.amazon.com/rds/aurora/dsql/"). Aurora PostgreSQL and Aurora MySQL offer full open source compatibility, so you can use your existing code, applications, drivers, and tools with little or no modification.

Aurora’s storage system is distributed, fault-tolerant, and self-healing — it automatically scales up to 256 TiB per database instance and replicates your data across three Availability Zones (AZs), you only pay for one copy. With Aurora PostgreSQL and MySQL, you get up to 15 low-latency read replicas, point-in-time recovery, and continuous backup to [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). Aurora automates administration tasks like hardware provisioning, patching, and backups, delivering commercial-grade reliability at the cost effectiveness of open source databases. With Aurora DSQL, its serverless distributed architecture means zero infrastructure management and virtually unlimited scalability.

## Is Amazon Aurora MySQL compatible?

Yes. Amazon Aurora is drop-in [compatible with MySQL](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.md") and adds support for new releases regularly. You can migrate MySQL databases to and from Aurora using standard tools like mysqldump and mysqlimport, or use [Amazon RDS DB Snapshot migration](../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.RDSMySQL.md"). Your existing MySQL code, applications, drivers, and tools work with Aurora with little or no change. See the [Aurora MySQL compatibility documentation](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.Overview.md") for supported versions.

## Is Amazon Aurora PostgreSQL compatible?

Yes. Amazon Aurora is drop-in [compatible with PostgreSQL](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraPostgreSQL.md") and adds support for new releases regularly. You can migrate PostgreSQL databases to and from Aurora using pg\_dump and pg\_restore, or use [RDS DB Snapshot migration](../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md "../../../AmazonRDS/latest/UserGuide/USER_CreateSnapshot.md"). For SQL Server migrations, [Babelfish for Aurora PostgreSQL](https://aws.amazon.com/rds/aurora/babelfish/ "https://aws.amazon.com/rds/aurora/babelfish/") lets your applications work without code changes. See the [Aurora PostgreSQL compatibility documentation](../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.md "../../../AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Updates.20180305.md") for supported versions.

## Does Amazon Aurora support PostgreSQL extensions?

Yes, Amazon Aurora PostgreSQL supports all PostgreSQL extensions available with Aurora. You can enable extensions using the standard CREATE EXTENSION command, just as you would with any PostgreSQL database. If you need help with a specific extension, contact [AWS Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/"). Customers with an active AWS Premium Support plan can reach out directly for Aurora-specific troubleshooting and guidance.

## How do I get started with Amazon Aurora?

Getting started with Amazon Aurora is straightforward and takes just a few minutes — or even seconds with the latest deployment options. You can create and connect to an Aurora PostgreSQL database in seconds using [express configuration](../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md "../../../AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.AuroraPostgreSQL.ExpressConfig.md") in the Amazon RDS console, pre-configured with an Aurora serverless cluster. Once created, you have access to Aurora features that can be modified at any time. You also get a new internet gateway supporting the Postgres wire protocol for secure connections from your favorite tools and IDEs outside AWS — no VPN required. New AWS customers can also get started with Aurora PostgreSQL serverless through the [Vercel Marketplace](https://vercel.com/marketplace/aws "https://vercel.com/marketplace/aws") using only an email address.

To customize configurations, sign in to the [Amazon RDS console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and navigate to Amazon RDS under the Database category. Select Amazon Aurora as your engine and choose either the MySQL-compatible or PostgreSQL-compatible edition for full configuration. The console guides you through instance size, storage, networking, and security settings.

For step-by-step instructions, tutorials, and best practices, visit the [Getting Started with Amazon Aurora](https://aws.amazon.com/rds/aurora/getting-started/ "https://aws.amazon.com/rds/aurora/getting-started/") page, which provides quickstart guides, sample code, and migration tools. If you're new to Aurora, consider starting with a development environment to familiarize yourself with Aurora's features before deploying production workloads.

## In which AWS Regions is Amazon Aurora available?

Aurora is available across AWS Regions worldwide. For a complete list, see [Supported features in Amazon Aurora by AWS Region and Aurora DB engine](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.md "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.md").

## Does Amazon Aurora require special drivers?

No. Aurora works with standard MySQL and PostgreSQL database drivers. You can use the same drivers and connection libraries you already use with MySQL or PostgreSQL databases, with no modifications required.
