# Release notes for Aurora DSQL

This page describes new features, service launches, and important updates for Aurora DSQL.
For documentation-specific changes, see the [Document
history](doc-history.md "doc-history.md").

## 2026

### August 2026

August 13, 2026

🐘 _PostgreSQL Compatibility_ — **Indexes on
expressions** — Aurora DSQL now supports indexes on expressions. An index key can be an
expression computed from one or more columns of the table row, so a query that filters on the
same expression can use the index. For example, an index on `lower(title)` gives
efficient case-insensitive searches. All functions and operators used in an index definition
must be immutable. For more information, see [CREATE INDEX](create-index-syntax-support.md "create-index-syntax-support.md").

August 3, 2026

🐘 _PostgreSQL Compatibility_ — **ALTER TABLE DROP
COLUMN** — Aurora DSQL now supports `ALTER TABLE ... DROP COLUMN` to remove a
column from an existing table, You can drop multiple columns in a single statement.
Dropping a primary key column isn't supported. For more information,
see [ALTER TABLE](alter-table-syntax-support.md "alter-table-syntax-support.md").

August 3, 2026

🐘 _PostgreSQL Compatibility_ — **ALTER TABLE ADD CONSTRAINT and VALIDATE CONSTRAINT** — Aurora DSQL now supports `ALTER TABLE ... ADD CONSTRAINT ... NOT VALID` for adding `CHECK` constraints without validating existing data, and `ALTER TABLE ASYNC ... VALIDATE CONSTRAINT` for validating existing data against constraints later. The `NOT VALID` option allows adding constraints to large tables without blocking operations. The validation runs as an asynchronous DDL job that can be monitored using `sys.jobs`. For more information, see [ALTER TABLE](alter-table-syntax-support.md "alter-table-syntax-support.md").

### July 2026

July 31, 2026

🌍 _Region Expansion_ — **Aurora DSQL available in
four additional Regions** — Multi-Region clusters are now available in Europe
(Stockholm), Europe (Spain), Asia Pacific (Mumbai), and Asia Pacific (Singapore). For a
complete list of supported Regions, see [Region availability for
Aurora DSQL](what-is-aurora-dsql.md#region-availability "what-is-aurora-dsql.md#region-availability").

July 30, 2026

✨ _Feature_ — **Cost visibility and alerting** — With the Aurora DSQL console, you can now view accumulated Aurora DSQL distributed processing
units (DPU) and more easily establish real-time alerts based on DPU usage.

July 15, 2026

✨ _AI Integration_ — **Aurora DSQL Assist in the Aurora DSQL
Playground** — Aurora DSQL Assist is a new artificial intelligence (AI) assistant in the
Aurora DSQL Playground that helps you go from idea to working query. You can generate and fix SQL
from natural language and design schemas and indexes for the distributed architecture of
Aurora DSQL. You can also explore errors and documentation conversationally. For more
information about Aurora DSQL Assist, see the [Aurora DSQL Playground website](https://playground.dsql.demo.aws/ "https://playground.dsql.demo.aws/").

July 6, 2026

🐘 _PostgreSQL Compatibility_ — **Additional ALTER
TABLE operations** — Aurora DSQL now supports additional `ALTER TABLE`
operations: `SET DEFAULT`, `DROP DEFAULT`, `DROP NOT
 NULL`, `DROP EXPRESSION`, `ADD GENERATED AS IDENTITY`, and
`DROP CONSTRAINT`. These metadata DDL operations enable more flexible schema
evolution without requiring table recreation. For more information, see [ALTER TABLE](alter-table-syntax-support.md "alter-table-syntax-support.md").

July 8, 2026

🆕 _Feature_ — **Change data capture now
generally available** — Change data capture (CDC) for Aurora DSQL is now generally
available. This release adds distinct operation types (`op: "u"` for updates,
`op: "c"` for inserts) and documents write-set compaction, which consolidates
multiple changes to the same row within a transaction into a single CDC record. If an
application inserts and deletes a row in the same transaction, Aurora DSQL recognizes zero
net change and omits the row from the stream. For more
information, see [CDC streams](cdc-streams.md "cdc-streams.md").

### June 2026

June 8, 2026

🐘 _PostgreSQL Compatibility_ — **JSONB data type
with compression** — Aurora DSQL now supports the PostgreSQL `JSONB`
data type, with optional compression for stored data. You can use `JSONB`
columns to store semi-structured data such as system configuration metadata, API
parameters, and event logs alongside relational data, and existing code and tools that
depend on PostgreSQL's `JSONB` type work with Aurora DSQL without modification.
Aurora DSQL enables PostgreSQL compression by default, storing larger `JSONB` payloads
more efficiently. For more information, see [Supported data
types in Aurora DSQL](working-with-postgresql-compatibility-supported-data-types.md "working-with-postgresql-compatibility-supported-data-types.md").

### May 2026

May 14, 2026

🆕 _Feature_ — **Change data capture
(Preview)** — Aurora DSQL introduces support for change data capture (CDC) in
preview, enabling you to stream real-time database changes directly to Amazon Kinesis Data
Streams. This fully managed capability removes the need to build or maintain custom
streaming pipelines, making it easier to build event-driven applications, power real-time
analytics pipelines, and synchronize data across systems. For more information, see
[Getting started with CDC](cdc-setup.md "cdc-setup.md").

May 11, 2026

🌍 _Region Expansion_ — **Aurora DSQL available in five
additional Regions** — Single-Region clusters are now available in
Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Singapore), Europe
(Stockholm), and South America (São Paulo). For a complete list of supported Regions,
see [Region availability for
Aurora DSQL](region-availability.md "region-availability.md").

May 4, 2026

🐘 _PostgreSQL Compatibility_ — **JSON data type with
compression** — Aurora DSQL now supports the PostgreSQL `JSON` data type
with optional compression. You can store semi-structured data such as API payloads,
configuration objects, or event logs alongside relational data. Aurora DSQL enables PostgreSQL
compression by default, storing larger `JSON` payloads more efficiently.

### April 2026

April 28, 2026

🆕 _Feature_ — **Cost Estimator in the Aurora DSQL
Playground** — The Aurora DSQL Playground now includes a Cost Estimator that helps you
estimate the cost of running your workload on Aurora DSQL. You can pin queries to build a
representative workload and review the estimated Distributed Processing Units (DPUs) those
queries consume. The estimator also shows how the AWS Free Tier allowance of 100,000 DPUs per month applies to your
workload.

To get started with the Cost Estimator, see the [Aurora DSQL Playground website](https://playground.dsql.demo.aws/ "https://playground.dsql.demo.aws/"). For more
information about how Aurora DSQL meters usage, see [Billing and Metering in Aurora DSQL](billing-metering.md "billing-metering.md").

April 24, 2026

🐘 _PostgreSQL Compatibility_ — **ALTER DEFAULT PRIVILEGES
support** — Aurora DSQL now supports PostgreSQL's `ALTER DEFAULT
 PRIVILEGES` for tables, sequences, functions, and types. Newly created objects
automatically inherit configured default privileges, removing the need for manual
`GRANT` statements after each object creation.

April 24, 2026

🐘 _PostgreSQL Compatibility_ — **CREATE SCHEMA with nested
statements** — Aurora DSQL now supports nested `CREATE SEQUENCE` and
`GRANT` statements within a `CREATE SCHEMA` command, enabling
developers to define schema objects and their permissions in a single atomic
operation.

April 24, 2026

🐘 _PostgreSQL Compatibility_ — **ALTER USER/ROLE RENAME
support** — Aurora DSQL now supports `ALTER USER/ROLE/GROUP ... RENAME
 TO`, enabling administrators to rename database roles without dropping and
recreating them. The rename propagates across all active sessions through catalog
version notifications.

April 24, 2026

🐘 _PostgreSQL Compatibility_ — **ALTER ROUTINE support** —
Aurora DSQL now supports `ALTER ROUTINE ... SET SCHEMA`, `SET
 OWNER`, and `RENAME TO`, along with `GRANT`,
`REVOKE`, `COMMENT ON`, and `DROP ROUTINE`. The
`ROUTINE` keyword is a PostgreSQL umbrella term covering both functions and
procedures, enabling object-relational mapping (ORM) and migration tools that emit
`ROUTINE` syntax to work without modification.

April 21, 2026

🆕 _Feature_ — **AWS Backup adds Aurora DSQL support for
AWS Organizations backup policies** — AWS Backup now supports Aurora DSQL clusters
as a resource type in AWS Organizations backup policies. Organization administrators
can define backup policy rules that directly target Aurora DSQL clusters across member
accounts, providing more precise control over which resources are included in
Organization-wide backup plans.

April 13, 2026

🔌 _Developer Tools_ — **Aurora DSQL Connector for PHP
(`PDO_PGSQL`)** — Added the Aurora DSQL Connector for PHP that handles IAM token
generation, Secure Sockets Layer (SSL) configuration, and connection pooling for PHP
applications. The connector provides opt-in optimistic concurrency control (OCC) retry
with exponential backoff. For
more information, see [Connecting to Aurora DSQL
clusters with a PHP connector](SECTION_program-with-dsql-connector-for-php-pdo-pgsql.md "SECTION_program-with-dsql-connector-for-php-pdo-pgsql.md").

### March 2026

March 31, 2026

🔌 _Developer Tools_ — **Aurora DSQL Connectors for .NET
(`Npgsql`) and Rust (`SQLx`)** — Added connectors for .NET and Rust that handle IAM
token generation, SSL configuration, and connection pooling. Both connectors provide
opt-in OCC retry with exponential backoff, custom IAM credential providers, and AWS
profile support. For more information, see [Aurora DSQL
connectors](SECTION_connectors.md "SECTION_connectors.md").

March 30, 2026

⚡ _Performance_ — **Faster INSERT ON CONFLICT
statements** — Aurora DSQL improves write performance for `INSERT ON
 CONFLICT` statements. The improvement scales with the number of rows proposed for
insertion per transaction, so workloads that batch many `INSERT ON CONFLICT`
statements into a single transaction see the largest gains.

March 30, 2026

⚡ _Performance_ — **Faster uniqueness validation for
large insert workloads** — Aurora DSQL now validates secondary unique-index
constraints in batches rather than one key at a time, accelerating large insert and
migration workloads. The speedup is most pronounced for transactions that touch many
rows or tables with multiple unique secondary indexes — workloads where uniqueness
validation was previously the bottleneck. For example, inserting 1,000 rows into a
table with one unique secondary index now completes in 577 ms, down from 1,041 ms (1.8x
faster).

March 26, 2026

🔌 _Developer Tools_ — **Aurora DSQL Connector for Ruby
(`pg` gem)** — Added the Aurora DSQL Connector for Ruby that handles IAM token
generation, SSL configuration, and connection pooling. The connector provides opt-in OCC
retry with exponential backoff and custom IAM credential providers. For more information,
see [Connecting to
Aurora DSQL clusters with a Ruby pg connector](SECTION_program-with-dsql-connector-for-ruby-pg.md "SECTION_program-with-dsql-connector-for-ruby-pg.md").

### February 2026

February 25, 2026

🔌 _Developer Tools_ — **Integrations for Visual
Studio Code SQLTools and DBeaver** — Added the Aurora DSQL Driver for SQLTools and
the Aurora DSQL Plugin for DBeaver Community Edition. Both integrations simplify database
connectivity by automatically handling IAM authentication and transparently managing
access tokens. The SQLTools driver is also available on Open VSX Registry for use with
VS Code-compatible editors such as Cursor and Kiro.

February 25, 2026

🆕 _Feature_ — **Aurora DSQL Playground** —
AWS launches a browser-based playground that enables developers to interact with an
Aurora DSQL database without requiring an AWS account. With zero setup or infrastructure
configuration, developers can create schemas, load data, and execute SQL queries directly
from their browser with built-in sample datasets. To start exploring, visit the
[Aurora DSQL Playground](https://playground.dsql.demo.aws/ "https://playground.dsql.demo.aws/").

February 25, 2026

🔌 _Developer Tools_ — **Support for Tortoise,
Flyway, and Prisma** — Added integrations for popular ORM and database migration
tools: an adapter for Tortoise (Python ORM), a dialect for Flyway (schema management
tool), and CLI tools for Prisma (Node.js ORM). These integrations handle IAM
authentication and Aurora DSQL-specific compatibility requirements automatically.

February 19, 2026

🔌 _Developer Tools_ — **Go, Python, and Node.js
connectors with WebSocket support** — Added Aurora DSQL Connectors for Go
(`pgx`), Python (`asyncpg`), and Node.js (WebSocket for
`Postgres.js`) that simplify IAM authentication. Each connector automatically
generates tokens for each connection. The `Postgres.js` connector additionally
supports WebSocket protocol for environments where
Transmission Control Protocol (TCP) connections aren't available. For more information, see [Aurora DSQL
connectors](SECTION_connectors.md "SECTION_connectors.md").

February 18, 2026

✨ _AI Integration_ — **Aurora DSQL integrates with Kiro
powers and AI agent skills** — Aurora DSQL integration with Kiro powers and AI
agent skills enables developers to build Aurora DSQL-backed applications faster with
AI-assisted development. The Kiro power bundles the Aurora DSQL Model Context Protocol (MCP)
server with development best practices for one-click installation. The Aurora DSQL skill extends the same capabilities
to additional AI coding agents through the Skills CLI. For more information, see [Aurora DSQL Steering: Skills and
Powers](SECTION_aurora-dsql-steering.md "SECTION_aurora-dsql-steering.md").

February 13, 2026

🐘 _PostgreSQL Compatibility_ — **Identity columns and sequence
objects** — Aurora DSQL now supports identity columns and sequence objects,
enabling developers to generate auto-incrementing, integer-based IDs directly in the
database using familiar SQL patterns. For more information, see [Sequences and identity columns](sequences-identity-columns.md "sequences-identity-columns.md").

February 11, 2026

🌍 _Region Expansion_ — **Aurora DSQL available in
Canada and Australia Regions** — Aurora DSQL is now available with single-Region
clusters in Asia Pacific (Melbourne), Asia Pacific (Sydney), Canada (Central), and Canada
West (Calgary). For a complete list of supported Regions, see [Region availability for Aurora DSQL](region-availability.md "region-availability.md").

February 5, 2026

🔌 _Developer Tools_ — **Aurora DSQL Connector for
Go** — Added the Aurora DSQL Connector for Go, which wraps `pgx` with automatic IAM
authentication for token generation, SSL configuration, and connection management. For
more information, see [Connecting
to Aurora DSQL clusters with a Go connector](SECTION_program-with-go-pgx-connector.md "SECTION_program-with-go-pgx-connector.md").

February 3, 2026

🐘 _PostgreSQL Compatibility_ — **Index support for the NUMERIC data
type** — Aurora DSQL now supports indexes on the `NUMERIC` data type,
allowing customers to use `NUMERIC` columns as primary keys and in secondary
indexes for improved query performance on decimal and financial data.

### January 2026

January 15, 2026

🔗 _Integration_ — **Aurora DSQL available in v0 by
Vercel** — AWS databases including Aurora DSQL are now available in v0 by
Vercel, enabling developers to quickly spin up and connect to Aurora DSQL databases directly
from the Vercel platform.

## 2025

### December 2025

December 19, 2025

✨ _AI Integration_ — **AWS Labs Aurora DSQL MCP Server
updates** — Updated MCP Server with installation approaches for Claude Code and
Codex, including CLI-based setup. For more information, see [AWS Labs Aurora DSQL MCP Server](SECTION_aurora-dsql-mcp-server.md "SECTION_aurora-dsql-mcp-server.md").

December 17, 2025

🔗 _Integration_ — **Aurora DSQL available in the Vercel
Marketplace** — AWS databases including Aurora DSQL are now available on the
Vercel Marketplace, allowing developers to provision Aurora DSQL clusters in seconds directly
from Vercel's developer platform.

December 11, 2025

🆕 _Feature_ — **Fast cluster creation** —
Aurora DSQL now supports cluster creation in seconds, enabling developers to instantly
provision Aurora DSQL databases to rapidly prototype new ideas and leverage the integrated
query editor in the AWS Management Console to immediately start building.

December 11, 2025

🆕 _Feature_ — **AWS PrivateLink with Direct Connect
support** — Added private Domain Name System (DNS) setup and the cluster ID
connection option for AWS PrivateLink with Direct Connect or Amazon VPC peering. For more information, see [Managing and connecting to Aurora DSQL clusters using
AWS PrivateLink](privatelink-managing-clusters.md "privatelink-managing-clusters.md").

### November 2025

November 21, 2025

🔌 _Developer Tools_ — **Python, Node.js, and JDBC
Connectors** — Aurora DSQL launches new Python, Node.js, and Java Database
Connectivity (JDBC) connectors that simplify IAM authorization, enabling developers to
connect to Aurora DSQL clusters using standard PostgreSQL drivers with automatic IAM token
management. For more information, see
[Aurora DSQL connectors](SECTION_connectors.md "SECTION_connectors.md").

November 21, 2025

🆕 _Feature_ — **Storage volume increased to 256
TiB** — Aurora DSQL database clusters now support up to 256 terabytes of storage
volume, doubling the previous 128 terabyte limit and allowing customers to store and
manage larger databases within a single database cluster.

November 21, 2025

🆕 _Feature_ — **Integrated Query Editor in AWS
Management Console** — Aurora DSQL now provides an integrated query editor for
browser-based SQL access in the AWS Management Console. Customers can securely connect
to their Aurora DSQL clusters and run SQL queries directly from the console without installing
or configuring external clients. For more information, see [Getting started with the Aurora DSQL Query
Editor](SECTION_getting-started-query-editor.md "SECTION_getting-started-query-editor.md").

November 20, 2025

🆕 _Feature_ — **Statement-level cost estimates in
query plans** — Aurora DSQL now provides statement-level cost estimates and query
plans, surfacing per-category breakdowns including compute, read, write, and multi-Region
costs with total estimated DPUs to help developers immediately get visibility into their
estimated cost profile. For more information, see [Working with Aurora DSQL explain
plans](working-with-dsql-explain-plans.md "working-with-dsql-explain-plans.md").

November 20, 2025

🔗 _Integration_ — **Using JupyterLab with
Aurora DSQL** — Published a step-by-step guide for connecting Aurora DSQL with JupyterLab
for both local and Amazon SageMaker AI environments. For more information, see [Using JupyterLab with Aurora DSQL](SECTION_program-with-jupyter.md "SECTION_program-with-jupyter.md").

### October 2025

October 31, 2025

🆕 _Feature_ — **FIPS 140-3 compliant
endpoints** — Aurora DSQL now supports Federal Information Processing Standards
(FIPS) 140-3 compliant endpoints, enabling customers in regulated industries and
government sectors to meet federal security requirements when connecting to Aurora DSQL
clusters.

October 24, 2025

🆕 _Feature_ — **Resource-based policy
support** — Aurora DSQL now supports resource-based policies, allowing customers
to attach inline policies directly to Aurora DSQL clusters for fine-grained access control
with new permissions: `PutClusterPolicy`, `GetClusterPolicy`, and
`DeleteClusterPolicy`. For more information, see [Resource-based policies for Aurora DSQL](resource-based-policies.md "resource-based-policies.md").

October 23, 2025

🌍 _Region Expansion_ — **Aurora DSQL available in Europe
(Frankfurt)** — Aurora DSQL is now available in the Europe (Frankfurt) Region,
expanding availability for European customers who need to deploy distributed SQL databases
with data residency in the European Union (EU).

### August 2025

August 26, 2025

🆕 _Feature_ — **AWS Fault Injection Service integration** —
Aurora DSQL now integrates with AWS Fault Injection Service (AWS FIS), allowing customers to inject failures
into single-Region and multi-Region Aurora DSQL clusters to test fault tolerance and validate
application error handling and recovery mechanisms.

### July 2025

July 29, 2025

🆕 _Feature_ — **AWS Backup improves Aurora DSQL multi-Region
restore workflow** — AWS Backup improves the Aurora DSQL multi-Region restore workflow,
simplifying the process of restoring Aurora DSQL backups across AWS Regions for disaster
recovery and data migration scenarios. For more information, see [Backup and restore for Aurora DSQL](backup.md "backup.md").

July 3, 2025

🌍 _Region Expansion_ — **Aurora DSQL available in Asia
Pacific (Seoul)** — Aurora DSQL is now available in the Asia Pacific (Seoul)
Region, expanding availability for customers in South Korea and the broader Asia Pacific
region.

### May 2025

May 27, 2025

🚀 _Major Release_ — **General availability of
Aurora DSQL** — Aurora DSQL is now generally available (GA). Aurora DSQL is a serverless,
distributed SQL database with PostgreSQL compatibility, active-active high availability, and
virtually unlimited scale. The GA release includes CloudWatch monitoring, AWS Backup integration,
and data encryption with customer-managed KMS keys. For more information, see [What is Aurora DSQL?](CHAP_what-is.md "CHAP_what-is.md")

May 8, 2025

🆕 _Feature_ — **AWS PrivateLink for
Aurora DSQL** — Aurora DSQL now supports AWS PrivateLink, enabling customers to simplify
private network connectivity between virtual private clouds (VPCs), Aurora DSQL, and
on-premises data centers using interface Amazon VPC endpoints and private IP addresses. For
more information, see [Managing and
connecting to Aurora DSQL clusters using AWS PrivateLink](privatelink-managing-clusters.md "privatelink-managing-clusters.md").

## 2024

### December 2024

December 3, 2024

🚀 _Major Release_ — **Public preview launch of
Aurora DSQL** — Aurora DSQL launches in public preview as a new serverless
distributed SQL database. Aurora DSQL offers virtually unlimited scale, PostgreSQL v16
compatibility, multi-Region active-active support with a 99.999% availability service
level agreement (SLA), IAM
authentication, and optimistic concurrency control. For more information, see [What is Aurora DSQL?](CHAP_what-is.md "CHAP_what-is.md")
