# Amazon Aurora PostgreSQL updates

Following, you can find information about versions of the Amazon Aurora PostgreSQL-Compatible Edition database
engine that have been released for Amazon Aurora.

For more information about Aurora PostgreSQL support dates, including extended and long-term support, see [Release calendars for Aurora PostgreSQL](aurorapostgresql-release-calendar.md "aurorapostgresql-release-calendar.md").

To determine the version number of your Aurora PostgreSQL database, see [Identifying versions of Amazon Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.Updates.md "../AuroraUserGuide/AuroraPostgreSQL.Updates.md") in the _Amazon Aurora User
Guide_.

For information about extensions and modules, see [Extension versions for
Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

For information about Amazon Aurora available releases, policies, and time lines, see [How long Amazon Aurora major versions remain available](../AuroraUserGuide/Aurora.md#Aurora.VersionPolicy.MajorVersionLifetime "../AuroraUserGuide/Aurora.md#Aurora.VersionPolicy.MajorVersionLifetime") in the _Amazon Aurora
User Guide_. For more information about support and other policies for
Amazon Aurora see [Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/ "https://aws.amazon.com/rds/faqs/").

To determine which Aurora PostgreSQL DB engine versions are available in an AWS Region, use
the [describe-db-engine-versions](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command as shown following.

```
aws rds describe-db-engine-versions --engine aurora-postgresql --query '*[].[EngineVersion]' --output text --region `aws-region`
```

For a list of AWS Regions, see [Aurora PostgreSQL Region availability](../AuroraUserGuide/Concepts.md#Aurora.Overview.Availability.PostgreSQL "../AuroraUserGuide/Concepts.md#Aurora.Overview.Availability.PostgreSQL") in the _Amazon Aurora User
Guide_.

###### Topics

- [PostgreSQL 18.1](#AuroraPostgreSQL.Updates.180X "#AuroraPostgreSQL.Updates.180X")
- [PostgreSQL 17 versions](#aurorapostgresql-versions-version17 "#aurorapostgresql-versions-version17")
- [PostgreSQL 16 versions](#aurorapostgresql-versions-version16 "#aurorapostgresql-versions-version16")
- [PostgreSQL 15 versions (includes some deprecated versions)](#aurorapostgresql-versions-version15 "#aurorapostgresql-versions-version15")
- [PostgreSQL 14 versions (includes some deprecated versions)](#aurorapostgresql-versions-version14 "#aurorapostgresql-versions-version14")
- [PostgreSQL 13 versions (includes some deprecated versions)](#aurorapostgresql-versions-version13 "#aurorapostgresql-versions-version13")
- [PostgreSQL 12 versions (includes some deprecated versions)](#aurorapostgresql-versions-version12 "#aurorapostgresql-versions-version12")
- [PostgreSQL 11 versions (includes
  some deprecated versions)](#AuroraPostgreSQL.versions-version11 "#AuroraPostgreSQL.versions-version11")
- [PostgreSQL 10 versions
  (Deprecated)](#AuroraPostgreSQL.versions-version10 "#AuroraPostgreSQL.versions-version10")
- [PostgreSQL 9.6 versions
  (Deprecated)](#AuroraPostgreSQL.versions-version96 "#AuroraPostgreSQL.versions-version96")

## PostgreSQL 18.1

The PostgreSQL community releases new Major versions of PostgreSQL annually. The Amazon RDS Database Preview Environment allows you to test beta, release candidate, and early production versions of Amazon Aurora releases. This allows customers to create DB Clusters on an early release of Aurora PostgreSQL 18 in the Preview environment and test its features.

The following limitations apply to Aurora PostgreSQL Clusters in the Preview environment:

1. All DB instances/clusters are deleted 60 days after you create them, along with any backups and snapshots.
2. You can't copy a snapshot of a DB instance from Preview to a production environment.
3. The following options are supported by the Preview.
   1. You can create DB instances using r6g, r6i, r7g, r7i, r8g, x2g, t3 and t4g instance types only. For more information about RDS Aurora instance classes, see DB instance classes.
   2. You can use both single-AZ and multi-AZ deployments.
   3. You can use standard PostgreSQL dump and load functions to export databases from or import databases to the Database Preview Environment.

Some of the Features that are not supported for APG18.1 Preview:

1. Serverless v1/v2
2. Major Version Upgrades i.e. MVU
3. No new minors will be released in preview region i.e. APG17.1 will not be released in preview region
4. RDS PostgreSQL to Aurora PostgreSQL Inbound replication
5. Amazon RDS Blue/Green deployment
6. Cross-Region snapshot copy
7. Global DB
8. Database Activity Streams (DAS), RDS Proxy and Data Migration Service (DMS)
9. Auto Scaling Read Replicas
10.
11. RDS Export
12. Performance Insights
13. Custom Endpoints
14. Snapshot Copy
15. zero-ETL
16. Babelfish
17. PostGis Topology module is not supported because of a community regression: [https://trac.osgeo.org/postgis/ticket/5983](https://trac.osgeo.org/postgis/ticket/5983 "https://trac.osgeo.org/postgis/ticket/5983")

### Creating a new DB Cluster in the preview environment

Use the following procedure to create a DB Cluster in the preview environment.

###### To create a DB Cluster in the preview environment

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose Dashboard from the navigation pane.
3. In the Dashboard page, locate the Database Preview Environment section on the Dashboard page, as shown in the following image.
4. You can navigate directly to the Database preview environment. Before you can proceed, you must acknowledge and accept the limitations.
5. To create the Aurora PostgreSQL DB instance, follow the same process as that for creating any Amazon Aurora PostgreSQL DB Cluster. For more information, see the Console procedure in Creating an Amazon Aurora PostgreSQL DB cluster.
6. To create an Cluster in the Database Preview Environment using the RDS API or the AWS CLI, use the following endpoint.

`rds-preview.us-east-2.amazonaws.com`

###### Releases and patches

- [Aurora PostgreSQL 18.1 in the Amazon RDS Preview environment](#AuroraPostgreSQL.Updates.181Preview "#AuroraPostgreSQL.Updates.181Preview")

### Aurora PostgreSQL 18.1 in the Amazon RDS Preview environment

**_This is preview documentation for Amazon Aurora PostgreSQL version 18.1. It is subject to change._**

This release of Aurora PostgreSQL is compatible with PostgreSQL 18.1. For more information about the improvements in PostgreSQL 18.1, see [PostgreSQL release 18.0](https://www.postgresql.org/docs/18/release-18.html "https://www.postgresql.org/docs/18/release-18.html") and [PostgreSQL release 18.1](https://www.postgresql.org/docs/18/release-18-1.html "https://www.postgresql.org/docs/18/release-18-1.html").

###### Parameter updates

- `track_cost_delay_timing` default is set to on
- `max_active_replication_origins` default is set to 20
- `client_connection_check_interval` default is set to 60000
- `log_connections` was updated to reflect the new PostgreSQL 18 behavior. The old default value of 0 is equivalent to the new default empty value, and the old value of 1 is equivalent to specifying all three values of receipt, authentication, and authorization
- `autovacuum_worker_slots`, `io_workers`, `io_max_concurrency`

###### Extension updates

- Added new extension pg_roaringbitmap version 0.5.5
- Updated h3-pg to version 4.2.3
- Updated PostGIS to version 3.6.0
- Updated pg_hint_plan to version 1.8.0
- Updated pg_cron to version 1.6.7
- Updated hypopg to version 1.4.2
- Updated MySQL FDW to version REL-2_9_3
- Updated pglogical to version 2.4.6
- Updated pgvector to version 0.8.1
- Updated PLv8 to version 3.2.4
- Updated TDS FDW to version 2.0.5
- Updated pg_tle to version 1.5.2
- Updated PgAudit to version 18.0
- Updated to PgRouting to version 3.8.0

###### General enhancements

- Reduced commit latency when I/O optimized is enabled

###### Unsupported Features

- Aurora PostgreSQL 18.1 will only support io_method of worker.
- Aurora PostgreSQL 18.1 does not currently support logical decoding on Aurora Read Replicas.
- Aurora PostgreSQL 18.1 does not currently support failover control within a Cluster.
- Aurora PostgreSQL 18.1 does not currently support pg_createsubscriber on Aurora Read Replicas.
- Aurora PostgreSQL 18.1 does not currently support Aurora PostgreSQL Query Plan Management.
- Aurora PostgreSQL 18.1 does not currently support in-region write forwarding

## PostgreSQL 17 versions

###### Version updates

- [PostgreSQL 17.7](#aurorapostgresql-versions-version177x "#aurorapostgresql-versions-version177x")
- [PostgreSQL 17.6](#aurorapostgresql-versions-version176x "#aurorapostgresql-versions-version176x")
- [PostgreSQL 17.5](#aurorapostgresql-versions-version175x "#aurorapostgresql-versions-version175x")
- [PostgreSQL 17.4](#aurorapostgresql-versions-version174x "#aurorapostgresql-versions-version174x")
- [PostgreSQL 17.0](#AuroraPostgreSQL.Updates.170X "#AuroraPostgreSQL.Updates.170X")

### PostgreSQL 17.7

This release of Aurora PostgreSQL is compatible with PostgreSQL 17.7. For more information about
the improvements in PostgreSQL 17.7, see [PostgreSQL release
17.7](https://www.postgresql.org/docs/17/release-17-7.html "https://www.postgresql.org/docs/17/release-17-7.html").

###### Releases and patches

- [Aurora PostgreSQL 17.7.1, January 16th, 2026](#aurorapostgresql-versions-version1771x-1771 "#aurorapostgresql-versions-version1771x-1771")
- [Aurora PostgreSQL 17.7, December, 18, 2025](#aurorapostgresql-versions-version177x-177 "#aurorapostgresql-versions-version177x-177")

#### Aurora PostgreSQL 17.7.1, January 16th, 2026

**Critical stability enhancements**

- Fixed a timing condition in the aws_s3 extension which, in rare cases, can cause database unavailability
- Fixed an issue where an UPDATE statement with OUTPUT clause may skip rows when there are concurrent updates on the same row

#### Aurora PostgreSQL 17.7, December, 18, 2025

**New features**

- Introduced a change which improves static availability of Aurora PostgreSQL writers when, in rare conditions, write operations to storage are delayed due to undergoing storage node maintenance.
- Improvements to minimize switchover downtime during Blue/Green switchover operations, by temporarily blocking transaction commit operations on the Blue environment prior to switchover, reducing drift between the Blue and Green clusters.
- Improved recovery time by optimizing commit log (clog) loading during database cold starts and unplanned restarts, with significant benefits for smaller instances with limited CPU cores.

**Critical stability enhancements**

- Improved cold start performance through faster cache initialization.
- Reduced memory footprint for idle connections in Serverless v2 instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")

- Fixed a database shutdown issue that could cause major version upgrades to fail.
- Fixed a rare major version upgrade failure with large memory allocations.
- Fixed an issue preventing rds_superuser from managing prepared transactions owned by other users.

**General enhancements**

- Updated the following extensions:
  - h3_pg to version 4.2.3.

- Fixed NOTIFY channel file cleanup issue that could cause excessive storage usage
- Fixed a race condition in Postgres lock release with optimized read enabled
- Improved PgAudit memory usage during parameter-heavy operations.
- Fixed a database initialization failure when max_connections is set to low values.
- Improved Serverless v2 scaling performance under high CPU load.
- Improved Serverless v2 write performance.
- Fixed delays in Serverless v2 scale-down operations.
- Fixed multiple low-risk memory leaks.
- Improved database shutdown during maintenance to enhance availability.
- Improved database startup performance through optimized storage initialization.
- Fixed storage metadata initialization issue that could delay engine startup.
- Fixed region determination failures in aws_s3, aws_ml, and aws_lambda extensions.
- Provided configuration in pg_columnmask extension's masking policies to allow predicates on masked columns in queries.
- Fixed role argument quoting in pg_columnmask policy management procedures.
- Fixed policy visibility in the pg_columnmask.ddm_policies view for administrators.
- Fixed a crash condition when using pg_buffercache extension during Serverless v2 scaling.

### PostgreSQL 17.6

This release of Aurora PostgreSQL is compatible with PostgreSQL 17.6. For more information about
the improvements in PostgreSQL 17.6, see [PostgreSQL release
17.6](https://www.postgresql.org/docs/17/release-17-6.html "https://www.postgresql.org/docs/17/release-17-6.html").

###### Releases and patches

- [Aurora PostgreSQL 17.6.1, November 25, 2025](#aurorapostgresql-versions-version1761x-1761 "#aurorapostgresql-versions-version1761x-1761")
- [Aurora PostgreSQL 17.6, November 25, 2025](#aurorapostgresql-versions-version176x-176 "#aurorapostgresql-versions-version176x-176")

#### Aurora PostgreSQL 17.6.1, November 25, 2025

**Critical stability enhancements**

- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")

- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 17.6, November 25, 2025

**New features**

- Introduced Dynamic Data Masking (DDM), a database-level security feature that protects sensitive data by masking column values before they are presented to database clients, without modifying the actual stored data. DDM enables organizations to control access to Personally Identifiable Information (PII) and other sensitive data through role-based masking policies that are applied dynamically at query execution time. For more details visit [Dynamic Data Masking](../AuroraUserGuide/AuroraPostgreSQL.Security.md "../AuroraUserGuide/AuroraPostgreSQL.Security.md").
- Introduced Shared Plan Cache to reduce memory usage by sharing query plans between backend processes.
- Added support for correlated subquery cache for EXISTS, NOT EXISTS, and row comparison subqueries.
- Introduced a new feature to significantly reduce database downtime during restarts by initializing Aurora storage metadata in parallel and reducing contention during initialization.
- Added new pg_columnmask extension

**Critical stability enhancements**

- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed an issue where clusters with enhanced logical replication (aurora.enhanced_logical_replication) enabled could experience instance restarts when decoding DDL-heavy workloads.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/")
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/")
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/")

- Fixed an issue in logical replication where subscriber databases could skip replicating transactions after recovering from a crash.
- Fixed an issue which could prevent logical replication from resuming after upgrade.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed a security issue when altering routine ownership.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

**General enhancements**

- Updated the following extensions:
  - oracle_fdw to version to 2.8.0
  - pg_repack extension to version 1.5.2
  - aws_lamba extension to version 2.0

- Improvements to the replay performance of the Aurora WAL replay process on read replica instances.
- Improved file metadata initialization times.
- Fixed an issue that caused reader instance to restart when attempting to create PostgreSQL SLRU files.
- Fixed an issue which caused prolonged Serverless v2 scaling time.
- Fixed an issue that could cause database restart during Serverless v2 scaling.
- Fixed a performance issue on 48xlarge graviton instances.
- Fixed a timing issue in replication diagnostics that could prevent accurate reporting of Aurora replica recovery status when state transitions occur in rapid succession.
- Updated the aws_lambda extension to version 2.0, which resolves a performance issue that was present in version 1.0.
- Added support to include Geodetic TIFF grid files for PROJ.
- Fixed an issue that could cause database restart during aws_s3 export.
- Addressed an issue with logging when replication slots are invalidated.
- Fixed CVE-2023-3079 for V8 Engine in the PLV8 extension.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue where read queries may time out on Aurora replica nodes during the replay of lazy truncation triggered by vacuum on the writer node.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue which prevented online recovery of an Aurora Replica forcing offline recovery.

### PostgreSQL 17.5

This release of Aurora PostgreSQL is compatible with PostgreSQL 17.5. For more information about
the improvements in PostgreSQL 17.5, see [PostgreSQL release
17.5](https://www.postgresql.org/docs/17/release-17-5.html "https://www.postgresql.org/docs/17/release-17-5.html").

###### Releases and patches

- [Aurora PostgreSQL 17.5.4, January 15,
  2026](#aurorapostgresql-versions-version1754x-1754 "#aurorapostgresql-versions-version1754x-1754")
- [Aurora PostgreSQL 17.5.3, September 16,
  2025](#aurorapostgresql-versions-version1753x-1753 "#aurorapostgresql-versions-version1753x-1753")
- [Aurora PostgreSQL 17.5.2, August 8,
  2025](#aurorapostgresql-versions-version1752x-1752 "#aurorapostgresql-versions-version1752x-1752")
- [Aurora PostgreSQL 17.5.1, June 30,
  2025](#aurorapostgresql-versions-version1751x-1751 "#aurorapostgresql-versions-version1751x-1751")
- [Aurora PostgreSQL 17.5, June 30,
  2025](#aurorapostgresql-versions-version175x-175 "#aurorapostgresql-versions-version175x-175")

#### Aurora PostgreSQL 17.5.4, January 15,

2026

**Critical stability enhancements**

- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 17.5.3, September 16,

2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few
  seconds longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that
  might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when fetching
  pages from storage.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security
  vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed an issue that can cause reboots of the primary db instance when reading from a
  logical replication slot in the presence of frequent DDL if
  aurora.enhanced_logical_replication is enabled.
- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from
  completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on
  tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately
  after installing the extension or resetting shared memory.
- Fixed an issue with Babelfish ZDP that could lead to instance reboot after
  minor version ugprade in some cases.
- Fixed an issue in enforcing, validating and evolving the `plans` extension
  in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with
  all-column selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release
  containing The `PostGIS` extension 3.5.1 without running
  postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart
  of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans`
  extension using the “bitmap heap scan” access method.
- Fixed an issue impacting query execution performance for execution the
  `plans` extension using the “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 17.5.2, August 8,

2025

**Critical stability enhancements**

- Fixed an issue which could prevent logical replication from resuming after
  upgrade.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when
  performing reads from Aurora Storage.

#### Aurora PostgreSQL 17.5.1, June 30,

2025

**High priority enhancements**

- Fixed a performance issue affecting instance restart operations.
- Fixed an issue where newly created storage volume keys were incorrectly cleaned up
  causing periodic restarts.

#### Aurora PostgreSQL 17.5, June 30,

2025

**New features**

- Improved Serverless v2 scaling for storage bound workloads.
- Improved Serverless v2 scaling through optimized management of memory maps.
- Aurora has doubled its maximum storage capacity from 128 TiB to 256 TiB. This
  increased storage limit allows customers to manage larger workloads in a single DB
  cluster. To access the increased storage limit for Aurora PostgreSQL, upgrade your DB cluster
  to version 17.5, 16.9, 15.13, or higher. Once upgraded, Aurora storage will automatically
  scale up to 256 TiB capacity based on the amount of data in the cluster volume.

**Critical stability enhancements**

- Fixed an issue where Serverless instances would fail to perform Zero Downtime Patching
  after automatic resume.
- Added library dependency verification during minor and patch upgrades to ensure
  storage metadata recovery is safe before proceeding.

**High priority enhancements**

- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads.
- Fixed an issue where server will fail to start if a previous startup was prematurely
  terminated.

**General enhancements**

- Updated the following extensions:
  - apg_plan_mgmt to 2.9.
  - The `pgaudit` extension to 17.1.
  - The `rdkit` extension to 4.6.1 (2024_09_6).

- Improvements to make Serverless v2 scaling more efficient on reader nodes.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  sub-transactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue that prevents Zero Downtime Patching from completing successfully on
  Serverless v2 auto-pause enabled instances.
- Fixed an issue in pgdam that causes the engine (with pgdam enabled) to crash when
  hitting maximum connections.
- Fixed an issue in the `pg_bigm` extension that can cause unavailability
  when the extension interacts with the GIN index.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
- Added validation to ensure only predefined GUCs with `aurora_stat_plans`
  the `prefix` extension are accepted on SET or SHOW commands.
- Added function aurora_stat_resource_usage() to report current CPU usage, allocated and
  used memory for all the backends.
- Fixed an issue which prevented ZDP when cache recovery is disabled.
- Fixed a synchronization issue where ZDP could fail due to premature engine ready state
  reporting.
- Fixed an issue in checkpoint replication to have storage metadata position be
  consistent in reader.
- Fixed an issue which causes RO node to restart while it’s reconnecting to RW
  node.
- Fixed an issue which causes instability to Zero-ETL integrations due to stale caches
  in the presence of frequent ALTER TABLE commands.
- Fixed an issue where RO client process can be stuck in LWLock:BufferIO wait event
  after being disconnected from the writer.
- Fixed an issue where RO node could crash when frequently falling behind RW
  node.
- Fixed an issue in the `aws_s3` extension that could cause an import
  operation to restart and reinsert previously inserted rows.
- Improved performance of EXPLAIN operations for queries involving tables with many
  columns and complex relations.
- Added separate GUC `apg_enable_correlated_scalar_index_transform` (OFF by
  default) to control whether to transform the correlated subquery when the correlated
  column in the inner table is a leading column of any index.

### PostgreSQL 17.4

This release of Aurora PostgreSQL is compatible with PostgreSQL 17.4. For more information about
the improvements in PostgreSQL 17.4, see [PostgreSQL release
17.4](https://www.postgresql.org/docs/17/release-17-4.html "https://www.postgresql.org/docs/17/release-17-4.html").

###### Releases and patches

- [Aurora PostgreSQL 17.4.5, February 02, 2026](#aurorapostgresql-versions-version1745x-1745 "#aurorapostgresql-versions-version1745x-1745")
- [Aurora PostgreSQL 17.4.4, October 9, 2025](#aurorapostgresql-versions-version1744x-1744 "#aurorapostgresql-versions-version1744x-1744")
- [Aurora PostgreSQL 17.4.3, June 03, 2025](#aurorapostgresql-versions-version1743x-1743 "#aurorapostgresql-versions-version1743x-1743")
- [Aurora PostgreSQL 17.4.2, May 01,
  2025](#aurorapostgresql-versions-version1742x-1742 "#aurorapostgresql-versions-version1742x-1742")
- [Aurora PostgreSQL 17.4, May 01, 2025](#aurorapostgresql-versions-version174x-174 "#aurorapostgresql-versions-version174x-174")

#### Aurora PostgreSQL 17.4.5, February 02, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://nvd.nist.gov/vuln/detail/CVE-2025-12817 "https://nvd.nist.gov/vuln/detail/CVE-2025-12817").
  - [CVE-2025-12818](https://nvd.nist.gov/vuln/detail/CVE-2025-12818 "https://nvd.nist.gov/vuln/detail/CVE-2025-12818").

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself.
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 17.4.4, October 9, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds
  longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might
  result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables
  larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after
  installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving the `plans` extension in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with all-column
  selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing
  The `PostGIS` extension 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an
  Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans` extension using the “bitmap
  heap scan” access method.
- Fixed an issue impacting query execution performance for execution the `plans` extension using the
  “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 17.4.3, June 03, 2025

**Critical stability enhancements**

- Fixed stuck scaling for serverless db instances with zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing actions
  with Aurora Storage.
- Fixed an issue related to the interaction between Aurora Serverless scaling and the improved
  reader availability functionality that might result in longer recover times and impact
  availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.
- Fixed an issue in handling parameter lists from previous versions of query plan management.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Fixed an issue that can cause RO instance crash under heavy workload.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.

#### Aurora PostgreSQL 17.4.2, May 01,

2025

**Critical priority enhancements**

- Fixed stuck scaling for serverless db instances with zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing
  actions with Aurora storage.

#### Aurora PostgreSQL 17.4, May 01, 2025

**New features**

- Aurora Optimized Reads now enables users to resize the allocated space for Optimized
  Reads-enabled temporary objects on Aurora I/O-Optimized clusters using a dynamic parameter
  `aurora_temp_space_size`. For more information, see [Aurora Optimized Reads](../AuroraUserGuide/AuroraPostgreSQL.optimized.md "../AuroraUserGuide/AuroraPostgreSQL.optimized.md").
- Added support for transforming correlated subquery into derived table to improve
  execution efficiency. For more information, see [Improving Aurora PostgreSQL query performance using subquery transformation](../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation "../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation") .
- Added support for caching the result of correlated subquery to improve execution
  efficiency. For more information, see [Using subquery cache to improve Aurora PostgreSQL query performance](../AuroraUserGuide/apg-correlated-subquery.md#apg-subquery-cache "../AuroraUserGuide/apg-correlated-subquery.md#apg-subquery-cache").
- Added adaptive join (preview feature) to dynamically optimize query performance by
  switching from nested loop to hash join operations at runtime when the PostgreSQL
  optimizer makes suboptimal join choices due to cardinality estimate errors. For more
  information on adaptive join, see [Improving query
  performance using adaptive join](../AuroraUserGuide/user-apg-adaptive-join.md "../AuroraUserGuide/user-apg-adaptive-join.md").

**Critical stability enhancements**

- When the system is under critical memory pressure for an extended duration, the
  largest customer backend will be cancelled to prevent system from restarting due to out of
  memory.

**High priority enhancements**

- The `rds.force_ssl` parameter is now set to 1 (on) by default in version 17
  and newer versions, enforcing SSL connections for enhanced security. For more information,
  see [Requiring an SSL/TLS connection to an Aurora PostgreSQL DB cluster](../AuroraUserGuide/AuroraPostgreSQL.md#AuroraPostgreSQL.Security.SSL.Requiring "../AuroraUserGuide/AuroraPostgreSQL.md#AuroraPostgreSQL.Security.SSL.Requiring").
- Fixed an issue where Aurora in-Region failovers would result in failures in database
  startup.
- Fixed a security issue in the `rds_activity_stream` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation.
  For more information, see [AWS-LC
  is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/") on AWS Security Blog.
- Aurora storage metadata now initializes more quickly during unplanned failovers and
  server restarts, reducing overall downtime. Larger instances benefit the most by
  leveraging higher parallelism.
- Improved performance of file metadata operations.
- Made improvements to database downtime during a `planned` extension
  switchover for Global Databases.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
  - Creating temporary objects with syntax such as CREATE TEMPORARY TABLE x AS SELECT \* FROM isn't supported.
  - Creating indexes on temporary tables isn't supported.

- The Blue/Green deployment switchover won’t be blocked by the `REFRESH
MATERIALIZED VIEW` statement.
- Updated the following parameter names to align with the PostgreSQL 17 version:
  - `multixact_offsets_cache_size` is now
    `multixact_offset_buffers`
  - `multixact_members_cache_size` is now
    `multixact_member_buffers`

- Improved allocation of Write-Ahead Log (WAL) stream numbers, resulting in increased
  throughput for write-heavy workloads on the new Graviton 4 high-end instances.
- Fixed an issue where the query identifier (queryid) wasn't being correctly updated in
  pg_stat_activity when using extended protocol in pipeline mode.
- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes
  to become stuck indefinitely.
- Updated the following extensions:
  - `pgvector` extension to 0.8.0.
  - `pg_cron` extension to v1.6.5.
  - `tds_fdw` extension to 2.0.4.
  - `postgis` extension to 3.5.1.
  - `pg_partman` extension to v5.2.4.
  - `orafce` extension to 4.14.0.
  - `rds_tools` extension to 1.9.
  - `rdkit` extension to Release_2024_09_3.
  - pg_repack extension to 1.5.1.
  - pglogical extension to 2.4.5.

### PostgreSQL 17.0

This release of Aurora PostgreSQL is compatible with PostgreSQL 17.0. For more information
about the improvements in PostgreSQL 17.0, see [PostgreSQL release
17.0](https://www.postgresql.org/docs/17/release-17.html "https://www.postgresql.org/docs/17/release-17.html").

To learn more on how to work with Database preview environment, see [Working with the database preview environment](../AuroraUserGuide/working-with-the-apg-database-preview-environment.md "../AuroraUserGuide/working-with-the-apg-database-preview-environment.md").

###### Releases and patches

- [Aurora PostgreSQL 17.0 in the Amazon RDS
  Preview environment, November 20, 2024](#AuroraPostgreSQL.Updates.170Preview "#AuroraPostgreSQL.Updates.170Preview")

#### Aurora PostgreSQL 17.0 in the Amazon RDS

Preview environment, November 20, 2024

**_This is
preview documentation for Amazon Aurora PostgreSQL version 17.0. It is
subject to change._**

###### General enhancements

- Reduced commit latency when I/O optimized is enabled.

###### Unsupported features in the preview version of Aurora PostgreSQL 17.0

- Logical decoding on Aurora Read Replicas.
- Failover control within a database cluster.
- `pg_createsubscriber` on Aurora Read Replicas.
- Aurora PostgreSQL query plan management.
- Aurora PostgreSQL local write forwarding.

###### Important

The Aurora PostgreSQL 17.0 preview release includes fixes for recent PostgreSQL
CVEs. These fixes may affect your login roles.

For details on the CVEs, see the [PostgreSQL release announcement](https://www.postgresql.org/about/news/postgresql-171-165-159-1414-1317-and-1221-released-2955/ "https://www.postgresql.org/about/news/postgresql-171-165-159-1414-1317-and-1221-released-2955/").

For information about the potential impact on login roles, refer to this [PostgreSQL mailing list post](https://www.postgresql.org/message-id/CADOZwSb0UsEr4_UTFXC5k7%3DfyyK8uKXekucd%2B-uuGjJsGBfxgw%40mail.gmail.com "https://www.postgresql.org/message-id/CADOZwSb0UsEr4_UTFXC5k7%3DfyyK8uKXekucd%2B-uuGjJsGBfxgw%40mail.gmail.com").

## PostgreSQL 16 versions

###### Migrating to Aurora PostgreSQL 16

The following minumum extension versions are required for major version upgrade to
Aurora PostgreSQL 16:

- PostGIS version 3.1
- PgRouting version 3.0.5
- Rdkit version 4.2

For more information on migration, see [Migration
to Version 16](https://www.postgresql.org/docs/16/release-16.html#RELEASE-16-MIGRATION "https://www.postgresql.org/docs/16/release-16.html#RELEASE-16-MIGRATION") and [Migration to Version 16.1](https://www.postgresql.org/docs/16/release-16-1.html#RELEASE-16-1-MIGRATION "https://www.postgresql.org/docs/16/release-16-1.html#RELEASE-16-1-MIGRATION").

For information about supported extensions versions for each Aurora PostgreSQL version,
see [Extension versions for
Amazon Aurora PostgreSQL](AuroraPostgreSQL.md "AuroraPostgreSQL.md").

To upgrade your Aurora PostgreSQL DB cluster including upgrading your extensions, see [Upgrading PostgreSQL extensions](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades").

###### Unsupported Features

- Aurora PostgreSQL 16 versions doesn't currently support logical decoding on Aurora Read
  Replicas.

###### Differences between PostgreSQL 16 and Aurora PostgreSQL 16

In Aurora PostgreSQL 16 versions, the newly introduced `pg_stat_io` view has
two additional I/O contexts:

- `index`: I/O operations performed during index creation.
- `walreplay`: I/O operations performed by the wal replay process on
  Aurora read replicas.

The following backend types and I/O contexts are not applicable to Aurora read
replicas:

- autovacuum launcher
- autovacuum worker
- bulkwrite
- index
- vacuum

In addition, Aurora PostgreSQL doesn't support writebacks and sync operations since data is
persisted to Aurora storage.

###### Version updates

- [PostgreSQL 16.11](#aurorapostgresql-versions-version1611x "#aurorapostgresql-versions-version1611x")
- [PostgreSQL 16.10](#aurorapostgresql-versions-version1610x "#aurorapostgresql-versions-version1610x")
- [PostgreSQL 16.9](#aurorapostgresql-versions-version169x "#aurorapostgresql-versions-version169x")
- [PostgreSQL 16.8](#aurorapostgresql-versions-version168x "#aurorapostgresql-versions-version168x")
- [PostgreSQL 16.6](#aurorapostgresql-versions-version166x "#aurorapostgresql-versions-version166x")
- [PostgreSQL 16.4](#aurorapostgresql-versions-version164x "#aurorapostgresql-versions-version164x")
- [PostgreSQL 16.3](#aurorapostgresql-versions-version163x "#aurorapostgresql-versions-version163x")
- [PostgreSQL 16.2](#AuroraPostgreSQL.Updates.20180305.162X "#AuroraPostgreSQL.Updates.20180305.162X")
- [PostgreSQL 16.1](#AuroraPostgreSQL.Updates.20180305.161X "#AuroraPostgreSQL.Updates.20180305.161X")

### PostgreSQL 16.11

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.11. For more information about
the improvements in PostgreSQL 16.11, see [PostgreSQL release
16.11](https://www.postgresql.org/docs/16/release-16-11.html "https://www.postgresql.org/docs/16/release-16-11.html").

###### Releases and patches

- [Aurora PostgreSQL 16.11.1, January 16th, 2026](#aurorapostgresql-versions-version16111x-16111 "#aurorapostgresql-versions-version16111x-16111")
- [Aurora PostgreSQL 16.11, December, 18, 2025](#aurorapostgresql-versions-version1611x-1611 "#aurorapostgresql-versions-version1611x-1611")

#### Aurora PostgreSQL 16.11.1, January 16th, 2026

**Critical stability enhancements**

- Fixed a timing condition in the aws_s3 extension which, in rare cases, can cause database unavailability
- Fixed an issue where an UPDATE statement with OUTPUT clause may skip rows when there are concurrent updates on the same row

#### Aurora PostgreSQL 16.11, December, 18, 2025

**New features**

- Introduced a change which improves static availability of Aurora PostgreSQL writers when, in rare conditions, write operations to storage are delayed due to undergoing storage node maintenance.
- Improvements to minimize switchover downtime during Blue/Green switchover operations, by temporarily blocking transaction commit operations on the Blue environment prior to switchover, reducing drift between the Blue and Green clusters.
- Improved recovery time by optimizing commit log (clog) loading during database cold starts and unplanned restarts, with significant benefits for smaller instances with limited CPU cores.

**Critical stability enhancements**

- Improved cold start performance through faster cache initialization.
- Reduced memory footprint for idle connections in Serverless v2 instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")

- Fixed a database shutdown issue that could cause major version upgrades to fail.
- Fixed a rare major version upgrade failure with large memory allocations.
- Fixed an issue preventing rds_superuser from managing prepared transactions owned by other users.

**General enhancements**

- Updated the following extensions:
  - h3_pg to version 4.2.3.

- Fixed NOTIFY channel file cleanup issue that could cause excessive storage usage
- Fixed a race condition in Postgres lock release with optimized read enabled
- Improved PgAudit memory usage during parameter-heavy operations.
- Fixed a database initialization failure when max_connections is set to low values.
- Improved Serverless v2 scaling performance under high CPU load.
- Improved Serverless v2 write performance.
- Fixed delays in Serverless v2 scale-down operations.
- Fixed multiple low-risk memory leaks.
- Improved database shutdown during maintenance to enhance availability.
- Improved database startup performance through optimized storage initialization.
- Fixed storage metadata initialization issue that could delay engine startup.
- Fixed region determination failures in aws_s3, aws_ml, and aws_lambda extensions.
- Provided configuration in pg_columnmask extension's masking policies to allow predicates on masked columns in queries.
- Fixed role argument quoting in pg_columnmask policy management procedures.
- Fixed policy visibility in the pg_columnmask.ddm_policies view for administrators.
- Fixed a crash condition when using pg_buffercache extension during Serverless v2 scaling.

### PostgreSQL 16.10

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.10. For more information about
the improvements in PostgreSQL 16.10, see [PostgreSQL release
16.10](https://www.postgresql.org/docs/16/release-16-10.html "https://www.postgresql.org/docs/16/release-16-10.html").

###### Releases and patches

- [Aurora PostgreSQL 16.10.1, November 25, 2025](#aurorapostgresql-versions-version16101x-16101 "#aurorapostgresql-versions-version16101x-16101")
- [Aurora PostgreSQL 16.10, November 25, 2025](#aurorapostgresql-versions-version1610x-1610 "#aurorapostgresql-versions-version1610x-1610")

#### Aurora PostgreSQL 16.10.1, November 25, 2025

**Critical stability enhancements**

- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")

- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 16.10, November 25, 2025

**New features**

- Introduced Dynamic Data Masking (DDM), a database-level security feature that protects sensitive data by masking column values before they are presented to database clients, without modifying the actual stored data. DDM enables organizations to control access to Personally Identifiable Information (PII) and other sensitive data through role-based masking policies that are applied dynamically at query execution time. For more details visit [Dynamic Data Masking](../AuroraUserGuide/AuroraPostgreSQL.Security.md "../AuroraUserGuide/AuroraPostgreSQL.Security.md").
- Introduced Shared Plan Cache to reduce memory usage by sharing query plans between backend processes.
- Added support for correlated subquery cache for EXISTS, NOT EXISTS, and row comparison subqueries.
- Introduced a new feature to significantly reduce database downtime during restarts by initializing Aurora storage metadata in parallel and reducing contention during initialization.
- Added new pg_columnmask extension

**Critical stability enhancements**

- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed an issue where clusters with enhanced logical replication (aurora.enhanced_logical_replication) enabled could experience instance restarts when decoding DDL-heavy workloads.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/")
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/")
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/")

- Fixed an issue in logical replication where subscriber databases could skip replicating transactions after recovering from a crash.
- Fixed an issue which could prevent logical replication from resuming after upgrade.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed a security issue when altering routine ownership.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

**General enhancements**

- Updated the following extensions:
  - oracle_fdw to version to 2.8.0
  - pg_repack extension to version 1.5.2
  - aws_lamba extension to version 2.0

- Improvements to the replay performance of the Aurora WAL replay process on read replica instances.
- Improved file metadata initialization times.
- Fixed an issue that caused reader instance to restart when attempting to create PostgreSQL SLRU files.
- Fixed an issue which caused prolonged Serverless v2 scaling time.
- Fixed an issue that could cause database restart during Serverless v2 scaling.
- Fixed a performance issue on 48xlarge graviton instances.
- Fixed a timing issue in replication diagnostics that could prevent accurate reporting of Aurora replica recovery status when state transitions occur in rapid succession.
- Updated the aws_lambda extension to version 2.0, which resolves a performance issue that was present in version 1.0.
- Added support to include Geodetic TIFF grid files for PROJ.
- Fixed an issue that could cause database restart during aws_s3 export.
- Addressed an issue with logging when replication slots are invalidated.
- Fixed CVE-2023-3079 for V8 Engine in the PLV8 extension.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue where read queries may time out on Aurora replica nodes during the replay of lazy truncation triggered by vacuum on the writer node.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue which prevented online recovery of an Aurora Replica forcing offline recovery.

### PostgreSQL 16.9

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.9. For more information about
the improvements in PostgreSQL 16.9, see [PostgreSQL release
16.9](https://www.postgresql.org/docs/16/release-16-9.html "https://www.postgresql.org/docs/16/release-16-9.html").

###### Releases and patches

- [Aurora PostgreSQL 16.9.4, January 15,
  2026](#aurorapostgresql-versions-version1694x-1694 "#aurorapostgresql-versions-version1694x-1694")
- [Aurora PostgreSQL 16.9.3, September 16,
  2025](#aurorapostgresql-versions-version1693x-1693 "#aurorapostgresql-versions-version1693x-1693")
- [Aurora PostgreSQL 16.9.2, August 8,
  2025](#aurorapostgresql-versions-version1692x-1692 "#aurorapostgresql-versions-version1692x-1692")
- [Aurora PostgreSQL 16.9.1, June 30,
  2025](#aurorapostgresql-versions-version1691x-1691 "#aurorapostgresql-versions-version1691x-1691")
- [Aurora PostgreSQL 16.9, June 30,
  2025](#aurorapostgresql-versions-version169x-169 "#aurorapostgresql-versions-version169x-169")

#### Aurora PostgreSQL 16.9.4, January 15,

2026

**Critical stability enhancements**

- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 16.9.3, September 16,

2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few
  seconds longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that
  might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when fetching
  pages from storage.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security
  vulnerabilities.
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed an issue that can cause reboots of the primary db instance when reading from a
  logical replication slot in the presence of frequent DDL if
  aurora.enhanced_logical_replication is enabled.
- Fixed a race where old writer may not step down after a new writer is promoted and
  continues to write.

**General enhancements**

- Implemented enhanced error handling mechanisms during TDS Connection reset
  operations.
- Fixed an issue that could in certain cases prevent online recovery of an Aurora Replica
  from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on
  tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately
  after installing the extension or resetting shared memory.
- Fixed an issue with Babelfish ZDP that could lead to instance reboot after
  minor version ugprade in some cases.
- Fixed an issue in enforcing, validating and evolving the `plans` extension
  in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with
  all-column selections.
- Fixed an issue with prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release
  containing The `PostGIS` extension 3.5.1 without running
  postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart
  of an Aurora replica in a Global Database.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 16.9.2, August 8,

2025

**Critical stability enhancements**

- Fixed an issue which could prevent logical replication from resuming after
  upgrade.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when
  performing reads from Aurora Storage.

#### Aurora PostgreSQL 16.9.1, June 30,

2025

**High priority enhancements**

- Fixed a performance issue affecting instance restart operations.

#### Aurora PostgreSQL 16.9, June 30,

2025

**New features**

- Improved Serverless v2 scaling for storage bound workloads.
- Improved Serverless v2 scaling through optimized management of memory maps.
- Aurora has doubled its maximum storage capacity from 128 TiB to 256 TiB. This
  increased storage limit allows customers to manage larger workloads in a single DB
  cluster. To access the increased storage limit for Aurora PostgreSQL, upgrade your DB cluster
  to version 17.5, 16.9, 15.13, or higher. Once upgraded, Aurora storage will automatically
  scale up to 256 TiB capacity based on the amount of data in the cluster volume.

**Critical stability enhancements**

- Fixed an issue where Serverless instances would fail to perform Zero Downtime Patching
  after automatic resume.
- Added library dependency verification during minor and patch upgrades to ensure
  storage metadata recovery is safe before proceeding.

**High priority enhancements**

- Fixed an issue in the `rds_activity_stream extension` that could cause
  brief periods of unavailability during configuration reloads.
- Fixed an issue where server will fail to start if a previous startup was prematurely
  terminated.

**General enhancements**

- Updated the following extensions:
  - apg_plan_mgmt to 2.9.
  - The `pgaudit` extension to 16.1.
  - The `rdkit` extension to 4.6.1 (2024_09_6).
  - The `pg_repack` extension to 1.5.1.
  - The `pglogical` extension to 2.4.5.

- Improvements to make Serverless v2 scaling more efficient on reader nodes.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  sub-transactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue that prevents Zero Downtime Patching from completing successfully on
  Serverless v2 auto-pause enabled instances.
- Fixed an issue in pgdam that causes the engine (with pgdam enabled) to crash when
  hitting maximum connections.
- Fixed an issue in the `pg_bigm` extension that can cause unavailability
  when the extension interacts with the GIN index.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
- Added validation to ensure only predefined GUCs with `aurora_stat_plans`
  the `prefix` extension are accepted on SET or SHOW commands.
- Added function aurora_stat_resource_usage() to report current CPU usage, allocated and
  used memory for all the backends.
- Fixed an issue which prevented Zero Downtime Patching when cache recovery is
  disabled.
- Fixed a synchronization issue where Zero Downtime Patching could fail due to premature
  engine ready state reporting.
- Fixed an issue in checkpoint replication to have storage metadata position be
  consistent in reader.
- Fixed an issue which causes RO node to restart while its reconnecting to RW
  node.
- Fixed an issue which causes instability to Zero-ETL integrations due to stale caches
  in the presence of frequent ALTER TABLE commands.
- Fixed an issue where RO client process can be stuck in LWLock:BufferIO wait event
  after being disconnected from the writer.
- Fixed an issue where RO node could crash when frequently falling behind RW
  node.
- Fixed an issue in the aws_s3 extension that could cause an import operation to restart
  and reinsert previously inserted rows.
- Improved performance of EXPLAIN operations for queries involving tables with many
  columns and complex relations.
- Added separate GUC `apg_enable_correlated_scalar_index_transform` (OFF by
  default) to control whether to transform the correlated subquery when the correlated
  column in the inner table is a leading column of any index.

### PostgreSQL 16.8

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.8. For more information about
the improvements in PostgreSQL 16.8, see [PostgreSQL release
16.8](https://www.postgresql.org/docs/16/release-16-8.html "https://www.postgresql.org/docs/16/release-16-8.html").

###### Releases and patches

- [Aurora PostgreSQL 16.8.5, February 03, 2026](#aurorapostgresql-versions-version1685x-1685 "#aurorapostgresql-versions-version1685x-1685")
- [Aurora PostgreSQL 16.8.4, October 9, 2025](#aurorapostgresql-versions-version1684x-1684 "#aurorapostgresql-versions-version1684x-1684")
- [Aurora PostgreSQL 16.8.3, June 03, 2025](#aurorapostgresql-versions-version1683x-1683 "#aurorapostgresql-versions-version1683x-1683")
- [Aurora PostgreSQL 16.8.2, May 01,
  2025](#aurorapostgresql-versions-version1682x-1682 "#aurorapostgresql-versions-version1682x-1682")
- [Aurora PostgreSQL 16.8, April 07,
  2025](#aurorapostgresql-versions-version168x-168 "#aurorapostgresql-versions-version168x-168")

#### Aurora PostgreSQL 16.8.5, February 03, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://nvd.nist.gov/vuln/detail/CVE-2025-12817 "https://nvd.nist.gov/vuln/detail/CVE-2025-12817").
  - [CVE-2025-12818](https://nvd.nist.gov/vuln/detail/CVE-2025-12818 "https://nvd.nist.gov/vuln/detail/CVE-2025-12818").

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself.
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 16.8.4, October 9, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds
  longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might
  result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables
  larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after
  installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving the `plans` extension in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with all-column
  selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing
  The `PostGIS` extension 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an
  Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans` extension using the “bitmap
  heap scan” access method.
- Fixed an issue impacting query execution performance for execution the `plans` extension using the
  “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 16.8.3, June 03, 2025

**Critical stability enhancements**

- Fixed stuck scaling for serverless db instances with Zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing actions
  with Aurora Storage.
- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.
- Fixed an issue in handling parameter lists from previous versions of query plan management.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Fixed an issue that can cause RO instance crash under heavy workload.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.

#### Aurora PostgreSQL 16.8.2, May 01,

2025

**Critical priority enhancements**

- Fixed stuck scaling for serverless db instances with ZeroETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing
  actions with Aurora storage.

#### Aurora PostgreSQL 16.8, April 07,

2025

**New features**

- Aurora Optimized Reads now enables users to resize the allocated space for Optimized
  Reads-enabled temporary objects on Aurora I/O-Optimized clusters using a dynamic parameter
  “aurora_temp_space_size”. For more information, see [Aurora
  Optimized Reads](../AuroraUserGuide/AuroraPostgreSQL.optimized.md "../AuroraUserGuide/AuroraPostgreSQL.optimized.md").
- Added support for transforming correlated subquery into derived table to improve
  execution efficiency. For more information, see [Improving Aurora PostgreSQL query performance using subquery transformation](../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation "../AuroraUserGuide/apg-correlated-subquery.md#apg-corsubquery-transformation") .
- Added support for caching the result of correlated subquery to improve execution
  efficiency. For more information, see [Using subquery cache to improve Aurora PostgreSQL query performance](../AuroraUserGuide/apg-correlated-subquery.md#apg-subquery-cache "../AuroraUserGuide/apg-correlated-subquery.md#apg-subquery-cache").

**Critical stability enhancements**

- Improved private memory allocation instrumentation to reduce CPU overhead for
  compute-heavy workloads that frequently invoke aset and slab allocation calls with
  `palloc`.
- When the system is under critical memory pressure for an extended duration, the
  largest customer backend will be cancelled to prevent system from restarting due to out of
  memory.

**High priority enhancements**

- Fixed an issue where Aurora in-Region failovers would result in failures in database
  startup.
- Fixed a security issue in the `rds_activity_stream` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**.

- Aurora storage metadata now initializes more quickly during unplanned failovers and
  server restarts, reducing overall downtime. Larger instances benefit the most by
  leveraging higher parallelism.
- Improved performance of file metadata operations.
- Made improvements to database downtime during a `planned` extension
  switchover for Global Databases.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
  - Creating temporary objects with syntax such as CREATE TEMPORARY TABLE x AS SELECT \* FROM isn't supported.
  - Creating indexes on temporary tables isn't supported.

- The Blue/Green deployment switchover won’t be blocked by the `REFRESH
MATERIALIZED VIEW` statement.
- Improved allocation of Write-Ahead Log (WAL) stream numbers, resulting in increased
  throughput for write-heavy workloads on the new Graviton 4 high-end instances.
- Fixed an issue where the query identifier (queryid) wasn't being correctly updated in
  pg_stat_activity when using extended protocol in pipeline mode.
- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes
  to become stuck indefinitely.
- Updated the following extensions:
  - Update the `pgvector` extension to 0.8.0.
  - Update the `pg_cron` extension to v1.6.5.
  - Update the `tds_fdw` extension to 2.0.4.
  - Update the `postgis` extension to 3.5.1.
  - Update the `pg_partman` extension to v5.2.4.
  - Update the `orafce` extension to 4.14.0.
  - Update the `rds_tools` extension to 1.9.
  - Update the `rdkit` extension to Release_2024_09_3.

### PostgreSQL 16.6

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.6. For more information about
the improvements in PostgreSQL 16.6, see [PostgreSQL release
16.6](https://www.postgresql.org/docs/16/release-16-6.html "https://www.postgresql.org/docs/16/release-16-6.html").

###### Releases and patches

- [Aurora PostgreSQL 16.6.7, January 28, 2026](#aurorapostgresql-versions-version1667x-1667 "#aurorapostgresql-versions-version1667x-1667")
- [Aurora PostgreSQL 16.6.6, November 13, 2025](#aurorapostgresql-versions-version1666x-1666 "#aurorapostgresql-versions-version1666x-1666")
- [Aurora PostgreSQL 16.6.5, June 24, 2025](#aurorapostgresql-versions-version1665x-1665 "#aurorapostgresql-versions-version1665x-1665")
- [Aurora PostgreSQL 16.6.4, March 24,
  2025](#aurorapostgresql-versions-version1664x-1664 "#aurorapostgresql-versions-version1664x-1664")
- [Aurora PostgreSQL 16.6.3, February 13,
  2025](#aurorapostgresql-versions-version1663x-1663 "#aurorapostgresql-versions-version1663x-1663")
- [Aurora PostgreSQL 16.6.2, January 20,
  2025](#aurorapostgresql-versions-version1662x-1662 "#aurorapostgresql-versions-version1662x-1662")
- [Aurora PostgreSQL 16.6.1, December 27,
  2024](#aurorapostgresql-versions-version1661x-1661 "#aurorapostgresql-versions-version1661x-1661")
- [Aurora PostgreSQL 16.6, December 27,
  2024](#aurorapostgresql-versions-version166x-166 "#aurorapostgresql-versions-version166x-166")

#### Aurora PostgreSQL 16.6.7, January 28, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 16.6.6, November 13, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 16.6.5, June 24, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 16.6.4, March 24,

2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 16.6.3, February 13,

2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8` extension.

#### Aurora PostgreSQL 16.6.2, January 20,

2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue in Global DB switchover and failover that could result in customers
  needing to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some
  cases.

**General enhancements**

- Fixed an ownership issue where the `postgis_raster` extension could not be
  updated correctly from a previous the `PostGIS` extension v2
  installation.

#### Aurora PostgreSQL 16.6.1, December 27,

2024

**Critical Priority enhancements**

- Fixed an issue where the server was restarting when the connections were reset by the
  peer.

#### Aurora PostgreSQL 16.6, December 27,

2024

###### New features

- Improved Aurora Global Database cross-Region resilience. This ensures secondary region
  read availability during unexpected issues like hardware failures, network disruption
  across regions, and others. For more information, see [Cross-Region resiliency for Global Database secondary clusters](../AuroraUserGuide/aurora-global-database-secondary-availability.md "../AuroraUserGuide/aurora-global-database-secondary-availability.md").
- Optimized the minor version and patch upgrade process to reduce downtime for read
  replicas.
- Performance enhancements that improve write throughput for 32xl and larger instances
  running on I/O-Optimized configuration.

###### Critical stability enhancements

- Fixed an issue that in rare cases can cause CPU usage spike.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")

- Fixed an issue related to logical replication when processing large aborted
  transactions in the presence of catalog modifying operations. This can result in a
  transient failure of the logical replication process.

###### General enhancements

- Improved handling of read replica lag, leading to higher write throughput on larger
  instances during peak usage.
- Made multiple improvements to Aurora in-Region failover which reduces database downtime
  further by improving storage metadata and faster buffer cache initialization.
- Made multiple improvements to upgrades with Zero-Downtime Patching (ZDP) which reduces
  connection restore time and enhances ZDP resilience from failures.
- Fixed an issue where the server_id value wasn’t updated after an Amazon RDS Blue/Green
  Deployment switchover.
- Fixed an issue that could cause database restart during hash index extension.
- Fixed an issue that would cause migration from RDS PostgreSQL to fail in the presence
  of nested tablespaces.
- Fixed an issue that would cause excessive engine startup times in the presence of a
  large number of logical replication files.
- Fixed an issue related to zero-ETL where altering the constraint of a table in a new
  database session may cause the command to fail.
- Fixed an issue that could cause a database restart when calling functions from `aws_s3`,
  `aws_lambda`, and `aws_ml` extensions in the same database session as `aws_s3.table_import_from_s3()`.
  This fix may decrease the per-call performance of functions from the `aws_s3`, `aws_lambda`, and `aws_ml` extensions.
- Fixed an issue that could cause database restart during serverless scaling.
- Fixed an issue where AuroraForwardingReplicaReadWaitLatency and
  AuroraForwardingReplicaDMLLatency were reported incorrectly.
- Fixed an issue that prevented updating the `pgTAP` extension to version
  1.3.0 or later.
- Fixed an issue in the `PostGIS` extension, which in rare cases, could cause
  a DB instance restart.
- Added generic `plan` informations in
  `aurora_stat_statements`/`aurora_stat_plans`.
- Fixed an issue in the `pg_repack` extension that compromises the integrity
  of invalid indexes.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_cron` extension to v1.6.4.
  - `PostGIS` extension to version 3.4.3.
  - `PROJ` library extension to version 9.5.0.
  - `GEOS` library extension to verison 3.13.0.
  - `orafce` extension to 4.12.0.
  - `pgvector` extension to 0.7.4.
  - `RDKit` extension to 2024_03_6 release (4.6).
  - `pg_hint_plan` extension to version 1.6.1.

### PostgreSQL 16.4

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.4. For more information about
the improvements in PostgreSQL 16.4, see [PostgreSQL release
16.4](https://www.postgresql.org/docs/16/release-16-4.html "https://www.postgresql.org/docs/16/release-16-4.html").

###### Releases and patches

- [Aurora PostgreSQL 16.4.7, February 13, 2026](#aurorapostgresql-versions-version1647x-1647 "#aurorapostgresql-versions-version1647x-1647")
- [Aurora PostgreSQL 16.4.6, November 21, 2025](#aurorapostgresql-versions-version1646x-1646 "#aurorapostgresql-versions-version1646x-1646")
- [Aurora PostgreSQL 16.4.5, July 11, 2025](#aurorapostgresql-versions-version1645x-1645 "#aurorapostgresql-versions-version1645x-1645")
- [Aurora PostgreSQL 16.4.4, April 17, 2025](#aurorapostgresql-versions-version1644x-1644 "#aurorapostgresql-versions-version1644x-1644")
- [Aurora PostgreSQL 16.4.2, January 29, 2025](#aurorapostgresql-versions-version1642x-1642 "#aurorapostgresql-versions-version1642x-1642")
- [Aurora PostgreSQL 16.4.1, January 02, 2025](#aurorapostgresql-versions-version1641x-1641 "#aurorapostgresql-versions-version1641x-1641")
- [Aurora PostgreSQL 16.4, September 30,
  2024](#aurorapostgresql-versions-version164x-164 "#aurorapostgresql-versions-version164x-164")

#### Aurora PostgreSQL 16.4.7, February 13, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

#### Aurora PostgreSQL 16.4.6, November 21, 2025

**Critical stability enhancements**

- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 16.4.5, July 11, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 16.4.4, April 17, 2025

**High priority enhancements**.

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 16.4.2, January 29, 2025

**Critical stability enhancements**.

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**.

- Fixed an issue in Global DB switchover and failover that could result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.

**General enhancements**.

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 16.4.1, January 02, 2025

**Critical stability enhancements**

- Fixed an issue related to Query Plan Management background worker.
- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed issue where Aurora in-Region failovers would result in failures in database startup.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue that prevented the scaling of Aurora Serverless v2 Read Replicas when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in longer
  upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime further
  with faster buffer cache initialization.
- Fixed an issue where reserved keyword “PRIMARY” caused syntax errors when
  used as a column name or alias in DML and DDL statements.
- Fixed an issue that could cause an error in the wal sender process when resuming logical
  replication.
- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension 2 installation.

#### Aurora PostgreSQL 16.4, September 30,

2024

**New features**

- Introduced a new fast failover feature to reduce database downtime during the
  `planned` extension failover events with fast storage metadata initialization
  and fast buffer cache recovery.
- Introduced an optimization to reduce Zero Downtime Patching (ZDP) quiet point duration
  to 1 second.

**Critical stability enhancements**

- Fixed a rare bug causing missing commit timestamps for subtransactions.

**High priority enhancements**

- Fixed issues where the replication of vacuum operations may cause a restart when
  handling conflicts with user queries.
- Fixed an issue where deleting a large range of keys from a BTree index could cause
  concurrent scans to crash.

**General enhancements**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation.
  For more information, see [AWS-LC
  is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/") on AWS Security Blog.
- Improvements to database startup time during initialization and engine
  upgrades.
- Fixed an issue during ZDP which causes some connections to be terminated due to long
  transferring time. A new ZDP metric in `postgresql.log` called
  `ZD_SOCKET_TRANSFER_CONN_DROPPED` represents these dropped
  connections.
- Improved reader availability for Aurora Replicas when using system administration
  functions.
- Fixed an in-memory two-phase commit (2PC) metadata caching issue that caused
  out-of-memory error on Aurora read replicas replicating from RDS PostgreSQL source
  instances.
- Introduced a new function pgadmap_get_set_mapping_cmd() in the
  `pg_ad_mapping` extension to display commands required to recreate existing
  Active directory security group to Aurora PostgreSQL database role mappings.
- Fixed an issue in storage metadata initialization that can cause prolonged database
  startup time.
- Fixed an issue that will prevent reclaiming Aurora storage space during major version
  upgrade.
- Fixed an issue that prevents ZDP from completing successfully on Optimized
  Reads-enabled instances.

**Additional improvements and enhancements**

- Updated the following extensions:
  - `pgvector` extension to version 0.7.3.
  - `mysql_fdw` extension to version REL-2_9_2.
  - `orafce` extension to version 4.10.3.
  - `pgTAP` extension to version 1.3.3.
  - `pg_cron` extension to version 1.6.3.
  - `RDKit` extension to version 4.5 (Release 2024_03_5).
  - `wal2json` extension to version 2.6.
  - pg_ad_mapping extension to version 1.0.
  - `HypoPG` extension to version 1.4.1.

### PostgreSQL 16.3

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.3. For more information
about the improvements in PostgreSQL 16.3, see [PostgreSQL release
16.3](https://www.postgresql.org/docs/16/release-16-3.html "https://www.postgresql.org/docs/16/release-16-3.html").

###### Releases and patches

- [Aurora PostgreSQL 16.3.5, July 17, 2025](#aurorapostgresql-versions-version1635x-1635 "#aurorapostgresql-versions-version1635x-1635")
- [Aurora PostgreSQL 16.3.4, March
  25, 2025](#aurorapostgresql-versions-version1634x-1634 "#aurorapostgresql-versions-version1634x-1634")
- [Aurora PostgreSQL 16.3.3, January
  29, 2025](#aurorapostgresql-versions-version1633x-1633 "#aurorapostgresql-versions-version1633x-1633")
- [Aurora PostgreSQL 16.3.2, January
  23, 2025](#aurorapostgresql-versions-version1632x-1632 "#aurorapostgresql-versions-version1632x-1632")
- [Aurora PostgreSQL 16.3.1,
  September 27, 2024](#aurorapostgresql-versions-version163x-1631 "#aurorapostgresql-versions-version163x-1631")
- [Aurora PostgreSQL 16.3, August
  8, 2024](#aurorapostgresql-versions-version163x-163 "#aurorapostgresql-versions-version163x-163")

#### Aurora PostgreSQL 16.3.5, July 17, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue that can cause process stuck indefinitely at `LWLock:BufferIO` wait event.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 16.3.4, March

25, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 16.3.3, January

29, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 16.3.2, January

23, 2025

###### Critical stability enhancements

- Fixed an issue related to Query Plan Management background worker.

###### High priority enhancements

- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in
  longer upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime
  further with faster buffer cache initialization.
- Fixed an issue that could cause an error in the wal sender process when
  resuming logical replication.

#### Aurora PostgreSQL 16.3.1,

September 27, 2024

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

#### Aurora PostgreSQL 16.3, August

8, 2024

###### New features

- Aurora Serverless v2 now applies pending database parameter
  `max_connections` changes during upgrades. The Serverless V2
  capacity changes result in pending `max_connections` changes. As many
  ZDP supported connections as allowed by `max_connections` will be
  preserved during upgrades.
- Introduced a feature to improve database start up time through faster buffer
  cache initialization during restarts and database upgrades.
- Minor version and patch upgrades may now complete faster in some cases.
- Reduced Aurora Serverless v2 scale up and scale down time in the presence of
  data intensive workloads or long running queries and busy or unresponsive
  connections.
- Added per-query memory usage information to
  `aurora_stat_statements` and `aurora_stat_plans`. For
  more information, see [aurora_stat_statements](../AuroraUserGuide/aurora_stat_statements.md "../AuroraUserGuide/aurora_stat_statements.md").

###### Critical stability enhancements

- Fixed a pg_repack issue that would incorrectly allow two vacuum processes to
  operate concurrently on the same table.

###### High priority enhancements

- Fixed an issue which leads to cancellation of long-running queries on Global
  Database replica instances.

###### General enhancements

- Improved Aurora PostgreSQL performance for AI workloads using
  `pgvector`.
- Fixed cumulative statistics data reset after manual reboot.
- Improvements to the replay performance of the Aurora WAL replay process on
  read replica instances.
- Fixed issue where minor version upgrades with ZDP would fail in some cases
  resulting in longer upgrade times.
- Improved replay performance of vacuum operations on Aurora Replica
  instances.
- Fixed an issue which can cause logical replication to terminate when
  attempting to access relation metadata.
- Fixed a bug where JDBC connections may not be preserved during ZDP enabled
  upgrades.
- Improvement to reduce postgres private memory fragmentation.
- Fixed an issue that caused two-phase commit files to remain, preventing proper
  cleanup.
- Improved memory handling while processing two phase commit files.
- Fixed an issue resulting in degraded performance during query planning on
  Aurora replicas.
- Improved availability of Aurora read replicas.
- Fixed an issue where server might restart if background worker tries to spawn
  parallel workers.
- Fixed an issue where the instance may restart when logically applying changes
  from a remote server when under resource constraints.
- Fixed an issue with database-wide and statement-level blk_read_time metric.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` extension to version 4.9.4.
  - `pg_cron` extension to version 1.6.2.
  - `pg_partman` extension to version 5.1.0.
  - `pg_repack` extension to version 1.5.0.
  - `pg_tle` to version 1.4.0.
  - `pg_vector` extension to version 0.7.0.
  - `pgrouting` extension to version 3.6.2.
  - `pgTap` extension to version 1.3.2.
  - `PostGIS` extension to version 3.4.2.
  - `RDKit` extension to version 2024_03_1.

### PostgreSQL 16.2

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.2. For more information
about the improvements in PostgreSQL 16.2, see [PostgreSQL release
16.2](https://www.postgresql.org/docs/16/release-16-2.html "https://www.postgresql.org/docs/16/release-16-2.html").

###### Releases and patches

- [Aurora PostgreSQL 16.2.6, July 28, 2025](#aurorapostgresql-versions-version1626x-1626 "#aurorapostgresql-versions-version1626x-1626")
- [Aurora PostgreSQL 16.2.5, April 16, 2025](#aurorapostgresql-versions-version1625x-1625 "#aurorapostgresql-versions-version1625x-1625")
- [Aurora PostgreSQL 16.2.4, February 02, 2025](#aurorapostgresql-versions-version1624x-1624 "#aurorapostgresql-versions-version1624x-1624")
- [Aurora PostgreSQL 16.2.3,
  October 7, 2024](#aurorapostgresql-versions-version162x-1623 "#aurorapostgresql-versions-version162x-1623")
- [Aurora PostgreSQL 16.2.2, June 20,
  2024](#AuroraPostgreSQL.Updates.20180305.1622 "#AuroraPostgreSQL.Updates.20180305.1622")
- [Aurora PostgreSQL 16.2.1, April
  29, 2024](#AuroraPostgreSQL.Updates.20180305.1621 "#AuroraPostgreSQL.Updates.20180305.1621")

#### Aurora PostgreSQL 16.2.6, July 28, 2025

**Critical stability enhancements**.

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 16.2.5, April 16, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 16.2.4, February 02, 2025

**Critical stability enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418")
  for V8 Engine in the `PLV8` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")

- **General enhancements**

Fixed an ownership issue where the postgis_raster extension could not be updated correctly
from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 16.2.3,

October 7, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart
  when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 16.2.2, June 20,

2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.

###### High priority enhancements

- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed an issue with background worker where it may crash when executed in
  parallel worker context.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same
  table.
- Fixed issues in how two-phase commit files are handled.

#### Aurora PostgreSQL 16.2.1, April

29, 2024

###### New features

- Added resource usage summary to `pg_dump`.
- Added function overloading for `aurora_stat_statements(bool
showtext)` and `aurora_stat_plans(bool showtext)`.

###### General enhancements

- Fixed multiple minor version upgrade issues to improve connection preservation
  with zero-downtime patching.
- Reduced database boot time due to improved initialization time for large
  volumes.
- Introduced faster COPY operations by reducing contention on the relation
  extension lock and proactively extending relations.
- Improvements to reduce replication lag by intelligently skipping the replay of
  certain log records, thereby reducing the replay load.
- Fixed an issue during recovery conflict on a read node which, in rare cases,
  could cause brief unavailability.
- Fixed an issue where a database would fail to startup during a major version
  upgrade patch, in rare scenarios.
- Improved availability of read replicas by allowing recovery from replication
  errors in more situations.
- Fixed an issue resulting in a deadlock when a logical replication table
  synchronization operation fails.
- Fixed a logical replication decoding issue that fails to process catalog
  modifying changes after spilling to storage if there was a concurrent aborted
  sub-transaction.
- Improved log record validation before it is written to storage.
- Fixed an issue that would result in sessions incorrectly reporting ClientRead
  wait events after a zero-downtime patching event.
- Fixed an ambiguous function definition of aws_s3.query_export_to_s3 when
  upgrading the aws_s3 extension from version 1.1 to 1.2.

###### High priority enhancements

- Fixed an issue related to resuming a logical replication slot where, in rare
  cases, it could cause the slot to become stuck.
- Fixed an issue that would result in a restart when creating a database in a
  tablespace.
- Fixed an issue related to incorrect logical replication error handling to
  improve DB stability.

###### Critical stability enhancements

- Fixed an issue related to replication origins that in rare cases might result
  in longer recovery time and impact availability.
- Fixed an issue that in rare cases may cause transactions to be partially
  replicated by newly created logical replication slots. For more information, see
  [Potential data loss due to race condition during logical replication slot
  creation](https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com "https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com").
- Fixed an issue where `pg_stat_statements` can cause zero-downtime
  patching to fail.
- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_tle` extension to version 1.3.4.
  - `PLV8` extension to version 3.1.10.
  - RDKit Cartridge to version Release_2023_09_4.

- New GUC Parameters has been added
  - `pgtle.clientauth_databases_to_skip`
  - `pgtle.clientauth_db_name`
  - `pgtle.clientauth_num_parallel_workers`
  - `pgtle.clientauth_users_to_skip`
  - `pgtle.enable_clientauth`
  - `pgtle.passcheck_db_name`

### PostgreSQL 16.1

This release of Aurora PostgreSQL is compatible with PostgreSQL 16.1. For more information
about the improvements in PostgreSQL 16.1, see [PostgreSQL release
16.1](https://www.postgresql.org/docs/16/release-16-1.html "https://www.postgresql.org/docs/16/release-16-1.html").

###### Releases and patches

- [Aurora PostgreSQL 16.1.8, July 30, 2025](#aurorapostgresql-versions-version1618x-1618 "#aurorapostgresql-versions-version1618x-1618")
- [Aurora PostgreSQL 16.1.7, April 22, 2025](#aurorapostgresql-versions-version1617x-1617 "#aurorapostgresql-versions-version1617x-1617")
- [Aurora PostgreSQL 16.1.6, February 5, 2025](#aurorapostgresql-versions-version1616x-1616 "#aurorapostgresql-versions-version1616x-1616")
- [Aurora PostgreSQL 16.1.5,
  September 17, 2024](#aurorapostgresql-versions-version161x-1615 "#aurorapostgresql-versions-version161x-1615")
- [Aurora PostgreSQL 16.1.4, June 24,
  2024](#AuroraPostgreSQL.Updates.20180305.1614 "#AuroraPostgreSQL.Updates.20180305.1614")
- [Aurora PostgreSQL 16.1.3, March
  13, 2024](#AuroraPostgreSQL.Updates.20180305.1613 "#AuroraPostgreSQL.Updates.20180305.1613")
- [Aurora PostgreSQL 16.1.2, February
  22, 2024](#AuroraPostgreSQL.Updates.20180305.1612 "#AuroraPostgreSQL.Updates.20180305.1612")
- [Aurora PostgreSQL 16.1, January 31,
  2024](#AuroraPostgreSQL.Updates.20180305.161 "#AuroraPostgreSQL.Updates.20180305.161")

#### Aurora PostgreSQL 16.1.8, July 30, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vaccum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 16.1.7, April 22, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 16.1.6, February 5, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements.**

- Fixed an ownership issue where the `postgis_raster` extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 16.1.5,

September 17, 2024

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart
  when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 16.1.4, June 24,

2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue with Parallel query execution in which a backend may get into
  indefinite hang in certain cases.
- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same
  table.

#### Aurora PostgreSQL 16.1.3, March

13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

#### Aurora PostgreSQL 16.1.2, February

22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version
  upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes
  due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer
  failover.
- Fixed an issue where active transactions during logical replication slot
  creation may be partially replicated by the slot.

#### Aurora PostgreSQL 16.1, January 31,

2024

###### New features

- Added support for the `HypoPG` extension at version 1.4.0.
- Added support for the `h3-pg` extension and the
  `h3-postgis` extension at version 4.1.3.
- Added support for `aurora_compute_plan_id` parameter which is
  turned on by default in an Aurora PostgreSQL DB Cluster and DB Parameter Group. For
  more information, see [Monitoring query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md "../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md").
- The `rds.rds_superuser_reserved_connections` parameter has been
  deprecated in Aurora PostgreSQL version 16. The `reserved_connections`
  parameter should be utilized to reserve the number of connection slots. The
  `reserved_connections` parameter sets the number of connection
  slots reserved for roles with the `pg_use_reserved_connections`
  privileges. `rds_superuser` is a member of the
  `pg_use_reserved_connections` role by default. For more
  information, see the PostgreSQL documentation [reserved connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-RESERVED-CONNECTIONS "https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-RESERVED-CONNECTIONS").

###### General enhancements

- Deprecated support for ssl protocols: TLSv1.0 and TLSv1.1.

###### Additional improvements and enhancements

Updated the following extensions:

- `postgis` to version 3.4.0
- `PgLogical` to version 2.4.4
- `PgCron` to version 1.6
- `orafce` to version 4.6.0
- `pg_hint_plan` to version 1.6.0
- `plv8` to version 3.1.8
- `oracle_fdw` to version 2.6.0
- `MySQL_FDW` to version 2.9.1
- `Hll` to version 2.18
- `RDKit` to version 4.4
- `aws_s3` to version 1.2
- `prefix` to version 1.2.10
- `pg_similarity` to version 1.0
- `pgdam` to version 1.7
- `pg_proctab` to version 0.0.10
- `pg_tle` to version 1.2.0
- `pg_vector` to version 0.5.1
- `PgAudit` to version 16.0
- `plprofiler` to version 4.2.4
- `pg_partman` to version 4.7.3
- `pgTAP` to version 1.3.0

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
16](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.16 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.16").

## PostgreSQL 15 versions (includes some deprecated versions)

###### Version updates

- [PostgreSQL 15.15](#aurorapostgresql-versions-version1515x "#aurorapostgresql-versions-version1515x")
- [PostgreSQL 15.14](#aurorapostgresql-versions-version1514x "#aurorapostgresql-versions-version1514x")
- [PostgreSQL 15.13](#aurorapostgresql-versions-version1513x "#aurorapostgresql-versions-version1513x")
- [PostgreSQL 15.12](#aurorapostgresql-versions-version1512x "#aurorapostgresql-versions-version1512x")
- [PostgreSQL 15.10](#aurorapostgresql-versions-version1510x "#aurorapostgresql-versions-version1510x")
- [PostgreSQL 15.8](#aurorapostgresql-versions-version158x "#aurorapostgresql-versions-version158x")
- [PostgreSQL 15.7](#aurorapostgresql-versions-version157x "#aurorapostgresql-versions-version157x")
- [PostgreSQL 15.6](#AuroraPostgreSQL.Updates.20180305.156X "#AuroraPostgreSQL.Updates.20180305.156X")
- [PostgreSQL 15.5](#AuroraPostgreSQL.Updates.20180305.155X "#AuroraPostgreSQL.Updates.20180305.155X")
- [PostgreSQL 15.4](#AuroraPostgreSQL.Updates.20180305.154X "#AuroraPostgreSQL.Updates.20180305.154X")
- [PostgreSQL 15.3](#AuroraPostgreSQL.Updates.20180305.153X "#AuroraPostgreSQL.Updates.20180305.153X")
- [PostgreSQL 15.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.152X "#AuroraPostgreSQL.Updates.20180305.152X")

### PostgreSQL 15.15

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.15. For more information about
the improvements in PostgreSQL 15.15, see [PostgreSQL release
15.15](https://www.postgresql.org/docs/15/release-15-15.html "https://www.postgresql.org/docs/15/release-15-15.html").

###### Releases and patches

- [Aurora PostgreSQL 15.15.1, January 16th, 2026](#aurorapostgresql-versions-version15151x-15151 "#aurorapostgresql-versions-version15151x-15151")
- [Aurora PostgreSQL 15.15, Decemeber, 18, 2025](#aurorapostgresql-versions-version1515x-1515 "#aurorapostgresql-versions-version1515x-1515")

#### Aurora PostgreSQL 15.15.1, January 16th, 2026

**Critical stability enhancements**

- Fixed a timing condition in the aws_s3 extension which, in rare cases, can cause database unavailability
- Fixed an issue where an UPDATE statement with OUTPUT clause may skip rows when there are concurrent updates on the same row

#### Aurora PostgreSQL 15.15, Decemeber, 18, 2025

**New features**

- Introduced a change which improves static availability of Aurora PostgreSQL writers when, in rare conditions, write operations to storage are delayed due to undergoing storage node maintenance.
- Improvements to minimize switchover downtime during Blue/Green switchover operations, by temporarily blocking transaction commit operations on the Blue environment prior to switchover, reducing drift between the Blue and Green clusters.
- Improved recovery time by optimizing commit log (clog) loading during database cold starts and unplanned restarts, with significant benefits for smaller instances with limited CPU cores.

**Critical stability enhancements**

- Improved cold start performance through faster cache initialization.
- Reduced memory footprint for idle connections in Serverless v2 instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")

- Fixed a database shutdown issue that could cause major version upgrades to fail.
- Fixed a rare major version upgrade failure with large memory allocations.
- Fixed an issue preventing rds_superuser from managing prepared transactions owned by other users.

**General enhancements**

- Updated the following extensions:
  - h3_pg to version 4.2.3.

- Fixed a race condition in Postgres lock release with optimized read enabled.
- Improved PgAudit memory usage during parameter-heavy operations.
- Fixed database initialization failure when max_connections is set to low values.
- Improved Serverless v2 scaling performance under high CPU load.
- Improved Serverless v2 write performance.
- Fixed delays in Serverless v2 scale-down operations.
- Fixed multiple low-risk memory leaks.
- Improved database shutdown during maintenance to enhance availability.
- Improved database startup performance through optimized storage initialization.
- Fixed storage metadata initialization issue that could delay engine startup.
- Fixed region determination failures in aws_s3, aws_ml, and aws_lambda extensions.
- Fixed crash scenario when using pg_buffercache extension during Serverless v2 scaling.

### PostgreSQL 15.14

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.14. For more information about
the improvements in PostgreSQL 15.14, see [PostgreSQL release
15.14](https://www.postgresql.org/docs/15/release-15-14.html "https://www.postgresql.org/docs/15/release-15-14.html").

###### Releases and patches

- [Aurora PostgreSQL 15.14.1, November 25, 2025](#aurorapostgresql-versions-version15141x-15141 "#aurorapostgresql-versions-version15141x-15141")
- [Aurora PostgreSQL 15.14, November 25, 2025](#aurorapostgresql-versions-version1514x-1514 "#aurorapostgresql-versions-version1514x-1514")

#### Aurora PostgreSQL 15.14.1, November 25, 2025

**Critical stability enhancements**

- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")

- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 15.14, November 25, 2025

**New features**

- Introduced a new feature to significantly reduce database downtime during restarts by initializing Aurora storage metadata in parallel and reducing contention during initialization.

**Critical stability enhancements**

- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/")
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/")
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/")

- Fixed an issue in logical replication where subscriber databases could skip replicating transactions after recovering from a crash.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed a security issue when altering routine ownership.

**General enhancements**

- Updated the following extensions:
  - oracle_fdw to version to 2.8.0
  - pg_repack extension to version 1.5.2
  - aws_lamba extension to version 2.0

- Improved file metadata initialization times.
- Fixed an issue that caused reader instance to restart when attempting to create PostgreSQL SLRU files.
- Fixed an issue which caused prolonged Serverless v2 scaling time.
- Fixed an issue that could cause database restart during Serverless v2 scaling.
- Fixed a timing issue in replication diagnostics that could prevent accurate reporting of Aurora replica recovery status when state transitions occur in rapid succession.
- Updated the aws_lambda extension to version 2.0, which resolves a performance issue that was present in version 1.0.
- Added support to include Geodetic TIFF grid files for PROJ.
- Fixed an issue that could cause database restart during aws_s3 export.
- Addressed an issue with logging when replication slots are invalidated.
- Fixed CVE-2023-3079 for V8 Engine in the PLV8 extension.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue where read queries may time out on Aurora replica nodes during the replay of lazy truncation triggered by vacuum on the writer node.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue which prevented online recovery of an Aurora Replica forcing offline recovery.

### PostgreSQL 15.13

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.13. For more information
about the improvements in PostgreSQL 15.13, see [PostgreSQL release
15.13](https://www.postgresql.org/docs/15/release-15-13.html "https://www.postgresql.org/docs/15/release-15-13.html").

###### Releases and patches

- [Aurora PostgreSQL 15.13.4, January 15,
  2026](#aurorapostgresql-versions-version15134x-15134 "#aurorapostgresql-versions-version15134x-15134")
- [Aurora PostgreSQL 15.13.3, September 16,
  2025](#aurorapostgresql-versions-version15133x-15133 "#aurorapostgresql-versions-version15133x-15133")
- [Aurora PostgreSQL 15.13.2, August 8,
  2025](#aurorapostgresql-versions-version15132x-15132 "#aurorapostgresql-versions-version15132x-15132")
- [Aurora PostgreSQL 15.13.1, June 30,
  2025](#aurorapostgresql-versions-version15131x-15131 "#aurorapostgresql-versions-version15131x-15131")
- [Aurora PostgreSQL 15.13, June 30,
  2025](#aurorapostgresql-versions-version1513x-1513 "#aurorapostgresql-versions-version1513x-1513")

#### Aurora PostgreSQL 15.13.4, January 15,

2026

**Critical stability enhancements**

- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 15.13.3, September 16,

2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few
  seconds longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that
  might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when fetching
  pages from storage.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security
  vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed an issue that can cause reboots of the primary db instance when reading from a
  logical replication slot in the presence of frequent DDL if
  aurora.enhanced_logical_replication is enabled.
- Fixed a race where old writer may not step down after a new writer is promoted and
  continues to write.

**General enhancements**

- Implemented enhanced error handling mechanisms during TDS Connection reset
  operations.
- Fixed an issue that could in certain cases prevent online recovery of an Aurora Replica
  from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on
  tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately
  after installing the extension or resetting shared memory.
- Fixed an issue with Babelfish ZDP that could lead to instance reboot after
  minor version ugprade in some cases.
- Fixed an issue in enforcing, validating and evolving the `plans` extension
  in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with
  all-column selections.
- Fixed an issue with prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release
  containing The `PostGIS` extension 3.5.1 without running
  postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart
  of an Aurora replica in a Global Database.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 15.13.2, August 8,

2025

**Critical stability enhancements**

- Fixed an issue which could prevent logical replication from resuming after
  upgrade.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when
  performing reads from Aurora Storage.

#### Aurora PostgreSQL 15.13.1, June 30,

2025

**High priority enhancements**

- Fixed a performance issue affecting instance restart operations.

#### Aurora PostgreSQL 15.13, June 30,

2025

**New features**

- Improved Serverless v2 scaling for storage bound workloads.
- Improved Serverless v2 scaling through optimized management of memory maps.
- Aurora has doubled its maximum storage capacity from 128 TiB to 256 TiB. This
  increased storage limit allows customers to manage larger workloads in a single DB
  cluster. To access the increased storage limit for Aurora PostgreSQL, upgrade your DB cluster
  to version 17.5, 16.9, 15.13, or higher. Once upgraded, Aurora storage will automatically
  scale up to 256 TiB capacity based on the amount of data in the cluster volume.

**Critical stability enhancements**

- Fixed an issue where Serverless instances would fail to perform Zero Downtime Patching
  after automatic resume.
- Added library dependency verification during minor and patch upgrades to ensure
  storage metadata recovery is safe before proceeding.

**High priority enhancements**

- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads.
- Fixed an issue where server will fail to start if a previous startup was prematurely
  terminated.

**General enhancements**

- Updated the following extensions:
  - apg_plan_mgmt to 2.9.
  - The `pgaudit` extension to 1.7.1.
  - The `rdkit` extension to 4.6.1 (2024_09_6).
  - The `pg_repack` extension to 1.5.1.
  - The `pglogical` extension to 2.4.5.

- Improvements to make Serverless v2 scaling more efficient on reader nodes.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  sub-transactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue that prevents Zero Downtime Patching from completing successfully on
  Serverless v2 auto-pause enabled instances.
- Fixed an issue in pgdam that causes the engine (with pgdam enabled) to crash when
  hitting maximum connections.
- Fixed an issue in the `pg_bigm` extension that can cause unavailability
  when the extension interacts with the GIN index.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
- Added validation to ensure only predefined GUCs with `aurora_stat_plans`
  the `prefix` extension are accepted on SET or SHOW commands.
- Added function aurora_stat_resource_usage() to report current CPU usage, allocated and
  used memory for all the backends.
- Fixed an issue which prevented Zero Downtime Patching when cache recovery is
  disabled.
- Fixed a synchronization issue where Zero Downtime Patching could fail due to premature
  engine ready state reporting.
- Fixed an issue in checkpoint replication to have storage metadata position be
  consistent in reader.
- Fixed an issue which causes RO node to restart while its reconnecting to RW
  node.
- Fixed an issue where RO client process can be stuck in LWLock:BufferIO wait event
  after being disconnected from the writer.
- Fixed an issue where RO node could crash when frequently falling behind RW
  node.
- Fixed an issue in the aws_s3 extension that could cause an import operation to restart
  and reinsert previously inserted rows.
- Improved performance of EXPLAIN operations for queries involving tables with many
  columns and complex relations.

### PostgreSQL 15.12

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.12. For more information
about the improvements in PostgreSQL 15.12, see [PostgreSQL release
15.12](https://www.postgresql.org/docs/15/release-15-12.html "https://www.postgresql.org/docs/15/release-15-12.html").

###### Releases and patches

- [Aurora PostgreSQL 15.12.4, October 9, 2025](#aurorapostgresql-versions-version15124x-15124 "#aurorapostgresql-versions-version15124x-15124")
- [Aurora PostgreSQL 15.12.3, June 03, 2025](#aurorapostgresql-versions-version15123x-15123 "#aurorapostgresql-versions-version15123x-15123")
- [Aurora PostgreSQL 15.12.2, May 01,
  2025](#aurorapostgresql-versions-version15122x-15122 "#aurorapostgresql-versions-version15122x-15122")
- [Aurora PostgreSQL 15.12, April 07,
  2025](#aurorapostgresql-versions-version1512x-1512 "#aurorapostgresql-versions-version1512x-1512")

#### Aurora PostgreSQL 15.12.4, October 9, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds
  longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might
  result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables
  larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after
  installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving the `plans` extension in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with all-column
  selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing
  The `PostGIS` extension 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an
  Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans` extension using the “bitmap
  heap scan” access method.
- Fixed an issue impacting query execution performance for execution the `plans` extension using the
  “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 15.12.3, June 03, 2025

**Critical stability enhancements**

- Fixed stuck scaling for serverless db instances with zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing actions
  with Aurora Storage.
- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.
- Fixed an issue in handling parameter lists from previous versions of Query Plan Management.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Fixed an issue that can cause RO instance crash under heavy workload.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.

#### Aurora PostgreSQL 15.12.2, May 01,

2025

**Critical priority enhancements**

- Fixed an issue which can cause the database to become unresponsive when performing
  actions with Aurora storage.

#### Aurora PostgreSQL 15.12, April 07,

2025

**New features**

- Aurora Optimized Reads now enables users to resize the allocated space for Optimized
  Reads-enabled temporary objects on Aurora I/O-Optimized clusters using a dynamic parameter
  “aurora_temp_space_size”. For more information. see [Aurora Optimized Reads](../AuroraUserGuide/AuroraPostgreSQL.optimized.md "../AuroraUserGuide/AuroraPostgreSQL.optimized.md").

**Critical stability enhancements**

- Improved private memory allocation instrumentation to reduce CPU overhead for
  compute-heavy workloads that frequently invoke aset and slab allocation calls with
  `palloc`.
- When the system is under critical memory pressure for an extended duration, the
  largest customer backend will be cancelled to prevent system from restarting due to out of
  memory.

**High priority enhancements**

- Fixed an issue where Aurora in-Region failovers would result in failures in database
  startup.
- Fixed a security issue in the `rds_activity_stream` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Aurora storage metadata now initializes more quickly during unplanned failovers and
  server restarts, reducing overall downtime. Larger instances benefit the most by
  leveraging higher parallelism.
- Improved performance of file metadata operations.
- Made improvements to database downtime during a `planned` extension
  switchover for Global Databases.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
  - Creating temporary objects with syntax such as CREATE TEMPORARY TABLE x AS SELECT \* FROM isn't supported.
  - Creating indexes on temporary tables isn't supported.

- The Blue/Green deployment switchover won’t be blocked by the `REFRESH
MATERIALIZED VIEW` statement.
- Improved allocation of Write-Ahead Log (WAL) stream numbers, resulting in increased
  throughput for write-heavy workloads on the new Graviton 4 high-end instances.
- Fixed an issue where the query identifier (queryid) wasn't being correctly updated in
  pg_stat_activity when using extended protocol in pipeline mode.
- Fixed an issue where reader upgrade was taking longer than expected.
- Updated the following extensions:
  - Update the `pgvector` extension to 0.8.0.
  - Update the `pg_cron` extension to v1.6.5.
  - Update the `tds_fdw` extension to 2.0.4.
  - Update the `postgis` extension to 3.5.1.
  - Update the `pg_partman` extension to v5.2.4.
  - Update the `orafce` extension to 4.14.0.
  - Update the `rds_tools` extension to 1.9.
  - Update the `rdkit` extension to Release_2024_09_3.

### PostgreSQL 15.10

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.10. For more information
about the improvements in PostgreSQL 15.10, see [PostgreSQL release
15.10](https://www.postgresql.org/docs/15/release-15-10.html "https://www.postgresql.org/docs/15/release-15-10.html").

###### Releases and patches

- [Aurora PostgreSQL 15.10.7, January 28, 2026](#aurorapostgresql-versions-version15107x-15107 "#aurorapostgresql-versions-version15107x-15107")
- [Aurora PostgreSQL 15.10.6, November 13, 2025](#aurorapostgresql-versions-version15106x-15106 "#aurorapostgresql-versions-version15106x-15106")
- [Aurora PostgreSQL 15.10.5, June 24, 2025](#aurorapostgresql-versions-version15105x-15105 "#aurorapostgresql-versions-version15105x-15105")
- [Aurora PostgreSQL 15.10.4, March 24,
  2025](#aurorapostgresql-versions-version15104x-15104 "#aurorapostgresql-versions-version15104x-15104")
- [Aurora PostgreSQL 15.10.3, February
  13, 2025](#aurorapostgresql-versions-version15103x-15103 "#aurorapostgresql-versions-version15103x-15103")
- [Aurora PostgreSQL 15.10.2, January 20th,
  2025](#aurorapostgresql-versions-version15102x-15102 "#aurorapostgresql-versions-version15102x-15102")
- [Aurora PostgreSQL 15.10.1, December
  27, 2024](#aurorapostgresql-versions-version15101x-15101 "#aurorapostgresql-versions-version15101x-15101")
- [Aurora PostgreSQL 15.10, December 27,
  2024](#aurorapostgresql-versions-version1510x-1510 "#aurorapostgresql-versions-version1510x-1510")

#### Aurora PostgreSQL 15.10.7, January 28, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 15.10.6, November 13, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 15.10.5, June 24, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.10.4, March 24,

2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 15.10.3, February

13, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8` extension.

#### Aurora PostgreSQL 15.10.2, January 20th,

2025

**Critical Priority enhancements**

- Fixed a security issue in the rds_activity_stream extension.

**High priority enhancements**

- Fixed an issue in Global DB switchover and failover that could result in customers
  needing to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some
  cases.

**General enhancements**

- Fixed an ownership issue where the `postgis_raster` extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 15.10.1, December

27, 2024

**Critical Priority enhancements**

- Fixed an issue where the server was restarting when the connections were reset by the
  peer.

#### Aurora PostgreSQL 15.10, December 27,

2024

###### New features

- Optimized the minor version and patch upgrade process to reduce downtime for read
  replicas.

###### Critical stability enhancements

- Fixed an issue that in rare cases can cause CPU usage spike.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")

- Fixed an issue related to logical replication when processing large aborted
  transactions in the presence of catalog modifying operations. This can result in a
  transient failure of the logical replication process.

###### General enhancements

- Made multiple improvements to Aurora in-Region failover which reduces database downtime
  further by improving storage metadata and faster buffer cache initialization.
- Made multiple improvements to upgrades with Zero-Downtime Patching (ZDP) which reduces
  connection restore time and enhances ZDP resilience from failures.
- Fixed an issue where the server_id value wasn’t updated after an Amazon RDS Blue/Green
  Deployment switchover.
- Fixed an issue that could cause database restart during hash index extension.
- Fixed an issue that would cause migration from RDS PostgreSQL to fail in the presence
  of nested tablespaces.
- Fixed an issue that would cause excessive engine startup times in the presence of a
  large number of logical replication files.
- Fixed an issue that could cause a database restart when calling functions from `aws_s3`,
  `aws_lambda`, and `aws_ml` extensions in the same database session as `aws_s3.table_import_from_s3()`.
  This fix may decrease the per-call performance of functions from the `aws_s3`, `aws_lambda`, and `aws_ml` extensions.
- Fixed an issue that could cause database restart during serverless scaling.
- Fixed an issue where AuroraForwardingReplicaReadWaitLatency and
  AuroraForwardingReplicaDMLLatency were reported incorrectly.
- Fixed an issue that prevented updating the `pgTAP` extension to version
  1.3.0 or later.
- Fixed an issue in the `PostGIS` extension, which in rare cases, could cause
  a DB instance restart.
- Added generic `plan` informations in
  `aurora_stat_statements`/`aurora_stat_plans`.
- Fixed an issue in the `pg_repack` extension that compromises the integrity
  of invalid indexes.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_cron` extension to v1.6.4.
  - `PostGIS` extension to version 3.4.3.
  - `PROJ` library extension to version 9.5.0.
  - `GEOS` library extension to verison 3.13.0.
  - `orafce` extension to 4.12.0.
  - `pgvector` extension to 0.7.4.
  - `RDKit` extension to 2024_03_6 release (4.6).
  - `pg_hint_plan` extension to version 1.5.2.

### PostgreSQL 15.8

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.8. For more
information about the improvements in PostgreSQL 15.8, see [PostgreSQL release 15.8](https://www.postgresql.org/docs/15/release-15-8.html "https://www.postgresql.org/docs/15/release-15-8.html").

###### Releases and patches

- [Aurora PostgreSQL 15.8.7, February 13, 2026](#aurorapostgresql-versions-version1587x-1587 "#aurorapostgresql-versions-version1587x-1587")
- [Aurora PostgreSQL 15.8.6, November 21, 2025](#aurorapostgresql-versions-version1586x-1586 "#aurorapostgresql-versions-version1586x-1586")
- [Aurora PostgreSQL 15.8.5, July 11, 2025](#aurorapostgresql-versions-version1585x-1585 "#aurorapostgresql-versions-version1585x-1585")
- [Aurora PostgreSQL 15.8.4, April 17, 2025](#aurorapostgresql-versions-version1584x-1584 "#aurorapostgresql-versions-version1584x-1584")
- [Aurora PostgreSQL 15.8.2, January 29, 2025](#aurorapostgresql-versions-version1582x-1582 "#aurorapostgresql-versions-version1582x-1582")
- [Aurora PostgreSQL 15.8.1, January 02, 2025](#aurorapostgresql-versions-version1581x-1581 "#aurorapostgresql-versions-version1581x-1581")
- [Aurora PostgreSQL 15.8, September 30, 2024](#aurorapostgresql-versions-version158x-158 "#aurorapostgresql-versions-version158x-158")

#### Aurora PostgreSQL 15.8.7, February 13, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

#### Aurora PostgreSQL 15.8.6, November 21, 2025

**Critical stability enhancements**

- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 15.8.5, July 11, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.8.4, April 17, 2025

**High priority enhancements**.

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 15.8.2, January 29, 2025

**Critical stability enhancements**.

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**.

- Fixed an issue in Global DB switchover and failover that could result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.

**General enhancements**.

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 15.8.1, January 02, 2025

**Critical stability enhancements**

- Fixed an issue related to Query Plan Management background worker.
- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed issue where Aurora in-Region failovers would result in failures in database startup.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue that prevented the scaling of Aurora Serverless v2 Read Replicas when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in longer
  upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime further
  with faster buffer cache initialization.
- Fixed an issue where reserved keyword “PRIMARY” caused syntax errors when
  used as a column name or alias in DML and DDL statements.
- Fixed an issue that could cause an error in the wal sender process when resuming logical
  replication.
- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension 2 installation.

#### Aurora PostgreSQL 15.8, September 30, 2024

**New features for 15.8**

- Introduced a new fast failover feature to reduce database downtime during the `planned` extension failover
  events with fast storage metadata initialization and fast buffer cache recovery.
- Introduced an optimization to reduce Zero Downtime Patching (ZDP) quiet point duration to 1 second.

**Critical stability enhancements for 15.8**

- Fixed a rare bug causing missing commit timestamps for subtransactions.

**High priority enhancements for 15.8**

- Fixed issues where the replication of vacuum operations may cause a restart when handling
  conflicts with user queries.
- Fixed an issue where deleting a large range of keys from a BTree index could cause
  concurrent scans to crash.

**General enhancements for 15.8**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation. For more
  information, see [AWS-LC is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/")
  on AWS Security Blog.
- Improvements to database startup time during initialization and engine
  upgrades.
- Fixed an issue that prevented the inclusion of the `pg_bigm` extension in
  shared_preload_libraries.
- Fixed an issue during ZDP which causes some connections to be terminated
  due to long transfer time. A new ZDP metric in postgresql.log called
  `ZD_SOCKET_TRANSFER_CONN_DROPPED` represents these dropped connections.
- Improved reader availability for Aurora Replicas when using system administration functions.
- Fixed an in-memory two-phase commit (2PC) metadata caching issue that caused out-of-memory
  errors on Aurora read replicas replicating from RDS PostgreSQL source instances.
- Introduced a new function pgadmap_get_set_mapping_cmd() in the `pg_ad_mapping` extension to
  display commands required to recreate existing Active directory security group to Aurora
  PostgreSQL database role mappings.
- Fixed an issue in storage metadata initialization that can cause prolonged database startup
  time.
- Fixed an issue that will prevent reclaiming Aurora storage space during major version
  upgrade.
- Fixed an issue that prevents ZDP from completing successfully on
  Optimized Reads-enabled instances.

**Additional improvements and enhancements for 15.8**

- Updated the following extensions:
  - `pgvector` extension to version 0.7.3.
  - `mysql_fdw` extension to version REL-2_9_2.
  - `orafce` extension to version 4.10.3.
  - `pgTAP` extension to version 1.3.3.
  - `pg_cron` extension to version 1.6.3.
  - `RDKit` extension to version 4.5 (Release 2024_03_5).
  - `wal2json` extension to version 2.6.
  - pg_ad_mapping extension to version 1.0.
  - `HypoPG` extension to version 1.4.1.

### PostgreSQL 15.7

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.7. For more information
about the improvements in PostgreSQL 15.7, see [PostgreSQL release
15.7](https://www.postgresql.org/docs/15/release-15-7.html "https://www.postgresql.org/docs/15/release-15-7.html").

###### Releases and patches

- [Aurora PostgreSQL 15.7.5, July 17, 2025](#aurorapostgresql-versions-version1575x-1575 "#aurorapostgresql-versions-version1575x-1575")
- [Aurora PostgreSQL 15.7.4, March
  25, 2025](#aurorapostgresql-versions-version1574x-1574 "#aurorapostgresql-versions-version1574x-1574")
- [Aurora PostgreSQL 15.7.3, January
  29, 2025](#aurorapostgresql-versions-version1573x-1573 "#aurorapostgresql-versions-version1573x-1573")
- [Aurora PostgreSQL 15.7.2, January
  23, 2025](#aurorapostgresql-versions-version1572x-1572 "#aurorapostgresql-versions-version1572x-1572")
- [Aurora PostgreSQL 15.7.1,
  September 27, 2024](#aurorapostgresql-versions-version157x-1571 "#aurorapostgresql-versions-version157x-1571")
- [Aurora PostgreSQL 15.7, August
  8, 2024](#aurorapostgresql-versions-version157x-157 "#aurorapostgresql-versions-version157x-157")

#### Aurora PostgreSQL 15.7.5, July 17, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.7.4, March

25, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 15.7.3, January

29, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 15.7.2, January

23, 2025

###### Critical stability enhancements

- Fixed an issue related to Query Plan Management background worker.

###### High priority enhancements

- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in
  longer upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime
  further with faster buffer cache initialization.
- Fixed an issue that could cause an error in the wal sender process when
  resuming logical replication.

#### Aurora PostgreSQL 15.7.1,

September 27, 2024

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

#### Aurora PostgreSQL 15.7, August

8, 2024

###### New features

- Aurora Serverless v2 now applies pending database parameter
  `max_connections` changes during upgrades. The Serverless V2
  capacity changes result in pending `max_connections` changes. As many
  ZDP supported connections as allowed by `max_connections` will be
  preserved during upgrades.
- Introduced a feature to improve database start up time through faster buffer
  cache initialization during restarts and database upgrades.
- Minor version and patch upgrades may now complete faster in some cases.
- Reduced Aurora Serverless v2 scale up and scale down time in the presence of
  data intensive workloads or long running queries and busy or unresponsive
  connections.
- Added per-query memory usage information to
  `aurora_stat_statements` and `aurora_stat_plans`. For
  more information, see [aurora_stat_statements](../AuroraUserGuide/aurora_stat_statements.md "../AuroraUserGuide/aurora_stat_statements.md").

###### Critical stability enhancements

- Fixed a pg_repack issue that would incorrectly allow two vacuum processes to
  operate concurrently on the same table.

###### High priority enhancements

- Fixed an issue which leads to cancellation of long-running queries on Global
  Database replica instances.

###### General enhancements

- Improved Aurora PostgreSQL performance for generative AI workloads using
  `pgvector`.
- Fixed cumulative statistics data reset after manual reboot.
- Fixed issue where minor version upgrades with ZDP would fail in some cases
  resulting in longer upgrade times.
- Improved replay performance of vacuum operations on Aurora Replica
  instances.
- Fixed a bug where JDBC connections may not be preserved during ZDP enabled
  upgrades.
- Improvement to reduce postgres private memory fragmentation.
- Fixed an issue that caused two-phase commit files to remain, preventing proper
  cleanup.
- Improved memory handling while processing two phase commit files.
- Fixed an issue resulting in degraded performance during query planning on
  Aurora replicas.
- Improved availability of Aurora read replicas.
- Fixed cumulative statistics data reset after manual reboot.
- Fixed an issue where server might restart if background worker tries to spawn
  parallel workers.
- Fixed an issue where the instance may restart when logically applying changes
  from a remote server when under resource constraints.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` extension to version 4.9.4.
  - `pg_cron` extension to version 1.6.2.
  - `pg_partman` extension to version 5.1.0.
  - `pg_repack` extension to version 1.5.0.
  - `pg_tle` to version 1.4.0.
  - `pg_vector` extension to version 0.7.0.
  - `pgrouting` extension to version 3.6.2.
  - `pgTap` extension to version 1.3.2.
  - `PostGIS` extension to version 3.4.2.
  - `RDKit` extension to version 2024_03_1.

### PostgreSQL 15.6

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.6. For more
information about the improvements in PostgreSQL 15.6, see [PostgreSQL release 15.6](https://www.postgresql.org/docs/15/release-15-6.html "https://www.postgresql.org/docs/15/release-15-6.html").

###### Releases and patches

- [Aurora PostgreSQL 15.6.6, July 28, 2025](#aurorapostgresql-versions-version1566x-1566 "#aurorapostgresql-versions-version1566x-1566")
- [Aurora PostgreSQL 15.6.5, April 16, 2025](#aurorapostgresql-versions-version1565x-1565 "#aurorapostgresql-versions-version1565x-1565")
- [Aurora PostgreSQL 15.6.4, February 02, 2025](#aurorapostgresql-versions-version1564x-1564 "#aurorapostgresql-versions-version1564x-1564")
- [Aurora PostgreSQL 15.6.3, October 7, 2024](#aurorapostgresql-versions-version156x-1563 "#aurorapostgresql-versions-version156x-1563")
- [Aurora PostgreSQL 15.6.2, June 20, 2024](#AuroraPostgreSQL.Updates.20180305.1562 "#AuroraPostgreSQL.Updates.20180305.1562")
- [Aurora PostgreSQL 15.6.1, April 29, 2024](#AuroraPostgreSQL.Updates.20180305.1561 "#AuroraPostgreSQL.Updates.20180305.1561")

#### Aurora PostgreSQL 15.6.6, July 28, 2025

**Critical stability enhancements**.

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.6.5, April 16, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 15.6.4, February 02, 2025

**Critical stability enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418")
  for V8 Engine in the `PLV8` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")

- **General enhancements**

Fixed an ownership issue where the postgis_raster extension could not be updated correctly
from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 15.6.3, October 7, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache instances while upgrading into this version.

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 15.6.2, June 20, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed an issue with background worker where it may crash when executed in parallel worker context.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed issues in how two-phase commit files are handled.

####

Aurora PostgreSQL 15.6.1, April 29, 2024

###### New features

- Added resource usage summary to `pg_dump`.
- Added function overloading for `aurora_stat_statements(bool showtext)` and `aurora_stat_plans(bool showtext)`.

###### General enhancements

- Fixed multiple minor version upgrade issues to improve connection preservation with zero-downtime patching.
- Reduced database boot time due to improved initialization time for large volumes.
- Introduced faster COPY operations by reducing contention on the relation extension lock and proactively extending relations.
- Improvements to reduce replication lag by intelligently skipping the replay of certain log records, thereby reducing the replay load.
- Fixed an issue during recovery conflict on a read node which, in rare cases, could cause brief unavailability.
- Fixed an issue where a database would fail to startup during a major version upgrade patch, in rare scenarios.
- Improved availability of read replicas by allowing recovery from replication errors in more situations.
- Fixed an issue that would cause zero-downtime patching to timeout.
- Fixed an issue resulting in a deadlock when a logical replication table synchronization operation fails.
- Fixed a logical replication decoding issue that fails to process catalog modifying changes after spilling to storage
  if there was a concurrent aborted sub-transaction.
- Improved log record validation before it is written to storage.
- Fixed an issue that would result in sessions incorrectly reporting ClientRead wait events after a zero-downtime patching event.
- Fixed an ambiguous function definition of aws_s3.query_export_to_s3 when upgrading the aws_s3 extension from version 1.1 to 1.2.

###### High priority enhancements

- Fixed an issue related to resuming a logical replication slot where, in rare cases, it could cause the slot to become stuck.
- Fixed an issue that would result in a restart when creating a database in a tablespace.
- Fixed an issue related to incorrect logical replication error handling to improve DB stability.

###### Critical stability enhancements

- Fixed an issue related to replication origins that in rare cases might result in longer recovery time and impact availability.
- Fixed an issue that in rare cases may cause transactions to be partially replicated by newly created logical replication slots. For more information, see
  [Potential data loss due to race condition during logical replication slot creation](https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com "https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com").
- Fixed an issue where `pg_stat_statements` can cause zero-downtime patching to fail.
- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_tle` extension to version 1.3.4.
  - `PLV8` extension to version 3.1.10.
  - RDKit Cartridge to version Release_2023_09_4.

- New GUC Parameters has been added
  - `pgtle.clientauth_databases_to_skip`
  - `pgtle.clientauth_db_name`
  - `pgtle.clientauth_num_parallel_workers`
  - `pgtle.clientauth_users_to_skip`
  - `pgtle.enable_clientauth`
  - `pgtle.passcheck_db_name`

### PostgreSQL 15.5

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.5. For more
information about the improvements in PostgreSQL 15.5, see [PostgreSQL release 15.5](https://www.postgresql.org/docs/15/release-15-5.html "https://www.postgresql.org/docs/15/release-15-5.html").

###### Releases and patches

- [Aurora PostgreSQL 15.5.8, July 30, 2025](#aurorapostgresql-versions-version1558x-1558 "#aurorapostgresql-versions-version1558x-1558")
- [Aurora PostgreSQL 15.5.7, April 22, 2025](#aurorapostgresql-versions-version1557x-1557 "#aurorapostgresql-versions-version1557x-1557")
- [Aurora PostgreSQL 15.5.6, February 5, 2025](#aurorapostgresql-versions-version1556x-1556 "#aurorapostgresql-versions-version1556x-1556")
- [Aurora PostgreSQL 15.5.5, September 17, 2024](#aurorapostgresql-versions-version155x-1555 "#aurorapostgresql-versions-version155x-1555")
- [Aurora PostgreSQL 15.5.4, June 24, 2024](#AuroraPostgreSQL.Updates.20180305.1554 "#AuroraPostgreSQL.Updates.20180305.1554")
- [Aurora PostgreSQL 15.5.3, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1553 "#AuroraPostgreSQL.Updates.20180305.1553")
- [Aurora PostgreSQL 15.5.2, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.1552 "#AuroraPostgreSQL.Updates.20180305.1552")
- [Aurora PostgreSQL 15.5.0, December 21, 2023](#AuroraPostgreSQL.Updates.20180305.1550 "#AuroraPostgreSQL.Updates.20180305.1550")

#### Aurora PostgreSQL 15.5.8, July 30, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Auorora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vaccum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.5.7, April 22, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 15.5.6, February 5, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 15.5.5, September 17, 2024

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 15.5.4, June 24, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

####

Aurora PostgreSQL 15.5.3, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

####

Aurora PostgreSQL 15.5.2, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 15.5.0, December 21, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition to support
PostgreSQL versions 15.5, 14.10, 13.13, and 12.17. These releases contain product improvements and bug fixes made by the PostgreSQL community,
along with Aurora-specific improvements. New features and improvements for Babelfish for Aurora PostgreSQL version 3.4 are also included.

Refer to the Aurora version policy to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder,
if you are running any version of Amazon Aurora PostgreSQL version 11, you must upgrade to a newer major version by February 29, 2024.

###### New features

- Amazon Bedrock integration – By using the Amazon Aurora machine learning extension with your Aurora PostgreSQLDB cluster, you can now use Amazon Bedrock
  foundational AI models.
- Using Active Directory security groups for Aurora PostgreSQL access control – Add group role authentication support using AWS Directory Service for Microsoft Active Directory with the new `pg_ad_mapping` extension.
- Delegated Extension Support – This feature allows delegating extension management to lower privileged user with the new rds_extension role.
- Added support for `aurora_compute_plan_id` parameter which is turned on by default in an Aurora PostgreSQL DB Cluster and DB Parameter Group.
  For more information, see [Monitoring query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md "../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md").
- Query Plan Management (QPM) enhancements:
  - Plan outlines will be updated to the latest format version as part of the `update_plan_hash`
    action for `apg_plan_mgmt.validate_plans()`.
  - Support was added for parallel append enforcement as a part of parallel query enforcement.

- Added support for the `HypoPG` extension at version 1.4.0.
- Added support for the `h3-pg` extension and the `h3-postgis` extension at version 4.1.3.

###### High priority enhancements

- Fixed an issue which may cause a reboot when logically replicating changes in the presence of concurrently-running DDL or canceled sub-transactions
- Fixed an issue which may cause an Aurora replica to reboot when reading a page which was modified during `WAL` replay
- Fixed an issue where if a specific volume metadata is invalid on a source cluster, it will remain invalid on a cloned cluster. Since the
  clone cluster uses a new volume, the metadata will now be recreated.
- Fixed a bug that may cause an engine crash during zero-downtime patching (ZDP)
- Introduced a new parameter, `rds.enable_memory_management`, which is used to enable and disable the improved memory management feature.
- Improved index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General enhancements

- Fixed an issue which caused the `AuroraGlobalDBRPOLag` metric to be zero when the `rds.global_db_rpo` parameter was not set.
- Fixed an issue which may cause an Aurora replica to reboot while reconnecting with the writer DB instance.
- Added support for the `rdkit.morgan_fp_size` parameter
- `rds-superuser` can now run the `pg_stat_reset_slru` function
- Fixed an issue where MultiXact SLRU accesses were not credited to the correct `pg_stat_slru` category.
- Fixed an issue which may cause unused `WAL` segements to not be properly removed
- Fixed an issue where `pglogical` does not correctly pass-through replication origin data when using the binary output format
- `rds_superuser` can now execute `ALTER COLLATION` to refresh the collation version of a locale in the catalog.
- Fixed a crash in `dblink` and `postgres_fdw` extensions due to invalid connections
- Fixed an issue where the `aws_s3` extension can import `HTTP` error responses into the table
- Fixed an issue which may cause an Aurora Replica instance with Optimized Reads to reboot while reconnecting with the writer DB instance.
- Fixed an issue which may cause an Aurora replica with Optimized Reads to reboot while caching a page to tiered cache.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `mysql_fdw` to version 2.9.1
  - `Oracle_fdw` to version 2.6.0
  - `Orafce` to version 4.6.0
  - `pg_cron` to version 1.6.0
  - `pg_hint_plan` to version 1.5.1
  - `pg_proctab` to version 0.0.10
  - `pg_tle` to version 1.2.0
  - `plv8` to version 3.1.8
  - `PostGIS` to version 3.4.0
  - `prefix` to version 1.2.10
  - `RDKit` to version 4.4.0 (Release_2023_09_1)

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
15](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15").

### PostgreSQL 15.4

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.4. For more information
about the improvements in PostgreSQL 15.4, see [PostgreSQL release
15.4](https://www.postgresql.org/docs/15/release-15-4.html "https://www.postgresql.org/docs/15/release-15-4.html").

###### Releases and patches

- [Aurora PostgreSQL 15.4.11, August 5, 2025](#aurorapostgresql-versions-version15411x-15411 "#aurorapostgresql-versions-version15411x-15411")
- [Aurora PostgreSQL 15.4.10, May
  7, 2025](#aurorapostgresql-versions-version15410x-15410 "#aurorapostgresql-versions-version15410x-15410")
- [Aurora PostgreSQL 15.4.9, February 27, 2025](#aurorapostgresql-versions-version1549x-1549 "#aurorapostgresql-versions-version1549x-1549")
- [Aurora PostgreSQL 15.4.8,
  November 14, 2024](#aurorapostgresql-versions-version154x-1548 "#aurorapostgresql-versions-version154x-1548")
- [Aurora PostgreSQL 15.4.7, June 25,
  2024](#AuroraPostgreSQL.Updates.20180305.1547 "#AuroraPostgreSQL.Updates.20180305.1547")
- [Aurora PostgreSQL 15.4.6, March
  13, 2024](#AuroraPostgreSQL.Updates.20180305.1546 "#AuroraPostgreSQL.Updates.20180305.1546")
- [Aurora PostgreSQL 15.4.5, Febraury
  22, 2024](#AuroraPostgreSQL.Updates.20180305.1545 "#AuroraPostgreSQL.Updates.20180305.1545")
- [Aurora PostgreSQL 15.4.3, December
  15, 2023](#AuroraPostgreSQL.Updates.20180305.1543 "#AuroraPostgreSQL.Updates.20180305.1543")
- [Aurora PostgreSQL 15.4.2, December
  13, 2023](#AuroraPostgreSQL.Updates.20180305.1542 "#AuroraPostgreSQL.Updates.20180305.1542")
- [Aurora PostgreSQL 15.4.1, November
  09, 2023](#AuroraPostgreSQL.Updates.20180305.1541 "#AuroraPostgreSQL.Updates.20180305.1541")
- [Aurora PostgreSQL 15.4.0, October
  24, 2023](#AuroraPostgreSQL.Updates.20180305.1540 "#AuroraPostgreSQL.Updates.20180305.1540")

#### Aurora PostgreSQL 15.4.11, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.4.10, May

7, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 15.4.9, February 27, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream`
  extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue in Global DB switchover and failover that can result in
  customers needing to rebuild their mirror clusters.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 15.4.8,

November 14, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when
  `rds.enable_plan_management` is turned on, but apg_plan_mgmt
  extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 15.4.7, June 25,

2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue which led to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same
  table.

#### Aurora PostgreSQL 15.4.6, March

13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

#### Aurora PostgreSQL 15.4.5, Febraury

22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version
  upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes
  due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer
  failover.
- Fixed an issue where active transactions during logical replication slot
  creation may be partially replicated by the slot.

#### Aurora PostgreSQL 15.4.3, December

15, 2023

###### High priority enhancements

- Fixed an issue which may cause a reboot when logically replicating changes in
  the presence of concurrently-running DDL or canceled sub-transactions

#### Aurora PostgreSQL 15.4.2, December

13, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page
  reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to
  database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone
  other than the table owner

#### Aurora PostgreSQL 15.4.1, November

09, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker
  processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale
  metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in
  a crash

#### Aurora PostgreSQL 15.4.0, October

24, 2023

###### New features

- Added support for `mysql_fdw` version 2.9.0
- Added support in the `aws_s3` extension for exporting to an S3
  bucket encrypted with a customer managed KMS key
- Improved the availability of Aurora replicas in the global DB secondary
  clusters
- Added support for query plan capture on Aurora replicas
- Added support for query plan enforcement with materialize nodes
- Added support for query plan enforcement with parallel query operators
- Query plans under a given cost threshold will not be captured

###### High priority enhancements

- Fixed an issue which could cause the database to fail to start up during
  database recovery
- Included optimizations to improve the time to scale up in Aurora Serverless v2
  instances

###### General enhancements

- Fixed an issue in the `aws_s3` extension where the number of rows
  exported is incorrectly reported when the total number exceeds 2 billion
- Provided options to configure timeouts in the `aws_s3` extension.
  By setting the following parameters (GUCs), customers will now be able to change
  the timeout thresholds for imports from S3:
  - `aws_s3.curlopt_low_speed_limit`
  - `aws_s3.curlopt_low_speed_time`

- Prevented instance creation failure in some edge cases
- Improved the performance of replay of commit transaction operations on Aurora
  replicas
- Fixed an issue where, in rare cases, an import from the `aws_s3`
  extension fails to complete
- Updated the GEOS library for PostGIS to version 3.12.0
- Improved Aurora Serverless v2 database memory scaling which reduces the overall
  database instance scale time
- Added the `WAIT_EVENT_Aurora_CLUSTER_CACHE_MANAGER_SENDER` wait
  event to denote wait times in the cluster cache manager sender
- Added the `WAIT_EVENT_Aurora_SERVERLESS_MONITORING_MAIN` wait event
  to denote wait times in Aurora Serverless resource monitoring
- Improved the handling of invalid non-persisted metadata during reads from
  storage on read replicas
- Fixed an issue where the database may crash during the start of a logical
  replication slot
- Increased the limit for `pg_cron`
  `cron.max_running_jobs` parameter from 100 to 1000
- The `pgAudit`
  `pgaudit.log_statement` parameter is now modifiable
- Fixed a bug in `CREATE TABLE` command to handle table name starting
  with '#' correctly.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` to version 4.3.0
  - `pg_logical` to version 2.4.3
  - `pg_tle` to version 1.1.1
  - `pgvector` to version 0.5.0
  - `plv8` to version 3.1.6
  - `PostGIS` to version 3.3.3
  - `RDKit` to version 4.3

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
15](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15").

### PostgreSQL 15.3

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.3. For more
information about the improvements in PostgreSQL 15.3, see [PostgreSQL release 15.3](https://www.postgresql.org/docs/15/release-15-3.html "https://www.postgresql.org/docs/15/release-15-3.html").

###### Releases and patches

- [Aurora PostgreSQL 15.3.10, August 5, 2025](#aurorapostgresql-versions-version15310x-15310 "#aurorapostgresql-versions-version15310x-15310")
- [Aurora PostgreSQL 15.3.9, April 30, 2025](#aurorapostgresql-versions-version1539x-1539 "#aurorapostgresql-versions-version1539x-1539")
- [Aurora PostgreSQL 15.3.8, February 24 2025](#aurorapostgresql-versions-version1538x-1538 "#aurorapostgresql-versions-version1538x-1538")
- [Aurora PostgreSQL 15.3.7, November 12, 2024](#aurorapostgresql-versions-version153x-1537 "#aurorapostgresql-versions-version153x-1537")
- [Aurora PostgreSQL 15.3.6, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1536 "#AuroraPostgreSQL.Updates.20180305.1536")
- [Aurora PostgreSQL 15.3.5, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1535 "#AuroraPostgreSQL.Updates.20180305.1535")
- [Aurora PostgreSQL 15.3.4, December 14, 2023](#AuroraPostgreSQL.Updates.20180305.1534 "#AuroraPostgreSQL.Updates.20180305.1534")
- [Aurora PostgreSQL 15.3.3, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.1533 "#AuroraPostgreSQL.Updates.20180305.1533")
- [Aurora PostgreSQL 15.3.2, October 4, 2023](#AuroraPostgreSQL.Updates.20180305.1532 "#AuroraPostgreSQL.Updates.20180305.1532")
- [Aurora PostgreSQL 15.3.0, July 13, 2023](#AuroraPostgreSQL.Updates.20180305.1530 "#AuroraPostgreSQL.Updates.20180305.1530")

#### Aurora PostgreSQL 15.3.10, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 15.3.9, April 30, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 15.3.8, February 24 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 15.3.7, November 12, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 15.3.6, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 15.3.5, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 15.3.4, December 14, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 15.3.3, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 15.3.2, October 4, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39418](https://nvd.nist.gov/vuln/detail/CVE-2023-39418 "https://nvd.nist.gov/vuln/detail/CVE-2023-39418")
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica
- Fixed an issue that would cause a crash when executing the `COPY FROM` command
- Fixed an issue that would cause high CPU usage and prevent new connections
- Fixed an issue where `UPDATE` and `DELETE` from a table with foreign key could fail unexpectedly
  with "ERROR: 40001: could not serialize access due to concurrent update when using Serializable snapshot"

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O
- Fixed an issue that prevented the enablement of improved memory management in certain scenarios in Aurora PostgreSQL 15.3

####

Aurora PostgreSQL 15.3.0, July 13, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition
to support PostgreSQL versions 15.3, 14.8, 13.11, 12.15, and 11.20. These releases contains product improvements and bug fixes made by
the PostgreSQL community, along with Aurora-specific improvements. The releases also contain new features and improvements for
[Babelfish for Aurora PostgreSQL version 3.2](AuroraBabelfish.md "AuroraBabelfish.md"), and improved support for
[AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish").
Refer to the [Amazon Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md")
to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder, if you are running any version of Amazon Aurora PostgreSQL 11,
you must upgrade to a newer major version by February 29, 2024.

###### New features

- This release contains memory management improvements which increase database stability and availability by proactively
  preventing issues caused by insufficient memory. For more information, see [Improved memory management in Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md "../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md").
- Added support for the `pgvector` extension version 0.4.1.

###### High priority enhancements

- Fixed an issue with the subtransaction metadata handling when performing a survivable reader reconnect
- Fixed an issue during ZDP which is related to the extension environment variables
- Addressed a transient error during logical replication that caused a process to incorrectly calculate that it had encountered an unexpected page
- Fixed an issue which causes a period of unavailability due to a partially created replication origin state file

###### General enhancements

- Addressed an issue where the computing query identifier displayed a warning, "WARNING: unrecognized node type: 378"
- Addressed an issue that caused the initial data sync of a relation to become blocked due to the premature removal of the logical replication slot on the publisher
- Added a new function, `aurora_stat_memctx_usage()`, to show backend memory use breakdown at a Postgres memory context level
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots
- Further reduced the database downtime during ZDP
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue which caused `pg_ls_waldir()` to return "ERROR: could not stat file"
- Added support for TLS 1.3 with ciphers TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384
- Addressed an issue that blocked a major version upgrade on the Aurora replica of an RDS for PostgreSQL DB instance
- Fixed an issue that could prevent scaling in Aurora Serverless v2 instances
- Fixed an issue in logical replication which, in rare cases, can cause a period of unavailability due to the incorrect subtransaction metadata
- Fixed an issue in the `pg_vector` extension where, in rare cases, infinite or NAN values caused a crash during the index creation
- Fixed an issue to improve the performance
- Upgraded `GEOS` to version 3.11.2
- Upgraded `pg_cron` to version 1.5
- Upgraded `pg_partman` to version 4.7.3
- Upgraded `pg_tle` to version 1.0.3
- Upgraded `plv8` to version 3.1.6

### PostgreSQL 15.2 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 15.2. For more
information about the improvements in PostgreSQL 15.2, see [PostgreSQL release 15.2](https://www.postgresql.org/docs/15/release-15-2.html "https://www.postgresql.org/docs/15/release-15-2.html").

###### Releases and patches

- [Aurora PostgreSQL 15.2.9, November 6, 2024](#aurorapostgresql-versions-version152x-1529 "#aurorapostgresql-versions-version152x-1529")
- [Aurora PostgreSQL 15.2.8, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1528 "#AuroraPostgreSQL.Updates.20180305.1528")
- [Aurora PostgreSQL 15.2.7, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1527 "#AuroraPostgreSQL.Updates.20180305.1527")
- [Aurora PostgreSQL 15.2.6, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.1526 "#AuroraPostgreSQL.Updates.20180305.1526")
- [Aurora PostgreSQL 15.2.5, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.1525 "#AuroraPostgreSQL.Updates.20180305.1525")
- [Aurora PostgreSQL 15.2.4, October 5, 2023](#AuroraPostgreSQL.Updates.20180305.1524 "#AuroraPostgreSQL.Updates.20180305.1524")
- [Aurora PostgreSQL 15.2.3, July 25, 2023](#AuroraPostgreSQL.Updates.20180305.1523 "#AuroraPostgreSQL.Updates.20180305.1523")
- [Aurora PostgreSQL 15.2.2, May 10, 2023](#AuroraPostgreSQL.Updates.20180305.1522 "#AuroraPostgreSQL.Updates.20180305.1522")
- [Aurora PostgreSQL 15.2.1, April 5, 2023](#AuroraPostgreSQL.Updates.20180305.1521 "#AuroraPostgreSQL.Updates.20180305.1521")

#### Aurora PostgreSQL 15.2.9, November 6, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 15.2.8, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 15.2.7, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 15.2.6, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 15.2.5, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 15.2.4, October 5, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-39418](https://nvd.nist.gov/vuln/detail/CVE-2023-39418 "https://nvd.nist.gov/vuln/detail/CVE-2023-39418")
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O

####

Aurora PostgreSQL 15.2.3, July 25, 2023

###### General enhancements

- Fixed an issue related to storage space reclamation following table drop or reindex or truncate operations.
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue that prevented reclaiming storage on transaction commits
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

- Fixed multiple issues which can cause Aurora replicas with the improved read availability feature to restart when reconnecting with the writer instance
- Fixed an issue preventing a survivable reader reconnect

####

Aurora PostgreSQL 15.2.2, May 10, 2023

###### General enhancements

- Fixed an error when loading the `test_decoding` plugin in `pg_create_logical_replication_slot`
- Fixed an issue that causes logical replication to fail when using write-through cache
- Updated the Oracle client used by the `oracle_fdw` extension to version 21.9.0.0.0

####

Aurora PostgreSQL 15.2.1, April 5, 2023

###### New features

- Introduced a new Query Plan Management (QPM) plan hash calculation for multi-schema support. If users want to use QPM in multi-schema
  environments, they can set the `apg_plan_mgmt.plan_hash` version to 2 and call `apg_plan_mgmt.validate_plans`
  ('`update_plan_hash`').
- Logical replication enhancements to improve memory and CPU usage during the processing of large transactions.
- The CloudWatch metric `ReplicationSlotDiskUsage` now tracks logical replication specific storage across Aurora storage and local storage.
- Starting with Aurora PostgreSQL versions 15.2 and 14.7, a user needs to be granted the `CONNECT` privilege on each database to connect
  even if the user is granted access to the `rds_superuser` role. Prior to Aurora PostgreSQL versions 15.2 and 14.7, a user was able to connect to
  any database and system table if the user was granted the `rds_superuser` role. Previous Aurora PostgreSQL versions are not impacted by
  this change, and users with access to the `rds_superuser` role do not require the `CONNECT` privilege to access databases in their
  Aurora PostgreSQL cluster.

###### General enhancements

- Upgraded `PROJ` support to version 9.1.0
- Upgraded the `GDAL` library in `PostGIS` to version 3.5.3
- Upgraded the `pg_hint_plan` to version 1.5.0
- Added support for the `TCN` and `SEG` extensions
- Improved performance of deletes from b-tree and hash indexes on Aurora replicas
- Includes Aurora Serverless v2 scaling enhancements
- Fixed issue in QPM that prevented the enforcement of approved plans when joining partitioned tables
- Improved engine startup time, particularly on large instances with many objects
- The Aurora function `aurora_stat_logical_wal_cache()` is now visible to all users
- Fixed an issue in QPM that could cause unavailability when enforcing plans from prepared statements

###### Additional improvements and enhancements

- Updated the following extensions:
  - `apg_plan_mgmt` to version 2.4
  - `hll` to version 2.17
  - `Oracle_fdw` to version 2.5.0
  - `orafce` to version 4.0.0
  - `pg_audit` to version 1.7.0
  - `pg_cron` to version 1.4.2
  - `pg_hint_plan` to version 1.5.0
  - `pg_logical` to version 2.4.2
  - `pg_repack` to version 1.4.8
  - `pg_stat_statements` to version 1.10
  - `pg_trgm` to version 1.4
  - `pgrouting` to version 3.4.1
  - `plv8` to version 3.1.4
  - `PostGIS` to version 3.3.2
  - `rds_activity_stream` to version 1.6
  - `SEG` to version 1.0
  - `TCN` to version 1.0
  - `tds_fdw` to version 2.0.3
  - `wal2json` to version 2.5

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
15](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.15").

###### Differences between PostgreSQL 15 and Aurora PostgreSQL 15

Due to Aurora's unique distributed storage system, Amazon Aurora PostgreSQL version 15 does not support server-side compression with Gzip, LZ4,
or Zstandard (zstd) using `pg_basebackup`, online backups using `pg_backup_start()` and `pg_backup_stop()`,
and prefetching during WAL recovery. In addition, sequences can be specified as unlogged, but this has no performance improvements over normal sequences.

## PostgreSQL 14 versions (includes some deprecated versions)

###### Version updates

- [PostgreSQL 14.20](#aurorapostgresql-versions-version1420x "#aurorapostgresql-versions-version1420x")
- [PostgreSQL 14.19](#aurorapostgresql-versions-version1419x "#aurorapostgresql-versions-version1419x")
- [PostgreSQL 14.18](#aurorapostgresql-versions-version1418x "#aurorapostgresql-versions-version1418x")
- [PostgreSQL 14.17](#aurorapostgresql-versions-version1417x "#aurorapostgresql-versions-version1417x")
- [PostgreSQL 14.15](#aurorapostgresql-versions-version1415x "#aurorapostgresql-versions-version1415x")
- [PostgreSQL 14.13](#aurorapostgresql-versions-version1413x "#aurorapostgresql-versions-version1413x")
- [PostgreSQL 14.12](#aurorapostgresql-versions-version1412x "#aurorapostgresql-versions-version1412x")
- [PostgreSQL 14.11](#AuroraPostgreSQL.Updates.20180305.1411X "#AuroraPostgreSQL.Updates.20180305.1411X")
- [PostgreSQL 14.10](#AuroraPostgreSQL.Updates.20180305.1410X "#AuroraPostgreSQL.Updates.20180305.1410X")
- [PostgreSQL 14.9](#AuroraPostgreSQL.Updates.20180305.149X "#AuroraPostgreSQL.Updates.20180305.149X")
- [PostgreSQL 14.8](#AuroraPostgreSQL.Updates.20180305.148X "#AuroraPostgreSQL.Updates.20180305.148X")
- [PostgreSQL 14.7 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.147X "#AuroraPostgreSQL.Updates.20180305.147X")
- [PostgreSQL 14.6](#AuroraPostgreSQL.Updates.20180305.146X "#AuroraPostgreSQL.Updates.20180305.146X")
- [PostgreSQL 14.5 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.145X "#AuroraPostgreSQL.Updates.20180305.145X")
- [PostgreSQL 14.4 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.144X "#AuroraPostgreSQL.Updates.20180305.144X")
- [PostgreSQL 14.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.143X "#AuroraPostgreSQL.Updates.20180305.143X")

### PostgreSQL 14.20

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.20. For more information about
the improvements in PostgreSQL 14.20, see [PostgreSQL release
14.20](https://www.postgresql.org/docs/14/release-14-20.html "https://www.postgresql.org/docs/14/release-14-20.html").

###### Releases and patches

- [Aurora PostgreSQL 14.20.1, January 16th, 2026](#aurorapostgresql-versions-version14201x-14201 "#aurorapostgresql-versions-version14201x-14201")
- [Aurora PostgreSQL 14.20, December, 18, 2025](#aurorapostgresql-versions-version1420x-1420 "#aurorapostgresql-versions-version1420x-1420")

#### Aurora PostgreSQL 14.20.1, January 16th, 2026

**Critical stability enhancements**

- Fixed a timing condition in the aws_s3 extension which, in rare cases, can cause database unavailability
- Fixed an issue where an UPDATE statement with OUTPUT clause may skip rows when there are concurrent updates on the same row

#### Aurora PostgreSQL 14.20, December, 18, 2025

**New features**

- Introduced a change which improves static availability of Aurora PostgreSQL writers when, in rare conditions, write operations to storage are delayed due to undergoing storage node maintenance.
- Improvements to minimize switchover downtime during Blue/Green switchover operations, by temporarily blocking transaction commit operations on the Blue environment prior to switchover, reducing drift between the Blue and Green clusters.
- Improved recovery time by optimizing commit log (clog) loading during database cold starts and unplanned restarts, with significant benefits for smaller instances with limited CPU cores.

**Critical stability enhancements**

- Improved cold start performance through faster cache initialization.
- Reduced memory footprint for idle connections in Serverless v2 instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")

- Fixed a database shutdown issue that could cause major version upgrades to fail.
- Fixed a rare major version upgrade failure with large memory allocations.
- Fixed an issue preventing rds_superuser from managing prepared transactions owned by other users.

**General enhancements**

- Updated the following extensions:
  - h3_pg to version 4.2.3.

- Fixed a race condition in Postgres lock release with optimized read enabled.
- Improved PgAudit memory usage during parameter-heavy operations.
- Fixed database initialization failure when max_connections is set to low values.
- Improved Serverless v2 scaling performance under high CPU load.
- Improved Serverless v2 write performance.
- Fixed delays in Serverless v2 scale-down operations.
- Fixed multiple low-risk memory leaks.
- Improved database shutdown during maintenance to enhance availability.
- Improved database startup performance through optimized storage initialization.
- Fixed storage metadata initialization issue that could delay engine startup.
- Fixed region determination failures in aws_s3, aws_ml, and aws_lambda extensions.
- Fixed crash scenario when using pg_buffercache extension during Serverless v2 scaling.

### PostgreSQL 14.19

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.19. For more information about
the improvements in PostgreSQL 14.19, see [PostgreSQL release
14.19](https://www.postgresql.org/docs/14/release-14-19.html "https://www.postgresql.org/docs/14/release-14-19.html").

###### Releases and patches

- [Aurora PostgreSQL 14.19.1, November 25, 2025](#aurorapostgresql-versions-version14191x-14191 "#aurorapostgresql-versions-version14191x-14191")
- [Aurora PostgreSQL 14.19, November 25, 2025](#aurorapostgresql-versions-version1419x-1419 "#aurorapostgresql-versions-version1419x-1419")

#### Aurora PostgreSQL 14.19.1, November 25, 2025

**Critical stability enhancements**

- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")

- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 14.19, November 25, 2025

**New features**

- Introduced a new feature to significantly reduce database downtime during restarts by initializing Aurora storage metadata in parallel and reducing contention during initialization.

**Critical stability enhancements**

- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/")
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/")
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/")

- Fixed an issue in logical replication where subscriber databases could skip replicating transactions after recovering from a crash.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed a security issue when altering routine ownership.

**General enhancements**

- Updated the following extensions:
  - oracle_fdw to version to 2.8.0
  - pg_repack extension to version 1.5.2
  - aws_lamba extension to version 2.0

- Improved file metadata initialization times.
- Fixed an issue that caused reader instance to restart when attempting to create PostgreSQL SLRU files.
- Fixed an issue which caused prolonged Serverless v2 scaling time.
- Fixed an issue that could cause database restart during Serverless v2 scaling.
- Fixed a timing issue in replication diagnostics that could prevent accurate reporting of Aurora replica recovery status when state transitions occur in rapid succession.
- Updated the aws_lambda extension to version 2.0, which resolves a performance issue that was present in version 1.0.
- Added support to include Geodetic TIFF grid files for PROJ.
- Fixed an issue that could cause database restart during aws_s3 export.
- Addressed an issue with logging when replication slots are invalidated.
- Fixed CVE-2023-3079 for V8 Engine in the PLV8 extension.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue where read queries may time out on Aurora replica nodes during the replay of lazy truncation triggered by vacuum on the writer node.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue which prevented online recovery of an Aurora Replica forcing offline recovery.

### PostgreSQL 14.18

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.18. For more information
about the improvements in PostgreSQL 14.18, see [PostgreSQL release
14.18](https://www.postgresql.org/docs/14/release-14-18.html "https://www.postgresql.org/docs/14/release-14-18.html").

###### Releases and patches

- [Aurora PostgreSQL 14.18.4, January 15,
  2026](#aurorapostgresql-versions-version14184x-14184 "#aurorapostgresql-versions-version14184x-14184")
- [Aurora PostgreSQL 14.18.3, September 16,
  2025](#aurorapostgresql-versions-version14183x-14183 "#aurorapostgresql-versions-version14183x-14183")
- [Aurora PostgreSQL 14.18.2, August 8,
  2025](#aurorapostgresql-versions-version14182x-14182 "#aurorapostgresql-versions-version14182x-14182")
- [Aurora PostgreSQL 14.18.1, June 30,
  2025](#aurorapostgresql-versions-version14181x-14181 "#aurorapostgresql-versions-version14181x-14181")
- [Aurora PostgreSQL 14.18, June 30,
  2025](#aurorapostgresql-versions-version1418x-1418 "#aurorapostgresql-versions-version1418x-1418")

#### Aurora PostgreSQL 14.18.4, January 15,

2026

**Critical stability enhancements**

- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 14.18.3, September 16,

2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few
  seconds longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that
  might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when fetching
  pages from storage.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security
  vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed an issue that can cause reboots of the primary db instance when reading from a
  logical replication slot in the presence of frequent DDL if
  aurora.enhanced_logical_replication is enabled.
- Fixed a race where old writer may not step down after a new writer is promoted and
  continues to write.

**General enhancements**

- Implemented enhanced error handling mechanisms during TDS Connection reset
  operations.
- Fixed an issue that could in certain cases prevent online recovery of an Aurora Replica
  from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on
  tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately
  after installing the extension or resetting shared memory.
- Fixed an issue with Babelfish ZDP that could lead to instance reboot after
  minor version ugprade in some cases.
- Fixed an issue in enforcing, validating and evolving the `plans` extension
  in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with
  all-column selections.
- Fixed an issue with prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release
  containing The `PostGIS` extension 3.5.1 without running
  postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart
  of an Aurora replica in a Global Database.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 14.18.2, August 8,

2025

**Critical stability enhancements**

- Fixed an issue which could prevent logical replication from resuming after
  upgrade.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when
  performing reads from Aurora Storage.

#### Aurora PostgreSQL 14.18.1, June 30,

2025

**High priority enhancements**

- Fixed a performance issue affecting instance restart operations.

#### Aurora PostgreSQL 14.18, June 30,

2025

**New features**

- Improved Serverless v2 scaling for storage bound workloads.
- Improved Serverless v2 scaling through optimized management of memory maps.

**Critical stability enhancements**

- Fixed an issue where Serverless instances would fail to perform Zero Downtime Patching
  after automatic resume.
- Added library dependency verification during minor and patch upgrades to ensure
  storage metadata recovery is safe before proceeding.

**High priority enhancements**

- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads.
- Fixed an issue where server will fail to start if a previous startup was prematurely
  terminated.

**General enhancements**

- Updated the following extensions:
  - apg_plan_mgmt to 2.9.
  - The `pgaudit` extension to 1.6.3.
  - The `rdkit` extension to 4.6.1 (2024_09_6).
  - The `pg_repack` extension to 1.5.1.
  - The `pglogical` extension to 2.4.5.

- Improvements to make Serverless v2 scaling more efficient on reader nodes.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  sub-transactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue that prevents Zero Downtime Patching from completing successfully on
  Serverless v2 auto-pause enabled instances.
- Fixed an issue in pgdam that causes the engine (with pgdam enabled) to crash when
  hitting maximum connections.
- Fixed an issue in the `pg_bigm` extension that can cause unavailability
  when the extension interacts with the GIN index.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
- Added function aurora_stat_resource_usage() to report current CPU usage, allocated and
  used memory for all the backends.
- Fixed an issue which prevented Zero Downtime Patching when cache recovery is
  disabled.
- Fixed a synchronization issue where Zero Downtime Patching could fail due to premature
  engine ready state reporting.
- Fixed an issue in checkpoint replication to have storage metadata position be
  consistent in reader.
- Fixed an issue which causes RO node to restart while its reconnecting to RW
  node.
- Fixed an issue where RO client process can be stuck in LWLock:BufferIO wait event
  after being disconnected from the writer.
- Fixed an issue where RO node could crash when frequently falling behind RW
  node.
- Fixed an issue in the aws_s3 extension that could cause an import operation to restart
  and reinsert previously inserted rows.
- Improved performance of EXPLAIN operations for queries involving tables with many
  columns and complex relations.

### PostgreSQL 14.17

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.17. For more information
about the improvements in PostgreSQL 14.17, see [PostgreSQL release
14.17](https://www.postgresql.org/docs/14/release-14-17.html "https://www.postgresql.org/docs/14/release-14-17.html").

###### Releases and patches

- [Aurora PostgreSQL 14.17.5, February 10, 2026](#aurorapostgresql-versions-version1417x-1417 "#aurorapostgresql-versions-version1417x-1417")
- [Aurora PostgreSQL 14.17.4, October 9, 2025](#aurorapostgresql-versions-version14174x-14174 "#aurorapostgresql-versions-version14174x-14174")
- [Aurora PostgreSQL 14.17.3, June 3, 2025](#aurorapostgresql-versions-version14173x-14173 "#aurorapostgresql-versions-version14173x-14173")
- [Aurora PostgreSQL 14.17.2, May 01,
  2025](#aurorapostgresql-versions-version14172x-14172 "#aurorapostgresql-versions-version14172x-14172")
- [Aurora PostgreSQL 14.17, April 07,
  2025](#aurorapostgresql-versions-version1417x-1417 "#aurorapostgresql-versions-version1417x-1417")

#### Aurora PostgreSQL 14.17.5, February 10, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://nvd.nist.gov/vuln/detail/CVE-2025-12817 "https://nvd.nist.gov/vuln/detail/CVE-2025-12817").
  - [CVE-2025-12818](https://nvd.nist.gov/vuln/detail/CVE-2025-12818 "https://nvd.nist.gov/vuln/detail/CVE-2025-12818").

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself.
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 14.17.4, October 9, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds
  longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might
  result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables
  larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after
  installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving the `plans` extension in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with all-column
  selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing
  The `PostGIS` extension 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an
  Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans` extension using the “bitmap
  heap scan” access method.
- Fixed an issue impacting query execution performance for execution the `plans` extension using the
  “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 14.17.3, June 3, 2025

**Critical stability enhancements**

- Fixed stuck scaling for serverless db instances with zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing actions
  with Aurora Storage.
- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.
- Fixed an issue in handling parameter lists from previous versions of Query Plan Management.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Fixed an issue that can cause RO instance crash under heavy workload.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.

#### Aurora PostgreSQL 14.17.2, May 01,

2025

**Critical priority enhancements**

- Fixed an issue which can cause the database to become unresponsive when performing
  actions with Aurora storage.

#### Aurora PostgreSQL 14.17, April 07,

2025

**New features**

- Aurora Optimized Reads now enables users to resize the allocated space for Optimized
  Reads-enabled temporary objects on Aurora I/O-Optimized clusters using a dynamic parameter
  `aurora_temp_space_size`. For more information. see [Aurora Optimized Reads](../AuroraUserGuide/AuroraPostgreSQL.optimized.md "../AuroraUserGuide/AuroraPostgreSQL.optimized.md").

**Critical stability enhancements**

- When the system is under critical memory pressure for an extended duration, the
  largest customer backend will be cancelled to prevent system from restarting due to out of
  memory.

**High priority enhancements**

- Fixed an issue where Aurora in-Region failovers would result in failures in database
  startup.
- Fixed a security issue in the `rds_activity_stream` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Aurora storage metadata now initializes more quickly during unplanned failovers and
  server restarts, reducing overall downtime. Larger instances benefit the most by
  leveraging higher parallelism.
- Improved performance of file metadata operations.
- Made improvements to database downtime during a `planned` extension
  switchover for Global Databases.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
  - Creating temporary objects with syntax such as CREATE TEMPORARY TABLE x AS SELECT \* FROM isn't supported.
  - Creating indexes on temporary tables isn't supported.

- The Blue/Green deployment switchover won’t be blocked by the `REFRESH
MATERIALIZED VIEW` statement.
- Improved allocation of Write-Ahead Log (WAL) stream numbers, resulting in increased
  throughput for write-heavy workloads on the new Graviton 4 high-end instances.
- Fixed an issue where the query identifier (queryid) wasn't being correctly updated in
  pg_stat_activity when using extended protocol in pipeline mode.
- Fixed an issue where reader upgrade was taking longer than expected.
- Updated the following extensions:
  - Update the `pgvector` extension to 0.8.0.
  - Update the `pg_cron` extension to v1.6.5.
  - Update the `tds_fdw` extension to 2.0.4.
  - Update the `postgis` extension to 3.5.1.
  - Update the `pg_partman` extension to v5.2.4.
  - Update the `orafce` extension to 4.14.0.
  - Update the `rds_tools` extension to 1.9.
  - Update the `rdkit` extension to Release_2024_09_3.

### PostgreSQL 14.15

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.15. For more information
about the improvements in PostgreSQL 14.15, see [PostgreSQL release
14.15](https://www.postgresql.org/docs/14/release-14-15.html "https://www.postgresql.org/docs/14/release-14-15.html").

###### Releases and patches

- [Aurora PostgreSQL 14.15.7, January 28, 2026](#aurorapostgresql-versions-version14157x-14157 "#aurorapostgresql-versions-version14157x-14157")
- [Aurora PostgreSQL 14.15.6, November 13, 2025](#aurorapostgresql-versions-version14156x-14156 "#aurorapostgresql-versions-version14156x-14156")
- [Aurora PostgreSQL 14.15.5, June 24, 2025](#aurorapostgresql-versions-version14155x-14155 "#aurorapostgresql-versions-version14155x-14155")
- [Aurora PostgreSQL 14.15.4, March 24,
  2025](#aurorapostgresql-versions-version14154x-14154 "#aurorapostgresql-versions-version14154x-14154")
- [Aurora PostgreSQL 14.15.3, February
  13, 2025](#aurorapostgresql-versions-version14153x-14153 "#aurorapostgresql-versions-version14153x-14153")
- [Aurora PostgreSQL 14.15.2, January 20th,
  2025](#aurorapostgresql-versions-version14152x-14152 "#aurorapostgresql-versions-version14152x-14152")
- [Aurora PostgreSQL 14.15.1, December
  27, 2024](#aurorapostgresql-versions-version14151x-14151 "#aurorapostgresql-versions-version14151x-14151")
- [Aurora PostgreSQL 14.15, December 27,
  2024](#aurorapostgresql-versions-version1415x-1415 "#aurorapostgresql-versions-version1415x-1415")

#### Aurora PostgreSQL 14.15.7, January 28, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 14.15.6, November 13, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 14.15.5, June 24, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.15.4, March 24,

2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 14.15.3, February

13, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8` extension.

#### Aurora PostgreSQL 14.15.2, January 20th,

2025

**Critical Priority enhancements**

- Fixed a security issue in the rds_activity_stream extension.

**High priority enhancements**

- Fixed an issue in Global DB switchover and failover that could result in customers
  needing to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some
  cases.

**General enhancements**

- Fixed an ownership issue where the `postgis_raster` extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 14.15.1, December

27, 2024

**Critical Priority enhancements**

- Fixed an issue where the server was restarting when the connections were reset by the
  peer.

#### Aurora PostgreSQL 14.15, December 27,

2024

###### New features

- Optimized the minor version and patch upgrade process to reduce downtime for read
  replicas.

###### Critical stability enhancements

- Fixed an issue that in rare cases can cause CPU usage spike.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")

- Fixed an issue related to logical replication when processing large aborted
  transactions in the presence of catalog modifying operations. This can result in a
  transient failure of the logical replication process.

###### General enhancements

- Made multiple improvements to Aurora in-Region failover which reduces database downtime
  further by improving storage metadata and faster buffer cache initialization.
- Made multiple improvements to upgrades with Zero-Downtime Patching (ZDP) which reduces
  connection restore time and enhances ZDP resilience from failures.
- Fixed an issue where the server_id value wasn’t updated after an Amazon RDS Blue/Green
  Deployment switchover.
- Fixed an issue that could cause database restart during hash index extension.
- Fixed an issue that would cause migration from RDS PostgreSQL to fail in the presence
  of nested tablespaces.
- Fixed an issue that would cause excessive engine startup times in the presence of a
  large number of logical replication files.
- Fixed an issue that could cause a database restart when calling functions from `aws_s3`,
  `aws_lambda`, and `aws_ml` extensions in the same database session as `aws_s3.table_import_from_s3()`.
  This fix may decrease the per-call performance of functions from the `aws_s3`, `aws_lambda`, and `aws_ml` extensions.
- Fixed an issue that could cause database restart during serverless scaling.
- Fixed an issue where AuroraForwardingReplicaReadWaitLatency and
  AuroraForwardingReplicaDMLLatency were reported incorrectly.
- Fixed an issue that prevented updating the `pgTAP` extension to version
  1.3.0 or later.
- Fixed an issue in the `PostGIS` extension, which in rare cases, could cause
  a DB instance restart.
- Added generic `plan` informations in
  `aurora_stat_statements`/`aurora_stat_plans`.
- Fixed an issue in the `pg_repack` extension that compromises the integrity
  of invalid indexes.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_cron` extension to v1.6.4.
  - `PostGIS` extension to version 3.4.3.
  - `PROJ` library extension to version 9.5.0.
  - `GEOS` library extension to verison 3.13.0.
  - `orafce` extension to 4.12.0.
  - `pgvector` extension to 0.7.4.
  - `RDKit` extension to 2024_03_6 release (4.6).
  - The `pg_hint_plan` extension to version extension 1.4.3.

### PostgreSQL 14.13

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.13. For more
information about the improvements in PostgreSQL 14.13, see [PostgreSQL release 14.13](https://www.postgresql.org/docs/14/release-14-13.html "https://www.postgresql.org/docs/14/release-14-13.html").

###### Releases and patches

- [Aurora PostgreSQL 14.13.7, February 13, 2026](#aurorapostgresql-versions-version14137x-14137 "#aurorapostgresql-versions-version14137x-14137")
- [Aurora PostgreSQL 14.13.6, November 21, 2025](#aurorapostgresql-versions-version14136x-14136 "#aurorapostgresql-versions-version14136x-14136")
- [Aurora PostgreSQL 14.13.5, July 11, 2025](#aurorapostgresql-versions-version14135x-14135 "#aurorapostgresql-versions-version14135x-14135")
- [Aurora PostgreSQL 14.13.4, April 17, 2025](#aurorapostgresql-versions-version14134x-14134 "#aurorapostgresql-versions-version14134x-14134")
- [Aurora PostgreSQL 14.13.2, January 29, 2025](#aurorapostgresql-versions-version14132x-14132 "#aurorapostgresql-versions-version14132x-14132")
- [Aurora PostgreSQL 14.13.1, January 02, 2025](#aurorapostgresql-versions-version14131x-14131 "#aurorapostgresql-versions-version14131x-14131")
- [Aurora PostgreSQL 14.13, September 30, 2024](#aurorapostgresql-versions-version1413x-1413 "#aurorapostgresql-versions-version1413x-1413")

#### Aurora PostgreSQL 14.13.7, February 13, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

#### Aurora PostgreSQL 14.13.6, November 21, 2025

**Critical stability enhancements**

- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 14.13.5, July 11, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.13.4, April 17, 2025

**High priority enhancements**.

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 14.13.2, January 29, 2025

**Critical stability enhancements**.

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**.

- Fixed an issue in Global DB switchover and failover that could result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.

**General enhancements**.

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 14.13.1, January 02, 2025

**Critical stability enhancements**

- Fixed an issue related to Query Plan Management background worker.
- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed issue where Aurora in-Region failovers would result in failures in database startup.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue that prevented the scaling of Aurora Serverless v2 Read Replicas when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in longer
  upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime further
  with faster buffer cache initialization.
- Fixed an issue where reserved keyword “PRIMARY” caused syntax errors when
  used as a column name or alias in DML and DDL statements.
- Fixed an issue that could cause an error in the wal sender process when resuming logical
  replication.
- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension 2 installation.

#### Aurora PostgreSQL 14.13, September 30, 2024

**New features for 14.13**

- Introduced a new fast failover feature to reduce database downtime during the `planned` extension failover
  events with fast storage metadata initialization and fast buffer cache recovery.
- Introduced an optimization to reduce Zero Downtime Patching (ZDP) quiet point duration to 1 second.

**High priority enhancements for 14.13**

- Fixed issues where the replication of vacuum operations may cause a restart when handling
  conflicts with user queries.
- Fixed an issue where deleting a large range of keys from a BTree index could cause
  concurrent scans to crash.

**General enhancements for 14.13**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation. For more
  information, see [AWS-LC is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/")
  on AWS Security Blog.
- Improvements to database startup time during initialization and engine
  upgrades.
- Fixed an issue that prevented the inclusion of the `pg_bigm` extension in
  shared_preload_libraries.
- Fixed an issue during Zero Downtime Patching which causes some connections to be terminated
  due to long transferring time. A new ZDP metric in postgresql.log called
  `ZD_SOCKET_TRANSFER_CONN_DROPPED` represents these dropped connections.
- Improved reader availability for Aurora Replicas when using system administration functions.
- Fixed an in-memory two-phase commit (2PC) metadata caching issue that caused out-of-memory
  error on Aurora read replicas replicating from RDS PostgreSQL source instances.
- Introduced a new function pgadmap_get_set_mapping_cmd() in the `pg_ad_mapping` extension to
  display commands required to recreate existing Active directory security group to Aurora
  PostgreSQL database role mappings.
- Fixed an issue in storage metadata initialization that can cause prolonged database startup
  time.
- Fixed an issue that will prevent reclaiming Aurora storage space during major version
  upgrade.
- Fixed an issue that prevents ZDP from completing successfully on
  Optimized Reads-enabled instances.

**Additional improvements and enhancements for 14.13**

- Updated the following extensions:
  - `pgvector` extension to version 0.7.3.
  - `mysql_fdw` extension to version REL-2_9_2.
  - `orafce` extension to version 4.10.3.
  - `pgTAP` extension to version 1.3.3.
  - `pg_cron` extension to version 1.6.3.
  - `RDKit` extension to version 4.5 (Release 2024_03_5).
  - `wal2json` extension to version 2.6.
  - pg_ad_mapping extension to version 1.0.
  - `HypoPG` extension to version 1.4.1.

### PostgreSQL 14.12

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.12. For more information
about the improvements in PostgreSQL 14.12, see [PostgreSQL release
14.12](https://www.postgresql.org/docs/14/release-14-12.html "https://www.postgresql.org/docs/14/release-14-12.html").

###### Releases and patches

- [Aurora PostgreSQL 14.12.5, July 17, 2025](#aurorapostgresql-versions-version14125x-14125 "#aurorapostgresql-versions-version14125x-14125")
- [Aurora PostgreSQL 14.12.4, March
  25, 2025](#aurorapostgresql-versions-version14124x-14124 "#aurorapostgresql-versions-version14124x-14124")
- [Aurora PostgreSQL 14.12.3, January
  29, 2025](#aurorapostgresql-versions-version14123x-14123 "#aurorapostgresql-versions-version14123x-14123")
- [Aurora PostgreSQL 14.12.2, January
  23, 2025](#aurorapostgresql-versions-version14122x-14122 "#aurorapostgresql-versions-version14122x-14122")
- [Aurora PostgreSQL 14.12.1,
  September 27, 2024](#aurorapostgresql-versions-version1412x-14121 "#aurorapostgresql-versions-version1412x-14121")
- [Aurora PostgreSQL 14.12,
  August 8, 2024](#aurorapostgresql-versions-version1412x-1412 "#aurorapostgresql-versions-version1412x-1412")

#### Aurora PostgreSQL 14.12.5, July 17, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.12.4, March

25, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 14.12.3, January

29, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 14.12.2, January

23, 2025

###### Critical stability enhancements

- Fixed an issue related to Query Plan Management background worker.

###### High priority enhancements

- Fixed an issue in Global DB switchover and failover that could result in
  customers needing to rebuild their mirror clusters.
- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in
  longer upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime
  further with faster buffer cache initialization.
- Fixed an issue that could cause an error in the wal sender process when
  resuming logical replication.

#### Aurora PostgreSQL 14.12.1,

September 27, 2024

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

#### Aurora PostgreSQL 14.12,

August 8, 2024

###### New features

- Aurora Serverless v2 now applies pending database parameter
  `max_connections` changes during upgrades. The Serverless V2
  capacity changes result in pending `max_connections` changes. As many
  ZDP supported connections as allowed by `max_connections` will be
  preserved during upgrades.
- Introduced a feature to improve database start up time through faster buffer
  cache initialization during restarts and database upgrades.
- Minor version and patch upgrades may now complete faster in some cases.
- Reduced Aurora Serverless v2 scale up and scale down time in the presence of
  data intensive workloads or long running queries and busy or unresponsive
  connections.
- Added per-query memory usage information to
  `aurora_stat_statements` and `aurora_stat_plans`. For
  more information, see [aurora_stat_statements](../AuroraUserGuide/aurora_stat_statements.md "../AuroraUserGuide/aurora_stat_statements.md").

###### Critical stability enhancements

- Fixed a pg_repack issue that would incorrectly allow two vacuum processes to
  operate concurrently on the same table.

###### High priority enhancements

- Fixed an issue which leads to cancellation of long-running queries on Global
  Database replica instances.

###### General enhancements

- Improved Aurora PostgreSQL performance for generative AI workloads using
  `pgvector`.
- Fixed issue where minor version upgrades with ZDP would fail in some cases
  resulting in longer upgrade times.
- Improved replay performance of vacuum operations on Aurora Replica
  instances.
- Fixed a bug where JDBC connections may not be preserved during ZDP enabled
  upgrades.
- Improvement to reduce postgres private memory fragmentation.
- Fixed an issue that caused two-phase commit files to remain, preventing proper
  cleanup.
- Improved memory handling while processing two phase commit files.
- Fixed an issue resulting in degraded performance during query planning on
  Aurora replicas.
- Improved availability of Aurora read replicas.
- Fixed an issue where server might restart if background worker tries to spawn
  parallel workers.
- Fixed an issue where the instance may restart when logically applying changes
  from a remote server when under resource constraints.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` extension to version 4.9.4.
  - `pg_cron` extension to version 1.6.2.
  - `pg_hint_plan` extension to version 1.4.2.
  - `pg_partman` extension to version 5.1.0.
  - `pg_repack` extension to version 1.5.0.
  - `pg_tle` to version 1.4.0.
  - `pg_vector` extension to version 0.7.0.
  - `pgrouting` extension to version 3.6.2.
  - `pgTap` extension to version 1.3.2.
  - `PostGIS` extension to version 3.4.2.
  - `RDKit` extension to version 2024_03_1.

### PostgreSQL 14.11

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.11. For more
information about the improvements in PostgreSQL 14.11, see [PostgreSQL release 14.11](https://www.postgresql.org/docs/14/release-14-11.html "https://www.postgresql.org/docs/14/release-14-11.html").

###### Releases and patches

- [Aurora PostgreSQL 14.11.6, July 28, 2025](#aurorapostgresql-versions-version14116x-14116 "#aurorapostgresql-versions-version14116x-14116")
- [Aurora PostgreSQL 14.11.5, April 16, 2025](#aurorapostgresql-versions-version14115x-14115 "#aurorapostgresql-versions-version14115x-14115")
- [Aurora PostgreSQL 14.11.4, February 02, 2025](#aurorapostgresql-versions-version14114x-14114 "#aurorapostgresql-versions-version14114x-14114")
- [Aurora PostgreSQL 14.11.3, October 7, 2024](#aurorapostgresql-versions-version1411x-14113 "#aurorapostgresql-versions-version1411x-14113")
- [Aurora PostgreSQL 14.11.2, June 20, 2024](#AuroraPostgreSQL.Updates.20180305.14112 "#AuroraPostgreSQL.Updates.20180305.14112")
- [Aurora PostgreSQL 14.11.1, April 29, 2024](#AuroraPostgreSQL.Updates.20180305.14111 "#AuroraPostgreSQL.Updates.20180305.14111")

#### Aurora PostgreSQL 14.11.6, July 28, 2025

**Critical stability enhancements**.

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.11.5, April 16, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 14.11.4, February 02, 2025

**Critical stability enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418")
  for V8 Engine in the `PLV8` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

- **General enhancements**

Fixed an ownership issue where the postgis_raster extension could not be updated correctly
from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 14.11.3, October 7, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache instances while upgrading into this version.

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.11.2, June 20, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed an issue with background worker where it may crash when executed in parallel worker context.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed issues in how two-phase commit files are handled.

####

Aurora PostgreSQL 14.11.1, April 29, 2024

###### New features

- Added resource usage summary to `pg_dump`.
- Added function overloading for `aurora_stat_statements(bool showtext)` and `aurora_stat_plans(bool showtext)`.

###### General enhancements

- Fixed multiple minor version upgrade issues to improve connection preservation with zero-downtime patching.
- Reduced database boot time due to improved initialization time for large volumes.
- Introduced faster COPY operations by reducing contention on the relation extension lock and proactively extending relations.
- Improvements to reduce replication lag by intelligently skipping the replay of certain log records, thereby reducing the replay load.
- Fixed an issue during recovery conflict on a read node which, in rare cases, could cause brief unavailability.
- Fixed an issue where a database would fail to startup during a major version upgrade patch, in rare scenarios.
- Improved availability of read replicas by allowing recovery from replication errors in more situations.
- Fixed an issue that would cause zero-downtime patching to timeout.
- Fixed an issue resulting in a deadlock when a logical replication table synchronization operation fails.
- Fixed a logical replication decoding issue that fails to process catalog modifying changes after spilling to storage
  if there was a concurrent aborted sub-transaction.
- Improved log record validation before it is written to storage.
- Fixed an issue that would result in sessions incorrectly reporting ClientRead wait events after a zero-downtime patching event.
- Fixed an ambiguous function definition of aws_s3.query_export_to_s3 when upgrading the aws_s3 extension from version 1.1 to 1.2.

###### High priority enhancements

- Fixed an issue related to resuming a logical replication slot where, in rare cases, it could cause the slot to become stuck.
- Fixed an issue that would result in a restart when creating a database in a tablespace.
- Fixed an issue related to incorrect logical replication error handling to improve DB stability.

###### Critical stability enhancements

- Fixed an issue related to replication origins that in rare cases might result in longer recovery time and impact availability.
- Fixed an issue that in rare cases may cause transactions to be partially replicated by newly created logical replication slots. For more information, see
  [Potential data loss due to race condition during logical replication slot creation](https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com "https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com").
- Fixed an issue where `pg_stat_statements` can cause zero-downtime patching to fail.
- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_tle` extension to version 1.3.4.
  - `PLV8` extension to version 3.1.10.
  - RDKit Cartridge to version Release_2023_09_4.

- New GUC Parameters has been added
  - `pgtle.clientauth_databases_to_skip`
  - `pgtle.clientauth_db_name`
  - `pgtle.clientauth_num_parallel_workers`
  - `pgtle.clientauth_users_to_skip`
  - `pgtle.enable_clientauth`
  - `pgtle.passcheck_db_name`

### PostgreSQL 14.10

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.10. For more
information about the improvements in PostgreSQL 14.10, see [PostgreSQL release 14.10](https://www.postgresql.org/docs/14/release-14-10.html "https://www.postgresql.org/docs/14/release-14-10.html").

###### Releases and patches

- [Aurora PostgreSQL 14.10.8, July 30, 2025](#aurorapostgresql-versions-version14108x-14108 "#aurorapostgresql-versions-version14108x-14108")
- [Aurora PostgreSQL 14.10.7, April 22, 2025](#aurorapostgresql-versions-version14107x-14107 "#aurorapostgresql-versions-version14107x-14107")
- [Aurora PostgreSQL 14.10.6, February 5, 2025](#aurorapostgresql-versions-version14106x-14106 "#aurorapostgresql-versions-version14106x-14106")
- [Aurora PostgreSQL 14.10.5, September 17, 2024](#aurorapostgresql-versions-version1410x-14105 "#aurorapostgresql-versions-version1410x-14105")
- [Aurora PostgreSQL 14.10.4, June 24, 2024](#AuroraPostgreSQL.Updates.20180305.14104 "#AuroraPostgreSQL.Updates.20180305.14104")
- [Aurora PostgreSQL 14.10.3, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.14103 "#AuroraPostgreSQL.Updates.20180305.14103")
- [Aurora PostgreSQL 14.10.2, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.14102 "#AuroraPostgreSQL.Updates.20180305.14102")
- [Aurora PostgreSQL 14.10.0, December 21, 2023](#AuroraPostgreSQL.Updates.20180305.14100 "#AuroraPostgreSQL.Updates.20180305.14100")

#### Aurora PostgreSQL 14.10.8, July 30, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vaccum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.10.7, April 22, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 14.10.6, February 5, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 14.10.5, September 17, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.10.4, June 24, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

####

Aurora PostgreSQL 14.10.3, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

####

Aurora PostgreSQL 14.10.2, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.10.0, December 21, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition to support
PostgreSQL versions 15.5, 14.10, 13.13, and 12.17. These releases contain product improvements and bug fixes made by the PostgreSQL community,
along with Aurora-specific improvements. New features and improvements for Babelfish for Aurora PostgreSQL version 3.4 are also included.

Refer to the Aurora version policy to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder,
if you are running any version of Amazon Aurora PostgreSQL version 11, you must upgrade to a newer major version by February 29, 2024.

###### New features

- Amazon Bedrock integration – By using the Amazon Aurora machine learning extension with your Aurora PostgreSQLDB cluster, you can now use Amazon Bedrock
  foundational AI models.
- Using Active Directory security groups for Aurora PostgreSQL access control – Add group role authentication support using AWS Directory Service for Microsoft Active Directory with the new `pg_ad_mapping` extension.
- Delegated Extension Support – This feature allows delegating extension management to lower privileged user with the new rds_extension role.
- Added support for `aurora_compute_plan_id` parameter which is turned on by default in an Aurora PostgreSQL DB Cluster and DB Parameter Group.
  For more information, see [Monitoring query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md "../AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.md").
- Query Plan Management (QPM) enhancements:
  - Plan outlines will be updated to the latest format version as part of the `update_plan_hash`
    action for `apg_plan_mgmt.validate_plans()`.
  - Support was added for parallel append enforcement as a part of parallel query enforcement.

- Added support for the `HypoPG` extension at version 1.4.0.
- Added support for the `h3-pg` extension and the `h3-postgis` extension at version 4.1.3.

###### High priority enhancements

- Fixed an issue which may cause a reboot when logically replicating changes in the presence of concurrently-running DDL or canceled sub-transactions
- Fixed an issue which may cause an Aurora replica to reboot when reading a page which was modified during `WAL` replay
- Fixed an issue where if a specific volume metadata is invalid on a source cluster, it will remain invalid on a cloned cluster. Since the
  clone cluster uses a new volume, the metadata will now be recreated.
- Fixed a bug that may cause an engine crash during zero-downtime patching (ZDP)
- Introduced a new parameter, `rds.enable_memory_management`, which is used to enable and disable the improved memory management feature.
- Improved index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General enhancements

- Fixed an issue which may cause an Aurora replica to reboot while reconnecting with the writer DB instance.
- Added support for the `rdkit.morgan_fp_size` parameter
- `rds-superuser` can now run the `pg_stat_reset_slru` function
- Fixed an issue where MultiXact SLRU accesses were not credited to the correct `pg_stat_slru` category.
- Fixed an issue which may cause unused `WAL` segements to not be properly removed
- Fixed an issue where `pglogical` does not correctly pass-through replication origin data when using the binary output format
- `rds_superuser` can now execute `ALTER COLLATION` to refresh the collation version of a locale in the catalog.
- Fixed a crash in `dblink` and `postgres_fdw` extensions due to invalid connections
- Fixed an issue where the `aws_s3` extension can import `HTTP` error responses into the table
- Fixed an issue which may cause an Aurora Replica instance with Optimized Reads to reboot while reconnecting with the writer DB instance.
- Fixed an issue which may cause an Aurora replica with Optimized Reads to reboot while caching a page to tiered cache.
- Record the version of the AWS independent default collation library version in `pg_collation catalog`.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `mysql_fdw` to version 2.9.1
  - `Oracle_fdw` to version 2.6.0
  - `Orafce` to version 4.6.0
  - `pg_cron` to version 1.6.0
  - `pg_proctab` to version 0.0.10
  - `pg_tle` to version 1.2.0
  - `plv8` to version 3.1.8
  - `PostGIS` to version 3.4.0
  - `prefix` to version 1.2.10
  - `RDKit` to version 4.4.0 (Release_2023_09_1)

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
14](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14").

### PostgreSQL 14.9

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.9. For more information
about the improvements in PostgreSQL 14.9, see [PostgreSQL release
14.9](https://www.postgresql.org/docs/14/release-14-9.html "https://www.postgresql.org/docs/14/release-14-9.html").

###### Releases and patches

- [Aurora PostgreSQL 14.9.11, August 5, 2025](#aurorapostgresql-versions-version14911x-14911 "#aurorapostgresql-versions-version14911x-14911")
- [Aurora PostgreSQL 14.9.10, May
  7, 2025](#aurorapostgresql-versions-version14910x-14910 "#aurorapostgresql-versions-version14910x-14910")
- [Aurora PostgreSQL 14.9.9, February 27, 2025](#aurorapostgresql-versions-version1499x-1499 "#aurorapostgresql-versions-version1499x-1499")
- [Aurora PostgreSQL 14.9.8,
  November 14, 2024](#aurorapostgresql-versions-version149x-1498 "#aurorapostgresql-versions-version149x-1498")
- [Aurora PostgreSQL 14.9.7, June 25,
  2024](#AuroraPostgreSQL.Updates.20180305.1497 "#AuroraPostgreSQL.Updates.20180305.1497")
- [Aurora PostgreSQL 14.9.6, March
  13, 2024](#AuroraPostgreSQL.Updates.20180305.1496 "#AuroraPostgreSQL.Updates.20180305.1496")
- [Aurora PostgreSQL 14.9.5, February
  22, 2024](#AuroraPostgreSQL.Updates.20180305.1495 "#AuroraPostgreSQL.Updates.20180305.1495")
- [Aurora PostgreSQL 14.9.3, December
  15, 2023](#AuroraPostgreSQL.Updates.20180305.1493 "#AuroraPostgreSQL.Updates.20180305.1493")
- [Aurora PostgreSQL 14.9.2, December
  13, 2023](#AuroraPostgreSQL.Updates.20180305.1492 "#AuroraPostgreSQL.Updates.20180305.1492")
- [Aurora PostgreSQL 14.9.1, November
  09, 2023](#AuroraPostgreSQL.Updates.20180305.1491 "#AuroraPostgreSQL.Updates.20180305.1491")
- [Aurora PostgreSQL 14.9.0, October
  24, 2023](#AuroraPostgreSQL.Updates.20180305.1490 "#AuroraPostgreSQL.Updates.20180305.1490")

#### Aurora PostgreSQL 14.9.11, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.9.10, May

7, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 14.9.9, February 27, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream`
  extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue in Global DB switchover and failover that can result in
  customers needing to rebuild their mirror clusters.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 14.9.8,

November 14, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when
  `rds.enable_plan_management` is turned on, but apg_plan_mgmt
  extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 14.9.7, June 25,

2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue which led to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same
  table.

#### Aurora PostgreSQL 14.9.6, March

13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

#### Aurora PostgreSQL 14.9.5, February

22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version
  upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes
  due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer
  failover.
- Fixed an issue where active transactions during logical replication slot
  creation may be partially replicated by the slot.

#### Aurora PostgreSQL 14.9.3, December

15, 2023

###### High priority enhancements

- Fixed an issue which may cause a reboot when logically replicating changes in
  the presence of concurrent canceled subtransactions and DDL

#### Aurora PostgreSQL 14.9.2, December

13, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page
  reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to
  database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone
  other than the table owner

#### Aurora PostgreSQL 14.9.1, November

09, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker
  processes

###### General enhancements

- Fixed an issue related to buffer pin locking that in rare cases can result in
  a crash

#### Aurora PostgreSQL 14.9.0, October

24, 2023

###### New features

- Added support for `mysql_fdw` version 2.9.0
- Added support in the `aws_s3` extension for exporting to an S3
  bucket encrypted with a customer managed KMS key
- Improved the availability of Aurora replicas in the global DB secondary
  clusters
- Added support for query plan capture on Aurora replicas
- Added support for query plan enforcement with materialize nodes
- Added support for query plan enforcement with parallel query operators
- Allowed query plans under a given cost threshold to not be captured

###### High priority enhancements

- Included optimizations to improve the time to scale up in Aurora Serverless
  instances

###### General enhancements

- Fixed an issue in the `aws_s3` extension where the number of rows
  exported is incorrectly reported when the total number exceeds 2 billion
- Provided options to configure timeouts in the `aws_s3` extension.
  By setting the following parameters (GUCs), customers will now be able to change
  the timeout thresholds for imports from S3:
  - `aws_s3.curlopt_low_speed_limit`
  - `aws_s3.curlopt_low_speed_time`

- Prevented instance creation failure in some edge cases
- Improved the performance of replay of commit transaction operations on Aurora
  replicas
- Fixed an issue where, in rare cases, an import from the `aws_s3`
  extension fails to complete
- Updated the GEOS library for PostGIS to version 3.12.0
- Improved Aurora Serverless v2 database memory scaling which reduces the overall
  database instance scale time
- Added the `WAIT_EVENT_Aurora_CLUSTER_CACHE_MANAGER_SENDER` wait
  event to denote wait times in the cluster cache manager sender
- Added the `WAIT_EVENT_Aurora_SERVERLESS_MONITORING_MAIN` wait event
  to denote wait times in Aurora Serverless resource monitoring
- Improved the handling of invalid non-persisted metadata during reads from
  storage on read replicas
- Fixed an issue where the database may crash during the start of a logical
  replication slot
- Increased the limit for `pg_cron`
  `cron.max_running_jobs` parameter from 100 to 1000
- The `pgAudit`
  `pgaudit.log_statement` parameter is now modifiable
- Introduced diagnostics for transient metadata used for I/O
- Fixed a bug in `CREATE TABLE` command to handle table name starting
  with '#' correctly

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` to version 4.3.0
  - `pg_logical` to version 2.4.3
  - `pg_tle` to version 1.1.1
  - `pgvector` to version 0.5.0
  - `PostGIS` to version 3.3.3
  - `RDKit` to version 4.3

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
14](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14").

### PostgreSQL 14.8

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.8. For more
information about the improvements in PostgreSQL 14.8, see [PostgreSQL release 14.8](https://www.postgresql.org/docs/14/release-14-8.html "https://www.postgresql.org/docs/14/release-14-8.html").

###### Releases and patches

- [Aurora PostgreSQL 14.8.10, August 5, 2025](#aurorapostgresql-versions-version14810x-14810 "#aurorapostgresql-versions-version14810x-14810")
- [Aurora PostgreSQL 14.8.9, April 30, 2025](#aurorapostgresql-versions-version1489x-1489 "#aurorapostgresql-versions-version1489x-1489")
- [Aurora PostgreSQL 14.8.8, February 24 2025](#aurorapostgresql-versions-version1488x-1488 "#aurorapostgresql-versions-version1488x-1488")
- [Aurora PostgreSQL 14.8.7, November 12, 2024](#aurorapostgresql-versions-version148x-1487 "#aurorapostgresql-versions-version148x-1487")
- [Aurora PostgreSQL 14.8.6, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1486 "#AuroraPostgreSQL.Updates.20180305.1486")
- [Aurora PostgreSQL 14.8.5, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1485 "#AuroraPostgreSQL.Updates.20180305.1485")
- [Aurora PostgreSQL 14.8.4, December 14, 2023](#AuroraPostgreSQL.Updates.20180305.1484 "#AuroraPostgreSQL.Updates.20180305.1484")
- [Aurora PostgreSQL 14.8.3, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.1483 "#AuroraPostgreSQL.Updates.20180305.1483")
- [Aurora PostgreSQL 14.8.2, October 4, 2023](#AuroraPostgreSQL.Updates.20180305.1482 "#AuroraPostgreSQL.Updates.20180305.1482")
- [Aurora PostgreSQL 14.8.0, July 13, 2023](#AuroraPostgreSQL.Updates.20180305.1480 "#AuroraPostgreSQL.Updates.20180305.1480")

#### Aurora PostgreSQL 14.8.10, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 14.8.9, April 30, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 14.8.8, February 24 2025

**Critical Priority enhancements**

- Fixed a security issue in the rds_activity_stream extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 14.8.7, November 12, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.8.6, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.8.5, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.8.4, December 14, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.8.3, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 14.8.2, October 4, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica
- Fixed an issue that would cause a crash when executing the `COPY FROM` command
- Fixed an issue that would cause high CPU usage and prevent new connections
- Fixed an issue where `UPDATE` and `DELETE` from a table with foreign key could fail unexpectedly with "ERROR: 40001: could not serialize access due to concurrent update when using Serializable snapshot"

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O
- Fixed an issue that prevented the enablement of improved memory management in certain scenarios in Aurora PostgreSQL 15.3

####

Aurora PostgreSQL 14.8.0, July 13, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition
to support PostgreSQL versions 15.3, 14.8, 13.11, 12.15, and 11.20. These releases contains product improvements and bug fixes made by
the PostgreSQL community, along with Aurora-specific improvements. The releases also contain new features and improvements for
[Babelfish for Aurora PostgreSQL version 3.2](AuroraBabelfish.md "AuroraBabelfish.md"), and improved support for
[AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish"). Refer to the [Amazon Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md")
to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder, if you are running any version of Amazon Aurora PostgreSQL 11,
you must upgrade to a newer major version by February 29, 2024.

###### New features

- This release contains memory management improvements which increase database stability and availability by proactively
  preventing issues caused by insufficient memory. For more information, see [Improved memory management in Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md "../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md").
- Added support for `pgvector` extension version 0.4.1

###### High priority enhancements

- Fixed an issue with the subtransaction metadata handling when performing a survivable reader reconnect
- Fixed an issue during ZDP which is related to the extension environment variables
- Addressed a transient error during logical replication that caused a process to incorrectly calculate that it had encountered an unexpected page
- Fixed an issue which causes a period of unavailability due to a partially created replication origin state file

###### General enhancements

- Addressed an issue where the computing query identifier displayed a warning, "WARNING: unrecognized node type: 378"
- Addressed an issue that caused the initial data sync of a relation to become blocked due to the premature removal of the logical replication slot on the publisher
- Added a new function, `aurora_stat_memctx_usage()`, to show backend memory use breakdown at a Postgres memory context level
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots
- Further reduced the database downtime during ZDP
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue which caused `pg_ls_waldir()` to return "ERROR: could not stat file"
- Added support for TLS 1.3 with ciphers TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384
- Addressed an issue that blocked a major version upgrade on the Aurora replica of an RDS for PostgreSQL DB instance
- Fixed an issue that could prevent scaling in Aurora Serverless v2 instances
- Fixed an issue in logical replication which, in rare cases, can cause a period of unavailability due to the incorrect subtransaction metadata
- Fixed an issue in the `pg_vector` extension where, in rare cases, infinite or NAN values caused a crash during the index creation
- Upgraded `GEOS` to version 3.11.2
- Upgraded `pg_cron` to version 1.5
- Upgraded `pg_partman` to version 4.7.3
- Upgraded `pg_tle` to version 1.0.3
- Upgraded `plv8` to version 3.1.6
- Upgraded `tds_fdw` to 2.0.3

### PostgreSQL 14.7 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.7. For more
information about the improvements in PostgreSQL 14.7, see [PostgreSQL release 14.7](https://www.postgresql.org/docs/14/release-14-7.html "https://www.postgresql.org/docs/14/release-14-7.html").

###### Releases and patches

- [Aurora PostgreSQL 14.7.9, November 6, 2024](#aurorapostgresql-versions-version147x-1479 "#aurorapostgresql-versions-version147x-1479")
- [Aurora PostgreSQL 14.7.8, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1478 "#AuroraPostgreSQL.Updates.20180305.1478")
- [Aurora PostgreSQL 14.7.7, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1477 "#AuroraPostgreSQL.Updates.20180305.1477")
- [Aurora PostgreSQL 14.7.6, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.1476 "#AuroraPostgreSQL.Updates.20180305.1476")
- [Aurora PostgreSQL 14.7.5, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.1475 "#AuroraPostgreSQL.Updates.20180305.1475")
- [Aurora PostgreSQL 14.7.4, October 5, 2023](#AuroraPostgreSQL.Updates.20180305.1474 "#AuroraPostgreSQL.Updates.20180305.1474")
- [Aurora PostgreSQL 14.7.3, July 24, 2023](#AuroraPostgreSQL.Updates.20180305.1473 "#AuroraPostgreSQL.Updates.20180305.1473")
- [Aurora PostgreSQL 14.7.2, May 10, 2023](#AuroraPostgreSQL.Updates.20180305.1472 "#AuroraPostgreSQL.Updates.20180305.1472")
- [Aurora PostgreSQL 14.7.1, April 5, 2023](#AuroraPostgreSQL.Updates.20180305.1471 "#AuroraPostgreSQL.Updates.20180305.1471")

#### Aurora PostgreSQL 14.7.9, November 6, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.7.8, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.7.7, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.7.6, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### High priority enhancements

- Improved the index scan query performance by skipping unnecessary B-tree page reads when a composite index is used with large data sets
- Fixed an issue with index scan queries that, in rare cases, could lead to database instance restarts

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.7.5, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 14.7.4, October 5, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O

####

Aurora PostgreSQL 14.7.3, July 24, 2023

###### General enhancements

- Fixed an issue related to storage space reclamation following table drop or reindex or truncate operations.
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue that prevented reclaiming storage on transaction commits
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

- Fixed multiple issues which can cause Aurora replicas with the improved read availability feature to restart when reconnecting with the writer instance
- Fixed an issue preventing a survivable reader reconnect

####

Aurora PostgreSQL 14.7.2, May 10, 2023

###### General enhancements

- Fixed an error when loading the `test_decoding` plugin in `pg_create_logical_replication_slot`
- Fixed an issue that causes logical replication to fail when using write-through cache
- Updated the Oracle client used by the `oracle_fdw` extension to version 21.9.0.0.0

####

Aurora PostgreSQL 14.7.1, April 5, 2023

###### New features

- Introduced a new QPM plan hash calculation for multi-schema support. If users want to use QPM in multi-schema
  environments, they can set the `apg_plan_mgmt.plan_hash` version to 2 and call `apg_plan_mgmt.validate_plans`('`update_plan_hash`').
- Logical replication enhancements to improve memory and CPU usage during the processing of large transactions.
- The CloudWatch metric `ReplicationSlotDiskUsage` now tracks logical replication specific storage across Aurora storage and local storage.
- Starting with Aurora PostgreSQL versions 15.2 and 14.7, a user needs to be granted the `CONNECT` privilege on each database to connect
  even if the user is granted access to the `rds_superuser` role. Prior to Aurora PostgreSQL versions 15.2 and 14.7, a user was able to connect to
  any database and system table if the user was granted the `rds_superuser` role. Previous Aurora PostgreSQL versions are not impacted by
  this change, and users with access to the `rds_superuser` role do not require the `CONNECT` privilege to access databases in their
  Aurora PostgreSQL cluster.

###### High priority stability enhancements

- Fixed an issue where the commit latency metrics weren't updated

###### General enhancements

- Upgraded `PROJ` support to version 9.1.0
- Upgraded the `GDAL` library in `PostGIS` to version 3.5.3
- Fixed the upgrade paths from `pg_hint_plan` 1.3x to 1.4
- Added support for the `TCN` and `SEG` extensions
- Improved performance of deletes from b-tree and hash indexes on Aurora replicas
- Includes Aurora Serverless v2 scaling enhancements
- Fixed an issue in QPM that prevented the enforcement of approved plans when joining partitioned tables
- Fixed an issue that caused incorrect buffer hit counts in `EXPLAIN`
- Improved the engine startup time, particularly on large instances with many objects
- The Aurora function `aurora_stat_logical_wal_cache()` is now visible to all users
- Fixed an issue in QPM that could cause unavailability when enforcing plans from prepared statements

###### Additional improvements and enhancements

- Updated the following extensions:
  - `hll` to version 2.17
  - `Oracle_fdw` to version 2.5.0
  - `orafce` to version 4.0.0
  - `pg_cron` to version 1.4.2
  - `pg_hint_plan` to version 1.4.1
  - `pg_logical` to version 2.4.2
  - `pg_trgm` to version 1.4
  - `pgrouting` to version 3.4.1
  - `plv8` to version 3.1.4
  - `PostGIS` to version 3.3.2
  - `SEG` to version 1.0
  - `TCN` to version 1.0
  - `wal2json` to version 2.5

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
14](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.14").

### PostgreSQL 14.6

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.6. For more
information about the improvements in PostgreSQL 14.6, see [PostgreSQL release 14.6](https://www.postgresql.org/docs/14/release-14-6.html "https://www.postgresql.org/docs/14/release-14-6.html").

###### Releases and patches

- [Aurora PostgreSQL 14.6.13, June 18, 2025](#aurorapostgresql-versions-version14613x-14613 "#aurorapostgresql-versions-version14613x-14613")
- [Aurora PostgreSQL 14.6.12, April 29, 2025](#aurorapostgresql-versions-version14612x-14612 "#aurorapostgresql-versions-version14612x-14612")
- [Aurora PostgreSQL 14.6.10, November 18, 2024](#aurorapostgresql-versions-version146x-14610 "#aurorapostgresql-versions-version146x-14610")
- [Aurora PostgreSQL 14.6.9, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1469 "#AuroraPostgreSQL.Updates.20180305.1469")
- [Aurora PostgreSQL 14.6.8, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1468 "#AuroraPostgreSQL.Updates.20180305.1468")
- [Aurora PostgreSQL 14.6.7, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.1467 "#AuroraPostgreSQL.Updates.20180305.1467")
- [Aurora PostgreSQL 14.6.6, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1466 "#AuroraPostgreSQL.Updates.20180305.1466")
- [Aurora PostgreSQL 14.6.5, October 04, 2023](#AuroraPostgreSQL.Updates.20180305.1465 "#AuroraPostgreSQL.Updates.20180305.1465")
- [Aurora PostgreSQL 14.6.4, September 13, 2023](#AuroraPostgreSQL.Updates.20180305.1464 "#AuroraPostgreSQL.Updates.20180305.1464")
- [Aurora PostgreSQL 14.6.2, March 3, 2023](#AuroraPostgreSQL.Updates.20180305.1462 "#AuroraPostgreSQL.Updates.20180305.1462")
- [Aurora PostgreSQL 14.6.1, February 17, 2023](#AuroraPostgreSQL.Updates.20180305.1461 "#AuroraPostgreSQL.Updates.20180305.1461")
- [Aurora PostgreSQL 14.6.0, January 20, 2023](#AuroraPostgreSQL.Updates.20180305.1460 "#AuroraPostgreSQL.Updates.20180305.1460")

#### Aurora PostgreSQL 14.6.13, June 18, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the improved reader availability functionality that might result in longer recover times and impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause increased latency on data processing.

#### Aurora PostgreSQL 14.6.12, April 29, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 14.6.10, November 18, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.6.9, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.6.8, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.6.7, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.6.6, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 14.6.5, October 04, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")

###### High priority stability enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue which can cause a database instance to restart while executing IO intensive read workloads
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O

####

Aurora PostgreSQL 14.6.4, September 13, 2023

###### General enhancements

- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue in `pg_cron` which can prevent scaling in Aurora Serverless v2
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

####

Aurora PostgreSQL 14.6.2, March 3, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

###### General stability enhancements

- Fixed an issue where the approved plans for joins with partitioned tables weren't being enforced
- Fixed an issue in `PostGIS` where the `GDAL` data wasn't loading
- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out
- Fixed an issue that causes logical replication to fail when using write-through cache

####

Aurora PostgreSQL 14.6.1, February 17, 2023

###### Critical stability enhancements

- Fixed a critical stability issue.

####

Aurora PostgreSQL 14.6.0, January 20, 2023

###### High priority stability enhancements

- Fixed an issue where an upgrade fails because the oldest `MultiXactId` is updated incorrectly
- Fixed an issue that could lead to a brief period of unavailability

###### General stability enhancements

- Fixed an issue that caused DB instance migration failures
- Fixed an issue where the DB fails to start because of an inconsistency in the metadata
- Improved the error handling and diagnosability
- Upgraded the `RDKit` extension to version 4.2
- Upgraded the `GDAL` library to version 3.4.3
- Fixed an issue where the cluster cache management process doesn't shutdown gracefully
- Fixed an issue that can cause certain processes to linger in an inconsistent state during a clean shutdown
- Fixed an issue with the `pg_repack` extension
- Improved the collation library, `glibc`, handling with a new independent default collation library

### PostgreSQL 14.5 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.5. For more
information about the improvements in PostgreSQL 14.5, see [PostgreSQL release 14.5](https://www.postgresql.org/docs/14/release-14-5.html "https://www.postgresql.org/docs/14/release-14-5.html").

###### Releases and patches

- [Aurora PostgreSQL 14.5.8, November 22, 2024](#aurorapostgresql-versions-version145x-1458 "#aurorapostgresql-versions-version145x-1458")
- [Aurora PostgreSQL 14.5.7, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1457 "#AuroraPostgreSQL.Updates.20180305.1457")
- [Aurora PostgreSQL 14.5.6, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1456 "#AuroraPostgreSQL.Updates.20180305.1456")
- [Aurora PostgreSQL 14.5.5, December 18, 2023](#AuroraPostgreSQL.Updates.20180305.1455 "#AuroraPostgreSQL.Updates.20180305.1455")
- [Aurora PostgreSQL 14.5.4, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1454 "#AuroraPostgreSQL.Updates.20180305.1454")
- [Aurora PostgreSQL 14.5.3, October 17, 2023](#AuroraPostgreSQL.Updates.20180305.1453 "#AuroraPostgreSQL.Updates.20180305.1453")
- [Aurora PostgreSQL 14.5.2, March 2, 2023](#AuroraPostgreSQL.Updates.20180305.1452 "#AuroraPostgreSQL.Updates.20180305.1452")
- [Aurora PostgreSQL 14.5.1, December 13, 2022](#AuroraPostgreSQL.Updates.20180305.1451 "#AuroraPostgreSQL.Updates.20180305.1451")
- [Aurora PostgreSQL 14.5.0, November 09, 2022](#AuroraPostgreSQL.Updates.20180305.1450 "#AuroraPostgreSQL.Updates.20180305.1450")

#### Aurora PostgreSQL 14.5.8, November 22, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.

####

Aurora PostgreSQL 14.5.7, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.5.6, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.5.5, December 18, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.5.4, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 14.5.3, October 17, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart
- Improved the scale times for Aurora Serverless v2
- Fix a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads
- Fixed an issue that causes logical replication to fail when using write-through cache

####

Aurora PostgreSQL 14.5.2, March 2, 2023

###### General stability enhancements

- Fixed an issue where the approved plans for joins with partitioned tables weren't being enforced
- Fixed an issue that could cause the unavailability of query plan management (QPM)
- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out
- Fixed an issue with the `pg_cron` parallel running of tasks

####

Aurora PostgreSQL 14.5.1, December 13, 2022

###### General stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance
- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades
- Fixed an issue that could cause unavailability during replication
- Fixed an issue that could cause data inconsistency during replication

####

Aurora PostgreSQL 14.5.0, November 09, 2022

###### High priority stability enhancements

- Fixed an Aurora Serverless v2 scaling issue
- Fixed an issue which caused Aurora Serverless v2 shrink failure

###### General stability enhancements

- Improved buffer cache scavenging when the buffer cache is in duress
- Fixed an issue in database activity streams that leads to high memory consumption
- Fixed an issue where DB instances could restart when applying changes from a logical replication subscription
- Fixed an issue that caused DB instance restarts
- Fixed an issue where a DB instance restarts recursively while generating monitoring metrics during a crash
- Fixed an issue where a DB instance restarted during performance metric collection
- Fixed an issue where an attempt to connect to the database would fail with `SSLV3_ALERT_CERTIFICATE_UNKNOWN`
- Improved the error reporting in case of an inconsistent `B-tree` index
- Improved the diagnostic logging around setting invalid hint bits
- Fixed an issue where autovacuum would incorrectly skip tables
- Improved the logical replication prefetching
- Fixed a durability issue in the `GIN` indexes
- Provided options to configure `MultiXact SLRU` cache. By setting the following parameters (GUCs),
  customers will now be able to change the `MultiXact SLRU` cache sizes:
  - `multixact_members_cache_size`
  - `multixact_offsets_cache_size`

- Fixed an issue to detect and cancel stuck major version upgrades
- Fixed an issue in hash join that could lead to increased memory consumption
- Improved the logical replication performance
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable
- Upgraded the `GEOS` version to 3.10.3
- Updated the `PLV8` version to 3.0.0
- Updated the `PostGIS` extension to version 3.2.3
- Fixed an issue with `st_orientedenvelope` that caused it to loop with a 1-D input to return 0
- Fixed an issue where the connection to SQL Server using `tds_fdw` fails

### PostgreSQL 14.4 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.4. For more
information about the improvements in PostgreSQL 14.4, see [PostgreSQL release 14.4](https://www.postgresql.org/docs/14/release-14-4.html "https://www.postgresql.org/docs/14/release-14-4.html").

###### Releases and patches

- [Aurora PostgreSQL 14.4.11, November 20, 2024](#aurorapostgresql-versions-version144x-14411 "#aurorapostgresql-versions-version144x-14411")
- [Aurora PostgreSQL 14.4.10, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.14410 "#AuroraPostgreSQL.Updates.20180305.14410")
- [Aurora PostgreSQL 14.4.9, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1449 "#AuroraPostgreSQL.Updates.20180305.1449")
- [Aurora PostgreSQL 14.4.8, December 22, 2023](#AuroraPostgreSQL.Updates.20180305.1448 "#AuroraPostgreSQL.Updates.20180305.1448")
- [Aurora PostgreSQL 14.4.7, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1447 "#AuroraPostgreSQL.Updates.20180305.1447")
- [Aurora PostgreSQL 14.4.6, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.1446 "#AuroraPostgreSQL.Updates.20180305.1446")
- [Aurora PostgreSQL 14.4.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.1445 "#AuroraPostgreSQL.Updates.20180305.1445")
- [Aurora PostgreSQL 14.4.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.1444 "#AuroraPostgreSQL.Updates.20180305.1444")
- [Aurora PostgreSQL 14.4.0, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.1440 "#AuroraPostgreSQL.Updates.20180305.1440")

#### Aurora PostgreSQL 14.4.11, November 20, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.4.10, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.4.9, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.4.8, December 22, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.4.7, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 14.4.6, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart
- Improved the scale times for Aurora Serverless v2
- Fix a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

####

Aurora PostgreSQL 14.4.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades
- Fixed an issue that could cause unavailability during replication
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable
- Fixed an issue that could cause data inconsistency during replication

####

Aurora PostgreSQL 14.4.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance

####

Aurora PostgreSQL 14.4.0, October 13, 2022

###### High priority stability enhancements

- Fixed an issue where `PLV8` crashed during a JavaScript error scenario
- Fixed an issue where `PLV8` crashed when trying to acquire a semaphore to execute the next task
- Fixed an issue where scaling an Aurora Serverless v2 instance gets stuck if VACUUM is running

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the `relfilenode`
- Fixed a database restart issue when a plan gets invaliated but the engine still checks if it is valid
- Fixed a stuck scaling issue when the current scaling event times out
- Upgraded the `plv8` extension to version 3.0.0
- Upgraded the `PostGIS` extension to version 3.2.3
- Fixed an issue where extended query messages might be lost during zero-downtime patching (ZDP) causing the extended query to hang after the ZDP completion

### PostgreSQL 14.3 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 14.3. For more
information about the improvements in PostgreSQL 14.3, see [PostgreSQL release 14.3](https://www.postgresql.org/docs/14/release-14-3.html "https://www.postgresql.org/docs/14/release-14-3.html").

###### Releases and patches

- [Aurora PostgreSQL 14.3.11, November 20, 2024](#aurorapostgresql-versions-version143x-14311 "#aurorapostgresql-versions-version143x-14311")
- [Aurora PostgreSQL 14.3.10, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.14310 "#AuroraPostgreSQL.Updates.20180305.14310")
- [Aurora PostgreSQL 14.3.9, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1439 "#AuroraPostgreSQL.Updates.20180305.1439")
- [Aurora PostgreSQL 14.3.8, December 22, 2023](#AuroraPostgreSQL.Updates.20180305.1438 "#AuroraPostgreSQL.Updates.20180305.1438")
- [Aurora PostgreSQL 14.3.7, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1437 "#AuroraPostgreSQL.Updates.20180305.1437")
- [Aurora PostgreSQL 14.3.6, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.1436 "#AuroraPostgreSQL.Updates.20180305.1436")
- [Aurora PostgreSQL 14.3.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.1435 "#AuroraPostgreSQL.Updates.20180305.1435")
- [Aurora PostgreSQL 14.3.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.1434 "#AuroraPostgreSQL.Updates.20180305.1434")
- [Aurora PostgreSQL 14.3.3, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.1433 "#AuroraPostgreSQL.Updates.20180305.1433")
- [Aurora PostgreSQL 14.3.1, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.1431 "#AuroraPostgreSQL.Updates.20180305.1431")
- [Aurora PostgreSQL 14.3.0, June 21, 2022](#AuroraPostgreSQL.Updates.20180305.1430 "#AuroraPostgreSQL.Updates.20180305.1430")

#### Aurora PostgreSQL 14.3.11, November 20, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 14.3.10, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 14.3.9, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 14.3.8, December 22, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 14.3.7, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 14.3.6, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica
- Fixed an issue that would cause high CPU usage and prevent new connections

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart
- Improved the scale times for Aurora Serverless v2
- Fix a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`
  - `aws_lambda.request_timeout_ms`

####

Aurora PostgreSQL 14.3.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades
- Fixed an issue that could cause unavailability during replication
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable
- Fixed an issue that could cause data inconsistency during replication

####

Aurora PostgreSQL 14.3.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance

####

Aurora PostgreSQL 14.3.3, October 13, 2022

###### High priority stability enhancements

- Fixed a `PLV8` issue where the base parameter doesn't get loaded properly into the memory
- Fixed an issue where scaling an Aurora Serverless v2 instance gets stuck if VACUUM is running

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the relfilenode
- Fixed a database restart issue when a plan gets invaliated but the engine still checks if it is valid
- Fixed a stuck scaling issue when the current scaling event times out
- Upgraded the `PostGIS` extension to version 3.1.7
- Fixed an issue where extended query messages might be lost during zero-downtime patching (ZDP) causing the extended query to hang after the ZDP completion

####

Aurora PostgreSQL 14.3.1, July 6, 2022

###### Critical stability enhancements

- Fixed an issue that could cause periods of unavailability during a storage node restart

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability
- Fixed an issue when the connection to SQL Server fails using the `TDS_FDW` extension to query a foreign table
- Fixed an issue that caused connections using the provided root certificate to fail
- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries

####

Aurora PostgreSQL 14.3.0, June 21, 2022

###### New features

- Supports SCRAM password encryption method. For more information,
  see [Using SCRAM for PostgreSQL password encryption](../AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.md#PostgreSQL_Password_Encryption_configuration "../AuroraUserGuide/Appendix.PostgreSQL.CommonDBATasks.md#PostgreSQL_Password_Encryption_configuration").
- Users with the `rds_superuser` role can now create roles for users.

###### Additional improvements and enhancements

- Contains all of the fixes, features, and improvements present in
  [Aurora PostgreSQL 13.7](AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.137X "AuroraPostgreSQL.md#AuroraPostgreSQL.Updates.20180305.137X").
- Backported the following bug fix from the PostgreSQL 14.4 release:
  [Reverted changes to `CONCURRENTLY`
  that "sped up" Xmin advance](https://github.com/postgres/postgres/commit/e28bb885196916b0a3d898ae4f2be0e38108d81b "https://github.com/postgres/postgres/commit/e28bb885196916b0a3d898ae4f2be0e38108d81b") to prevent Index Corruption with the `CREATE INDEX CONCURRENTLY` / `REINDEX CONCURRENTLY` commands.
- This release supports [`lo`](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") extension version 1.1.
- This release supports [`old_snapshot`](https://www.postgresql.org/docs/14/oldsnapshot.html "https://www.postgresql.org/docs/14/oldsnapshot.html") extension version 1.0.
- This release supports EBCDIC collations for the mainframe modernization efforts. For more information,
  see [Aurora PostgreSQL collations for EBCDIC and other mainframe migrations](../AuroraUserGuide/AuroraPostgreSQL.md#AuroraPostgreSQL.Reference.Collations.mainframe.migration "../AuroraUserGuide/AuroraPostgreSQL.md#AuroraPostgreSQL.Reference.Collations.mainframe.migration") in the _Amazon Aurora User Guide_.
- Updated the following extensions:
  - `amcheck` to version 1.3
  - `btree_gist` to version 1.6
  - `cube` to version 1.5
  - `hll` to version 2.16
  - `hstore` to version 1.8
  - `intarray` to version 1.5
  - `log_fdw` to version 1.3
  - `oracle_fdw` to version 2.4.0
  - `pg_hint_plan` to version 1.4
  - `pg_partman` to version 4.6.0
  - `pg_repack` to version 1.4.7
  - `pg_stat_statements` to version 1.9
  - `pg_trgm` to version 1.6
  - `pgaudit` to version 1.6.1
  - `pgrouting` to version 3.2.0
  - `pgtap` to version 1.2.0
  - `postgres_fdw` to version 1.1

## PostgreSQL 13 versions (includes some deprecated versions)

###### Version updates

- [PostgreSQL 13.23](#aurorapostgresql-versions-version1323x "#aurorapostgresql-versions-version1323x")
- [PostgreSQL 13.22](#aurorapostgresql-versions-version1322x "#aurorapostgresql-versions-version1322x")
- [PostgreSQL 13.21](#aurorapostgresql-versions-version1321x "#aurorapostgresql-versions-version1321x")
- [PostgreSQL 13.20](#aurorapostgresql-versions-version1320x "#aurorapostgresql-versions-version1320x")
- [PostgreSQL 13.18](#aurorapostgresql-versions-version1318x "#aurorapostgresql-versions-version1318x")
- [PostgreSQL 13.16](#aurorapostgresql-versions-version1316x "#aurorapostgresql-versions-version1316x")
- [PostgreSQL 13.15](#aurorapostgresql-versions-version1315x "#aurorapostgresql-versions-version1315x")
- [PostgreSQL 13.14](#AuroraPostgreSQL.Updates.20180305.1314X "#AuroraPostgreSQL.Updates.20180305.1314X")
- [PostgreSQL 13.13](#AuroraPostgreSQL.Updates.20180305.1313X "#AuroraPostgreSQL.Updates.20180305.1313X")
- [PostgreSQL 13.12](#AuroraPostgreSQL.Updates.20180305.1312X "#AuroraPostgreSQL.Updates.20180305.1312X")
- [PostgreSQL 13.11](#AuroraPostgreSQL.Updates.20180305.1311X "#AuroraPostgreSQL.Updates.20180305.1311X")
- [PostgreSQL 13.10 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1310X "#AuroraPostgreSQL.Updates.20180305.1310X")
- [PostgreSQL 13.9](#AuroraPostgreSQL.Updates.20180305.139X "#AuroraPostgreSQL.Updates.20180305.139X")
- [PostgreSQL 13.8 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.138X "#AuroraPostgreSQL.Updates.20180305.138X")
- [PostgreSQL 13.7 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.137X "#AuroraPostgreSQL.Updates.20180305.137X")
- [PostgreSQL 13.6 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.136X "#AuroraPostgreSQL.Updates.20180305.136X")
- [PostgreSQL 13.5 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.135X "#AuroraPostgreSQL.Updates.20180305.135X")
- [PostgreSQL 13.4 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.134X "#AuroraPostgreSQL.Updates.20180305.134X")
- [PostgreSQL 13.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.133X "#AuroraPostgreSQL.Updates.20180305.133X")

### PostgreSQL 13.23

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.23. For more information about
the improvements in PostgreSQL 13.23, see [PostgreSQL release
13.23](https://www.postgresql.org/docs/13/release-13-23.html "https://www.postgresql.org/docs/13/release-13-23.html").

###### Releases and patches

- [Aurora PostgreSQL 13.23.1, January 16th, 2026](#aurorapostgresql-versions-version13231x-13231 "#aurorapostgresql-versions-version13231x-13231")
- [Aurora PostgreSQL 13.23, December, 18, 2025](#aurorapostgresql-versions-version1323x-1323 "#aurorapostgresql-versions-version1323x-1323")

#### Aurora PostgreSQL 13.23.1, January 16th, 2026

**Critical stability enhancements**

- Fixed a timing condition in the aws_s3 extension which, in rare cases, can cause database unavailability
- Fixed an issue where an UPDATE statement with OUTPUT clause may skip rows when there are concurrent updates on the same row

#### Aurora PostgreSQL 13.23, December, 18, 2025

**New features**

- Introduced a change which improves static availability of Aurora PostgreSQL writers when, in rare conditions, write operations to storage are delayed due to undergoing storage node maintenance.
- Improvements to minimize switchover downtime during Blue/Green switchover operations, by temporarily blocking transaction commit operations on the Blue environment prior to switchover, reducing drift between the Blue and Green clusters.
- Improved recovery time by optimizing commit log (clog) loading during database cold starts and unplanned restarts, with significant benefits for smaller instances with limited CPU cores.

**Critical stability enhancements**

- Improved cold start performance through faster cache initialization.
- Reduced memory footprint for idle connections in Serverless v2 instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")

- Fixed a database shutdown issue that could cause major version upgrades to fail.
- Fixed a rare major version upgrade failure with large memory allocations.
- Fixed an issue preventing rds_superuser from managing prepared transactions owned by other users.

**General enhancements**

- Updated the following extensions:
  - h3_pg to version 4.2.3.

- Fixed a race condition in Postgres lock release with optimized read enabled.
- Improved PgAudit memory usage during parameter-heavy operations.
- Fixed database initialization failure when max_connections is set to low values.
- Improved Serverless v2 scaling performance under high CPU load.
- Improved Serverless v2 write performance.
- Fixed delays in Serverless v2 scale-down operations.
- Fixed multiple low-risk memory leaks.
- Improved database shutdown during maintenance to enhance availability.
- Improved database startup performance through optimized storage initialization.
- Fixed storage metadata initialization issue that could delay engine startup.
- Fixed region determination failures in aws_s3, aws_ml, and aws_lambda extensions.
- Fixed crash scenario when using pg_buffercache extension during Serverless v2 scaling.

### PostgreSQL 13.22

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.22. For more information about
the improvements in PostgreSQL 13.22, see [PostgreSQL release
13.22](https://www.postgresql.org/docs/13/release-13-22.html "https://www.postgresql.org/docs/13/release-13-22.html").

###### Releases and patches

- [Aurora PostgreSQL 13.22.1, November 25, 2025](#aurorapostgresql-versions-version13221x-13221 "#aurorapostgresql-versions-version13221x-13221")
- [Aurora PostgreSQL 13.22, November 25, 2025](#aurorapostgresql-versions-version1322x-1322 "#aurorapostgresql-versions-version1322x-1322")

#### Aurora PostgreSQL 13.22.1, November 25, 2025

**Critical stability enhancements**

- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/")
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/")

- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 13.22, November 25, 2025

**New features**

- Introduced a new feature to significantly reduce database downtime during restarts by initializing Aurora storage metadata in parallel and reducing contention during initialization.

**Critical stability enhancements**

- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.

**High priority enhancements**

- Back-ported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/")
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/")
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/")

- Fixed an issue in logical replication where subscriber databases could skip replicating transactions after recovering from a crash.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed a security issue when altering routine ownership.

**General enhancements**

- Updated the following extensions:
  - oracle_fdw to version to 2.8.0
  - pg_repack extension to version 1.5.2
  - aws_lamba extension to version 2.0

- Improved file metadata initialization times.
- Fixed an issue that caused reader instance to restart when attempting to create PostgreSQL SLRU files.
- Fixed an issue which caused prolonged Serverless v2 scaling time.
- Fixed an issue that could cause database restart during Serverless v2 scaling.
- Fixed a timing issue in replication diagnostics that could prevent accurate reporting of Aurora replica recovery status when state transitions occur in rapid succession.
- Updated the aws_lambda extension to version 2.0, which resolves a performance issue that was present in version 1.0.
- Added support to include Geodetic TIFF grid files for PROJ.
- Fixed an issue that could cause database restart during aws_s3 export.
- Addressed an issue with logging when replication slots are invalidated.
- Fixed CVE-2023-3079 for V8 Engine in the PLV8 extension.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue where read queries may time out on Aurora replica nodes during the replay of lazy truncation triggered by vacuum on the writer node.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue which prevented online recovery of an Aurora Replica forcing offline recovery.

### PostgreSQL 13.21

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.21. For more information
about the improvements in PostgreSQL 13.21, see [PostgreSQL release
13.21](https://www.postgresql.org/docs/13/release-13-21.html "https://www.postgresql.org/docs/13/release-13-21.html").

###### Releases and patches

- [Aurora PostgreSQL 13.21.4, January 15,
  2026](#aurorapostgresql-versions-version13214x-13214 "#aurorapostgresql-versions-version13214x-13214")
- [Aurora PostgreSQL 13.21.3, September 16,
  2025](#aurorapostgresql-versions-version13213x-13213 "#aurorapostgresql-versions-version13213x-13213")
- [Aurora PostgreSQL 13.21.2, August 8,
  2025](#aurorapostgresql-versions-version13212x-13212 "#aurorapostgresql-versions-version13212x-13212")
- [Aurora PostgreSQL 13.21.1, June 30,
  2025](#aurorapostgresql-versions-version13211x-13211 "#aurorapostgresql-versions-version13211x-13211")
- [Aurora PostgreSQL 13.21, June 30,
  2025](#aurorapostgresql-versions-version1321x-1321 "#aurorapostgresql-versions-version1321x-1321")

#### Aurora PostgreSQL 13.21.4, January 15,

2026

**Critical stability enhancements**

- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

**General enhancements**

- Fixed an issue that could cause delays in scaling down for Serverless V2 instances.
- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 13.21.3, September 16,

2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few
  seconds longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that
  might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when fetching
  pages from storage.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security
  vulnerabilities.
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed an issue that can cause reboots of the primary db instance when reading from a
  logical replication slot in the presence of frequent DDL if
  aurora.enhanced_logical_replication is enabled.
- Fixed a race where old writer may not step down after a new writer is promoted and
  continues to write.

**General enhancements**

- Implemented enhanced error handling mechanisms during TDS Connection reset
  operations.
- Fixed an issue that could in certain cases prevent online recovery of an Aurora Replica
  from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on
  tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately
  after installing the extension or resetting shared memory.
- Fixed an issue with Babelfish ZDP that could lead to instance reboot after
  minor version ugprade in some cases.
- Fixed an issue in enforcing, validating and evolving the `plans` extension
  in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with
  all-column selections.
- Fixed an issue with prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release
  containing The `PostGIS` extension 3.5.1 without running
  postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart
  of an Aurora replica in a Global Database.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 13.21.2, August 8,

2025

**Critical stability enhancements**

- Fixed an issue which could prevent logical replication from resuming after
  upgrade.
- Fixed an issue with Serverless v2 scaling that may cause unavailability when
  performing reads from Aurora Storage.

#### Aurora PostgreSQL 13.21.1, June 30,

2025

**High priority enhancements**

- Fixed a performance issue affecting instance restart operations.

#### Aurora PostgreSQL 13.21, June 30,

2025

**New features**

- Improved Serverless v2 scaling for storage bound workloads.
- Improved Serverless v2 scaling through optimized management of memory maps.

**Critical stability enhancements**

- Fixed an issue where Serverless instances would fail to perform Zero Downtime Patching
  after automatic resume.
- Added library dependency verification during minor and patch upgrades to ensure
  storage metadata recovery is safe before proceeding.

**High priority enhancements**

- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads.
- Fixed an issue where server will fail to start if a previous startup was prematurely
  terminated.

**General enhancements**

- Updated the following extensions:
  - apg_plan_mgmt to 2.9.
  - The `pgaudit` extension to 1.5.3.
  - The `rdkit` extension to 4.6.1 (2024_09_6).
  - The `pg_repack` extension to 1.5.1.
  - The `pglogical` extension to 2.4.5.

- Improvements to make Serverless v2 scaling more efficient on reader nodes.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  sub-transactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue that prevents Zero Downtime Patching from completing successfully on
  Serverless v2 auto-pause enabled instances.
- Fixed an issue in pgdam that causes the engine (with pgdam enabled) to crash when
  hitting maximum connections.
- Fixed an issue in the `pg_bigm` extension that can cause unavailability
  when the extension interacts with the GIN index.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
- Added function aurora_stat_resource_usage() to report current CPU usage, allocated and
  used memory for all the backends.
- Fixed an issue which prevented Zero Downtime Patching when cache recovery is
  disabled.
- Fixed a synchronization issue where Zero Downtime Patching could fail due to premature
  engine ready state reporting.
- Fixed an issue in checkpoint replication to have storage metadata position be
  consistent in reader.
- Fixed an issue which causes RO node to restart while its reconnecting to RW
  node.
- Fixed an issue where RO client process can be stuck in LWLock:BufferIO wait event
  after being disconnected from the writer.
- Fixed an issue where RO node could crash when frequently falling behind RW
  node.
- Fixed an issue in the aws_s3 extension that could cause an import operation to restart
  and reinsert previously inserted rows.

### PostgreSQL 13.20

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.20. For more information
about the improvements in PostgreSQL 13.20, see [PostgreSQL release
13.20](https://www.postgresql.org/docs/13/release-13-20.html "https://www.postgresql.org/docs/13/release-13-20.html").

###### Releases and patches

- [Aurora PostgreSQL 13.20.5, February 03, 2026](#aurorapostgresql-versions-version1417x-1417 "#aurorapostgresql-versions-version1417x-1417")
- [Aurora PostgreSQL 13.20.4, October 9, 2025](#aurorapostgresql-versions-version13204x-13204 "#aurorapostgresql-versions-version13204x-13204")
- [Aurora PostgreSQL 13.20.3, June 03, 2025](#aurorapostgresql-versions-version13203x-13203 "#aurorapostgresql-versions-version13203x-13203")
- [Aurora PostgreSQL 13.20.2, May 01,
  2025](#aurorapostgresql-versions-version13202x-13202 "#aurorapostgresql-versions-version13202x-13202")
- [Aurora PostgreSQL 13.20, April 07,
  2025](#aurorapostgresql-versions-version1320x-1320 "#aurorapostgresql-versions-version1320x-1320")

#### Aurora PostgreSQL 13.20.5, February 03, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed a database shutdown issue which could cause major version upgrade to fail.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://nvd.nist.gov/vuln/detail/CVE-2025-12817 "https://nvd.nist.gov/vuln/detail/CVE-2025-12817").
  - [CVE-2025-12818](https://nvd.nist.gov/vuln/detail/CVE-2025-12818 "https://nvd.nist.gov/vuln/detail/CVE-2025-12818").

- Fixed an issue which could cause a restart during the start of logical replication data synchronization.
- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.
- Fixes crashes and/or intermittent errors when a procedure variable is assigned to itself.
- Fixed an issue with the cleanup of files created by NOTIFY channels, which could lead to high local storage usage.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 13.20.4, October 9, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can
  incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds
  longer because the runtime process wasn't exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might
  result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension’s V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer
  instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is
  enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables
  larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after
  installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving the `plans` extension in Query Plan Management.
- Fixed an issue during numeric calculations involving aggregate functions with all-column
  selections.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing
  The `PostGIS` extension 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an
  Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution the `plans` extension using the “bitmap
  heap scan” access method.
- Fixed an issue impacting query execution performance for execution the `plans` extension using the
  “bitmap heap scan” access method.
- Fixed and issue where storage client may crash during instance restart.

#### Aurora PostgreSQL 13.20.3, June 03, 2025

**Critical stability enhancements**

- Fixed stuck scaling for serverless db instances with zero-ETL enabled.
- Fixed an issue which can cause the database to become unresponsive when performing actions
  with Aurora Storage.
- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.
- Fixed an issue in handling parameter lists from previous versions of Query Plan Management.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Fixed an issue that can cause RO instance crash under heavy workload.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.

#### Aurora PostgreSQL 13.20.2, May 01,

2025

**Critical priority enhancements**

- Fixed an issue which can cause the database to become unresponsive when performing
  actions with Aurora storage.

#### Aurora PostgreSQL 13.20, April 07,

2025

**High priority enhancements**

- Fixed an issue where Aurora in-Region failovers would result in failures in database
  startup.
- Fixed a security issue in the `rds_activity_stream` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Aurora storage metadata now initializes more quickly during unplanned failovers and
  server restarts, reducing overall downtime. Larger instances benefit the most by
  leveraging higher parallelism.
- Improved performance of file metadata operations.
- Made improvements to database downtime during a `planned` extension
  switchover for Global Databases.
- In Blue/Green deployments, creating or modifying temporary objects is no longer
  classified as restricted DDL.
  - Creating temporary objects with syntax such as CREATE TEMPORARY TABLE x AS SELECT \* FROM isn't supported.
  - Creating indexes on temporary tables isn't supported.

- The Blue/Green deployment switchover won’t be blocked by the `REFRESH
MATERIALIZED VIEW` statement.
- Improved allocation of Write-Ahead Log (WAL) stream numbers, resulting in increased
  throughput for write-heavy workloads on the new Graviton 4 high-end instances.
- Fixed an issue where reader upgrade was taking longer than expected.
- Updated the following extensions:
  - Update the `pgvector` extension to 0.8.0.
  - Update the `pg_cron` extension to v1.6.5.
  - Update the `tds_fdw` extension to 2.0.4.
  - Update the `postgis` extension to 3.5.1.
  - Update the `pg_partman` extension to v5.2.4.
  - Update the `orafce` extension to 4.14.0.
  - Update the `rds_tools` extension to 1.9.
  - Update the `rdkit` extension to Release_2024_09_3.

### PostgreSQL 13.18

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.18. For more information
about the improvements in PostgreSQL 13.18, see [PostgreSQL release
13.18](https://www.postgresql.org/docs/13/release-13-18.html "https://www.postgresql.org/docs/13/release-13-18.html").

###### Releases and patches

- [Aurora PostgreSQL 13.18.7, January 28, 2026](#aurorapostgresql-versions-version13187x-13187 "#aurorapostgresql-versions-version13187x-13187")
- [Aurora PostgreSQL 13.18.6, November 13, 2025](#aurorapostgresql-versions-version13186x-13186 "#aurorapostgresql-versions-version13186x-13186")
- [Aurora PostgreSQL 13.18.5, June 24, 2025](#aurorapostgresql-versions-version13185x-13185 "#aurorapostgresql-versions-version13185x-13185")
- [Aurora PostgreSQL 13.18.4, March
  24, 2025](#aurorapostgresql-versions-version13184x-13184 "#aurorapostgresql-versions-version13184x-13184")
- [Aurora PostgreSQL 13.18.3,
  February 13, 2025](#aurorapostgresql-versions-version13183x-13183 "#aurorapostgresql-versions-version13183x-13183")
- [Aurora PostgreSQL 13.18.2, January
  20, 2025](#aurorapostgresql-versions-version13182x-13182 "#aurorapostgresql-versions-version13182x-13182")
- [Aurora PostgreSQL 13.18.1,
  December 27, 2024](#aurorapostgresql-versions-version13181x-13181 "#aurorapostgresql-versions-version13181x-13181")
- [Aurora PostgreSQL 13.18, December
  27, 2024](#aurorapostgresql-versions-version1318x-1318 "#aurorapostgresql-versions-version1318x-1318")

#### Aurora PostgreSQL 13.18.7, January 28, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 13.18.6, November 13, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 13.18.5, June 24, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.18.4, March

24, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 13.18.3,

February 13, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 13.18.2, January

20, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream`
  extension.

**High priority enhancements**

- Fixed an issue in Global DB switchover and failover that could result in
  customers needing to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in
  some cases.

**General enhancements**

- Fixed an ownership issue where the `postgis_raster` extension could
  not be updated correctly from a previous the PostGIS extension v2
  installation.

#### Aurora PostgreSQL 13.18.1,

December 27, 2024

**Critical Priority enhancements**

- Fixed an issue where the server was restarting when the connections were reset
  by the peer.

#### Aurora PostgreSQL 13.18, December

27, 2024

###### New features for 13.18

- Optimized the minor version and patch upgrade process to reduce downtime for
  read replicas.

###### Critical stability enhancements for 13.18

- Fixed an issue that in rare cases can cause CPU usage spike.

###### High priority enhancements for 13.18

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")

###### General enhancements for 13.18

- Made multiple improvements to Aurora in-Region failover which reduces database
  downtime further by improving storage metadata and faster buffer cache
  initialization.
- Made multiple improvements to upgrades with Zero-Downtime Patching (ZDP) which
  reduces connection restore time and enhances ZDP resilience from
  failures.
- Fixed an issue where the server_id value wasn’t updated after an Amazon RDS
  Blue/Green Deployment switchover.
- Fixed an issue that could cause database restart during hash index
  extension.
- Fixed an issue that would cause migration from RDS PostgreSQL to fail in the
  presence of nested tablespaces.
- Fixed an issue that would cause excessive engine startup times in the presence
  of a large number of logical replication files.
- Fixed an issue that could cause a database restart when calling functions from `aws_s3`,
  `aws_lambda`, and `aws_ml` extensions in the same database session as `aws_s3.table_import_from_s3()`.
  This fix may decrease the per-call performance of functions from the `aws_s3`, `aws_lambda`, and `aws_ml` extensions.
- Fixed an issue that could cause database restart during serverless
  scaling.
- Fixed an issue that prevented updating the `pgTAP` extension to
  version 1.3.0 or later.
- Fixed an issue in the `PostGIS` extension, which in rare cases,
  could cause a DB instance restart.
- Fixed an issue in the `pg_repack` extension that compromises the
  integrity of invalid indexes.

###### Additional improvements and enhancements for 13.18

- Updated the following extensions:
  - `pg_cron` extension to v1.6.4.
  - `PostGIS` extension to version 3.4.3.
  - `PROJ` library extension to version 9.5.0.
  - `GEOS` library extension to verison 3.13.0.
  - `orafce` extension to 4.12.0.
  - `pgvector` extension to 0.7.4.
  - `RDKit` extension to 2024_03_6 release (4.6).
  - `pg_hint_plan` extension to version 1.3.10.

### PostgreSQL 13.16

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.16. For more
information about the improvements in PostgreSQL 13.16, see [PostgreSQL release 13.16](https://www.postgresql.org/docs/13/release-13-16.html "https://www.postgresql.org/docs/13/release-13-16.html").

###### Releases and patches

- [Aurora PostgreSQL 13.16.7, February 13, 2026](#aurorapostgresql-versions-version13166x-13166 "#aurorapostgresql-versions-version13166x-13166")
- [Aurora PostgreSQL 13.16.6, November 21, 2025](#aurorapostgresql-versions-version13166x-13166 "#aurorapostgresql-versions-version13166x-13166")
- [Aurora PostgreSQL 13.16.5, July 11, 2025](#aurorapostgresql-versions-version13165x-13165 "#aurorapostgresql-versions-version13165x-13165")
- [Aurora PostgreSQL 13.16.4, April 17, 2025](#aurorapostgresql-versions-version13164x-13164 "#aurorapostgresql-versions-version13164x-13164")
- [Aurora PostgreSQL 13.16.2, January 29, 2025](#aurorapostgresql-versions-version13162x-13162 "#aurorapostgresql-versions-version13162x-13162")
- [Aurora PostgreSQL 13.16.1, January 02, 2025](#aurorapostgresql-versions-version13161x-13161 "#aurorapostgresql-versions-version13161x-13161")
- [Aurora PostgreSQL 13.16, September 30, 2024](#aurorapostgresql-versions-version1316x-1316 "#aurorapostgresql-versions-version1316x-1316")

#### Aurora PostgreSQL 13.16.7, February 13, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

#### Aurora PostgreSQL 13.16.6, November 21, 2025

**Critical stability enhancements**

- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 13.16.5, July 11, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.16.4, April 17, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues.
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 13.16.2, January 29, 2025

**Critical stability enhancements**.

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**.

- Fixed an issue in Global DB switchover and failover that could result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.

**General enhancements**.

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 13.16.1, January 02, 2025

**Critical stability enhancements**

- Fixed an issue related to Query Plan Management background worker.
- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed issue where Aurora in-Region failovers would result in failures in database startup.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue that prevented the scaling of Aurora Serverless v2 Read Replicas when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in longer
  upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime further
  with faster buffer cache initialization.
- Fixed an issue where reserved keyword “PRIMARY” caused syntax errors when
  used as a column name or alias in DML and DDL statements.
- Fixed an issue that could cause an error in the wal sender process when resuming logical
  replication.

#### Aurora PostgreSQL 13.16, September 30, 2024

**New features**

- Introduced a new fast failover feature to reduce database downtime during the `planned` extension failover
  events with fast storage metadata initialization and fast buffer cache recovery.
- Introduced an optimization to reduce Zero Downtime Patching (ZDP) quiet point duration to 1 second.

**High priority enhancements**

- Fixed issues where the replication of vacuum operations may cause a restart when handling
  conflicts with user queries.
- Fixed an issue where deleting a large range of keys from a BTree index could cause
  concurrent scans to crash.

**General enhancements**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation. For more
  information, see [AWS-LC is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/")
  on AWS Security Blog.
- Improvements to database startup time during initialization and engine
  upgrades.
- Fixed an issue that prevented the inclusion of the `pg_bigm` extension in
  shared_preload_libraries.
- Fixed an issue during Zero Downtime Patching which causes some connections to be terminated
  due to long transferring time. A new ZDP metric in postgresql.log called
  `ZD_SOCKET_TRANSFER_CONN_DROPPED` represents these dropped connections.
- Improved reader availability for Aurora Replicas when using system administration functions.
- Fixed an in-memory two-phase commit (2PC) metadata caching issue that caused out-of-memory
  error on Aurora read replicas replicating from RDS PostgreSQL source instances.
- Fixed an issue in storage metadata initialization that can cause prolonged database startup
  time.
- Fixed an issue that will prevent reclaiming Aurora storage space during major version
  upgrade.

**Additional improvements and enhancements**

- Updated the following extensions:
  - `pgvector` extension to version 0.7.3.
  - `mysql_fdw` extension to version REL-2_9_2.
  - `orafce` extension to version 4.10.3.
  - `pgTAP` extension to version 1.3.3.
  - `pg_cron` extension to version 1.6.3.
  - `RDKit` extension to version 4.5 (Release 2024_03_5).
  - `wal2json` extension to version 2.6.
  - `HypoPG` extension to version 1.4.1.

### PostgreSQL 13.15

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.15. For more information
about the improvements in PostgreSQL 13.15, see [PostgreSQL release
13.15](https://www.postgresql.org/docs/13/release-13-15.html "https://www.postgresql.org/docs/13/release-13-15.html").

###### Releases and patches

- [Aurora PostgreSQL 13.15.5, July 17, 2025](#aurorapostgresql-versions-version13155x-13155 "#aurorapostgresql-versions-version13155x-13155")
- [Aurora PostgreSQL 13.15.4, March
  25, 2025](#aurorapostgresql-versions-version13154x-13154 "#aurorapostgresql-versions-version13154x-13154")
- [Aurora PostgreSQL 13.15.3, January
  29, 2025](#aurorapostgresql-versions-version13153x-13153 "#aurorapostgresql-versions-version13153x-13153")
- [Aurora PostgreSQL 13.15.2, January
  23, 2025](#aurorapostgresql-versions-version13152x-13152 "#aurorapostgresql-versions-version13152x-13152")
- [Aurora PostgreSQL 13.15.1,
  September 27, 2024](#aurorapostgresql-versions-version1315x-13151 "#aurorapostgresql-versions-version1315x-13151")
- [Aurora PostgreSQL 13.15,
  August 8, 2024](#aurorapostgresql-versions-version1315x-1315 "#aurorapostgresql-versions-version1315x-1315")

#### Aurora PostgreSQL 13.15.5, July 17, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.15.4, March

25, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 13.15.3, January

29, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 13.15.2, January

23, 2025

###### Critical stability enhancements

- Fixed an issue related to Query Plan Management background worker.

###### High priority enhancements

- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in
  longer upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime
  further with faster buffer cache initialization.
- Fixed an issue that could cause an error in the wal sender process when
  resuming logical replication.

#### Aurora PostgreSQL 13.15.1,

September 27, 2024

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

#### Aurora PostgreSQL 13.15,

August 8, 2024

###### New features

- Aurora Serverless v2 now applies pending database parameter
  `max_connections` changes during upgrades. The Serverless V2
  capacity changes result in pending `max_connections` changes. As many
  ZDP supported connections as allowed by `max_connections` will be
  preserved during upgrades.
- Introduced a feature to improve database start up time through faster buffer
  cache initialization during restarts and database upgrades.
- Minor version and patch upgrades may now complete faster in some cases.
- Reduced Aurora Serverless v2 scale up and scale down time in the presence of
  data intensive workloads or long running queries and busy or unrespoive
  connections.

###### Critical stability enhancements

- Fixed a pg_repack issue that would incorrectly allow two vacuum processes to
  operate concurrently on the same table.

###### High priority enhancements

- Fixed an issue which leads to cancellation of long-running queries on Global
  Database replica instances.

###### General enhancements

- Improved Aurora PostgreSQL performance for generative AI workloads using
  `pgvector`.
- Fixed issue where minor version upgrades with ZDP would fail in some cases
  resulting in longer upgrade times.
- Improved replay performance of vacuum operations on Aurora Replica
  instances.
- Fixed a bug where JDBC connections may not be preserved during ZDP enabled
  upgrades.
- Improvement to reduce postgres private memory fragmentation.
- Fixed an issue that caused two-phase commit files to remain, preventing proper
  cleanup.
- Improved memory handling while processing two phase commit files.
- Fixed an issue resulting in degraded performance during query planning on
  Aurora replicas.
- Improved availability of Aurora read replicas.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` extension to version 4.9.4.
  - `pg_cron` extension to version 1.6.2.
  - `pg_partman` extension to version 5.1.0.
  - `pg_repack` extension to version 1.5.0.
  - `pg_tle` to version 1.4.0.
  - `pg_vector` extension to version 0.7.0.
  - `pgrouting` extension to version 3.6.2.
  - `pgTap` extension to version 1.3.2.
  - `PostGIS` extension to version 3.4.2.
  - `RDKit` extension to version 2024_03_1.

### PostgreSQL 13.14

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.14. For more
information about the improvements in PostgreSQL 13.14, see [PostgreSQL release 13.14](https://www.postgresql.org/docs/13/release-13-14.html "https://www.postgresql.org/docs/13/release-13-14.html").

###### Releases and patches

- [Aurora PostgreSQL 13.14.6, July 28, 2025](#aurorapostgresql-versions-version13146x-13146 "#aurorapostgresql-versions-version13146x-13146")
- [Aurora PostgreSQL 13.14.5, April 16, 2025](#aurorapostgresql-versions-version13145x-13145 "#aurorapostgresql-versions-version13145x-13145")
- [Aurora PostgreSQL 13.14.4, February 02, 2025](#aurorapostgresql-versions-version13144x-13144 "#aurorapostgresql-versions-version13144x-13144")
- [Aurora PostgreSQL 13.14.3, October 7, 2024](#aurorapostgresql-versions-version1314x-13143 "#aurorapostgresql-versions-version1314x-13143")
- [Aurora PostgreSQL 13.14.2, June 20, 2024](#AuroraPostgreSQL.Updates.20180305.13142 "#AuroraPostgreSQL.Updates.20180305.13142")
- [Aurora PostgreSQL 13.14.1, April 29, 2024](#AuroraPostgreSQL.Updates.20180305.13141 "#AuroraPostgreSQL.Updates.20180305.13141")

#### Aurora PostgreSQL 13.14.6, July 28, 2025

**Critical stability enhancements**.

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**.

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the `aws_s3` extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.14.5, April 16, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 13.14.4, February 02, 2025

**Critical stability enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418")
  for V8 Engine in the `PLV8` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

- **General enhancements**

Fixed an ownership issue where the postgis_raster extension could not be updated correctly
from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 13.14.3, October 7, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache instances while upgrading into this version.

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.14.2, June 20, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed an issue with background worker where it may crash when executed in parallel worker context.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed issues in how two-phase commit files are handled.

####

Aurora PostgreSQL 13.14.1, April 29, 2024

###### New features

- Added resource usage summary to `pg_dump`.

###### General enhancements

- Fixed multiple minor version upgrade issues to improve connection preservation with zero-downtime patching.
- Reduced database boot time due to improved initialization time for large volumes.
- Introduced faster COPY operations by reducing contention on the relation extension lock and proactively extending relations.
- Improvements to reduce replication lag by intelligently skipping the replay of certain log records, thereby reducing the replay load.
- Fixed an issue during recovery conflict on a read node which, in rare cases, could cause brief unavailability.
- Fixed an issue where a database would fail to startup during a major version upgrade patch, in rare scenarios.
- Improved availability of read replicas by allowing recovery from replication errors in more situations.
- Fixed an issue that would cause zero-downtime patching to timeout.
- Fixed a logical replication decoding issue that fails to process catalog modifying changes after spilling to storage
  if there was a concurrent aborted sub-transaction.
- Improved log record validation before it is written to storage.
- Fixed an issue that would result in sessions incorrectly reporting ClientRead wait events after a zero-downtime patching event.
- Fixed an ambiguous function definition of aws_s3.query_export_to_s3 when upgrading the aws_s3 extension from version 1.1 to 1.2.

###### High priority enhancements

- Fixed an issue related to resuming a logical replication slot where, in rare cases, it could cause the slot to become stuck.
- Fixed an issue that would result in a restart when creating a database in a tablespace.
- Fixed an issue related to incorrect logical replication error handling to improve DB stability.

###### Critical stability enhancements

- Fixed an issue related to replication origins that in rare cases might result in longer recovery time and impact availability.
- Fixed an issue that in rare cases may cause transactions to be partially replicated by newly created logical replication slots. For more information, see
  [Potential data loss due to race condition during logical replication slot creation](https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com "https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com").
- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_tle` extension to version 1.3.4.
  - `PLV8` extension to version 3.1.10.
  - RDKit Cartridge to version Release_2023_09_4.

- New GUC Parameters has been added
  - `pgtle.clientauth_databases_to_skip`
  - `pgtle.clientauth_db_name`
  - `pgtle.clientauth_num_parallel_workers`
  - `pgtle.clientauth_users_to_skip`
  - `pgtle.enable_clientauth`
  - `pgtle.passcheck_db_name`

### PostgreSQL 13.13

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.13. For more
information about the improvements in PostgreSQL 13.13, see [PostgreSQL release 13.13](https://www.postgresql.org/docs/13/release-13-13.html "https://www.postgresql.org/docs/13/release-13-13.html").

###### Releases and patches

- [Aurora PostgreSQL 13.13.8, July 30, 2025](#aurorapostgresql-versions-version13138x-13138 "#aurorapostgresql-versions-version13138x-13138")
- [Aurora PostgreSQL 13.13.7 April 22, 2025](#aurorapostgresql-versions-version13137x-13137 "#aurorapostgresql-versions-version13137x-13137")
- [Aurora PostgreSQL 13.13.6, February 5, 2025](#aurorapostgresql-versions-version13136x-13136 "#aurorapostgresql-versions-version13136x-13136")
- [Aurora PostgreSQL 13.13.5, September 17, 2024](#aurorapostgresql-versions-version1313x-13135 "#aurorapostgresql-versions-version1313x-13135")
- [Aurora PostgreSQL 13.13.4, June 24, 2024](#AuroraPostgreSQL.Updates.20180305.13134 "#AuroraPostgreSQL.Updates.20180305.13134")
- [Aurora PostgreSQL 13.13.3, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.13133 "#AuroraPostgreSQL.Updates.20180305.13133")
- [Aurora PostgreSQL 13.13.2, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.13132 "#AuroraPostgreSQL.Updates.20180305.13132")
- [Aurora PostgreSQL 13.13.0, December 21, 2023](#AuroraPostgreSQL.Updates.20180305.13130 "#AuroraPostgreSQL.Updates.20180305.13130")

#### Aurora PostgreSQL 13.13.8, July 30, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue in the read replica deletion which could result in a vaccum being held back
  and causing eventual unavailability of database.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.13.7 April 22, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 13.13.6, February 5, 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 13.13.5, September 17, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.13.4, June 24, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

####

Aurora PostgreSQL 13.13.3, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

####

Aurora PostgreSQL 13.13.2, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.13.0, December 21, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition to support
PostgreSQL versions 15.5, 14.10, 13.13, and 12.17. These releases contain product improvements and bug fixes made by the PostgreSQL community,
along with Aurora-specific improvements. New features and improvements for Babelfish for Aurora PostgreSQL version 3.4 are also included.

Refer to the Aurora version policy to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder,
if you are running any version of Amazon Aurora PostgreSQL version 11, you must upgrade to a newer major version by February 29, 2024.

###### New features

- Amazon Bedrock integration – By using the Amazon Aurora machine learning extension with your Aurora PostgreSQLDB cluster, you can now use Amazon Bedrock
  foundational AI models.
- Delegated Extension Support – This feature allows delegating extension management to lower privileged user with the new rds_extension role.
- Query Plan Management (QPM) enhancements:
  - Plan outlines will be updated to the latest format version as part of the `update_plan_hash`
    action for `apg_plan_mgmt.validate_plans()`.
  - Support was added for parallel append enforcement as a part of parallel query enforcement.

- Added support for the `HypoPG` extension at version 1.4.0.
- Added support for the `h3-pg` extension and the `h3-postgis` extension at version 4.1.3.

###### High priority enhancements

- Fixed an issue which may cause an Aurora replica to reboot when reading a page which was modified during `WAL` replay
- Fixed an issue where if a specific volume metadata is invalid on a source cluster, it will remain invalid on a cloned cluster. Since the
  clone cluster uses a new volume, the metadata will now be recreated.
- Fixed an issue which could, in rare cases, lead to an engine unavailable condition following a minor or patch version upgrade
- Fixed a bug that may cause an engine crash during zero-downtime patching (ZDP)
- Introduced a new parameter, `rds.enable_memory_management`, which is used to enable and disable the improved memory management feature.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General enhancements

- Fixed an issue which may cause an Aurora replica to reboot while reconnecting with the writer DB instance.
- Added support for the `rdkit.morgan_fp_size` parameter
- `rds-superuser` can now run the `pg_stat_reset_slru` function
- Fixed an issue where MultiXact SLRU accesses were not credited to the correct `pg_stat_slru` category.
- Fixed an issue which may cause unused `WAL` segements to not be properly removed
- Fixed an issue where `pglogical` does not correctly pass-through replication origin data when using the binary output format
- `rds_superuser` can now execute `ALTER COLLATION` to refresh the collation version of a locale in the catalog.
- Fixed a crash in `dblink` and `postgres_fdw` extensions due to invalid connections
- Fixed an issue where the `aws_s3` extension can import `HTTP` error responses into the table
- Record the version of the AWS independent default collation library version in pg_collation catalog.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `mysql_fdw` to version 2.9.1
  - `Oracle_fdw` to version 2.6.0
  - `Orafce` to version 4.6.0
  - `pg_cron` to version 1.6.0
  - `pg_hint_plan` to version 1.3.9
  - `pg_proctab` to version 0.0.10
  - `plv8` to version 3.1.8
  - `PostGIS` to version 3.4.0
  - `prefix` to version 1.2.10
  - `RDKit` to version 4.4.0 (Release_2023_09_1)

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
13](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13").

### PostgreSQL 13.12

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.12. For more information
about the improvements in PostgreSQL 13.12, see [PostgreSQL release
13.12](https://www.postgresql.org/docs/13/release-13-12.html "https://www.postgresql.org/docs/13/release-13-12.html").

###### Releases and patches

- [Aurora PostgreSQL 13.12.11, August 5, 2025](#aurorapostgresql-versions-version131211x-131211 "#aurorapostgresql-versions-version131211x-131211")
- [Aurora PostgreSQL 13.12.10, May
  7, 2025](#aurorapostgresql-versions-version131210x-131210 "#aurorapostgresql-versions-version131210x-131210")
- [Aurora PostgreSQL 13.12.9,
  February 27 2025](#aurorapostgresql-versions-version13129x-13129 "#aurorapostgresql-versions-version13129x-13129")
- [Aurora PostgreSQL 13.12.8,
  November 14, 2024](#aurorapostgresql-versions-version1312x-13128 "#aurorapostgresql-versions-version1312x-13128")
- [Aurora PostgreSQL 13.12.7, June
  25, 2024](#AuroraPostgreSQL.Updates.20180305.13127 "#AuroraPostgreSQL.Updates.20180305.13127")
- [Aurora PostgreSQL 13.12.6, March
  13, 2024](#AuroraPostgreSQL.Updates.20180305.13126 "#AuroraPostgreSQL.Updates.20180305.13126")
- [Aurora PostgreSQL 13.12.5,
  February 22, 2024](#AuroraPostgreSQL.Updates.20180305.13125 "#AuroraPostgreSQL.Updates.20180305.13125")
- [Aurora PostgreSQL 13.12.2,
  December 13, 2023](#AuroraPostgreSQL.Updates.20180305.13122 "#AuroraPostgreSQL.Updates.20180305.13122")
- [Aurora PostgreSQL 13.12.1,
  November 09, 2023](#AuroraPostgreSQL.Updates.20180305.13121 "#AuroraPostgreSQL.Updates.20180305.13121")
- [Aurora PostgreSQL 13.12.0, October
  24, 2023](#AuroraPostgreSQL.Updates.20180305.1312 "#AuroraPostgreSQL.Updates.20180305.1312")

#### Aurora PostgreSQL 13.12.11, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.12.10, May

7, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 13.12.9,

February 27 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream`
  extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue in Global DB switchover and failover that can result in
  customers needing to rebuild their mirror clusters.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 13.12.8,

November 14, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when
  `rds.enable_plan_management` is turned on, but apg_plan_mgmt
  extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 13.12.7, June

25, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue which led to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version
  upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same
  table.

#### Aurora PostgreSQL 13.12.6, March

13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

#### Aurora PostgreSQL 13.12.5,

February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version
  upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes
  due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer
  failover.
- Fixed an issue where active transactions during logical replication slot
  creation may be partially replicated by the slot.

#### Aurora PostgreSQL 13.12.2,

December 13, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone
  other than the table owner

#### Aurora PostgreSQL 13.12.1,

November 09, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker
  processes

###### General enhancements

- Fixed an issue related to buffer pin locking that in rare cases can result in
  a crash

#### Aurora PostgreSQL 13.12.0, October

24, 2023

###### New features

- Added support for `mysql_fdw` version 2.9.0
- Added support in the `aws_s3` extension for exporting to an S3
  bucket encrypted with a customer managed KMS key
- Improved the availability of Aurora replicas in the global DB secondary
  clusters
- Added support for query plan capture on Aurora replicas
- Added support for query plan enforcement with parallel query operators
- Allowed query plans under a given cost threshold to not be captured

###### High priority enhancements

- Included optimizations to improve the time to scale up in Aurora Serverless
  instances

###### General enhancements

- Fixed an issue in the `aws_s3` extension where the number of rows
  exported is incorrectly reported when the total number exceeds 2 billion
- Provided options to configure timeouts in the `aws_s3` extension.
  By setting the following parameters (GUCs), customers will now be able to change
  the timeout thresholds for imports from S3:
  - `aws_s3.curlopt_low_speed_limit`
  - `aws_s3.curlopt_low_speed_time`

- Prevented instance creation failure in some edge cases
- Improved the performance of replay of commit transaction operations on Aurora
  replicas
- Fixed an issue where, in rare cases, an import from the `aws_s3`
  extension fails to complete
- Updated the GEOS library for PostGIS to version 3.12.0
- Improved Aurora Serverless v2 database memory scaling which reduces the overall
  database instance scale time
- Added the `WAIT_EVENT_Aurora_CLUSTER_CACHE_MANAGER_SENDER` wait
  event to denote wait times in the cluster cache manager sender
- Added the `WAIT_EVENT_Aurora_SERVERLESS_MONITORING_MAIN` wait event
  to denote wait times in Aurora Serverless resource monitoring
- Fixed an issue where the database may crash during the start of a logical
  replication slot
- Increased the limit for `pg_cron`
  `cron.max_running_jobs` parameter from 100 to 1000
- Fixed a bug in `CREATE TABLE` command to handle table name starting
  with '#' correctly.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` to version 4.3.0
  - `pg_logical` to version 2.4.3
  - `pgvector` to version 0.5.0
  - `PostGIS` to version 3.3.3
  - `RDKit` to version 4.3

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
13](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13").

### PostgreSQL 13.11

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.11. For more
information about the improvements in PostgreSQL 13.11, see [PostgreSQL release 13.11](https://www.postgresql.org/docs/15/release-13-11.html "https://www.postgresql.org/docs/15/release-13-11.html").

###### Releases and patches

- [Aurora PostgreSQL 13.11.10, August 5, 2025](#aurorapostgresql-versions-version131110x-131110 "#aurorapostgresql-versions-version131110x-131110")
- [Aurora PostgreSQL 13.11.9 April 30, 2025](#aurorapostgresql-versions-version13119x-13119 "#aurorapostgresql-versions-version13119x-13119")
- [Aurora PostgreSQL 13.11.8, February 24 2025](#aurorapostgresql-versions-version13118x-13118 "#aurorapostgresql-versions-version13118x-13118")
- [Aurora PostgreSQL 13.11.7, November 12, 2024](#aurorapostgresql-versions-version1311x-13117 "#aurorapostgresql-versions-version1311x-13117")
- [Aurora PostgreSQL 13.11.6, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.13116 "#AuroraPostgreSQL.Updates.20180305.13116")
- [Aurora PostgreSQL 13.11.5, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.13115 "#AuroraPostgreSQL.Updates.20180305.13115")
- [Aurora PostgreSQL 13.11.4, December 14, 2023](#AuroraPostgreSQL.Updates.20180305.13114 "#AuroraPostgreSQL.Updates.20180305.13114")
- [Aurora PostgreSQL 13.11.3, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.13113 "#AuroraPostgreSQL.Updates.20180305.13113")
- [Aurora PostgreSQL 13.11.2, October 4, 2023](#AuroraPostgreSQL.Updates.20180305.13112 "#AuroraPostgreSQL.Updates.20180305.13112")
- [Aurora PostgreSQL 13.11.0, July 13, 2023](#AuroraPostgreSQL.Updates.20180305.13110 "#AuroraPostgreSQL.Updates.20180305.13110")

#### Aurora PostgreSQL 13.11.10, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 13.11.9 April 30, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

  **General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly re-establish
  connection with the writer.

#### Aurora PostgreSQL 13.11.8, February 24 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 13.11.7, November 12, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.11.6, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 13.11.5, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.11.4, December 14, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 13.11.3, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 13.11.2, October 4, 2023

###### High priority stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica.
- Fixed an issue that would cause a crash when executing the `COPY FROM` command.
- Fixed an issue that would cause high CPU usage and prevent new connections.
- Fixed an issue where `UPDATE` and `DELETE` from a table with foreign key could fail unexpectedly with "ERROR: 40001: could not serialize access due to concurrent update when using Serializable snapshot".

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.
- Fixed an issue that prevented the enablement of improved memory management in certain scenarios in Aurora PostgreSQL 15.3.

####

Aurora PostgreSQL 13.11.0, July 13, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition
to support PostgreSQL versions 15.3, 14.8, 13.11, 12.15, and 11.20. These releases contains product improvements and bug fixes made by
the PostgreSQL community, along with Aurora-specific improvements. The releases also contain new features and improvements for
[Babelfish for Aurora PostgreSQL version 3.2](AuroraBabelfish.md "AuroraBabelfish.md"), and improved support for
[AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish"). Refer to the [Amazon Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md")
to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder, if you are running any version of Amazon Aurora PostgreSQL 11,
you must upgrade to a newer major version by February 29, 2024.

###### New features

- This release contains memory management improvements which increase database stability and availability by proactively
  preventing issues caused by insufficient memory. For more information, see [Improved memory management in Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md "../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md").
- Added support for the `pgvector` extension version 0.4.1.

###### High priority enhancements

- Fixed an issue with the subtransaction metadata handling when performing a survivable reader reconnect.
- Fixed an issue during ZDP which is related to the extension environment variables.
- Addressed a transient error during logical replication that caused a process to incorrectly calculate that it had encountered an unexpected page.
- Fixed an issue which causes a period of unavailability due to a partially created replication origin state file.

###### General enhancements

- Added a new function, `aurora_stat_memctx_usage()`, to show backend memory use breakdown at a Postgres memory context level.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue with the calculation of the `AuroraReplicaLag` metric.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Further reduced the database downtime during ZDP.
- Fixed a bug which can cause unavailability during ZDP.
- Fixed an issue which caused `pg_ls_waldir()` to return "ERROR: could not stat file".
- Added support for TLS 1.3 with ciphers TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384.
- Addressed an issue that blocked a major version upgrade on the Aurora replica of an RDS for PostgreSQL DB instance.
- Fixed an issue that could prevent scaling in Aurora Serverless v2 instances.
- Fixed an issue in the `pg_vector` extension where, in rare cases, infinite or NAN values caused a crash during the index creation.
- Fixed an issue to improve the performance.
- Upgraded `GEOS` to version 3.11.2.
- Upgraded `pg_cron` to version 1.5.
- Upgraded `pg_partman` to version 4.7.3.
- Upgraded `plv8` to version 3.1.6.
- Upgraded `tds_fdw` to 2.0.3.

### PostgreSQL 13.10 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.10. For more
information about the improvements in PostgreSQL 13.10, see [PostgreSQL release 13.10](https://www.postgresql.org/docs/13/release-13-10.html "https://www.postgresql.org/docs/13/release-13-10.html").

###### Releases and patches

- [Aurora PostgreSQL 13.10.9, November 6, 2024](#aurorapostgresql-versions-version1310x-13109 "#aurorapostgresql-versions-version1310x-13109")
- [Aurora PostgreSQL 13.10.8, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.13108 "#AuroraPostgreSQL.Updates.20180305.13108")
- [Aurora PostgreSQL 13.10.7, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.13107 "#AuroraPostgreSQL.Updates.20180305.13107")
- [Aurora PostgreSQL 13.10.6, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.13106 "#AuroraPostgreSQL.Updates.20180305.13106")
- [Aurora PostgreSQL 13.10.5, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.13105 "#AuroraPostgreSQL.Updates.20180305.13105")
- [Aurora PostgreSQL 13.10.4, October 5, 2023](#AuroraPostgreSQL.Updates.20180305.13104 "#AuroraPostgreSQL.Updates.20180305.13104")
- [Aurora PostgreSQL 13.10.3, July 24, 2023](#AuroraPostgreSQL.Updates.20180305.13103 "#AuroraPostgreSQL.Updates.20180305.13103")
- [Aurora PostgreSQL 13.10.2, May 10, 2023](#AuroraPostgreSQL.Updates.20180305.13102 "#AuroraPostgreSQL.Updates.20180305.13102")
- [Aurora PostgreSQL 13.10.1, April 5, 2023](#AuroraPostgreSQL.Updates.20180305.13101 "#AuroraPostgreSQL.Updates.20180305.13101")

#### Aurora PostgreSQL 13.10.9, November 6, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.10.8, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 13.10.7, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.10.6, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 13.10.5, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 13.10.4, October 5, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.

####

Aurora PostgreSQL 13.10.3, July 24, 2023

###### General enhancements

- Fixed an issue related to storage space reclamation following table drop or reindex or truncate operations.
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric.
- Fixed a bug which can cause unavailability during ZDP.
- Fixed an issue that prevented reclaiming storage on transaction commits.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Added Aurora Serverless v2 scaling enhancements.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed multiple issues which can cause Aurora replicas with the improved read availability feature to restart when reconnecting with the writer instance.
- Fixed an issue preventing a survivable reader reconnect.

####

Aurora PostgreSQL 13.10.2, May 10, 2023

###### General enhancements

- Fixed an error when loading the `test_decoding` plugin in `pg_create_logical_replication_slot`.
- Fixed an issue that causes logical replication to fail when using write-through cache.
- Updated the Oracle client used by the `oracle_fdw` extension to version 21.9.0.0.0.

####

Aurora PostgreSQL 13.10.1, April 5, 2023

###### New features

- Introduced a new QPM plan hash calculation for multi-schema support. If users want to use QPM in multi-schema
  environments, they can set the `apg_plan_mgmt.plan_hash` version to 2 and call `apg_plan_mgmt.validate_plans`('`update_plan_hash`').

###### General enhancements

- Upgraded `PROJ` support to version 9.1.0.
- Upgraded the `GDAL` library in `PostGIS` to version 3.5.3.
- Added support for the `TCN` and `SEG` extensions.
- Improved performance of deletes from b-tree and hash indexes on Aurora replicas.
- Includes Aurora Serverless v2 scaling enhancements.
- Fixed an issue in QPM that prevented the enforcement of approved plans when joining partitioned tables.
- Fixed an issue that caused incorrect buffer hit counts in `EXPLAIN`.
- Improved the engine startup time, particularly on large instances with many objects.
- The Aurora function `aurora_stat_logical_wal_cache()` is now visible to all users.
- Fixed an issue in QPM that could cause unavailability when enforcing plans from prepared statements.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `hll` to version 2.17
  - `Oracle_fdw` to version 2.5.0
  - `orafce` to version 4.0.0
  - `pg_cron` to version 1.4.2
  - `pg_hint_plan` to version 1.3.8
  - `pg_logical` to version 2.4.2
  - `pg_trgm` to version 1.4
  - `pgrouting` to version 3.4.1
  - `PostGIS` to version 3.3.2
  - `SEG` to version 1.0
  - `TCN` to version 1.0
  - `wal2json` to version 2.5

### PostgreSQL 13.9

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.9. For more
information about the improvements in PostgreSQL 13.9, see [PostgreSQL release 13.9](https://www.postgresql.org/docs/13/release-13-9.html "https://www.postgresql.org/docs/13/release-13-9.html").

###### Releases and patches

- [Aurora PostgreSQL 13.9.13, June 18, 2025](#aurorapostgresql-versions-version13913x-13913 "#aurorapostgresql-versions-version13913x-13913")
- [Aurora PostgreSQL 13.9.12, April 29, 2025](#aurorapostgresql-versions-version13912x-13912 "#aurorapostgresql-versions-version13912x-13912")
- [Aurora PostgreSQL 13.9.10, November 18, 2024](#aurorapostgresql-versions-version139x-13910 "#aurorapostgresql-versions-version139x-13910")
- [Aurora PostgreSQL 13.9.9, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1399 "#AuroraPostgreSQL.Updates.20180305.1399")
- [Aurora PostgreSQL 13.9.8, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1398 "#AuroraPostgreSQL.Updates.20180305.1398")
- [Aurora PostgreSQL 13.9.7, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.1397 "#AuroraPostgreSQL.Updates.20180305.1397")
- [Aurora PostgreSQL 13.9.6, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1396 "#AuroraPostgreSQL.Updates.20180305.1396")
- [Aurora PostgreSQL 13.9.5, October 04, 2023](#AuroraPostgreSQL.Updates.20180305.1395 "#AuroraPostgreSQL.Updates.20180305.1395")
- [Aurora PostgreSQL 13.9.4, September 13, 2023](#AuroraPostgreSQL.Updates.20180305.1394 "#AuroraPostgreSQL.Updates.20180305.1394")
- [Aurora PostgreSQL 13.9.2, March 3, 2023](#AuroraPostgreSQL.Updates.20180305.1392 "#AuroraPostgreSQL.Updates.20180305.1392")
- [Aurora PostgreSQL 13.9.0, January 20, 2023](#AuroraPostgreSQL.Updates.20180305.1390 "#AuroraPostgreSQL.Updates.20180305.1390")

#### Aurora PostgreSQL 13.9.13, June 18, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the improved reader availability functionality that might result in longer recover times and impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause increased latency on data processing.

#### Aurora PostgreSQL 13.9.12, April 29, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 13.9.10, November 18, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.9.9, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 13.9.8, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.9.7, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 13.9.6, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 13.9.5, October 04, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQl community security issue:
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")

###### High priority stability enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue which can cause a database instance to restart while executing IO intensive read workloads.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.

####

Aurora PostgreSQL 13.9.4, September 13, 2023

###### General enhancements

- Added Aurora Serverless v2 scaling enhancements.
- Fixed an issue in `pg_cron` which can prevent scaling in Aurora Serverless v2.
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric.
- Fixed a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

####

Aurora PostgreSQL 13.9.2, March 3, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

###### General stability enhancements

- Fixed an issue where the approved plans for joins with partitioned tables weren't being enforced.
- Fixed an issue in `PostGIS` where the `GDAL` data wasn't loading.
- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled.
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out.
- Fixed an issue that causes logical replication to fail when using write-through cache

####

Aurora PostgreSQL 13.9.0, January 20, 2023

###### High priority stability enhancements

- Fixed an issue where an upgrade fails because the oldest `MultiXactId` is updated incorrectly.
- Fixed an issue where the commit latency metrics weren't updated.
- Fixed an issue that could lead to a brief period of unavailability.

###### General stability enhancements

- Fixed an issue that caused DB instance migration failures.
- Fixed an issue where the DB fails to start because of an inconsistency in the metadata.
- Improved the error handling and diagnosability.
- Upgraded the RDKit extension to version 4.2.
- Upgraded the `GDAL` library to version 3.4.3.
- Fixed an issue where the cluster cache management process doesn't shutdown gracefully.
- Fixed an issue that can cause certain processes to linger in an inconsistent state during a clean shutdown.
- Fixed an issue with the pg_repack extension.
- Improved the collation library (glibc) handling with a new independent default collation library.

### PostgreSQL 13.8 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.8. For more
information about the improvements in PostgreSQL 13.8, see [PostgreSQL release 13.8](https://www.postgresql.org/docs/13/release-13-8.html "https://www.postgresql.org/docs/13/release-13-8.html").

###### Releases and patches

- [Aurora PostgreSQL 13.8.8, November 22, 2024](#aurorapostgresql-versions-version138x-1388 "#aurorapostgresql-versions-version138x-1388")
- [Aurora PostgreSQL 13.8.7, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.1387 "#AuroraPostgreSQL.Updates.20180305.1387")
- [Aurora PostgreSQL 13.8.6, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1386 "#AuroraPostgreSQL.Updates.20180305.1386")
- [Aurora PostgreSQL 13.8.5, December 18, 2023](#AuroraPostgreSQL.Updates.20180305.1385 "#AuroraPostgreSQL.Updates.20180305.1385")
- [Aurora PostgreSQL 13.8.4, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1384 "#AuroraPostgreSQL.Updates.20180305.1384")
- [Aurora PostgreSQL 13.8.3, October 17, 2023](#AuroraPostgreSQL.Updates.20180305.1383 "#AuroraPostgreSQL.Updates.20180305.1383")
- [Aurora PostgreSQL 13.8.2, March 2, 2023](#AuroraPostgreSQL.Updates.20180305.1382 "#AuroraPostgreSQL.Updates.20180305.1382")
- [Aurora PostgreSQL 13.8.1, December 13, 2022](#AuroraPostgreSQL.Updates.20180305.1381 "#AuroraPostgreSQL.Updates.20180305.1381")
- [Aurora PostgreSQL 13.8.0, November 09, 2022](#AuroraPostgreSQL.Updates.20180305.1380 "#AuroraPostgreSQL.Updates.20180305.1380")

#### Aurora PostgreSQL 13.8.8, November 22, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.

####

Aurora PostgreSQL 13.8.7, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 13.8.6, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.8.5, December 18, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 13.8.4, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 13.8.3, October 17, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue that causes logical replication to fail when using write-through cache

####

Aurora PostgreSQL 13.8.2, March 2, 2023

###### General stability enhancements

- Fixed an issue where the approved plans for joins with partitioned tables weren't being enforced.
- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled.
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out.
- Fixed an issue with the `pg_cron` parallel running of tasks.

####

Aurora PostgreSQL 13.8.1, December 13, 2022

###### General stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades.
- Fixed an issue that could cause data inconsistency during replication.

####

Aurora PostgreSQL 13.8.0, November 09, 2022

###### High priority stability enhancements

- Fixed an Aurora Serverless v2 scaling issue.
- Fixed an issue which caused Aurora Serverless v2 shrink failure.

###### General stability enhancements

- Improved buffer cache scavenging when the buffer cache is in duress.
- Fixed an issue in Database Activity Streams that leads to high memory consumption.
- Fixed an issue that caused DB instance restarts.
- Fixed an issue where a DB instance restarts recursively while generating monitoring metrics during a crash.
- Fixed an issue where a DB instance restarted during performance metric collection.
- Fixed an issue where an attempt to connect to the database would fail with SSLV3_ALERT_CERTIFICATE_UNKNOWN.
- Improved the error reporting in case of an inconsistent B-tree index.
- Improved the diagnostic logging around setting invalid hint bits.
- Fixed an issue where autovacuum would incorrectly skip tables.
- Improved the logical replication prefetching.
- Fixed a durability issue in the GIN indexes.
- Provided options to configure MultiXact SLRU cache. By setting the following parameters (GUCs),
  customers will now be able to change the MultiXact SLRU cache sizes:
  - multixact_members_cache_size
  - multixact_offsets_cache_size

- Fixed an issue to detect and cancel stuck major version upgrades.
- Fixed an issue in hash join that could lead to increased memory consumption.
- Improved the logical replication performance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Upgraded the `GEOS` version to 3.10.3.
- Updated the `PLV8` version to 3.0.0.
- Updated the `PostGIS` extension to version 3.2.3.
- Fixed an issue with `st_orientedenvelope` that caused it to loop with a 1-D input to return 0.
- Fixed an issue where the connection to SQL Server using tds_fdw fails.

### PostgreSQL 13.7 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.7. For more
information about the improvements in PostgreSQL 13.7, see [PostgreSQL 13.7](https://www.postgresql.org/docs/13/release-13-7.html "https://www.postgresql.org/docs/13/release-13-7.html").

###### Releases and patches

- [Aurora PostgreSQL 13.7.11, November 20, 2024](#aurorapostgresql-versions-version137x-13711 "#aurorapostgresql-versions-version137x-13711")
- [Aurora PostgreSQL 13.7.10, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.13710 "#AuroraPostgreSQL.Updates.20180305.13710")
- [Aurora PostgreSQL 13.7.9, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.1379 "#AuroraPostgreSQL.Updates.20180305.1379")
- [Aurora PostgreSQL 13.7.8, December 22, 2023](#AuroraPostgreSQL.Updates.20180305.1378 "#AuroraPostgreSQL.Updates.20180305.1378")
- [Aurora PostgreSQL 13.7.7, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1377 "#AuroraPostgreSQL.Updates.20180305.1377")
- [Aurora PostgreSQL 13.7.6, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.1376 "#AuroraPostgreSQL.Updates.20180305.1376")
- [Aurora PostgreSQL 13.7.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.1375 "#AuroraPostgreSQL.Updates.20180305.1375")
- [Aurora PostgreSQL 13.7.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.1374 "#AuroraPostgreSQL.Updates.20180305.1374")
- [Aurora PostgreSQL 13.7.3, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.1373 "#AuroraPostgreSQL.Updates.20180305.1373")
- [Aurora PostgreSQL 13.7.1, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.1371 "#AuroraPostgreSQL.Updates.20180305.1371")
- [Aurora PostgreSQL 13.7.0, June 9, 2022](#AuroraPostgreSQL.Updates.20180305.1370 "#AuroraPostgreSQL.Updates.20180305.1370")

#### Aurora PostgreSQL 13.7.11, November 20, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 13.7.10, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 13.7.9, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 13.7.8, December 22, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 13.7.7, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 13.7.6, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

####

Aurora PostgreSQL 13.7.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Fixed an issue that could cause data inconsistency during replication.

####

Aurora PostgreSQL 13.7.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.

####

Aurora PostgreSQL 13.7.3, October 13, 2022

###### High priority stability enhancements

- Fixed a `PLV8` issue where the base parameter doesn't get loaded properly into the memory.
- Fixed an issue where scaling an Aurora Serverless v2 instance gets stuck if VACUUM is running.

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the relfilenode.
- Fixed a database restart issue when a plan gets invaliated but the engine still checks if it is valid.
- Fixed a stuck scaling issue when the current scaling events time out.
- Upgraded the `PostGIS` extension to version 3.1.7.
- Fixed an issue where extended query messages might be lost during zero-downtime patching (ZDP) causing the extended query to hang after the ZDP completion.

####

Aurora PostgreSQL 13.7.1, July 6, 2022

###### Critical stability enhancements

- Fixed an issue that could cause periods of unavailability during a storage node restart.

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue when the connection to SQL Server fails using the `TDS_FDW` extension to query a foreign table.
- Fixed an issue that caused connections using the provided root certificate to fail.
- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries.

####

Aurora PostgreSQL 13.7.0, June 9, 2022

###### New features

- Added support for the `large object` module (extension). For more information,
  see [Managing
  large objects with the lo module](../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md "../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md").
- Added support for zero-downtime patching (ZDP) for minor version upgrades and patches. For more information, see
  [Minor
  release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor")
  in the _Amazon Aurora User Guide_.

###### Critical updates

- Fixed a replay crash due to an LSN mismatch
- Fixed the `aws_s3` extension to prevent invalid region injection

###### High stability updates

- Fixed multiple issues related to out-of-memory conditions which could result in brief periods of unavailability
- Fixed an Aurora Serverless v2 scaling issue.

###### General enhancements

- Fixed a lock contention crash during an Aurora Serverless v1 scaling event.
- Fixed an issue where logical replication becomes stuck after a restart.
- Fixed multiple issues that could lead to brief periods of unavailability.
- Fixed a crash in `pg_cron` due to a task still running but being unscheduled.
- Fixed, during redo, an invalid page hit on the Generic Redo for GENERIC_XLOG_FULL_PAGE_DATA.
  This happens due to a timing hole between generating the log record and then writing the metadata
  for the record on the RW node and the RO node replays between those operations.
- Improved the query performance by supporting parallel workers.
- Upgraded the plugin `wal2json` version to 2.4.
- Upgraded the `pglogical` extension to version 2.4.1.

### PostgreSQL 13.6 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.6. For more
information about the improvements in PostgreSQL 13.6, see [PostgreSQL release
13.6](https://www.postgresql.org/docs/13/release-13-6.html "https://www.postgresql.org/docs/13/release-13-6.html").

###### Releases and patches

- [Aurora PostgreSQL 13.6.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.1366 "#AuroraPostgreSQL.Updates.20180305.1366")
- [Aurora PostgreSQL 13.6.5, October 18, 2022](#AuroraPostgreSQL.Updates.20180305.1365 "#AuroraPostgreSQL.Updates.20180305.1365")
- [Aurora PostgreSQL 13.6.4, July 18, 2022](#AuroraPostgreSQL.Updates.20180305.1364 "#AuroraPostgreSQL.Updates.20180305.1364")
- [Aurora PostgreSQL 13.6.3, June 2, 2022](#AuroraPostgreSQL.Updates.20180305.1363 "#AuroraPostgreSQL.Updates.20180305.1363")
- [Aurora PostgreSQL 13.6.2, May 12, 2022](#AuroraPostgreSQL.Updates.20180305.1362 "#AuroraPostgreSQL.Updates.20180305.1362")
- [Aurora PostgreSQL 13.6.1, April 27, 2022](#AuroraPostgreSQL.Updates.20180305.1361 "#AuroraPostgreSQL.Updates.20180305.1361")
- [Aurora PostgreSQL 13.6.0, March 29, 2022](#AuroraPostgreSQL.Updates.20180305.1360 "#AuroraPostgreSQL.Updates.20180305.1360")

####

Aurora PostgreSQL 13.6.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 13.6.5, October 18, 2022

###### High priority enhancements

- Fixed an issue where Amazon Aurora Serverless v2 scaling may get blocked if VACUUM is running.
- Fixed an issue where Amazon Aurora Serverless v2 scaling may get blocked on Aurora replicas.

###### General enhancements

- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries.
- Updated the PostGIS extension to version 3.1.7.

####

Aurora PostgreSQL 13.6.4, July 18, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others
  omit "security restricted operation". For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in periods of unavailability.

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files that could result in periods of unavailability.
- Fixed a defect where the validation of cached plans may lead to a database restart when the plan was previously invalidated.

####

Aurora PostgreSQL 13.6.3, June 2, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others
  omit "security restricted operation". For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability updates

- Fixed an issue that can lead to a blocked scale operation when a `COPY` command is in progress in Amazon Aurora Serverless v2.
- Fixed an issue that can cause a restart of the database when dropping or truncating tables in Amazon Aurora Serverless v2.
- Fixed an issue in the `apg_prewarm` extension that can lead to a blocked scale operation in Amazon Aurora Serverless v2.
- Fixed an issue in the dynamic shared memory allocation that can lead to a blocked scale operation in Amazon Aurora Serverless v2.
- Fixed an issue that can cause a restart of the postmaster process in Amazon Aurora Serverless v2.
- Fixed an issue where a minor version ugprade may get blocked when there is a SQL view that refers to the `checksum()` function in Babelfish for Aurora PostgreSQL.
- Fixed an issue in `apg_plan_mgmt` that can cause a restart when Query Plan Management (QPM) is enabled.

####

Aurora PostgreSQL 13.6.2, May 12, 2022

###### High priority stability enhancements

- Fixed an issue that causes upgrades to fail when Babelfish for Aurora PostgreSQL is enabled.
- Fixed an issue that causes scaling in Aurora Serverless v2 to fail.

###### General enhancements

- Fixed an issue that could cause unavailability due to improper locking of shared memory.

####

Aurora PostgreSQL 13.6.1, April 27, 2022

###### High priority stability enhancements

- Fixed an issue that could cause incorrect `WriteIOPS` reporting in the AWS console.
- Fixed an issue that could cause unavailability after removal of a read node from a cluster.

###### General enhancements

- Fixed an issue that could cause an engine restart during periods of low free memory.

####

Aurora PostgreSQL 13.6.0, March 29, 2022

###### New features

- Added support for the `tds_fdw` extension version 2.0.2.

###### High priority stability enhancements

- Fixed multiple issues that may result in unavailability of a read node.
- Fixed an issue that may result in a read node being unable to replay WAL requiring the replication slot to be dropped and resynchronized.
- Fixed an issue that could cause excess storage use due to files not being properly closed.

###### General enhancements

- Fixed a small memory leak on read nodes when `commit_ts` is set.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".
- Fixed an issue that could cause an import from Amazon S3 to fail when using the `aws_s3` extension
- Fixed multiple issues that could result in periods of unavailability when using `apg_plan_mgmt`
- Fixed multiple issues that could result in periods of unavailability when QPM is enabled

### PostgreSQL 13.5 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.5. For more
information about the improvements in PostgreSQL 13.5, see [PostgreSQL release
13.5](https://www.postgresql.org/docs/13/release-13-5.html "https://www.postgresql.org/docs/13/release-13-5.html").

###### Releases and patches

- [Aurora PostgreSQL 13.5.7, August 24, 2023](#AuroraPostgreSQL.Updates.20180305.1357 "#AuroraPostgreSQL.Updates.20180305.1357")
- [Aurora PostgreSQL 13.5.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.1356 "#AuroraPostgreSQL.Updates.20180305.1356")
- [Aurora PostgreSQL 13.5.5, October 18, 2022](#AuroraPostgreSQL.Updates.20180305.1355 "#AuroraPostgreSQL.Updates.20180305.1355")
- [Aurora PostgreSQL 13.5.4, July 20, 2022](#AuroraPostgreSQL.Updates.20180305.1354 "#AuroraPostgreSQL.Updates.20180305.1354")
- [Aurora PostgreSQL 13.5.3, April 13, 2022](#AuroraPostgreSQL.Updates.20180305.1353 "#AuroraPostgreSQL.Updates.20180305.1353")
- [Aurora PostgreSQL 13.5.1, March 3, 2022](#AuroraPostgreSQL.Updates.20180305.1351 "#AuroraPostgreSQL.Updates.20180305.1351")
- [Aurora PostgreSQL 13.5.0, February 25, 2022](#AuroraPostgreSQL.Updates.20180305.1350 "#AuroraPostgreSQL.Updates.20180305.1350")

####

Aurora PostgreSQL 13.5.7, August 24, 2023

###### General enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.

####

Aurora PostgreSQL 13.5.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 13.5.5, October 18, 2022

###### General enhancements

- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries.
- Updated the PostGIS extension to version 3.1.7.

####

Aurora PostgreSQL 13.5.4, July 20, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others
  omit "security restricted operation". For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files that could result in periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that can cause a restart of the postmaster process in Amazon Aurora Serverless v2.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".

####

Aurora PostgreSQL 13.5.3, April 13, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

###### General enhancements

- Fixed a bug that could cause an engine restart during periods of low free memory.

####

Aurora PostgreSQL 13.5.1, March 3, 2022

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to 3.1.5.
  This update contains a PostGIS fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 13.5.0, February 25, 2022

###### High priority stability enhancements

- Fixed a bug where logical replication may hang resulting in the replay falling behind on the read node. The instance may eventually restart.

###### Additional improvements and enhancements

- Added the `Buffers: shared hit` metric to the Explain output.
- Fixed a buffer cache bug that could cause brief periods of unavailability.
- Fixed a bug in the `apg_plan_mgmt` extension where an index based plan was not being enforced.
- Fixed a bug in the `pg_logical` extension that could cause brief periods of unavailability due to improper handling of `NULL` arguments.
- Fixed a bug that could cause brief periods of unavailability due to reading uninitialized pages.
- Fixed an issue where orphaned files caused major version upgrades to fail.
- Fixed incorrect Aurora Storage Daemon log write metrics.
- Fixed multiple bugs that could result in `WAL` replay falling behind and eventually causing the reader instances to restart.
- Improved the Aurora buffer cache page validation on reads.
- Improved the Aurora storage metadata validation.

This version also includes the following change:

- The [pg_cron](https://github.com/citusdata/pg_cron "https://github.com/citusdata/pg_cron") extension is updated to 1.4.1

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
13](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.13").

### PostgreSQL 13.4 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.4. For more
information about the improvements in PostgreSQL 13.4, see [PostgreSQL release
13.4](https://www.postgresql.org/docs/13/release-13-4.html "https://www.postgresql.org/docs/13/release-13-4.html").

###### Releases and patches

- [Aurora PostgreSQL 13.4.6, December 19, 2022](#AuroraPostgreSQL.Updates.20180305.1346 "#AuroraPostgreSQL.Updates.20180305.1346")
- [Aurora PostgreSQL 13.4.5, October 18, 2022](#AuroraPostgreSQL.Updates.20180305.1345 "#AuroraPostgreSQL.Updates.20180305.1345")
- [Aurora PostgreSQL 13.4.4, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.1344 "#AuroraPostgreSQL.Updates.20180305.1344")
- [Aurora PostgreSQL 13.4.2, April 12, 2022](#AuroraPostgreSQL.Updates.20180305.1342 "#AuroraPostgreSQL.Updates.20180305.1342")
- [Aurora PostgreSQL 13.4.1](#AuroraPostgreSQL.Updates.20180305.1341 "#AuroraPostgreSQL.Updates.20180305.1341")
- [Aurora PostgreSQL 13.4.0](#AuroraPostgreSQL.Updates.20180305.1340 "#AuroraPostgreSQL.Updates.20180305.1340")

####

Aurora PostgreSQL 13.4.6, December 19, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 13.4.5, October 18, 2022

###### General enhancements

- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries.
- Updated the `PostGIS` extension to version 3.1.7.

####

Aurora PostgreSQL 13.4.4, July 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### General enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that could cause a restart of the postmaster process in Amazon Aurora Serverless v2.
- Fixed an issue that could cause Performance Insights to display "Unknown wait event".
- Fixed an issue that could result in periods of unavailability due to the existence of duplicate relation files.

####

Aurora PostgreSQL 13.4.2, April 12, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

###### General enhancements

- Fixed a buffer cache bug that could cause brief periods of unavailability.

####

Aurora PostgreSQL 13.4.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to 3.1.5.
  This update contains a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 13.4.0

###### New features

- This version supports Babelfish 1.0.0 which extends your Amazon Aurora PostgreSQL database with the ability to accept database connections from Microsoft SQL Server clients.
  For more information, see [Working with Babelfish for Aurora PostgreSQL](../AuroraUserGuide/babelfish.md "../AuroraUserGuide/babelfish.md").

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major version update
  with the message: "PANIC: could not access status of next transaction id
  xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue which can cause vacuum operations to become blocked after all Aurora read replicas have been removed from a secondary cluster.
- Fixed an issue where read nodes restart due to a replication origin cache lookup failure.
- Fixed an issue where read queries may time out on read nodes during the replay of lazy truncation triggered by vacuum on the write node.
- Fixed an issue that causes Performance Insights to incorrectly set the backend type of a database connection.
- Fixed an issue where the aurora_postgres_replica_status() function returned stale or lagging CPU stats.
- Fixed an issue where the role `rds_superuser` did not have permission to execute the `pg_stat_statements_reset()` function.
- Fixed an issue with the `apg_plan_mgmt` extension where the planning and execution times were reported as 0.
- Removed support for the DES, 3DES, and RC4 cipher suites.
- Updated the `PostGIS` extension to version 3.1.4.
- Updated the `pgrouting` extension to 3.1.3.
- Updated the `pglogical` extension to 2.4.0.
- Added support for the following SPI module extensions:
  - `autoinc version 1.0`
  - `insert_username version 1.0`
  - `moddatetime version 1.0`
  - `refint version 1.0`

- Fixed multiple issues in the Aurora storage daemon that could lead to brief periods of unavailability when specific network configurations are used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that leads to writer node restart. This also reduces the overall system memory consumption.

### PostgreSQL 13.3 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 13.3. For more
information about the improvements in PostgreSQL 13.3, see [PostgreSQL release
13.3](https://www.postgresql.org/docs/13/release-13-3.html "https://www.postgresql.org/docs/13/release-13-3.html").

###### Releases and patches

- [Aurora PostgreSQL 13.3.5, December 30, 2022](#AuroraPostgreSQL.Updates.20180305.1335 "#AuroraPostgreSQL.Updates.20180305.1335")
- [Aurora PostgreSQL 13.3.4, July 14, 2022](#AuroraPostgreSQL.Updates.20180305.1334 "#AuroraPostgreSQL.Updates.20180305.1334")
- [Aurora PostgreSQL 13.3.3, April 7, 2022](#AuroraPostgreSQL.Updates.20180305.1333 "#AuroraPostgreSQL.Updates.20180305.1333")
- [Aurora PostgreSQL 13.3.2](#AuroraPostgreSQL.Updates.20180305.1332 "#AuroraPostgreSQL.Updates.20180305.1332")
- [Aurora PostgreSQL 13.3.1](#AuroraPostgreSQL.Updates.20180305.1331 "#AuroraPostgreSQL.Updates.20180305.1331")
- [Aurora PostgreSQL 13.3.0](#AuroraPostgreSQL.Updates.20180305.1330 "#AuroraPostgreSQL.Updates.20180305.1330")

####

Aurora PostgreSQL 13.3.5, December 30, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 13.3.4, July 14, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".

####

Aurora PostgreSQL 13.3.3, April 7, 2022

###### Security enhancements

- Includes additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 13.3.2

###### Security enhancements

- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to `PostGIS` 3.0.3.
  This is a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL 13.3.1

###### Releases and patches

###### Security enhancements

- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major version
  update with the message: "PANIC: could not access status of next transaction
  id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue where read nodes restart due to a replication origin cache lookup failure.
- Fixed an issue with the `apg_plan_mgmt` extension where the planning and execution times were reported as 0.
- Fixed an issue that causes Performance Insights to incorrectly set the backend type of a database connection.
- Fixed an issue with the `apg_plan_mgmt` extension where plan outline on a partitioned table did not enforce an index-based plan.
- Fixed an issue where orphaned files caused failed translations in read codepaths during or after a major version upgrade.
- Fixed multiple issues in the Aurora storage daemon that could lead to brief periods of unavailability when specific network configurations are used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that leads to writer node restart. This also reduces the overall system memory consumption.

####

Aurora PostgreSQL 13.3.0

###### New features

- Supports a major version upgrade from
  [Aurora PostgreSQL 4.0.0](#AuroraPostgreSQL.Updates.20180305.400 "#AuroraPostgreSQL.Updates.20180305.400") and later versions
- Supports `bool_plperl` version 1.0
- Supports `rds_tools` version 1.0

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read node may be inconsistent following a restart of that node.

###### Additional improvements and enhancements

- Contains several improvements that were announced for PostgreSQL releases [13.0](https://www.postgresql.org/docs/13/release-13.html "https://www.postgresql.org/docs/13/release-13.html"),
  [13.1](https://www.postgresql.org/docs/13/release-13-1.html "https://www.postgresql.org/docs/13/release-13-1.html"),
  [13.2](https://www.postgresql.org/docs/13/release-13-2.html "https://www.postgresql.org/docs/13/release-13-2.html")
  and [13.3](https://www.postgresql.org/docs/13/release-13-3.html "https://www.postgresql.org/docs/13/release-13-3.html")
- Instance type R4 was deprecated.
- Updated the following extensions:
  - `hll` to version 2.15.
  - `hstore` to version 1.7.
  - `intarray` to version 1.3.
  - `log_fdw` to version 1.2.
  - `ltree` to version 1.2.
  - `pg_hint_plan` to version 1.3.7.
  - `pg_repack` to version 1.4.6.
  - `pg_stat_statements` to version 1.8.
  - `pg_trgm` to version 1.5.
  - `pgaudit` to version 1.5.
  - `pglogical` to version 2.3.3.
  - `pgrouting` to version 3.1.0
  - `plcoffee` to version 2.3.15.
  - `plls` to version 2.3.15.
  - `plv8` to version 2.3.15.

## PostgreSQL 12 versions (includes some deprecated versions)

###### Version updates

- [PostgreSQL 12.22](#aurorapostgresql-versions-version1222x "#aurorapostgresql-versions-version1222x")
- [PostgreSQL 12.20 (Deprecated)](#aurorapostgresql-versions-version1220x "#aurorapostgresql-versions-version1220x")
- [PostgreSQL 12.19
  (Deprecated)](#aurorapostgresql-versions-version1219x "#aurorapostgresql-versions-version1219x")
- [PostgreSQL 12.18 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1218X "#AuroraPostgreSQL.Updates.20180305.1218X")
- [PostgreSQL 12.17 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1217X "#AuroraPostgreSQL.Updates.20180305.1217X")
- [PostgreSQL 12.16 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1216X "#AuroraPostgreSQL.Updates.20180305.1216X")
- [PostgreSQL 12.15 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1215X "#AuroraPostgreSQL.Updates.20180305.1215X")
- [PostgreSQL 12.14 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1214X "#AuroraPostgreSQL.Updates.20180305.1214X")
- [PostgreSQL 12.13 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1213X "#AuroraPostgreSQL.Updates.20180305.1213X")
- [PostgreSQL 12.12 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1212X "#AuroraPostgreSQL.Updates.20180305.1212X")
- [PostgreSQL 12.11 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1211X "#AuroraPostgreSQL.Updates.20180305.1211X")
- [PostgreSQL 12.10 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1210X "#AuroraPostgreSQL.Updates.20180305.1210X")
- [PostgreSQL 12.9](#AuroraPostgreSQL.Updates.20180305.129 "#AuroraPostgreSQL.Updates.20180305.129")
- [PostgreSQL 12.8 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.128X "#AuroraPostgreSQL.Updates.20180305.128X")
- [PostgreSQL 12.7,
  Aurora PostgreSQL 4.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.42 "#AuroraPostgreSQL.Updates.20180305.42")
- [PostgreSQL 12.6,
  Aurora PostgreSQL 4.1 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.41 "#AuroraPostgreSQL.Updates.20180305.41")
- [PostgreSQL 12.4,
  Aurora PostgreSQL 4.0 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.40 "#AuroraPostgreSQL.Updates.20180305.40")

### PostgreSQL 12.22

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.22. For more information
about the improvements in PostgreSQL 12.22, see [PostgreSQL release
12.22](https://www.postgresql.org/docs/12/release-12-22.html "https://www.postgresql.org/docs/12/release-12-22.html").

###### Releases and patches

- [Aurora PostgreSQL 12.22.7, January 28, 2026](#aurorapostgresql-versions-version12227x-12227 "#aurorapostgresql-versions-version12227x-12227")
- [Aurora PostgreSQL 12.22.6, November 13, 2025](#aurorapostgresql-versions-version12226x-12226 "#aurorapostgresql-versions-version12226x-12226")
- [Aurora PostgreSQL 12.22.5, June 24, 2025](#aurorapostgresql-versions-version12225x-12225 "#aurorapostgresql-versions-version12225x-12225")
- [Aurora PostgreSQL 12.22.4, March 24,
  2025](#aurorapostgresql-versions-version12224x-12224 "#aurorapostgresql-versions-version12224x-12224")
- [Aurora PostgreSQL 12.22.3, February
  13, 2025](#aurorapostgresql-versions-version12223x-12223 "#aurorapostgresql-versions-version12223x-12223")
- [Aurora PostgreSQL 12.22.2, January 20,
  2025](#aurorapostgresql-versions-version12222x-12222 "#aurorapostgresql-versions-version12222x-12222")
- [Aurora PostgreSQL 12.22.1, December
  27, 2024](#aurorapostgresql-versions-version12221x-12221 "#aurorapostgresql-versions-version12221x-12221")
- [Aurora PostgreSQL 12.22, December 27,
  2024](#aurorapostgresql-versions-version1222x-1222 "#aurorapostgresql-versions-version1222x-1222")

#### Aurora PostgreSQL 12.22.7, January 28, 2026

**Critical stability enhancements**

- Fixed an issue that could cause garbage collection to get blocked on a change data capture (CDC) volume.
- Fix an issue which could trigger a race in change data capture (CDC) volume expansion.
- Process cleanup improvements during zero downtime patching to ensure that all database processes are properly terminated, preventing shutdown stalls and improving zero downtime patching success.
- Fixed an Issue that could cause readers to restart or readers cannot perform read operations due to missing storage segments.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").
  - [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Fixed an issue where premature status updates during zero downtime patching could cause unnecessary failures by ensuring proper synchronization with server startup.

**General enhancements**

- Fixed IMDS throttling issues by reducing IMDS requests for region related information.

#### Aurora PostgreSQL 12.22.6, November 13, 2025

**Critical stability enhancements**

- Fixed an issue in engine minor and patch upgrades where in rare cases a backend can incorrectly process an interrupt early.
- Fixed an issue where minor version upgrades and patch upgrades might take a few seconds longer because the runtime process was not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").
  - [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").
  - [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Improved error handling mechanisms during TDS Connection reset operations.
- Fixed an issue that could prevent online recovery of an Aurora Replica from completing.
- Fixed an issue that could cause unavailability when apg_plan_mgmt is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue in Query Plan Management with running a utility statement immediately after installing the extension or resetting shared memory.
- Fixed an issue in enforcing, validating and evolving plans in Query Plan Management.
- Fixed an issue that could cause prolonged Serverless v2 scaling time.
- Fixed a crash that occurred when using ST_AsGeoJSON after upgrading to a release containing PostGIS 3.5.1 without running postgis_extensions_upgrade.
- Fixed an issue causing a replica restart during the replica join case.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica in a Global Database.
- Fixed an issue causing query execution failure for execution plans using the "bitmap heap scan" access method.
- Fixed an issue impacting query execution performance for execution plans using the "bitmap heap scan" access method.

#### Aurora PostgreSQL 12.22.5, June 24, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in handling of asynchronous I/O cancellation that could cause processes to
  become stuck indefinitely.
- Fixed an issue that causes minor version upgrades to fail with sleep/wake feature.
- Fixed an issue related to the interactions between out-of-row storage and aborted
  subtransactions that could cause issues in logical streaming when
  `aurora.enhanced_logical_replication` is enabled.
- Fixed an issue that can cause process stuck indefinitely at LWLock:BufferIO wait event.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL 12.22.4, March 24,

2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues.
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not correctly
  re-establish connection with the writer.

#### Aurora PostgreSQL 12.22.3, February

13, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8` extension.

#### Aurora PostgreSQL 12.22.2, January 20,

2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue in Global DB switchover and failover that could result in customers
  needing to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some
  cases.

**General enhancements.**

- Fixed an ownership issue where the `postgis_raster` extension could not be
  updated correctly from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 12.22.1, December

27, 2024

**Critical Priority enhancements**

- Fixed an issue where the server was restarting when the connections were reset by the
  peer.

#### Aurora PostgreSQL 12.22, December 27,

2024

###### New features for 12.22

- Optimized the minor version and patch upgrade process to reduce downtime for read
  replicas.

###### Critical stability enhancements for 12.22

- Fixed an issue that in rare cases can cause CPU usage spike.

###### High priority enhancements for 12.22

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979")
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978")
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977")
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976")

###### General enhancements for 12.22

- Made multiple improvements to Aurora in-Region failover which reduces database downtime
  further by improving storage metadata and faster buffer cache initialization.
- Made multiple improvements to upgrades with Zero-Downtime Patching (ZDP) which reduces
  connection restore time and enhances ZDP resilience from failures.
- Fixed an issue where the server_id value wasn’t updated after an Amazon RDS Blue/Green
  Deployment switchover.
- Fixed an issue that could cause database restart during hash index extension.
- Fixed an issue that would cause migration from RDS PostgreSQL to fail in the presence
  of nested tablespaces.
- Fixed an issue that would cause excessive engine startup times in the presence of a
  large number of logical replication files.
- Fixed an issue that could cause a database restart when calling functions from `aws_s3`,
  `aws_lambda`, and `aws_ml` extensions in the same database session as `aws_s3.table_import_from_s3()`.
  This fix may decrease the per-call performance of functions from the `aws_s3`, `aws_lambda`, and `aws_ml` extensions.
- Fixed an issue that prevented updating the `pgTAP` extension to version
  1.3.0 or later.
- Fixed an issue in the `PostGIS` extension, which in rare cases, could cause
  a DB instance restart.
- Fixed an issue in the `pg_repack` extension that compromises the integrity
  of invalid indexes.

###### Additional improvements and enhancements for 12.22

- Updated the following extensions:
  - `pg_cron` extension to v1.6.4.
  - `PostGIS` extension to version 3.4.3.
  - `PROJ` library extension to version 9.5.0.
  - `GEOS` library extension to verison 3.13.0.
  - `orafce` extension to 4.12.0.
  - `pgvector` extension to 0.7.4.
  - `RDKit` extension to 2024_03_6 release (4.6).
  - `pg_hint_plan` extension to version 1.3.10.

### PostgreSQL 12.20 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.20. For more
information about the improvements in PostgreSQL 12.20, see [PostgreSQL release 12.20](https://www.postgresql.org/docs/12/release-12-20.html "https://www.postgresql.org/docs/12/release-12-20.html").

###### Releases and patches

- [Aurora PostgreSQL 12.20.2, January 29, 2025](#aurorapostgresql-versions-version12202x-12202 "#aurorapostgresql-versions-version12202x-12202")
- [Aurora PostgreSQL 12.20.1, January 02, 2025](#aurorapostgresql-versions-version12201x-12201 "#aurorapostgresql-versions-version12201x-12201")
- [Aurora PostgreSQL 12.20, September 30, 2024](#aurorapostgresql-versions-version1220x-1220 "#aurorapostgresql-versions-version1220x-1220")

#### Aurora PostgreSQL 12.20.2, January 29, 2025

**Critical stability enhancements**.

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**.

- Fixed an issue in Global DB switchover and failover that could result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.

**General enhancements**.

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 12.20.1, January 02, 2025

**Critical stability enhancements**

- Fixed an issue related to Query Plan Management background worker.
- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed issue where Aurora in-Region failovers would result in failures in database startup.
- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue that prevented the scaling of Aurora Serverless v2 Read Replicas when
  aurora.enhanced_logical_replication is enabled.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in longer
  upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime further
  with faster buffer cache initialization.
- Fixed an issue where reserved keyword “PRIMARY” caused syntax errors when
  used as a column name or alias in DML and DDL statements.
- Fixed an issue that could cause an error in the wal sender process when resuming logical
  replication.
- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the `PostGIS` extension 2 installation.

#### Aurora PostgreSQL 12.20, September 30, 2024

**New features**

- Introduced a new fast failover feature to reduce database downtime during the `planned` extension failover
  events with fast storage metadata initialization and fast buffer cache recovery.
- Introduced an optimization to reduce Zero Downtime Patching (ZDP) quiet point duration to 1 second.

**High priority enhancements**

- Fixed issues where the replication of vacuum operations may cause a restart when handling
  conflicts with user queries.
- Fixed an issue where deleting a large range of keys from a BTree index could cause
  concurrent scans to crash.

**General enhancements**

- Enabled support for FIPS-validated cryptography, a fully owned AWS implementation. For more
  information, see [AWS-LC is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/ "https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/")
  on AWS Security Blog.
- Improvements to database startup time during initialization and engine
  upgrades.
- Fixed an issue that prevented the inclusion of the `pg_bigm` extension in
  shared_preload_libraries.
- Fixed an issue during ZDP which causes some connections to be terminated
  due to long transferring time. A new ZDP metric in postgresql.log called
  `ZD_SOCKET_TRANSFER_CONN_DROPPED` represents these dropped connections.
- Improved reader availability for Aurora Replicas when using system administration functions.
- Fixed an in-memory two-phase commit (2PC) metadata caching issue that caused out-of-memory
  error on Aurora read replicas replicating from RDS PostgreSQL source instances.
- Fixed an issue in storage metadata initialization that can cause prolonged database startup
  time.
- Fixed an issue that will prevent reclaiming Aurora storage space during major version
  upgrade.

**Additional improvements and enhancements**

- Updated the following extensions:
  - `pgvector` extension to version 0.7.3.
  - `mysql_fdw` extension to version REL-2_9_2.
  - `orafce` extension to version 4.10.3.
  - `pgTAP` extension to version 1.3.3.
  - `pg_cron` extension to version 1.6.3.
  - `RDKit` extension to version 4.5 (Release 2024_03_5).
  - `wal2json` extension to version 2.6.
  - pg_ad_mapping extension to version 1.0.
  - `HypoPG` extension to version 1.4.1.

### PostgreSQL 12.19

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.19. For more information
about the improvements in PostgreSQL 12.19, see [PostgreSQL release
12.19](https://www.postgresql.org/docs/12/release-12-19.html "https://www.postgresql.org/docs/12/release-12-19.html").

###### Releases and patches

- [Aurora PostgreSQL 12.19.4, March
  25, 2025](#aurorapostgresql-versions-version12194x-12194 "#aurorapostgresql-versions-version12194x-12194")
- [Aurora PostgreSQL 12.19.3, January
  23, 2025](#aurorapostgresql-versions-version12193x-12193 "#aurorapostgresql-versions-version12193x-12193")
- [Aurora PostgreSQL 12.19.2, January
  23, 2025](#aurorapostgresql-versions-version12192x-12192 "#aurorapostgresql-versions-version12192x-12192")
- [Aurora PostgreSQL 12.19.1,
  September 27, 2024](#aurorapostgresql-versions-version1219x-12191 "#aurorapostgresql-versions-version1219x-12191")
- [Aurora PostgreSQL 12.19,
  August 8, 2024](#aurorapostgresql-versions-version1219x-1219 "#aurorapostgresql-versions-version1219x-1219")

#### Aurora PostgreSQL 12.19.4, March

25, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 12.19.3, January

23, 2025

**High priority enhancements**

- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

#### Aurora PostgreSQL 12.19.2, January

23, 2025

###### Critical stability enhancements

- Fixed an issue related to Query Plan Management background worker.

###### High priority enhancements

- Fixed an issue for date functions to allow them to take into account the
  local/session timezone setting.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

**General enhancements**

- Fixed an issue where minor version upgrades with ZDP would fail resulting in
  longer upgrade times.
- Made improvements to Aurora in-Region failover which reduces database downtime
  further with faster buffer cache initialization.
- Fixed an issue that could cause an error in the wal sender process when
  resuming logical replication.

#### Aurora PostgreSQL 12.19.1,

September 27, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache
  instances while upgrading into this version.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL 12.19,

August 8, 2024

###### New features

- Introduced a feature to capture database downtime metrics during upgrades and
  restarts.

###### General enhancements

- Improved Aurora PostgreSQL performance for generative AI workloads using
  `pgvector`.
- Fixed issue where minor version upgrades with ZDP would fail in some cases
  resulting in longer upgrade times.
- Fixed a bug where JDBC connections may not be preserved during ZDP enabled
  upgrades.
- Fixed an issue that caused two-phase commit files to remain, preventing proper
  cleanup.
- Improved memory handling while processing two phase commit files.
- Improved availability of Aurora read replicas.

###### High priority enhancements

- Fixed an issue which leads to cancellation of long-running queries on Global
  Database replica instances.

###### Critical stability enhancements

- Fixed a pg_repack issue that would incorrectly allow two vacuum processes to
  operate concurrently on the same table.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` extension to version 4.9.4.
  - `pg_cron` extension to version 1.6.2.
  - `pg_partman` extension to version 5.1.0.
  - `pg_repack` extension to version 1.5.0.
  - `pg_tle` to version 1.4.0.
  - `pg_vector` extension to version 0.7.0.
  - `pgrouting` extension to version 3.6.2.
  - `pgTap` extension to version 1.3.2.
  - `PostGIS` extension to version 3.4.2.
  - `RDKit` extension to version 2024_03_1.

### PostgreSQL 12.18 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.18. For more
information about the improvements in PostgreSQL 12.18, see [PostgreSQL release 12.18](https://www.postgresql.org/docs/12/release-12-18.html "https://www.postgresql.org/docs/12/release-12-18.html").

###### Releases and patches

- [Aurora PostgreSQL 12.18.4, February 02, 2025](#aurorapostgresql-versions-version12184x-12184 "#aurorapostgresql-versions-version12184x-12184")
- [Aurora PostgreSQL 12.18.3, October 7, 2024](#aurorapostgresql-versions-version1218x-12183 "#aurorapostgresql-versions-version1218x-12183")
- [Aurora PostgreSQL 12.18.2, June 20, 2024](#AuroraPostgreSQL.Updates.20180305.12182 "#AuroraPostgreSQL.Updates.20180305.12182")
- [Aurora PostgreSQL 12.18.1, April 29, 2024](#AuroraPostgreSQL.Updates.20180305.1218 "#AuroraPostgreSQL.Updates.20180305.1218")

#### Aurora PostgreSQL 12.18.4, February 02, 2025

**Critical stability enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

**High priority enhancements**

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing to
  rebuild their mirror clusters.
- Fixed an issue where transactional commands may terminate the connection in some cases.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418")
  for V8 Engine in the `PLV8` extension.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").

- **General enhancements**

Fixed an ownership issue where the postgis_raster extension could not be updated correctly
from a previous the `PostGIS` extension v2 installation.

#### Aurora PostgreSQL 12.18.3, October 7, 2024

###### General enhancements

- Fixed an issue that would cause ZDP to fail on Aurora Optimized Reads Cache instances while upgrading into this version.

###### High priority enhancements

- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.18.2, June 20, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed an issue with background worker where it may crash when executed in parallel worker context.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed issues in how two-phase commit files are handled.

####

Aurora PostgreSQL 12.18.1, April 29, 2024

###### New features

- Added resource usage summary to `pg_dump`.

###### General enhancements

- Fixed multiple minor version upgrade issues to improve connection preservation with zero-downtime patching.
- Reduced database boot time due to improved initialization time for large volumes.
- Introduced faster COPY operations by reducing contention on the relation extension lock and proactively extending relations.
- Improvements to reduce replication lag by intelligently skipping the replay of certain log records, thereby reducing the replay load.
- Fixed an issue during recovery conflict on a read node which, in rare cases, could cause brief unavailability.
- Fixed an issue where a database would fail to startup during a major version upgrade patch, in rare scenarios.
- Improved availability of read replicas by allowing recovery from replication errors in more situations.
- Fixed an issue that would cause zero-downtime patching to timeout.
- Fixed a logical replication decoding issue that fails to process catalog modifying changes after spilling to storage
  if there was a concurrent aborted sub-transaction.
- Improved log record validation before it is written to storage.
- Fixed an issue that would result in sessions incorrectly reporting ClientRead wait events after a zero-downtime patching event.
- Fixed an ambiguous function definition of aws_s3.query_export_to_s3 when upgrading the aws_s3 extension from version 1.1 to 1.2.

###### High priority enhancements

- Fixed an issue related to resuming a logical replication slot where, in rare cases, it could cause the slot to become stuck.
- Fixed an issue that would result in a restart when creating a database in a tablespace.
- Fixed an issue related to incorrect logical replication error handling to improve DB stability.

###### Critical stability enhancements

- Fixed an issue related to replication origins that in rare cases might result in longer recovery time and impact availability.
- Fixed an issue that in rare cases may cause transactions to be partially replicated by newly created logical replication slots. For more information, see
  [Potential data loss due to race condition during logical replication slot creation](https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com "https://www.postgresql.org/message-id/29273AF3-9684-4069-9257-D05090B03B99%40amazon.com").
- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.

###### Additional improvements and enhancements

- Updated the following extensions:
  - `pg_tle` extension to version 1.3.4.
  - `PLV8` extension to version 3.1.10.
  - RDKit Cartridge to version Release_2023_09_4.

- New GUC Parameters has been added
  - `pgtle.clientauth_databases_to_skip`
  - `pgtle.clientauth_db_name`
  - `pgtle.clientauth_num_parallel_workers`
  - `pgtle.clientauth_users_to_skip`
  - `pgtle.enable_clientauth`
  - `pgtle.passcheck_db_name`

### PostgreSQL 12.17 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.17. For more
information about the improvements in PostgreSQL 12.17, see [PostgreSQL release 12.17](https://www.postgresql.org/docs/15/release-12-17.html "https://www.postgresql.org/docs/15/release-12-17.html").

###### Releases and patches

- [Aurora PostgreSQL 12.17.6, February 5 2025](#aurorapostgresql-versions-version12176x-12176 "#aurorapostgresql-versions-version12176x-12176")
- [Aurora PostgreSQL 12.17.5, September 17, 2024](#aurorapostgresql-versions-version1217x-12175 "#aurorapostgresql-versions-version1217x-12175")
- [Aurora PostgreSQL 12.17.4, June 24, 2024](#AuroraPostgreSQL.Updates.20180305.12174 "#AuroraPostgreSQL.Updates.20180305.12174")
- [Aurora PostgreSQL 12.17.3, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12173 "#AuroraPostgreSQL.Updates.20180305.12173")
- [Aurora PostgreSQL 12.17.2, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.12172 "#AuroraPostgreSQL.Updates.20180305.12172")
- [Aurora PostgreSQL 12.17.0, December 21, 2023](#AuroraPostgreSQL.Updates.20180305.12170 "#AuroraPostgreSQL.Updates.20180305.12170")

#### Aurora PostgreSQL 12.17.6, February 5 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 12.17.5, September 17, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.17.4, June 24, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue with Parallel query execution in which a backend may get into indefinite hang in certain cases.
- Fixed a crash with execution of pltsql user defined functions.
- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

####

Aurora PostgreSQL 12.17.3, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

####

Aurora PostgreSQL 12.17.2, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.17.0, December 21, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition to support
PostgreSQL versions 15.5, 14.10, 13.13, and 12.17. These releases contain product improvements and bug fixes made by the PostgreSQL community,
along with Aurora-specific improvements. New features and improvements for Babelfish for Aurora PostgreSQL version 3.4 are also included.

Refer to the Aurora version policy to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder,
if you are running any version of Amazon Aurora PostgreSQL version 11, you must upgrade to a newer major version by February 29, 2024.

###### New features

- Amazon Bedrock integration – By using the Amazon Aurora machine learning extension with your Aurora PostgreSQLDB cluster, you can now use Amazon Bedrock
  foundational AI models.
- Delegated Extension Support – This feature allows delegating extension management to lower privileged user with the new rds_extension role.
- Query Plan Management (QPM) enhancements – Plan outlines will be updated to the latest format version as part of the `update_plan_hash`
  action for `apg_plan_mgmt.validate_plans()`.
- Added support for the `HypoPG` extension at version 1.4.0.
- Added support for the `h3-pg` extension and the `h3-postgis` extension at version 4.1.3.

###### High priority enhancements

- Fixed an issue which may cause an Aurora replica to reboot when reading a page which was modified during `WAL` replay
- Fixed an issue where if a specific volume metadata is invalid on a source cluster, it will remain invalid on a cloned cluster. Since the
  clone cluster uses a new volume, the metadata will now be recreated.
- Fixed an issue which could, in rare cases, lead to an engine unavailable condition following a minor or patch version upgrade
- Fixed a bug that may cause an engine crash during zero-downtime patching (ZDP)
- Introduced a new parameter, `rds.enable_memory_management`, which is used to enable and disable the improved memory management feature.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General enhancements

- Fixed an issue which may cause an Aurora replica to reboot while reconnecting with the writer DB instance.
- Added support for the `rdkit.morgan_fp_size` parameter
- Fixed an issue which may cause unused `WAL` segements to not be properly removed
- Fixed an issue where `pglogical` does not correctly pass-through replication origin data when using the binary output format
- Fixed a crash in `dblink` and `postgres_fdw` extensions due to invalid connections
- Fixed an issue where the `aws_s3` extension can import `HTTP` error responses into the table

###### Additional improvements and enhancements

- Updated the following extensions:
  - `mysql_fdw` to version 2.9.1
  - `Oracle_fdw` to version 2.6.0
  - `Orafce` to version 4.6.0
  - `pg_cron` to version 1.6.0
  - `pg_hint_plan` to version 1.3.9
  - `pg_proctab` to version 0.0.10
  - `plv8` to version 3.1.8
  - `PostGIS` to version 3.4.0
  - `prefix` to version 1.2.10
  - `RDKit` to version 4.4.0 (Release_2023_09_1)

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
12](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12").

### PostgreSQL 12.16 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.16. For more
information about the improvements in PostgreSQL 12.16, see [PostgreSQL release 12.16](https://www.postgresql.org/docs/12/release-12-16.html "https://www.postgresql.org/docs/12/release-12-16.html").

###### Releases and patches

- [Aurora PostgreSQL 12.16.9, February 27 2025](#aurorapostgresql-versions-version12169x-12169 "#aurorapostgresql-versions-version12169x-12169")
- [Aurora PostgreSQL 12.16.8, November 14, 2024](#aurorapostgresql-versions-version1216x-12168 "#aurorapostgresql-versions-version1216x-12168")
- [Aurora PostgreSQL 12.16.7, June 25, 2024](#AuroraPostgreSQL.Updates.20180305.12167 "#AuroraPostgreSQL.Updates.20180305.12167")
- [Aurora PostgreSQL 12.16.6, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12166 "#AuroraPostgreSQL.Updates.20180305.12166")
- [Aurora PostgreSQL 12.16.5, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.12165 "#AuroraPostgreSQL.Updates.20180305.12165")
- [Aurora PostgreSQL 12.16.2, December 13, 2023](#AuroraPostgreSQL.Updates.20180305.12162 "#AuroraPostgreSQL.Updates.20180305.12162")
- [Aurora PostgreSQL 12.16.1, November 09, 2023](#AuroraPostgreSQL.Updates.20180305.12161 "#AuroraPostgreSQL.Updates.20180305.12161")
- [Aurora PostgreSQL 12.16.0, October 24, 2023](#AuroraPostgreSQL.Updates.20180305.12160 "#AuroraPostgreSQL.Updates.20180305.12160")

#### Aurora PostgreSQL 12.16.9, February 27 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue in Global DB switchover and failover that can result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 12.16.8, November 14, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.16.7, June 25, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail resulting in longer upgrade times.

###### High priority enhancements

- Fixed an issue which led to cancellation of long-running queries on Global Database replica instances.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor version upgrade can cause zero-downtime patching and engine startup to fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.

####

Aurora PostgreSQL 12.16.6, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8` extension.

####

Aurora PostgreSQL 12.16.5, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.16.2, December 13, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.16.1, November 09, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 12.16.0, October 24, 2023

###### New features

- Added support for `mysql_fdw` version 2.9.0
- Added support in the `aws_s3` extension for exporting to an S3 bucket encrypted with a customer managed KMS key
- Improved the availability of Aurora replicas in the global DB secondary clusters
- Added support for query plan capture on Aurora replicas
- Allowed query plans under a given cost threshold to not be captured

###### General enhancements

- Fixed an issue in the `aws_s3` extension where the number of rows exported is incorrectly reported when the total number exceeds 2 billion
- Provided options to configure timeouts in the `aws_s3` extension. By setting the following parameters (GUCs), customers will now be able to
  change the timeout thresholds for imports from S3:
  - `aws_s3.curlopt_low_speed_limit`
  - `aws_s3.curlopt_low_speed_time`

- Improved the performance of replay of commit transaction operations on Aurora replicas
- Fixed an issue where, in rare cases, an import from the `aws_s3` extension fails to complete
- Updated the GEOS library for PostGIS to version 3.12.0
- Added the `WAIT_EVENT_Aurora_CLUSTER_CACHE_MANAGER_SENDER` wait event to denote wait times in the cluster cache manager sender
- Added the `WAIT_EVENT_Aurora_SERVERLESS_MONITORING_MAIN` wait event to denote wait times in Aurora Serverless resource monitoring
- Fixed an issue where the database may crash during the start of a logical replication slot
- Increased the limit for `pg_cron` `cron.max_running_jobs` parameter from 100 to 1000

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` to version 4.3.0
  - `pg_logical` to version 2.4.3
  - `pgvector` to version 0.5.0
  - `plv8` to version 3.1.6
  - `PostGIS` to version 3.3.3
  - `RDKit` to version 4.3

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
12](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12").

### PostgreSQL 12.15 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.15. For more
information about the improvements in PostgreSQL 12.15, see [PostgreSQL release 12.15](https://www.postgresql.org/docs/15/release-12-15.html "https://www.postgresql.org/docs/15/release-12-15.html").

###### Releases and patches

- [Aurora PostgreSQL 12.15.8, February 24 2025](#aurorapostgresql-versions-version12158x-12158 "#aurorapostgresql-versions-version12158x-12158")
- [Aurora PostgreSQL 12.15.7, November 12, 2024](#aurorapostgresql-versions-version1215x-12157 "#aurorapostgresql-versions-version1215x-12157")
- [Aurora PostgreSQL 12.15.6, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.12156 "#AuroraPostgreSQL.Updates.20180305.12156")
- [Aurora PostgreSQL 12.15.5, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12155 "#AuroraPostgreSQL.Updates.20180305.12155")
- [Aurora PostgreSQL 12.15.4, December 14, 2023](#AuroraPostgreSQL.Updates.20180305.12154 "#AuroraPostgreSQL.Updates.20180305.12154")
- [Aurora PostgreSQL 12.15.3, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.12153 "#AuroraPostgreSQL.Updates.20180305.12153")
- [Aurora PostgreSQL 12.15.2, October 4, 2023](#AuroraPostgreSQL.Updates.20180305.12152 "#AuroraPostgreSQL.Updates.20180305.12152")
- [Aurora PostgreSQL 12.15.0, July 13, 2023](#AuroraPostgreSQL.Updates.20180305.12150 "#AuroraPostgreSQL.Updates.20180305.12150")

#### Aurora PostgreSQL 12.15.8, February 24 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream` extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue for date functions to allow them to take into account the local/session
  timezone setting.
- Fixed an issue in Global DB switchover and failover that could result in customers needing
  to rebuild their mirror clusters.
- Fixed
  [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for
  V8 Engine in the `PLV8` extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not be updated correctly
  from a previous the PostGIS extension v2 installation.

#### Aurora PostgreSQL 12.15.7, November 12, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.15.6, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 12.15.5, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.15.4, December 14, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.15.3, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 12.15.2, October 4, 2023

###### High priority stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica.
- Fixed an issue that would cause a crash when executing the `COPY FROM` command.
- Fixed an issue that would cause high CPU usage and prevent new connections.
- Fixed an issue where `UPDATE` and `DELETE` from a table with foreign key could fail unexpectedly with "ERROR: 40001: could not serialize access due to concurrent update when using Serializable snapshot".

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.
- Updated the `plv8`, `pll`, and `plcoffee` extensions to version 2.3.15.
- Fixed an issue that prevented the enablement of improved memory management in certain scenarios in Aurora PostgreSQL 15.3.

####

Aurora PostgreSQL 12.15.0, July 13, 2023

Following the announcement of updates to the PostgreSQL database by the open source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition
to support PostgreSQL versions 15.3, 14.8, 13.11, 12.15, and 11.20. These releases contains product improvements and bug fixes made by
the PostgreSQL community, along with Aurora-specific improvements. The releases also contain new features and improvements for
[Babelfish for Aurora PostgreSQL version 3.2](AuroraBabelfish.md "AuroraBabelfish.md"), and improved support for
[AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish"). Refer to the [Amazon Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md")
to help you to decide how often to upgrade and how to plan your upgrade process. As a reminder, if you are running any version of Amazon Aurora PostgreSQL 11,
you must upgrade to a newer major version by February 29, 2024.

###### New features

- This release contains memory management improvements which increase database stability and availability by proactively
  preventing issues caused by insufficient memory. For more information, see [Improved memory management in Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md "../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md").
- Added support for the `pgvector` extension version 0.4.1.

###### High priority enhancements

- Fixed an issue with the subtransaction metadata handling when performing a survivable reader reconnect.
- Fixed an issue during ZDP which is related to the extension environment variables.
- Addressed a transient error during logical replication that caused a process to incorrectly calculate that it had encountered an unexpected page.
- Fixed an issue which causes a period of unavailability due to a partially created replication origin state file.

###### General enhancements

- Added a new function, `aurora_stat_memctx_usage()`, to show backend memory use breakdown at a Postgres memory context level.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue with the calculation of the `AuroraReplicaLag` metric.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Further reduced the database downtime during ZDP.
- Fixed a bug which can cause unavailability during ZDP.
- Fixed an issue which caused `pg_ls_waldir()` to return "ERROR: could not stat file".
- Added support for TLS 1.3 with ciphers TLS_AES_128_GCM_SHA256 and TLS_AES_256_GCM_SHA384.
- Addressed an issue that blocked a major version upgrade on the Aurora replica of an RDS for PostgreSQL DB instance.
- Fixed an issue in the `pg_vector` extension where, in rare cases, infinite or NAN values caused a crash during the index creation
- Upgraded `GEOS` to version 3.11.2.
- Upgraded `pg_cron` to version 1.5.
- Upgraded `pg_partman` to version 4.7.3.
- Upgraded `tds_fdw` to 2.0.3.

### PostgreSQL 12.14 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.14. For more
information about the improvements in PostgreSQL 12.14, see [PostgreSQL release 12.14](https://www.postgresql.org/docs/12/release-12-14.html "https://www.postgresql.org/docs/12/release-12-14.html").

###### Releases and patches

- [Aurora PostgreSQL 12.14.9, November 6, 2024](#aurorapostgresql-versions-version1214x-12149 "#aurorapostgresql-versions-version1214x-12149")
- [Aurora PostgreSQL 12.14.8, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.12148 "#AuroraPostgreSQL.Updates.20180305.12148")
- [Aurora PostgreSQL 12.14.7, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12147 "#AuroraPostgreSQL.Updates.20180305.12147")
- [Aurora PostgreSQL 12.14.6, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.12146 "#AuroraPostgreSQL.Updates.20180305.12146")
- [Aurora PostgreSQL 12.14.5, November 14, 2023](#AuroraPostgreSQL.Updates.20180305.12145 "#AuroraPostgreSQL.Updates.20180305.12145")
- [Aurora PostgreSQL 12.14.4, October 5, 2023](#AuroraPostgreSQL.Updates.20180305.12144 "#AuroraPostgreSQL.Updates.20180305.12144")
- [Aurora PostgreSQL 12.14.3, July 24, 2023](#AuroraPostgreSQL.Updates.20180305.12143 "#AuroraPostgreSQL.Updates.20180305.12143")
- [Aurora PostgreSQL 12.14.2, May 10, 2023](#AuroraPostgreSQL.Updates.20180305.12142 "#AuroraPostgreSQL.Updates.20180305.12142")
- [Aurora PostgreSQL 12.14.1, April 5, 2023](#AuroraPostgreSQL.Updates.20180305.12141 "#AuroraPostgreSQL.Updates.20180305.12141")

#### Aurora PostgreSQL 12.14.9, November 6, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.14.8, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 12.14.7, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Fixed an issue that would cause a logical replication slot to transiently error out in the presence of aborted subtransactions and DDL.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.14.6, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.14.5, November 14, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

###### General enhancements

- Fixed an issue that could result in read replica lag due to stale metadata
- Fixed an issue related to buffer pin locking that in rare cases can result in a crash

####

Aurora PostgreSQL 12.14.4, October 5, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.
- Updated the `plv8`, `pll`, and `plcoffee` extensions to version 2.3.15.

####

Aurora PostgreSQL 12.14.3, July 24, 2023

###### General enhancements

- Fixed an issue related to storage space reclamation following table drop or reindex or truncate operations.
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue that prevented reclaiming storage on transaction commits
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters (GUCs),
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed multiple issues which can cause Aurora replicas with the improved read availability feature to restart when reconnecting with the writer instance.
- Fixed an issue preventing a survivable reader reconnect

####

Aurora PostgreSQL 12.14.2, May 10, 2023

###### General enhancements

- Fixed an error when loading the `test_decoding` plugin in `pg_create_logical_replication_slot`.
- Updated the Oracle client used by the `oracle_fdw` extension to version 21.9.0.0.0.

####

Aurora PostgreSQL 12.14.1, April 5, 2023

###### New features

- Introduced a new QPM plan hash calculation for multi-schema support. If users want to use QPM in multi-schema
  environments, they can set the `apg_plan_mgmt.plan_hash` version to 2 and call `apg_plan_mgmt.validate_plans`('`update_plan_hash`').

###### General enhancements

- Upgraded `PROJ` support to version 9.1.0
- Upgraded the `GDAL` library in `PostGIS` to version 3.5.3
- Added support for the `TCN` and `SEG` extensions
- Fixed an issue which may increase the amount of recovery work the database does to startup with logical
  replication enabled
- Improved performance of deletes from b-tree and hash indexes on Aurora replicas
- Fixed issues that caused incorrect I/O timing metrics in `EXPLAIN`
- Fixed an issue that caused incorrect buffer hit counts in `EXPLAIN`
- Improved the engine startup time, particularly on large instances with many objects
- The Aurora function `aurora_stat_logical_wal_cache()` is now visible to all users
- Fixed an issue in QPM that could cause unavailability when enforcing plans from prepared statements

###### Additional improvements and enhancements

- Updated the following extensions:
  - `hll` to version 2.17
  - `Oracle_fdw` to version 2.5.0
  - `orafce` to version 4.0.0
  - `pg_cron` to version 1.4.2
  - `pg_hint_plan` to version 1.3.8
  - `pg_logical` to version 2.4.2
  - `pg_trgm` to version 1.4
  - `pgrouting` to version 3.4.1
  - `PostGIS` to version 3.3.2
  - `SEG` to version 1.0
  - `TCN` to version 1.0
  - `wal2json` to version 2.5

### PostgreSQL 12.13 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.13. For more
information about the improvements in PostgreSQL 12.13, see [PostgreSQL release 12.13](https://www.postgresql.org/docs/12/release-12-13.html "https://www.postgresql.org/docs/12/release-12-13.html").

###### Releases and patches

- [Aurora PostgreSQL 12.13.10, November 18, 2024](#aurorapostgresql-versions-version1213x-121310 "#aurorapostgresql-versions-version1213x-121310")
- [Aurora PostgreSQL 12.13.9, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.12139 "#AuroraPostgreSQL.Updates.20180305.12139")
- [Aurora PostgreSQL 12.13.8, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12138 "#AuroraPostgreSQL.Updates.20180305.12138")
- [Aurora PostgreSQL 12.13.7, December 15, 2023](#AuroraPostgreSQL.Updates.20180305.12137 "#AuroraPostgreSQL.Updates.20180305.12137")
- [Aurora PostgreSQL 12.13.6, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.12136 "#AuroraPostgreSQL.Updates.20180305.12136")
- [Aurora PostgreSQL 12.13.5, October 04, 2023](#AuroraPostgreSQL.Updates.20180305.12135 "#AuroraPostgreSQL.Updates.20180305.12135")
- [Aurora PostgreSQL 12.13.4, September 13, 2023](#AuroraPostgreSQL.Updates.20180305.12134 "#AuroraPostgreSQL.Updates.20180305.12134")
- [Aurora PostgreSQL 12.13.2, March 3, 2023](#AuroraPostgreSQL.Updates.20180305.12132 "#AuroraPostgreSQL.Updates.20180305.12132")
- [Aurora PostgreSQL 12.13.0, January 20, 2023](#AuroraPostgreSQL.Updates.20180305.12130 "#AuroraPostgreSQL.Updates.20180305.12130")

#### Aurora PostgreSQL 12.13.10, November 18, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.13.9, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 12.13.8, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.13.7, December 15, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.13.6, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 12.13.5, October 04, 2023

###### High priority stability enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue which can cause a database instance to restart while executing IO intensive read workloads.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.

####

Aurora PostgreSQL 12.13.4, September 13, 2023

###### General enhancements

- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue in `pg_cron` which can prevent scaling in Aurora Serverless v2
- Fixed an issue with the calculation of the `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an Amazon S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Updated the `plv8`, `plls`, and `plcoffee` extensions to version 2.3.15.

####

Aurora PostgreSQL 12.13.2, March 3, 2023

###### General stability enhancements

- Fixed an issue in `PostGIS` where the `GDAL` data wasn't loading.
- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled.
- Fixed an issue for the better error handling of procedures with large numbers of parameters.
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out.

####

Aurora PostgreSQL 12.13.0, January 20, 2023

###### High priority stability enhancements

- Fixed an issue where an upgrade fails because the oldest `MultiXactId` is updated incorrectly.
- Fixed an issue where the commit latency metrics weren't updated.
- Fixed an issue that could lead to a brief period of unavailability.

###### General stability enhancements

- Fixed an issue that caused DB instance migration failures.
- Fixed an issue where the DB fails to start because of an inconsistency in the metadata.
- Improved the error handling and diagnosability.
- Upgraded the RDKit extension to version 4.2.
- Upgraded the `GDAL` library to version 3.4.3.
- The apg_plan_mgmt.copy_outline function now copies environment_variables.
- Fixed an issue that can cause certain processes to linger in an inconsistent state during a clean shutdown.
- Fixed an issue with the pg_repack extension.
- Improved the collation library (glibc) handling with a new independent default collation library.

### PostgreSQL 12.12 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.12. For more
information about the improvements in PostgreSQL 12.12, see [PostgreSQL release 12.12](https://www.postgresql.org/docs/12/release-12-12.html "https://www.postgresql.org/docs/12/release-12-12.html").

###### Releases and patches

- [Aurora PostgreSQL 12.12.8, November 22, 2024](#aurorapostgresql-versions-version1212x-12128 "#aurorapostgresql-versions-version1212x-12128")
- [Aurora PostgreSQL 12.12.7, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.12127 "#AuroraPostgreSQL.Updates.20180305.12127")
- [Aurora PostgreSQL 12.12.6, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12126 "#AuroraPostgreSQL.Updates.20180305.12126")
- [Aurora PostgreSQL 12.12.5, December 18, 2023](#AuroraPostgreSQL.Updates.20180305.12125 "#AuroraPostgreSQL.Updates.20180305.12125")
- [Aurora PostgreSQL 12.12.4, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.12124 "#AuroraPostgreSQL.Updates.20180305.12124")
- [Aurora PostgreSQL 12.12.3, October 17, 2023](#AuroraPostgreSQL.Updates.20180305.12123 "#AuroraPostgreSQL.Updates.20180305.12123")
- [Aurora PostgreSQL 12.12.2, March 2, 2023](#AuroraPostgreSQL.Updates.20180305.12122 "#AuroraPostgreSQL.Updates.20180305.12122")
- [Aurora PostgreSQL 12.12.1, December 13, 2022](#AuroraPostgreSQL.Updates.20180305.12121 "#AuroraPostgreSQL.Updates.20180305.12121")
- [Aurora PostgreSQL 12.12.0, November 09, 2022](#AuroraPostgreSQL.Updates.20180305.12120 "#AuroraPostgreSQL.Updates.20180305.12120")

#### Aurora PostgreSQL 12.12.8, November 22, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.

####

Aurora PostgreSQL 12.12.7, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 12.12.6, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.12.5, December 18, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.12.4, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 12.12.3, October 17, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue which can cause a database instance to restart while executing I/O intensive read workloads.
- Updated the `plv8`, `pll`, and `plcoffee` extensions to version 2.3.15.

####

Aurora PostgreSQL 12.12.2, March 2, 2023

###### General stability enhancements

- Fixed an issue that increased the amount of recovery work during startup if logical replication is enabled.
- Fixed an issue for better error handling of procedures with large numbers of parameters.
- Fixed an issue with the `aws_s3` extension where loading a large number of records can time out.
- Fixed an issue with the `pg_cron` parallel running of tasks.

####

Aurora PostgreSQL 12.12.1, December 13, 2022

###### General stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades.
- Fixed an issue that could cause data inconsistency during replication.

####

Aurora PostgreSQL 12.12.0, November 09, 2022

###### General stability enhancements

- Added support for the `rds_superuser` role to execute `CREATE OPERATOR CLASS`, `REATE OPERATOR FAMILY`, and `ALTER OPERATOR FAMILY`,
  which are available in the higher versions.
- Improved buffer cache scavenging when the buffer cache is in duress.
- Fixed an issue in database activity streams that leads to high memory consumption.
- Fixed an issue that caused DB instance restarts.
- Fixed an issue where a DB instance restarts recursively while generating monitoring metrics during a crash.
- Fixed an issue where a DB instance restarted during performance metric collection.
- Fixed an issue where an attempt to connect to the database would fail with `SSLV3_ALERT_CERTIFICATE_UNKNOWN`.
- Improved the diagnostic logging around setting invalid hint bits.
- Fixed an issue where autovacuum would incorrectly skip tables.
- Improved the logical replication prefetching.
- Fixed a durability issue in the GIN indexes.
- Fixed an issue to detect and cancel stuck major version upgrades.
- Fixed an issue in hash join that could lead to increased memory consumption.
- Improved the logical replication performance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Upgraded the `GEOS` version to 3.10.3.
- Updated the `PostGIS` extension to version 3.2.3.
- Fixed an issue with `st_orientedenvelope` that caused it to loop with a 1-D input to return 0.
- Fixed an issue where the connection to SQL Server using tds_fdw fails.

### PostgreSQL 12.11 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.11. For more
information about the improvements in PostgreSQL 12.11, see [PostgreSQL release
12.11](https://www.postgresql.org/docs/12/release-12-11.html "https://www.postgresql.org/docs/12/release-12-11.html").

###### Releases and patches

- [Aurora PostgreSQL 12.11.11, November 20, 2024](#aurorapostgresql-versions-version1211x-121111 "#aurorapostgresql-versions-version1211x-121111")
- [Aurora PostgreSQL 12.11.10, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.121110 "#AuroraPostgreSQL.Updates.20180305.121110")
- [Aurora PostgreSQL 12.11.9, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12119 "#AuroraPostgreSQL.Updates.20180305.12119")
- [Aurora PostgreSQL 12.11.8, December 22, 2023](#AuroraPostgreSQL.Updates.20180305.12118 "#AuroraPostgreSQL.Updates.20180305.12118")
- [Aurora PostgreSQL 12.11.7, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.12117 "#AuroraPostgreSQL.Updates.20180305.12117")
- [Aurora PostgreSQL 12.11.6, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.12116 "#AuroraPostgreSQL.Updates.20180305.12116")
- [Aurora PostgreSQL 12.11.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.12115 "#AuroraPostgreSQL.Updates.20180305.12115")
- [Aurora PostgreSQL 12.11.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.12114 "#AuroraPostgreSQL.Updates.20180305.12114")
- [Aurora PostgreSQL 12.11.3, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.12113 "#AuroraPostgreSQL.Updates.20180305.12113")
- [Aurora PostgreSQL 12.11.1, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.12111 "#AuroraPostgreSQL.Updates.20180305.12111")
- [Aurora PostgreSQL 12.11.0, June 9, 2022](#AuroraPostgreSQL.Updates.20180305.12110 "#AuroraPostgreSQL.Updates.20180305.12110")

#### Aurora PostgreSQL 12.11.11, November 20, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.
- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

####

Aurora PostgreSQL 12.11.10, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

###### General enhancements

- Fixed issue where minor version upgrades with ZDP would fail resulting in longer upgrade times.

####

Aurora PostgreSQL 12.11.9, March 13, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer failover.
- Fixed an issue where active transactions during logical replication slot creation may be partially replicated by the slot.

####

Aurora PostgreSQL 12.11.8, December 22, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.11.7, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 12.11.6, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension could fail to import from an S3 bucket with a name containing dots.
- Provided options to configure the timeouts within the `aws_lambda` extension. By setting the following parameters,
  customers will now be able to change the connect and request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Updated the `plv8`, `pll`, and `plcoffee` extensions to version 2.3.15.

####

Aurora PostgreSQL 12.11.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experiences stability issues during database minor and patch release upgrades.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Fixed an issue that could cause data inconsistency during replication.

####

Aurora PostgreSQL 12.11.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.

####

Aurora PostgreSQL 12.11.3, October 13, 2022

###### High priority stability enhancements

- Fixed a `PLV8` issue where the base parameter doesn't get loaded properly into the memory.

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the relfilenode.
- Fixed a stuck scaling issue when the current scaling event times out.
- Upgraded the `PostGIS` extension to version 3.1.7.
- Fixed an issue where extended query messages might be lost during zero-downtime patching (ZDP) causing the extended query to hang after the ZDP completion.

####

Aurora PostgreSQL 12.11.1, July 6, 2022

###### Critical stability enhancements

- Fixed an issue that could cause periods of unavailability during a storage node restart.

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue when the connection to SQL Server fails using the `TDS_FDW` extension to query a foreign table.
- Fixed an issue that caused connections using the provided root certificate to fail.
- Improved the diagnostic and supportability information in case of inconsistent B-tree index entries.

####

Aurora PostgreSQL 12.11.0, June 9, 2022

###### New features

- Added support for the `large object` module (extension). For more information,
  see [Managing large objects with the lo module](../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md "../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md").
- Added support for zero-downtime patching (ZDP) for minor version upgrades and patches. For more information, see
  [Minor
  release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor")
  in the _Amazon Aurora User Guide_.

###### Critical updates

- Fixed a replay crash due to an LSN mismatch.
- Fixed the `aws_s3` extension to prevent invalid region injection.

###### High stability updates

- Fixed multiple issues related to out-of-memory conditions which could result in brief periods of unavailability.

###### General stability updates

- Fixed a lock contention crash during an Aurora Serverless v1 scaling event.
- Fixed an issue where logical replication becomes stuck after a restart.
- Fixed multiple issues that could lead to brief periods of unavailability.
- Fixed a crash in `pg_cron` due to a task still running but being unscheduled.
- Fixed, during redo, an invalid page hit on the Generic Redo for GENERIC_XLOG_FULL_PAGE_DATA.
  This happens due to a timing hole between generating the log record and then writing the metadata
  for the record on the RW node and the RO node replays between those operations.
- Improved the query performance by supporting parallel workers.
- Upgraded the plugin `wal2json` version to 2.4.
- Upgraded the `pglogical` extension to version 2.4.1.

### PostgreSQL 12.10 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.10. For more
information about the improvements in PostgreSQL 12.10, see [PostgreSQL release
12.10](https://www.postgresql.org/docs/13/release-12-10.html "https://www.postgresql.org/docs/13/release-12-10.html").

###### Releases and patches

- [Aurora PostgreSQL 12.10.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.12106 "#AuroraPostgreSQL.Updates.20180305.12106")
- [Aurora PostgreSQL 12.10.4, July 18, 2022](#AuroraPostgreSQL.Updates.20180305.12104 "#AuroraPostgreSQL.Updates.20180305.12104")
- [Aurora PostgreSQL 12.10.1, April 27, 2022](#AuroraPostgreSQL.Updates.20180305.12101 "#AuroraPostgreSQL.Updates.20180305.12101")
- [Aurora PostgreSQL 12.10.0, March 29, 2022](#AuroraPostgreSQL.Updates.20180305.12100 "#AuroraPostgreSQL.Updates.20180305.12100")

####

Aurora PostgreSQL 12.10.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Updated the `PostGIS` extension to version 3.1.7.

####

Aurora PostgreSQL 12.10.4, July 18, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others
  omit "security restricted operation". For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files that could result in periods of unavailability.
- Fixed a defect where the validation of cached plans may lead to a database restart when the plan was previously invalidated.

####

Aurora PostgreSQL 12.10.1, April 27, 2022

###### High priority stability enhancements

- Fixed an issue that could cause incorrect `WriteIOPS` reporting in the AWS console.
- Fixed an issue that could cause unavailability after removal of a read node from a cluster.

###### General enhancements

- Fixed an issue that could cause an engine restart during periods of low free memory.

####

Aurora PostgreSQL 12.10.0, March 29, 2022

###### High priority stability enhancements

- Fixed multiple issues that may result in unavailability of a read node.
- Fixed an issue that may result in a read node being unable to replay WAL requiring the replication slot to be dropped and resynchronized.
- Fixed an issue that could cause excess storage use due to files not being properly closed.

###### General enhancements

- Fixed a small memory leak on read nodes when `commit_ts` is set.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".
- Fixed an issue that could cause an import from Amazon S3 to fail when using the `aws_s3` extension.
- Fixed multiple issues that could result in periods of unavailability when using `apg_plan_mgmt`.
- Fixed multiple issues that could result in periods of unavailability when QPM is enabled.

### PostgreSQL 12.9

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.9. For more
information about the improvements in PostgreSQL 12.9, see [PostgreSQL release
12.9](https://www.postgresql.org/docs/12/release-12-9.html "https://www.postgresql.org/docs/12/release-12-9.html").

###### Releases and patches

- [Aurora PostgreSQL 12.9.18, January 15th, 2026](#aurorapostgresql-versions-version12918x-12918 "#aurorapostgresql-versions-version12918x-12918")
- [Aurora PostgreSQL 12.9.16, June 18, 2025](#aurorapostgresql-versions-version12916x-12916 "#aurorapostgresql-versions-version12916x-12916")
- [Aurora PostgreSQL 12.9.15 April 29, 2025](#aurorapostgresql-versions-version12915x-12915 "#aurorapostgresql-versions-version12915x-12915")
- [Aurora PostgreSQL 12.9.13, November 22, 2024](#aurorapostgresql-versions-version129x-12913 "#aurorapostgresql-versions-version129x-12913")
- [Aurora PostgreSQL 12.9.12, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.12912 "#AuroraPostgreSQL.Updates.20180305.12912")
- [Aurora PostgreSQL 12.9.11, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.12911 "#AuroraPostgreSQL.Updates.20180305.12911")
- [Aurora PostgreSQL 12.9.10, December 27, 2023](#AuroraPostgreSQL.Updates.20180305.12910 "#AuroraPostgreSQL.Updates.20180305.12910")
- [Aurora PostgreSQL 12.9.9, November 17, 2023](#AuroraPostgreSQL.Updates.20180305.1299 "#AuroraPostgreSQL.Updates.20180305.1299")
- [Aurora PostgreSQL 12.9.8, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.1298 "#AuroraPostgreSQL.Updates.20180305.1298")
- [Aurora PostgreSQL 12.9.7, August 24, 2023](#AuroraPostgreSQL.Updates.20180305.1297 "#AuroraPostgreSQL.Updates.20180305.1297")
- [Aurora PostgreSQL 12.9.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.1296 "#AuroraPostgreSQL.Updates.20180305.1296")
- [Aurora PostgreSQL 12.9.4, July 20, 2022](#AuroraPostgreSQL.Updates.20180305.1294 "#AuroraPostgreSQL.Updates.20180305.1294")
- [Aurora PostgreSQL 12.9.3, April 13, 2022](#AuroraPostgreSQL.Updates.20180305.1293 "#AuroraPostgreSQL.Updates.20180305.1293")
- [Aurora PostgreSQL 12.9.1](#AuroraPostgreSQL.Updates.20180305.1291 "#AuroraPostgreSQL.Updates.20180305.1291")
- [Aurora PostgreSQL 12.9.0](#AuroraPostgreSQL.Updates.20180305.1290 "#AuroraPostgreSQL.Updates.20180305.1290")

#### Aurora PostgreSQL 12.9.18, January 15th, 2026

###### Critical stability enhancements

- Fixed a security issue when altering routine ownership.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").

  [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").

  [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

  [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

###### General stability enhancements

- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.

#### Aurora PostgreSQL 12.9.16, June 18, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the improved reader availability functionality that might result in longer recover times and impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.

#### Aurora PostgreSQL 12.9.15 April 29, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL 12.9.13, November 22, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when `rds.enable_plan_management` is turned on, but apg_plan_mgmt extension is not installed.
- Fixed issues where the replication of vacuum operations may cause a restart when handling conflicts with user queries.

####

Aurora PostgreSQL 12.9.12, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

####

Aurora PostgreSQL 12.9.11, March 13, 2024

###### General stability enhancements

- Allow `rds_superuser` to terminate backends which are not explicitly associated with a role.
- Upgraded `PLV8` extension to version 2.3.15.

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed an issue where active transactions during slot creation may be partially replicated by the slot.
- Fixed a deadlock issue in Aurora storage which can result in writer failover.

####

Aurora PostgreSQL 12.9.10, December 27, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by someone other than the table owner

####

Aurora PostgreSQL 12.9.9, November 17, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

- Fixed an issue related to `pg_cron` background worker processes

####

Aurora PostgreSQL 12.9.8, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-41862](https://nvd.nist.gov/vuln/detail/CVE-2022-41862 "https://nvd.nist.gov/vuln/detail/CVE-2022-41862")

####

Aurora PostgreSQL 12.9.7, August 24, 2023

###### General enhancements

- Fixed an issue which causes the stats collector process to repeatedly restart.
- Fixed an issue preventing `pglogical` from logging conflicting rows during the apply phase.

####

Aurora PostgreSQL 12.9.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.
- Updated the `PostGIS` extension to version 3.1.7.

####

Aurora PostgreSQL 12.9.4, July 20, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others
  omit "security restricted operation". For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files that could result in periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".

####

Aurora PostgreSQL 12.9.3, April 13, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

###### General enhancements

- Fixed a bug that could cause an engine restart during periods of low free memory.

####

Aurora PostgreSQL 12.9.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to 3.1.5.
  This update contains a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 12.9.0

###### Critical stability enhancements

- Fixed a bug where logical replication may hang resulting in the replay falling behind on the read node. The instance may eventually restart.

###### Additional improvements and enhancements

- Fixed a buffer cache bug that could cause brief periods of unavailability.
- Fixed a bug in the `apg_plan_mgmt` extension where an index based plan was not being enforced.
- Fixed a bug in the `pg_logical` extension that could cause brief periods of unavailability due to improper handling of NULL arguments.
- Fixed an issue where orphaned files caused major version upgrades to fail.
- Fixed incorrect Aurora Storage Daemon log write metrics.
- Fixed multiple bugs that could result in WAL replay falling behind and eventually causing the reader instances to restart.
- Improved the Aurora buffer cache page validation on reads.
- Improved the Aurora storage metadata validation.
- Updated the `pg_cron` extension to v1.4.
- Updated the `pg_hint_pan` extension to v1.3.7.

- For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
  12](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.12").

### PostgreSQL 12.8 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.8. For more
information about the improvements in PostgreSQL 12.8, see [PostgreSQL release
12.8](https://www.postgresql.org/docs/12/release-12-8.html "https://www.postgresql.org/docs/12/release-12-8.html").

###### Releases and patches

- [Aurora PostgreSQL 12.8.6, December 19, 2022](#AuroraPostgreSQL.Updates.20180305.1286 "#AuroraPostgreSQL.Updates.20180305.1286")
- [Aurora PostgreSQL 12.8.4, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.1284 "#AuroraPostgreSQL.Updates.20180305.1284")
- [Aurora PostgreSQL 12.8.2, April 12, 2022](#AuroraPostgreSQL.Updates.20180305.1282 "#AuroraPostgreSQL.Updates.20180305.1282")
- [Aurora PostgreSQL 12.8.1](#AuroraPostgreSQL.Updates.20180305.1281 "#AuroraPostgreSQL.Updates.20180305.1281")
- [Aurora PostgreSQL 12.8.0](#AuroraPostgreSQL.Updates.20180305.1280 "#AuroraPostgreSQL.Updates.20180305.1280")

####

Aurora PostgreSQL 12.8.6, December 19, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 12.8.4, July 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### General enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that could cause Performance Insights to display "Unknown wait event".
- Fixed an issue that could result in periods of unavailability due to the existence of duplicate relation files.

####

Aurora PostgreSQL 12.8.2, April 12, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

###### General enhancements

- Fixed a buffer cache bug that could cause brief periods of unavailability.

####

Aurora PostgreSQL 12.8.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to 3.1.5.
  This update contains a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL 12.8.0

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major
  version update with the message: "PANIC: could not access status of next
  transaction id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue which can cause vacuum operations to become blocked after all Aurora read replicas have been removed from a secondary cluster.
- Fixed an issue where read nodes restart due to a replication origin cache lookup failure.
- Fixed an issue where read queries may time out on read nodes during the replay of lazy truncation triggered by vacuum on the write node.
- Fixed an issue that causes Performance Insights to incorrectly set the backend type of a database connection.
- Fixed an issue where the aurora_postgres_replica_status() function returned stale or lagging CPU stats.
- Fixed an issue where the role `rds_superuser` did not have permission to execute the `pg_stat_statements_reset()` function.
- Fixed an issue with the `apg_plan_mgmt` extension where the planning and execution times were reported as 0.
- Removed support for the DES, 3DES, and RC4 cipher suites.
- Updated `PostGIS` extension to version 3.1.4.

### PostgreSQL 12.7,

Aurora PostgreSQL 4.2 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.7. For more
information about the improvements in PostgreSQL 12.7, see [PostgreSQL release
12.7](https://www.postgresql.org/docs/12/release-12-7.html "https://www.postgresql.org/docs/12/release-12-7.html").

###### Releases and patches

- [Aurora PostgreSQL 12.7.5, December 30, 2022](#AuroraPostgreSQL.Updates.20180305.1275 "#AuroraPostgreSQL.Updates.20180305.1275")
- [Aurora PostgreSQL 12.7.4, July 14, 2022](#AuroraPostgreSQL.Updates.20180305.1274 "#AuroraPostgreSQL.Updates.20180305.1274")
- [Aurora PostgreSQL 4.2.3, April 7, 2022](#AuroraPostgreSQL.Updates.20180305.423 "#AuroraPostgreSQL.Updates.20180305.423")
- [Aurora PostgreSQL 4.2.2](#AuroraPostgreSQL.Updates.20180305.422 "#AuroraPostgreSQL.Updates.20180305.422")
- [Aurora PostgreSQL 4.2.1](#AuroraPostgreSQL.Updates.20180305.127 "#AuroraPostgreSQL.Updates.20180305.127")
- [Aurora PostgreSQL 4.2.0](#AuroraPostgreSQL.Updates.20180305.420 "#AuroraPostgreSQL.Updates.20180305.420")

####

Aurora PostgreSQL 12.7.5, December 30, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when the monitoring agent is unavailable.

####

Aurora PostgreSQL 12.7.4, July 14, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552: Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait event".

####

Aurora PostgreSQL 4.2.3, April 7, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 4.2.2

###### Security enhancements

- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory disclosure in certain queries”. For more information,
  see [CVE-2021-3677](https://www.postgresql.org/support/security/CVE-2021-3677 "https://www.postgresql.org/support/security/CVE-2021-3677")
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to PostGIS 3.0.3.
  This is a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL 4.2.1

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major version
  update with the message: "PANIC: could not access status of next transaction
  id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue where read nodes restart due to a replication origin cache lookup failure.
- Fixed an issue with the `apg_plan_mgmt` extension where planning and execution time were reported as 0.
- Fixed an issue that causes Performance Insights to incorrectly set the backend type of a database connection.
- Fixed an issue with the `apg_plan_mgmt` extension where plan outline on a partitioned table did not enforce an index-based plan.
- Fixed an issue where orphaned files caused failed translations in read codepaths during or after major version upgrade.
- Fixed multiple issues in the Aurora storage daemon that could lead to brief periods of unavailability when specific network configurations are used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that leads to writer node restart. This also reduces the overall system memory consumption.

####

Aurora PostgreSQL 4.2.0

###### New features

- Added support for the `oracle_fdw` extension version 2.3.0.

###### High priority stability enhancements

- Fixed an issue where creating a database from an existing
  template database with tablespace resulted in an error with
  the message `ERROR: could not open file pg_tblspc/...: No such file or directory`.
- Fixed an issue where, in rare cases, an Aurora replica may be unable to start when a
  large number of PostgreSQL subtransactions (i.e. SQL savepoints) have been used.
- Fixed an issue where, in rare circumstances, read results may be inconsistent for repeated read
  requests on replica nodes.

###### Additional improvements and enhancements

- Upgraded OpenSSL to 1.1.1k.
- Reduced CPU usage and memory consumption of the WAL apply process on Aurora replicas for some workloads.
- Improved safety checks in the write path to detect incorrect writes to metadata.
- Improved security by removing 3DES and other older ciphers for SSL/TLS connections.
- Fixed an issue where a duplicate file entry can prevent the Aurora PostgreSQL engine from starting up.
- Fixed an issue that could cause temporary unavailability under heavy workloads.
- Added back ability to use a leading forward slash in the Amazon S3 path during S3 import.
- Added Graviton support for oracle_fdw extension version 2.3.0.
- Changed the following extensions:
  - Updated the `orafce` extension to version 3.16.
  - Updated the `pg_partman` extension to version 4.5.1.
  - Updated the `pg_cron` extension to version 1.3.1.
  - Updated the `postgis` extension to version 3.0.3.

### PostgreSQL 12.6,

Aurora PostgreSQL 4.1 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.6. For more
information about the improvements in PostgreSQL 12.6, see [PostgreSQL release
12.6](https://www.postgresql.org/docs/12/release-12-6.html "https://www.postgresql.org/docs/12/release-12-6.html").

###### Releases and patches

- [Aurora PostgreSQL 4.1.2, April 7, 2022](#AuroraPostgreSQL.Updates.20180305.412 "#AuroraPostgreSQL.Updates.20180305.412")
- [Aurora PostgreSQL 4.1.1](#AuroraPostgreSQL.Updates.20180305.411 "#AuroraPostgreSQL.Updates.20180305.411")
- [Aurora PostgreSQL 4.1.0](#AuroraPostgreSQL.Updates.20180305.410 "#AuroraPostgreSQL.Updates.20180305.410")

####

Aurora PostgreSQL 4.1.2, April 7, 2022

###### Security enhancements

- Additional modifications to the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

####

Aurora PostgreSQL 4.1.1

###### Security enhancements

- Modified the `pg_cron` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security issue during create extension. The issue was addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue during create extension. The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory disclosure in certain queries”. For more information,
  see [CVE-2021-3677](https://www.postgresql.org/support/security/CVE-2021-3677 "https://www.postgresql.org/support/security/CVE-2021-3677")
- Backpatched [pg_partman](https://github.com/pgpartman/pg_partman/commit/0b6565ad378c358f8a6cd1d48ddc482eb7f854d3 "https://github.com/pgpartman/pg_partman/commit/0b6565ad378c358f8a6cd1d48ddc482eb7f854d3") to 4.4.0. This is a `pg_partman` fix for
  the vulnerability addressed in core PostgreSQL by CVE-2020-14350. For more
  information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to `PostGIS` 3.0.2.
  This is a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw` extension function parameters.

####

Aurora PostgreSQL 4.1.0

###### New features

- Added support for the following extensions:
  - The `pg_proctab` extension version 0.0.9
  - The `pg_partman` extension version 4.4.0. For more information, see
    [Managing PostgreSQL partitions with the pg_partman extension](../AuroraUserGuide/PostgreSQL_Partitions.md "../AuroraUserGuide/PostgreSQL_Partitions.md")
    in the _Amazon Aurora User Guide_.
  - The `pg_cron` extension version 1.3.0. For more information, see
    [Scheduling maintenance with the PostgreSQL pg_cron extension](../AuroraUserGuide/PostgreSQL_pg_cron.md "../AuroraUserGuide/PostgreSQL_pg_cron.md")
    in the _Amazon Aurora User Guide_.
  - The `pg_bigm` extension version 1.2

###### High priority stability enhancements

- Fixed a bug in the `pglogical` extension that could lead to
  data inconsistency for inbound replication.
- Fixed a bug where in rare cases a reader had inconsistent results when it restarted while a transaction
  with more than 64 subtransactions was being processed.
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2021-32027](https://nvd.nist.gov/vuln/detail/CVE-2021-32027 "https://nvd.nist.gov/vuln/detail/CVE-2021-32027")
  - [CVE-2021-32028](https://nvd.nist.gov/vuln/detail/CVE-2021-32028 "https://nvd.nist.gov/vuln/detail/CVE-2021-32028")
  - [CVE-2021-32029](https://nvd.nist.gov/vuln/detail/CVE-2021-32029 "https://nvd.nist.gov/vuln/detail/CVE-2021-32029")

###### Additional improvements and enhancements

- Fixed a bug where the database could not be started when there were
  many relations in memory-constrained environments.
- Fixed a bug in the
  `apg_plan_mgmt` extension that could cause brief periods
  of unavailability due to an internal buffer overflow.
- Fixed a bug on reader nodes that could
  cause brief periods of unavailability during WAL replay.
- Fixed a bug in the
  `rds_activity_stream` extension that caused an error
  during startup when attempting to log audit events.
- Fixed bugs in the
  `aurora_replica_status` function where rows were
  sometimes partially populated and some values such as Replay Latency,
  and CPU usage were always 0.
- Fixed a bug where the database engine would attempt to create shared
  memory segments larger than the instance total memory and fail
  repeatedly. For example, attempts to create 128 GiB shared buffers on a
  db.r5.large instance would fail. With this change, requests for total
  shared memory allocations larger than the instance memory allow setting
  the instance to incompatible parameters.
- Added logic to clean up unnecessary
  `pg_wal` temporary files on a database startup.
- Fixed a bug that could lead to
  outbound replication synchronization errors after a major version
  upgrade.
- Fixed a bug that reported
  \*\*`ERROR: rds_activity_stream stack item 2 not found on top

* cannot pop`** when attempting to create the
`rds_activity_stream` extension.

- Fixed a bug that could cause the error
  **`failed to build any 3-way joins`** in a
  correlated `IN` subquery under an `EXISTS`
  subquery.
- Backported the following performance
  improvement from the PostgreSQL community: [pg_stat_statements: add missing check for
  pgss_enabled()](https://github.com/postgres/postgres/commit/6f40ee4f837ec1ac59c8ddc73b67a04978a184d "https://github.com/postgres/postgres/commit/6f40ee4f837ec1ac59c8ddc73b67a04978a184d").
- Fixed a bug that could cause upgrades
  to Aurora PostgreSQL 12.x to fail due to the inability to open the
  `pg_control` file.
- Fixed a bug that could cause brief
  periods of unavailability due to running out of memory when creating the
  `postgis` extension with `pgAudit`
  enabled.
- Backported the following bug fix from
  the PostgreSQL community: [Fix use-after-free bug with
  AfterTriggersTableData.storeslot](https://github.com/postgres/postgres/commit/262eb990c72097bd804e5c747fe38bf9b3a1ded9 "https://github.com/postgres/postgres/commit/262eb990c72097bd804e5c747fe38bf9b3a1ded9").
- Fixed a bug when using outbound
  logical replication to synchronize changes to another database that
  could fail with an error message like **`ERROR: could not map
filenode "base/16395/228486645" to relation OID`**.
- Fixed a bug that could cause a brief
  period of unavailability when canceling a transaction.
- Fixed a bug that caused no ICU
  collations to be shown in the `pg_collation` catalog table
  after creating a new Aurora PostgreSQL 12.x instance. This issue does not
  affect upgrading from an older version.
- Fixed a bug where the
  `rds_ad` role wasn't created after upgrading from a
  version of Aurora PostgreSQL that doesn't support Microsoft Active
  Directory authentication.
- Added btree page checks to detect
  tuple metadata inconsistency.
- Fixed a bug in asynchronous buffer
  reads that could cause brief periods of unavailability on reader nodes
  during WAL replay.
- Fixed a bug where reading a TOAST
  value from disk could cause a brief period of unavailability.
- Fixed a bug that caused brief periods
  of unavailability when attempting to fetch a tuple from and index
  scan.

### PostgreSQL 12.4,

Aurora PostgreSQL 4.0 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 12.4. For more
information about the improvements in PostgreSQL 12.4, see [PostgreSQL release
12.4](https://www.postgresql.org/docs/12/release-12-4.html "https://www.postgresql.org/docs/12/release-12-4.html").

###### Releases and patches

- [Aurora PostgreSQL 4.0.5](#AuroraPostgreSQL.Updates.20180305.405 "#AuroraPostgreSQL.Updates.20180305.405")
- [Aurora PostgreSQL 4.0.2](#AuroraPostgreSQL.Updates.20180305.402 "#AuroraPostgreSQL.Updates.20180305.402")
- [Aurora PostgreSQL 4.0.1](#AuroraPostgreSQL.Updates.20180305.401 "#AuroraPostgreSQL.Updates.20180305.401")
- [Aurora PostgreSQL 4.0.0](#AuroraPostgreSQL.Updates.20180305.400 "#AuroraPostgreSQL.Updates.20180305.400")

####

Aurora PostgreSQL 4.0.5

- Modified the `ip4r` extension to mitigate a security issue during create extension.
  The issue was originally disclosed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory disclosure in certain queries”.
  For more information, see [CVE-2021-3677](https://www.postgresql.org/support/security/CVE-2021-3677 "https://www.postgresql.org/support/security/CVE-2021-3677")
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to `PostGIS` 3.0.2.
  This is a `PostGIS` fix for the vulnerability addressed in core PostgreSQL by CVE-2020-14350.
  For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw` extension function parameters.

####

Aurora PostgreSQL 4.0.2

###### High priority stability enhancements

- Fixed a bug where a reader node might render an extra or missing row
  if the reader restarted while the writer node is processing a long
  transaction with more than 64 subtransactions.
- Fixed a bug that can cause vacuum to block on GiST indexes.
- Fixed a bug where after upgrade to PostgreSQL 12, vacuum can fail on
  the system table `pg_catalog.pg_shdescription` with the
  following error. **`ERROR: found xmin 484 from before
relfrozenxid`**

###### Additional improvements and enhancements

- Fixed a bug that could lead to intermittent unavailability due to a
  race condition when handling responses from storage nodes.
- Fixed a bug that could lead to intermittent unavailability due to the
  rotation of network encryption keys.
- Fixed a bug that could lead to intermittent unavailability due to heat
  management of the underlying storage segments.
- Fixed a bug where a large Amazon S3 import with thousands of clients can
  cause one or more of the import clients to stop responding.
- Removed a restriction that prevented setting configuration variable
  strings that contained `brazil`.
- Fixed a bug that could lead to intermittent unavailability if a reader
  node runs a query that access many tables while the writer node is
  acquiring exclusive locks on all of the same tables.

####

Aurora PostgreSQL 4.0.1

###### New features

- This release adds support for the Graviton2 db.r6g instance classes
  to the PostgreSQL engine version 12.4. For more information, see [Supported DB engines for DB instance classes](../AuroraUserGuide/Concepts.md#Concepts.DBInstanceClass.SupportAurora "../AuroraUserGuide/Concepts.md#Concepts.DBInstanceClass.SupportAurora")
  in the _Amazon Aurora User Guide_.

###### Critical stability enhancements

- Fixed a bug that caused a read replica to unsuccessfully restart
  repeatedly in rare cases.
- Fixed a bug where a cluster became unavailable when attempting to
  create more than 16 read replicas or Aurora global database secondary
  AWS Regions. The cluster became available again when the new read
  replica or secondary AWS Region was removed.

###### Additional improvements and enhancements

- Fixed a bug that when under heavy load, snapshot import, COPY import,
  or Amazon S3 import stopped responding in rare cases.
- Fixed a bug where a read replica might not join the cluster when the
  writer was very busy with a write-intensive workload.
- Fixed a bug where a cluster could be unavailable briefly when a
  high-volume Amazon S3 import was running.
- Fixed a bug that caused a cluster to take several minutes to restart
  if a logical replication stream was terminated while handling many
  complex transactions.
- Fixed the Just-in-Time (JIT) compilation, which was incorrectly
  enabled by default in Aurora PostgreSQL 4.0.0.
- Disallowed the use of both AWS Identity and Access Management (IAM) and Kerberos authentication for the
  same user.

####

Aurora PostgreSQL 4.0.0

###### New features

- This version supports a major version upgrade from
  [PostgreSQL 11.7,
  Aurora PostgreSQL 3.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.32 "#AuroraPostgreSQL.Updates.20180305.32")
  and later versions.

###### Additional improvements and enhancements

- Contains several improvements that were announced for PostgreSQL
  releases [12.0](https://www.postgresql.org/docs/12/release-12.html "https://www.postgresql.org/docs/12/release-12.html"), [12.1](https://www.postgresql.org/docs/12/release-12-1.html "https://www.postgresql.org/docs/12/release-12-1.html"), [12.2](https://www.postgresql.org/docs/12/release-12-2.html "https://www.postgresql.org/docs/12/release-12-2.html"), [12.3](https://www.postgresql.org/docs/12/release-12-3.html "https://www.postgresql.org/docs/12/release-12-3.html"), and [12.4](https://www.postgresql.org/docs/12/release-12-4.html "https://www.postgresql.org/docs/12/release-12-4.html").
- Contains all fixes, features, and improvements present in [PostgreSQL 11.9,
  Aurora PostgreSQL 3.4](#AuroraPostgreSQL.Updates.20180305.34 "#AuroraPostgreSQL.Updates.20180305.34") .
- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
  - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
  - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

- Updated the following extensions:
  - `address_standardizer` to version 3.0.2
  - `address_standardizer_data_us` to version 3.0.2
  - `amcheck` to version 1.2
  - `citext` to version 1.6
  - `hll` to version 2.14
  - `hstore` to version 1.6
  - `ip4r` to version 2.4
  - `pg_repack` to version 1.4.5
  - `pg_stat_statements` to version 1.7
  - `pgaudit` to version 1.4
  - `pglogical` to version 2.3.2
  - `pgrouting` to version 3.0.3
  - `plv8` to version 2.3.14
  - `postGIS` to version 3.0.2
  - `postgis_tiger_geocoder` to version 3.0.2
  - `postgis_topology` to version 3.0.2

## PostgreSQL 11 versions (includes

some deprecated versions)

###### Version updates

- [PostgreSQL 11.21](#AuroraPostgreSQL.Updates.20180305.1121X "#AuroraPostgreSQL.Updates.20180305.1121X")
- [PostgreSQL 11.20
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1120X "#AuroraPostgreSQL.Updates.20180305.1120X")
- [PostgreSQL 11.19
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1119X "#AuroraPostgreSQL.Updates.20180305.1119X")
- [PostgreSQL 11.18
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1118X "#AuroraPostgreSQL.Updates.20180305.1118X")
- [PostgreSQL 11.17
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1117X "#AuroraPostgreSQL.Updates.20180305.1117X")
- [PostgreSQL 11.16
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1116X "#AuroraPostgreSQL.Updates.20180305.1116X")
- [PostgreSQL 11.15
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1115X "#AuroraPostgreSQL.Updates.20180305.1115X")
- [PostgreSQL 11.14
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1114 "#AuroraPostgreSQL.Updates.20180305.1114")
- [PostgreSQL 11.13
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1113 "#AuroraPostgreSQL.Updates.20180305.1113")
- [PostgreSQL 11.12,
  Aurora PostgreSQL 3.6 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.36 "#AuroraPostgreSQL.Updates.20180305.36")
- [PostgreSQL 11.11,
  Aurora PostgreSQL 3.5 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.35 "#AuroraPostgreSQL.Updates.20180305.35")
- [PostgreSQL 11.9,
  Aurora PostgreSQL 3.4](#AuroraPostgreSQL.Updates.20180305.34 "#AuroraPostgreSQL.Updates.20180305.34")
- [PostgreSQL 11.8,
  Aurora PostgreSQL 3.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.33 "#AuroraPostgreSQL.Updates.20180305.33")
- [PostgreSQL 11.7,
  Aurora PostgreSQL 3.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.32 "#AuroraPostgreSQL.Updates.20180305.32")
- [PostgreSQL 11.6,
  Aurora PostgreSQL 3.1 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.31 "#AuroraPostgreSQL.Updates.20180305.31")
- [PostgreSQL 11.4,
  Aurora PostgreSQL 3.0 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.30 "#AuroraPostgreSQL.Updates.20180305.30")

### PostgreSQL 11.21

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.21. For more
information about the improvements in PostgreSQL 11.21, see [PostgreSQL release
11.21](https://www.postgresql.org/docs/11/release-11-21.html "https://www.postgresql.org/docs/11/release-11-21.html").

###### Releases and patches

- [Aurora PostgreSQL 11.21.12, January 14, 2026](#aurorapostgresql-versions-version112112x-112112 "#aurorapostgresql-versions-version112112x-112112")
- [Aurora PostgreSQL 11.21.11, August 5, 2025](#aurorapostgresql-versions-version112111x-112111 "#aurorapostgresql-versions-version112111x-112111")
- [Aurora PostgreSQL
  11.21.10, May 7, 2025](#aurorapostgresql-versions-version112110x-112110 "#aurorapostgresql-versions-version112110x-112110")
- [Aurora PostgreSQL 11.21.9,
  February 27 2025](#aurorapostgresql-versions-version11219x-11219 "#aurorapostgresql-versions-version11219x-11219")
- [Aurora PostgreSQL
  11.21.8, November 14, 2024](#aurorapostgresql-versions-version1121x-11218 "#aurorapostgresql-versions-version1121x-11218")
- [Aurora PostgreSQL
  11.21.7, June 25, 2024](#AuroraPostgreSQL.Updates.20180305.11217 "#AuroraPostgreSQL.Updates.20180305.11217")
- [Aurora PostgreSQL
  11.21.6, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.11216 "#AuroraPostgreSQL.Updates.20180305.11216")
- [Aurora PostgreSQL
  11.21.5, February 22, 2024](#AuroraPostgreSQL.Updates.20180305.11215 "#AuroraPostgreSQL.Updates.20180305.11215")
- [Aurora PostgreSQL
  11.21.2, December 13, 2023](#AuroraPostgreSQL.Updates.20180305.11212 "#AuroraPostgreSQL.Updates.20180305.11212")
- [Aurora PostgreSQL
  11.21.1, November 09, 2023](#AuroraPostgreSQL.Updates.20180305.11211 "#AuroraPostgreSQL.Updates.20180305.11211")
- [Aurora PostgreSQL
  11.21.0, October 24, 2023](#AuroraPostgreSQL.Updates.20180305.11210 "#AuroraPostgreSQL.Updates.20180305.11210")

#### Aurora PostgreSQL 11.21.12, January 14, 2026

**Critical stability enhancements**

- Fixed an issue where engine minor and patch upgrade takes few seconds longer downtime due to runtime process not exiting gracefully.
- Fixed an issue related to Optimized Reads-enabled tiered cache functionality that might result in longer recovery times after a failover to Aurora replica instances.
- Fixed a security issue when altering routine ownership.

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").

  [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").

  [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

  [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2022-1364](https://nvd.nist.gov/vuln/detail/CVE-2022-1364 "https://nvd.nist.gov/vuln/detail/CVE-2022-1364").
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

**General enhancements**

- Fixed an issue that could cause unavailability when `apg_plan_mgmt` is enabled.
- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.
- Fixed an issue with prolonged Serverless v2 scaling.

#### Aurora PostgreSQL 11.21.11, August 5, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the
  improved reader availability functionality that might result in longer recover times and
  impact availability.
- Fixed an issue in the rds_activity_stream extension that could cause brief periods of
  unavailability during configuration reloads and when maximum connections are consumed.

**General enhancements**

- Fixed an issue in the read replica deletion which could result in a vacuum being held back
  and causing eventual unavailability of database.
- Added support of newly released Regions for the aws_s3 extension.
- Fixed an issue where unexpected internal communication channel re-establishments may cause
  increased latency on data processing.

#### Aurora PostgreSQL

11.21.10, May 7, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

**General enhancements**

- Fixed an issue on the replica where a network interruption may not
  correctly re-establish connection with the writer.

#### Aurora PostgreSQL 11.21.9,

February 27 2025

**Critical Priority enhancements**

- Fixed a security issue in the `rds_activity_stream`
  extension.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-10979](https://nvd.nist.gov/vuln/detail/CVE-2024-10979 "https://nvd.nist.gov/vuln/detail/CVE-2024-10979").
  - [CVE-2024-10978](https://nvd.nist.gov/vuln/detail/CVE-2024-10978 "https://nvd.nist.gov/vuln/detail/CVE-2024-10978").
  - [CVE-2024-10977](https://nvd.nist.gov/vuln/detail/CVE-2024-10977 "https://nvd.nist.gov/vuln/detail/CVE-2024-10977").
  - [CVE-2024-10976](https://nvd.nist.gov/vuln/detail/CVE-2024-10976 "https://nvd.nist.gov/vuln/detail/CVE-2024-10976").

- Fixed an issue in Global DB switchover and failover that can result in
  customers needing to rebuild their mirror clusters.
- Fixed [CVE-2020-6418](https://nvd.nist.gov/vuln/detail/cve-2020-6418 "https://nvd.nist.gov/vuln/detail/cve-2020-6418") for V8 Engine in the `PLV8`
  extension.

**General enhancements**

- Fixed an ownership issue where the postgis_raster extension could not
  be updated correctly from a previous the PostGIS extension v2
  installation.

#### Aurora PostgreSQL

11.21.8, November 14, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when
  `rds.enable_plan_management` is turned on, but
  apg_plan_mgmt extension is not installed.
- Backported fixes for the following PostgreSQL community security
  issue:
  - [CVE-2024-7348](https://nvd.nist.gov/vuln/detail/CVE-2024-7348 "https://nvd.nist.gov/vuln/detail/CVE-2024-7348")

#### Aurora PostgreSQL

11.21.7, June 25, 2024

###### General enhancements

- Fixed multiple issues where minor version upgrades with ZDP would fail
  resulting in longer upgrade times.
- Fixed an issue which prevented upgrading older PostGIS 2.4
  installations to version 3.3.3.

###### Critical stability enhancements

- Fixed an issue where a change in memory requirements during a minor
  version upgrade can cause zero-downtime patching and engine startup to
  fail.
- Fixed a pg_repack issue causing two vacuums to concurrently process
  the same table.

#### Aurora PostgreSQL

11.21.6, March 13, 2024

###### General enhancements

- Fixed a performance degradation issue in `PLV8`
  extension.

#### Aurora PostgreSQL

11.21.5, February 22, 2024

###### General enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.

###### High priority enhancements

- Fixed an issue where `pg_stat_statements` can block minor
  version upgrade during ZDP.
- Fixed an issue where a logical replication slot would no longer emit
  changes due to an overly strict data consistency check.
- Backported fixes for the following PostgreSQL community security
  issue:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed a deadlock issue in Aurora Storage which can result in writer
  failover.
- Fixed an issue where active transactions during logical replication
  slot creation may be partially replicated by the slot.

#### Aurora PostgreSQL

11.21.2, December 13, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by
  someone other than the table owner

#### Aurora PostgreSQL

11.21.1, November 09, 2023

###### Critical stability enhancements

- Backported a fix for the following security issue:
  - [CVE-2023-38545](https://nvd.nist.gov/vuln/detail/CVE-2023-38545 "https://nvd.nist.gov/vuln/detail/CVE-2023-38545")

#### Aurora PostgreSQL

11.21.0, October 24, 2023

###### New features

- Added support in the `aws_s3` extension for exporting to an
  S3 bucket encrypted with a customer managed KMS key

###### General enhancements

- Fixed an issue in the `aws_s3` extension where the number
  of rows exported is incorrectly reported when the total number exceeds 2
  billion
- Provided options to configure timeouts in the `aws_s3`
  extension. By setting the following parameters (GUCs), customers will
  now be able to change the timeout thresholds for imports from S3:
  - `aws_s3.curlopt_low_speed_limit`
  - `aws_s3.curlopt_low_speed_time`

- Improved the performance of replay of commit transaction operations on
  Aurora replicas
- Fixed an issue where, in rare cases, an import from the
  `aws_s3` extension fails to complete
- Updated the GEOS library for PostGIS to version 3.12.0
- Added the `WAIT_EVENT_Aurora_CLUSTER_CACHE_MANAGER_SENDER`
  wait event to denote wait times in the cluster cache manager
  sender
- Added the `WAIT_EVENT_Aurora_SERVERLESS_MONITORING_MAIN`
  wait event to denote wait times in Aurora Serverless resource
  monitoring
- Fixed an issue where the database may crash during the start of a
  logical replication slot

###### Additional improvements and enhancements

- Updated the following extensions:
  - `orafce` to version 4.3.0
  - `pg_logical` to version 2.4.3
  - `plv8` to version 3.1.6
  - `PostGIS` to version 3.3.3
  - `RDKit` to version 4.3

For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
11](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.11 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.11").

### PostgreSQL 11.20

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.20. For more
information about the improvements in PostgreSQL 11.20, see [PostgreSQL release
11.20](https://www.postgresql.org/docs/11/release-11-20.html "https://www.postgresql.org/docs/11/release-11-20.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.20.2, October 4, 2023](#AuroraPostgreSQL.Updates.20180305.11202 "#AuroraPostgreSQL.Updates.20180305.11202")
- [Aurora PostgreSQL
  11.20.0, July 13, 2023](#AuroraPostgreSQL.Updates.20180305.11200 "#AuroraPostgreSQL.Updates.20180305.11200")

#### Aurora PostgreSQL

11.20.2, October 4, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security
  issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while
  executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked
  after the restart of an Aurora replica.
- Fixed an issue that would cause a crash when executing the `COPY
FROM` command.
- Fixed an issue that would cause high CPU usage and prevent new
  connections.
- Fixed an issue where `UPDATE` and `DELETE` from
  a table with foreign key could fail unexpectedly with "ERROR: 40001:
  could not serialize access due to concurrent update when using
  Serializable snapshot".

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.
- Updated the `plv8`, `pll`, and
  `plcoffee` extensions to version 2.3.15.
- Fixed an issue that prevented the enablement of improved memory
  management in certain scenarios in Aurora PostgreSQL 15.3.

#### Aurora PostgreSQL

11.20.0, July 13, 2023

Following the announcement of updates to the PostgreSQL database by the open
source community, we have updated Amazon Aurora PostgreSQL-Compatible Edition to support PostgreSQL
versions 15.3, 14.8, 13.11, 12.15, and 11.20. These releases contains product
improvements and bug fixes made by the PostgreSQL community, along with
Aurora-specific improvements. The releases also contain new features and
improvements for [Babelfish for Aurora PostgreSQL version
3.2](AuroraBabelfish.md "AuroraBabelfish.md"), and improved support for [AWS Database Migration Service](../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish "../../../dms/latest/userguide/CHAP_Target.md#CHAP_Target.PostgreSQL.Babelfish"). Refer to the [Amazon
Aurora versions](../AuroraUserGuide/Aurora.md "../AuroraUserGuide/Aurora.md") to help you to decide how often to upgrade and how to
plan your upgrade process. As a reminder, if you are running any version of
Amazon Aurora PostgreSQL 11, you must upgrade to a newer major version by February 29, 2024.

###### New features

- This release contains memory management improvements which increase
  database stability and availability by proactively preventing issues
  caused by insufficient memory. For more information, see [Improved memory management in Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md "../AuroraUserGuide/AuroraPostgreSQL.BestPractices.memory.md").

###### High priority enhancements

- Fixed an issue during ZDP which is related to the extension
  environment variables.
- Addressed a transient error during logical replication that caused a
  process to incorrectly calculate that it had encountered an unexpected
  page.
- Fixed an issue which causes a period of unavailability due to a
  partially created replication origin state file.

###### General enhancements

- Added a new function, `aurora_stat_memctx_usage()`, to show
  backend memory use breakdown at a Postgres memory context level.
- Provided options to configure the timeouts within the
  `aws_lambda` extension. By setting the following
  parameters (GUCs), customers will now be able to change the connect and
  request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue with the calculation of the
  `AuroraReplicaLag` metric.
- Fixed an issue where, in rare cases, the `aws_s3` extension
  could fail to import from an Amazon S3 bucket with a name containing
  dots.
- Further reduced the database downtime during ZDP.
- Fixed a bug which can cause unavailability during ZDP.
- Fixed an issue which caused `pg_ls_waldir()` to return
  "ERROR: could not stat file".
- Added support for TLS 1.3 with ciphers TLS_AES_128_GCM_SHA256 and
  TLS_AES_256_GCM_SHA384.
- Addressed an issue that blocked a major version upgrade on the Aurora
  replica of an RDS for PostgreSQL DB instance.
- Upgraded `GEOS` to version 3.11.2.
- Upgraded `tds_fdw` to 2.0.3.

### PostgreSQL 11.19

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.19. For more
information about the improvements in PostgreSQL 11.19, see [PostgreSQL release
11.19](https://www.postgresql.org/docs/12/release-11-19.html "https://www.postgresql.org/docs/12/release-11-19.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.19.4, October 5, 2023](#AuroraPostgreSQL.Updates.20180305.11194 "#AuroraPostgreSQL.Updates.20180305.11194")
- [Aurora PostgreSQL
  11.19.3, July 24, 2023](#AuroraPostgreSQL.Updates.20180305.11193 "#AuroraPostgreSQL.Updates.20180305.11193")
- [Aurora PostgreSQL
  11.19.2, May 10, 2023](#AuroraPostgreSQL.Updates.20180305.11192 "#AuroraPostgreSQL.Updates.20180305.11192")
- [Aurora PostgreSQL
  11.19.1, April 5, 2023](#AuroraPostgreSQL.Updates.20180305.11191 "#AuroraPostgreSQL.Updates.20180305.11191")

#### Aurora PostgreSQL

11.19.4, October 5, 2023

###### Critical stability enhancements

- Backported a fix for the following PostgreSQL community security
  issue:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")

###### High priority enhancements

- Fixed an issue which can cause a database instance to restart while
  executing I/O intensive read workloads.
- Fixed an issue which can cause vacuum operations to become blocked
  after the restart of an Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new
  connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.
- Updated the `plv8`, `pll`, and
  `plcoffee` extensions to version 2.3.15.

#### Aurora PostgreSQL

11.19.3, July 24, 2023

###### General enhancements

- Fixed an issue related to storage space reclamation following table
  drop or reindex or truncate operations.
- Fixed an issue with the calculation of the
  `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue that prevented reclaiming storage on transaction
  commits
- Fixed an issue preventing `pglogical` from logging
  conflicting rows during the apply phase
- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue where, in rare cases, the `aws_s3` extension
  could fail to import from an Amazon S3 bucket with a name containing
  dots.
- Provided options to configure the timeouts within the
  `aws_lambda` extension. By setting the following
  parameters (GUCs), customers will now be able to change the connect and
  request timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed multiple issues which can cause Aurora replicas with the improved
  read availability feature to restart when reconnecting with the writer
  instance.
- Fixed an issue preventing a survivable reader reconnect.

#### Aurora PostgreSQL

11.19.2, May 10, 2023

###### General enhancements

- Fixed an error when loading the `test_decoding` plugin in
  `pg_create_logical_replication_slot`.

#### Aurora PostgreSQL

11.19.1, April 5, 2023

###### General enhancements

- Upgraded `PROJ` support to version 9.1.0
- Upgraded the `GDAL` library in `PostGIS` to
  version 3.5.3
- Added support for the `TCN` and `SEG`
  extensions
- Fixed an issue which may increase the amount of recovery work the
  database does to startup with logical replication enabled
- Fixed issues that caused incorrect I/O timing metrics in
  `EXPLAIN`
- Fixed an issue that caused incorrect buffer hit counts in
  `EXPLAIN`
- Improved the engine startup time, particularly on large instances with
  many objects
- The Aurora function `aurora_stat_logical_wal_cache()` is now
  visible to all users

###### Additional improvements and enhancements

- Updated the following extensions:
  - `hll` to version 2.17
  - `orafce` to version 4.0.0
  - `pg_hint_plan` to version 1.3.8
  - `pg_logical` to version 2.4.2
  - `pg_trgm` to version 1.4
  - `pgrouting` to version 3.4.1
  - `PostGIS` to version 3.3.2
  - `SEG` to version 1.0
  - `TCN` to version 1.0
  - `wal2json` to version 2.5

### PostgreSQL 11.18

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.18. For more
information about the improvements in PostgreSQL 11.18, see [PostgreSQL release
11.18](https://www.postgresql.org/docs/11/release-11-18.html "https://www.postgresql.org/docs/11/release-11-18.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.18.5, October 04, 2023](#AuroraPostgreSQL.Updates.20180305.11185 "#AuroraPostgreSQL.Updates.20180305.11185")
- [Aurora PostgreSQL
  11.18.4, September 13, 2023](#AuroraPostgreSQL.Updates.20180305.11184 "#AuroraPostgreSQL.Updates.20180305.11184")
- [Aurora PostgreSQL
  11.18.2, March 3, 2023](#AuroraPostgreSQL.Updates.20180305.11182 "#AuroraPostgreSQL.Updates.20180305.11182")
- [Aurora PostgreSQL
  11.18.0, January 20, 2023](#AuroraPostgreSQL.Updates.20180305.11180 "#AuroraPostgreSQL.Updates.20180305.11180")

#### Aurora PostgreSQL

11.18.5, October 04, 2023

###### High priority stability enhancements

- Fixed an issue which can cause a database instance to restart while
  executing IO intensive read workloads.
- Fixed an issue that would cause high CPU usage and prevent new
  connections.

###### General enhancements

- Introduced diagnostics for the transient metadata used for I/O.

#### Aurora PostgreSQL

11.18.4, September 13, 2023

###### General enhancements

- Added Aurora Serverless v2 scaling enhancements
- Fixed an issue with the calculation of the
  `AuroraReplicaLag` metric
- Fixed a bug which can cause unavailability during ZDP
- Fixed an issue preventing `pglogical` from logging
  conflicting rows during the apply phase
- Fixed an issue where, in rare cases, the `aws_s3` extension
  could fail to import from an Amazon S3 bucket with a name containing
  dots.
- Provided options to configure the timeouts within the
  `aws_lambda` extension. By setting the following
  parameters, customers will now be able to change the connect and request
  timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Updated the `plv8`, `plls`, and
  `plcoffee` extensions to version 2.3.15.

#### Aurora PostgreSQL

11.18.2, March 3, 2023

###### General stability enhancements

- Fixed an issue in `PostGIS` where the `GDAL`
  data wasn't loading.
- Fixed an issue that increased the amount of recovery work during
  startup if logical replication is enabled.
- Fixed an issue for the better error handling of procedures with large
  numbers of parameters.
- Fixed an issue with the `aws_s3` extension where loading a
  large number of records can time out.

#### Aurora PostgreSQL

11.18.0, January 20, 2023

###### High priority stability enhancements

- Fixed an issue where an upgrade fails because the oldest
  `MultiXactId` is updated incorrectly.
- Fixed an issue where the commit latency metrics weren't updated.
- Fixed an issue that could lead to a brief period of unavailability.

###### General stability enhancements

- Fixed an issue that caused DB instance migration failures.
- Fixed an issue where the DB fails to start because of an
  inconsistency in the metadata.
- Improved the error handling and diagnosability.
- Upgraded the RDKit extension to version 4.2.
- Upgraded the `GDAL` library to version 3.4.3.
- Fixed an issue with the pg_repack extension.
- Improved the collation library (glibc) handling with a new
  independent default collation library.

### PostgreSQL 11.17

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.17. For more
information about the improvements in PostgreSQL 11.17, see [PostgreSQL release
11.17](https://www.postgresql.org/docs/11/release-11-17.html "https://www.postgresql.org/docs/11/release-11-17.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.17.3, October 17, 2023](#AuroraPostgreSQL.Updates.20180305.11173 "#AuroraPostgreSQL.Updates.20180305.11173")
- [Aurora PostgreSQL
  11.17.2, March 2, 2023](#AuroraPostgreSQL.Updates.20180305.11172 "#AuroraPostgreSQL.Updates.20180305.11172")
- [Aurora PostgreSQL
  11.17.1, December 13, 2022](#AuroraPostgreSQL.Updates.20180305.11171 "#AuroraPostgreSQL.Updates.20180305.11171")
- [Aurora PostgreSQL
  11.17.0, November 09, 2022](#AuroraPostgreSQL.Updates.20180305.11170 "#AuroraPostgreSQL.Updates.20180305.11170")

#### Aurora PostgreSQL

11.17.3, October 17, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an
  Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new
  connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly
  restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging
  conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension
  could fail to import from an S3 bucket with a name containing
  dots.
- Provided options to configure the timeouts within the
  `aws_lambda` extension. By setting the following
  parameters, customers will now be able to change the connect and request
  timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Fixed an issue which can cause a database instance to restart while
  executing I/O intensive read workloads.
- Updated the `plv8`, `pll`, and
  `plcoffee` extensions to version 2.3.15.

#### Aurora PostgreSQL

11.17.2, March 2, 2023

###### General stability enhancements

- Fixed an issue that increased the amount of recovery work during
  startup if logical replication is enabled.
- Fixed an issue for better error handling of procedures with large
  numbers of parameters.
- Fixed an issue with the `aws_s3` extension where loading a
  large number of records can time out.

#### Aurora PostgreSQL

11.17.1, December 13, 2022

###### General stability enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.
- Fixed an issue where the engine experiences stability issues during
  database minor and patch release upgrades.
- Fixed an issue that could cause data inconsistency during
  replication.

#### Aurora PostgreSQL

11.17.0, November 09, 2022

###### General stability enhancements

- Improved buffer cache scavenging when the buffer cache is in duress.
- Fixed an issue in Database Activity Streams that leads to high memory
  consumption.
- Fixed an issue that caused DB instance restarts.
- Fixed an issue where a DB instance restarts recursively while
  generating monitoring metrics during a crash.
- Fixed an issue where a DB instance restarted during performance
  metric collection.
- Fixed an issue where an attempt to connect to the database would fail
  with SSLV3_ALERT_CERTIFICATE_UNKNOWN.
- Improved the diagnostic logging around setting invalid hint bits.
- Fixed an issue where autovacuum would incorrectly skip tables.
- Improved the logical replication prefetching.
- Fixed a durability issue in the GIN indexes.
- Fixed an issue to detect and cancel stuck major version upgrades.
- Fixed an issue in hash join that could lead to increased memory
  consumption.
- Improved the logical replication performance.
- Fixed an issue that causes database activity stream inconsistency
  when the monitoring agent is unavailable.
- Upgraded the `GEOS` version to 3.10.3.
- Updated the `PostGIS` extension to version 3.2.3.
- Fixed an issue with `st_orientedenvelope` that caused it
  to loop with a 1-D input to return 0.
- Fixed an issue where the connection to SQL Server using tds_fdw
  fails.

### PostgreSQL 11.16

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.16. For more
information about the improvements in PostgreSQL 11.16, see [PostgreSQL release
11.16](https://www.postgresql.org/docs/13/release-11-16.html "https://www.postgresql.org/docs/13/release-11-16.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.16.6, October 19, 2023](#AuroraPostgreSQL.Updates.20180305.11166 "#AuroraPostgreSQL.Updates.20180305.11166")
- [Aurora PostgreSQL
  11.16.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.11165 "#AuroraPostgreSQL.Updates.20180305.11165")
- [Aurora PostgreSQL
  11.16.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.11164 "#AuroraPostgreSQL.Updates.20180305.11164")
- [Aurora PostgreSQL
  11.16.3, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.11163 "#AuroraPostgreSQL.Updates.20180305.11163")
- [Aurora PostgreSQL
  11.16.1, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.11161 "#AuroraPostgreSQL.Updates.20180305.11161")
- [Aurora PostgreSQL
  11.16.0, June 9, 2022](#AuroraPostgreSQL.Updates.20180305.11160 "#AuroraPostgreSQL.Updates.20180305.11160")

#### Aurora PostgreSQL

11.16.6, October 19, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

###### High priority enhancements

- Fixed an issue which blocked vacuum operations after the restart of an
  Aurora replica.
- Fixed an issue that would cause high CPU usage and prevent new
  connections.

###### General stability enhancements

- Fixed an issue which causes the stats collector process to repeatedly
  restart.
- Improved the scale times for Aurora Serverless v2.
- Fix a bug which can cause unavailability during ZDP.
- Fixed an issue preventing `pglogical` from logging
  conflicting rows during the apply phase.
- Fixed an issue where, in rare cases, the `aws_s3` extension
  could fail to import from an S3 bucket with a name containing
  dots.
- Provided options to configure the timeouts within the
  `aws_lambda` extension. By setting the following
  parameters, customers will now be able to change the connect and request
  timeouts for AWS Lambda integration:
  - `aws_lambda.connect_timeout_ms`.
  - `aws_lambda.request_timeout_ms`.

- Updated the `plv8`, `pll`, and
  `plcoffee` extensions to version 2.3.15.
- Introduced diagnostics for transient metadata used for I/O.

#### Aurora PostgreSQL

11.16.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experiences stability issues during
  database minor and patch release upgrades.
- Fixed an issue that causes database activity stream inconsistency
  when the monitoring agent is unavailable.
- Fixed an issue that could cause data inconsistency during
  replication.

#### Aurora PostgreSQL

11.16.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.

#### Aurora PostgreSQL

11.16.3, October 13, 2022

###### High priority stability enhancements

- Fixed a `PLV8` issue where the base parameter doesn't
  get loaded properly into the memory.

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the relfilenode.
- Fixed a stuck scaling issue when the current scaling event times out.
- Upgraded the `PostGIS` extension to version 3.1.7.
- Fixed an issue where extended query messages might be lost during
  zero-downtime patching (ZDP) causing the extended query to hang after
  the ZDP completion.

#### Aurora PostgreSQL

11.16.1, July 6, 2022

###### Critical stability enhancements

- Fixed an issue that could cause periods of unavailability during a
  storage node restart.

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue when the connection to SQL Server fails using the
  `TDS_FDW` extension to query a foreign table.
- Fixed an issue that caused connections using the provided root
  certificate to fail.
- Improved the diagnostic and supportability information in case of
  inconsistent B-tree index entries.

#### Aurora PostgreSQL

11.16.0, June 9, 2022

###### New features

- Added support for the `large object` module (extension).
  For more information, see [Managing large objects with the lo module](../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md "../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md").
- Added support for zero-downtime patching (ZDP) for minor version
  upgrades and patches. For more information, see [Minor release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor") in the
  _Amazon Aurora User Guide_.

###### Critical updates

- Fixed a replay crash due to an LSN mismatch.
- Fixed the `aws_s3` extension to prevent invalid region
  injection.

###### High stability updates

- Fixed multiple issues related to out-of-memory conditions which could
  result in brief periods of unavailability.

###### General stability updates

- Fixed a lock contention crash during an Aurora Serverless v1 scaling event.
- Fixed an issue where logical replication becomes stuck after a
  restart.
- Fixed multiple issues that could lead to brief periods of
  unavailability.
- Fixed, during redo, an invalid page hit on the Generic Redo for
  GENERIC_XLOG_FULL_PAGE_DATA. This happens due to a timing hole between
  generating the log record and then writing the metadata for the record
  on the RW node and the RO node replays between those operations.
- Improved the query performance by supporting parallel workers.
- Upgraded the plugin `wal2json` version to 2.4.
- Upgraded the `pglogical` extension to version 2.4.1.

### PostgreSQL 11.15

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.15. For more
information about the improvements in PostgreSQL 11.15, see [PostgreSQL release
11.15](https://www.postgresql.org/docs/13/release-11-15.html "https://www.postgresql.org/docs/13/release-11-15.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.15.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.11156 "#AuroraPostgreSQL.Updates.20180305.11156")
- [Aurora PostgreSQL
  11.15.4, July 18, 2022](#AuroraPostgreSQL.Updates.20180305.11154 "#AuroraPostgreSQL.Updates.20180305.11154")
- [Aurora PostgreSQL
  11.15.1, April 27, 2022](#AuroraPostgreSQL.Updates.20180305.11151 "#AuroraPostgreSQL.Updates.20180305.11151")
- [Aurora PostgreSQL
  11.15.0, March 29, 2022](#AuroraPostgreSQL.Updates.20180305.11150 "#AuroraPostgreSQL.Updates.20180305.11150")

#### Aurora PostgreSQL

11.15.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.
- Updated the `PostGIS` extension to version 3.1.7.

#### Aurora PostgreSQL

11.15.4, July 18, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in
  periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that
  could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files
  that could result in periods of unavailability.
- Fixed a defect where the validation of cached plans may lead to a
  database restart when the plan was previously invalidated.

#### Aurora PostgreSQL

11.15.1, April 27, 2022

###### High priority stability enhancements

- Fixed an issue that could cause incorrect `WriteIOPS`
  reporting in the AWS console.
- Fixed an issue that could cause unavailability after removal of a
  read node from a cluster.

###### General enhancements

- Fixed an issue that could cause an engine restart during periods of
  low free memory.

#### Aurora PostgreSQL

11.15.0, March 29, 2022

###### High priority stability enhancements

- Fixed multiple issues that may result in unavailability of a read
  node.
- Fixed an issue that may result in a read node being unable to replay
  WAL requiring the replication slot to be dropped and resynchronized.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.

###### General enhancements

- Fixed a small memory leak on read nodes when `commit_ts`
  is set.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".
- Fixed an issue that could cause an import from Amazon S3 to fail when
  using the `aws_s3` extension.
- Fixed multiple issues that could result in periods of unavailability
  when using `apg_plan_mgmt`.
- Fixed multiple issues that could result in periods of unavailability
  when QPM is enabled.

### PostgreSQL 11.14

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.14. For more
information about the improvements in PostgreSQL 11.14, see [PostgreSQL release
11.14](https://www.postgresql.org/docs/11/release-11-14.html "https://www.postgresql.org/docs/11/release-11-14.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.14.7, August 24, 2023](#AuroraPostgreSQL.Updates.20180305.11147 "#AuroraPostgreSQL.Updates.20180305.11147")
- [Aurora PostgreSQL
  11.14.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.11146 "#AuroraPostgreSQL.Updates.20180305.11146")
- [Aurora PostgreSQL
  11.14.4, July 20, 2022](#AuroraPostgreSQL.Updates.20180305.11144 "#AuroraPostgreSQL.Updates.20180305.11144")
- [Aurora PostgreSQL
  11.14.3, April 13, 2022](#AuroraPostgreSQL.Updates.20180305.11143 "#AuroraPostgreSQL.Updates.20180305.11143")
- [Aurora PostgreSQL
  11.14.1](#AuroraPostgreSQL.Updates.20180305.11141 "#AuroraPostgreSQL.Updates.20180305.11141")
- [Aurora PostgreSQL
  11.14.0](#AuroraPostgreSQL.Updates.20180305.11140 "#AuroraPostgreSQL.Updates.20180305.11140")

#### Aurora PostgreSQL

11.14.7, August 24, 2023

###### General enhancements

- Fixed an issue which causes the stats collector process to repeatedly
  restart.
- Fixed an issue preventing `pglogical` from logging
  conflicting rows during the apply phase.

#### Aurora PostgreSQL

11.14.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.
- Updated the `PostGIS` extension to version 3.1.7.

#### Aurora PostgreSQL

11.14.4, July 20, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in
  periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that
  could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files
  that could result in periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".

#### Aurora PostgreSQL

11.14.3, April 13, 2022

###### General enhancements

- Fixed a bug that could cause an engine restart during periods of low
  free memory.

#### Aurora PostgreSQL

11.14.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to
  3.1.5. This update contains a `PostGIS` fix for the
  vulnerability addressed in core PostgreSQL by CVE-2020-14350. For more
  information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security
  issue during create extension. The issue was addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL

11.14.0

###### Critical stability enhancements

- Fixed a bug where logical replication may hang resulting in the
  replay falling behind on the read node. The instance may eventually
  restart.

###### Additional improvements and enhancements

- Fixed a buffer cache bug that could cause brief periods of
  unavailability.
- Fixed a bug in the `apg_plan_mgmt` extension where an
  index based plan was not being enforced.
- Fixed a bug in the `pg_logical` extension that could cause
  brief periods of unavailability due to improper handling of NULL
  arguments.
- Fixed an issue where orphaned files caused major version upgrades to
  fail.
- Fixed incorrect Aurora Storage Daemon log write metrics.
- Fixed multiple bugs that could result in WAL replay falling behind
  and eventually causing the reader instances to restart.
- Improved the Aurora buffer cache page validation on reads.
- Improved the Aurora storage metadata validation.
- Updated the `pg_hint_pan` extension to v1.3.7.

- For information about extensions and modules, see [Extensions supported for Aurora PostgreSQL
  11](AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.11 "AuroraPostgreSQL.md#AuroraPostgreSQL.Extensions.11").

### PostgreSQL 11.13

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.13. For more
information about the improvements in PostgreSQL 11.13, see [PostgreSQL release
11.13](https://www.postgresql.org/docs/12/release-11-13.html "https://www.postgresql.org/docs/12/release-11-13.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.13.6, December 19, 2022](#AuroraPostgreSQL.Updates.20180305.11136 "#AuroraPostgreSQL.Updates.20180305.11136")
- [Aurora PostgreSQL
  11.13.4, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.11134 "#AuroraPostgreSQL.Updates.20180305.11134")
- [Aurora PostgreSQL
  11.13.3, June 6, 2022](#AuroraPostgreSQL.Updates.20180305.11133 "#AuroraPostgreSQL.Updates.20180305.11133")
- [Aurora PostgreSQL
  11.13.2, April 12, 2022](#AuroraPostgreSQL.Updates.20180305.11132 "#AuroraPostgreSQL.Updates.20180305.11132")
- [Aurora PostgreSQL
  11.13.1](#AuroraPostgreSQL.Updates.20180305.11131 "#AuroraPostgreSQL.Updates.20180305.11131")
- [Aurora PostgreSQL
  11.13.0](#AuroraPostgreSQL.Updates.20180305.11130 "#AuroraPostgreSQL.Updates.20180305.11130")

#### Aurora PostgreSQL

11.13.6, December 19, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.

#### Aurora PostgreSQL

11.13.4, July 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### General enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that could cause Performance Insights to display
  "Unknown wait event".
- Fixed an issue that could result in periods of unavailability due to
  the existence of duplicate relation files.

#### Aurora PostgreSQL

11.13.3, June 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability updates

- Fixed an issue that can cause a restart of the postmaster process in
  Amazon Aurora Serverless v1.
- Fixed an issue that can cause a restart of the Aurora Runtime process
  in Amazon Aurora Serverless v1.

###### General enhancements

- Fixed a memory leak in the Aurora Runtime that could lead to an
  out-of-memory condition.

#### Aurora PostgreSQL

11.13.2, April 12, 2022

###### General enhancements

- Fixed a buffer cache bug that could cause brief periods of
  unavailability.

#### Aurora PostgreSQL

11.13.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to
  3.1.5. This update contains a `PostGIS` fix for the
  vulnerability addressed in core PostgreSQL by CVE-2020-14350. For more
  information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `pg_bigm` extension to mitigate a security
  issue during create extension. The issue was addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL

11.13.0

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read
  node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O
  resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major
  version update with the message: "PANIC: could not access status of next
  transaction id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue which can cause vacuum operations to become blocked
  after all Aurora read replicas have been removed from a secondary
  cluster.
- Fixed an issue where read nodes restart due to a replication origin
  cache lookup failure.
- Fixed an issue where read queries may time out on read nodes during
  the replay of lazy truncation triggered by vacuum on the write node.
- Fixed an issue that causes Performance Insights to incorrectly set
  the backend type of a database connection.
- Fixed an issue where the `aurora_postgres_replica_status`
  function returned stale or lagging CPU stats.
- Fixed an issue where, in rare cases, an Aurora Global Database
  secondary mirror cluster may restart due to a stall in the log apply
  process.
- Fixed an issue with the `apg_plan_mgmt` extension where
  the planning and execution times were reported as 0.
- Removed support for the DES, 3DES, and RC4 cipher suites.
- Updated `PostGIS` extension to version 3.1.4.
- Added support for `postgis_raster` extension version
  3.1.4.

### PostgreSQL 11.12,

Aurora PostgreSQL 3.6 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.12. For more
information about the improvements in PostgreSQL 11.12, see [PostgreSQL release
11.12](https://www.postgresql.org/docs/11/release-11-12.html "https://www.postgresql.org/docs/11/release-11-12.html").

###### Releases and patches

- [Aurora PostgreSQL
  11.12.5, December 30, 2022](#AuroraPostgreSQL.Updates.20180305.11125 "#AuroraPostgreSQL.Updates.20180305.11125")
- [Aurora PostgreSQL
  11.12.4, July 14, 2022](#AuroraPostgreSQL.Updates.20180305.11124 "#AuroraPostgreSQL.Updates.20180305.11124")
- [Aurora PostgreSQL 3.6.2](#AuroraPostgreSQL.Updates.20180305.362 "#AuroraPostgreSQL.Updates.20180305.362")
- [Aurora PostgreSQL 3.6.1](#AuroraPostgreSQL.Updates.20180305.1112 "#AuroraPostgreSQL.Updates.20180305.1112")
- [Aurora PostgreSQL
  3.6.0](#AuroraPostgreSQL.Updates.20180305.360 "#AuroraPostgreSQL.Updates.20180305.360")

#### Aurora PostgreSQL

11.12.5, December 30, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.

#### Aurora PostgreSQL

11.12.4, July 14, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".

#### Aurora PostgreSQL 3.6.2

###### Security enhancements

- Modified the `pg_bigm` extension to mitigate a security
  issue during create extension. The issue was addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory
  disclosure in certain queries”. [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350")
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to PostGIS 2.5.2. This is a `PostGIS`
  fix for the vulnerability addressed in core PostgreSQL by
  CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL 3.6.1

###### Critical stability enhancements

- Fixed an issue where, in rare circumstances, a data cache of a read
  node may be inconsistent following a restart of that node.

###### High priority stability enhancements

- Fixed an issue where queries may become unresponsive due to I/O
  resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major version
  update with the message: "PANIC: could not access status of next
  transaction id xxxxxxxx".
- Fixed multiple issues in the Aurora storage daemon that could lead to
  brief periods of unavailability when specific network configurations are
  used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that
  leads to writer node restart. This also reduces the overall system
  memory consumption.

###### Additional improvements and enhancements

- Fixed an issue where read nodes restart due to a replication origin
  cache lookup failure.
- Fixed an issue with the `apg_plan_mgmt` extension where
  planning and execution time were reported as 0.
- Fixed an issue that causes Performance Insights to incorrectly set the
  backend type of a database connection.
- Fixed an issue where in rare cases, an Aurora Global Database secondary
  mirror cluster may restart due to a stall in the log apply
  process.
- Fixed an issue where orphaned files caused failed translations in read
  codepaths during or after major version upgrade.
- Fixed multiple issues in the Aurora storage daemon that could lead to
  brief periods of unavailability when specific network configurations are
  used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that
  leads to writer node restart. This also reduces the overall system
  memory consumption.

#### Aurora PostgreSQL

3.6.0

###### High priority stability enhancements

- Fixed an issue where creating a database from an existing template
  database with tablespace resulted in an error with the message
  `ERROR: could not open file pg_tblspc/...: No such file or
directory`.
- Fixed an issue where, in rare cases, an Aurora replica may be unable to
  start when a large number of PostgreSQL subtransactions (i.e. SQL
  savepoints) have been used.
- Fixed an issue where, in rare circumstances, read results may be
  inconsistent for repeated read requests on replica nodes.

###### Additional improvements and enhancements

- Upgraded OpenSSL to 1.1.1k.
- Reduced CPU usage and memory consumption of the WAL apply process on
  Aurora replicas for some workloads.
- Improved metadata protection from accidental erasure.
- Improved safety checks in the write path to detect incorrect writes
  to metadata.
- Improved security by removing 3DES and other older ciphers for
  SSL/TLS connections.
- Fixed an issue where a duplicate file entry can prevent the Aurora
  PostgreSQL engine from starting up.
- Fixed an issue that could cause temporary unavailability under heavy
  workloads.
- Added back ability to use a leading forward slash in the Amazon S3 path
  during S3 import.
- Updated the `orafce` extension to version 3.16.

### PostgreSQL 11.11,

Aurora PostgreSQL 3.5 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.11. For more
information about the improvements in PostgreSQL 11.11, see [PostgreSQL release
11.11](https://www.postgresql.org/docs/11/release-11-11.html "https://www.postgresql.org/docs/11/release-11-11.html").

###### Releases and patches

- [Aurora PostgreSQL 3.5.1](#AuroraPostgreSQL.Updates.20180305.351 "#AuroraPostgreSQL.Updates.20180305.351")
- [Aurora PostgreSQL
  3.5.0](#AuroraPostgreSQL.Updates.20180305.350 "#AuroraPostgreSQL.Updates.20180305.350")

#### Aurora PostgreSQL 3.5.1

###### Security enhancements

- Modified the `pg_bigm` extension to mitigate a security
  issue during create extension. The issue was addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory
  disclosure in certain queries”. For more information, see [CVE-2021-3677](https://www.postgresql.org/support/security/CVE-2021-3677 "https://www.postgresql.org/support/security/CVE-2021-3677")
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to PostGIS 2.5.2. This is a `PostGIS`
  fix for the vulnerability addressed in core PostgreSQL by
  CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw`
  extension function parameters.

#### Aurora PostgreSQL

3.5.0

###### New features

- Added support for the following extensions:
  - The `pg_proctab` extension version 0.0.9
  - The `pg_bigm` extension version 1.2

###### High priority stability enhancements

- Fixed a bug where in rare cases a reader had inconsistent results when
  it restarted while a transaction with more than 64 subtransactions was
  being processed.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2021-32027](https://nvd.nist.gov/vuln/detail/CVE-2021-32027 "https://nvd.nist.gov/vuln/detail/CVE-2021-32027")
  - [CVE-2021-32028](https://nvd.nist.gov/vuln/detail/CVE-2021-32028 "https://nvd.nist.gov/vuln/detail/CVE-2021-32028")
  - [CVE-2021-32029](https://nvd.nist.gov/vuln/detail/CVE-2021-32029 "https://nvd.nist.gov/vuln/detail/CVE-2021-32029")

###### Additional improvements and enhancements

- Fixed a bug where the database could not be started when there were
  many relations in memory-constrained environments.
- Fixed a bug in the `apg_plan_mgmt` extension that could
  cause brief periods of unavailability due to an internal buffer
  overflow.
- Fixed a bug on reader nodes that could cause brief periods of
  unavailability during WAL replay.
- Fixed a bug in the `rds_activity_stream` extension that
  caused an error during startup when attempting to log audit
  events.
- Fixed bugs in the `aurora_replica_status` function where
  rows were sometimes partially populated and some values such as Replay
  Latency, and CPU usage were always 0.
- Fixed a bug where the database engine would attempt to create shared
  memory segments larger than the instance total memory and fail
  repeatedly. For example, attempts to create 128 GiB shared buffers on a
  db.r5.large instance would fail. With this change, requests for total
  shared memory allocations larger than the instance memory allow setting
  the instance to incompatible parameters.
- Added logic to clean up unnecessary `pg_wal` temporary
  files on a database startup.
- Fixed a bug that reported **`ERROR: rds_activity_stream stack
item 2 not found on top - cannot pop`** when attempting to
  create the `rds_activity_stream` extension.
- Fixed a bug that could cause the error **`failed to build any
3-way joins`** in a correlated `IN` subquery
  under an `EXISTS` subquery.
- Backported the following performance improvement from the PostgreSQL
  community: [pg_stat_statements: add missing check for
  pgss_enabled()](https://github.com/postgres/postgres/commit/6f40ee4f837ec1ac59c8ddc73b67a04978a184d "https://github.com/postgres/postgres/commit/6f40ee4f837ec1ac59c8ddc73b67a04978a184d").
- Fixed a bug that could cause brief periods of unavailability due to
  running out of memory when creating the `postgis` extension
  with `pgAudit` enabled.
- Fixed a bug when using outbound logical replication to synchronize
  changes to another database that could fail with an error message like
  **`ERROR: could not map filenode "base/16395/228486645" to
relation OID`**.
- Fixed a bug that could cause a brief period of unavailability when
  canceling a transaction.
- Fixed a bug where the `rds_ad` role wasn't created
  after upgrading from a version of Aurora PostgreSQL that doesn't
  support Microsoft Active Directory authentication.
- Added btree page checks to detect tuple metadata inconsistency.
- Fixed a bug in asynchronous buffer reads that could cause brief
  periods of unavailability on reader nodes during WAL replay.

### PostgreSQL 11.9,

Aurora PostgreSQL 3.4

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.9. For more
information about the improvements in PostgreSQL 11.9, see [PostgreSQL release
11.9](https://www.postgresql.org/docs/11/release-11-9.html "https://www.postgresql.org/docs/11/release-11-9.html").

###### Releases and patches

- [Aurora PostgreSQL 11.9.18, January 15, 2026](#aurorapostgresql-versions-version11918x-11918 "#aurorapostgresql-versions-version11918x-11918")
- [Aurora PostgreSQL 11.9.16, June 18, 2025](#aurorapostgresql-versions-version11916x-11916 "#aurorapostgresql-versions-version11916x-11916")
- [Aurora PostgreSQL 11.9.15
  April 29, 2025](#aurorapostgresql-versions-version11915x-11915 "#aurorapostgresql-versions-version11915x-11915")
- [Aurora PostgreSQL
  11.9.13, November 22, 2024](#aurorapostgresql-versions-version119x-11913 "#aurorapostgresql-versions-version119x-11913")
- [Aurora PostgreSQL
  11.9.12, August 7, 2024](#AuroraPostgreSQL.Updates.20180305.11912 "#AuroraPostgreSQL.Updates.20180305.11912")
- [Aurora PostgreSQL
  11.9.11, March 13, 2024](#AuroraPostgreSQL.Updates.20180305.11911 "#AuroraPostgreSQL.Updates.20180305.11911")
- [Aurora PostgreSQL 11.9.9,
  December 27, 2023](#AuroraPostgreSQL.Updates.20180305.1199 "#AuroraPostgreSQL.Updates.20180305.1199")
- [Aurora PostgreSQL 3.4.8,
  October 10, 2023](#AuroraPostgreSQL.Updates.20180305.1198 "#AuroraPostgreSQL.Updates.20180305.1198")
- [Aurora PostgreSQL 3.4.7,
  December 22, 2022](#AuroraPostgreSQL.Updates.20180305.1197 "#AuroraPostgreSQL.Updates.20180305.1197")
- [Aurora PostgreSQL 3.4.6,
  July 8, 2022](#AuroraPostgreSQL.Updates.20180305.1196 "#AuroraPostgreSQL.Updates.20180305.1196")
- [Aurora PostgreSQL 3.4.5](#AuroraPostgreSQL.Updates.20180305.345 "#AuroraPostgreSQL.Updates.20180305.345")
- [Aurora PostgreSQL
  3.4.3](#AuroraPostgreSQL.Updates.20180305.343 "#AuroraPostgreSQL.Updates.20180305.343")
- [Aurora PostgreSQL
  3.4.2](#AuroraPostgreSQL.Updates.20180305.342 "#AuroraPostgreSQL.Updates.20180305.342")
- [Aurora PostgreSQL
  3.4.1](#AuroraPostgreSQL.Updates.20180305.341 "#AuroraPostgreSQL.Updates.20180305.341")
- [Aurora PostgreSQL
  3.4.0](#AuroraPostgreSQL.Updates.20180305.340 "#AuroraPostgreSQL.Updates.20180305.340")

#### Aurora PostgreSQL 11.9.18, January 15, 2026

###### Critical stability enhancements

- Fixed a security issue when altering routine ownership.

###### High priority enhancements

- Backported fixes for the following PostgreSQL community security issues:
  - [CVE-2025-8713](https://www.postgresql.org/support/security/CVE-2025-8713/ "https://www.postgresql.org/support/security/CVE-2025-8713/").

  [CVE-2025-8714](https://www.postgresql.org/support/security/CVE-2025-8714/ "https://www.postgresql.org/support/security/CVE-2025-8714/").

  [CVE-2025-8715](https://www.postgresql.org/support/security/CVE-2025-8715/ "https://www.postgresql.org/support/security/CVE-2025-8715/").

  [CVE-2025-12817](https://www.postgresql.org/support/security/CVE-2025-12817/ "https://www.postgresql.org/support/security/CVE-2025-12817/").

  [CVE-2025-12818](https://www.postgresql.org/support/security/CVE-2025-12818/ "https://www.postgresql.org/support/security/CVE-2025-12818/").

- Backported fixes for the following PLv8 extension's V8 Engine security vulnerabilities:
  - [CVE-2023-3079](https://nvd.nist.gov/vuln/detail/CVE-2023-3079 "https://nvd.nist.gov/vuln/detail/CVE-2023-3079").

- Fixed a race condition where old writer instance may not step down after a new writer instance is promoted and continues to write.

###### General stability enhancements

- Fixed an issue with parallel heap scans that could lead to index inconsistency on tables larger than 16TiB when synchronize_seqscans is enabled.

#### Aurora PostgreSQL 11.9.16, June 18, 2025

**Critical stability enhancements**

- Fixed an issue related to the interaction between Aurora Serverless scaling and the improved reader availability functionality that might result in longer recover times and impact availability.
- Fixed an issue in the `rds_activity_stream` extension that could cause brief periods of unavailability during configuration reloads and when maximum connections are consumed.

#### Aurora PostgreSQL 11.9.15

April 29, 2025

**High priority enhancements**

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2025-1094](https://www.postgresql.org/support/security/CVE-2025-1094/ "https://www.postgresql.org/support/security/CVE-2025-1094/").

#### Aurora PostgreSQL

11.9.13, November 22, 2024

###### High priority enhancements

- Fixed an issue that would cause a longer restart time when
  `rds.enable_plan_management` is turned on, but
  apg_plan_mgmt extension is not installed.

#### Aurora PostgreSQL

11.9.12, August 7, 2024

###### Critical stability enhancements

- Fixed a pg_repack issue causing two vacuums to concurrently process
  the same table.
- Fixed a V8 Engine [CVE-2018-6065](https://nvd.nist.gov/vuln/detail/CVE-2018-6065 "https://nvd.nist.gov/vuln/detail/CVE-2018-6065") for PLV8 2.x.

#### Aurora PostgreSQL

11.9.11, March 13, 2024

###### General stability enhancements

- Allow `rds_superuser` to terminate backends which are not
  explicitly associated with a role.
- Upgraded `PLV8` extension to version 2.3.15.

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2024-0985](https://nvd.nist.gov/vuln/detail/CVE-2024-0985 "https://nvd.nist.gov/vuln/detail/CVE-2024-0985")

###### Critical stability enhancements

- Fixed an issue related to `apg_plan_mgmt`.
- Fixed an issue where active transactions during slot creation may be
  partially replicated by the slot.
- Fixed a deadlock issue in Aurora storage which can result in writer
  failover.

#### Aurora PostgreSQL 11.9.9,

December 27, 2023

###### Critical stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-5870](https://nvd.nist.gov/vuln/detail/CVE-2023-5870 "https://nvd.nist.gov/vuln/detail/CVE-2023-5870")
  - [CVE-2023-5869](https://nvd.nist.gov/vuln/detail/CVE-2023-5869 "https://nvd.nist.gov/vuln/detail/CVE-2023-5869")
  - [CVE-2023-5868](https://nvd.nist.gov/vuln/detail/CVE-2023-5868 "https://nvd.nist.gov/vuln/detail/CVE-2023-5868")

###### General stability enhancements

- Fixed an issue with logical replication actions being performed by
  someone other than the table owner

#### Aurora PostgreSQL 3.4.8,

October 10, 2023

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2023-39417](https://nvd.nist.gov/vuln/detail/CVE-2023-39417 "https://nvd.nist.gov/vuln/detail/CVE-2023-39417")
  - [CVE-2023-2455](https://nvd.nist.gov/vuln/detail/CVE-2023-2455 "https://nvd.nist.gov/vuln/detail/CVE-2023-2455")
  - [CVE-2023-2454](https://nvd.nist.gov/vuln/detail/CVE-2023-2454 "https://nvd.nist.gov/vuln/detail/CVE-2023-2454")
  - [CVE-2022-2625](https://nvd.nist.gov/vuln/detail/CVE-2022-2625 "https://nvd.nist.gov/vuln/detail/CVE-2022-2625")

#### Aurora PostgreSQL 3.4.7,

December 22, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.

#### Aurora PostgreSQL 3.4.6,

July 8, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

#### Aurora PostgreSQL 3.4.5

###### Security enhancements

- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched the PostgreSQL community fix for CVE-2021-3677: “Memory
  disclosure in certain queries”. For more information, see [CVE-2021-3677](https://www.postgresql.org/support/security/CVE-2021-3677 "https://www.postgresql.org/support/security/CVE-2021-3677")
- Backpatched the PostgreSQL community fix for CVE-2021-3393: "Partition
  constraint violation errors leak values of denied columns". For more
  information, see [CVE-2021-3393](https://www.postgresql.org/support/security/CVE-2021-3393 "https://www.postgresql.org/support/security/CVE-2021-3393")
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to PostGIS 2.5.2. This is a `PostGIS`
  fix for the vulnerability addressed in core PostgreSQL by
  CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw`
  extension function parameters.

#### Aurora PostgreSQL

3.4.3

###### High priority stability enhancements

- Provided a patch for PostgreSQL community security issues
  CVE-2021-32027, CVE-2021-32028 and CVE-2021-32029.

###### Additional improvements and enhancements

- Fixed a bug in the `aws_s3` extension to allow import of
  objects with leading forward slashes in the object identifier.
- Fixed a bug in the `rds_activity_stream` extension that
  caused an error during startup when attempting to log audit
  events.
- Fixed a bug that returned an `ERROR` when attempting to
  create the `rds_activity_stream` extension.
- Fixed a bug that could cause brief periods of unavailability due to
  running out of memory when creating the `postgis` extension
  with `pgAudit` enabled.
- Fixed multiple issues in the Aurora storage daemon that could lead to
  brief periods of unavailability when specific network configurations are
  used.

#### Aurora PostgreSQL

3.4.2

###### High priority stability enhancements

- Fixed a bug where in rare cases a reader had inconsistent results when
  it restarted while a transaction with more than 64 subtransactions was
  being processed.

###### Additional improvements and enhancements

- Fixed a bug that could lead to intermittent unavailability due to a
  race condition when handling responses from storage nodes.
- Fixed a bug that could lead to intermittent unavailability due to the
  rotation of network encryption keys.
- Fixed a bug that could lead to intermittent unavailability due to heat
  management of the underlying storage segments.
- Fixed a bug where a large S3 import with thousands of clients can
  cause one or more of the import clients to stop responding.
- Removed a restriction that prevented setting configuration variable
  strings that contained `brazil`.
- Fixed a bug that could lead to intermittent unavailability if a reader
  node runs a query that access many tables while the writer node is
  acquiring exclusive locks on all of the same tables.

#### Aurora PostgreSQL

3.4.1

###### Critical stability enhancements

- Fixed a bug that caused a read replica to unsuccessfully restart
  repeatedly in rare cases.
- Fixed a bug where a cluster became unavailable when attempting to
  create more than 16 read replicas or Aurora global database secondary
  AWS Regions. The cluster became available again when the new read
  replica or secondary AWS Region was removed.

###### Additional improvements and enhancements

- Fixed a bug that when under heavy load, snapshot import, COPY import,
  or S3 import stopped responding in rare cases.
- Fixed a bug where a read replica might not join the cluster when the
  writer was very busy with a write-intensive workload.
- Fixed a bug where a cluster could be unavailable briefly when a
  high-volume S3 import was running.
- Fixed a bug that caused a cluster to take several minutes to restart
  if a logical replication stream was terminated while handling many
  complex transactions.
- Disallowed the use of both IAM and Kerberos authentication for the
  same user.

#### Aurora PostgreSQL

3.4.0

###### New features

- Aurora PostgreSQL now supports invocation of AWS Lambda functions. This
  includes the new `aws_lambda` extension. For more
  information, see [Invoking an AWS Lambda function from an Aurora PostgreSQL DB
  cluster](../AuroraUserGuide/PostgreSQL-Lambda.md "../AuroraUserGuide/PostgreSQL-Lambda.md") in the _Amazon Aurora User Guide_.
- The db.r6g instance classes are now available in preview for Aurora.
  For more information, see [Aurora DB instance classes](../AuroraUserGuide/Concepts.md "../AuroraUserGuide/Concepts.md") in the _Amazon Aurora User
  Guide_.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Fixed a bug in Aurora PostgreSQL replication that could result in the
  error message **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.
- Fixed a bug where in some cases, DB clusters that have logical
  replication enabled did not remove truncated WAL segment files from
  storage. This resulted in volume size growth.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
  - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
  - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

- Fixed a bug in the `pg_stat_statements` extension that
  caused excessive CPU consumption.

###### Additional improvements and enhancements

- You can now use `pg_replication_slot_advance` to advance a
  logical replication slot for the roles `rds_replication` and
  `rds_superuser`.
- Improved the asynchronous mode performance of database activity
  streams.
- Reduced the delay when publishing to CloudWatch the
  `rpo_lag_in_msec` metric for Aurora global database
  clusters.
- Aurora PostgreSQL no longer falls behind on a read node when the backend
  is blocked writing to the database client.
- Fixed a bug that in rare cases caused a brief period of unavailability
  on a read replica when the storage volume grew.
- Fixed a bug when creating a database that could return the following:
  **`ERROR: could not create directory on local
disk`**
- Updated data grid files to fix errors or incorrect transformation
  results from the `ST_Transform` method of the
  `PostGIS` extension.
- Fixed a bug where in some cases replaying
  `XLOG_BTREE_REUSE_PAGE` records on Aurora reader instances
  caused unnecessary replay lag.
- Fixed a small memory leak in a b-tree index that could lead to an out
  of memory condition.
- Fixed a bug in the `GiST` index that could result in an out
  of memory condition after promoting an Aurora read replica.
- Fixed an S3 import bug that reported **`ERROR: HTTP 403.
Permission denied`** when importing data from a file inside
  an S3 subfolder.
- Fixed a bug in the `aws_s3` extension for pre-signed URL
  handling that could result in the error message **`S3 bucket
names with a period (.) are not supported`**.
- Fixed a bug in the `aws_s3` extension where an import might
  be blocked indefinitely if an exclusive lock was taken on the relation
  prior to beginning the operation.
- Fixed a bug related to replication when Aurora PostgreSQL is acting as a
  physical replica of an RDS for PostgreSQL instance that uses
  `GiST` indexes. In rare cases, this bug caused a brief
  period of unavailability after promoting the Aurora cluster.
- Fixed a bug in database activity streams where customers were not
  notified of the end of an outage.
- Updated the `pg_audit` extension to version 1.3.1.

### PostgreSQL 11.8,

Aurora PostgreSQL 3.3 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.8. For more
information about the improvements in PostgreSQL 11.8, see [PostgreSQL release
11.8](https://www.postgresql.org/docs/11/release-11-8.html "https://www.postgresql.org/docs/11/release-11-8.html").

###### Releases and patches

- [Aurora PostgreSQL release
  3.3.2](#AuroraPostgreSQL.Updates.20180305.332 "#AuroraPostgreSQL.Updates.20180305.332")
- [Aurora PostgreSQL
  3.3.1](#AuroraPostgreSQL.Updates.20180305.331 "#AuroraPostgreSQL.Updates.20180305.331")
- [Aurora PostgreSQL
  3.3.0](#AuroraPostgreSQL.Updates.20180305.330 "#AuroraPostgreSQL.Updates.20180305.330")

#### Aurora PostgreSQL release

3.3.2

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Fixed a bug in Aurora PostgreSQL replication that could result in the
  error message **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.
- Fixed a bug where in some cases, DB clusters that have logical
  replication enabled did not remove truncated WAL segment files from
  storage. This resulted in volume size growth.
- Fixed an issue with creating a global database cluster in a secondary
  region.
- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
  - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
  - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

- Fixed a bug in the `pg_stat_statements` extension that
  caused excessive CPU consumption.

###### Additional improvements and enhancements

- Aurora PostgreSQL no longer falls behind on a read node when the backend
  is blocked writing to the database client.
- Reduced the delay when publishing to CloudWatch the
  `rpo_lag_in_msec` metric for Aurora global database
  clusters.
- Fixed a bug where a `DROP DATABASE` statement didn't
  remove any relation files.
- Fixed a bug where in some cases replaying
  `XLOG_BTREE_REUSE_PAGE` records on Aurora reader instances
  caused unnecessary replay lag.
- Fixed a small memory leak in a b-tree index that could lead to an out
  of memory condition.
- Fixed a bug in the `aurora_replica_status()` function where
  the `server_id` field was sometimes truncated.
- Fixed a bug where a log record was incorrectly processed causing the
  Aurora replica to crash.
- Fixed an S3 import bug that reported **`ERROR: HTTP 403.
Permission denied`** when importing data from a file inside
  an S3 subfolder.
- You can now use `pg_replication_slot_advance` to advance a
  logical replication slot for the roles `rds_replication` and
  `rds_superuser`.
- Improved performance of the asynchronous mode for database activity
  streams.
- Fixed a bug in the `aws_s3` extension that could result in
  the error message **`S3 bucket names with a period (.) are not
supported`**.
- Fixed a race condition that caused valid imports to intermittently
  fail.
- Fixed a bug related to replication when Aurora PostgreSQL is acting as a
  physical replica of an RDS for PostgreSQL instance that uses GiST indexes. In
  rare cases, this bug caused a brief period of unavailability after
  promoting the Aurora DB cluster.
- Fixed a bug in the `aws_s3` extension where an import may
  be blocked indefinitely if an exclusive lock was taken on the relation
  prior to beginning the operation.

#### Aurora PostgreSQL

3.3.1

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug that appears when the `NOT EXISTS` operator
   incorrectly returns TRUE, which can only happen when the following unusual
   set of circumstances occurs:
   - A query is using the `NOT EXISTS` operator.
   - The column or columns being evaluated against the outer
     query in the `NOT EXISTS` subquery contain a NULL value.
   - There isn't a another predicate in the subquery that removes the need
     for the evaluation of the NULL values.
   - The filter used in the subquery does not use an index seek for its execution.
   - The operator isn't converted to a join by the query optimizer.

#### Aurora PostgreSQL

3.3.0

###### New features

- Added support for the RDKit extension version 3.8.

The RDKit extension provides modeling functions for cheminformatics.
Cheminformatics is storing, indexing, searching, retrieving, and
applying information about chemical compounds. For example, with the
RDKit extension you can construct models of molecules, search for
molecular structures, and read or create molecules in various notations.
You can also perform research on data loaded from the [ChEMBL website](https://www.ebi.ac.uk/chembl/ "https://www.ebi.ac.uk/chembl/") or a
SMILES file. The Simplified Molecular Input Line Entry System (SMILES)
is a typographical notation for representing molecules and reactions.
For more information, see [The RDKit database
cartridge](https://rdkit.org/docs/Cartridge.html "https://rdkit.org/docs/Cartridge.html") in the RDKit documentation.

- Added support for a minimum TLS version

Support for a minimum Transport Layer Security (TLS) version is back
ported from PostgreSQL 12. It allows the Aurora PostgreSQL server to
constrain the TLS protocols with which a client is allowed to connect
via two new PostgreSQL parameters. These parameters include [ssl_min_protocol_version](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-SSL-MIN-PROTOCOL-VERSION "https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-SSL-MIN-PROTOCOL-VERSION")and [ssl_max_protocol_version](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-SSL-MAX-PROTOCOL-VERSION "https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-SSL-MAX-PROTOCOL-VERSION"). For example, to limit client
connections to the Aurora PostgreSQL server to at least TLS 1.2 protocol
version, set the `ssl_min_protocol_version` to
`TLSv1.2`.

- Added support for the `pglogical` extension version
  2.2.2.

The `pglogical` extension is a logical streaming
replication system that provides additional features beyond what's
available in PostgreSQL native logical replication. Features include
conflict handling, row filtering, DDL/sequence replication and delayed
apply. You can use the `pglogical` extension to set up
replication between Aurora PostgreSQL clusters, between RDS for PostgreSQL and
Aurora PostgreSQL, and with PostgreSQL databases running outside of
RDS.

- Aurora dynamically resizes your cluster storage space. With dynamic
  resizing, the storage space for your Aurora DB cluster automatically
  decreases when you remove data from the DB cluster. For more
  information, see [Storage scaling](../AuroraUserGuide/Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling "../AuroraUserGuide/Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling") in the _Amazon Aurora User
  Guide_.

###### Note

The dynamic resizing feature is being deployed in phases to the
AWS Regions where Aurora is available. Depending on the Region
where your cluster is, this feature might not be available yet. For
more information, see [the What's New announcement](https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-aurora-enables-dynamic-resizing-database-storage-space/ "https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-aurora-enables-dynamic-resizing-database-storage-space/").

###### Critical stability enhancements

- Fixed a bug related to heap page extend that in rare cases resulted in
  longer recovery time and impacted availability.

###### High priority stability enhancements

- Fixed a bug in Aurora Global Database that could cause delays in
  upgrading the database engine in a secondary AWS Region. For more
  information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
  User Guide_.
- Fixed a bug that in rare cases caused delays in upgrading a database
  to engine version 11.8.

###### Additional improvements and enhancements

- Fixed a bug where the Aurora replica crashed when workloads with heavy
  subtransactions are made on the writer instance.
- Fixed a bug where the writer instance crashed due to a memory leak and
  the depletion of memory used to track active transactions.
- Fixed a bug that lead to a crash due to improper initialization when
  there is no free memory available during PostgreSQL backend
  startup.
- Fixed a bug where an Aurora PostgreSQL Serverless DB cluster might return
  the following error after a scaling event: **`ERROR: prepared
statement "S_6" already exists`**.
- Fixed an out-of-memory problem when issuing the `CREATE
EXTENSION` command with PostGIS when Database Activity Streams
  is enabled.
- Fixed a bug where a `SELECT` query might incorrectly return
  the error **`Attempting to read past EOF of relation rrrr.
blockno=bbb nblocks=nnn`**.
- Fixed a bug where the database might be unavailable briefly due to
  error handling in database storage growth.
- Fixed a bug in Aurora PostgreSQL Serverless where queries that executed on
  previously idle connections got delayed until the scale operation
  completed.
- Fixed a bug where an Aurora PostgreSQL DB cluster with Database Activity
  Streams enabled might report the beginning of a potential loss window
  for activity records, but does not report the restoration of
  connectivity.
- Fixed a bug with the `aws_s3.table_import_from_s3` function
  where a `COPY` from S3 failed with the error **`HTTP
error code: 248`**. For more information, see [aws_s3.table_import_from_s3](../AuroraUserGuide/USER_PostgreSQL.md#aws_s3.table_import_from_s3 "../AuroraUserGuide/USER_PostgreSQL.md#aws_s3.table_import_from_s3") in the _Amazon Aurora
  User Guide_.

### PostgreSQL 11.7,

Aurora PostgreSQL 3.2 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.7. For more
information about the improvements in PostgreSQL 11.7, see [PostgreSQL release
11.7](https://www.postgresql.org/docs/11/release-11-7.html "https://www.postgresql.org/docs/11/release-11-7.html").

###### Releases and patches

- [Aurora PostgreSQL
  3.2.7](#AuroraPostgreSQL.Updates.20180305.327 "#AuroraPostgreSQL.Updates.20180305.327")
- [Aurora PostgreSQL
  3.2.6](#AuroraPostgreSQL.Updates.20180305.326 "#AuroraPostgreSQL.Updates.20180305.326")
- [Aurora PostgreSQL
  3.2.4](#AuroraPostgreSQL.Updates.20180305.324 "#AuroraPostgreSQL.Updates.20180305.324")
- [Aurora PostgreSQL
  3.2.3](#AuroraPostgreSQL.Updates.20180305.323 "#AuroraPostgreSQL.Updates.20180305.323")
- [Aurora PostgreSQL
  3.2.2](#AuroraPostgreSQL.Updates.20180305.322 "#AuroraPostgreSQL.Updates.20180305.322")
- [Aurora PostgreSQL
  3.2.1](#AuroraPostgreSQL.Updates.20180305.321 "#AuroraPostgreSQL.Updates.20180305.321")

#### Aurora PostgreSQL

3.2.7

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
  - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
  - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

3.2.6

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Fixed a bug in Aurora PostgreSQL replication that might result in the
  error message, **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.

###### Additional improvements and enhancements

- Fixed a bug that in rare cases caused brief read replica
  unavailability when storage volume grew.
- Aurora PostgreSQL Serverless now supports execution of queries on all
  connections during a scale event.
- Fixed a bug in Aurora PostgreSQL Serverless where a leaked lock
  resulted in a prolonged scale event.
- Fixed a bug where the `aurora_replica_status` function
  showed truncated server identifiers.
- Fixed a bug in Aurora PostgreSQL Serverless where connections being
  migrated during a scale event disconnected with the message:
  "**`ERROR: could not open relation with OID
...`**.
- Fixed a small memory leak in a b-tree index that could lead to an out
  of memory condition.
- Fixed a bug in a GiST index that might result in an out-of-memory
  condition after promoting an Aurora Read Replica.
- Improved performance for Database Activity Streams.
- Fixed a bug in Database Activity Streams where customers were not
  notified when an outage ended.
- Fixed a bug in the `aws_s3` extension for pre-signed URL
  handling that could have resulted in the error message **`S3
bucket names with a period (.) are not supported`**.
- Fixed a bug in the `aws_s3` extension where incorrect error
  handling could lead to failures during the import process.
- Fixed a bug in the `aws_s3` extension where an import may
  be blocked indefinitely if an exclusive lock was taken on the relation
  prior to beginning the operation.

#### Aurora PostgreSQL

3.2.4

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug that appears when the `NOT EXISTS` operator
   incorrectly returns TRUE, which can only happen when the following unusual
   set of circumstances occurs:
   - A query is using the `NOT EXISTS` operator.
   - The column or columns being evaluated against the outer
     query in the `NOT EXISTS` subquery contain a NULL value.
   - There isn't a another predicate in the subquery that removes the need
     for the evaluation of the NULL values.
   - The filter used in the subquery does not use an index seek for its execution.
   - The operator isn't converted to a join by the query optimizer.

#### Aurora PostgreSQL

3.2.3

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- None

###### Additional improvements and enhancements

- Fixed a bug in Aurora PostgreSQL Serverless where queries that ran on
  previously idle connections got delayed until the scale operation
  completed.
- Fixed a bug that might cause brief unavailability for heavy
  subtransaction workloads when multiple reader instances restart or
  rejoin the cluster.

#### Aurora PostgreSQL

3.2.2

You can find the following improvements in this release.

###### Critical stability enhancements

- Fixed a bug related to heap page extend that in rare cases resulted in
  longer recovery time and impacted availability.

###### High priority stability enhancements

- Fixed a bug in Aurora Global Database that could cause delays in
  upgrading the database engine in a secondary region. For more
  information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
  User Guide_.
- Fixed a bug that in rare cases caused delays in upgrading a database
  to engine version 11.7.

###### Additional improvements and enhancements

- Fixed a bug where the database might be unavailable briefly due to
  error handling in database storage growth.
- Fixed a bug where a SELECT query might incorrectly return the error,
  **`Attempting to read past EOF of relation rrrr. blockno=bbb
nblocks=nnn`**.
- Fixed a bug where an Aurora PostgreSQL Serverless DB cluster might
  return the following error after a scaling event: **`ERROR:
prepared statement "S_6" already exists`**.

#### Aurora PostgreSQL

3.2.1

###### New features

- Added support for Amazon Aurora PostgreSQL Global Database. For more
  information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
  User Guide_.
- Added the ability to configure the recovery point objective (RPO) of a
  global database for Aurora PostgreSQL. For more information, see [Managing RPOs for Aurora PostgreSQL–based global databases](../AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery "../AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery") in
  the _Amazon Aurora User Guide_.

You can find the following improvements in this release.

###### Critical stability enhancements

None.

###### High priority stability enhancements

- Improved performance and availability of read instances when applying
  DROP TABLE and TRUNCATE TABLE operations.
- Fixed a small but continuous memory leak in a diagnostic module that
  could lead to an out-of-memory condition on smaller DB instance
  types.
- Fixed a bug in the `PostGIS` extension which could lead to
  a database restart. This has been reported to the PostGIS community as
  [https://trac.osgeo.org/postgis/ticket/4646](https://trac.osgeo.org/postgis/ticket/4646 "https://trac.osgeo.org/postgis/ticket/4646").
- Fixed a bug where read requests might stop responding due to incorrect
  error handling in the storage engine.
- Fixed a bug that fails for some queries and results in the message
  **`ERROR: found xmin xxxxxx from before relfrozenxid
yyyyyyy`**. This could occur following the promotion of a
  read instance to a write instance.
- Fixed a bug where an Aurora serverless DB cluster might crash while
  rolling back a scale attempt.

###### Additional improvements and enhancements

- Improved performance for queries that read many rows from
  storage.
- Improved performance and availability of reader DB instances during
  heavy read workload.
- Enabled correlated IN and NOT IN subqueries to be transformed to joins
  when possible.
- Improved the filtering estimation for enhanced semi-join filter
  pushdown by using multi-column statistics or indexes when
  available.
- Improved read performance of the `pg_prewarm`
  extension.
- Fixed a bug where an Aurora serverless DB cluster might report the
  message **`ERROR: incorrect binary data format in bind parameter
...`** following a scale event.
- Fixed a bug where a serverless DB cluster might report the message
  **`ERROR: insufficient data left in message`**
  following a scale event.
- Fixed a bug where an Aurora serverless DB cluster can experience
  prolonged or failed scale attempts.
- Fixed a bug that resulted in the message **`ERROR: could not
create file "base/xxxxxx/yyyyyyy" as a previous version still exists
on disk: Success. Please contact AWS customer support`**.
  This can occur during object creation after PostgreSQL's 32-bit
  object identifier has wrapped around.
- Fixed a bug where the write-ahead-log (WAL) segment files for
  PostgreSQL logical replication were not deleted when changing the
  `wal_level` value from `logical` to
  `replica`.
- Fixed a bug in the `pg_hint_plan` extension where a
  multi-statement query could lead to a crash when
  `enable_hint_table` is enabled. This is tracked in the
  PostgreSQL community as [https://github.com/ossc-db/pg_hint_plan/issues/25](https://github.com/ossc-db/pg_hint_plan/issues/25 "https://github.com/ossc-db/pg_hint_plan/issues/25").
- Fixed a bug where JDBC clients might report the message
  **`java.io.IOException: Unexpected packet type:
75`** following a scale event in an Aurora serverless DB
  cluster.
- Fixed a bug in PostgreSQL logical replication that resulted in the
  message **`ERROR: snapshot reference is not owned by resource
owner TopTransaction`**.
- Changed the following extensions:
  - Updated `orafce` to version 3.8
  - Updated `pgTAP` to version 1.1

- Provided support for fault injection queries.

### PostgreSQL 11.6,

Aurora PostgreSQL 3.1 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.6. For more
information about the improvements in PostgreSQL 11.6, see [PostgreSQL release
11.6](https://www.postgresql.org/docs/11/release-11-6.html "https://www.postgresql.org/docs/11/release-11-6.html").

This release contains multiple critical stability enhancements. Amazon highly
recommends upgrading your Aurora PostgreSQL clusters that use older PostgreSQL 11
engines to this release.

###### Releases and patches

- [Aurora PostgreSQL
  3.1.4](#AuroraPostgreSQL.Updates.20180305.314 "#AuroraPostgreSQL.Updates.20180305.314")
- [Aurora PostgreSQL
  3.1.3](#AuroraPostgreSQL.Updates.20180305.313 "#AuroraPostgreSQL.Updates.20180305.313")
- [Aurora PostgreSQL
  3.1.2](#AuroraPostgreSQL.Updates.20180305.312 "#AuroraPostgreSQL.Updates.20180305.312")
- [Aurora PostgreSQL
  3.1.1](#AuroraPostgreSQL.Updates.20180305.311 "#AuroraPostgreSQL.Updates.20180305.311")
- [Aurora PostgreSQL
  3.1.0](#AuroraPostgreSQL.Updates.20180305.310 "#AuroraPostgreSQL.Updates.20180305.310")

#### Aurora PostgreSQL

3.1.4

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Backported fixes for the following PostgreSQL community security
  issues:
  - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
  - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
  - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

3.1.3

###### New features

- Aurora PostgreSQL now supports the PostgreSQL [vacuum_truncate](https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE "https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE") storage parameter to manage vacuum
  truncation for specific tables. Set this [storage parameter](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS "https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS") to false for a table to prevent the
  [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html") SQL command from truncating the table's
  trailing empty pages.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- Fixed a bug where reads from storage might stop responding due to
  incorrect error handling.

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

3.1.2

This release contains a critical stability enhancement. Amazon highly
recommends updating your older Aurora PostgreSQL 11-compatible clusters to this
release.

###### Critical stability enhancements

- Fixed a bug in which a reader DB instance might temporarily use stale
  data. This could lead to wrong results such as too few or too many rows.
  This error is not persisted on storage, and will clear when the database
  page containing the row has been evicted from cache. This can happen
  when the primary DB instance enters a transaction snapshot overflow due
  to having more than 64 subtransactions in a single transaction.
  Applications susceptible to this bug include those that use SQL
  savepoints or PostgreSQL exception handlers with more than 64
  subtransactions in the top transaction.

###### High priority stability enhancements

- Fixed a bug that might cause a reader DB instance to crash causing
  unavailability while attempting to the join the DB cluster. This can
  happen in some cases when the primary DB instance has a transaction
  snapshot overflow due to a high number of subtransactions. In this
  situation the reader DB instance will be unable to join until the
  snapshot overflow has cleared.

###### Additional improvements and enhancements

- Fixed a bug that prevented Performance Insights from determining the
  query ID of a running statement.

#### Aurora PostgreSQL

3.1.1

You can find the following improvements in this release.

###### Critical stability enhancements

- Fixed a bug in which the DB instance might be briefly unavailable due
  to the self-healing function of the underlying storage.

###### High priority stability enhancements

- Fixed a bug in which the database engine might crash causing
  unavailability. This occurred while scanning an included, non-key column
  of a B-Tree index. This only applies to PostgreSQL 11 "included column"
  indexes.
- Fixed a bug that might cause the database engine to crash causing
  unavailability. This occurred if a newly established database connection
  encountered a resource exhaustion-related error during initialization
  after successful authentication.

###### Additional improvements and enhancements

- Provided a fix for the `pg_hint_plan` extension that could
  lead the database engine to crash causing unavailability. The open
  source issue can be tracked at [https://github.com/ossc-db/pg_hint_plan/pull/45](https://github.com/ossc-db/pg_hint_plan/pull/45 "https://github.com/ossc-db/pg_hint_plan/pull/45").
- Fixed a bug where SQL of the form `ALTER FUNCTION ... OWNER TO
...` incorrectly reported `ERROR: improper qualified name
(too many dotted names)`.
- Improved the performance of `GIN` index vacuum via
  prefetching.
- Fixed a bug in open source PostgreSQL that could lead to a database
  engine crash causing unavailability. This occurred during parallel
  B-Tree index scans. This issue has been reported to the PostgreSQL
  community.
- Improved the performance of in-memory B-Tree index scans.

#### Aurora PostgreSQL

3.1.0

You can find the following new features and improvements in this engine
version.

###### New features

1.  Support for exporting data to Amazon S3. For more information, see [Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](../AuroraUserGuide/postgresql-s3-export.md "../AuroraUserGuide/postgresql-s3-export.md") in
    the _Amazon Aurora User Guide_.
2.  Support for Amazon Aurora Machine Learning. For more information, see
    [Using
    machine learning (ML) with Aurora PostgreSQL](../AuroraUserGuide/postgresql-ml.md "../AuroraUserGuide/postgresql-ml.md") in the
    _Amazon Aurora User Guide_.
3.  SQL processing enhancements include:

        * Optimizations for `NOT IN` with the
         `apg_enable_not_in_transform` parameter.
        * Semi-join filter pushdown enhancements for hash joins with the
         `apg_enable_semijoin_push_down` parameter.
        * Optimizations for redundant inner join removal with the
         `apg_enable_remove_redundant_inner_joins`
         parameter.
        * Improved ANSI compatibility options with the
         `ansi_constraint_trigger_ordering`,
         `ansi_force_foreign_key_checks` and
         `ansi_qualified_update_set_target`
         parameters.

    For more information, see [Amazon Aurora PostgreSQL parameters](../AuroraUserGuide/AuroraPostgreSQL.Reference.md "../AuroraUserGuide/AuroraPostgreSQL.Reference.md") in the _Amazon Aurora
    User Guide_.

4.  New and updated PostgreSQL extensions include:
    - The new `aws_ml` extension. For more information,
      see [Using machine learning (ML) with Aurora PostgreSQL](../AuroraUserGuide/postgresql-ml.md "../AuroraUserGuide/postgresql-ml.md") in
      the _Amazon Aurora User Guide_.
    - The new `aws_s3` extension. For more information,
      see [Exporting data from an Aurora PostgreSQL DB cluster to
      Amazon S3](../AuroraUserGuide/postgresql-s3-export.md "../AuroraUserGuide/postgresql-s3-export.md") in the _Amazon Aurora User
      Guide_.
    - Updates to the `apg_plan_mgmt` extension. For more
      information, see [Managing query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md")
      in the _Amazon Aurora User Guide_.

###### Critical stability enhancements

1. Fixed a bug related to creating B-tree indexes on temporary tables
   that in rare cases might result in longer recovery time, and impact
   availability.
2. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
   physical replica of an RDS for PostgreSQL instance. In rare cases, this bug
   causes a log write failure that might result in longer recovery time,
   and impact availability.
3. Fixed a bug related to handling of reads with high I/O latency that in
   rare cases might result in longer recovery time, and impact
   availability.

###### High priority stability enhancements

1. Fixed a bug related to logical replication in which `wal`
   segments are not properly removed from storage. This can result in
   storage bloat. To monitor this, view the
   `TransactionLogDiskUsage` parameter.
2. Fixed multiple bugs, which cause Aurora to crash during prefetch
   operations on Btree indexes.
3. Fixed a bug in which an Aurora restart might time out when logical
   replication is used.
4. Enhanced the validation checks performed on data blocks in the buffer
   cache. This improves Aurora's detection of inconsistency.

###### Additional improvements and enhancements

1. The query plan management extension `apg_plan_mgmt` has an
   improved algorithm for managing plan generation for highly partitioned
   tables.
2. Reduced startup time on instances with large caches via improvements
   in the buffer cache recovery algorithm.
3. Improved the performance of the read-node-apply process under high
   transaction rate workloads by using changes to PostgreSQL
   `LWLock` prioritization. These changes prevent starvation
   of the read-node-apply process while the PostgreSQL
   `ProcArray` is under heavy contention.
4. Improved handling of batch reads during vacuum, table scans, and index
   scans. This results in greater throughput and lower CPU
   consumption.
5. Fixed a bug in which a read node might crash during the replay of a
   PostgreSQL `SLRU`-truncate operation.
6. Fixed a bug where in rare cases, database writes might stall following
   an error returned by one of the six copies of an Aurora log record.
7. Fixed a bug related to logical replication where an individual
   transaction larger than 1 GB in size might result in an engine
   crash.
8. Fixed a memory leak on read nodes when cluster cache management is
   enabled.
9. Fixed a bug in which importing an RDS for PostgreSQL snapshot might stop
   responding if the source snapshot contains a large number of unlogged
   relations.
10. Fixed a bug in which the Aurora storage daemon might crash under heavy
    I/O load.
11. Fixed a bug related to `hot_standby_feedback` for read
    nodes in which the read node might report the wrong transaction id epoch
    to the write node. This can cause the write node to ignore the
    `hot_standby_feedback` and invalidate snapshots on the
    read node.
12. Fixed a bug in which storage errors that occur during `CREATE
DATABASE` statements are not properly handled. The bug left
    the resulting database inaccessible. The correct behavior is to fail the
    database creation and return the appropriate error to the user.
13. Improved handling of PostgreSQL snapshot overflow when a read node
    attempts to connect to a write node. Prior to this change, if the write
    node was in a snapshot overflow state, the read node was unable to join.
    A message appeared in the PostgreSQL log file in the form `DEBUG:
recovery snapshot waiting for non-overflowed snapshot or until
oldest active xid on standby is at least
`xxxxxxx`(now`yyyyyyy`)`. A snapshot overflow
    occurs when an individual transaction has created over 64
    subtransactions.
14. Fixed a bug related to common table expressions in which an error is
    incorrectly raised when a NOT IN class exists in a CTE. The error is
    `CTE with NOT IN fails with ERROR: could not find CTE
`CTE-Name``.
15. Fixed a bug related to an incorrect `last_error_timestamp`
    value in the `aurora_replica_status` table.
16. Fixed a bug to avoid populating shared buffers with blocks belonging
    to temporary objects. These blocks correctly reside in PostgreSQL
    backend local buffers.
17. Changed the following extensions:
    - Updated `pg_hint_plan` to version 1.3.4.
    - Added `plprofiler` version 4.1.
    - Added `pgTAP` version 1.0.0.

### PostgreSQL 11.4,

Aurora PostgreSQL 3.0 (Deprecated)

###### Note

The PostgreSQL engine version 11.4 with the Aurora PostgreSQL 3.0 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 11.4. For more
information about the improvements in PostgreSQL 11.4, see [PostgreSQL release
11.4](https://www.postgresql.org/docs/11/release-11-4.html "https://www.postgresql.org/docs/11/release-11-4.html").

You can find the following improvements in this release.

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [Aurora PostgreSQL
   2.3.5](#AuroraPostgreSQL.Updates.20180305.235 "#AuroraPostgreSQL.Updates.20180305.235").
2. Partitioning – Partitioning improvements include support for hash
   partitioning, enabling creation of a default partition, and dynamic row
   movement to another partition based on the key column update.
3. Performance – Performance improvements include parallelism while
   creating indexes, materialized views, hash joins, and sequential scans to
   make the operations perform better.
4. Stored procedures – SQL stored procedures now added support for
   embedded transactions.
5. Autovacuum improvements – To provide valuable logging, the
   parameter `rds.force_autovacuum_logging` is ON by default in
   conjunction with the `log_autovacuum_min_duration` parameter set
   to 10 seconds. To increase autovacuum effectiveness, the values for the
   `autovacuum_max_workers` and
   `autovacuum_vacuum_cost_limit` parameters are computed based
   on host memory capacity to provide larger default values.
6. Improved transaction timeout – The parameter
   `idle_in_transaction_session_timeout` is set to 24 hours. Any
   session that has been idle more than 24 hours is terminated.
7. The `tsearch2` module is no longer supported – If your
   application uses `tsearch2` functions, update it to use the
   equivalent functions provided by the core PostgreSQL engine. For more
   information about the tsearch2 module, see [PostgreSQL
   tsearch2](https://www.postgresql.org/docs/9.6/tsearch2.html "https://www.postgresql.org/docs/9.6/tsearch2.html").
8. The `chkpass` module is no longer supported – For more
   information about the chkpass module, see [PostgreSQL
   chkpass](https://www.postgresql.org/docs/10/chkpass.html "https://www.postgresql.org/docs/10/chkpass.html").
9. Updated the following extensions:
   - `address_standardizer` to version 2.5.1
   - `address_standardizer_data_us` to version 2.5.1
   - `btree_gin` to version 1.3
   - `citext` to version 1.5
   - `cube` to version 1.4
   - `hstore` to version 1.5
   - `ip4r` to version 2.2
   - `isn` to version 1.2
   - `orafce` to version 3.7
   - `pg_hint_plan` to version 1.3.4
   - `pg_prewarm` to version 1.2
   - `pg_repack` to version 1.4.4
   - `pg_trgm` to version 1.4
   - `pgaudit` to version 1.3
   - `pgrouting` to version 2.6.1
   - `pgtap` to version 1.0.0
   - `plcoffee` to version 2.3.8
   - `plls` to version 2.3.8
   - `plv8` to version 2.3.8
   - `postgis` to version 2.5.1
   - `postgis_tiger_geocoder` to version 2.5.1
   - `postgis_topology` to version 2.5.1
   - `rds_activity_stream` to version 1.3

## PostgreSQL 10 versions

(Deprecated)

###### Version updates

- [PostgreSQL 10.21
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1021X "#AuroraPostgreSQL.Updates.20180305.1021X")
- [PostgreSQL 10.20
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1020X "#AuroraPostgreSQL.Updates.20180305.1020X")
- [PostgreSQL 10.19
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1019 "#AuroraPostgreSQL.Updates.20180305.1019")
- [PostgreSQL 10.18
  (Deprecated)](#AuroraPostgreSQL.Updates.20180305.1018 "#AuroraPostgreSQL.Updates.20180305.1018")
- [PostgreSQL 10.17,
  Aurora PostgreSQL 2.9 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.29 "#AuroraPostgreSQL.Updates.20180305.29")
- [PostgreSQL 10.16,
  Aurora PostgreSQL 2.8 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.28 "#AuroraPostgreSQL.Updates.20180305.28")
- [PostgreSQL 10.14,
  Aurora PostgreSQL 2.7 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.27 "#AuroraPostgreSQL.Updates.20180305.27")
- [PostgreSQL 10.13,
  Aurora PostgreSQL 2.6 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.26 "#AuroraPostgreSQL.Updates.20180305.26")
- [PostgreSQL 10.12,
  Aurora PostgreSQL 2.5 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.25 "#AuroraPostgreSQL.Updates.20180305.25")
- [PostgreSQL 10.11,
  Aurora PostgreSQL 2.4 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.24 "#AuroraPostgreSQL.Updates.20180305.24")
- [PostgreSQL 10.7,
  Aurora PostgreSQL 2.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.23 "#AuroraPostgreSQL.Updates.20180305.23")
- [PostgreSQL 10.6,
  Aurora PostgreSQL 2.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.22 "#AuroraPostgreSQL.Updates.20180305.22")
- [PostgreSQL 10.5,
  Aurora PostgreSQL 2.1 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.21 "#AuroraPostgreSQL.Updates.20180305.21")
- [PostgreSQL 10.4,
  Aurora PostgreSQL 2.0 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.20 "#AuroraPostgreSQL.Updates.20180305.20")

### PostgreSQL 10.21

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.21. For more
information about the improvements in PostgreSQL 10.21, see [PostgreSQL release
10.21](https://www.postgresql.org/docs/13/release-10-21.html "https://www.postgresql.org/docs/13/release-10-21.html").

###### Releases and patches

- [Aurora PostgreSQL
  10.21.5, December 14, 2022](#AuroraPostgreSQL.Updates.20180305.10215 "#AuroraPostgreSQL.Updates.20180305.10215")
- [Aurora PostgreSQL
  10.21.4, November 17, 2022](#AuroraPostgreSQL.Updates.20180305.10214 "#AuroraPostgreSQL.Updates.20180305.10214")
- [Aurora PostgreSQL
  10.21.3, October 13, 2022](#AuroraPostgreSQL.Updates.20180305.10213 "#AuroraPostgreSQL.Updates.20180305.10213")
- [Aurora PostgreSQL
  10.21.1, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.10211 "#AuroraPostgreSQL.Updates.20180305.10211")
- [Aurora PostgreSQL
  10.21.0, June 9, 2022](#AuroraPostgreSQL.Updates.20180305.10210 "#AuroraPostgreSQL.Updates.20180305.10210")

#### Aurora PostgreSQL

10.21.5, December 14, 2022

###### General stability enhancements

- Fixed an issue where the engine experienced stability issues.

#### Aurora PostgreSQL

10.21.4, November 17, 2022

###### High priority stability enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.

#### Aurora PostgreSQL

10.21.3, October 13, 2022

###### High priority stability enhancements

- Fixed a `PLV8` issue where the base parameter doesn't
  get loaded properly into the memory.

###### General stability enhancements

- Fixed a bug where Aurora PostgreSQL can't file the relfilenode.
- Fixed a stuck scaling issue when the current scaling event times out.
- Upgraded the `PostGIS` extension to version 3.1.7.
- Fixed an issue where extended query messages might be lost during
  zero-downtime patching (ZDP) causing the extended query to hang after
  the ZDP completion.

#### Aurora PostgreSQL

10.21.1, July 6, 2022

###### Critical stability enhancements

- Fixed an issue that could cause periods of unavailability during a
  storage node restart.

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue when the connection to SQL Server fails using the
  `TDS_FDW` extension to query a foreign table.
- Fixed an issue that caused connections using the provided root
  certificate to fail.
- Improved the diagnostic and supportability information in case of
  inconsistent B-tree index entries.

#### Aurora PostgreSQL

10.21.0, June 9, 2022

###### New features

- Added support for the `large object` module (extension).
  For more information, see [Managing large objects with the lo module](../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md "../AuroraUserGuide/PostgreSQL_large_objects_lo_extension.md").
- Added support for zero-downtime patching (ZDP) for minor version
  upgrades and patches. For more information, see [Minor release upgrades and zero-downtime patching](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.Minor") in the
  _Amazon Aurora User Guide_.

###### Critical updates

- Fixed a replay crash due to an LSN mismatch.
- Fixed the `aws_s3` extension to prevent invalid region
  injection.

###### High stability updates

- Fixed multiple issues related to out-of-memory conditions which could
  result in brief periods of unavailability.

###### General stability updates

- Fixed a lock contention crash during an Aurora Serverless v1 scaling event.
- Fixed an issue where logical replication becomes stuck after a
  restart.
- Fixed multiple issues that could lead to brief periods of
  unavailability.
- Fixed, during redo, an invalid page hit on the Generic Redo for
  GENERIC_XLOG_FULL_PAGE_DATA. This happens due to a timing hole between
  generating the log record and then writing the metadata for the record
  on the RW node and the RO node replays between those operations.
- Improved the query performance by supporting parallel workers.
- Upgraded the plugin `wal2json` version to 2.4.
- Upgraded the `pglogical` extension to version 2.4.1.

### PostgreSQL 10.20

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.20. For more
information about the improvements in PostgreSQL 10.20, see [PostgreSQL release
10.20](https://www.postgresql.org/docs/13/release-10-20.html "https://www.postgresql.org/docs/13/release-10-20.html").

###### Releases and patches

- [Aurora PostgreSQL
  10.20.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.10206 "#AuroraPostgreSQL.Updates.20180305.10206")
- [Aurora PostgreSQL
  10.20.4, July 18, 2022](#AuroraPostgreSQL.Updates.20180305.10204 "#AuroraPostgreSQL.Updates.20180305.10204")
- [Aurora PostgreSQL
  10.20.1, April 27, 2022](#AuroraPostgreSQL.Updates.20180305.10201 "#AuroraPostgreSQL.Updates.20180305.10201")
- [Aurora PostgreSQL
  10.20.0, March 29, 2022](#AuroraPostgreSQL.Updates.20180305.10200 "#AuroraPostgreSQL.Updates.20180305.10200")

#### Aurora PostgreSQL

10.20.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.
- Updated the PostGIS extension to version 3.1.7.

#### Aurora PostgreSQL

10.20.4, July 18, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in
  periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that
  could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files
  that could result in periods of unavailability.
- Fixed a defect where the validation of cached plans may lead to a
  database restart when the plan was previously invalidated.

#### Aurora PostgreSQL

10.20.1, April 27, 2022

###### High priority stability enhancements

- Fixed an issue that could cause incorrect `WriteIOPS`
  reporting in the AWS console.
- Fixed an issue that could cause unavailability after removal of a
  read node from a cluster.

###### General enhancements

- Fixed an issue that could cause an engine restart during periods of
  low free memory.

#### Aurora PostgreSQL

10.20.0, March 29, 2022

###### High priority stability enhancements

- Fixed multiple issues that may result in unavailability of a read
  node.
- Fixed an issue that may result in a read node being unable to replay
  WAL requiring the replication slot to be dropped and resynchronized.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.

###### General enhancements

- Fixed a small memory leak on read nodes when `commit_ts`
  is set.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".
- Fixed an issue that could cause an import from S3 to fail when using
  the `aws_s3` extension.
- Fixed multiple issues that could result in periods of unavailability
  when using `apg_plan_mgmt`.
- Fixed multiple issues that could result in periods of unavailability
  when QPM is enabled.

### PostgreSQL 10.19

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.19. For more
information about the improvements in PostgreSQL 10.19, see [PostgreSQL release
10.19](https://www.postgresql.org/docs/10/release-10-19.html "https://www.postgresql.org/docs/10/release-10-19.html").

###### Releases and patches

- [Aurora PostgreSQL
  10.19.6, December 16, 2022](#AuroraPostgreSQL.Updates.20180305.10196 "#AuroraPostgreSQL.Updates.20180305.10196")
- [Aurora PostgreSQL
  10.19.4, July 20, 2022](#AuroraPostgreSQL.Updates.20180305.10194 "#AuroraPostgreSQL.Updates.20180305.10194")
- [Aurora PostgreSQL
  10.19.3, April 13, 2022](#AuroraPostgreSQL.Updates.20180305.10193 "#AuroraPostgreSQL.Updates.20180305.10193")
- [Aurora PostgreSQL
  10.19.1](#AuroraPostgreSQL.Updates.20180305.10191 "#AuroraPostgreSQL.Updates.20180305.10191")
- [Aurora PostgreSQL
  10.19.0](#AuroraPostgreSQL.Updates.20180305.10190 "#AuroraPostgreSQL.Updates.20180305.10190")

#### Aurora PostgreSQL

10.19.6, December 16, 2022

###### General enhancements

- Fixed an issue that can cause increased network traffic when a writer
  instance transmits logs to a replica instance.
- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.
- Updated the PostGIS extension to version 3.1.7.

#### Aurora PostgreSQL

10.19.4, July 20, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### Critical enhancements

- Fixed an issue during a storage node restart that could result in
  periods of unavailability.

###### High stability enhancements

- Fixed an error handling issue related to out-of-memory conditions that
  could result in brief periods of unavailability.
- Fixed an issue related to the existence of duplicate relation files
  that could result in periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".

#### Aurora PostgreSQL

10.19.3, April 13, 2022

###### General enhancements

- Fixed a bug that could cause an engine restart during periods of low
  free memory.

#### Aurora PostgreSQL

10.19.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to
  3.1.5. This update contains a PostGIS fix for the vulnerability
  addressed in core PostgreSQL by CVE-2020-14350. For more information,
  see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL

10.19.0

###### Critical stability enhancements

- Fixed a bug where logical replication may hang resulting in the
  replay falling behind on the read node. The instance may eventually
  restart.

###### Additional improvements and enhancements

- Fixed a buffer cache bug that could cause brief periods of
  unavailability.
- Fixed a bug in the `apg_plan_mgmt` extension where an
  index based plan was not being enforced.
- Fixed a bug in the `pg_logical` extension that could cause
  brief periods of unavailability due to improper handling of NULL
  arguments.
- Fixed an issue where orphaned files caused major version upgrades to
  fail.
- Fixed incorrect Aurora Storage Daemon log write metrics.
- Fixed multiple bugs that could result in WAL replay falling behind
  and eventually causing the reader instances to restart.
- Improved the Aurora buffer cache page validation on reads.
- Improved the Aurora storage metadata validation.
- Updated the `pg_hint_pan` extension to v1.3.6.

### PostgreSQL 10.18

(Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.18. For more
information about the improvements in PostgreSQL 10.18, see [PostgreSQL release
10.18](https://www.postgresql.org/docs/12/release-10-18.html "https://www.postgresql.org/docs/12/release-10-18.html").

###### Releases and patches

- [Aurora PostgreSQL
  10.18.6, December 19, 2022](#AuroraPostgreSQL.Updates.20180305.10186 "#AuroraPostgreSQL.Updates.20180305.10186")
- [Aurora PostgreSQL
  10.18.4, July 6, 2022](#AuroraPostgreSQL.Updates.20180305.10184 "#AuroraPostgreSQL.Updates.20180305.10184")
- [Aurora PostgreSQL
  10.18.3, June 6, 2022](#AuroraPostgreSQL.Updates.20180305.10183 "#AuroraPostgreSQL.Updates.20180305.10183")
- [Aurora PostgreSQL
  10.18.2, April 12, 2022](#AuroraPostgreSQL.Updates.20180305.10182 "#AuroraPostgreSQL.Updates.20180305.10182")
- [Aurora PostgreSQL
  10.18.1](#AuroraPostgreSQL.Updates.20180305.10181 "#AuroraPostgreSQL.Updates.20180305.10181")
- [Aurora PostgreSQL
  10.18.0](#AuroraPostgreSQL.Updates.20180305.10180 "#AuroraPostgreSQL.Updates.20180305.10180")

#### Aurora PostgreSQL

10.18.6, December 19, 2022

###### General enhancements

- Fixed an issue that causes database activity stream inconsistency when
  the monitoring agent is unavailable.

#### Aurora PostgreSQL

10.18.4, July 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### General enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that could cause Performance Insights to display
  "Unknown wait event".
- Fixed an issue that could result in periods of unavailability due to
  the existence of duplicate relation files.

#### Aurora PostgreSQL

10.18.3, June 6, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability updates

- Fixed an issue that can cause a restart of the postmaster process in
  Amazon Aurora Serverless v1.
- Fixed an issue that can cause a restart of the Aurora Runtime process
  in Amazon Aurora Serverless v1.

###### General enhancements

- Fixed a memory leak in the Aurora Runtime that could lead to an
  out-of-memory condition.

#### Aurora PostgreSQL

10.18.2, April 12, 2022

###### General updates

- Fixed a buffer cache bug that could cause brief periods of
  unavailability.

#### Aurora PostgreSQL

10.18.1

###### Security enhancements

- Updated the `PostGIS` extension from version 3.1.4 to
  3.1.5. This update contains a PostGIS fix for the vulnerability
  addressed in core PostgreSQL by CVE-2020-14350. For more information,
  see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL

10.18.0

###### Critical stability updates

- Fixed an issue where, in rare circumstances, a data cache of a read
  node may be inconsistent following a restart of that node.

###### High priority stability updates

- Fixed an issue where queries may become unresponsive due to I/O
  resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major
  version update with the message: "PANIC: could not access status of next
  transaction id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue which can cause vacuum operations to become blocked
  after all Aurora read replicas have been removed from a secondary
  cluster.
- Fixed an issue where read nodes restart due to a replication origin
  cache lookup failure.
- Fixed an issue where read queries may time out on read nodes during
  the replay of lazy truncation triggered by vacuum on the write node.
- Fixed an issue that causes Performance Insights to incorrectly set
  the backend type of a database connection.
- Fixed an issue where the aurora_postgres_replica_status() function
  returned stale or lagging CPU stats.
- Fixed an issue where, in rare cases, an Aurora Global Database
  secondary mirror cluster may restart due to a stall in the log apply
  process.
- Removed support for the DES, 3DES, and RC4 cipher suites.
- Updated `PostGIS` extension to version 3.1.4.
- Added support for `postgis_raster` extension version
  3.1.4.

### PostgreSQL 10.17,

Aurora PostgreSQL 2.9 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.17. For more
information about the improvements in PostgreSQL 10.17, see [PostgreSQL release
10.17](https://www.postgresql.org/docs/11/release-10-17.html "https://www.postgresql.org/docs/11/release-10-17.html").

###### Releases and patches

- [Aurora PostgreSQL
  10.17.5, December 30, 2022](#AuroraPostgreSQL.Updates.20180305.10175 "#AuroraPostgreSQL.Updates.20180305.10175")
- [Aurora PostgreSQL
  10.17.4, July 14, 2022](#AuroraPostgreSQL.Updates.20180305.10174 "#AuroraPostgreSQL.Updates.20180305.10174")
- [Aurora PostgreSQL
  2.9.2](#AuroraPostgreSQL.Updates.20180305.10171 "#AuroraPostgreSQL.Updates.20180305.10171")
- [Aurora PostgreSQL
  2.9.1](#AuroraPostgreSQL.Updates.20180305.10170 "#AuroraPostgreSQL.Updates.20180305.10170")
- [Aurora PostgreSQL
  2.9](#AuroraPostgreSQL.Updates.20180305.290 "#AuroraPostgreSQL.Updates.20180305.290")

#### Aurora PostgreSQL

10.17.5, December 30, 2022

###### General enhancements

- Amazon Aurora PostgreSQL version 10.17.5 was released with general
  enhancements.

#### Aurora PostgreSQL

10.17.4, July 14, 2022

###### Security enhancements

- Backpatched the PostgreSQL community fix for CVE-2022-1552:
  Autovacuum, REINDEX, and others omit "security restricted operation".
  For more information, see [CVE-2022-1552](https://www.postgresql.org/support/security/CVE-2022-1552 "https://www.postgresql.org/support/security/CVE-2022-1552").

###### High priority stability enhancements

- Fixed an error handling issue related to out-of-memory conditions
  which could result in brief periods of unavailability.
- Fixed an issue that could cause excess storage use due to files not
  being properly closed.
- Fixed an issue that caused Performance Insights to show "Unknown wait
  event".

#### Aurora PostgreSQL

2.9.2

###### Security enhancements

- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to `PostGIS` 2.4.7. This is a
  `PostGIS` fix for the vulnerability addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").

#### Aurora PostgreSQL

2.9.1

###### Critical stability updates

- Fixed an issue where, in rare circumstances, a data cache of a read
  node may be inconsistent following a restart of that node.

###### High priority stability updates

- Fixed an issue where queries may become unresponsive due to I/O
  resource exhaustion triggered by prefetch.
- Fixed an issue where Aurora may flag an issue following a major version
  update with the message: "PANIC: could not access status of next
  transaction id xxxxxxxx".

###### Additional improvements and enhancements

- Fixed an issue where read nodes restart due to a replication origin
  cache lookup failure.
- Fixed an issue where in rare cases, an Aurora Global Database secondary
  mirror cluster may restart due to a stall in the log apply
  process.
- Fixed an issue that causes Performance Insights to incorrectly set the
  backend type of a database connection.
- Fixed an issue where orphaned files caused failed translations in read
  codepaths during or after major version upgrade.
- Fixed multiple issues in the Aurora storage daemon that could lead to
  brief periods of unavailability when specific network configurations are
  used.
- Fixed an out-of-memory crash issue with Aurora storage daemon that
  leads to writer node restart. This also reduces the overall system
  memory consumption.

#### Aurora PostgreSQL

2.9

###### High priority stability updates

1. Fixed an issue where creating a database from an existing template
   database with tablespace resulted in an error with the message
   `ERROR: could not open file pg_tblspc/...: No such file or
directory`.
2. Fixed an issue where, in rare cases, an Aurora replica may be unable to
   start when a large number of PostgreSQL subtransactions (i.e. SQL
   savepoints) have been used.
3. Fixed an issue where, in rare circumstances, read results may be
   inconsistent for repeated read requests on replica nodes.

###### Additional improvements and enhancements

1. Upgraded OpenSSL to 1.1.1k.
2. Reduced CPU usage and memory consumption of the WAL apply process on
   Aurora replicas for some workloads.
3. Improved safety checks in the write path to detect incorrect writes
   to metadata.
4. Improved security by removing 3DES and other older ciphers for
   SSL/TLS connections.
5. Fixed an issue where a duplicate file entry can prevent the Aurora
   PostgreSQL engine from starting up.
6. Fixed an issue that could cause temporary unavailability under heavy
   workloads.
7. Added back ability to use a leading forward slash in the S3 path
   during S3 import.
8. Updated the orafce extension to version 3.16.
9. Updated the `PostGIS` extension to version 2.4.7.

### PostgreSQL 10.16,

Aurora PostgreSQL 2.8 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.16. For more
information about the improvements in PostgreSQL 10.16, see [PostgreSQL release
10.16](https://www.postgresql.org/docs/10/release-10-16.html "https://www.postgresql.org/docs/10/release-10-16.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.8.1](#AuroraPostgreSQL.Updates.20180305.281 "#AuroraPostgreSQL.Updates.20180305.281")
- [Aurora PostgreSQL
  2.8.0](#AuroraPostgreSQL.Updates.20180305.280 "#AuroraPostgreSQL.Updates.20180305.280")

#### Aurora PostgreSQL

2.8.1

###### Security enhancements

- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to `PostGIS` 2.4.4. This is a
  `PostGIS` fix for the vulnerability addressed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw`
  extension function parameters.

#### Aurora PostgreSQL

2.8.0

###### High priority stability updates

1. Fixed a bug where in rare cases a reader had inconsistent results when
   it restarted while a transaction with more than 64 subtransactions was
   being processed.
2. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2021-32027](https://nvd.nist.gov/vuln/detail/CVE-2021-32027 "https://nvd.nist.gov/vuln/detail/CVE-2021-32027")
   - [CVE-2021-32028](https://nvd.nist.gov/vuln/detail/CVE-2021-32028 "https://nvd.nist.gov/vuln/detail/CVE-2021-32028")
   - [CVE-2021-32029](https://nvd.nist.gov/vuln/detail/CVE-2021-32029 "https://nvd.nist.gov/vuln/detail/CVE-2021-32029")

###### Additional improvements and enhancements

1. Fixed a bug where the database could not be started when there were
   many relations in memory-constrained environments.
2. Fixed a bug in the `apg_plan_mgmt` extension that could
   cause brief periods of unavailability due to an internal buffer
   overflow.
3. Fixed a bug on reader nodes that could cause brief periods of
   unavailability during WAL replay.
4. Fixed a bug in the `rds_activity_stream` extension that
   caused an error during startup when attempting to log audit
   events.
5. Fixed a bug that prevented minor version updates of an Aurora global
   database cluster.
6. Fixed bugs in the `aurora_replica_status` function where
   rows were sometimes partially populated and some values such as Replay
   Latency, and CPU usage were always 0.
7. Fixed a bug where the database engine would attempt to create shared
   memory segments larger than the instance total memory and fail
   repeatedly. For example, attempts to create 128 GiB shared buffers on a
   db.r5.large instance would fail. With this change, requests for total
   shared memory allocations larger than the instance memory allow setting
   the instance to incompatible parameters.
8. Added logic to clean up unnecessary `pg_wal` temporary
   files on a database startup.
9. Fixed a bug that reported **`ERROR: rds_activity_stream stack
item 2 not found on top - cannot pop`** when attempting to
   create the `rds_activity_stream` extension.
10. Fixed a bug that could cause the error **`failed to build any
3-way joins`** in a correlated `IN` subquery
    under an `EXISTS` subquery.
11. Fixed a bug that could cause brief periods of unavailability due to
    running out of memory when creating the `postgis` extension
    with `pgAudit` enabled.
12. Fixed a bug when using outbound logical replication to synchronize
    changes to another database that could fail with an error message like
    **`ERROR: could not map filenode "base/16395/228486645" to
relation OID`**.
13. Fixed a bug where the `rds_ad` role wasn't created
    after upgrading from a version of Aurora PostgreSQL that doesn't
    support Microsoft Active Directory authentication.
14. Added btree page checks to detect tuple metadata inconsistency.
15. Fixed a bug in asynchronous buffer reads that could cause brief
    periods of unavailability on reader nodes during WAL replay.

### PostgreSQL 10.14,

Aurora PostgreSQL 2.7 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.14. For more
information about the improvements in PostgreSQL 10.14, see [PostgreSQL release
10.14](https://www.postgresql.org/docs/10/release-10-14.html "https://www.postgresql.org/docs/10/release-10-14.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.7.5](#AuroraPostgreSQL.Updates.20180305.275 "#AuroraPostgreSQL.Updates.20180305.275")
- [Aurora PostgreSQL
  2.7.3](#AuroraPostgreSQL.Updates.20180305.273 "#AuroraPostgreSQL.Updates.20180305.273")
- [Aurora PostgreSQL
  2.7.2](#AuroraPostgreSQL.Updates.20180305.272 "#AuroraPostgreSQL.Updates.20180305.272")
- [Aurora PostgreSQL
  2.7.1](#AuroraPostgreSQL.Updates.20180305.271 "#AuroraPostgreSQL.Updates.20180305.271")
- [Aurora PostgreSQL
  2.7.0](#AuroraPostgreSQL.Updates.20180305.270 "#AuroraPostgreSQL.Updates.20180305.270")

#### Aurora PostgreSQL

2.7.5

###### Security enhancements

- Modified the `ip4r` extension to mitigate a security issue
  during create extension. The issue was originally disclosed in core
  PostgreSQL by CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched [postgis](https://git.osgeo.org/gitea/postgis/postgis/pulls/79 "https://git.osgeo.org/gitea/postgis/postgis/pulls/79") to PostGIS 2.4.4. This is a `PostGIS`
  fix for the vulnerability addressed in core PostgreSQL by
  CVE-2020-14350. For more information, see [CVE-2020-14350](https://www.postgresql.org/support/security/CVE-2020-14350 "https://www.postgresql.org/support/security/CVE-2020-14350").
- Backpatched an input validation error in the `log_fdw`
  extension function parameters.

#### Aurora PostgreSQL

2.7.3

###### High priority stability updates

1. Provided a patch for PostgreSQL community security issues
   CVE-2021-32027, CVE-2021-32028 and CVE-2021-32029.

###### Additional improvements and enhancements

1. Fixed a bug in the `aws_s3` extension to allow import of
   objects with leading forward slashes in the object identifier.
2. Fixed a bug in the `rds_activity_stream` extension that
   caused an error during startup when attempting to log audit
   events.
3. Fixed a bug that returned an `ERROR` when attempting to
   create the `rds_activity_stream` extension.
4. Fixed a bug that could cause brief periods of unavailability due to
   running out of memory when creating the `postgis` extension
   with `pgAudit` enabled.
5. Fixed multiple issues in the Aurora storage daemon that could lead to
   brief periods of unavailability when specific network configurations are
   used.

#### Aurora PostgreSQL

2.7.2

###### High priority stability updates

1. Fixed a bug where a reader node might render an extra or missing row
   if the reader restarted while the writer node is processing a long
   transaction with more than 64 subtransactions.

###### Additional improvements and enhancements

1. Fixed a bug that could lead to intermittent unavailability due to the
   rotation of network encryption keys.
2. Fixed a bug where a large S3 import with thousands of clients can
   cause one or more of the import clients to stop responding.

#### Aurora PostgreSQL

2.7.1

###### Critical stability updates

1. Fixed a bug that caused a read replica to unsuccessfully restart
   repeatedly in rare cases.
2. Fixed a bug where a cluster became unavailable when attempting to
   create more than 16 read replicas or Aurora global database secondary
   AWS Regions. The cluster became available again when the new read
   replica or secondary AWS Region was removed.

###### Additional improvements and enhancements

1. Fixed a bug that when under heavy load, snapshot import, COPY import,
   or S3 import stopped responding in rare cases.
2. Fixed a bug where a read replica might not join the cluster when the
   writer was very busy with a write-intensive workload.
3. Fixed a bug that caused a cluster to take several minutes to restart
   if a logical replication stream was terminated while handling many
   complex transactions.
4. Disallowed the use of both IAM and Kerberos authentication for the
   same user.

#### Aurora PostgreSQL

2.7.0

###### Critical stability updates

- None

###### High priority stability updates

1. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

2. Fixed a bug in Aurora PostgreSQL replication that could result in the
   error message **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.
3. Fixed a bug where in some cases, DB clusters that have logical
   replication enabled did not remove truncated WAL segment files from
   storage. This resulted in volume size growth.
4. Fixed a bug in the `pg_stat_statements` extension that
   caused excessive CPU consumption.

###### Additional improvements and enhancements

1. Improved the asynchronous mode performance of database activity
   streams.
2. Aurora Serverless v1 for PostgreSQL now supports query execution on all
   connections during a scale event.
3. Reduced the delay when publishing to CloudWatch the
   `rpo_lag_in_msec` metric for Aurora global database
   clusters.
4. Fixed a bug in Serverless clusters where transaction processing was
   unnecessarily suspended for long periods when creating a scale
   point.
5. Fixed a bug in Aurora Serverless v1 for PostgreSQL where a leaked lock
   resulted in a prolonged scale event.
6. Fixed a bug in Aurora Serverless v1 for PostgreSQL where connections being
   migrated during a scale event was disconnected with the following
   message: **`ERROR: could not open relation with OID
...`**
7. Aurora PostgreSQL no longer falls behind on a read node when the backend
   is blocked writing to the database client.
8. Fixed a bug that in rare cases caused a brief period of unavailability
   on a read replica when the storage volume grew.
9. Fixed a bug when creating a database that could return the following
   error: **`ERROR: could not create directory on local
disk`**
10. Fixed a bug where in some cases replaying
    `XLOG_BTREE_REUSE_PAGE` records on Aurora reader instances
    caused unnecessary replay lag.
11. Fixed a bug in the `GiST` index that could result in an out
    of memory condition after promoting an Aurora read replica.
12. Fixed a bug where the `aurora_replica_status` function
    showed truncated server identifiers.
13. Fixed an S3 import bug that reported **`ERROR: HTTP 403.
Permission denied`** when importing data from a file inside
    an S3 subfolder.
14. Fixed a bug in the `aws_s3` extension for pre-signed URL
    handling that could result in the error message **`S3 bucket
names with a period (.) are not supported`**.
15. Fixed a bug in the `aws_s3` extension where an import might
    be blocked indefinitely if an exclusive lock was taken on the relation
    prior to beginning the operation.
16. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
    physical replica of an RDS for PostgreSQL instance that uses
    `GiST` indexes. In rare cases, this bug caused a brief
    period of unavailability after promoting the Aurora cluster.
17. Fixed a bug in database activity streams where customers were not
    notified of the end of an outage.

### PostgreSQL 10.13,

Aurora PostgreSQL 2.6 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.13. For more
information about the improvements in PostgreSQL 10.13, see [PostgreSQL release
10.13](https://www.postgresql.org/docs/10/release-10-13.html "https://www.postgresql.org/docs/10/release-10-13.html").

###### Releases and patches

- [Aurora PostgreSQL release
  2.6.2](#AuroraPostgreSQL.Updates.20180305.262 "#AuroraPostgreSQL.Updates.20180305.262")
- [Aurora PostgreSQL
  2.6.1](#AuroraPostgreSQL.Updates.20180305.261 "#AuroraPostgreSQL.Updates.20180305.261")
- [Aurora PostgreSQL
  2.6.0](#AuroraPostgreSQL.Updates.20180305.260 "#AuroraPostgreSQL.Updates.20180305.260")

#### Aurora PostgreSQL release

2.6.2

###### Critical stability updates

1. None

###### High priority stability updates

1. Fixed a bug in Aurora PostgreSQL replication that could result in the
   error message **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.
2. Fixed a bug where in some cases, DB clusters that have logical
   replication enabled did not remove truncated WAL segment files from
   storage. This resulted in volume size growth.
3. Fixed an issue with creating a global database cluster in a secondary
   region.
4. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

5. Fixed a bug in the `pg_stat_statements` extension that
   caused excessive CPU consumption.

###### Additional improvements and enhancements

1. Aurora PostgreSQL no longer falls behind on a read node when the backend
   is blocked writing to the database client.
2. Reduced the delay when publishing to CloudWatch the
   `rpo_lag_in_msec` metric for Aurora global database
   clusters.
3. Fixed a bug where a `DROP DATABASE` statement didn't
   remove any relation files.
4. Fixed a bug where in some cases replaying
   `XLOG_BTREE_REUSE_PAGE` records on Aurora reader instances
   caused unnecessary replay lag.
5. Fixed a small memory leak in a b-tree index that could lead to an out
   of memory condition.
6. Fixed a bug in the `aurora_replica_status()` function where
   the `server_id` field was sometimes truncated.
7. Fixed a bug where a log record was incorrectly processed causing the
   Aurora replica to crash.
8. Fixed an S3 import bug that reported **`ERROR: HTTP 403.
Permission denied`** when importing data from a file inside
   an S3 subfolder.
9. Improved performance of the asynchronous mode for database activity
   streams.
10. Fixed a bug in the `aws_s3` extension that could result in
    the error message **`S3 bucket names with a period (.) are not
supported`**.
11. Fixed a race condition that caused valid imports to intermittently
    fail.
12. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
    physical replica of an RDS for PostgreSQL instance that uses GiST indexes. In
    rare cases, this bug caused a brief period of unavailability after
    promoting the Aurora DB cluster.
13. Fixed a bug in the `aws_s3` extension where an import may
    be blocked indefinitely if an exclusive lock was taken on the relation
    prior to beginning the operation.

#### Aurora PostgreSQL

2.6.1

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug that appears when the `NOT EXISTS` operator
   incorrectly returns TRUE, which can only happen when the following unusual
   set of circumstances occurs:
   - A query is using the `NOT EXISTS` operator.
   - The column or columns being evaluated against the outer
     query in the `NOT EXISTS` subquery contain a NULL value.
   - There isn't a another predicate in the subquery that removes the need
     for the evaluation of the NULL values.
   - The filter used in the subquery does not use an index seek for its execution.
   - The operator isn't converted to a join by the query optimizer.

#### Aurora PostgreSQL

2.6.0

You can find the following improvements in this release.

###### New features

1. Added support for the RDKit extension version 3.8.

The RDKit extension provides modeling functions for cheminformatics.
Cheminformatics is storing, indexing, searching, retrieving, and
applying information about chemical compounds. For example, with the
RDKit extension you can construct models of molecules, search for
molecular structures, and read or create molecules in various notations.
You can also perform research on data loaded from the [ChEMBL website](https://www.ebi.ac.uk/chembl/ "https://www.ebi.ac.uk/chembl/") or a
SMILES file. The Simplified Molecular Input Line Entry System (SMILES)
is a typographical notation for representing molecules and reactions.
For more information, see [The RDKit database
cartridge](https://rdkit.org/docs/Cartridge.html "https://rdkit.org/docs/Cartridge.html") in the RDKit documentation. 2. Added support for the `pglogical` extension version
2.2.2.

The `pglogical` extension is a logical streaming
replication system that provides additional features beyond what's
available in PostgreSQL native logical replication. Features include
conflict handling, row filtering, DDL/sequence replication and delayed
apply. You can use the `pglogical` extension to set up
replication between Aurora PostgreSQL clusters, between RDS for PostgreSQL and
Aurora PostgreSQL, and with PostgreSQL databases running outside of
RDS. 3. Aurora dynamically resizes your cluster storage space. With dynamic
resizing, the storage space for your Aurora DB cluster automatically
decreases when you remove data from the DB cluster. For more
information, see [Storage scaling](../AuroraUserGuide/Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling "../AuroraUserGuide/Aurora.Managing.md#Aurora.Managing.Performance.StorageScaling") in the _Amazon Aurora User
Guide_.

###### Note

The dynamic resizing feature is being deployed in phases to the
AWS Regions where Aurora is available. Depending on the Region
where your cluster is, this feature might not be available yet. For
more information, see [the What's New announcement](https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-aurora-enables-dynamic-resizing-database-storage-space/ "https://aws.amazon.com/about-aws/whats-new/2020/10/amazon-aurora-enables-dynamic-resizing-database-storage-space/").

###### Critical stability updates

1. Fixed a bug related to heap page extend that in rare cases resulted in
   longer recovery time and impacted availability.

###### High priority stability updates

1. Fixed a bug when upgrading Aurora Global Database clusters from
   10.11.
2. Fixed a bug in Aurora Global Database that could cause delays in
   upgrading the database engine in a secondary AWS Region. For more
   information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
   User Guide_.
3. Fixed a bug that in rare cases caused delays in upgrading a database
   to engine version 10.13.

###### Additional improvements and enhancements

1. Fixed a bug where the Aurora replica crashed when workloads with heavy
   subtransactions are made on the writer instance.
2. Fixed a bug where the writer instance crashed due to a memory leak and
   the depletion of memory used to track active transactions.
3. Fixed a bug that lead to a crash due to improper initialization when
   there is no free memory available during PostgreSQL backend
   startup.
4. Fixed a bug where an Aurora PostgreSQL Serverless DB cluster might return
   the following error after a scaling event: **`ERROR: prepared
statement "S_6" already exists`**.
5. Fixed an out-of-memory problem when issuing the `CREATE
EXTENSION` command with `PostGIS` when Database
   Activity Streams is enabled.
6. Fixed a bug where a `SELECT` query might incorrectly return
   the error **`Attempting to read past EOF of relation rrrr.
blockno=bbb nblocks=nnn`**.
7. Fixed a bug where the database might be unavailable briefly due to
   error handling in database storage growth.
8. Fixed a bug in Aurora PostgreSQL Serverless where queries that executed on
   previously idle connections got delayed until the scale operation
   completed.
9. Fixed a bug where an Aurora PostgreSQL DB cluster with Database Activity
   Streams enabled might report the beginning of a potential loss window
   for activity records, but does not report the restoration of
   connectivity.

### PostgreSQL 10.12,

Aurora PostgreSQL 2.5 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.12. For more
information about the improvements in PostgreSQL 10.12, see [PostgreSQL release
10.12](https://www.postgresql.org/docs/10/release-10-12.html "https://www.postgresql.org/docs/10/release-10-12.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.5.7](#AuroraPostgreSQL.Updates.20180305.257 "#AuroraPostgreSQL.Updates.20180305.257")
- [Aurora PostgreSQL
  2.5.6](#AuroraPostgreSQL.Updates.20180305.256 "#AuroraPostgreSQL.Updates.20180305.256")
- [Aurora PostgreSQL
  2.5.4](#AuroraPostgreSQL.Updates.20180305.254 "#AuroraPostgreSQL.Updates.20180305.254")
- [Aurora PostgreSQL
  2.5.3](#AuroraPostgreSQL.Updates.20180305.253 "#AuroraPostgreSQL.Updates.20180305.253")
- [Aurora PostgreSQL
  2.5.2](#AuroraPostgreSQL.Updates.20180305.252 "#AuroraPostgreSQL.Updates.20180305.252")
- [Aurora PostgreSQL
  2.5.1](#AuroraPostgreSQL.Updates.20180305.251 "#AuroraPostgreSQL.Updates.20180305.251")

#### Aurora PostgreSQL

2.5.7

You can find the following improvements in this release.

###### Critical stability updates

- None

###### High priority stability updates

1. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

2.5.6

You can find the following improvements in this release.

###### Critical stability updates

- None

###### High priority stability updates

1. Fixed a bug in Aurora PostgreSQL replication that might result in the
   error message, **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.

###### Additional improvements and enhancements

1. Fixed a bug that in rare cases caused brief read replica
   unavailability when storage volume grew.
2. Aurora PostgreSQL Serverless now supports execution of queries on all
   connections during a scale event.
3. Fixed a bug in Aurora PostgreSQL Serverless where a leaked lock resulted
   in a prolonged scale event.
4. Fixed a bug where the `aurora_replica_status` function
   showed truncated server identifiers.
5. Fixed a bug in Aurora PostgreSQL Serverless where connections being
   migrated during a scale event disconnected with the message:
   "**`ERROR: could not open relation with OID
...`**.
6. Fixed a bug in a GiST index that might result in an out-of-memory
   condition after promoting an Aurora Read Replica.
7. Improved performance for Database Activity Streams.
8. Fixed a bug in Database Activity Streams where customers were not
   notified when an outage ended.
9. Fixed a bug in the `aws_s3` extension for pre-signed URL
   handling that could have resulted in the error message **`S3
bucket names with a period (.) are not supported`**.
10. Fixed a bug in the `aws_s3` extension where incorrect error
    handling could lead to failures during the import process.
11. Fixed a bug in the `aws_s3` extension where an import may
    be blocked indefinitely if an exclusive lock was taken on the relation
    prior to beginning the operation.

#### Aurora PostgreSQL

2.5.4

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug that appears when the `NOT EXISTS` operator
   incorrectly returns TRUE, which can only happen when the following unusual
   set of circumstances occurs:
   - A query is using the `NOT EXISTS` operator.
   - The column or columns being evaluated against the outer
     query in the `NOT EXISTS` subquery contain a NULL value.
   - There isn't a another predicate in the subquery that removes the need
     for the evaluation of the NULL values.
   - The filter used in the subquery does not use an index seek for its execution.
   - The operator isn't converted to a join by the query optimizer.

#### Aurora PostgreSQL

2.5.3

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- None

###### Additional improvements and enhancements

1. Fixed a bug in Aurora PostgreSQL Serverless where queries that ran on
   previously idle connections got delayed until the scale operation
   completed.
2. Fixed a bug that might cause brief unavailability for heavy
   subtransaction workloads when multiple reader instances restart or
   rejoin the cluster.
3. Fixed a bug in Aurora PostgreSQL Global Database where upgrading a
   secondary cluster might result in failure due to incorrect checksum
   versioning. This might have required re-creating the secondary
   clusters.

#### Aurora PostgreSQL

2.5.2

You can find the following improvements in this release.

###### Critical stability updates

1. Fixed a bug related to heap page extend that in rare cases resulted in
   longer recovery time and impacted availability.

###### High priority stability updates

1. Fixed a bug in Aurora Global Database that could cause delays in
   upgrading the database engine in a secondary region. For more
   information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
   User Guide_.
2. Fixed a bug that in rare cases caused delays in upgrading a database
   to engine version 10.12.

###### Additional improvements and enhancements

1. Fixed a bug where the database might be unavailable briefly due to
   error handling in database storage growth.
2. Fixed a bug where a SELECT query might incorrectly return the error,
   **`Attempting to read past EOF of relation rrrr. blockno=bbb
nblocks=nnn`**.
3. Fixed a bug where an Aurora PostgreSQL Serverless DB cluster might return
   the following error after a scaling event: **`ERROR: prepared
statement "S_6" already exists`**.

#### Aurora PostgreSQL

2.5.1

###### New features

1. Added support for Amazon Aurora PostgreSQL Global Database. For more
   information, see [Using Amazon Aurora global databases](../AuroraUserGuide/aurora-global-database.md "../AuroraUserGuide/aurora-global-database.md") in the _Amazon Aurora
   User Guide_.
2. Added the ability to configure the recovery point objective (RPO) of a
   global database for Aurora PostgreSQL. For more information, see [Managing RPOs for Aurora PostgreSQL–based global databases](../AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery "../AuroraUserGuide/aurora-global-database-disaster-recovery.md#aurora-global-database-manage-recovery") in
   the _Amazon Aurora User Guide_.

You can find the following improvements in this release.

###### Critical stability updates

None.

###### High priority stability updates

1. Improved performance and availability of read instances when applying
   DROP TABLE and TRUNCATE TABLE operations.
2. Fixed a small but continuous memory leak in a diagnostic module that
   could lead to an out-of-memory condition on smaller DB instance
   types.
3. Fixed a bug in the `PostGIS` extension which could lead to
   a database restart. This has been reported to the PostGIS community as
   [https://trac.osgeo.org/postgis/ticket/4646](https://trac.osgeo.org/postgis/ticket/4646 "https://trac.osgeo.org/postgis/ticket/4646").
4. Fixed a bug where read requests might stop responding due to incorrect
   error handling in the storage engine.
5. Fixed a bug that fails for some queries and results in the message
   **`ERROR: found xmin xxxxxx from before relfrozenxid
yyyyyyy`**. This could occur following the promotion of a
   read instance to a write instance.
6. Fixed a bug where an Aurora serverless DB cluster might crash while
   rolling back a scale attempt.

###### Additional improvements and enhancements

1. Improved performance for queries that read many rows from
   storage.
2. Improved performance and availability of reader DB instances during
   heavy read workload.
3. Enabled correlated IN and NOT IN subqueries to be transformed to joins
   when possible.
4. Improved read performance of the `pg_prewarm`
   extension.
5. Fixed a bug where an Aurora serverless DB cluster might report the
   message **`ERROR: incorrect binary data format in bind parameter
...`** following a scale event.
6. Fixed a bug where a serverless DB cluster might report the message
   **`ERROR: insufficient data left in message`**
   following a scale event.
7. Fixed a bug where an Aurora serverless DB cluster may experience
   prolonged or failed scale attempts.
8. Fixed a bug that resulted in the message **`ERROR: could not
create file "base/xxxxxx/yyyyyyy" as a previous version still exists
on disk: Success. Please contact AWS customer support`**.
   This can occur during object creation after PostgreSQL's 32-bit
   object identifier has wrapped around.
9. Fixed a bug where the write-ahead-log (WAL) segment files for
   PostgreSQL logical replication were not deleted when changing the
   `wal_level` value from `logical` to
   `replica`.
10. Fixed a bug in the `pg_hint_plan` extension where a
    multi-statement query could lead to a crash when
    `enable_hint_table` is enabled. This is tracked in the
    PostgreSQL community as [https://github.com/ossc-db/pg_hint_plan/issues/25](https://github.com/ossc-db/pg_hint_plan/issues/25 "https://github.com/ossc-db/pg_hint_plan/issues/25").
11. Fixed a bug where JDBC clients might report the message
    **`java.io.IOException: Unexpected packet type:
75`** following a scale event in an Aurora serverless DB
    cluster.
12. Fixed a bug in PostgreSQL logical replication that resulted in the
    message **`ERROR: snapshot reference is not owned by resource
owner TopTransaction`**.
13. Changed the following extensions:
    - Updated `orafce` to version 3.8

### PostgreSQL 10.11,

Aurora PostgreSQL 2.4 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.11. For more
information about the improvements in PostgreSQL 10.11, see [PostgreSQL release
10.11](https://www.postgresql.org/docs/10/release-10-11.html "https://www.postgresql.org/docs/10/release-10-11.html").

This release contains multiple critical stability updates. Amazon highly
recommends upgrading your Aurora PostgreSQL clusters that use older PostgreSQL 10
engines to this release.

###### Releases and patches

- [Aurora PostgreSQL
  2.4.4](#AuroraPostgreSQL.Updates.20180305.244 "#AuroraPostgreSQL.Updates.20180305.244")
- [Aurora PostgreSQL
  2.4.3](#AuroraPostgreSQL.Updates.20180305.243 "#AuroraPostgreSQL.Updates.20180305.243")
- [Aurora PostgreSQL
  2.4.2](#AuroraPostgreSQL.Updates.20180305.242 "#AuroraPostgreSQL.Updates.20180305.242")
- [Aurora PostgreSQL
  2.4.1](#AuroraPostgreSQL.Updates.20180305.241 "#AuroraPostgreSQL.Updates.20180305.241")
- [Aurora PostgreSQL
  2.4.0](#AuroraPostgreSQL.Updates.20180305.240 "#AuroraPostgreSQL.Updates.20180305.240")

#### Aurora PostgreSQL

2.4.4

You can find the following improvements in this release.

###### Critical stability updates

- None

###### High priority stability updates

1. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

2.4.3

###### New features

1. Aurora PostgreSQL now supports the PostgreSQL [vacuum_truncate](https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE "https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE") storage parameter to manage vacuum
   truncation for specific tables. Set this [storage parameter](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS "https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS") to false for a table to prevent the
   [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html") SQL command from truncating the table's
   trailing empty pages.

###### Critical stability updates

- None

###### High priority stability updates

1. Fixed a bug where reads from storage might stop responding due to
   incorrect error handling.

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

2.4.2

You can find the following improvements in this release.

###### Critical stability updates

1. Fixed a bug in which a reader DB instance might temporarily use stale
   data. This could lead to wrong results such as too few or too many rows.
   This error is not persisted on storage, and will clear when the database
   page containing the row has been evicted from cache. This can happen
   when the primary DB instance enters a transaction snapshot overflow due
   to having more than 64 subtransactions in a single transaction.
   Applications susceptible to this bug include those that use SQL
   savepoints or PostgreSQL exception handlers with more than 64
   subtransactions in the top transaction.

###### High priority stability updates

1. Fixed a bug that may cause a reader DB instance to crash causing
   unavailability while attempting to the join the DB cluster. This can
   happen in some cases when the primary DB instance has a transaction
   snapshot overflow due to a high number of subtransactions. In this
   situation the reader DB instance will be unable to join until the
   snapshot overflow has cleared.

###### Additional improvements and enhancements

1. Fixed a bug that prevented Performance Insights from determining the
   query ID of a running statement.

#### Aurora PostgreSQL

2.4.1

You can find the following improvements in this release.

###### Critical stability updates

1. Fixed a bug in which the DB instance might be briefly unavailable due
   to the self-healing function of the underlying storage.

###### High priority stability updates

1. Fixed a bug that might cause the database engine to crash causing
   unavailability. This occurred if a newly established database connection
   encountered a resource exhaustion-related error during initialization
   after successful authentication.

###### Additional improvements and enhancements

1. Provided a fix for the `pg_hint_plan` extension that could
   lead the database engine to crash causing unavailability. The open
   source issue can be tracked at [https://github.com/ossc-db/pg_hint_plan/pull/45](https://github.com/ossc-db/pg_hint_plan/pull/45 "https://github.com/ossc-db/pg_hint_plan/pull/45").
2. Fixed a bug where SQL of the form `ALTER FUNCTION ... OWNER TO
...` incorrectly reported `ERROR: improper qualified name
(too many dotted names)`.
3. Improved the performance of `GIN` index vacuum via
   prefetching.
4. Fixed a bug in open source PostgreSQL that could lead to a database
   engine crash causing unavailability. This occurred during parallel
   B-Tree index scans. This issue has been reported to the PostgreSQL
   community.
5. Improved the performance of in-memory B-Tree index scans.
6. Additional general improvements to the stability and availability of
   Aurora PostgreSQL.

#### Aurora PostgreSQL

2.4.0

You can find the following new features and improvements in this engine
version.

###### New features

1.  Support for exporting data to Amazon S3. For more information, see [Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](../AuroraUserGuide/postgresql-s3-export.md "../AuroraUserGuide/postgresql-s3-export.md") in
    the _Amazon Aurora User Guide_.
2.  Support for Amazon Aurora Machine Learning. For more information, see
    [Using
    machine learning (ML) with Aurora PostgreSQL](../AuroraUserGuide/postgresql-ml.md "../AuroraUserGuide/postgresql-ml.md") in the
    _Amazon Aurora User Guide_.
3.  SQL processing enhancements include:

        * Optimizations for `NOT IN` with the
         `apg_enable_not_in_transform` parameter.
        * Semi-join filter pushdown enhancements for hash joins with the
         `apg_enable_semijoin_push_down` parameter.
        * Optimizations for redundant inner join removal with the
         `apg_enable_remove_redundant_inner_joins`
         parameter.
        * Improved ANSI compatibility options with the
         `ansi_constraint_trigger_ordering`,
         `ansi_force_foreign_key_checks` and
         `ansi_qualified_update_set_target`
         parameters.

    For more information, see [Amazon Aurora PostgreSQL parameters](../AuroraUserGuide/AuroraPostgreSQL.Reference.md "../AuroraUserGuide/AuroraPostgreSQL.Reference.md") in the _Amazon Aurora
    User Guide_.

4.  New and updated PostgreSQL extensions include:
    - The new `aws_ml` extension. For more information,
      see [Using machine learning (ML) with Aurora PostgreSQL](../AuroraUserGuide/postgresql-ml.md "../AuroraUserGuide/postgresql-ml.md") in
      the _Amazon Aurora User Guide_.
    - The new `aws_s3` extension. For more information,
      see [Exporting data from an Aurora PostgreSQL DB cluster to
      Amazon S3](../AuroraUserGuide/postgresql-s3-export.md "../AuroraUserGuide/postgresql-s3-export.md") in the _Amazon Aurora User
      Guide_.
    - Updates to the `apg_plan_mgmt` extension. For more
      information, see [Managing query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md")
      in the _Amazon Aurora User Guide_.

###### Critical stability updates

1. Fixed a bug related to creating B-tree indexes on temporary tables
   that in rare cases may result in longer recovery time, and impact
   availability.
2. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
   physical replica of an RDS for PostgreSQL instance. In rare cases, this bug
   causes a log write failure that may result in longer recovery time, and
   impact availability.
3. Fixed a bug related to handling of reads with high I/O latency that in
   rare cases may result in longer recovery time, and impact
   availability.

###### High priority stability updates

1. Fixed a bug related to logical replication in which `wal`
   segments are not properly removed from storage. This can result in
   storage bloat. To monitor this, view the
   `TransactionLogDiskUsage` parameter.
2. Fixed multiple bugs, which cause Aurora to crash during prefetch
   operations on Btree indexes.
3. Fixed a bug in which an Aurora restart may timeout when logical
   replication is used.
4. Enhanced the validation checks performed on data blocks in the buffer
   cache. This improves Aurora's detection of inconsistency.

###### Additional improvements and enhancements

1. The query plan management extension `apg_plan_mgmt` has an
   improved algorithm for managing plan generation for highly partitioned
   tables.
2. Reduced startup time on instances with large caches via improvements
   in the buffer cache recovery algorithm.
3. Improved the performance of the read-node-apply process under high
   transaction rate workloads by using changes to PostgreSQL
   `LWLock` prioritization. These changes prevent starvation
   of the read-node-apply process while the PostgreSQL
   `ProcArray` is under heavy contention.
4. Improved handling of batch reads during vacuum, table scans, and index
   scans. This results in greater throughput and lower CPU
   consumption.
5. Fixed a bug in which a read node may crash during the replay of a
   PostgreSQL `SLRU`-truncate operation.
6. Fixed a bug where in rare cases, database writes may stall following
   an error returned by one of the six copies of an Aurora log record.
7. Fixed a bug related to logical replication where an individual
   transaction larger than 1 GB in size may result in an engine
   crash.
8. Fixed a memory leak on read nodes when cluster cache management is
   enabled.
9. Fixed a bug in which importing an RDS for PostgreSQL snapshot might stop
   responding if the source snapshot contains a large number of unlogged
   relations.
10. Fixed a bug in which the Aurora storage daemon may crash under heavy
    I/O load.
11. Fixed a bug related to `hot_standby_feedback` for read
    nodes in which the read node may report the wrong transaction id epoch
    to the write node. This can cause the write node to ignore the
    `hot_standby_feedback` and invalidate snapshots on the
    read node.
12. Fixed a bug in which storage errors that occur during `CREATE
DATABASE` statements are not properly handled. The bug left
    the resulting database inaccessible. The correct behavior is to fail the
    database creation and return the appropriate error to the user.
13. Improved handling of PostgreSQL snapshot overflow when a read node
    attempts to connect to a write node. Prior to this change, if the write
    node was in a snapshot overflow state, the read node was unable to join.
    A message appeared in the PostgreSQL log file in the form `DEBUG:
recovery snapshot waiting for non-overflowed snapshot or until
oldest active xid on standby is at least
`xxxxxxx`(now`yyyyyyy`)`. A snapshot overflow
    occurs when an individual transaction has created over 64
    subtransactions.
14. Fixed a bug related to common table expressions in which an error is
    incorrectly raised when a NOT IN class exists in a CTE. The error is
    `CTE with NOT IN fails with ERROR: could not find CTE
`CTE-Name``.
15. Fixed a bug related to an incorrect `last_error_timestamp`
    value in the `aurora_replica_status` table.
16. Fixed a bug to avoid populating shared buffers with blocks belonging
    to temporary objects. These blocks correctly reside in PostgreSQL
    backend local buffers.
17. Improved the performance of vacuum cleanup on GIN indexes.
18. Fixed a bug where in rare cases Aurora may exhibit 100% CPU utilization
    while acting as a replica of an RDS for PostgreSQL instance even when the
    replication stream is idle.
19. Backported a change from PostgreSQL 11 which improves the cleanup of
    orphaned temporary tables. Without this change, it is possible that in
    rare cases orphaned temporary tables can lead to transaction ID
    wraparound. For more information, see this [PostgreSQL community commit](https://github.com/postgres/postgres/commit/246a6c8f7b237cc1943efbbb8a7417da9288f5c4 "https://github.com/postgres/postgres/commit/246a6c8f7b237cc1943efbbb8a7417da9288f5c4").
20. Fixed a bug where a Writer instance may accept replication
    registration requests from Reader instances while having an
    uninitialized startup process.
21. Changed the following extensions:
    - Updated `pg_hint_plan` to version 1.3.3.
    - Added `plprofiler` version 4.1.

### PostgreSQL 10.7,

Aurora PostgreSQL 2.3 (Deprecated)

###### Note

The PostgreSQL engine version 10.7 with the Aurora PostgreSQL 2.3 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.7. For more
information about the improvements in PostgreSQL 10.7, see [PostgreSQL release
10.7](https://www.postgresql.org/docs/10/release-10-7.html "https://www.postgresql.org/docs/10/release-10-7.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.3.5](#AuroraPostgreSQL.Updates.20180305.235 "#AuroraPostgreSQL.Updates.20180305.235")
- [Aurora PostgreSQL
  2.3.3](#AuroraPostgreSQL.Updates.20180305.233 "#AuroraPostgreSQL.Updates.20180305.233")
- [Aurora PostgreSQL
  2.3.1](#AuroraPostgreSQL.Updates.20180305.231 "#AuroraPostgreSQL.Updates.20180305.231")
- [Aurora PostgreSQL
  2.3.0](#AuroraPostgreSQL.Updates.20180305.230 "#AuroraPostgreSQL.Updates.20180305.230")

#### Aurora PostgreSQL

2.3.5

You can find the following improvements in this release.

###### Improvements

1. Fixed a bug that could cause DB instance restarts.
2. Fixed a bug that could cause a crash when the PostgreSQL backend exits
   while using logical replication.
3. Fixed a bug that could cause a restart when reads occurred during
   failovers.
4. Fixed a bug with the `wal2json` module for logical
   replication.
5. Fixed a bug that could result in inconsistent metadata.

#### Aurora PostgreSQL

2.3.3

You can find the following improvements in this release.

###### Improvements

1. Provided a backport fix for the PostgreSQL community security issue
   CVE-2019-10130.
2. Provided a backport fix for the PostgreSQL community security issue
   CVE-2019-10164.
3. Fixed a bug in which data activity streaming could consume excessive
   CPU time.
4. Fixed a bug in which parallel threads scanning a B-tree index might
   stop responding following a disk read.
5. Fixed a bug where use of the `not in` predicate against a
   common table expression (CTE) could return the following error: "ERROR:
   bad levelsup for CTE".
6. Fixed a bug in which the read node replay process might stop
   responding while applying a modification to a generalized search tree
   (GiST) index.
7. Fixed a bug in which visibility map pages could contain incorrect
   freeze bits following a failover to a read node.
8. Optimized log traffic between the write node and read nodes during
   index maintenance.
9. Fixed a bug in which queries on read nodes may crash while performing
   a B-tree index scan.
10. Fixed a bug in which a query that has been optimized for redundant
    inner join removal could crash.
11. The function `aurora_stat_memctx_usage` now reports the
    number of instances of a given context name.
12. Fixed a bug in which the function
    `aurora_stat_memctx_usage` reported incorrect
    results.
13. Fixed a bug in which the read node replay process could wait to stop
    conflicting queries beyond the configured
    `max_standby_streaming_delay` value.
14. Additional information is now logged on read nodes when active
    connections conflict with the relay process.
15. Provided a backport fix for the PostgreSQL community bug #15677, where
    a crash could occur while deleting from a partitioned table.

#### Aurora PostgreSQL

2.3.1

You can find the following improvements in this release.

###### Improvements

1. Fixed multiple bugs related to I/O prefetching that caused engine
   crashes.

#### Aurora PostgreSQL

2.3.0

You can find the following improvements in this release.

###### New features

1. Aurora PostgreSQL now performs I/O prefetching while scanning B-tree
   indexes. This results in significantly improved performance for B-tree
   scans over uncached data.

###### Improvements

1. Fixed a bug in which read nodes may fail with the error "too many
   LWLocks taken".
2. Addressed numerous issues that caused read nodes to fail to startup
   while the cluster is under heavy write workload.
3. Fixed a bug in which usage of the
   `aurora_stat_memctx_usage()` function could lead to a
   crash.
4. Improved the cache replacement strategy used by table scans to
   minimize thrashing of the buffer cache.

### PostgreSQL 10.6,

Aurora PostgreSQL 2.2 (Deprecated)

###### Note

The PostgreSQL engine version 10.6 with the Aurora PostgreSQL 2.2 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.6. For more
information about the improvements in PostgreSQL 10.6, see [PostgreSQL release
10.6](https://www.postgresql.org/docs/10/release-10-6.html "https://www.postgresql.org/docs/10/release-10-6.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.2.1](#AuroraPostgreSQL.Updates.20180305.221 "#AuroraPostgreSQL.Updates.20180305.221")
- [Aurora PostgreSQL
  2.2.0](#AuroraPostgreSQL.Updates.20180305.220 "#AuroraPostgreSQL.Updates.20180305.220")

#### Aurora PostgreSQL

2.2.1

You can find the following improvements in this release.

###### Improvements

1. Improved stability of logical replication.
2. Fixed a bug which could cause an error running queries. The message
   reported was of the form "CLOG segment 123 does not exist: No such file
   or directory".
3. Increased the supported size of IAM passwords to 8KB.
4. Improved consistency of performance under high throughput write
   workloads.
5. Fixed a bug which could cause a read replica to crash during a
   restart.
6. Fixed a bug which could cause an error running queries. The message
   reported was of the form "SQL ERROR: Attempting to read past EOF of
   relation".
7. Fixed a bug which could cause an increase in memory usage after a
   restart.
8. Fixed a bug which could cause a transaction with a large number of
   subtransactions to fail.
9. Merged a patch from community PostgreSQL which addresses potential
   failures when using GIN indexes. For more information, see [https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18 "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18").
10. Fixed a bug which could cause a snapshot import from RDS for
    PostgreSQL to fail.

#### Aurora PostgreSQL

2.2.0

You can find the following improvements in this release.

###### New features

1. Added the restricted password management feature. Restricted password
   management enables you to restrict who can manage user passwords and
   password expiration changes by using the parameter
   `rds.restrict_password_commands` and the role
   `rds_password`. For more information, see [Restricting password management](../AuroraUserGuide/AuroraPostgreSQL.md#RestrictPasswordMgmt "../AuroraUserGuide/AuroraPostgreSQL.md#RestrictPasswordMgmt") in the _Amazon Aurora
   User Guide_.

### PostgreSQL 10.5,

Aurora PostgreSQL 2.1 (Deprecated)

###### Note

The PostgreSQL engine version 10.5 with the Aurora PostgreSQL 2.1 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.5. For more
information about the improvements in PostgreSQL 10.5, see [PostgreSQL release 10.5](https://www.postgresql.org/docs/current/static/release-10-5.html "https://www.postgresql.org/docs/current/static/release-10-5.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.1.1](#AuroraPostgreSQL.Updates.20180305.211 "#AuroraPostgreSQL.Updates.20180305.211")
- [Aurora PostgreSQL
  2.1.0](#AuroraPostgreSQL.Updates.20180305.210 "#AuroraPostgreSQL.Updates.20180305.210")

#### Aurora PostgreSQL

2.1.1

You can find the following improvements in this release.

###### Improvements

1. Fixed a bug which could cause an error running queries. The message
   reported was of the form "CLOG segment 123 does not exist: No such file
   or directory".
2. Increased the supported size of IAM passwords to 8KB.
3. Improved consistency of performance under high throughput write
   workloads.
4. Fixed a bug which could cause a read replica to crash during a
   restart.
5. Fixed a bug which could cause an error running queries. The message
   reported was of the form "SQL ERROR: Attempting to read past EOF of
   relation".
6. Fixed a bug which could cause an increase in memory usage after a
   restart.
7. Fixed a bug which could cause a transaction with a large number of
   subtransactions to fail.
8. Merged a patch from community PostgreSQL which addresses potential
   failures when using GIN indexes. For more information, see [https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18 "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18").
9. Fixed a bug which could cause a snapshot import from RDS for
   PostgreSQL to fail.

#### Aurora PostgreSQL

2.1.0

You can find the following improvements in this release.

###### New features

1. General availability of Aurora Query Plan Management, which enables
   customers to track and manage any or all query plans used by their
   applications, to control query optimizer plan selection, and to ensure
   high and stable applicationperformance. For more information, see [Managing query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md") in the
   _Amazon Aurora User Guide_.
2. Updated the `libprotobuf` extension to version 1.3.0. This
   is used by the `PostGIS` extension.
3. Updated the `pg_similarity` extension to version
   1.0.
4. Updated the `log_fdw` extension to version 1.1.
5. Updated the `pg_hint_plan` extension to version
   1.3.1.

###### Improvements

1. Network traffic between the writer and reader nodes is now compressed
   to reduce network utilization. This reduces the chance of read node
   unavailability due to network saturation.
2. Implemented a high performance, scalable subsystem for PostgreSQL
   subtransactions. This improves the performance of applications which
   make extensive use of savepoints and `PL/pgSQL` exception
   handlers.
3. The `rds_superuser` role can now set the following
   parameters on a per-session, database, or role level:
   - `log_duration`
   - `log_error_verbosity`
   - `log_executor_stats`
   - `log_lock_waits`
   - `log_min_duration_statement`
   - `log_min_error_statement`
   - `log_min_messages`
   - `log_parser_stats`
   - `log_planner_stats`
   - `log_replication_commands`
   - `log_statement_stats`
   - `log_temp_files`

4. Fixed a bug in which the SQL command "ALTER FUNCTION ... OWNER TO ..."
   might fail with error "improper qualified name (too many dotted
   names)".
5. Fixed a bug in which a crash could occur while committing a
   transaction with more than two million subtransactions.
6. Fixed a bug in community PostgreSQL code related to GIN indexes which
   can cause the Aurora Storage volume to become unavailable.
7. Fixed a bug in which an Aurora PostgreSQL replica of an RDS for PostgreSQL
   instance might fail to start, reporting error: "PANIC: could not locate
   a valid checkpoint record".
8. Fixed a bug in which passing an invalid parameter to the
   `aurora_stat_backend_waits` function could cause a
   crash.

###### Known issues

1. The `pageinspect` extension is not supported in
   Aurora PostgreSQL.

### PostgreSQL 10.4,

Aurora PostgreSQL 2.0 (Deprecated)

###### Note

The PostgreSQL engine version 10.4 with the Aurora PostgreSQL 2.0 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 10.4. For more
information about the improvements in PostgreSQL 10.4, see [PostgreSQL release
10.4](https://www.postgresql.org/docs/10/release-10-4.html "https://www.postgresql.org/docs/10/release-10-4.html").

###### Releases and patches

- [Aurora PostgreSQL
  2.0.1](#AuroraPostgreSQL.Updates.20180305.201 "#AuroraPostgreSQL.Updates.20180305.201")
- [Aurora PostgreSQL
  2.0.0](#AuroraPostgreSQL.Updates.20180305.200 "#AuroraPostgreSQL.Updates.20180305.200")

#### Aurora PostgreSQL

2.0.1

You can find the following improvements in this release.

###### Improvements

1. Fixed a bug which could cause an error running queries. The message
   reported was of the form "CLOG segment 123 does not exist: No such file
   or directory".
2. Increased the supported size of IAM passwords to 8KB.
3. Improved consistency of performance under high throughput write
   workloads.
4. Fixed a bug which could cause a read replica to crash during a
   restart.
5. Fixed a bug which could cause an error running queries. The message
   reported was of the form "SQL ERROR: Attempting to read past EOF of
   relation".
6. Fixed a bug which could cause an increase in memory usage after a
   restart.
7. Fixed a bug which could cause a transaction with a large number of
   subtransactions to fail.
8. Merged a patch from community PostgreSQL which addresses potential
   failures when using GIN indexes. For more information, see [https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18 "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18").
9. Fixed a bug which could cause a snapshot import from RDS for
   PostgreSQL to fail.

#### Aurora PostgreSQL

2.0.0

You can find the following improvements in this release.

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [PostgreSQL 9.6.9,
   Aurora PostgreSQL 1.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.13 "#AuroraPostgreSQL.Updates.20180305.13").
2. The temporary file size limitation is user-configurable. You require
   the **rds_superuser** role to modify the
   `temp_file_limit` parameter.
3. Upgraded the `GDAL` library, which is used by the
   `PostGIS` extension.
4. Updated the `ip4r` extension to version 2.1.1.
5. Updated the `pg_repack` extension to version 1.4.3.
6. Updated the `plv8` extension to version 2.1.2.
7. Parallel queries – When you create a new Aurora PostgreSQL version
   2.0 instance, parallel queries are enabled for the
   `default.postgres10` parameter group. The parameter
   `max_parallel_workers_per_gather` is set to 2 by default,
   but you can modify it to support your specific workload
   requirements.
8. Fixed a bug in which read nodes may crash following a specific type of
   free space change from the write node.

## PostgreSQL 9.6 versions

(Deprecated)

###### Version updates

- [PostgreSQL 9.6.22,
  Aurora PostgreSQL 1.11 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.111 "#AuroraPostgreSQL.Updates.20180305.111")
- [PostgreSQL 9.6.21,
  Aurora PostgreSQL 1.10 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.110 "#AuroraPostgreSQL.Updates.20180305.110")
- [PostgreSQL 9.6.19,
  Aurora PostgreSQL 1.9 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.19 "#AuroraPostgreSQL.Updates.20180305.19")
- [PostgreSQL 9.6.18,
  Aurora PostgreSQL 1.8 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.18 "#AuroraPostgreSQL.Updates.20180305.18")
- [PostgreSQL 9.6.17,
  Aurora PostgreSQL 1.7 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.17 "#AuroraPostgreSQL.Updates.20180305.17")
- [PostgreSQL 9.6.16,
  Aurora PostgreSQL 1.6 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.16 "#AuroraPostgreSQL.Updates.20180305.16")
- [PostgreSQL 9.6.12,
  Aurora PostgreSQL 1.5 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.15 "#AuroraPostgreSQL.Updates.20180305.15")
- [PostgreSQL 9.6.11,
  Aurora PostgreSQL 1.4 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.14 "#AuroraPostgreSQL.Updates.20180305.14")
- [PostgreSQL 9.6.9,
  Aurora PostgreSQL 1.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.13 "#AuroraPostgreSQL.Updates.20180305.13")
- [PostgreSQL 9.6.8,
  Aurora PostgreSQL 1.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.12 "#AuroraPostgreSQL.Updates.20180305.12")
- [PostgreSQL 9.6.6
  Aurora PostgreSQL 1.1 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.11 "#AuroraPostgreSQL.Updates.20180305.11")
- [PostgreSQL 9.6.3,
  Aurora PostgreSQL 1.0 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.10 "#AuroraPostgreSQL.Updates.20180305.10")

### PostgreSQL 9.6.22,

Aurora PostgreSQL 1.11 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.22 and Aurora PostgreSQL 1.10 are no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.22. For more
information about the improvements in PostgreSQL 9.6.22, see [PostgreSQL release
9.6.22](https://www.postgresql.org/docs/96/release-9-6.html "https://www.postgresql.org/docs/96/release-9-6.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.11.1](#AuroraPostgreSQL.Updates.20180305.9622 "#AuroraPostgreSQL.Updates.20180305.9622")
- [Aurora PostgreSQL
  1.11](#AuroraPostgreSQL.Updates.20180305.111 "#AuroraPostgreSQL.Updates.20180305.111")

#### Aurora PostgreSQL

1.11.1

###### High priority stability updates

- Fixed an issue where queries may become unresponsive due to I/O
  resource exhaustion triggered by prefetch.

###### Additional improvements and stability updates

- Fixed multiple issues in the Aurora storage daemon that could lead to
  brief periods of unavailability when specific network configurations are
  used.

#### Aurora PostgreSQL

1.11

###### High priority stability enhancements

1. Fixed an issue where creating a database from an existing template
   database with tablespace resulted in an error with the message
   `ERROR: could not open file pg_tblspc/...: No such file or
directory`.
2. Fixed an issue where, in rare cases, an Aurora replica may be unable
   to start when a large number of PostgreSQL subtransactions (i.e. SQL
   savepoints) have been used.
3. Fixed an issue where, in rare circumstances, read results may be
   inconsistent for repeated read requests on replica nodes.

###### Additional improvements and enhancements

1. Upgraded OpenSSL to 1.1.1k.
2. Reduced CPU usage and memory consumption of the WAL apply process on
   Aurora replicas for some workloads.
3. Improve safety checks in the write path to detect incorrect writes to
   metadata.
4. Fixed an issue where a duplicate file entry can prevent the Aurora
   PostgreSQL engine from starting up.
5. Fixed an issue that could cause temporary unavailability under heavy
   workloads.
6. Added back ability to use a leading forward slash in the S3 path
   during S3 import.
7. Updated the `PostGIS` extension to version 2.4.7.
8. Updated the `orafce` extension to version 3.16.

### PostgreSQL 9.6.21,

Aurora PostgreSQL 1.10 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.21 and Aurora PostgreSQL 1.10 are no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.21. For more
information about the improvements in PostgreSQL 9.6.21, see [PostgreSQL release
9.6.21](https://www.postgresql.org/docs/9.6/release-9-6-21.html "https://www.postgresql.org/docs/9.6/release-9-6-21.html").

#### Aurora PostgreSQL

1.10.0

###### High priority stability enhancements

1. Fixed a bug where in rare cases a reader had inconsistent results when
   it restarted while a transaction with more than 64 subtransactions was
   being processed.
2. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2021-32027](https://nvd.nist.gov/vuln/detail/CVE-2021-32027 "https://nvd.nist.gov/vuln/detail/CVE-2021-32027")
   - [CVE-2021-32028](https://nvd.nist.gov/vuln/detail/CVE-2021-32028 "https://nvd.nist.gov/vuln/detail/CVE-2021-32028")
   - [CVE-2021-32029](https://nvd.nist.gov/vuln/detail/CVE-2021-32029 "https://nvd.nist.gov/vuln/detail/CVE-2021-32029")

###### Additional improvements and enhancements

1. Fixed a bug where the database could not be started when there were
   many relations in memory-constrained environments.
2. Fixed a bug in the `apg_plan_mgmt` extension that could
   cause brief periods of unavailability due to an internal buffer
   overflow.
3. Fixed a bug where the database engine would attempt to create shared
   memory segments larger than the instance total memory and fail
   repeatedly. For example, attempts to create 128 GiB shared buffers on a
   db.r5.large instance would fail. With this change, requests for total
   shared memory allocations larger than the instance memory allow setting
   the instance to incompatible parameters.
4. Added logic to clean up unnecessary `pg_wal` temporary
   files on a database startup.
5. Fixed a bug in Aurora PostgreSQL 9.6 that sometimes prevented read/write
   nodes from starting up when inbound replication is used.
6. Fixed a bug that could cause brief periods of unavailability due to
   running out of memory when creating the `PostGIS` extension
   with `pgAudit` enabled.
7. Added btree page checks to detect tuple metadata inconsistency.

### PostgreSQL 9.6.19,

Aurora PostgreSQL 1.9 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.19 and Aurora PostgreSQL 1.9 are no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.19. For more
information about the improvements in PostgreSQL 9.6.19, see [PostgreSQL
release 9.6.19](https://www.postgresql.org/docs/9.6/release-9-6-19.html "https://www.postgresql.org/docs/9.6/release-9-6-19.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.9.2](#AuroraPostgreSQL.Updates.20180305.192 "#AuroraPostgreSQL.Updates.20180305.192")
- [Aurora PostgreSQL
  1.9.1](#AuroraPostgreSQL.Updates.20180305.191 "#AuroraPostgreSQL.Updates.20180305.191")
- [Aurora PostgreSQL
  1.9.0](#AuroraPostgreSQL.Updates.20180305.190 "#AuroraPostgreSQL.Updates.20180305.190")

#### Aurora PostgreSQL

1.9.2

###### High priority stability enhancements

1. Fixed a bug where a reader node might render an extra or missing row
   if the reader restarted while the writer node is processing a long
   transaction with more than 64 subtransactions.

###### Additional improvements and enhancements

1. Fixed a bug where a large S3 import with thousands of clients can
   cause one or more of the import clients to stop responding.

#### Aurora PostgreSQL

1.9.1

###### Critical stability enhancements

1. Fixed a bug that caused a read replica to unsuccessfully restart
   repeatedly in rare cases.

###### Additional improvements and enhancements

1. Fixed a bug that when under heavy load, snapshot import, COPY import,
   or S3 import stopped responding in rare cases.
2. Fixed a bug where a read replica might not join the cluster when the
   writer was very busy with a write-intensive workload.

#### Aurora PostgreSQL

1.9.0

###### Critical stability enhancements

- None

###### High priority stability enhancements

1. Backported fixes for the PostgreSQL community security issues
   CVE-2020-25694, CVE-2020-25695, and CVE-2020-25696.
2. Fixed a bug in Aurora PostgreSQL replication that might result in the
   following error message: **`ERROR: `MultiXactId` nnnn
has not been created yet -- apparent wraparound`**

###### Additional improvements and enhancements

1. Aurora PostgreSQL no longer falls behind on a read node when the backend
   is blocked writing to the database client.
2. Fixed a bug that in rare cases caused a brief period of unavailability
   on a read replica when the storage volume grew.
3. Fixed a bug when creating a database that could return the following
   error: **`ERROR: could not create directory on local
disk`**
4. Fixed a bug in the `GiST` index that could result in an out
   of memory condition after promoting an Aurora read replica.
5. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
   physical replica of an RDS for PostgreSQL instance that uses
   `GiST` indexes. In rare cases, this bug caused a brief
   period of unavailability after promoting the Aurora cluster.

### PostgreSQL 9.6.18,

Aurora PostgreSQL 1.8 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.18 and Aurora PostgreSQL 1.8 are no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.18. For more
information about the improvements in PostgreSQL 9.6.18, see [PostgreSQL
release 9.6.18](https://www.postgresql.org/docs/9.6/release-9-6-18.html "https://www.postgresql.org/docs/9.6/release-9-6-18.html").

###### Releases and patches

- [Aurora PostgreSQL release
  1.8.2](#AuroraPostgreSQL.Updates.20180305.182 "#AuroraPostgreSQL.Updates.20180305.182")
- [Aurora PostgreSQL
  1.8.0](#AuroraPostgreSQL.Updates.20180305.180 "#AuroraPostgreSQL.Updates.20180305.180")

There is no version 1.8.1.

#### Aurora PostgreSQL release

1.8.2

###### Critical stability enhancements

1. None

###### High priority stability enhancements

1. Fixed a bug in Aurora PostgreSQL replication that could result in the
   error message **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.
2. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

1. Aurora PostgreSQL no longer falls behind on a read node when the backend
   is blocked writing to the database client.
2. Fixed a bug where a `DROP DATABASE` statement didn't
   remove any relation files.
3. Fixed a small memory leak in a b-tree index that could lead to an out
   of memory condition.
4. Fixed a bug in the `aurora_replica_status()` function where
   the `server_id` field was sometimes truncated.
5. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
   physical replica of an RDS for PostgreSQL instance that uses GiST indexes. In
   rare cases, this bug caused a brief period of unavailability after
   promoting the Aurora DB cluster.

#### Aurora PostgreSQL

1.8.0

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug related to heap page extend that in rare cases resulted in
   longer recovery time and impacted availability.

###### Additional improvements and enhancements

1. Fixed a bug where the Aurora replica crashed when workloads with heavy
   subtransactions are made on the writer instance.
2. Fixed a bug where the writer instance crashed due to a memory leak and
   the depletion of memory used to track active transactions.
3. Fixed a bug that lead to a crash due to improper initialization when
   there is no free memory available during PostgreSQL backend
   startup.
4. Fixed a crash during a BTree prefetch that occurred under certain
   conditions that depended on the shape and data contained in the
   index.
5. Fixed a bug where a `SELECT` query might incorrectly return
   the error **`Attempting to read past EOF of relation rrrr.
blockno=bbb nblocks=nnn`**.
6. Fixed a bug where the database might be unavailable briefly due to
   error handling in database storage growth.

### PostgreSQL 9.6.17,

Aurora PostgreSQL 1.7 (Deprecated)

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.17. For more
information about the improvements in PostgreSQL 9.6.17, see [PostgreSQL
release 9.6.17](https://www.postgresql.org/docs/9.6/release-9-6-17.html "https://www.postgresql.org/docs/9.6/release-9-6-17.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.7.7](#AuroraPostgreSQL.Updates.20180305.177 "#AuroraPostgreSQL.Updates.20180305.177")
- [Aurora PostgreSQL
  1.7.6](#AuroraPostgreSQL.Updates.20180305.176 "#AuroraPostgreSQL.Updates.20180305.176")
- [Aurora PostgreSQL
  1.7.3](#AuroraPostgreSQL.Updates.20180305.173 "#AuroraPostgreSQL.Updates.20180305.173")
- [Aurora PostgreSQL
  1.7.2](#AuroraPostgreSQL.Updates.20180305.172 "#AuroraPostgreSQL.Updates.20180305.172")
- [Aurora PostgreSQL
  1.7.1](#AuroraPostgreSQL.Updates.20180305.171 "#AuroraPostgreSQL.Updates.20180305.171")

#### Aurora PostgreSQL

1.7.7

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

1. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

1.7.6

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

1. Fixed a bug in Aurora PostgreSQL replication that might result in the
   error message, **`ERROR: `MultiXactId` nnnn has not
been created yet -- apparent wraparound`**.

###### Additional improvements and enhancements

1. Fixed a bug that in rare cases caused brief read replica
   unavailability when storage volume grew.
2. Fixed a bug in a b-tree index read optimization that might have caused
   a brief period of unavailability.
3. Fixed a bug in a GiST index that might result in an out-of-memory
   condition after promoting an Aurora Read Replica.

#### Aurora PostgreSQL

1.7.3

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

- None

###### Additional improvements and enhancements

1. Fixed a bug that might cause brief unavailability for heavy
   subtransaction workloads when multiple reader instances restart or
   rejoin the cluster.

#### Aurora PostgreSQL

1.7.2

You can find the following improvements in this release.

###### Critical stability enhancements

1. Fixed a bug related to heap page extend that in rare cases resulted in
   longer recovery time and impacted availability.

###### High Priority Stability Enhancements

None

###### Additional improvements and enhancements

1. Fixed a bug where the database might be unavailable briefly due to
   error handling in database storage growth.
2. Fixed a bug where a SELECT query might incorrectly return the error,
   **`Attempting to read past EOF of relation rrrr. blockno=bbb
nblocks=nnn`**.
3. Fixed an issue with the internal metrics collector that could result
   in erratic CPU spikes on database instances.

#### Aurora PostgreSQL

1.7.1

You can find the following improvements in this release.

###### Critical stability enhancements

None.

###### High priority stability enhancements

1. Improved performance and availability of read instances when applying
   DROP TABLE and TRUNCATE TABLE operations.
2. Fixed a small but continuous memory leak in a diagnostic module that
   could lead to an out-of-memory condition on smaller DB instance
   types.
3. Fixed a bug in the `PostGIS` extension which could lead to
   a database restart. This has been reported to the PostGIS community as
   [https://trac.osgeo.org/postgis/ticket/4646](https://trac.osgeo.org/postgis/ticket/4646 "https://trac.osgeo.org/postgis/ticket/4646").
4. Fixed a bug where read requests might stop responding due to incorrect
   error handling in the storage engine.
5. Fixed a bug that fails for some queries and results in the message
   **`ERROR: found xmin xxxxxx from before relfrozenxid
yyyyyyy`**. This could occur following the promotion of a
   read instance to a write instance.

###### Additional improvements and enhancements

1. Improved performance for queries that read many rows from
   storage.
2. Improved performance and availability of reader DB instances during
   heavy read workload.
3. Fixed a bug that resulted in the message **`ERROR: could not
create file "base/xxxxxx/yyyyyyy" as a previous version still exists
on disk: Success. Please contact AWS customer support`**.
   This can occur during object creation after PostgreSQL's 32-bit
   object identifier has wrapped around.
4. Fixed a bug in the `pg_hint_plan` extension where a
   multi-statement query could lead to a crash when
   `enable_hint_table` is enabled. This is tracked in the
   PostgreSQL community as [https://github.com/ossc-db/pg_hint_plan/issues/25](https://github.com/ossc-db/pg_hint_plan/issues/25 "https://github.com/ossc-db/pg_hint_plan/issues/25").
5. Changed the following extensions:
   - Updated `orafce` to version 3.8

### PostgreSQL 9.6.16,

Aurora PostgreSQL 1.6 (Deprecated)

This version of Aurora PostgreSQL is compatible with PostgreSQL 9.6.16. For more
information about the improvements in release 9.6.16, see [PostgreSQL release
9.6.16](https://www.postgresql.org/docs/9.6/release-9-6-16.html "https://www.postgresql.org/docs/9.6/release-9-6-16.html").

This release contains multiple critical stability enhancements. Amazon highly
recommends upgrading your Aurora PostgreSQL clusters that use older PostgreSQL 9.6
engines to this release.

###### Patch versions

- [Aurora PostgreSQL
  1.6.4](#AuroraPostgreSQL.Updates.20180305.164 "#AuroraPostgreSQL.Updates.20180305.164")
- [Aurora PostgreSQL
  1.6.3](#AuroraPostgreSQL.Updates.20180305.163 "#AuroraPostgreSQL.Updates.20180305.163")
- [Aurora PostgreSQL
  1.6.2](#AuroraPostgreSQL.Updates.20180305.162 "#AuroraPostgreSQL.Updates.20180305.162")
- [Aurora PostgreSQL
  1.6.1](#AuroraPostgreSQL.Updates.20180305.161 "#AuroraPostgreSQL.Updates.20180305.161")
- [Aurora PostgreSQL
  1.6.0](#AuroraPostgreSQL.Updates.20180305.160 "#AuroraPostgreSQL.Updates.20180305.160")

#### Aurora PostgreSQL

1.6.4

You can find the following improvements in this release.

###### Critical stability enhancements

- None

###### High priority stability enhancements

1. Backported fixes for the following PostgreSQL community security
   issues:
   - [CVE-2020-25694](https://nvd.nist.gov/vuln/detail/CVE-2020-25694 "https://nvd.nist.gov/vuln/detail/CVE-2020-25694")
   - [CVE-2020-25695](https://nvd.nist.gov/vuln/detail/CVE-2020-25695 "https://nvd.nist.gov/vuln/detail/CVE-2020-25695")
   - [CVE-2020-25696](https://nvd.nist.gov/vuln/detail/CVE-2020-25696 "https://nvd.nist.gov/vuln/detail/CVE-2020-25696")

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

1.6.3

###### New features

1. Aurora PostgreSQL now supports the PostgreSQL [vacuum_truncate](https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE "https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE") storage parameter to manage vacuum
   truncation for specific tables. Set this [storage parameter](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS "https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS") to false when creating or altering a
   table to prevent the [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html") SQL command from truncating the table's
   trailing empty pages.

###### Critical stability enhancements

- None

###### High priority stability enhancements

1. Fixed a bug where reads from storage might stop responding due to
   incorrect error handling.

###### Additional improvements and enhancements

- None

#### Aurora PostgreSQL

1.6.2

You can find the following improvements in this engine update.

###### Critical stability enhancements

1. Fixed a bug in which a reader DB instance might temporarily use stale
   data. This could lead to wrong results such as too few or too many rows.
   This error is not persisted on storage, and will clear when the database
   page containing the row has been evicted from cache. This can happen
   when the primary DB instance enters a transaction snapshot overflow due
   to having more than 64 subtransactions in a single transaction.
   Applications susceptible to this bug include those that use SQL
   savepoints or PostgreSQL exception handlers with more than 64
   subtransactions in the top transaction.

###### High priority stability enhancements

1. Fixed a bug that may cause a reader DB instance to crash causing
   unavailability while attempting to the join the DB cluster. This can
   happen in some cases when the primary DB instance has a transaction
   snapshot overflow due to a high number of subtransactions. In this
   situation the reader DB instance will be unable to join until the
   snapshot overflow has cleared.

###### Additional improvements and enhancements

1. Fixed a bug that prevented Performance Insights from determining the
   query ID of a running statement.

#### Aurora PostgreSQL

1.6.1

You can find the following improvements in this engine update.

###### Critical stability enhancements

1. None

###### High priority stability enhancements

1. Fixed a bug that might cause the database engine to crash causing
   unavailability. This occurred if a newly established database connection
   encountered a resource exhaustion-related error during initialization
   after successful authentication.

###### Additional improvements and enhancements

1. Provided general improvements to the stability and availability of
   Aurora PostgreSQL.

#### Aurora PostgreSQL

1.6.0

You can find the following new features and improvements in this engine
version.

###### New features

1. Updates to the `apg_plan_mgmt` extension. For more
   information, see [Managing query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md") in the
   _Amazon Aurora User Guide_.

###### Critical stability enhancements

1. Fixed a bug related to creating B-tree indexes on temporary tables
   that in rare cases may result in longer recovery time, and impact
   availability.
2. Fixed a bug related to replication when Aurora PostgreSQL is acting as a
   physical replica of an RDS for PostgreSQL instance. In rare cases, this bug
   causes a log write failure that may result in longer recovery time, and
   impact availability.
3. Fixed a bug related to handling of reads with high I/O latency that in
   rare cases may result in longer recovery time, and impact
   availability.

###### High priority stability enhancements

1. Fixed multiple bugs, which cause Aurora to crash during prefetch
   operations on Btree indexes.
2. Enhanced the validation checks performed on data blocks in the buffer
   cache. This improves Aurora's detection of inconsistency.

###### Additional improvements and enhancements

1. The query plan management extension `apg_plan_mgmt` has an
   improved algorithm for managing plan generation for highly partitioned
   tables.
2. Reduced startup time on instances with large caches via improvements
   in the buffer cache recovery algorithm.
3. Improved the performance of the read-node-apply process under high
   transaction rate workloads by using changes to PostgreSQL
   `LWLock` prioritization. These changes prevent starvation
   of the read-node-apply process while the PostgreSQL
   `ProcArray` is under heavy contention.
4. Fixed a bug in which a read node may crash during the replay of a
   PostgreSQL `SLRU`-truncate operation.
5. Fixed a bug where in rare cases, database writes might stall following
   an error returned by one of the six copies of an Aurora log record.
6. Fixed a memory leak on read nodes when cluster cache management is
   enabled.
7. Fixed a bug in which importing an RDS for PostgreSQL snapshot might stop
   responding if the source snapshot contains a large number of unlogged
   relations.
8. Fixed a bug related to `hot_standby_feedback` for read
   nodes in which the read node may report the wrong transaction id epoch
   to the write node. This can cause the write node to ignore the
   `hot_standby_feedback` and invalidate snapshots on the
   read node.
9. Fixed a bug in which storage errors that occur during `CREATE
DATABASE` statements are not properly handled. The bug left
   the resulting database inaccessible. The correct behavior is to fail the
   database creation and return the appropriate error to the user.
10. Improved handling of PostgreSQL snapshot overflow when a read node
    attempts to connect to a write node. Prior to this change, if the write
    node was in a snapshot overflow state, the read node was unable to join.
    A message appear in the PostgreSQL log file in the form `DEBUG:
recovery snapshot waiting for non-overflowed snapshot or until
oldest active xid on standby is at least
`xxxxxxx`(now`yyyyyyy`)`. A snapshot overflow
    occurs when an individual transaction has created over 64
    subtransactions.
11. Fixed a bug related to common table expressions in which an error is
    incorrectly raised when a NOT IN class exists in a CTE. The error is
    `CTE with NOT IN fails with ERROR: could not find CTE
`CTE-Name``.
12. Fixed a bug related to an incorrect `last_error_timestamp`
    value in the `aurora_replica_status` table.
13. Fixed a bug to avoid populating shared buffers with blocks belonging
    to temporary objects. These blocks correctly reside in PostgreSQL
    backend local buffers.
14. Fixed a bug where in rare cases Aurora may exhibit 100% CPU
    utilization while acting as a replica of an RDS for PostgreSQL instance even
    when the replication stream is idle.
15. Backported a change from PostgreSQL 11 which improves the cleanup of
    orphaned temporary tables. Without this change, it is possible that in
    rare cases orphaned temporary tables can to lead to transaction ID
    wraparound. For more information, see this [PostgreSQL community commit](https://github.com/postgres/postgres/commit/246a6c8f7b237cc1943efbbb8a7417da9288f5c4 "https://github.com/postgres/postgres/commit/246a6c8f7b237cc1943efbbb8a7417da9288f5c4").
16. Fixed a bug where a Writer instance may accept replication
    registration requests from Reader instances while having an
    uninitialized startup process.
17. Changed the following extensions:
    - Updated `pg_hint_plan` to version 1.2.5.

### PostgreSQL 9.6.12,

Aurora PostgreSQL 1.5 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.12 with the Aurora PostgreSQL 1.5 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.12. For more
information about the improvements in PostgreSQL 9.6.12, see [PostgreSQL release
9.6.12](https://www.postgresql.org/docs/9.6/release-9-6-12.html "https://www.postgresql.org/docs/9.6/release-9-6-12.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.5.3](#AuroraPostgreSQL.Updates.20180305.153 "#AuroraPostgreSQL.Updates.20180305.153")
- [Aurora PostgreSQL
  1.5.2](#AuroraPostgreSQL.Updates.20180305.152 "#AuroraPostgreSQL.Updates.20180305.152")
- [Aurora PostgreSQL
  1.5.1](#AuroraPostgreSQL.Updates.20180305.151 "#AuroraPostgreSQL.Updates.20180305.151")
- [Aurora PostgreSQL
  1.5.0](#AuroraPostgreSQL.Updates.20180305.150 "#AuroraPostgreSQL.Updates.20180305.150")

#### Aurora PostgreSQL

1.5.3

You can find the following improvements in this release.

###### Improvements

1. Fixed a bug that could cause DB instance restarts.
2. Fixed a bug that could cause a restart when reads occurred during
   failovers.
3. Fixed a bug that could result in inconsistent metadata.

#### Aurora PostgreSQL

1.5.2

You can find the following improvements in this release.

###### Improvements

1. Provided a backport fix for the PostgreSQL community security issue
   CVE-2019-10130.
2. Fixed a bug in which the read node replay process might stop
   responding while applying a modification to a generalized search tree
   (GiST) index.
3. Fixed a bug in which visibility map pages may contain incorrect freeze
   bits following a failover to a read node.
4. Fixed a bug in which the error "relation `relation-name`
   does not exist" is incorrectly reported.
5. Optimized log traffic between the write node and read nodes during
   index maintenance.
6. Fixed a bug in which queries on read nodes may crash while performing
   a B-tree index scan.
7. The function `aurora_stat_memctx_usage` now reports the
   number of instances of a given context name.
8. Fixed a bug in which the function
   `aurora_stat_memctx_usage` reported incorrect
   results.
9. Fixed a bug in which the read node replay process may wait to stop
   conflicting queries beyond the configured
   `max_standby_streaming_delay`.
10. Additional information is now logged on read nodes when active
    connections conflict with the relay process.

#### Aurora PostgreSQL

1.5.1

You can find the following improvements in this release.

###### Improvements

1. Fixed multiple bugs related to I/O prefetching, which caused engine
   crashes.

#### Aurora PostgreSQL

1.5.0

You can find the following improvements in this release.

###### New features

1. Aurora PostgreSQL now performs I/O prefetching while scanning B-tree
   indexes. This results in significantly improved performance for B-tree
   scans over uncached data.

###### Improvements

1. Addressed numerous issues that caused read nodes to fail to startup
   while the cluster is under heavy write workload.
2. Fixed a bug in which usage of the
   `aurora_stat_memctx_usage()` function could lead to a
   crash.
3. Improved the cache replacement strategy used by table scans to
   minimize thrashing of the buffer cache.

### PostgreSQL 9.6.11,

Aurora PostgreSQL 1.4 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.11 with the Aurora PostgreSQL 1.4 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.11. For more
information about the improvements in PostgreSQL 9.6.11, see [PostgreSQL release
9.6.11](https://www.postgresql.org/docs/9.6/release-9-6-11.html "https://www.postgresql.org/docs/9.6/release-9-6-11.html").

You can find the following improvements in this release.

###### New features

1. Support is added for the `pg_similarity` extension version
   1.0.
2. Aurora PostgreSQL now supports the PostgreSQL [vacuum_truncate](https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE "https://www.postgresql.org/docs/current/sql-createtable.html#RELOPTION-VACUUM-TRUNCATE") storage parameter to manage vacuum truncation
   for specific tables. Set this [storage parameter](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS "https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-STORAGE-PARAMETERS") to false when creating or altering a table to
   prevent the [VACUUM](https://www.postgresql.org/docs/current/sql-vacuum.html "https://www.postgresql.org/docs/current/sql-vacuum.html") SQL command from truncating the table's trailing
   empty pages.

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [PostgreSQL 9.6.9,
   Aurora PostgreSQL 1.3 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.13 "#AuroraPostgreSQL.Updates.20180305.13").
2. Network traffic between the writer and reader nodes is now compressed to
   reduce network utilization. This reduces the chance of read node
   unavailability due to network saturation.
3. Performance of subtransactions has improved under high concurrency
   workloads.
4. An update for the `pg_hint_plan` extension to version
   1.2.3.
5. Fixed an issue where on a busy system, a commit with millions of
   subtransactions (and sometimes with commit timestamps enabled) can cause
   Aurora to crash.
6. Fixed an issue where an `INSERT` statement with
   `VALUES` could fail with the message "Attempting to read past
   EOF of relation".
7. An upgrade of the `apg_plan_mgmt` extension to version 1.0.1.
   For details, see [Version 1.0.1 of the
   Aurora PostgreSQL apg_plan_mgmt extension](auroraqpm.md#auroraqpm-version.101 "auroraqpm.md#auroraqpm-version.101").

The `apg_plan_mgmt` extension is used with query plan
management. For more about how to install, upgrade, and use the
`apg_plan_mgmt` extension, see [Managing query execution plans for Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md") in the
_Amazon Aurora User Guide_.

### PostgreSQL 9.6.9,

Aurora PostgreSQL 1.3 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.9 with the Aurora PostgreSQL 1.3 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

This release of Aurora PostgreSQL is compatible with PostgreSQL 9.6.9. For more
information about the improvements in PostgreSQL 9.6.9, see [PostgreSQL release
9.6.9](https://www.postgresql.org/docs/9.6/release-9-6-9.html "https://www.postgresql.org/docs/9.6/release-9-6-9.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.3.2](#AuroraPostgreSQL.Updates.20180305.132 "#AuroraPostgreSQL.Updates.20180305.132")
- [Aurora PostgreSQL
  1.3.0](#AuroraPostgreSQL.Updates.20180305.130 "#AuroraPostgreSQL.Updates.20180305.130")

#### Aurora PostgreSQL

1.3.2

You can find the following improvements in this release.

###### New features

1. Added the `ProcArrayGroupUpdate` wait event.

###### Improvements

1. Fixed a bug which could cause an error running queries. The message
   reported was of the form "CLOG segment 123 does not exist: No such file
   or directory".
2. Increased the supported size of IAM passwords to 8KB.
3. Improved consistency of performance under high throughput write
   workloads.
4. Fixed a bug which could cause a read replica to crash during a
   restart.
5. Fixed a bug which could cause an error running queries. The message
   reported was of the form "SQL ERROR: Attempting to read past EOF of
   relation".
6. Fixed a bug which could cause an increase in memory usage after a
   restart.
7. Fixed a bug which could cause a transaction with a large number of
   subtransactions to fail.
8. Merged a patch from community PostgreSQL which addresses potential
   failures when using GIN indexes. For more information, see [https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18 "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18").
9. Fixed a bug which could cause a snapshot import from RDS for
   PostgreSQL to fail.

#### Aurora PostgreSQL

1.3.0

You can find the following improvements in this release.

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [PostgreSQL 9.6.8,
   Aurora PostgreSQL 1.2 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.12 "#AuroraPostgreSQL.Updates.20180305.12").
2. Updated the `GDAL` library, which is used by the
   `PostGIS` extension.
3. Updated the following PostgreSQL extensions:
   - `ip4r` updated to version 2.1.1.
   - `pgaudit` updated to version 1.1.1.
   - `pg_repack` updated to version 1.4.3.
   - `plv8` updated to version 2.1.2.

4. Fixed an issue in the monitoring system that could incorrectly cause a
   failover when local disk usage is high.
5. Fixed a bug in which Aurora PostgreSQL can repeatedly crash,
   reporting:

`PANIC: new_record_total_len (8201) must be less than BLCKSZ
 (8192), rmid (6), info (32)` 6. Fixed a bug in which an Aurora PostgreSQL read node might be unable to
rejoin a cluster due to recovery of a large buffer cache. This issue is
unlikely to occur on instances other than **r4.16xlarge.** 7. Fixed a bug in which inserting into an empty GIN index leaf page
imported from pre-9.4 engine versions can cause the Aurora storage
volume to become unavailable. 8. Fixed a bug in which, in rare circumstances, a crash during
transaction commit could result in the loss of `CommitTs`
data for the committing transaction. The actual durability of the
transaction was not impacted by this bug. 9. Fixed a bug in the `PostGIS` extension in which
`PostGIS` can crash in the function
`gserialized_gist_picksplit_2d()`. 10. Improved the stability of read-only nodes during heavy write traffic
on instances smaller than **r4.8xl**. This
specifically addresses a situation where the network bandwidth between
the writer and the reader is constrained. 11. Fixed a bug in which an Aurora PostgreSQL instance acting as a replication
target of an RDS for PostgreSQL instance crashed with the following
error:

`FATAL: could not open file "base/16411/680897_vm": No such file
 or directory" during "xlog redo at 782/3122D540 for
 Storage/TRUNCATE"` 12. Fixed a memory leak on read-only nodes in which the heap size for the
"aurora wal replay process" will continue to grow. This is observable
via Enhanced Monitoring. 13. Fixed a bug in which Aurora PostgreSQL can fail to start, with the
following message reported in the PostgreSQL log:

`FATAL: Storage initialization failed`. 14. Fixed a performance limitation on heavy write workloads that caused
waits on the `LWLock:buffer_content` and
`IO:ControlFileSyncUpdate` events. 15. Fixed a bug in which read nodes could crash following a specific type
of free space change from the write node.

### PostgreSQL 9.6.8,

Aurora PostgreSQL 1.2 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.8 with the Aurora PostgreSQL 1.2 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

For more information about PostgreSQL 9.6.8, see [PostgreSQL release
9.6.8](https://www.postgresql.org/docs/9.6/release-9-6-8.html "https://www.postgresql.org/docs/9.6/release-9-6-8.html").

###### Releases and patches

- [Aurora PostgreSQL
  1.2.2](#AuroraPostgreSQL.Updates.20180305.122 "#AuroraPostgreSQL.Updates.20180305.122")
- [Aurora PostgreSQL
  1.2.0](#AuroraPostgreSQL.Updates.20180305.120 "#AuroraPostgreSQL.Updates.20180305.120")

#### Aurora PostgreSQL

1.2.2

You can find the following improvements in this release.

###### New features

1. Added the `ProcArrayGroupUpdate` wait event.

###### Improvements

1. Fixed a bug which could cause an error running queries. The message
   reported was of the form "CLOG segment 123 does not exist: No such file
   or directory".
2. Increased the supported size of IAM passwords to 8KB.
3. Improved consistency of performance under high throughput write
   workloads.
4. Fixed a bug which could cause a read replica to crash during a
   restart.
5. Fixed a bug which could cause an error running queries. The message
   reported was of the form "SQL ERROR: Attempting to read past EOF of
   relation".
6. Fixed a bug which could cause an increase in memory usage after a
   restart.
7. Fixed a bug which could cause a transaction with a large number of
   subtransactions to fail.
8. Merged a patch from community PostgreSQL which addresses potential
   failures when using GIN indexes. For more information, see [https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18](https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18 "https://git.postgresql.org/gitweb/?p=postgresql.git;a=commit;h=f9e66f2fbbb49a493045c8d8086a9b15d95b8f18").
9. Fixed a bug which could cause a snapshot import from RDS for
   PostgreSQL to fail.

#### Aurora PostgreSQL

1.2.0

You can find the following improvements in this release.

###### New features

1. Introduced the `aurora_stat_memctx_usage()` function. This
   function reports internal memory context usage for each PostgreSQL
   backend. You can use this function to help determine why certain
   backends are consuming large amounts of memory.

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [PostgreSQL 9.6.6
   Aurora PostgreSQL 1.1 (Deprecated)](#AuroraPostgreSQL.Updates.20180305.11 "#AuroraPostgreSQL.Updates.20180305.11").
2. Updates the following PostgreSQL extensions:
   - `pg_hint_plan` updated to version 1.2.2
   - `plv8` updated to version 2.1.0

3. Improves efficiency of traffic between writer and reader nodes.
4. Improves connection establishment performance.
5. Improve the diagnostic data provided in the PostgreSQL error log when
   an out-of-memory error is encountered.
6. Multiple fixes to improve the reliability and performance of snapshot
   import from Amazon RDS for PostgreSQL to Aurora PostgreSQL-Compatible Edition.
7. Multiple fixes to improve the reliability and performance of
   Aurora PostgreSQL read nodes.
8. Fixes a bug in which an otherwise idle instance can generate
   unnecessary read traffic on an Aurora storage volume.
9. Fixes a bug in which duplicate sequence values can be encountered
   during insert. The problem only occurs when migrating a snapshot from
   RDS for PostgreSQL to Aurora PostgreSQL. The fix prevents the problem from
   being introduced when performing the migration. Instances migrated
   before this release can still encounter duplicate key errors.
10. Fixes a bug in which an RDS for PostgreSQL instance migrated to
    Aurora PostgreSQL using replication can run out of memory doing
    insert/update of GIST indexes, or cause other issues with GIST
    indexes.
11. Fixes a bug in which vacuum can fail to update the corresponding
    `pg_database.datfrozenxid` value for a database.
12. Fixes a bug in which a crash while creating a new MultiXact (contended
    row level lock) can cause Aurora PostgreSQL to stop responding indefinitely
    on the first access to the same relation after the engine
    restarts.
13. Fixes a bug in which a PostgreSQL backend can't be terminated or
    canceled while invoking an `fdw` call.
14. Fixes a bug in which one vCPU is fully utilized at all times by the
    Aurora storage daemon. This issue is especially noticeable on smaller
    instance classes, such as r4.large, where it can lead to 25–50
    percent CPU usage when idle.
15. Fixes a bug in which an Aurora PostgreSQL writer node can fail over
    spuriously.
16. Fixes a bug in which, in a rare scenario, an Aurora PostgreSQL read node
    can report:

"FATAL: lock buffer_io is not held" 17. Fixes a bug in which stale relcache entries can halt vacuuming of
relations and push the system close to transaction ID wraparound. The
fix is a port of a PostgreSQL community patch scheduled to be released
in a future minor version. 18. Fixes a bug in which a failure while extending a relation can cause
Aurora to crash while scanning the partially extended relation.

### PostgreSQL 9.6.6

Aurora PostgreSQL 1.1 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.6 with the Aurora PostgreSQL 1.1 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

For more information about PostgreSQL 9.6.6 see, [PostgreSQL
release 9.6.6](https://www.postgresql.org/docs/9.6/static/release-9-6-6.html "https://www.postgresql.org/docs/9.6/static/release-9-6-6.html").

You can find the following improvements in this engine update:

###### New features

1. Introduced the `aurora_stat_utils` extension. This extension
   includes two functions:
   - aurora_wait_report() function for wait event monitoring
   - aurora_log_report() for log record write monitoring

2. Added support for the following extensions:
   - orafce 3.6.1
   - pgrouting 2.4.2
   - postgresql-hll 2.10.2
   - prefix 1.2.6

###### Improvements

1. This release contains all fixes, features, and improvements present in
   [Aurora PostgreSQL
   1.0.11](#AuroraPostgreSQL.Updates.20180305.1011 "#AuroraPostgreSQL.Updates.20180305.1011")
2. Updates for the following PostgreSQL extensions:
   - `PostGIS` extension updated to version 2.3.4
   - `geos` library updated to version 3.6.2
   - `pg_repack` updated to version 1.4.2

3. Access to the `pg_statistic` relation enabled.
4. Disabled the 'effective_io_concurrency' guc parameter, as it does not
   apply to Aurora storage.
5. Changed the 'hot_standby_feedback' guc parameter to not-modifiable and set
   the value to '1'.
6. Improved heap page read performance during a vacuum operation.
7. Improved performance of snapshot conflict resolution on read nodes.
8. Improved performance of transaction snapshot acquisition on read
   nodes.
9. Improved write performance for GIN meta page updates.
10. Improved buffer cache recovery performance during startup.
11. Fixes a bug that caused a database engine crash at startup while
    recovering prepared transactions.
12. Fixes a bug that could result in the inability to start a read node when
    there are a large number of prepared transactions.
13. Fixes a bug that could cause a read node to report:

ERROR: could not access status of transaction 6080077

DETAIL:\* \*Could not open file "pg_subtrans/005C": No such file or
directory. 14. Fixes a bug that could cause the error below when replicating from RDS
PostgreSQL to Aurora PostgreSQL:

FATAL: lock buffer_content is not held

CONTEXT: xlog redo at 46E/F1330870 for Storage/TRUNCATE:
base/13322/8058750 to 0 blocks flags 7 15. Fixes a bug that could cause Aurora PostgreSQL to stop responding while
replaying a multixact WAL record when replicating from RDS for PostgreSQL to
Aurora PostgreSQL. 16. Multiple improvements to the reliability of importing snapshots from RDS
PostgreSQL to Aurora PostgreSQL.

### PostgreSQL 9.6.3,

Aurora PostgreSQL 1.0 (Deprecated)

###### Note

The PostgreSQL engine version 9.6.3 with the Aurora PostgreSQL 1.0 is no longer
supported. To upgrade, see [Upgrading the PostgreSQL DB engine for Aurora PostgreSQL](../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades "../AuroraUserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.Upgrading.ExtensionUpgrades") in the
_Amazon Aurora User Guide_.

For more information about PostgreSQL 9.6.3 see, [PostgreSQL release
9.6.3](https://www.postgresql.org/docs/9.6/release-9-6-3.html "https://www.postgresql.org/docs/9.6/release-9-6-3.html").

This version includes the following Releases:

###### Releases and patches

- [Aurora PostgreSQL
  1.0.11](#AuroraPostgreSQL.Updates.20180305.1011 "#AuroraPostgreSQL.Updates.20180305.1011")
- [Aurora PostgreSQL
  1.0.10](#AuroraPostgreSQL.Updates.20180305.1010 "#AuroraPostgreSQL.Updates.20180305.1010")
- [Aurora PostgreSQL
  1.0.9](#AuroraPostgreSQL.Updates.20180305.109 "#AuroraPostgreSQL.Updates.20180305.109")
- [Aurora PostgreSQL
  1.0.8](#AuroraPostgreSQL.Updates.20180305.108 "#AuroraPostgreSQL.Updates.20180305.108")
- [Aurora PostgreSQL
  1.0.7](#AuroraPostgreSQL.Updates.20180305.107 "#AuroraPostgreSQL.Updates.20180305.107")

#### Aurora PostgreSQL

1.0.11

You can find the following improvements in this engine update:

1. Fixes an issue with parallel query processing that can lead to
   incorrect results.
2. Fixes an issue with visibility map handling during replication from
   Amazon RDS for PostgreSQL that can cause the Aurora storage volume to become
   unavailable.
3. Corrects the pg-repack extension.
4. Implements improvements to maintain fresh nodes.
5. Fixes issues that can lead to an engine crash.

#### Aurora PostgreSQL

1.0.10

This update includes a new feature. You can now replicate an Amazon RDS PostgreSQL
DB instance to Aurora PostgreSQL. For more information, see [Replication with Amazon Aurora PostgreSQL](../AuroraUserGuide/AuroraPostgreSQL.md "../AuroraUserGuide/AuroraPostgreSQL.md") in the _Amazon Aurora User
Guide_.

You can find the following improvements in this engine update:

1. Adds error logging when a cache exists and a parameter change results
   in a mismatched buffer cache, storage format, or size.
2. Fixes an issue that causes an engine reboot if there is an
   incompatible parameter value for huge pages.
3. Improves handling of multiple truncate table statements during a
   replay of a write ahead log (WAL) on a read node.
4. Reduces static memory overhead to reduce out-of-memory errors.
5. Fixes an issue that can lead to out-of-memory errors while performing
   an insert with a GiST index.
6. Improves snapshot import from RDS for PostgreSQL, removing the requirement
   that a vacuum be performed on uninitialized pages.
7. Fixes an issue that causes prepared transactions to return to the
   previous state following an engine crash.
8. Implements improvements to prevent read nodes from becoming
   stale.
9. Implements improvements to reduce downtime with an engine
   restart.
10. Fixes issues that can cause an engine crash.

#### Aurora PostgreSQL

1.0.9

In this engine update, we fix an issue that can cause the Aurora storage
volume to become unavailable when importing a snapshot from RDS for PostgreSQL that
contained uninitialized pages.

#### Aurora PostgreSQL

1.0.8

You can find the following improvements in this engine update:

1. Fixes an issue that prevented the engine from starting if the
   `shared_preload_libraries` instance parameter contained
   `pg_hint_plan`.
2. Fixes the error "Attempt to fetch heap block XXX is beyond end of heap
   (YYY blocks)," which can occur during parallel scans.
3. Improves the effectiveness of prefetching on reads for a
   vacuum.
4. Fixes issues with snapshot import from RDS for PostgreSQL, which can fail
   if there are incompatible pg_internal.init files in the source
   snapshot.
5. Fixes an issue that can cause a read node to crash with the message
   "aurora wal replay process (PID XXX) was terminated by signal 11:
   Segmentation fault". This issue occurs when the reader applied a
   visibility map change for an uncached visibility map page.

#### Aurora PostgreSQL

1.0.7

This is the first generally available release of Amazon
Aurora PostgreSQL-Compatible Edition.
