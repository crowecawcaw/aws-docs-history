# Amazon RDS for PostgreSQL updates

Amazon RDS supports DB instances running several versions of PostgreSQL. You can specify any
currently available PostgreSQL version when creating a new DB instance. You can specify the
major version (such as PostgreSQL 10) and any available minor version for the specified
major version. If no version is specified, Amazon RDS defaults to an available version, typically
the most recent version. If a major version is specified but a minor version isn't,
Amazon RDS defaults to a recent release of the major version that you specified.

To see a list of available versions, and also defaults for newly created DB instances, use
the [`describe-db-engine-versions`](../../../cli/latest/reference/rds/describe-db-engine-versions.md "../../../cli/latest/reference/rds/describe-db-engine-versions.md") AWS CLI command. For example, to display
the default PostgreSQL engine version, use the following command.

```
aws rds describe-db-engine-versions --default-only --engine postgres
```

To learn more about versioning policy for RDS for PostgreSQL, see [Amazon RDS FAQs](https://aws.amazon.com/rds/faqs/ "https://aws.amazon.com/rds/faqs/"). For more information about PostgreSQL versions, see
[Versioning Policy](https://www.postgresql.org/support/versioning/ "https://www.postgresql.org/support/versioning/") in
the PostgreSQL documentation.

###### Topics

- [PostgreSQL 18 versions](#postgresql-version18 "#postgresql-version18")
- [PostgreSQL 17 versions](#postgresql-version17 "#postgresql-version17")
- [PostgreSQL 16 versions](#postgresql-version16 "#postgresql-version16")
- [PostgreSQL 15 versions (Some of these versions have
  reached the end of standard support or deprecated.)](#postgresql-version15 "#postgresql-version15")
- [PostgreSQL 14 versions](#postgresql-versions-version14 "#postgresql-versions-version14")
- [PostgreSQL 13 versions](#postgresql-versions-version13 "#postgresql-versions-version13")
- [PostgreSQL 12 versions (Some of these versions have reached the end of standard support or deprecated.)](#postgresql-versions-version12 "#postgresql-versions-version12")
- [PostgreSQL 11 versions (Some of these versions
  have reached the end of standard support or deprecated.)](#postgresql-versions-version11 "#postgresql-versions-version11")
- [PostgreSQL 10 versions (Deprecated)](#postgresql-versions-version10 "#postgresql-versions-version10")
- [PostgreSQL 9.6 versions (Deprecated)](#postgresql-versions-version96 "#postgresql-versions-version96")
- [Deprecation of
  PostgreSQL 10](#postgresql-versions-version10-deprecation-notice "#postgresql-versions-version10-deprecation-notice")
- [Deprecation of
  PostgreSQL 9.6](#postgresql-versions-version96-deprecation-notice "#postgresql-versions-version96-deprecation-notice")

## PostgreSQL 18 versions

###### Minor versions

- [PostgreSQL version 18.0 in the
  Amazon RDS Preview environment](#postgresql-versions-version180Preview "#postgresql-versions-version180Preview")
- [PostgreSQL version 18 RC1 in the
  Amazon RDS Preview environment](#postgresql-versions-version18RC1 "#postgresql-versions-version18RC1")
- [PostgreSQL version 18 Beta 3 in the
  Amazon RDS Preview environment](#postgresql-versions-version18Beta3 "#postgresql-versions-version18Beta3")
- [PostgreSQL version 18 Beta 2 in the
  Amazon RDS Preview environment](#postgresql-versions-version18Beta2 "#postgresql-versions-version18Beta2")
- [PostgreSQL version 18 Beta 1 in the
  Amazon RDS Preview environment](#postgresql-versions-version18Beta1 "#postgresql-versions-version18Beta1")

### PostgreSQL version 18.0 in the

Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 18 is subject to change.

PostgreSQL 18 contains many new features and enhancements that can be seen in the
following release documentation, [PostgreSQL 18](https://www.postgresql.org/docs/18/release-18.html "https://www.postgresql.org/docs/18/release-18.html").

The following extensions were added:

- pglogical
- postgis
- pgrouting
- h3-pg

This version also includes the following extension changes:

- The `pg_bigm` extension was updated to version v1.2-20250903

The following extension supported in RDS for PostgreSQL version 17 isn't supported for
RDS for PostgreSQL version 18.0 in preview:

- `pgAudit`
- `plrust`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
18](postgresql-extensions.md#postgresql-extensions-18x "postgresql-extensions.md#postgresql-extensions-18x").

### PostgreSQL version 18 RC1 in the

Amazon RDS Preview environment

PostgreSQL 18 RC1 contains many new features and enhancements that can be seen in the
release documentation: [PostgreSQL 18 RC1 Released!](https://www.postgresql.org/about/news/postgresql-18-rc-1-released-3130/ "https://www.postgresql.org/about/news/postgresql-18-rc-1-released-3130/").

The following extensions were added:

- `pg_hint_plan`
- `tds_fdw`
- `pg_transport`

This version also includes the following extension changes:

- The `hypopg` extension was updated to version 1.4.2
- The `pg_repack` extension was updated to version 1.5.2
- The `pgactive` extension was updated to version 2.1.6

The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't supported for Amazon RDS PostgreSQL version 18 Beta 3 in preview:

- `address_standardizer`
- `address_standardizer_data_us`
- `h3-pg`
- `pgAudit`
- `pglogical`
- `pgrouting`
- `plrust`
- `PostGIS`
- `postgis_raster`
- `postgis_tiger_geocoder`
- `postgis_topology`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
18](postgresql-extensions.md#postgresql-extensions-18x "postgresql-extensions.md#postgresql-extensions-18x").

### PostgreSQL version 18 Beta 3 in the

Amazon RDS Preview environment

PostgreSQL 18 Beta 3 contains many new features and enhancements that can be seen in the
release documentation: [PostgreSQL 18 Beta 3 Released!](https://www.postgresql.org/about/news/postgresql-176-1610-1514-1419-1322-and-18-beta-3-released-3118/ "https://www.postgresql.org/about/news/postgresql-176-1610-1514-1419-1322-and-18-beta-3-released-3118/").

The following modifiable parameters were added:

- `autovacuum_vacuum_max_threshold`
- `track_cost_delay_timing`
- `idle_replication_slot_timeout`
- `md5_password_warnings`
- `log_lock_failure`
- `restrict_nonsystem_relation_kind`
- `vacuum_truncate`
- `vacuum_max_eager_freeze_failure_rate`
- `enable_distinct_reordering`
- `enable_self_join_elimination`
- `max_active_replication_origins`
- `io_max_combine_limit`

The following extensions were added:

- `plv8`
- `pgactive`

The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't supported for Amazon RDS PostgreSQL version 18 Beta 3 in preview:

- `address_standardizer`
- `address_standardizer_data_us`
- `h3-pg`
- `pg_hint_plan`
- `pg_transport`
- `pgAudit`
- `pglogical`
- `pgrouting`
- `plrust`
- `PostGIS`
- `postgis_raster`
- `postgis_tiger_geocoder`
- `postgis_topology`
- `tds_fdw`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
18](postgresql-extensions.md#postgresql-extensions-18x "postgresql-extensions.md#postgresql-extensions-18x").

### PostgreSQL version 18 Beta 2 in the

Amazon RDS Preview environment

PostgreSQL 18 Beta 2 contains many new features and enhancements that can be seen in the
release documentation: [PostgreSQL 18 Beta 2 Released!](https://www.postgresql.org/about/news/postgresql-18-beta-2-released-3103/ "https://www.postgresql.org/about/news/postgresql-18-beta-2-released-3103/").

The following loadable module was added in this release:

- `pg_overexplain`

The following extensions were added in this release:

- `pg_tap`
- `oracle_fdw`
- `pg_bigm`
- `pg_partman`
- `pg_proctab`
- `pg_repack`
- `pg_tle`
- `rdkit`

The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't supported for Amazon RDS PostgreSQL version 18 Beta 2 in preview:

- `address_standardizer`
- `address_standardizer_data_us`
- `h3-pg`
- `pg_hint_plan`
- `pg_transport`
- `pgactive`
- `pgAudit`
- `pglogical`
- `pgrouting`
- `plrust`
- `plv8`
- `PostGIS`
- `postgis_raster`
- `postgis_tiger_geocoder`
- `postgis_topology`
- `tds_fdw`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
18](postgresql-extensions.md#postgresql-extensions-18x "postgresql-extensions.md#postgresql-extensions-18x").

### PostgreSQL version 18 Beta 1 in the

Amazon RDS Preview environment

PostgreSQL 18 Beta 1 contains many new features and enhancements that can be seen in the
release documentation: [PostgreSQL 18 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/ "https://www.postgresql.org/about/news/postgresql-18-beta-1-released-3070/").

This release includes the following version updates:

- `LLVM` version updated to 20.1.1
- `LZ4` version updated to 1.10.0
- `Zstd` version updated to 1.5.7
- `Zlib` version updated to 1.3.1
- `AWS-LC` version updated to AWS-LC FIPS 3.0
- `Kerberos` version updated to 1.21.3
- `Perl` version updated to 5.40.2
- `ossp-uuid` now uses the e2fs UUID implementation

The following extensions that are supported in Amazon RDS PostgreSQL version 17 aren't supported for Amazon RDS PostgreSQL version 18 Beta 1 in preview:

- `address_standardizer`
- `address_standardizer_data_us`
- `h3-pg`
- `oracle_fdw`
- `pg_bigm`
- `pg_hint_plan`
- `pg_partman`
- `pg_proctab`
- `pg_repack`
- `pg_tle`
- `pg_transport`
- `pgactive`
- `pgAudit`
- `pglogical`
- `pgrouting`
- `pgTAP`
- `plrust`
- `pltcl`
- `plv8`
- `PostGIS`
- `postgis_raster`
- `postgis_tiger_geocoder`
- `postgis_topology`
- `rdkit`
- `tds_fdw`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
18](postgresql-extensions.md#postgresql-extensions-18x "postgresql-extensions.md#postgresql-extensions-18x").

## PostgreSQL 17 versions

###### Minor versions

- [PostgreSQL version 17.6-R2 on
  Amazon RDS](#postgresql-versions-version176R2 "#postgresql-versions-version176R2")
- [PostgreSQL version 17.6 on Amazon RDS](#postgresql-versions-version176 "#postgresql-versions-version176")
- [PostgreSQL version 17.5-R2 on Amazon RDS](#postgresql-versions-version175R2 "#postgresql-versions-version175R2")
- [PostgreSQL version 17.5 on Amazon RDS](#postgresql-versions-version175R1 "#postgresql-versions-version175R1")
- [PostgreSQL version 17.4-R2 on Amazon RDS](#postgresql-versions-version174R2 "#postgresql-versions-version174R2")
- [PostgreSQL version 17.4 on Amazon RDS](#postgresql-versions-version174 "#postgresql-versions-version174")
- [PostgreSQL version 17.3 on Amazon RDS](#postgresql-versions-version173R1 "#postgresql-versions-version173R1")
- [PostgreSQL version 17.2-R2 on Amazon RDS](#postgresql-versions-version172R2 "#postgresql-versions-version172R2")
- [PostgreSQL version 17.2 on Amazon RDS](#postgresql-versions-version172 "#postgresql-versions-version172")
- [PostgreSQL version 17.1 on Amazon RDS](#postgresql-versions-version171 "#postgresql-versions-version171")
- [PostgreSQL version 17.0 in the
  Amazon RDS Preview environment](#postgresql-versions-version170Preview "#postgresql-versions-version170Preview")
- [PostgreSQL version 17 RC1 in the Amazon RDS
  Preview environment](#postgresql-versions-version17RC1 "#postgresql-versions-version17RC1")
- [PostgreSQL version 17 Beta 3 in the
  Amazon RDS Preview environment](#postgresql-versions-version17Beta3 "#postgresql-versions-version17Beta3")
- [PostgreSQL version 17 Beta 2 in the
  Amazon RDS Preview environment](#postgresql-versions-version17Beta2 "#postgresql-versions-version17Beta2")
- [PostgreSQL version 17 Beta 1 in the
  Amazon RDS Preview environment](#postgresql-versions-version17Beta1 "#postgresql-versions-version17Beta1")

### PostgreSQL version 17.6-R2 on

Amazon RDS

PostgreSQL version 17.6-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 17.6](https://www.postgresql.org/docs/release/17.6/ "https://www.postgresql.org/docs/release/17.6/").

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 17.6 on Amazon RDS

PostgreSQL version 17.6 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 17.6 release](https://www.postgresql.org/docs/release/17.6/ "https://www.postgresql.org/docs/release/17.6/").

**General enhancements**

- Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical
  upgrades and verification/validation.
- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.2.
- The `oracle_fdw` extension was updated to version 2.8.0.
- The `pgactive` extension was updated to version 2.1.5.

### PostgreSQL version 17.5-R2 on Amazon RDS

PostgreSQL version 17.5-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
17.6](https://www.postgresql.org/docs/release/17.6/ "https://www.postgresql.org/docs/release/17.6/").

**General enhancements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 17.5 on Amazon RDS

PostgreSQL version 17.5 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 17.5 release](https://www.postgresql.org/docs/release/17.5/ "https://www.postgresql.org/docs/release/17.5/").

**General enhancements**

- Fixed for the `address_standardizer_data_us` extension issue regarding ALTER
  EXTENSION UPDATE failure.
- Changed the Oracle client library version for the `oracle_fdw` extension on
  x86 to 19.26.0.0.0.
- Fixed the `pgactive` extension unable to upgrade issue due to incorrect
  extension upgrade scripts which causes replication to break after engine upgrade.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.1.
- The `pglogical` extension was updated to version 2.4.5.
- The `PgAudit` extension was updated to version 17.1.
- The `RDKit` extension was updated to version 2024_09_6.

### PostgreSQL version 17.4-R2 on Amazon RDS

PostgreSQL version 17.4-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
17.4](https://www.postgresql.org/docs/release/17.4/ "https://www.postgresql.org/docs/release/17.4/").

**Fixes and improvements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 17.4 on Amazon RDS

PostgreSQL version 17.4 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 17.4 release](https://www.postgresql.org/docs/release/17.4/ "https://www.postgresql.org/docs/release/17.4/").

### PostgreSQL version 17.3 on Amazon RDS

PostgreSQL version 17.3 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 17.3 release](https://www.postgresql.org/docs/release/17.3/ "https://www.postgresql.org/docs/release/17.3/").

**New features and enhancements**.

- In Blue/Green deployments, creating or modifying temporary objects is no longer classified as restricted DDL.
- The `postgres_get_av_diag` function has been updated to support radix tree optimization on PostgreSQL 17.
  Recommendations are now tailored to account for this new optimization feature.
- Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
- Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, see
  [RUSTSEC-2024-0421](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html").
- Applied Promise.any error allocation fix for V8 9.7.37, PLV8 3.1.10.

**This version also includes the following extension changes:**.

- The `rds_tools` extension was updated to 1.9.
- The `orafce` extension was updated to 4.14.0.
- The `pg_cron` extension was updated to 1.6.5.
- The `rdkit` extension was updated to 2024_09_3.
- The `pg_active` extension was updated to 2.1.4.
- The `pg_partman` extension was updated to 5.2.4.
- The `prefix` extension was updated to 1.2.10.
- The `PostGIS` extension was updated to 3.5.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17.2-R2 on Amazon RDS

PostgreSQL version 17.2-R2 is now available on Amazon RDS. This release contains fix for PLV8 [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in
[PostgreSQL 17.2](https://www.postgresql.org/docs/release/17.2/ "https://www.postgresql.org/docs/release/17.2/").

### PostgreSQL version 17.2 on Amazon RDS

PostgreSQL version 17.2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 17.2 release](https://www.postgresql.org/docs/release/17.2/ "https://www.postgresql.org/docs/release/17.2/").

### PostgreSQL version 17.1 on Amazon RDS

PostgreSQL version 17.1 is now available on Amazon RDS. This release contains many new features
and enhancements that can be seen in the following release documentation, [PostgreSQL 17.1](https://www.postgresql.org/docs/release/17.1/ "https://www.postgresql.org/docs/release/17.1/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is
  granted to Amazon RDS administrative users. The number of reserved connection slots is
  determined by the `rds.rds_reserved_connections` parameter. You may need
  to adjust the value of the `max_connections` parameter to account for the
  number of Amazon RDS reserved connection slots.

The `rds_reserved` role is a new predefined role created by Amazon RDS.
Predefined roles and their privileges can't be changed. You can't drop, rename, or
modify privileges for these predefined roles. Attempting to modify a predefined role
results in an error.

- Added vacuum blocker detection to improve autovacuum monitoring. For more
  information, see [Identify and resolve aggressive vacuum blockers in RDS for PostgreSQL](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md")
- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in
  Blue/Green replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.
- Added support for `plrust` version 1.2.7.

###### Updated features

- `PostGIS` was updated to version 3.5.0, and the following dependencies
  were updated:
  - `json-c` was updated to version 0.18_20240915.
  - `GDAL` was updated to version 3.9.3
  - `PROJ` was updated to version 9.5.0
  - `PROJ_DATA` was updated to version 1.19

- The `orafce` extension was updated to version 4.13.4.
- The `pg_bigm` extension was updated to version 1.2_20240606.
- The `pg_proctab` extension was updated to version 0.0.12.
- The `pg_repack` extension was updated to version 1.5.1.
- The `pgrouting` extension was updated to version 3.6.3.
- The `pgvector` extension was updated to version 0.8.0.
- The `rdkit` extension was updated to version 2024_09_2(4.6.1).
- The `rds_tools` extension was updated to version 1.8.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17.0 in the

Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 17 is subject to change.

PostgreSQL 17 contains many new features and enhancements that can be seen in the
following release documentation, [PostgreSQL 17](https://www.postgresql.org/docs/17/release-17.html "https://www.postgresql.org/docs/17/release-17.html").

###### New features

- `GCC` was upgraded to version 12.4.0
- Introduced a new Amazon RDS-specific parameter,
  `rds.logical_slot_sync_dbname`, to specify the dbname for the
  PostgreSQL version 17 logical slots synchronization and failover feature.For more
  information, see [Managing logical slot synchronization for RDS for PostgreSQL](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.pglogical.slot.md").

This version also includes the following extension and dependency updates:

- The following `PostGIS` dependencies were updated:
  - `gdal` was upgraded to version 3.9.2
  - `PROJ` was upgraded to version 9.4.1
  - `PROJ_DATA` was upgraded to version 1.18
  - `GEOS` was upgraded to version 3.13.0

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.12.0.
- The `pg_buffercache` extension was updated to version 1.5.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_stat_statements` extension was updated to version 1.11.
- The `pgaudit` extension was updated to version 17.0.
- The `pgvector` extension was updated to version 0.7.4.
- The `plprofiler` extension was updated to version 4.2.5.
- The `rds_tools` extension was updated to version 1.6.
- The `tds_fdw` extension was updated to version 2.0.4.

The following extension supported in RDS for PostgreSQL version 16 isn't supported for
RDS for PostgreSQL version 17.0 in preview:

- `plrust`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17 RC1 in the Amazon RDS

Preview environment

###### Note

The preview documentation for Amazon RDS for PostgreSQL version 17 is subject to
change.

PostgreSQL 17 RC1 contains many new features and enhancements that can be seen in the
following release documentation, [PostgreSQL
17 RC1 Released!](https://www.postgresql.org/about/news/postgresql-17-rc1-released-2926/ "https://www.postgresql.org/about/news/postgresql-17-rc1-released-2926/").

###### New features

- Performance Insights is supported in the preview environment.

###### New extensions

- The `pg_logical` extension was added.

This version also includes the following extension updates:

- The `address_standardizer` extension was updated to version
  3.5.0alpha2.
- The `address_standardizer_data_us` extension was updated to version
  3.5.0alpha2.
- The `PostGIS` extension was updated to version 3.5.0alpha2.
- The `postgis_raster` extension was updated to version
  3.5.0alpha2.
- The `postgis_tiger_geocoder` extension was updated to version
  3.5.0alpha2.
- The `postgis_topology` extension was updated to version
  3.5.0alpha2.

The following extension supported in RDS for PostgreSQL version 16 isn't supported in
RDS for PostgreSQL version 17 RC1 in preview:

- `plrust`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17 Beta 3 in the

Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 17 is subject to change.

PostgreSQL 17 Beta 3 contains many new features and enhancements that can be seen in the
following release documentation, [PostgreSQL 17 Beta 3 Released!](https://www.postgresql.org/about/news/postgresql-164-158-1413-1316-1220-and-17-beta-3-released-2910/ "https://www.postgresql.org/about/news/postgresql-164-158-1413-1316-1220-and-17-beta-3-released-2910/").

###### New features

- The t4g instance type is supported in the Preview environment.
- The `wal_compression` default value for TAZ cluster is now
  `lz4` instead of `zstd`.

###### New extensions

- The `pg_hint_plan` extension was added.
- The `plv8` extension was added.
- The `rdkit` extension was added.

This version also includes the following extension updates:

- The `orafce` extension was updated to version 4.10.3.
- The `pg_cron` extension was updated to version 1.6.3.
- The `pg_vector` extension was updated to version 0.7.3.

The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported
for Amazon RDS PostgreSQL version 17 Beta 3 in preview:

- `pglogical`
- `plrust`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17 Beta 2 in the

Amazon RDS Preview environment

PostgreSQL 17 Beta 2 contains many new features and enhancements that can be seen in the
following release documentation, [PostgreSQL 17 Beta 2 Released!](https://www.postgresql.org/about/news/postgresql-17-beta-2-released-2885/ "https://www.postgresql.org/about/news/postgresql-17-beta-2-released-2885/").

###### New extensions

- The `h3-pg` extension was added.
- The `mysql_fdw` extension was added.
- The `pg_cron` extension was added.
- The `pgactive` extension was added.
- The `pgAudit` extension was added.
- The `pg_repack` extension was added.
- The `tds_fdw` extension was added.

This version also includes the following extension update:

- The `pgTAP` extension was updated to version 1.3.3.

The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported
for Amazon RDS PostgreSQL version 17 Beta 2 in preview:

- `pg_hint_plan`
- `pglogical`
- `plrust`
- `plv8`
- `rdkit`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

### PostgreSQL version 17 Beta 1 in the

Amazon RDS Preview environment

PostgreSQL 17 Beta 1 contains many new features and enhancements that can be seen in the
release documentation: [PostgreSQL 17 Beta 1 Released!](https://www.postgresql.org/about/news/postgresql-164-158-1413-1316-1220-and-17-beta-3-released-2910/ "https://www.postgresql.org/about/news/postgresql-164-158-1413-1316-1220-and-17-beta-3-released-2910/").

The following extensions supported in Amazon RDS PostgreSQL version 16 aren't supported
for Amazon RDS PostgreSQL version 17 Beta 1 in preview:

- `h3pg`
- `MySQL_FDW`
- `pg_cron`
- `pg_repack`
- `pgactive`
- `pgaudit`
- `pghintplan`
- `pglogical`
- `plrust`
- `plv8`
- `rdkit`
- `tds_fdw`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
17](postgresql-extensions.md#postgresql-extensions-17x "postgresql-extensions.md#postgresql-extensions-17x").

## PostgreSQL 16 versions

###### Minor versions

- [PostgreSQL version 16.10-R2 on
  Amazon RDS](#postgresql-versions-version1610R2 "#postgresql-versions-version1610R2")
- [PostgreSQL version 16.10 on Amazon RDS](#postgresql-versions-version1610 "#postgresql-versions-version1610")
- [PostgreSQL version 16.9-R2 on Amazon RDS](#postgresql-versions-version169 "#postgresql-versions-version169")
- [PostgreSQL version 16.9 on Amazon RDS](#postgresql-versions-version169R1 "#postgresql-versions-version169R1")
- [PostgreSQL version 16.8-R2 on Amazon RDS](#postgresql-versions-version168R2 "#postgresql-versions-version168R2")
- [PostgreSQL version 16.8 on Amazon RDS](#postgresql-versions-version168 "#postgresql-versions-version168")
- [PostgreSQL version 16.7 on Amazon RDS](#postgresql-versions-version167R1 "#postgresql-versions-version167R1")
- [PostgreSQL version 16.6-R2 on Amazon RDS](#postgresql-versions-version166R2 "#postgresql-versions-version166R2")
- [PostgreSQL version 16.6 on Amazon RDS](#postgresql-versions-version166 "#postgresql-versions-version166")
- [PostgreSQL version 16.5 on Amazon RDS](#postgresql-versions-version165 "#postgresql-versions-version165")
- [PostgreSQL version 16.4-R3 on
  Amazon RDS](#postgresql-versions-version164R3 "#postgresql-versions-version164R3")
- [PostgreSQL version 16.4-R2 on Amazon RDS](#postgresql-versions-version164R2 "#postgresql-versions-version164R2")
- [PostgreSQL version 16.4 on Amazon RDS](#postgresql-versions-version164 "#postgresql-versions-version164")
- [PostgreSQL version 16.3-R4 on Amazon RDS](#postgresql-versions-version163R4 "#postgresql-versions-version163R4")
- [PostgreSQL version 16.3-R3 on Amazon RDS](#postgresql-versions-version163R3 "#postgresql-versions-version163R3")
- [PostgreSQL version 16.3-R2 on Amazon RDS](#postgresql-versions-version163R2 "#postgresql-versions-version163R2")
- [PostgreSQL version 16.3 on Amazon RDS](#postgresql-versions-version163 "#postgresql-versions-version163")
- [PostgreSQL version 16.2-R3 on Amazon RDS](#postgresql-versions-version162R3 "#postgresql-versions-version162R3")
- [PostgreSQL version 16.2-R2 on Amazon RDS](#postgresql-versions-version162R2 "#postgresql-versions-version162R2")
- [PostgreSQL version 16.2 on Amazon RDS](#postgresql-versions-version162 "#postgresql-versions-version162")
- [PostgreSQL version 16.1-R2 on Amazon RDS](#postgresql-versions-version161R2 "#postgresql-versions-version161R2")
- [PostgreSQL version 16.1 on Amazon RDS](#postgresql-versions-version161 "#postgresql-versions-version161")
- [PostgreSQL version 16.0 in the Amazon RDS
  Preview environment](#postgresql-versions-version160Preview "#postgresql-versions-version160Preview")
- [PostgreSQL version 16 RC1 in the Amazon RDS
  Preview environment](#postgresql-versions-version16RC1 "#postgresql-versions-version16RC1")
- [PostgreSQL version 16 Beta 3 in the
  Amazon RDS Preview environment](#postgresql-versions-version16Beta3 "#postgresql-versions-version16Beta3")
- [PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment](#postgresql-versions-version16Beta2 "#postgresql-versions-version16Beta2")
- [PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment](#postgresql-versions-version16Beta1 "#postgresql-versions-version16Beta1")

### PostgreSQL version 16.10-R2 on

Amazon RDS

PostgreSQL version 16.10-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 16.10](https://www.postgresql.org/docs/release/16.10/ "https://www.postgresql.org/docs/release/16.10/").

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 16.10 on Amazon RDS

PostgreSQL version 16.10 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 16.10 release](https://www.postgresql.org/docs/release/16.10/ "https://www.postgresql.org/docs/release/16.10/").

**General enhancements**

- Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical
  upgrades and verification/validation.
- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.2.
- The `oracle_fdw` extension was updated to version 2.8.0.
- The `pgactive` extension was updated to version 2.1.5.

### PostgreSQL version 16.9-R2 on Amazon RDS

PostgreSQL version 16.9-R2 is now available on Amazon RDS. This release contains several fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
16.10](https://www.postgresql.org/docs/release/16.10/ "https://www.postgresql.org/docs/release/16.10/").

**General enhancements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 16.9 on Amazon RDS

PostgreSQL version 16.9 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 16.9 release](https://www.postgresql.org/docs/release/16.9/ "https://www.postgresql.org/docs/release/16.9/").

**General enhancements**

- Fixed for the `address_standardizer_data_us` extension issue regarding ALTER
  EXTENSION UPDATE failure.
- Changed the Oracle client library version on x86 to 19.26.0.0.0.
- Fixed the `pgactive` extension unable to upgrade issue due to incorrect
  extension upgrade scripts which causes replication to break after engine upgrade.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.1.
- The `pglogical` extension was updated to version 2.4.5.
- The `PgAudit` extension was updated to version 16.1.
- The `RDKit` extension was updated to version 2024_09_6.

### PostgreSQL version 16.8-R2 on Amazon RDS

PostgreSQL version 16.8-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
16.8](https://www.postgresql.org/docs/release/16.8/ "https://www.postgresql.org/docs/release/16.8/").

**Fixes and improvements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 16.8 on Amazon RDS

PostgreSQL version 16.8 is now available on Amazon RDS. This release contains several fixes and improvements for
PostgreSQL announced in the [PostgreSQL 16.8 release](https://www.postgresql.org/docs/release/16.8/ "https://www.postgresql.org/docs/release/16.8/").

### PostgreSQL version 16.7 on Amazon RDS

PostgreSQL version 16.7 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 16.7 release](https://www.postgresql.org/docs/release/16.7/ "https://www.postgresql.org/docs/release/16.7/").

**New features and enhancements**.

- In Blue/Green deployments, creating or modifying temporary objects is no longer classified as restricted DDL.
- Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
- Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, see
  [RUSTSEC-2024-0421](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html").
- Applied Promise.any error allocation fix for V8 9.7.37, PLV8 3.1.10.

**This version also includes the following extension changes:**.

- The `rds_tools` extension was updated to 1.9.
- The `orafce` extension was updated to 4.14.0.
- The `pg_cron` extension was updated to 1.6.5.
- The `rdkit` extension was updated to 2024_09_3.
- The `pg_active` extension was updated to 2.1.4.
- The `pg_partman` extension was updated to 5.2.4.
- The `prefix` extension was updated to 1.2.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.6-R2 on Amazon RDS

PostgreSQL version 16.6-R2 is now available on Amazon RDS. This release contains fix for PLV8 [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in
[PostgreSQL 16.6](https://www.postgresql.org/docs/release/16.6/ "https://www.postgresql.org/docs/release/16.6/").

### PostgreSQL version 16.6 on Amazon RDS

PostgreSQL version 16.6 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 16.6 release](https://www.postgresql.org/docs/release/16.6/ "https://www.postgresql.org/docs/release/16.6/").

### PostgreSQL version 16.5 on Amazon RDS

PostgreSQL version 16.5 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 16.5](https://www.postgresql.org/docs/release/16.5/ "https://www.postgresql.org/docs/release/16.5/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is granted
  to Amazon RDS administrative users. The number of reserved connection slots is determined by the
  `rds.rds_reserved_connections` parameter . You may need to adjust the value of
  the `max_connections` parameter to account for the number of Amazon RDS reserved
  connection slots.

The `rds_reserved` role is a new predefined role created by Amazon RDS. Predefined
roles and their privileges can't be changed. You can't drop, rename, or modify privileges
for these predefined roles. Attempting to modify a predefined role results in an
error.

- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in Blue/Green
  replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.

###### Updated features

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.13.4.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_hint_plan` extension was updated to version 1.6.1.
- The `pgvector` extension was updated to version 0.8.0.
- The `plprofiler` extension was updated to version 4.2.5.
- The `PostGIS` extension was updated to version 3.4.3.
- The `rdkit` extension was updated to version 4.6.1.
- The `rds_tools` extension was updated to version 1.7.
- The `tds_fdw` extension was updated to version 2.0.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.4-R3 on

Amazon RDS

PostgreSQL version 16.4-R3 is now available on Amazon RDS. This release contains fixes for
[CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 16.4](https://www.postgresql.org/docs/release/16.4/ "https://www.postgresql.org/docs/release/16.4/").

### PostgreSQL version 16.4-R2 on Amazon RDS

PostgreSQL version 16.4-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 16.4 release](https://www.postgresql.org/docs/release/16.4/ "https://www.postgresql.org/docs/release/16.4/").

### PostgreSQL version 16.4 on Amazon RDS

PostgreSQL version 16.4 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 16.4 release](https://www.postgresql.org/docs/release/16.4/ "https://www.postgresql.org/docs/release/16.4/").

**New features and enhancements**

- [Delegated extension role](../UserGuide/RDS_delegated_ext.md "../UserGuide/RDS_delegated_ext.md") was added.
- Fixed [CVE-2024-7348](https://www.postgresql.org/support/security/CVE-2024-7348/ "https://www.postgresql.org/support/security/CVE-2024-7348/") that prevents search path restrictions bypass through
  pattern-matching queries in information_schema.

This version also includes the following extension updates:

- The `hypopg` extension was updated to 1.4.1.
- The `mysql_fdw` extension was updated to 2.9.2.
- The `orafce` extension was updated to 4.10.3.
- The `pg_cron` extension was updated to 1.6.3.
- The `pgTAP` extension was updated to 1.3.3.
- The `pgvector` extension was updated to 0.7.3.
- The `rdkit` extension was updated to 4.5.0 (Release 2024_03_5).
- The `wal2json` extension was updated to 2.6.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.3-R4 on Amazon RDS

PostgreSQL version 16.3-R4 is now available on Amazon RDS. This release contains fixes for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and Rust
[CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 16.3](https://www.postgresql.org/docs/release/16.3/ "https://www.postgresql.org/docs/release/16.3/").

### PostgreSQL version 16.3-R3 on Amazon RDS

PostgreSQL version 16.3-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 16.3 release](https://www.postgresql.org/docs/release/16.3/ "https://www.postgresql.org/docs/release/16.3/").

### PostgreSQL version 16.3-R2 on Amazon RDS

PostgreSQL version 16.3-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 16.3 release](https://www.postgresql.org/docs/release/16.3/ "https://www.postgresql.org/docs/release/16.3/").

**New features and enhancements**

- Includes support for four new crates in PL/Rust, including:
  - `regex`
  - `serde`
  - `serde_json`
  - `url`

- Fixed a security issue in `pg_repack`
- Fixed a performance issue in `pgvector` for index creation on halfvec data
  type
- Fixed a bug in `aws_s3` causing import queries to occasionally get stuck and
  fail to terminate

### PostgreSQL version 16.3 on Amazon RDS

PostgreSQL version 16.3 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 16.3 release](https://www.postgresql.org/docs/release/16.3/ "https://www.postgresql.org/docs/release/16.3/").

**New features and enhancements**

- The blue/green deployment switchover won’t be blocked by the `REFRESH MATERIALIZED
VIEW` statement.
- Fixed the permission denial for the `CREATE DATABASE WITH OWNER`
  statement.
- Upgraded the `aws_s3` extension to version 1.2 to support the export to S3
  with the KMS customer managed key.
- Fixed a pgvector compatibility issue with some of the previous generations of DB
  instances, such as m4.

This version also includes the following extension updates:

- The `aws_s3` extension was updated to 1.2.
- The `orafce` extension was updated to 4.9.4.
- The `pg_partman` extension was updated to 5.1.0.
- The `pgvector` extension was updated to 0.7.0.
- The `postgis` extension was updated to 3.4.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.2-R3 on Amazon RDS

PostgreSQL version 16.2-R3 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 16.2 release](https://www.postgresql.org/docs/release/16.2/ "https://www.postgresql.org/docs/release/16.2/").

**New features and enhancements**.

- Fixed a security issue in `pg_repack`

### PostgreSQL version 16.2-R2 on Amazon RDS

PostgreSQL version 16.2-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 16.2 release](https://www.postgresql.org/docs/release/16.2/ "https://www.postgresql.org/docs/release/16.2/").

**New features and enhancements**.

- Fixed a bug allowing the querying of the security invoker views as an unprivileged user.
- Fixed a bug preventing `tds_fdw` from connecting when TLS is enabled.
- Fixed a bug preventing upgrades to `PostGIS` version 3.4.1.
- Fixed an error with the `aws_s3` extension when the Region was not provided.

**This version also includes the following extension changes:**.

- The `pg_partman` extension was updated to 5.0.1.
- The `pg_tle` extension was updated to 1.4.0.
- The `pgactive` extension was updated to 2.1.3.
- The `pgtap` extension was updated to 1.3.2.
- The `pgvector` extension was updated to 0.6.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.2 on Amazon RDS

#### PostgreSQL version 16.2 on Amazon RDS

PostgreSQL version 16.2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 16.2 release.](https://www.postgresql.org/docs/release/16.2/ "https://www.postgresql.org/docs/release/16.2/").

###### New features and enhancements

- Added support for `pg_log_standby_snapshot`
- Fixed the multisecond latency on the `aws_lambda` calls
- Fixed a bug preventing the termination of autovacuum
- Fixed a bug preventing the creation of the `h3` extension

This version includes the following changes:

- The `orafce` extension was updated to version 4.9.0.
- The `pg_repack` extension was updated to version 1.5.0.
- The `pgactive` extension was updated to version 2.1.2.
- The `pgvector` extension was updated to 0.6.0.
- The `plv8` extension was updated to 3.1.10.
- The `PostGIS` extension was updated to 3.4.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.1-R2 on Amazon RDS

PostgreSQL version 16.1-R2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 16 release.](https://www.postgresql.org/docs/release/16.1/ "https://www.postgresql.org/docs/release/16.1/").

###### New features and enhancements

- Fixed a crash in `CatalogCacheComputeHashValue` with `dblink_connect` due to a `Null` or `invalid` connection
- Supported the AWS SDK version of the `aws_s3` extension
- Fixed the overflow in the `pg_transport` extension
- Removed the unsupported shared libraries from the engine binary

This version includes the following changes:

- The `plrust` extension was updated to version 1.2.7.
- The `plv8` extension was updated to version 3.1.9.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.1 on Amazon RDS

PostgreSQL version 16.1 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 16 release.](https://www.postgresql.org/docs/release/16.1/ "https://www.postgresql.org/docs/release/16.1/").

###### New features and enhancements

- The aws-lc now uses a FIPS version.
- Allow setting TLS 1.3 as the `ssl_min_protocol_version` and `ssl_max_protocol_version`.
- The `pgactive` extension was added.
- The `pglogical` extension was added.
- By default, the `default_toast_compression` DB instance parameter is set to `lz4`.
- The `rds.rds_superuser_reserved_connections` parameter has been deprecated in RDS for PostgreSQL version 16.
  The `reserved_connections` parameter should be utilized to reserve the number of connection slots. The
  `reserved_connections` parameter sets the number of connection slots reserved for roles with the
  `pg_use_reserved_connections` privileges. `rds_superuser` is a member of the
  `pg_use_reserved_connections` role by default. For more information, see the PostgreSQL
  documentation [reserved connections](https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-RESERVED-CONNECTIONS "https://www.postgresql.org/docs/current/runtime-config-connection.html#GUC-RESERVED-CONNECTIONS").

This version includes the following changes:

- The `hll` extension was updated to version 2.1.8.
- The `oracle_fdw` extension was updated to version 2.6.0.
- The `orafce` extension was updated to version 4.6.1.
- The `pg_cron` extension was updated to version 1.6.1.
- The `pg_partman` extension was updated to version 5.0.0.
- The `pgtap` extension was updated to version 1.3.1.
- The `pgvector` extension was updated to version 0.5.1.
- The `plprofiler` extension was updated to version 4.2.4.
- The `plrust` extension was updated to version 1.2.6.
- The `plv8` extension was updated to version 3.1.8.
- The `rdkit` extension was updated to version 4.4.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16.0 in the Amazon RDS

Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 16.0 is subject to
change.

###### Note

RDS for PostgreSQL versions 16 RC1, 16 Beta 3, 16 Beta 2, and 16 Beta 1 will not be
supported after RDS for PostgreSQL version 16.0 is released in the Preview
environment.

PostgreSQL version 16.0 is now available in the Amazon RDS Preview environment. PostgreSQL
version 16 contains several improvements that are described in the [PostgreSQL 16
release](https://www.postgresql.org/about/news/postgresql-16-released-2715/ "https://www.postgresql.org/about/news/postgresql-16-released-2715/").

This version includes the following changes:

- The `mysql_fdw` extension was updated to version 2.9.1
- The `pgrouting` extension was updated to version 3.5.0
- The `pgvector` extension was updated to version 0.5.0

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16 RC1 in the Amazon RDS

Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 16 RC1 is subject to
change.

PostgreSQL version 16 RC1 is now available in the Amazon RDS Preview environment. PostgreSQL
version 16 RC1 contains several improvements that are described in the following PostgreSQL
documentation: [PostgreSQL
16 RC1 Released](https://www.postgresql.org/about/news/postgresql-16-rc1-released-2702/ "https://www.postgresql.org/about/news/postgresql-16-rc1-released-2702/").

###### New extensions

- The `pg_proctab` extension was added.
- The `rdkit` extension was added.
- The `hll` extension was added.
- The `pg_cron` extension was added.

This version also includes the following change:

- The `PostGIS` extension was updated to version 3.4.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16 Beta 3 in the

Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 16 beta 3 is subject to
change.

PostgreSQL version 16 Beta 3 is now available in the Amazon RDS Preview environment. PostgreSQL
version 16 Beta 3 contains several improvements that are described in the following
PostgreSQL documentation: [PostgreSQL 16 Beta 3 Released](https://www.postgresql.org/about/news/postgresql-154-149-1312-1216-1121-and-postgresql-16-beta-3-released-2689/ "https://www.postgresql.org/about/news/postgresql-154-149-1312-1216-1121-and-postgresql-16-beta-3-released-2689/").

###### New extensions

- The `h3-pg` extension was added.
- The `mysql_fdw` extension was added.
- The `oracle_fdw` extension was added.
- The `pg_bigm` extension was added.
- The `pg_hint_plan` extension was added.
- The `pgAudit` extension was added.
- The `plprofiler` extension was added.
- The `plrust` extension was added.
- The `plv8` extension was added.

This version also includes the following change:

- The `pg_tle` extension was updated to version 1.1.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16 Beta 2 in the Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 16 Beta 2 is subject to change.

PostgreSQL version 16 Beta 2 is now available in the Amazon RDS Preview environment.
PostgreSQL version 16 Beta 2 contains several improvements that are described in the following PostgreSQL documentation:
[PostgreSQL 16 Beta 2 Released](https://www.postgresql.org/about/news/postgresql-16-beta-2-released-2665/ "https://www.postgresql.org/about/news/postgresql-16-beta-2-released-2665/").

###### New extensions

- The `aws_commons` extension was added.
- The `aws_lambda` extension was added.
- The `aws_s3` extension was added.
- The `hypopg` extension was added.
- The `orafce` extension was added.

This version also includes the following change:

- `pgvector` was updated to version 0.4.4

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

### PostgreSQL version 16 Beta 1 in the Amazon RDS Preview environment

###### Note

The preview documentation for Amazon RDS PostgreSQL version 16 Beta 1 is subject to change.

PostgreSQL version 16 Beta 1 is now available in the Amazon RDS Preview environment.
PostgreSQL version 16 Beta 1 contains several improvements that are described in the following PostgreSQL documentation:
[PostgreSQL 16 Beta 1 Released](https://www.postgresql.org/about/news/postgresql-16-beta-1-released-2643/ "https://www.postgresql.org/about/news/postgresql-16-beta-1-released-2643/").

The following extensions supported in Amazon RDS PostgreSQL version 15 aren't supported for Amazon RDS PostgreSQL version 16 Beta 1 in preview:

- `aws_commons`
- `aws_lambda`
- `aws_s3`
- `hll`
- `hypoPG`
- `mysql_fdw`
- `oracle_fdw`
- `orafce`
- `pg_bigm`
- `pg_cron`
- `pg_proctab`
- `pgaudit`
- `pghintplan`
- `pglogical`
- `plprofiler`
- `plrust`
- `plv8`
- `rdkit`

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
16](postgresql-extensions.md#postgresql-extensions-16x "postgresql-extensions.md#postgresql-extensions-16x").

## PostgreSQL 15 versions (Some of these versions have

reached the end of standard support or deprecated.)

###### Minor versions

- [PostgreSQL version 15.14-R2 on
  Amazon RDS](#postgresql-versions-version1514R2 "#postgresql-versions-version1514R2")
- [PostgreSQL version 15.14 on Amazon RDS](#postgresql-versions-version1514 "#postgresql-versions-version1514")
- [PostgreSQL version 15.13-R2 on Amazon RDS](#postgresql-versions-version1513 "#postgresql-versions-version1513")
- [PostgreSQL version 15.13 on Amazon RDS](#postgresql-versions-version1513R1 "#postgresql-versions-version1513R1")
- [PostgreSQL version 15.12-R2 on Amazon RDS](#postgresql-versions-version1512R2 "#postgresql-versions-version1512R2")
- [PostgreSQL version 15.12 on Amazon RDS](#postgresql-versions-version1512 "#postgresql-versions-version1512")
- [PostgreSQL version 15.11 on Amazon RDS](#postgresql-versions-version1511R1 "#postgresql-versions-version1511R1")
- [PostgreSQL version 15.10-R2 on Amazon RDS](#postgresql-versions-version1510R2 "#postgresql-versions-version1510R2")
- [PostgreSQL version 15.10 on Amazon RDS](#postgresql-versions-version1510 "#postgresql-versions-version1510")
- [PostgreSQL version 15.9 on Amazon RDS](#postgresql-versions-version159 "#postgresql-versions-version159")
- [PostgreSQL version 15.8-R3 on Amazon RDS](#postgresql-versions-version158R3 "#postgresql-versions-version158R3")
- [PostgreSQL version 15.8-R2 on Amazon RDS](#postgresql-versions-version158R2 "#postgresql-versions-version158R2")
- [PostgreSQL version 15.8 on Amazon RDS](#postgresql-versions-version158 "#postgresql-versions-version158")
- [PostgreSQL version 15.7-R4 on
  Amazon RDS](#postgresql-versions-version157R4 "#postgresql-versions-version157R4")
- [PostgreSQL version 15.7-R3 on Amazon RDS](#postgresql-versions-version157R3 "#postgresql-versions-version157R3")
- [PostgreSQL version 15.7-R2 on Amazon RDS](#postgresql-versions-version157R2 "#postgresql-versions-version157R2")
- [PostgreSQL version 15.7 on Amazon RDS](#postgresql-versions-version157 "#postgresql-versions-version157")
- [PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version156R3 "#postgresql-versions-version156R3")
- [PostgreSQL version 15.6-R2 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version156R2 "#postgresql-versions-version156R2")
- [PostgreSQL version 15.6 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version156 "#postgresql-versions-version156")
- [PostgreSQL version 15.5-R2 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version155R2 "#postgresql-versions-version155R2")
- [PostgreSQL version 15.5 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version155 "#postgresql-versions-version155")
- [PostgreSQL version 15.4-R3 on
  Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version154R3 "#postgresql-versions-version154R3")
- [PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version154R2 "#postgresql-versions-version154R2")
- [PostgreSQL version 15.4 on Amazon RDS (This version has reached the end of standard support.)](#postgresql-versions-version154 "#postgresql-versions-version154")
- [PostgreSQL version 15.3-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version153R2 "#postgresql-versions-version153R2")
- [PostgreSQL version 15.3 on Amazon RDS (Deprecated)](#postgresql-versions-version153 "#postgresql-versions-version153")
- [PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version152R2 "#postgresql-versions-version152R2")
- [PostgreSQL version 15.2 on Amazon RDS (Deprecated)](#postgresql-versions-version152 "#postgresql-versions-version152")

### PostgreSQL version 15.14-R2 on

Amazon RDS

PostgreSQL version 15.14-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 15.14](https://www.postgresql.org/docs/release/15.14/ "https://www.postgresql.org/docs/release/15.14/").

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 15.14 on Amazon RDS

PostgreSQL version 15.14 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.14 release](https://www.postgresql.org/docs/release/15.14/ "https://www.postgresql.org/docs/release/15.14/").

**General enhancements**

- Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical
  upgrades and verification/validation.
- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.2.
- The `oracle_fdw` extension was updated to version 2.8.0.
- The `pgactive` extension was updated to version 2.1.5.

### PostgreSQL version 15.13-R2 on Amazon RDS

PostgreSQL version 15.13-R2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.13 release](https://www.postgresql.org/docs/release/15.13/ "https://www.postgresql.org/docs/release/15.13/").

[CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
15.14](https://www.postgresql.org/docs/release/15.14/ "https://www.postgresql.org/docs/release/15.14/").

**General enhancements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 15.13 on Amazon RDS

PostgreSQL version 15.13 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 15.13 release](https://www.postgresql.org/docs/release/15.13/ "https://www.postgresql.org/docs/release/15.13/").

**General enhancements**

- Fixed for the `address_standardizer_data_us` extension issue regarding ALTER
  EXTENSION UPDATE failure.
- Changed the Oracle client library version on x86 to 19.26.0.0.0.
- Fixed the `pgactive` extension unable to upgrade issue due to incorrect
  extension upgrade scripts which causes replication to break after engine upgrade.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.1.
- The `pglogical` extension was updated to version 2.4.5.
- The `PgAudit` extension was updated to version 1.7.1.
- The `RDKit` extension was updated to version 2024_09_6.

### PostgreSQL version 15.12-R2 on Amazon RDS

PostgreSQL version 15.12-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
15.12](https://www.postgresql.org/docs/release/15.12/ "https://www.postgresql.org/docs/release/15.12/").

**Fixes and improvements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 15.12 on Amazon RDS

PostgreSQL version 15.12 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced
in the [PostgreSQL 15.12 release](https://www.postgresql.org/docs/release/15.12/ "https://www.postgresql.org/docs/release/15.12/").

### PostgreSQL version 15.11 on Amazon RDS

PostgreSQL version 15.11 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.11 release](https://www.postgresql.org/docs/release/15.11/ "https://www.postgresql.org/docs/release/15.11/").

**New features and enhancements**.

- In Blue/Green deployments, creating or modifying temporary objects is no longer classified as restricted DDL.
- Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
- Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, see
  [RUSTSEC-2024-0421](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html").
- Applied Promise.any error allocation fix for V8 9.7.37, PLV8 3.1.10.

**This version also includes the following extension changes:**.

- The `rds_tools` extension was updated to 1.9.
- The `orafce` extension was updated to 4.14.0.
- The `pg_cron` extension was updated to 1.6.5.
- The `rdkit` extension was updated to 2024_09_3.
- The `pg_active` extension was updated to 2.1.4.
- The `pg_partman` extension was updated to 5.2.4.
- The `prefix` extension was updated to 1.2.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.10-R2 on Amazon RDS

PostgreSQL version 15.10-R2 is now available on Amazon RDS. This release fix for PLV8 [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in
[PostgreSQL 15.10](https://www.postgresql.org/docs/release/15.10/ "https://www.postgresql.org/docs/release/15.10/").

### PostgreSQL version 15.10 on Amazon RDS

PostgreSQL version 15.10 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 15.10 release](https://www.postgresql.org/docs/release/15.10/ "https://www.postgresql.org/docs/release/15.10/").

### PostgreSQL version 15.9 on Amazon RDS

PostgreSQL version 15.9 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 15.9](https://www.postgresql.org/docs/release/15.9/ "https://www.postgresql.org/docs/release/15.9/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is granted
  to Amazon RDS administrative users. The number of reserved connection slots is determined by the
  `rds.rds_reserved_connections` parameter . You may need to adjust the value of
  the `max_connections` parameter to account for the number of Amazon RDS reserved
  connection slots.

The `rds_reserved` role is a new predefined role created by
Amazon RDS. Predefined roles and their privileges can't be changed. You can't drop, rename, or
modify privileges for these predefined roles. Attempting to modify a predefined role results
in an error.

- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in Blue/Green
  replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.

###### Updated features

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.13.4.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_hint_plan` extension was updated to version 1.5.2.
- The `pgvector` extension was updated to version 0.8.0.
- The `plprofiler` extension was updated to version 4.2.5.
- The `PostGIS` extension was updated to version 3.4.3.
- The `rdkit` extension was updated to version 4.6.1.
- The `rds_tools` extension was updated to version 1.7.
- The `tds_fdw` extension was updated to version 2.0.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.8-R3 on Amazon RDS

PostgreSQL version 15.8-R3 is now available on Amazon RDS. This release contains fix for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced
in [PostgreSQL 15.8](https://www.postgresql.org/docs/release/15.8/ "https://www.postgresql.org/docs/release/15.8/").

### PostgreSQL version 15.8-R2 on Amazon RDS

PostgreSQL version 15.8-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 15.8 release](https://www.postgresql.org/docs/release/15.8/ "https://www.postgresql.org/docs/release/15.8/").

### PostgreSQL version 15.8 on Amazon RDS

PostgreSQL version 15.8 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.8 release](https://www.postgresql.org/docs/release/15.8/ "https://www.postgresql.org/docs/release/15.8/").

**New features and enhancements**

- [Delegated extension role](../UserGuide/RDS_delegated_ext.md "../UserGuide/RDS_delegated_ext.md") was added.

This version also includes the following extension updates:

- The `hypopg` extension was updated to 1.4.1.
- The `mysql_fdw` extension was updated to 2.9.2.
- The `orafce` extension was updated to 4.10.3.
- The `pg_cron` extension was updated to 1.6.3.
- The `pgTAP` extension was updated to 1.3.3.
- The `pgvector` extension was updated to 0.7.3.
- The `rdkit` extension was updated to 4.5.0 (Release 2024_03_5).
- The `wal2json` extension was updated to 2.6.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.7-R4 on

Amazon RDS

PostgreSQL version 15.7-R4 is now available on Amazon RDS. This release contains fixes for
[CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 15.7](https://www.postgresql.org/docs/release/15.7/ "https://www.postgresql.org/docs/release/15.7/").

### PostgreSQL version 15.7-R3 on Amazon RDS

PostgreSQL version 15.7-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 15.7 release](https://www.postgresql.org/docs/release/15.7/ "https://www.postgresql.org/docs/release/15.7/").

### PostgreSQL version 15.7-R2 on Amazon RDS

PostgreSQL version 15.7-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the [PostgreSQL 15.7 release](https://www.postgresql.org/docs/release/15.7/ "https://www.postgresql.org/docs/release/15.7/").

**New features and enhancements**

- Includes support for four new crates in PL/Rust, including:
  - `regex`
  - `serde`
  - `serde_json`
  - `url`

- Fixed a security issue in `pg_repack`
- Fixed a performance issue in `pgvector` for index creation on halfvec data type
- Fixed a bug in `aws_s3` causing import queries to occasionally get stuck and fail to terminate

### PostgreSQL version 15.7 on Amazon RDS

PostgreSQL version 15.7 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.7 release](https://www.postgresql.org/docs/release/15.7/ "https://www.postgresql.org/docs/release/15.7/").

**New features and enhancements**

- The blue/green deployment switchover won’t be blocked by the `REFRESH MATERIALIZED
VIEW` statement.
- Fixed the permission denial for the `CREATE DATABASE WITH OWNER`
  statement.
- Upgraded the `aws_s3` extension to version 1.2 to support the export to S3
  with the KMS customer managed key.
- Fixed a pgvector compatibility issue with some of the previous generations of DB
  instances, such as m4.

This version also includes the following extension updates:

- The `aws_s3` extension was updated to 1.2.
- The `orafce` extension was updated to 4.9.4.
- The `pg_hint_plan` extension was updated to 1.5.1.
- The `pg_partman` extension was updated to 5.1.0.
- The `pgvector` extension was updated to 0.7.0.
- The `postgis` extension was updated to 3.4.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.6-R3 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.6-R3 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.6 release](https://www.postgresql.org/docs/release/15.6/ "https://www.postgresql.org/docs/release/15.6/").

**New features and enhancements**

- Fixed a security issue in `pg_repack`

### PostgreSQL version 15.6-R2 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.6-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.6 release](https://www.postgresql.org/docs/release/15.6/ "https://www.postgresql.org/docs/release/15.6/").

**New features and enhancements**.

- Fixed a bug allowing the querying of the security invoker views as an unprivileged user.
- Fixed a bug preventing upgrades to `PostGIS` version 3.4.1.
- Fixed an error with the `aws_s3` extension when the Region was not provided.

**This version also includes the following extension changes:**

- The `pg_partman` extension was updated to version 5.0.1.
- The `pg_tle` extension was updated to version 1.4.0.
- The `pgactive` extension was updated to version 2.1.3.
- The `pgtap` extension was updated to version 1.3.2.
- The `pgvector` extension was updated to version 0.6.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.6 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.6 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.6 release](https://www.postgresql.org/docs/release/15.6/ "https://www.postgresql.org/docs/release/15.6/").

###### New features and enhancements

- Fixed the multisecond latency on the `aws_lambda` calls
- Fixed a bug preventing the termination of autovacuum

This version includes the following changes:

- The `orafce` extension was updated to version 4.9.0.
- The `pgactive` extension was updated to version 2.1.2.
- The `pgvector` extension was updated to 0.6.0.
- The `plv8` extension was updated to 3.1.10.
- The `PostGIS` extension was updated to 3.4.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.5-R2 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.5-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.5 release](https://www.postgresql.org/docs/release/15.5/ "https://www.postgresql.org/docs/release/15.5/").

###### New features and enhancements

- Fixed a crash in `CatalogCacheComputeHashValue` with `dblink_connect` due to a `Null` or `invalid` connection.
- Backported run_as_owner to RPG 15:
  - Backported a security fix for the logical replication apply worker that allows regular table owners to obtain privilege escalation to the subscription owner (an rds_superuser).
    The logical apply worker mitigates the risk by temporarily switching the role from the subscription owner to the table owner during logical apply.

  In the cases of potential security breaches, the fix will break your existing logical replication if any table in the subscription is owned by a regular user, and there are
  security-restricted operations attached to the table via triggers or default expressions. We recommend that you carefully examine the operations attached to the table
  if you notice the logical replication is broken after the upgrade. If all of the operations are as expected and you wish to revert the behavior of the logical replication so your application
  can continue, you can do so by setting the new parameter `rds.run_logical_replication_as_subscription_owner` to true. Be aware that by doing so your logical replication will be
  vulnerable to the aforementioned security risk again.

- Added `rds.run_logical_replication_as_subscription_owner` to the Amazon RDS parameter group.
- Supported the AWS SDK version of the `aws_s3` extension.
- Fixed the overflow in the `pg_transport` extension.
- Removed the unsupported shared libraries from the engine binary.

This version includes the following changes:

- The `plrust` extension was updated to version 1.2.7.
- The `plv8` extension was updated to version 3.1.9.

### PostgreSQL version 15.5 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.5 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.5 release](https://www.postgresql.org/docs/release/15.5/ "https://www.postgresql.org/docs/release/15.5/").

###### New features and enhancements

- Fixed a bug where `pg_database_size()` with an invalid OID causes a crash.
- Added support for the `rds.enable_pgactive` parameter in rdsutils to avoid the warning message.
- Exposed RDKit guc param `rdkit.morgan_fp_size`.
- Fixed the bug where setting `TABLESPACE` with `DEFAULT` option in `CREATE` or `ALTER DATABASE` fails.

This version includes the following changes:

- The `h3-pg` extension was updated to version 4.1.3.
- The `hll` extension was updated to version 2.18.
- The `oracle_fdw` extension was updated to version 2.6.0.
- The `orafce` extension was updated to version 4.6.1.
- The `pg_cron` extension was updated to version 1.6.1.
- The `pg_partman` extension was updated to version 5.0.0.
- The `pg_proctab` extension was updated to version 0.0.10.
- The `pgactive` extension was updated to version 2.1.1.
- The `pgtap` extension was updated to version 1.3.1.
- The `plprofiler` extension was updated to version 4.2.4.
- The `plrust` extension was updated to version 1.2.6.
- The `PostGIS` extension was updated to version 3.4.0.
- The `rdkit` extension was updated to version 4.4.0.

### PostgreSQL version 15.4-R3 on

Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.4-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 15.4
release](https://www.postgresql.org/docs/release/15.4/ "https://www.postgresql.org/docs/release/15.4/").

This version includes the following changes:

- Bug and security fixes for pgactive.
- The `pgvector` extension was updated to version 0.5.1.

### PostgreSQL version 15.4-R2 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.4-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.4 release](https://www.postgresql.org/docs/release/15.4/ "https://www.postgresql.org/docs/release/15.4/").

###### New features and enhancements

- Fixed a bug preventing database owners without the `rds_superuser` role from being able to create tables in the public schema.
- The `pgactive` extension was added.
- A new `rds.cte_materialize_mode` parameter was introduced which controls the materialization behavior of the query of a `WITH` clause,
  also known as a Common Table Expression. See [`WITH` Queries](https://www.postgresql.org/docs/current/queries-with.html "https://www.postgresql.org/docs/current/queries-with.html") for more information.
  The parameter values include the following:
  - _default_: The `WITH` clause will be treated using the engine's default behavior.
  - _always_: The full output of the query in the `WITH` clause will be materialized and the output reused in the outer query.
  - _never_: The query in the `WITH` clause will be inlined with the outer query if possible. This parameter will also override the
    `MATERIALIZED` and `NOT MATERIALIZED` keywords supplied to the `WITH` clause.

This version also includes the following changes:

- The `mysql_fdw` extension was updated to version 2.9.1.
- The `pgvector` extension was updated to version 0.5.0.
- The `plrust` extension was updated to version 1.2.5.
- The `plv8` extension was updated to version 3.1.8.
- The `rdkit` extension was updated to version 4.3.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.4 on Amazon RDS (This version has reached the end of standard support.)

PostgreSQL version 15.4 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.4 release](https://www.postgresql.org/docs/release/15.4/ "https://www.postgresql.org/docs/release/15.4/").

###### New features and enhancements

- Fixed a bug preventing users with the `rds_superuser` role from creating schemas in databases owned by other users.
- Users with the `rds_superuser` role can now access toast tables in the `pg_toast schema` that are owned by other users.
- Fixed an issue where `ALTER TABLE` took a ShareLock and may cause deadlocks.

This version also includes the following changes:

- The `hypopg` extension was updated to version 1.4.0.
- The `orafce` extension was updated to version 4.3.0.
- The `pg_tle` extension was updated to version 1.1.1.
- The `pglogical` extension was updated to version 2.4.3.
- The `plrust` extension was updated to version 1.2.3.
- The `PostGIS` extension was updated to version 3.3.3.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.3-R2 on Amazon RDS (Deprecated)

PostgreSQL version 15.3-R2 is now available on Amazon RDS. This release contains logical
replication for Multi-AZ DB clusters, improved `plrust` performance, and an
update to `pgvector`.

###### New features and enhancements

- Improves the performance of `plrust`
- Fixed a Patroni 2.1.7 restart issue and instead enables replication slot from the
  disk

This version also includes the following changes:

- The `pgvector` extension was updated to version 0.4.4.
- The `plrust` extension was updated to version 1.1.3.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.3 on Amazon RDS (Deprecated)

PostgreSQL version 15.3 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.3
release](https://www.postgresql.org/docs/release/15.3/ "https://www.postgresql.org/docs/release/15.3/").

###### New features and enhancements

- Includes changes to allow `rds-superuser` to run the
  `pg_stat_reset_slru` function
- Fixed a security issue involving `rds_sec_override` which wasn't reset
  after the intended usage, allowing unauthorized access to restricted tables
- Added the `hypopg` extension at version 1.3.1
- You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in
  order to establish logical replication connection between the source and the
  restored target database. You can then use logical replication to continuously
  stream the newer data recorded after the LSN and synchronize the changes from
  publisher to subscriber. Specifically, it allows the customer to create a logical
  slot on a source RDS database, take a snapshot, restore the snapshot to a new RDS
  instance (target), and use the value of logical_seed_lsn() from the target instance
  to advance the logical slot on the source instance in order to subscribe the target
  to the source.

This version also includes the following changes:

- `compat-collation-for-glibc` was updated to version 1.8.
- `libgeos` was updated to version 3.11.2.
- The `pg_cron` extension was updated to version 1.5.2.
- The `pg_partman` extension was updated to version 4.7.3.
- The `pg_tle` extension was updated to version 1.0.4.
- The `plrust` extension was updated to version 1.1.1.
- The `plv8` extension was updated to version 3.1.6.
- The `PostGIS` extension was updated to version 3.3.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.2-R2 on Amazon RDS (Deprecated)

PostgreSQL version 15.2-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 15.2 release](https://www.postgresql.org/docs/release/15.2/ "https://www.postgresql.org/docs/release/15.2/").

###### New extensions

- The `pgvector` extension was added.
- The `plrust` extension was added.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

### PostgreSQL version 15.2 on Amazon RDS (Deprecated)

PostgreSQL version 15.2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 15.2
release](https://www.postgresql.org/docs/release/15.2/ "https://www.postgresql.org/docs/release/15.2/").

###### New features and enhancements

- The archive library `rds_archive` is now used for archiving WAL files
  instead of `archive_command`.
- The `lz4` and `zstd` WAL compression methods are now
  supported.
- By default, the `default_toast_compression` DB instance parameter is
  set to `lz4`.

###### New extensions

- The `pg_walinspect` extension version 1.0 was added.

This version also includes the following changes:

- The `btree_gist` extension was updated to version 1.7.
- The `hll` extension was updated to version 2.17.
- The `mysql_fdw` extension was updated to version 2.9.0.
- The `pageinspect` extension was updated to version 1.11.
- The `pg_hint_plan` extension was updated to version 1.5.0.
- The `pg_repack` extension was updated to version 1.4.8.
- The `pg_stat_statements` extension was updated to version 1.10.
- The `pgaudit` extension was updated to version 1.7.0.
- The `pglogical` extension was updated to version 2.4.2.
- The `pgrouting` extension was updated to version 3.4.1.
- The `pllcoffee` extension was updated to version 3.1.4.
- The `plls` extensionwas updated to version 3.1.4.
- The `plprofiler` extension was updated to version 4.2.1.
- The `plv8` extension was updated to version 3.1.4.
- The `PostGIS` extension was updated to version 3.3.2.
- The `tds_fdw` extension was updated to version 2.0.3.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
15](postgresql-extensions.md#postgresql-extensions-15x "postgresql-extensions.md#postgresql-extensions-15x").

## PostgreSQL 14 versions

###### Minor versions

- [PostgreSQL version 14.19-R2 on
  Amazon RDS](#postgresql-versions-version1419R2 "#postgresql-versions-version1419R2")
- [PostgreSQL version 14.19 on Amazon RDS](#postgresql-versions-version1419 "#postgresql-versions-version1419")
- [PostgreSQL version 14.18-R2 on Amazon RDS](#postgresql-versions-version1418 "#postgresql-versions-version1418")
- [PostgreSQL version 14.18 on Amazon RDS](#postgresql-versions-version1418R1 "#postgresql-versions-version1418R1")
- [PostgreSQL version 14.17-R2 on Amazon RDS](#postgresql-versions-version1417R2 "#postgresql-versions-version1417R2")
- [PostgreSQL version 14.17 on Amazon RDS](#postgresql-versions-version1417 "#postgresql-versions-version1417")
- [PostgreSQL version 14.16 on Amazon RDS](#postgresql-versions-version1416R1 "#postgresql-versions-version1416R1")
- [PostgreSQL version 14.15-R2 on Amazon RDS](#postgresql-versions-version1415R2 "#postgresql-versions-version1415R2")
- [PostgreSQL version 14.15 on Amazon RDS](#postgresql-versions-version1415 "#postgresql-versions-version1415")
- [PostgreSQL version 14.14 on Amazon RDS](#postgresql-versions-version1414 "#postgresql-versions-version1414")
- [PostgreSQL version 14.13-R3 on
  Amazon RDS](#postgresql-versions-version1413R3 "#postgresql-versions-version1413R3")
- [PostgreSQL version 14.13-R2 on Amazon RDS](#postgresql-versions-version1413R2 "#postgresql-versions-version1413R2")
- [PostgreSQL version 14.13 on Amazon RDS](#postgresql-versions-version1413 "#postgresql-versions-version1413")
- [PostgreSQL version 14.12-R4 on
  Amazon RDS](#postgresql-versions-version1412R4 "#postgresql-versions-version1412R4")
- [PostgreSQL version 14.12-R3 on
  Amazon RDS](#postgresql-versions-version1412R3 "#postgresql-versions-version1412R3")
- [PostgreSQL version 14.12-R2 on Amazon RDS](#postgresql-versions-version1412-R2 "#postgresql-versions-version1412-R2")
- [PostgreSQL version 14.12 on Amazon RDS](#postgresql-versions-version1412 "#postgresql-versions-version1412")
- [PostgreSQL version 14.11-R4 on Amazon RDS](#postgresql-versions-version1411R4 "#postgresql-versions-version1411R4")
- [PostgreSQL version 14.11-R3 on Amazon RDS](#postgresql-versions-version1411R3 "#postgresql-versions-version1411R3")
- [PostgreSQL version 14.11-R2 on Amazon RDS](#postgresql-versions-version1411R2 "#postgresql-versions-version1411R2")
- [PostgreSQL version 14.11 on Amazon RDS](#postgresql-versions-version1411 "#postgresql-versions-version1411")
- [PostgreSQL version 14.10-R2 on Amazon RDS](#postgresql-versions-version1410R2 "#postgresql-versions-version1410R2")
- [PostgreSQL version 14.10 on Amazon RDS](#postgresql-versions-version1410 "#postgresql-versions-version1410")
- [PostgreSQL version 14.9-R2 on Amazon RDS](#postgresql-versions-version149R2 "#postgresql-versions-version149R2")
- [PostgreSQL version 14.9 on Amazon RDS](#postgresql-versions-version149 "#postgresql-versions-version149")
- [PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version148R2 "#postgresql-versions-version148R2")
- [PostgreSQL version 14.8 on Amazon RDS
  (Deprecated)](#postgresql-versions-version148 "#postgresql-versions-version148")
- [PostgreSQL version 14.7 on Amazon RDS (Deprecated)](#postgresql-versions-version147 "#postgresql-versions-version147")
- [PostgreSQL version 14.6 on Amazon RDS (Deprecated)](#postgresql-versions-version146 "#postgresql-versions-version146")
- [PostgreSQL version 14.5 on Amazon RDS (Deprecated)](#postgresql-versions-version145 "#postgresql-versions-version145")
- [PostgreSQL version 14.4 on Amazon RDS (Deprecated)](#postgresql-versions-version144 "#postgresql-versions-version144")
- [PostgreSQL version 14.3 on Amazon RDS (Deprecated)](#postgresql-versions-version143 "#postgresql-versions-version143")
- [PostgreSQL version 14.2 on Amazon RDS (Deprecated)](#postgresql-versions-version142 "#postgresql-versions-version142")
- [PostgreSQL version 14.1 on Amazon RDS (Deprecated)](#postgresql-versions-version141 "#postgresql-versions-version141")

### PostgreSQL version 14.19-R2 on

Amazon RDS

PostgreSQL version 14.19-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 14.19](https://www.postgresql.org/docs/release/14.19/ "https://www.postgresql.org/docs/release/14.19/").

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 14.19 on Amazon RDS

PostgreSQL version 14.19 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.19 release](https://www.postgresql.org/docs/release/14.19/ "https://www.postgresql.org/docs/release/14.19/").

**General enhancements**

- Grant rds_superuser access to pg_wal_pause / pg_wal_replay functions to perform logical
  upgrades and verification/validation.
- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.2.
- The `oracle_fdw` extension was updated to version 2.8.0.
- The `pgactive` extension was updated to version 2.1.5.

### PostgreSQL version 14.18-R2 on Amazon RDS

PostgreSQL version 14.18-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
14.19](https://www.postgresql.org/docs/release/14.19/ "https://www.postgresql.org/docs/release/14.19/").

**General enhancements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 14.18 on Amazon RDS

PostgreSQL version 14.18 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 14.18 release](https://www.postgresql.org/docs/release/14.18/ "https://www.postgresql.org/docs/release/14.18/").

**General enhancements**

- Fixed for the `address_standardizer_data_us` extension issue regarding ALTER
  EXTENSION UPDATE failure.
- Changed the Oracle client library version on x86 to 19.26.0.0.0.
- Fixed the `pgactive` extension unable to upgrade issue due to incorrect
  extension upgrade scripts which causes replication to break after engine upgrade.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.1.
- The `pglogical` extension was updated to version 2.4.5.
- The `PgAudit` extension was updated to version 1.6.3.
- The `RDKit` extension was updated to version 2024_09_6.

### PostgreSQL version 14.17-R2 on Amazon RDS

PostgreSQL version 14.17-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
14.17](https://www.postgresql.org/docs/release/14.17/ "https://www.postgresql.org/docs/release/14.17/").

**Fixes and improvements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 14.17 on Amazon RDS

PostgreSQL version 14.17 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL
announced in the [PostgreSQL 14.17 release](https://www.postgresql.org/docs/release/14.17/ "https://www.postgresql.org/docs/release/14.17/").

### PostgreSQL version 14.16 on Amazon RDS

PostgreSQL version 14.16 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.16 release](https://www.postgresql.org/docs/release/14.16/ "https://www.postgresql.org/docs/release/14.16/").

**New features and enhancements**.

- In Blue/Green deployments, creating or modifying temporary objects is no longer classified as restricted DDL.
- Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
- Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, see
  [RUSTSEC-2024-0421](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html").
- Applied Promise.any error allocation fix for V8 9.7.37, PLV8 3.1.10.

**This version also includes the following extension changes:**.

- The `rds_tools` extension was updated to 1.9.
- The `orafce` extension was updated to 4.14.0.
- The `pg_cron` extension was updated to 1.6.5.
- The `rdkit` extension was updated to 2024_09_3.
- The `pg_active` extension was updated to 2.1.4.
- The `pg_partman` extension was updated to 5.2.4.
- The `prefix` extension was updated to 1.2.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.15-R2 on Amazon RDS

PostgreSQL version 14.15-R2 is now available on Amazon RDS. This release contains fix for PLV8 [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in
[PostgreSQL 14.15](https://www.postgresql.org/docs/release/14.15/ "https://www.postgresql.org/docs/release/14.15/").

### PostgreSQL version 14.15 on Amazon RDS

PostgreSQL version 14.15 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 14.15 release](https://www.postgresql.org/docs/release/14.15/ "https://www.postgresql.org/docs/release/14.15/").

### PostgreSQL version 14.14 on Amazon RDS

PostgreSQL version 14.14 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 14.14](https://www.postgresql.org/docs/release/14.14/ "https://www.postgresql.org/docs/release/14.14/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is granted
  to Amazon RDS administrative users. The number of reserved connection slots is determined by the
  `rds.rds_reserved_connections` parameter . You may need to adjust the value of
  the `max_connections` parameter to account for the number of Amazon RDS reserved
  connection slots.

The `rds_reserved` role is a new predefined role created by
Amazon RDS. Predefined roles and their privileges can't be changed. You can't drop, rename, or
modify privileges for these predefined roles. Attempting to modify a predefined role results
in an error.

- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in Blue/Green
  replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.
- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

###### Updated features

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.13.4.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_hint_plan` extension was updated to version 1.4.3
- The `pgvector` extension was updated to version 0.8.0.
- The `plprofiler` extension was updated to version 4.2.5.
- The `PostGIS` extension was updated to version 3.4.3.
- The `rdkit` extension was updated to version 4.6.1.
- The `rds_tools` extension was updated to version 1.7.
- The `tds_fdw` extension was updated to version 2.0.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.13-R3 on

Amazon RDS

PostgreSQL version 14.13-R3 is now available on Amazon RDS. This release contains fixes for
[CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 14.13](https://www.postgresql.org/docs/release/14.13/ "https://www.postgresql.org/docs/release/14.13/").

### PostgreSQL version 14.13-R2 on Amazon RDS

PostgreSQL version 14.13-R2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.13 release](https://www.postgresql.org/docs/release/14.13/ "https://www.postgresql.org/docs/release/14.13/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 14.13 on Amazon RDS

PostgreSQL version 14.13 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.13 release](https://www.postgresql.org/docs/release/14.13/ "https://www.postgresql.org/docs/release/14.13/").

**New features and enhancements**

- [Delegated extension role](../UserGuide/RDS_delegated_ext.md "../UserGuide/RDS_delegated_ext.md") was added.

This version also includes the following extension updates:

- The `hypopg` extension was updated to 1.4.1.
- The `mysql_fdw` extension was updated to 2.9.2.
- The `orafce` extension was updated to 4.10.3.
- The `pg_cron` extension was updated to 1.6.3.
- The `pgTAP` extension was updated to 1.3.3.
- The `pgvector` extension was updated to 0.7.3.
- The `rdkit` extension was updated to 4.5.0 (Release 2024_03_5).
- The `wal2json` extension was updated to 2.6.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.12-R4 on

Amazon RDS

PostgreSQL version 14.12-R4 is now available on Amazon RDS. This release contains fixes for
[CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 14.12](https://www.postgresql.org/docs/release/14.12/ "https://www.postgresql.org/docs/release/14.12/").

### PostgreSQL version 14.12-R3 on

Amazon RDS

PostgreSQL version 14.12-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 14.12 release](https://www.postgresql.org/docs/release/14.12/ "https://www.postgresql.org/docs/release/14.12/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 14.12-R2 on Amazon RDS

PostgreSQL version 14.12-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the [PostgreSQL 14.12 release](https://www.postgresql.org/docs/release/14.12/ "https://www.postgresql.org/docs/release/14.12/").

**New features and enhancements**

- Includes support for four new crates in PL/Rust, including:
  - `regex`
  - `serde`
  - `serde_json`
  - `url`

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`
- Fixed a performance issue in `pgvector` for index creation on halfvec data type
- Fixed a bug in `aws_s3` causing import queries to occasionally get stuck and fail to terminate

**This version also includes the following extension changes:**.

- The `plv8` extension was updated to 3.1.10.

### PostgreSQL version 14.12 on Amazon RDS

PostgreSQL version 14.12 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.12 release](https://www.postgresql.org/docs/release/14.12/ "https://www.postgresql.org/docs/release/14.12/").

**New features and enhancements**

- The blue/green deployment switchover won’t be blocked by the `REFRESH MATERIALIZED
VIEW` statement.
- Fixed the permission denial for the `CREATE DATABASE WITH OWNER`
  statement.
- Upgraded the `aws_s3` extension to version 1.2 to support the export to S3
  with the KMS customer managed key.
- Fixed a pgvector compatibility issue with some of the previous generations of DB
  instances, such as m4.

This version also includes the following extension updates:

- The `aws_s3` extension was updated to 1.2.
- The `orafce` extension was updated to 4.9.4.
- The `pg_hint_plan` extension was updated to 1.4.2.
- The `pg_partman` extension was updated to 5.1.0.
- The `pgvector` extension was updated to 0.7.0.
- The `postgis` extension was updated to 3.4.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.11-R4 on Amazon RDS

PostgreSQL version 14.11-R4 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 14.11 release](https://www.postgresql.org/docs/release/14.11/ "https://www.postgresql.org/docs/release/14.11/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 14.11-R3 on Amazon RDS

PostgreSQL version 14.11-R3 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.11 release](https://www.postgresql.org/docs/release/14.11/ "https://www.postgresql.org/docs/release/14.11/").

**New features and enhancements**

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`

**This version also includes the following extension change:**

- The `plv8` extension was updated to 3.1.10.

### PostgreSQL version 14.11-R2 on Amazon RDS

PostgreSQL version 14.11-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.11 release](https://www.postgresql.org/docs/release/14.11/ "https://www.postgresql.org/docs/release/14.11/").

**New features and enhancements**.

- Fixed a bug preventing upgrades to `PostGIS` version 3.4.1.
- Fixed an error with the `aws_s3` extension when the Region was not provided.

**This version also includes the following extension changes:**

- The `pg_partman` extension was updated to version 5.0.1.
- The `pg_tle` extension was updated to version 1.4.0.
- The `pgactive` extension was updated to version 2.1.3.
- The `pgtap` extension was updated to version 1.3.2.
- The `pgvector` extension was updated to version 0.6.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.11 on Amazon RDS

PostgreSQL version 14.11 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 14.11 release.](https://www.postgresql.org/docs/release/14.11/ "https://www.postgresql.org/docs/release/14.11/").

###### New features and enhancements

- Fixed the multisecond latency on the `aws_lambda` calls
- Fixed a bug preventing the termination of autovacuum

This version includes the following changes:

- The `orafce` extension was updated to version 4.9.0.
- The `pg_cron` extension was updated to version 1.6.2.
- The `pgactive` extension was updated to version 2.1.2.
- The `pgvector` extension was updated to 0.6.0.
- The `PostGIS` extension was updated to 3.4.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.10-R2 on Amazon RDS

PostgreSQL version 14.10-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.10 release](https://www.postgresql.org/docs/release/14.10/ "https://www.postgresql.org/docs/release/14.10/").

###### New features and enhancements

- Fixed a crash in `CatalogCacheComputeHashValue` with `dblink_connect` due to a `Null` or `invalid` connection.
- Backported run_as_owner to RPG 14
  - Backported a security fix for the logical replication apply worker that allows regular table owners to obtain privilege escalation to the subscription owner (an rds_superuser).
    The logical apply worker mitigates the risk by temporarily switching the role from the subscription owner to the table owner during logical apply.

  In the cases of potential security breaches, the fix will break your existing logical replication if any table in the subscription is owned by a regular user, and there are
  security-restricted operations attached to the table via triggers or default expressions. We recommend that you carefully examine the operations attached to the table
  if you notice the logical replication is broken after the upgrade. If all of the operations are as expected and you wish to revert the behavior of the logical replication so your application
  can continue, you can do so by setting the new parameter `rds.run_logical_replication_as_subscription_owner` to true. Be aware that by doing so your logical replication will be
  vulnerable to the aforementioned security risk again.

- Added `rds.run_logical_replication_as_subscription_owner` to the Amazon RDS parameter group.
- Supported the AWS SDK version of the `aws_s3` extension.
- Fixed the overflow in the `pg_transport` extension.
- Removed the unsupported shared libraries from the engine binary.

This version includes the following change:

- The `plrust` extension was updated to version 1.2.7.

### PostgreSQL version 14.10 on Amazon RDS

PostgreSQL version 14.10 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.10 release](https://www.postgresql.org/docs/release/14.10/ "https://www.postgresql.org/docs/release/14.10/").

###### New features and enhancements

- Fixed a bug where `pg_database_size()` with an invalid OID causes a crash.
- Added support for the `rds.enable_pgactive` parameter in rdsutils to avoid the warning message.
- Exposed RDKit guc param `rdkit.morgan_fp_size`.
- Fixed the bug where setting `TABLESPACE` with `DEFAULT` option in `CREATE` or `ALTER DATABASE` fails.
- Added the `pgactive` extension.

This version includes the following changes:

- The `h3-pg` extension was updated to version 4.1.3.
- The `hll` extension was updated to version 2.18
- The `oracle_fdw` extension was updated to version 2.6.0.
- The `orafce` extension was updated to version 4.6.1.
- The `pg_cron` extension was updated to version 1.6.1.
- The `pg_partman` extension was updated to version 5.0.0.
- The `pg_proctab` extension was updated to version 0.0.10.
- The `pgtap` extension was updated to version 1.3.1.
- The `pgvector` extension was updated to version 0.5.1.
- The `plprofiler` extension was updated to version 4.2.4.
- The `plrust` extension was updated to version 1.2.6.
- The `PostGIS` extension was updated to version 3.4.0.
- The `rdkit` extension was updated to version 4.4.0.

### PostgreSQL version 14.9-R2 on Amazon RDS

PostgreSQL version 14.9-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.9 release](https://www.postgresql.org/docs/release/14.9/ "https://www.postgresql.org/docs/release/14.9/").

###### New features and enhancements

- A new `rds.cte_materialize_mode` parameter was introduced which controls the materialization behavior of the query of a `WITH` clause,
  also known as a Common Table Expression. See [`WITH` Queries](https://www.postgresql.org/docs/current/queries-with.html "https://www.postgresql.org/docs/current/queries-with.html") for more information.
  The parameter values include the following:
  - _default_: The `WITH` clause will be treated using the engine's default behavior.
  - _always_: The full output of the query in the `WITH` clause will be materialized and the output reused in the outer query.
  - _never_: The query in the `WITH` clause will be inlined with the outer query if possible. This parameter will also override the
    `MATERIALIZED` and `NOT MATERIALIZED` keywords supplied to the `WITH` clause.

This version also includes the following changes:

- The `pgvector` extension was updated to version 0.5.0.
- The `plrust` extension was updated to version 1.2.5.
- The `rdkit` extension was updated to version 4.3.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.9 on Amazon RDS

PostgreSQL version 14.9 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 14.9 release](https://www.postgresql.org/docs/release/14.9/ "https://www.postgresql.org/docs/release/14.9/").

###### New features and enhancements

- A bug was fixed preventing users with the `rds_superuser` role from creating schemas in databases owned by other users.
- Users with the `rds_superuser` role can now access toast tables in the `pg_toast schema` that are owned by other users.
- Fixed an issue where `ALTER TABLE` took a ShareLock and may cause deadlocks.

This version also includes the following changes:

- The `hypopg` extension was updated to version 1.4.0.
- The `orafce` extension was updated to version 4.3.0.
- The `pg_tle` extension was updated to version 1.1.1.
- The `pglogical` extension was updated to version 2.4.3.
- The `plrust` extension was added at version 1.2.3.
- The `PostGIS` extension was updated to version 3.3.3

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.8-R2 on Amazon RDS (Deprecated)

PostgreSQL version 14.8-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 14.8
release](https://www.postgresql.org/docs/release/14.8/ "https://www.postgresql.org/docs/release/14.8/").

###### New features and enhancements

- Fixed a Patroni 2.1.7 restart issue and instead enables replication slot from the
  disk

This version also includes the following change:

- The `pgvector` extension was updated to version 0.4.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.8 on Amazon RDS

(Deprecated)

PostgreSQL version 14.8 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.8
release](https://www.postgresql.org/docs/release/14.8/ "https://www.postgresql.org/docs/release/14.8/").

###### New features and enhancements

- Includes changes to allow rds-superuser to run the `pg_stat_reset_slru`
  function
- Fixed a security issue involving `rds_sec_override` which wasn't reset
  after the intended usage, allowing unauthorized access to restricted tables
- Added extension `hypopg` version 1.3.1
- Added extension `pgvector` version 0.4.1
- You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in
  order to establish logical replication connection between the source and the
  restored target database. You can then use logical replication to continuously
  stream the newer data recorded after the LSN and synchronize the changes from
  publisher to subscriber. Specifically, it allows the customer to create a logical
  slot on a source RDS database, take a snapshot, restore the snapshot to a new RDS
  instance (target), and use the value of logical_seed_lsn() from the target instance
  to advance the logical slot on the source instance in order to subscribe the target
  to the source.

This version also includes the following changes:

- `compat-collation-for-glibc` was updated to version 1.8.
- The `pg_cron` extension was updated to version 1.5.2.
- The `pg_tle` extension was updated to version 1.0.4.
- The `pglogical` extension was updated to version 2.4.2.
- The `PostGIS` extension was updated to version 3.3.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.7 on Amazon RDS (Deprecated)

PostgreSQL version 14.7 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.7
release](https://www.postgresql.org/docs/release/14.7/ "https://www.postgresql.org/docs/release/14.7/").

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.6 on Amazon RDS (Deprecated)

PostgreSQL version 14.6 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.6
release](https://www.postgresql.org/docs/release/14.6/ "https://www.postgresql.org/docs/release/14.6/").

###### New features and enhancements

- PostgreSQL version 14.6 added support for the `tcn` ("triggered change
  notification") extension which generates notification events on table changes via a
  trigger function called `triggered_change_notification`. The tcn
  extension is useful for applications using drivers which support asynchronous
  notification. This makes it possible to notify all clients if the contents of a
  table have been changed, enabling them to take appropriate action in near-real time,
  such as updating a table cache or information display.

However, such functionality should only be used with care as it makes all data
changes on the table available to all clients (including unprivileged users) through
the notification events when they listen on the tcn channel. It is the user’s
responsibility to avoid using tcn trigger on a table with sensitive data to avoid
information leakage.

This version includes the following changes:

- The `seg` extension version 1.4 was added.
- The `tcn` extension version 1.0 was added.
- The `orafce` extension was updated to version 3.24.
- The `pgaudit` extension was updated to version 1.6.2.
- The `pgtap` extension was updated to version 1.2.0.
- The `rdkit` extension was updated to version 4.2.0.
- The PostGIS dependency GDAL was updated to version 3.4.3.
- The `wal2json` extension was updated to version 2.5.
- The `aws_s3` extension was updated to version 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.5 on Amazon RDS (Deprecated)

PostgreSQL version 14.5 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.5
release](https://www.postgresql.org/docs/release/14.5/ "https://www.postgresql.org/docs/release/14.5/").

This version includes the following changes:

- The `PostGIS` extension was updated to version 3.1.7.
- The `pg_partman` extension was updated to version 4.6.2.
- The `pgrouting` extension was updated to version 3.2.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.4 on Amazon RDS (Deprecated)

PostgreSQL version 14.4 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.4
release](https://www.postgresql.org/docs/release/14.4/ "https://www.postgresql.org/docs/release/14.4/").

###### New features and enhancements

- While this release includes other fixes, a noteworthy fix included in this release
  is for `CREATE INDEX CONCURRENTLY` and `REINDEX CONCURRENTLY`
  that can potentially cause silent data corruption of indexes. Amazon RDS has made the fix
  for the index corruption available since the release of Amazon RDS for PostgreSQL 14.3. This
  release does not include any RDS specific changes or extension version
  updates.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.3 on Amazon RDS (Deprecated)

PostgreSQL version 14.3 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 14.3
release](https://www.postgresql.org/docs/release/14.3/ "https://www.postgresql.org/docs/release/14.3/").

###### New features and enhancements

- This release includes Amazon RDS collations designed to help with data migration from
  EBCDIC-based systems. For more information, see [RDS for PostgreSQL collations for EBCDIC and other mainframe
  migrations](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Collations.mainframe.migration "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.Collations.mainframe.migration").
- This release includes a fix that was made available in the [PostgreSQL out-of-cycle release June 16, 2022](https://www.postgresql.org/about/news/postgresql-14-out-of-cycle-release-coming-june-16-2022-2466/ "https://www.postgresql.org/about/news/postgresql-14-out-of-cycle-release-coming-june-16-2022-2466/") that resolves the
  `CREATE INDEX CONCURRENTLY` and `REINDEX CONCURRENTLY`
  issue. The issue affects all community PostgreSQL 14 versions prior to 14.4. For
  information about how to detect and remediate the issue, see [PostgreSQL 14 out-of-cycle release June 16, 2022](https://www.postgresql.org/about/news/postgresql-14-out-of-cycle-release-coming-june-16-2022-2466/ "https://www.postgresql.org/about/news/postgresql-14-out-of-cycle-release-coming-june-16-2022-2466/").
- Users with the `rds_superuser` role can now create roles for
  users.

This version also includes the following changes:

- The [pglogical](https://github.com/2ndQuadrant/pglogical "https://github.com/2ndQuadrant/pglogical")
  extension was updated to version 2.4.1.
- The [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan "https://github.com/ossc-db/pg_hint_plan")
  extension was updated to version 1.4.
- The [postgresql-hll](https://github.com/citusdata/postgresql-hll "https://github.com/citusdata/postgresql-hll")extension was updated to version 2.16.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.2 on Amazon RDS (Deprecated)

PostgreSQL version 14.2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 14.2](https://www.postgresql.org/docs/release/14.2/ "https://www.postgresql.org/docs/release/14.2/").

This version also includes the following changes:

- The [mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw "https://github.com/EnterpriseDB/mysql_fdw")
  extension version 2.7.0 is added. For more information, see [Working with MySQL databases by using the mysql_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-mysql-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-mysql-fdw").
- The [tds_fdw](https://github.com/tds-fdw/tds_fdw "https://github.com/tds-fdw/tds_fdw") extension
  version 2.0.2 is added. For more information, see [Working with SQL Server databases by using the tds_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-tds-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-tds-fdw") in the
  _Amazon RDS User Guide_.
- The [pgaudit](https://github.com/pgaudit/pgaudit/ "https://github.com/pgaudit/pgaudit/") extension is
  updated to 1.6.1. For information about using this extension with RDS for PostgreSQL, see
  [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit").
- The [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") (large
  objects) module is updated to version 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 14.1 on Amazon RDS (Deprecated)

PostgreSQL version 14.1 is now available on Amazon RDS. This release contains several
improvements that were announced in [PostgreSQL 14.1](https://www.postgresql.org/docs/14/release-14.html "https://www.postgresql.org/docs/14/release-14.html").

This version also includes the following changes:

- The [old_snapshot](https://www.postgresql.org/docs/14/oldsnapshot.html "https://www.postgresql.org/docs/14/oldsnapshot.html") extension 1.0 is added. If you set `old_snapshot_threshold` to a
  value, this extension lets you map transaction ID to a timestamp.
- The [amcheck](https://www.postgresql.org/docs/14/amcheck.html "https://www.postgresql.org/docs/14/amcheck.html")
  extension was updated to version 1.3.
- The [btree_gist](http://www.postgresql.org/docs/14/btree-gist.html "http://www.postgresql.org/docs/14/btree-gist.html") extension was updated to version 1.6.
- The [cube](http://www.postgresql.org/docs/14/cube.html "http://www.postgresql.org/docs/14/cube.html")
  extension was updated to version 1.5.
- The [hstore](http://www.postgresql.org/docs/14/hstore.html "http://www.postgresql.org/docs/14/hstore.html")
  extension was updated to version 1.8.
- The [intarray](http://www.postgresql.org/docs/14/intarray.html "http://www.postgresql.org/docs/14/intarray.html")
  extension was updated to version 1.5.
- The [pageinspect](https://www.postgresql.org/docs/current/pageinspect.html "https://www.postgresql.org/docs/current/pageinspect.html") extension was updated to version 1.9.
- The pg_cron extension was updated to version 1.4
- The pg_partman extension was updated to version
  4.6.0.
- The [pg_repack](http://reorg.github.io/pg_repack/ "http://reorg.github.io/pg_repack/") extension was
  updated to version 1.4.7.
- The [pg_stat_statements](http://www.postgresql.org/docs/14/pgstatstatements.html "http://www.postgresql.org/docs/14/pgstatstatements.html") extension was updated to version 1.9.
- The [pg_trgm](http://www.postgresql.org/docs/14/pgtrgm.html "http://www.postgresql.org/docs/14/pgtrgm.html")
  extension was updated to version 1.6.
- The [pgaudit](https://github.com/pgaudit/pgaudit/blob/master/README.md "https://github.com/pgaudit/pgaudit/blob/master/README.md") extension was updated to version 1.6.
- The [pgrouting](http://docs.pgrouting.org/latest/en/index.html "http://docs.pgrouting.org/latest/en/index.html")
  extension was updated to version 3.2.0.
- The [postgres_fdw](http://www.postgresql.org/docs/14/postgres-fdw.html "http://www.postgresql.org/docs/14/postgres-fdw.html") extension was updated to version 1.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

## PostgreSQL 13 versions

###### Minor versions

- [PostgreSQL version 13.22-R2 on
  Amazon RDS](#postgresql-versions-version1322R2 "#postgresql-versions-version1322R2")
- [PostgreSQL version 13.22 on Amazon RDS](#postgresql-versions-version1322 "#postgresql-versions-version1322")
- [PostgreSQL version 13.21-R2 on Amazon RDS](#postgresql-versions-version1321 "#postgresql-versions-version1321")
- [PostgreSQL version 13.21 on Amazon RDS](#postgresql-versions-version1321R1 "#postgresql-versions-version1321R1")
- [PostgreSQL version 13.20-R2 on Amazon RDS](#postgresql-versions-version1320R2 "#postgresql-versions-version1320R2")
- [PostgreSQL version 13.20 on Amazon RDS](#postgresql-versions-version1320 "#postgresql-versions-version1320")
- [PostgreSQL version 13.19 on Amazon RDS](#postgresql-versions-version1319R1 "#postgresql-versions-version1319R1")
- [PostgreSQL version 13.18-R2 on Amazon RDS](#postgresql-versions-version1318R2 "#postgresql-versions-version1318R2")
- [PostgreSQL version 13.18 on Amazon RDS](#postgresql-versions-version1318 "#postgresql-versions-version1318")
- [PostgreSQL version 13.17 on Amazon RDS](#postgresql-versions-version1317 "#postgresql-versions-version1317")
- [PostgreSQL version 13.16-R3 on
  Amazon RDS](#postgresql-versions-version1316R3 "#postgresql-versions-version1316R3")
- [PostgreSQL version 13.16-R2 on Amazon RDS](#postgresql-versions-version1316R2 "#postgresql-versions-version1316R2")
- [PostgreSQL version 13.16 on Amazon RDS](#postgresql-versions-version1316 "#postgresql-versions-version1316")
- [PostgreSQL version 13.15-R4 on Amazon RDS](#postgresql-versions-version1315R4 "#postgresql-versions-version1315R4")
- [PostgreSQL version 13.15-R3 on Amazon RDS](#postgresql-versions-version1315R3 "#postgresql-versions-version1315R3")
- [PostgreSQL version 13.15-R2 on Amazon RDS](#postgresql-versions-version1315R2 "#postgresql-versions-version1315R2")
- [PostgreSQL version 13.15 on Amazon RDS](#postgresql-versions-version1315 "#postgresql-versions-version1315")
- [PostgreSQL version 13.14-R4 on Amazon RDS](#postgresql-versions-version1314R4 "#postgresql-versions-version1314R4")
- [PostgreSQL version 13.14-R3 on Amazon RDS](#postgresql-versions-version1314R3 "#postgresql-versions-version1314R3")
- [PostgreSQL version 13.14-R2 on Amazon RDS](#postgresql-versions-version1314R2 "#postgresql-versions-version1314R2")
- [PostgreSQL version 13.14 on Amazon RDS](#postgresql-versions-version1314 "#postgresql-versions-version1314")
- [PostgreSQL version 13.13-R2 on Amazon RDS](#postgresql-versions-version1313R2 "#postgresql-versions-version1313R2")
- [PostgreSQL version 13.13 on Amazon RDS](#postgresql-versions-version1313 "#postgresql-versions-version1313")
- [PostgreSQL version 13.12-R2 on Amazon RDS](#postgresql-versions-version1312R2 "#postgresql-versions-version1312R2")
- [PostgreSQL version 13.12 on Amazon RDS](#postgresql-versions-version1312 "#postgresql-versions-version1312")
- [PostgreSQL version 13.11-R2 on Amazon RDS](#postgresql-versions-version1311R2 "#postgresql-versions-version1311R2")
- [PostgreSQL version 13.11 on Amazon RDS](#postgresql-versions-version1311 "#postgresql-versions-version1311")
- [PostgreSQL version 13.10 on Amazon RDS (Deprecated)](#postgresql-versions-version1310 "#postgresql-versions-version1310")
- [PostgreSQL version 13.9 on Amazon RDS (Deprecated)](#postgresql-versions-version139 "#postgresql-versions-version139")
- [PostgreSQL version 13.8 on Amazon RDS (Deprecated)](#postgresql-versions-version138 "#postgresql-versions-version138")
- [PostgreSQL version 13.7 on Amazon RDS (Deprecated)](#postgresql-versions-version137 "#postgresql-versions-version137")
- [PostgreSQL version 13.6 on Amazon RDS (Deprecated)](#postgresql-versions-version136 "#postgresql-versions-version136")
- [PostgreSQL version 13.5 on Amazon RDS (Deprecated)](#postgresql-versions-version135 "#postgresql-versions-version135")
- [PostgreSQL version 13.4 on Amazon RDS (Deprecated)](#postgresql-versions-version134 "#postgresql-versions-version134")
- [PostgreSQL version 13.3 on Amazon RDS (Deprecated)](#postgresql-versions-version133 "#postgresql-versions-version133")
- [PostgreSQL version 13.2 on Amazon RDS (Deprecated)](#postgresql-versions-version132 "#postgresql-versions-version132")
- [PostgreSQL version 13.1 on Amazon RDS (Deprecated)](#postgresql-versions-version131 "#postgresql-versions-version131")

### PostgreSQL version 13.22-R2 on

Amazon RDS

PostgreSQL version 13.22-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 13.22](https://www.postgresql.org/docs/release/13.22/ "https://www.postgresql.org/docs/release/13.22/").

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 13.22 on Amazon RDS

PostgreSQL version 13.22 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 13.22 release](https://www.postgresql.org/docs/release/13.22/ "https://www.postgresql.org/docs/release/13.22/").

**General enhancements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.2.
- The `oracle_fdw` extension was updated to version 2.8.0.
- The `pgactive` extension was updated to version 2.1.5.

### PostgreSQL version 13.21-R2 on Amazon RDS

PostgreSQL version 13.21-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.21
release](https://www.postgresql.org/docs/release/13.21/ "https://www.postgresql.org/docs/release/13.21/").

[CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for
PostgreSQL announced in [PostgreSQL 13.22](https://www.postgresql.org/docs/release/13.22/ "https://www.postgresql.org/docs/release/13.22/").

### PostgreSQL version 13.21 on Amazon RDS

PostgreSQL version 13.21 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.21 release](https://www.postgresql.org/docs/release/13.21/ "https://www.postgresql.org/docs/release/13.21/").

**General enhancements**

- Fixed for the `address_standardizer_data_us` extension issue regarding ALTER
  EXTENSION UPDATE failure.
- Changed the Oracle client library version on x86 to 19.26.0.0.0.
- Fixed the `pgactive` extension unable to upgrade issue due to incorrect
  extension upgrade scripts which causes replication to break after engine upgrade.

This version also includes the following extension changes:

- The `pg_repack` extension was updated to version 1.5.1.
- The `pglogical` extension was updated to version 2.4.5.
- The `PgAudit` extension was updated to version 1.5.3.

### PostgreSQL version 13.20-R2 on Amazon RDS

PostgreSQL version 13.20-R2 is now available on Amazon RDS. This release contains fix for [CVE-2025-8714](https://nvd.nist.gov/vuln/detail/CVE-2025-8714 "https://nvd.nist.gov/vuln/detail/CVE-2025-8714"), and [CVE-2025-8715](https://nvd.nist.gov/vuln/detail/CVE-2025-8715 "https://nvd.nist.gov/vuln/detail/CVE-2025-8715") for PostgreSQL
announced in [PostgreSQL
13.22](https://www.postgresql.org/docs/release/13.22/ "https://www.postgresql.org/docs/release/13.22/").

**Fixes and Improvements**

- Updated V8 engine to version 11.5.150.2 for the `plv8` extension
  3.1.10.

This version also includes the following extension changes:

- The `pgactive` extension was updated to version 2.1.6.

### PostgreSQL version 13.20 on Amazon RDS

PostgreSQL version 13.20 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced
in the [PostgreSQL 13.20 release](https://www.postgresql.org/docs/release/13.20/ "https://www.postgresql.org/docs/release/13.20/").

### PostgreSQL version 13.19 on Amazon RDS

PostgreSQL version 13.19 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.19 release](https://www.postgresql.org/docs/release/13.19/ "https://www.postgresql.org/docs/release/13.19/").

**New features and enhancements**.

- In Blue/Green deployments, creating or modifying temporary objects is no longer classified as restricted DDL.
- Resolved an issue where DVB returned duplicate rows during slow vacuum analysis.
- Resolved CVE RUSTSEC-2024-0421 by upgrading URL Rust crate to 2.5.4. For more information, see
  [RUSTSEC-2024-0421](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html").
- Applied Promise.any error allocation fix for V8 9.7.37, PLV8 3.1.10.

**This version also includes the following extension changes:**.

- The `rds_tools` extension was updated to 1.9.
- The `orafce` extension was updated to 4.14.0.
- The `pg_cron` extension was updated to 1.6.5.
- The `pg_active` extension was updated to 2.1.4.
- The `prefix` extension was updated to 1.2.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.18-R2 on Amazon RDS

PostgreSQL version 13.18-R2 is now available on Amazon RDS. This release contains fix for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in
[PostgreSQL 13.18](https://www.postgresql.org/docs/release/13.18/ "https://www.postgresql.org/docs/release/13.18/").

### PostgreSQL version 13.18 on Amazon RDS

PostgreSQL version 13.18 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.18 release](https://www.postgresql.org/docs/release/13.18/ "https://www.postgresql.org/docs/release/13.18/").

### PostgreSQL version 13.17 on Amazon RDS

PostgreSQL version 13.17 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 13.17 release](https://www.postgresql.org/docs/release/13.17/ "https://www.postgresql.org/docs/release/13.17/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is granted
  to Amazon RDS administrative users. The number of reserved connection slots is determined by the
  `rds.rds_reserved_connections` parameter . You may need to adjust the value of
  the `max_connections` parameter to account for the number of Amazon RDS reserved
  connection slots.

The `rds_reserved` role is a new predefined role created by Amazon RDS. Predefined
roles and their privileges can't be changed. You can't drop, rename, or modify privileges
for these predefined roles. Attempting to modify a predefined role results in an
error.

- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in Blue/Green
  replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.
- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

###### Updated features

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.13.4.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_hint_plan` extension was updated to version 1.3.10.
- The `pgvector` extension was updated to version 0.8.0.
- The `plprofiler` extension was updated to version 4.2.5.
- The `PostGIS` extension was updated to version 3.4.3.
- The `rds_tools` extension was updated to version 1.7.
- The `tds_fdw` extension was updated to version 2.0.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.16-R3 on

Amazon RDS

PostgreSQL version 13.16-R3 is now available on Amazon RDS. This release contains fixes for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and Rust [CVE RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html")
for PostgreSQL announced in [PostgreSQL 13.16](https://www.postgresql.org/docs/release/13.16/ "https://www.postgresql.org/docs/release/13.16/").

### PostgreSQL version 13.16-R2 on Amazon RDS

PostgreSQL version 13.16-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.16 release](https://www.postgresql.org/docs/release/13.16/ "https://www.postgresql.org/docs/release/13.16/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 13.16 on Amazon RDS

PostgreSQL version 13.16 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 13.16 release](https://www.postgresql.org/docs/release/13.16/ "https://www.postgresql.org/docs/release/13.16/").

**New features and enhancements**

- [Delegated extension role](../UserGuide/RDS_delegated_ext.md "../UserGuide/RDS_delegated_ext.md") was added.

This version also includes the following extension updates:

- The `hypopg` extension was updated to 1.4.1.
- The `mysql_fdw` extension was updated to 2.9.2.
- The `orafce` extension was updated to 4.10.3.
- The `pg_cron` extension was updated to 1.6.3.
- The `pgTAP` extension was updated to 1.3.3.
- The `pgvector` extension was updated to 0.7.3.
- The `wal2json` extension was updated to 2.6.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.15-R4 on Amazon RDS

PostgreSQL version 13.15-R4 is now available on Amazon RDS. This release contains fixed for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced
in [PostgreSQL 13.15](https://www.postgresql.org/docs/release/13.15/ "https://www.postgresql.org/docs/release/13.15/").

### PostgreSQL version 13.15-R3 on Amazon RDS

PostgreSQL version 13.15-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.15 release](https://www.postgresql.org/docs/release/13.15/ "https://www.postgresql.org/docs/release/13.15/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 13.15-R2 on Amazon RDS

PostgreSQL version 13.15-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the [PostgreSQL 13.15 release](https://www.postgresql.org/docs/release/13.15/ "https://www.postgresql.org/docs/release/13.15/").

**New features and enhancements**

- Includes support for four new crates in PL/Rust, including:
  - `regex`
  - `serde`
  - `serde_json`
  - `url`

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`
- Fixed a performance issue in `pgvector` for index creation on halfvec data type
- Fixed a bug in `aws_s3` causing import queries to occasionally get stuck and fail to terminate
- Fixed a performance issue in `aws_s3` and `aws_lambda`

**This version also includes the following extension change:**

- The `plv8` extension was updated to 3.1.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.15 on Amazon RDS

PostgreSQL version 13.15 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 13.15 release](https://www.postgresql.org/docs/release/13.15/ "https://www.postgresql.org/docs/release/13.15/").

**New features and enhancements**

- The blue/green deployment switchover won’t be blocked by the `REFRESH MATERIALIZED
VIEW` statement.
- Fixed the permission denial for the `CREATE DATABASE WITH OWNER`
  statement.
- Upgraded the `aws_s3` extension to version 1.2 to support the export to S3
  with the KMS customer managed key.
- Fixed a pgvector compatibility issue with some of the previous generations of DB
  instances, such as m4.

This version also includes the following extension updates:

- The `aws_s3` extension was updated to 1.2.
- The `orafce` extension was updated to 4.9.4.
- The `pg_hint_plan` extension was updated to 1.3.9.
- The `pgvector` extension was updated to 0.7.0.
- The `postgis` extension was updated to 3.4.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.14-R4 on Amazon RDS

PostgreSQL version 13.14-R4 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 13.14 release](https://www.postgresql.org/docs/release/13.14/ "https://www.postgresql.org/docs/release/13.14/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 13.14-R3 on Amazon RDS

PostgreSQL version 13.14-R3 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.14 release](https://www.postgresql.org/docs/release/13.14/ "https://www.postgresql.org/docs/release/13.14/").

**New features and enhancements**

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`

**This version also includes the following extension change:**

- The `plv8` extension was updated to 3.1.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.14-R2 on Amazon RDS

PostgreSQL version 13.14-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.14 release](https://www.postgresql.org/docs/release/13.14/ "https://www.postgresql.org/docs/release/13.14/").

**New features and enhancements**

- Fixed a bug preventing upgrades to `PostGIS` version 3.4.1.

**This version also includes the following extension changes:**

- The `pg_partman` extension was updated to version 4.5.1.
- The `pg_tle` extension was updated to version 1.4.0.
- The `pgactive` extension was updated to version 2.1.3.
- The `pgtap` extension was updated to version 1.3.2.
- The `pgvector` extension was updated to version 0.6.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.14 on Amazon RDS

PostgreSQL version 13.14 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 13.14 release.](https://www.postgresql.org/docs/release/13.14/ "https://www.postgresql.org/docs/release/13.14/").

###### New features and enhancements

- Fixed the multisecond latency on the `aws_lambda` calls
- Fixed a bug preventing the termination of autovacuum

This version includes the following changes:

- The `orafce` extension was updated to version 4.9.0.
- The `pg_cron` extension was updated to version 1.6.2.
- The `pgactive` extension was updated to version 2.1.2.
- The `pgvector` extension was updated to 0.6.0.
- The `PostGIS` extension was updated to 3.4.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.13-R2 on Amazon RDS

PostgreSQL version 13.13-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.13 release](https://www.postgresql.org/docs/release/13.13/ "https://www.postgresql.org/docs/release/13.13/").

###### New features and enhancements

- Fixed a crash in `CatalogCacheComputeHashValue` with `dblink_connect` due to a `Null` or `invalid` connection.
- Backported run_as_owner to RPG 13:
  - Backported a security fix for the logical replication apply worker that allows regular table owners to obtain privilege escalation to the subscription owner (an rds_superuser).
    The logical apply worker mitigates the risk by temporarily switching the role from the subscription owner to the table owner during logical apply.

  In the cases of potential security breaches, the fix will break your existing logical replication if any table in the subscription is owned by a regular user, and there are
  security-restricted operations attached to the table via triggers or default expressions. We recommend that you carefully examine the operations attached to the table
  if you notice the logical replication is broken after the upgrade. If all of the operations are as expected and you wish to revert the behavior of the logical replication so your application
  can continue, you can do so by setting the new parameter `rds.run_logical_replication_as_subscription_owner` to true. Be aware that by doing so your logical replication will be
  vulnerable to the aforementioned security risk again.

- Added `rds.run_logical_replication_as_subscription_owner` to the Amazon RDS parameter group.
- Fixed the overflow in the `pg_transport` extension.
- Removed the unsupported shared libraries from the engine binary.

This version includes the following change:

- The `plrust` extension was updated to version 1.2.7.

### PostgreSQL version 13.13 on Amazon RDS

PostgreSQL version 13.13 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.13 release](https://www.postgresql.org/docs/release/13.13/ "https://www.postgresql.org/docs/release/13.13/").

###### New features and enhancements

- Fixed a bug where `pg_database_size()` with an invalid OID causes a crash.
- Added support for the `rds.enable_pgactive` parameter in rdsutils to avoid the warning message.
- Exposed RDKit guc param `rdkit.morgan_fp_size`.
- Fixed the bug where setting `TABLESPACE` with `DEFAULT` option in `CREATE` or `ALTER DATABASE` fails.
- Added the `pgactive` extension.

This version includes the following changes:

- The `h3-pg` extension was updated to version 4.1.3.
- The `hll` extension was updated to version 2.18
- The `oracle_fdw` extension was updated to version 2.6.0.
- The `orafce` extension was updated to version 4.6.1.
- The `pg_cron` extension was updated to version 1.6.1.
- The `pg_proctab` extension was updated to version 0.0.10.
- The `pgtap` extension was updated to version 1.3.1.
- The `pgvector` extension was updated to version 0.5.1.
- The `plprofiler` extension was updated to version 4.2.4.
- The `plrust` extension was updated to version 1.2.6.
- The `PostGIS` extension was updated to version 3.4.0.

### PostgreSQL version 13.12-R2 on Amazon RDS

PostgreSQL version 13.12-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.12 release](https://www.postgresql.org/docs/release/13.12/ "https://www.postgresql.org/docs/release/13.12/").

This version includes the following change:

- The `pgvector` extension was updated to version 0.5.0.
- The `plrust` extension was updated to version 1.2.5.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.12 on Amazon RDS

PostgreSQL version 13.12 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.12 release](https://www.postgresql.org/docs/release/13.12/ "https://www.postgresql.org/docs/release/13.12/").

###### New features and enhancements

- A bug was fixed preventing users with the `rds_superuser` role from creating schemas in databases owned by other users.
- Users with the `rds_superuser` role can now access toast tables in the `pg_toast schema` that are owned by other users.
- Fixed an issue where `ALTER TABLE` took a ShareLock and may cause deadlocks.

This version also includes the following changes:

- `hypopg` was updated to 1.4.0
- `orafce` was updated to 4.3.0
- `pg_tle` was added at version 1.1.1
- `pglogical` was updated to 2.4.3
- `plrust` was added at version 1.2.3
- `PostGIS` was updated to 3.3.3

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.11-R2 on Amazon RDS

PostgreSQL version 13.11-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.11 release](https://www.postgresql.org/docs/release/13.11/ "https://www.postgresql.org/docs/release/13.11/").

This version also includes the following change:

- The `pgvector` extension was updated to version 0.4.4.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
14](postgresql-extensions.md#postgresql-extensions-14x "postgresql-extensions.md#postgresql-extensions-14x").

### PostgreSQL version 13.11 on Amazon RDS

PostgreSQL version 13.11 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.11 release](https://www.postgresql.org/docs/release/13.11/ "https://www.postgresql.org/docs/release/13.11/").

###### New features and enhancements

- Includes changes to allow rds-superuser to run the `pg_stat_reset_slru` function
- Fixed a security issue involving `rds_sec_override` which wasn't reset after the intended usage, allowing unauthorized
  access to restricted tables
- Added extension `hypopg` version 1.3.1
- Added extension `pgvector` version 0.4.1
- You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to establish logical replication
  connection between the source and the restored target database. You can then use logical replication to continuously stream the newer
  data recorded after the LSN and synchronize the changes from publisher to subscriber. Specifically, it allows the customer to create a
  logical slot on a source RDS database, take a snapshot, restore the snapshot to a new RDS instance (target), and use the value of
  logical_seed_lsn() from the target instance to advance the logical slot on the source instance in order to subscribe the target to
  the source.

This version also includes the following changes:

- `compat-collation-for-glibc` was updated to version 1.8
- `libcompat` was updated to version 1.8
- `pg_cron` was updated to version 1.5.2
- `pglogical` was updated to version 2.4.2
- `PostGIS` was updated to version 3.3.2

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.10 on Amazon RDS (Deprecated)

PostgreSQL version 13.10 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 13.10 release](https://www.postgresql.org/docs/release/13.10/ "https://www.postgresql.org/docs/release/13.10/").

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.9 on Amazon RDS (Deprecated)

PostgreSQL version 13.9 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 13.9
release](https://www.postgresql.org/docs/release/13.9/ "https://www.postgresql.org/docs/release/13.9/").

New features and enhancements

- PostgreSQL version 13.9 added support for the `tcn` ("triggered change
  notification") extension which generates notification events on table changes via a
  trigger function called `triggered_change_notification`. The tcn
  extension is useful for applications using drivers which support asynchronous
  notification. This makes it possible to notify all clients if the contents of a
  table have been changed, enabling them to take appropriate action in near-real time,
  such as updating a table cache or information display.

However, such functionality should only be used with care as it makes all data
changes on the table available to all clients (including unprivileged users) through
the notification events when they listen on the tcn channel. It is the user’s
responsibility to avoid using tcn trigger on a table with sensitive data to avoid
information leakage.

This version includes the following changes:

- The seg extension version 1.3 is added.
- The tcn extension version 1.0 is added.
- The orafce extension is updated to 3.24.
- The pgaudit extension is updated to 1.5.2.
- The pgtap extension is updated to 1.2.0.
- The PostGIS dependency GDAL is updated to 3.4.3.
- The PostGIS dependency PROJ is updated to 8.0.1.
- The wal2json extension is updated to 2.5.
- The aws_s3 extension is updated to 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.8 on Amazon RDS (Deprecated)

PostgreSQL version 13.8 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in
[PostgreSQL 13.8](https://www.postgresql.org/docs/release/13.8/ "https://www.postgresql.org/docs/release/13.8/").

This version includes the following changes:

- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to 3.1.7
- The [pgRouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html") extension is updated to 3.1.4

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.7 on Amazon RDS (Deprecated)

PostgreSQL version 13.7 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 13.7](https://www.postgresql.org/docs/release/13.7/ "https://www.postgresql.org/docs/release/13.7/").

This version also includes the following changes:

- The [pglogical](https://github.com/2ndQuadrant/pglogical "https://github.com/2ndQuadrant/pglogical")
  extension is updated to 2.4.1

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.6 on Amazon RDS (Deprecated)

PostgreSQL version 13.6 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.6](https://www.postgresql.org/docs/release/13.6/ "https://www.postgresql.org/docs/release/13.6/").

This version also includes the following changes:

- The [mysql_fdw](https://github.com/EnterpriseDB/mysql_fdw "https://github.com/EnterpriseDB/mysql_fdw")
  extension version 2.7.0 is added. For more information, see [Working with MySQL databases by using the mysql_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-mysql-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-mysql-fdw") in the
  _Amazon RDS User Guide_.
- The [tds_fdw](https://github.com/tds-fdw/tds_fdw "https://github.com/tds-fdw/tds_fdw") extension
  version 2.0.2 is added. For more information, see [Working with SQL Server databases by using the tds_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-tds-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-tds-fdw") in the
  _Amazon RDS User Guide_.
- The [pgaudit](https://github.com/pgaudit/pgaudit/ "https://github.com/pgaudit/pgaudit/") extension is
  updated to 1.5.1. For information about using this extension with RDS for PostgreSQL, see
  [Logging at the session and object level with the pgaudit extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit") in
  the _Amazon RDS User Guide_.
- The [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") (large
  objects) module is updated to version 1.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.5 on Amazon RDS (Deprecated)

PostgreSQL version 13.5 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.5](https://www.postgresql.org/docs/release/13.5/ "https://www.postgresql.org/docs/release/13.5/").

This version also includes the following change:

- The [pg_cron](https://github.com/citusdata/pg_cron "https://github.com/citusdata/pg_cron") extension
  is updated to 1.4.1

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.4 on Amazon RDS (Deprecated)

PostgreSQL version 13.4 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.4](https://www.postgresql.org/docs/release/13.4/ "https://www.postgresql.org/docs/release/13.4/").

This version also includes the following changes:

- The `flow_control` extension version 1.0 is added in this
  release.
- The [spi
  module](https://www.postgresql.org/docs/13/contrib-spi.html "https://www.postgresql.org/docs/13/contrib-spi.html") extensions refint, autoinc, inset_username, and moddatetime
  version 1.0 are added.
- The [pgrouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html")
  extension is updated to version 3.1.3.
- The `pglogical` extension is updated to version 2.4.0.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.1.4, along with the following
  related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.3 on Amazon RDS (Deprecated)

PostgreSQL version 13.3 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.3](https://www.postgresql.org/docs/release/13.3/ "https://www.postgresql.org/docs/release/13.3/").

This version also includes the following changes:

- The [oracle_fdw](https://github.com/laurenz/oracle_fdw "https://github.com/laurenz/oracle_fdw")
  extension version 2.3.0 is added. For more information, see [Working with Oracle databases by using the oracle_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-oracle-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-oracle-fdw") in the
  _Amazon RDS User Guide_.
- The [orafce](https://github.com/orafce/orafce "https://github.com/orafce/orafce") extension is
  updated to version 3.15.
- The [pg_cron](../UserGuide/PostgreSQL_pg_cron.md "../UserGuide/PostgreSQL_pg_cron.md")
  extension is updated to version 1.3.1.
- The [pg_partman](../UserGuide/PostgreSQL_Partitions.md "../UserGuide/PostgreSQL_Partitions.md")
  extension is updated to version 4.5.1.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.0.3, along with the following
  related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.2 on Amazon RDS (Deprecated)

PostgreSQL version 13.2 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.2](https://www.postgresql.org/docs/release/13.2/ "https://www.postgresql.org/docs/release/13.2/").

This version also added the following new extensions:

- The `aws_lambda` extension version 1.0. For more information, see
  [Invoking an AWS Lambda
  function from an RDS for PostgreSQL DB instance](../UserGuide/PostgreSQL-Lambda.md "../UserGuide/PostgreSQL-Lambda.md") in the
  _Amazon RDS User Guide_.
- The [pg_bigm](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html "https://pgbigm.osdn.jp/pg_bigm_en-1-2.html")
  extension version 1.2.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

### PostgreSQL version 13.1 on Amazon RDS (Deprecated)

PostgreSQL version 13.1 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [PostgreSQL 13.0](https://www.postgresql.org/docs/13/release-13.html "https://www.postgresql.org/docs/13/release-13.html") and
[PostgreSQL
13.1](https://www.postgresql.org/docs/13/release-13-1.html "https://www.postgresql.org/docs/13/release-13-1.html").

This version added:

- The `bool_plperl` extension version 1.0.
- The `rds_tools` extension version 1.0. For more information, see [Checking for users with non-SCRAM passwords](https://aws.amazon.com/blogs/database/scram-authentication-in-rds-for-postgresql-13/ "https://aws.amazon.com/blogs/database/scram-authentication-in-rds-for-postgresql-13/") .

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
13](postgresql-extensions.md#postgresql-extensions-13x "postgresql-extensions.md#postgresql-extensions-13x").

## PostgreSQL 12 versions (Some of these versions have reached the end of standard support or deprecated.)

###### Minor versions

- [PostgreSQL version 12.22-R2 on Amazon RDS (This
  version has reached the end of standard support.)](#postgresql-versions-version1222R2 "#postgresql-versions-version1222R2")
- [PostgreSQL version 12.22 on Amazon RDS (This
  version has reached the end of standard support.)](#postgresql-versions-version1222 "#postgresql-versions-version1222")
- [PostgreSQL version 12.21 on Amazon RDS (Deprecated)](#postgresql-versions-version1221 "#postgresql-versions-version1221")
- [PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated)](#postgresql-versions-version1220R3 "#postgresql-versions-version1220R3")
- [PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version1220R2 "#postgresql-versions-version1220R2")
- [PostgreSQL version 12.20 on Amazon RDS (Deprecated)](#postgresql-versions-version1220 "#postgresql-versions-version1220")
- [PostgreSQL version 12.19-R4 on Amazon RDS (Deprecated)](#postgresql-versions-version1219R4 "#postgresql-versions-version1219R4")
- [PostgreSQL version 12.19-R3 on Amazon RDS (Deprecated)](#postgresql-versions-version1219R3 "#postgresql-versions-version1219R3")
- [PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version1219R2 "#postgresql-versions-version1219R2")
- [PostgreSQL version 12.19 on Amazon RDS (Deprecated)](#postgresql-versions-version1219 "#postgresql-versions-version1219")
- [PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated)](#postgresql-versions-version1218R4 "#postgresql-versions-version1218R4")
- [PostgreSQL version 12.18-R3 on Amazon RDS (Deprecated)](#postgresql-versions-version1218R3 "#postgresql-versions-version1218R3")
- [PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version1218R2 "#postgresql-versions-version1218R2")
- [PostgreSQL version 12.18 on Amazon RDS (Deprecated)](#postgresql-versions-version1218 "#postgresql-versions-version1218")
- [PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version1217R2 "#postgresql-versions-version1217R2")
- [PostgreSQL version 12.17 on Amazon RDS (Deprecated)](#postgresql-versions-version1217 "#postgresql-versions-version1217")
- [PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated)](#postgresql-versions-version1216R2 "#postgresql-versions-version1216R2")
- [PostgreSQL version 12.16 on Amazon RDS (Deprecated)](#postgresql-versions-version1216 "#postgresql-versions-version1216")
- [PostgreSQL version 12.15 on Amazon RDS (Deprecated)](#postgresql-versions-version1215 "#postgresql-versions-version1215")
- [PostgreSQL version 12.14 on Amazon RDS (Deprecated)](#postgresql-versions-version1214 "#postgresql-versions-version1214")
- [PostgreSQL version 12.13 on Amazon RDS (Deprecated)](#postgresql-versions-version1213 "#postgresql-versions-version1213")
- [PostgreSQL version 12.12 on Amazon RDS (Deprecated)](#postgresql-versions-version1212 "#postgresql-versions-version1212")
- [PostgreSQL version 12.11 on Amazon RDS (Deprecated)](#postgresql-versions-version1211 "#postgresql-versions-version1211")
- [PostgreSQL version 12.10 on Amazon RDS (Deprecated)](#postgresql-versions-version1210 "#postgresql-versions-version1210")
- [PostgreSQL version 12.9 on Amazon RDS (Deprecated)](#postgresql-versions-version129 "#postgresql-versions-version129")
- [PostgreSQL version 12.8 on Amazon RDS (Deprecated)](#postgresql-versions-version128 "#postgresql-versions-version128")
- [PostgreSQL version 12.7 on Amazon RDS (Deprecated)](#postgresql-versions-version127 "#postgresql-versions-version127")
- [PostgreSQL version 12.6 on Amazon RDS (Deprecated)](#postgresql-versions-version126 "#postgresql-versions-version126")
- [PostgreSQL version 12.5 on Amazon RDS (Deprecated)](#postgresql-versions-version125 "#postgresql-versions-version125")
- [PostgreSQL version 12.4 on Amazon RDS (Deprecated)](#postgresql-versions-version124 "#postgresql-versions-version124")
- [PostgreSQL version 12.3 on Amazon RDS (Deprecated)](#postgresql-versions-version123 "#postgresql-versions-version123")
- [PostgreSQL version 12.2 on Amazon RDS (Deprecated)](#postgresql-versions-version122 "#postgresql-versions-version122")

### PostgreSQL version 12.22-R2 on Amazon RDS (This

version has reached the end of standard support.)

PostgreSQL version 12.22-R2 is now available on Amazon RDS. This release contains several fix for PLV8 [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") for
PostgreSQL announced in
[PostgreSQL 12.22](https://www.postgresql.org/docs/release/12.22/ "https://www.postgresql.org/docs/release/12.22/").

### PostgreSQL version 12.22 on Amazon RDS (This

version has reached the end of standard support.)

PostgreSQL version 12.22 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.22 release](https://www.postgresql.org/docs/release/12.22/ "https://www.postgresql.org/docs/release/12.22/").

### PostgreSQL version 12.21 on Amazon RDS (Deprecated)

PostgreSQL version 12.21 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in [PostgreSQL 12.21](https://www.postgresql.org/docs/release/12.21/ "https://www.postgresql.org/docs/release/12.21/").

###### New features

- Starting in RDS for PostgreSQL versions 17.1, 16.5, 15.9, 14.14, 13.17, and 12.21, some
  connection slots are reserved for the new `rds_reserved` role, which is granted
  to Amazon RDS administrative users. The number of reserved connection slots is determined by the
  `rds.rds_reserved_connections` parameter . You may need to adjust the value of
  the `max_connections` parameter to account for the number of Amazon RDS reserved
  connection slots.

The `rds_reserved` role is a new predefined role created by Amazon RDS. Predefined
roles and their privileges can't be changed. You can't drop, rename, or modify privileges
for these predefined roles. Attempting to modify a predefined role results in an
error.

- Unblocked `ALTER TEMP TABLE` and `DROP TEMP TABLE` in Blue/Green
  replication.
- Added the `rds_tools.pg_ls_multixactdir()` function for
  `pg_multixact` to monitor the directory disk space usage.
- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

###### Updated features

- The `oracle_fdw` extension was updated to version 2.7.0.
- The `orafce` extension was updated to version 4.13.4.
- The `pg_cron` extension was updated to version 1.6.4.
- The `pg_hint_plan` extension was updated to version 1.3.10.
- The `pgvector` extension was updated to version 0.7.4.
- The `PostGIS` extension was updated to version 3.4.3.
- The `rds_tools` extension was updated to version 1.7.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.20-R3 on Amazon RDS (Deprecated)

PostgreSQL version 12.20-R3 is now available on Amazon RDS. This release contains fixes for
[CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced in [PostgreSQL 12.20](https://www.postgresql.org/docs/release/12.20/ "https://www.postgresql.org/docs/release/12.20/").

### PostgreSQL version 12.20-R2 on Amazon RDS (Deprecated)

PostgreSQL version 12.20-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.20 release](https://www.postgresql.org/docs/release/12.20/ "https://www.postgresql.org/docs/release/12.20/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 12.20 on Amazon RDS (Deprecated)

PostgreSQL version 12.20 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 12.20 release](https://www.postgresql.org/docs/release/12.20/ "https://www.postgresql.org/docs/release/12.20/").

**New features and enhancements**

- [Delegated extension role](../UserGuide/RDS_delegated_ext.md "../UserGuide/RDS_delegated_ext.md") was added.

This version also includes the following extension updates:

- The `orafce` extension was updated to 4.10.3.
- The `pg_cron` extension was updated to 1.6.3.
- The `pgTAP` extension was updated to 1.3.3.
- The `pgvector` extension was updated to 0.7.3.
- The `wal2json` extension was updated to 2.6.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.19-R4 on Amazon RDS (Deprecated)

PostgreSQL version 12.19-R4 is now available on Amazon RDS. This release contains fixes for [CVE-2022-4174](https://nvd.nist.gov/vuln/detail/cve-2022-4174 "https://nvd.nist.gov/vuln/detail/cve-2022-4174") and
Rust [CVE
RUSTSEC-2024-042](https://rustsec.org/advisories/RUSTSEC-2024-0421.html "https://rustsec.org/advisories/RUSTSEC-2024-0421.html") for PostgreSQL announced
in [PostgreSQL 12.19](https://www.postgresql.org/docs/release/12.19/ "https://www.postgresql.org/docs/release/12.19/").

### PostgreSQL version 12.19-R3 on Amazon RDS (Deprecated)

PostgreSQL version 12.19-R3 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.19 release](https://www.postgresql.org/docs/release/12.19/ "https://www.postgresql.org/docs/release/12.19/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring after
  database upgrades.

### PostgreSQL version 12.19-R2 on Amazon RDS (Deprecated)

PostgreSQL version 12.19-R2 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.19 release](https://www.postgresql.org/docs/release/12.19/ "https://www.postgresql.org/docs/release/12.19/").

**New features and enhancements**

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`
- Fixed a performance issue in `pgvector` for index creation on halfvec data
  type
- Fixed a bug in `aws_s3` causing import queries to occasionally get stuck and
  fail to terminate
- Fixed a performance issue in `aws_s3` and `aws_lambda`

**This version also includes the following extension change:**

- The `plv8` extension was updated to 3.1.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.19 on Amazon RDS (Deprecated)

PostgreSQL version 12.19 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the [PostgreSQL 12.19 release](https://www.postgresql.org/docs/release/12.19/ "https://www.postgresql.org/docs/release/12.19/").

**New features and enhancements**

- The blue/green deployment switchover won’t be blocked by the `REFRESH MATERIALIZED
VIEW` statement.
- Fixed the permission denial for the `CREATE DATABASE WITH OWNER`
  statement.
- Upgraded the `aws_s3` extension to version 1.2 to support the export to S3
  with the KMS customer managed key.
- Fixed a pgvector compatibility issue with some of the previous generations of DB
  instances, such as m4.

This version also includes the following extension updates:

- The `aws_s3` extension was updated to 1.2.
- The `orafce` extension was updated to 4.9.4.
- The `pg_hint_plan` extension was updated to 1.3.9.
- The `pgvector` extension was updated to 0.7.0.
- The `postgis` extension was updated to 3.4.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.18-R4 on Amazon RDS (Deprecated)

PostgreSQL version 12.18-R4 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.18
release](https://www.postgresql.org/docs/release/12.18/ "https://www.postgresql.org/docs/release/12.18/").

**New features and enhancements**

- Fixed potential incompatibilities in the `plv8` extension occurring
  after database upgrades.

### PostgreSQL version 12.18-R3 on Amazon RDS (Deprecated)

PostgreSQL version 12.18-R3 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 12.18 release.](https://www.postgresql.org/docs/release/12.18/ "https://www.postgresql.org/docs/release/12.18/").

**New features and enhancements**

- Fixed a security exploit issue in `plv8`
- Fixed a security issue in `pg_repack`

**This version also includes the following extension change:**

- The `plv8` extension was updated to 3.1.10.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.18-R2 on Amazon RDS (Deprecated)

PostgreSQL version 12.18-R2 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 12.18 release.](https://www.postgresql.org/docs/release/12.18/ "https://www.postgresql.org/docs/release/12.18/").

**This version includes the following extension changes:**

- The `pg_partman` extension was updated to version 5.0.1.
- The `pgactive` extension was updated to version 2.1.3.
- The `pgtap` extension was updated to version 1.3.2.
- The `pgvector` extension was updated to version 0.6.2.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.18 on Amazon RDS (Deprecated)

PostgreSQL version 12.18 is now available on Amazon RDS. This release contains several fixes and
improvements for PostgreSQL announced in the
[PostgreSQL 12.18 release.](https://www.postgresql.org/docs/release/12.18/ "https://www.postgresql.org/docs/release/12.18/").

###### New features and enhancements

- Fixed the multisecond latency on the `aws_lambda` calls
- Fixed a bug preventing the termination of autovacuum

This version includes the following changes:

- The `orafce` extension was updated to version 4.9.0.
- The `pg_cron` extension was updated to version 1.6.2.
- The `pgactive` extension was updated to version 2.1.2.
- The `pgvector` extension was updated to 0.6.0.
- The `PostGIS` extension was updated to 3.4.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.17-R2 on Amazon RDS (Deprecated)

PostgreSQL version 12.17-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 12.17 release](https://www.postgresql.org/docs/release/12.17/ "https://www.postgresql.org/docs/release/12.17/").

###### New features and enhancements

- Fixed a crash in `CatalogCacheComputeHashValue` with `dblink_connect` due to a `Null` or `invalid` connection.
- Backported run_as_owner to RPG 12:
  - Backported a security fix for the logical replication apply worker that allows regular table owners to obtain privilege escalation to the subscription owner (an rds_superuser).
    The logical apply worker mitigates the risk by temporarily switching the role from the subscription owner to the table owner during logical apply.

  In the cases of potential security breaches, the fix will break your existing logical replication if any table in the subscription is owned by a regular user, and there are
  security-restricted operations attached to the table via triggers or default expressions. We recommend that you carefully examine the operations attached to the table
  if you notice the logical replication is broken after the upgrade. If all of the operations are as expected and you wish to revert the behavior of the logical replication so your application
  can continue, you can do so by setting the new parameter `rds.run_logical_replication_as_subscription_owner` to true. Be aware that by doing so your logical replication will be
  vulnerable to the aforementioned security risk again.

- Added `rds.run_logical_replication_as_subscription_owner` to the Amazon RDS parameter group.
- Fixed the overflow in the `pg_transport` extension.
- Removed the unsupported shared libraries from the engine binary.

### PostgreSQL version 12.17 on Amazon RDS (Deprecated)

PostgreSQL version 12.17 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.17
release](https://www.postgresql.org/docs/release/12.17/ "https://www.postgresql.org/docs/release/12.17/").

###### New features and enhancements

- Fixed a bug where `pg_database_size()` with an invalid OID causes a
  crash.
- Added support for the `rds.enable_pgactive` parameter in rdsutils to
  avoid the warning message.
- Exposed RDKit guc param `rdkit.morgan_fp_size`.
- Fixed the bug where setting `TABLESPACE` with `DEFAULT`
  option in `CREATE` or `ALTER DATABASE` fails.
- Added the `pgactive` extension.

This version includes the following changes:

- The `hll` extension was updated to version 2.18
- The `oracle_fdw` extension was updated to version 2.6.0.
- The `orafce` extension was updated to version 4.6.1.
- The `pg_cron` extension was updated to version 1.6.1.
- The `pg_proctab` extension was updated to version 0.0.10.
- The `pgtap` extension was updated to version 1.3.1.
- The `pgvector` extension was updated to version 0.5.1.
- The `plprofiler` extension was updated to version 4.2.4.
- The `PostGIS` extension was updated to version 3.4.0.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.16-R2 on Amazon RDS (Deprecated)

PostgreSQL version 12.16-R2 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 12.16 release](https://www.postgresql.org/docs/release/12.16/ "https://www.postgresql.org/docs/release/12.16/").

###### New features and enhancements

- The `pgvector` extension was added.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.16 on Amazon RDS (Deprecated)

PostgreSQL version 12.16 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.16
release](https://www.postgresql.org/docs/release/12.16/ "https://www.postgresql.org/docs/release/12.16/").

###### New features and enhancements

- A bug was fixed preventing users with the `rds_superuser` role from
  creating schemas in databases owned by other users.
- Users with the `rds_superuser` role can now access toast tables in the
  `pg_toast schema` that are owned by other users.
- Fixed an issue where `ALTER TABLE` took a ShareLock and may cause
  deadlocks.

This version also includes the following changes:

- The `orafce` extension was updated to version 4.3.0.
- The `pglogical` extension was updated to version 2.4.3.
- The `PostGIS` extension was updated to version 3.3.3.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.15 on Amazon RDS (Deprecated)

PostgreSQL version 12.15 is now available on Amazon RDS. This release contains several fixes and improvements for PostgreSQL announced in the
[PostgreSQL 12.15 release](https://www.postgresql.org/docs/release/12.15/ "https://www.postgresql.org/docs/release/12.15/").

###### New features and enhancements

- Fixed a security issue involving `rds_sec_override` which wasn't reset after the intended usage, allowing unauthorized
  access to restricted tables
- You can use logical_seed_lsn to determine the LSN at which a snapshot is taken in order to establish logical replication
  connection between the source and the restored target database. You can then use logical replication to continuously stream the newer
  data recorded after the LSN and synchronize the changes from publisher to subscriber. Specifically, it allows the customer to create a
  logical slot on a source RDS database, take a snapshot, restore the snapshot to a new RDS instance (target), and use the value of
  logical_seed_lsn() from the target instance to advance the logical slot on the source instance in order to subscribe the target to
  the source.

This version also includes the following changes:

- `compat-collation-for-glibc` was updated to version 1.8
- `pg_cron` was updated to version 1.5.2
- `pglogical` was updated to version 2.4.2
- `PostGIS` was updated to version 3.3.2

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.14 on Amazon RDS (Deprecated)

PostgreSQL version 12.14 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.14
release](https://www.postgresql.org/docs/release/12.14/ "https://www.postgresql.org/docs/release/12.14/").

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.13 on Amazon RDS (Deprecated)

PostgreSQL version 12.13 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in the [PostgreSQL 12.13
release](https://www.postgresql.org/docs/release/12.13/ "https://www.postgresql.org/docs/release/12.13/").

New features and enhancements

- PostgreSQL version 12.13 added support for the `tcn` ("triggered change
  notification") extension which generates notification events on table changes via a
  trigger function called `triggered_change_notification`. The tcn
  extension is useful for applications using drivers which support asynchronous
  notification. This makes it possible to notify all clients if the contents of a
  table have been changed, enabling them to take appropriate action in near-real time,
  such as updating a table cache or information display.

However, such functionality should only be used with care as it makes all data
changes on the table available to all clients (including unprivileged users) through
the notification events when they listen on the tcn channel. It is the user’s
responsibility to avoid using tcn trigger on a table with sensitive data to avoid
information leakage.

This version includes the following changes:

- The seg extension version 1.3 is added.
- The tcn extension version 1.0 is added.
- The orafce extension is updated to 3.24.
- The pgaudit extension is updated to 1.4.3.
- The pgtap extension is updated to 1.2.0.
- The PostGIS dependency GDAL is updated to 3.4.3.
- The PostGIS dependency PROJ is updated to 7.0.1.
- The wal2json extension is updated to 2.5.
- The aws_s3 extension is updated to 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.12 on Amazon RDS (Deprecated)

PostgreSQL version 12.12 is now available on Amazon RDS. This release contains several fixes
and improvements for PostgreSQL announced in [PostgreSQL 12.12](https://www.postgresql.org/docs/release/12.12/ "https://www.postgresql.org/docs/release/12.12/").

This version includes the following changes:

- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to 3.1.7
- The [pgRouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html")
  extension is updated to 3.0.6

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.11 on Amazon RDS (Deprecated)

PostgreSQL version 12.11 is now available on Amazon RDS. This release contains several fixes
and improvements that were announced in [PostgreSQL 12.11](https://www.postgresql.org/docs/release/12.11/ "https://www.postgresql.org/docs/release/12.11/").

This version also includes the following changes:

- The [pglogical](https://github.com/2ndQuadrant/pglogical "https://github.com/2ndQuadrant/pglogical")
  extension is updated to 2.4.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.10 on Amazon RDS (Deprecated)

PostgreSQL version 12.10 is now available on Amazon RDS. This release contains several fixes
and improvements that were announced in [12.10](https://www.postgresql.org/docs/release/12.10/ "https://www.postgresql.org/docs/release/12.10/").

This version also includes the following changes:

- The [pgaudit](https://github.com/pgaudit/pgaudit/ "https://github.com/pgaudit/pgaudit/") extension is
  updated to 1.4.2. For information about using this extension with RDS for PostgreSQL, see
  [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit").
- The [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") (large
  objects) module is updated to version 1.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.9 on Amazon RDS (Deprecated)

PostgreSQL version 12.9 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [12.9](https://www.postgresql.org/docs/release/12.9/ "https://www.postgresql.org/docs/release/12.9/").

This version also includes the following changes:

- The [pg_cron](https://github.com/citusdata/pg_cron "https://github.com/citusdata/pg_cron") extension
  is updated to 1.4.1
- The [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan/ "https://github.com/ossc-db/pg_hint_plan/")
  extension is updated to 1.3.7.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.8 on Amazon RDS (Deprecated)

PostgreSQL version 12.8 is now available on Amazon RDS. This release contains several fixes and
improvements that were announced in [12.8](https://www.postgresql.org/docs/release/12.8/ "https://www.postgresql.org/docs/release/12.8/").

This version also includes the following changes:

- The [pgRouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html")
  extension is updated to version 3.0.5.
- The `pglogical` extension is updated to version 2.4.0.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.1.4, along with the following
  related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.7 on Amazon RDS (Deprecated)

PostgreSQL version 12.7 is now available on Amazon RDS. PostgreSQL version 12.7 contains
several improvements that were announced for PostgreSQL release [12.7](https://www.postgresql.org/docs/release/12.7/ "https://www.postgresql.org/docs/release/12.7/").

This version also includes the following changes:

- The [oracle_fdw](https://github.com/laurenz/oracle_fdw "https://github.com/laurenz/oracle_fdw")
  extension version 2.3.0 is added. For more information, see [Working with Oracle databases by using the oracle_fdw extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-oracle-fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#postgresql-oracle-fdw") in the
  _Amazon RDS User Guide_.
- The [orafce](https://github.com/orafce/orafce "https://github.com/orafce/orafce") extension is
  updated to version 3.15.
- The [pg_cron](../UserGuide/PostgreSQL_pg_cron.md "../UserGuide/PostgreSQL_pg_cron.md")
  extension is updated to version 1.3.1.
- The [pg_partman](../UserGuide/PostgreSQL_Partitions.md "../UserGuide/PostgreSQL_Partitions.md")
  extension is updated to version 4.5.1.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.0.3, along with the following
  related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.6 on Amazon RDS (Deprecated)

PostgreSQL version 12.6 is now available on Amazon RDS. PostgreSQL version 12.6 contains
several improvements that were announced for PostgreSQL release [12.6](https://www.postgresql.org/docs/release/12.6/ "https://www.postgresql.org/docs/release/12.6/").

This version also includes the following changes:

- The `aws_lambda` extension version 1.0 is added. For more information,
  see [Invoking an AWS Lambda
  function from an RDS for PostgreSQL DB instance](../UserGuide/PostgreSQL-Lambda.md "../UserGuide/PostgreSQL-Lambda.md") in the
  _Amazon RDS User Guide_.
- The [pg_bigm](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html "https://pgbigm.osdn.jp/pg_bigm_en-1-2.html")
  extension version 1.2 is added.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.0.2.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.5 on Amazon RDS (Deprecated)

PostgreSQL version 12.5 is now available on Amazon RDS. PostgreSQL version 12.5 contains
several improvements that were announced for PostgreSQL release [12.5](https://www.postgresql.org/docs/12/release-12-5.html "https://www.postgresql.org/docs/12/release-12-5.html").

This version also includes the following changes:

- Added the `pg_partman` extension version 4.4.0. For more information,
  see [Managing PostgreSQL
  partitions with the pg_partman extension](../UserGuide/PostgreSQL_Partitions.md "../UserGuide/PostgreSQL_Partitions.md") in the _Amazon RDS User
  Guide_.
- Added the `pg_cron` extension version 1.3.0. For more information, see
  [Scheduling maintenance
  with the PostgreSQL pg_cron extension](../UserGuide/PostgreSQL_pg_cron.md "../UserGuide/PostgreSQL_pg_cron.md") in the
  _Amazon RDS User Guide_.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.4 on Amazon RDS (Deprecated)

PostgreSQL version 12.4 is now available on Amazon RDS. PostgreSQL version 12.4 contains
several improvements that were announced for PostgreSQL release [12.4](https://www.postgresql.org/docs/12/release-12-4.html "https://www.postgresql.org/docs/12/release-12-4.html").

This version also includes the following changes:

- Added the `pg_proctab` extension version 0.0.9
- Added the `rdkit` extension version 3.8
- Upgraded the `aws_s3` extension to version 1.1.
- Upgraded the `pglogical` extension to version 2.3.2
- Upgraded the `wal2json` extension to version 2.3

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.3 on Amazon RDS (Deprecated)

PostgreSQL version 12.3 is now available on Amazon RDS. PostgreSQL version 12.3 contains
several improvements that were announced for PostgreSQL release [12.3](https://www.postgresql.org/docs/12/release-12-3.html "https://www.postgresql.org/docs/12/release-12-3.html").

This version also includes the following changes:

- Upgraded the `pg_hint_plan` extension to version 1.3.5.
- Upgraded the `pglogical` extension to version 2.3.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

### PostgreSQL version 12.2 on Amazon RDS (Deprecated)

PostgreSQL version 12.2 is now available on Amazon RDS. PostgreSQL version 12.2 contains
several improvements that were announced for PostgreSQL releases [12.0](https://www.postgresql.org/docs/12/release-12.html "https://www.postgresql.org/docs/12/release-12.html"), [12.1](https://www.postgresql.org/docs/12/release-12-1.html "https://www.postgresql.org/docs/12/release-12-1.html"), and [12.2](https://www.postgresql.org/docs/12/release-12-2.html "https://www.postgresql.org/docs/12/release-12-2.html").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
12](postgresql-extensions.md#postgresql-extensions-12x "postgresql-extensions.md#postgresql-extensions-12x").

## PostgreSQL 11 versions (Some of these versions

have reached the end of standard support or deprecated.)

###### Minor versions

- [PostgreSQL version 11.22-R2 on
  Amazon RDS (This
  version has reached the end of standard support.)](#postgresql-versions-version1122R2 "#postgresql-versions-version1122R2")
- [PostgreSQL version 11.22 on Amazon RDS (This
  version has reached the end of standard support.)](#postgresql-versions-version1122 "#postgresql-versions-version1122")
- [PostgreSQL version 11.21 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1121 "#postgresql-versions-version1121")
- [PostgreSQL version 11.20 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1120 "#postgresql-versions-version1120")
- [PostgreSQL version 11.19 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1119 "#postgresql-versions-version1119")
- [PostgreSQL version 11.18 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1118 "#postgresql-versions-version1118")
- [PostgreSQL version 11.17 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1117 "#postgresql-versions-version1117")
- [PostgreSQL version 11.16 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1116 "#postgresql-versions-version1116")
- [PostgreSQL version 11.15 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1115 "#postgresql-versions-version1115")
- [PostgreSQL version 11.14 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1114 "#postgresql-versions-version1114")
- [PostgreSQL version 11.13 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1113 "#postgresql-versions-version1113")
- [PostgreSQL version 11.12 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1112 "#postgresql-versions-version1112")
- [PostgreSQL version 11.11 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1111 "#postgresql-versions-version1111")
- [PostgreSQL version 11.10 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1110 "#postgresql-versions-version1110")
- [PostgreSQL version 11.9 on Amazon RDS
  (Deprecated)](#postgresql-versions-version119 "#postgresql-versions-version119")
- [PostgreSQL version 11.8 on Amazon RDS
  (Deprecated)](#postgresql-versions-version118 "#postgresql-versions-version118")
- [PostgreSQL version 11.7 on Amazon RDS
  (Deprecated)](#postgresql-versions-version117 "#postgresql-versions-version117")
- [PostgreSQL version 11.6 on Amazon RDS
  (Deprecated)](#postgresql-versions-version116 "#postgresql-versions-version116")
- [PostgreSQL version 11.5 on Amazon RDS
  (Deprecated)](#postgresql-versions-version115 "#postgresql-versions-version115")
- [PostgreSQL version 11.4 on Amazon RDS
  (Deprecated)](#postgresql-versions-version114 "#postgresql-versions-version114")
- [PostgreSQL version 11.2 on Amazon RDS
  (Deprecated)](#postgresql-versions-version112 "#postgresql-versions-version112")
- [PostgreSQL version 11.1 on Amazon RDS
  (Deprecated)](#postgresql-versions-version111 "#postgresql-versions-version111")

### PostgreSQL version 11.22-R2 on

Amazon RDS (This
version has reached the end of standard support.)

PostgreSQL version 11.22-R2 is now available on Amazon RDS. This release contains
several fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.22
release](https://www.postgresql.org/docs/release/11.22/ "https://www.postgresql.org/docs/release/11.22/").

###### New features and enhancements

- Backported run_as_owner to RPG 11:
  - Backported a security fix for the logical replication apply
    worker that allows regular table owners to obtain privilege
    escalation to the subscription owner (an rds_superuser). The logical
    apply worker mitigates the risk by temporarily switching the role
    from the subscription owner to the table owner during logical
    apply.

  In the cases of potential security breaches, the fix will break
  your existing logical replication if any table in the subscription
  is owned by a regular user, and there are security-restricted
  operations attached to the table via triggers or default
  expressions. We recommend that you carefully examine the operations
  attached to the table if you notice the logical replication is
  broken after the upgrade. If all of the operations are as expected
  and you wish to revert the behavior of the logical replication so
  your application can continue, you can do so by setting the new
  parameter
  `rds.run_logical_replication_as_subscription_owner`
  to true. Be aware that by doing so your logical replication will be
  vulnerable to the aforementioned security risk again.

- Added `rds.run_logical_replication_as_subscription_owner` to
  the Amazon RDS parameter group.
- Fixed the overflow in the `pg_transport` extension.
- Removed the unsupported shared libraries from the engine binary.

### PostgreSQL version 11.22 on Amazon RDS (This

version has reached the end of standard support.)

PostgreSQL version 11.22 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.22
release](https://www.postgresql.org/docs/release/11.22/ "https://www.postgresql.org/docs/release/11.22/").

###### New features and enhancements

- Fixed a bug where `pg_database_size()` with an invalid OID
  causes a crash.
- Added support for the `rds.enable_pgactive` parameter in
  rdsutils to avoid the warning message.
- Exposed RDKit guc param `rdkit.morgan_fp_size`.
- Fixed the bug where setting `TABLESPACE` with
  `DEFAULT` option in `CREATE` or `ALTER
DATABASE` fails.
- Added the `pgactive` extension.

This version includes the following changes:

- The `hll` extension was updated to version 2.18
- The `orafce` extension was updated to version 4.6.1.
- The `pg_proctab` extension was updated to version
  0.0.10.
- The `pgtap` extension was updated to version 1.3.1.
- The `plprofiler` extension was updated to version 4.2.4.

### PostgreSQL version 11.21 on Amazon RDS

(Deprecated)

PostgreSQL version 11.21 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.21
release](https://www.postgresql.org/docs/release/11.21/ "https://www.postgresql.org/docs/release/11.21/").

###### New features and enhancements

- A bug was fixed preventing users with the `rds_superuser` role
  from creating schemas in databases owned by other users.
- Users with the `rds_superuser` role can now access toast tables
  in the `pg_toast schema` that are owned by other users.
- Fixed an issue where `ALTER TABLE` took a ShareLock and may
  cause deadlocks.

This version also includes the following changes:

- The `orafce` extension was updated to version 4.3.0.
- The `pglogical` extension was updated to version 2.4.3.
- The `PostGIS` extension was updated to version 3.3.3.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.20 on Amazon RDS

(Deprecated)

PostgreSQL version 11.20 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.20
release](https://www.postgresql.org/docs/release/11.20/ "https://www.postgresql.org/docs/release/11.20/").

###### New features and enhancements

- Fixed a security issue involving `rds_sec_override` which
  wasn't reset after the intended usage, allowing unauthorized access to
  restricted tables
- You can use logical_seed_lsn to determine the LSN at which a snapshot is
  taken in order to establish logical replication connection between the
  source and the restored target database. You can then use logical
  replication to continuously stream the newer data recorded after the LSN and
  synchronize the changes from publisher to subscriber. Specifically, it
  allows the customer to create a logical slot on a source RDS database, take
  a snapshot, restore the snapshot to a new RDS instance (target), and use the
  value of logical_seed_lsn() from the target instance to advance the logical
  slot on the source instance in order to subscribe the target to the
  source.

This version also includes the following changes:

- `compat-collation-for-glibc` was updated to version 1.8
- `pglogical` was updated to version 2.4.2
- `PostGIS` was updated to version 3.3.2

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.19 on Amazon RDS

(Deprecated)

PostgreSQL version 11.19 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.19
release](https://www.postgresql.org/docs/release/11.19/ "https://www.postgresql.org/docs/release/11.19/").

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.18 on Amazon RDS

(Deprecated)

PostgreSQL version 11.18 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 11.18
release](https://www.postgresql.org/docs/release/11.18/ "https://www.postgresql.org/docs/release/11.18/").

New features and enhancements

- PostgreSQL version 11.18 added support for the `tcn`
  ("triggered change notification") extension which generates notification
  events on table changes via a trigger function called
  `triggered_change_notification`. The tcn extension is useful
  for applications using drivers which support asynchronous notification. This
  makes it possible to notify all clients if the contents of a table have been
  changed, enabling them to take appropriate action in near-real time, such as
  updating a table cache or information display.

However, such functionality should only be used with care as it makes all
data changes on the table available to all clients (including unprivileged
users) through the notification events when they listen on the tcn channel.
It is the user’s responsibility to avoid using tcn trigger on a table with
sensitive data to avoid information leakage.

This version includes the following changes:

- The seg extension version 1.3 is added.
- The tcn extension version 1.0 is added.
- The orafce extension is updated to 3.24.
- The pgaudit extension is updated to 1.3.4.
- The pgtap extension is updated to 1.2.0.
- The PostGIS dependency GDAL is updated to 3.4.3.
- The PostGIS dependency PROJ is updated to 7.0.1.
- The wal2json extension is updated to 2.5.
- The aws_s3 extension is updated to 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.17 on Amazon RDS

(Deprecated)

PostgreSQL version 11.17 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in [PostgreSQL
11.17](https://www.postgresql.org/docs/release/11.17/ "https://www.postgresql.org/docs/release/11.17/").

This version includes the following change:

- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to 3.1.7

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.16 on Amazon RDS

(Deprecated)

PostgreSQL version 11.16 is now available on Amazon RDS. This release contains several
fixes and improvements that were announced in [PostgreSQL
11.16](https://www.postgresql.org/docs/release/11.16/ "https://www.postgresql.org/docs/release/11.16/").

This version also includes the following changes:

- The [pglogical](https://github.com/2ndQuadrant/pglogical "https://github.com/2ndQuadrant/pglogical") extension is updated to 2.4.1.
- The [aws_commons](../UserGuide/USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri "../UserGuide/USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri") extension is updated to 1.2.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.15 on Amazon RDS

(Deprecated)

PostgreSQL version 11.15 is now available on Amazon RDS. PostgreSQL version 11.15
contains several improvements that were announced for PostgreSQL release [11.15](https://www.postgresql.org/docs/release/11.15/ "https://www.postgresql.org/docs/release/11.15/").

This version also includes the following changes:

- The [pgaudit](https://github.com/pgaudit/pgaudit/ "https://github.com/pgaudit/pgaudit/")
  extension is updated to 1.3.3. For information about using this extension
  with RDS for PostgreSQL, see [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit").
- The [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") module is updated to version 1.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.14 on Amazon RDS

(Deprecated)

PostgreSQL version 11.14 is now available on Amazon RDS. PostgreSQL version 11.14
contains several improvements that were announced for PostgreSQL release [11.14](https://www.postgresql.org/docs/release/11.14/ "https://www.postgresql.org/docs/release/11.14/").

This version also includes the following change:

- The [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan/ "https://github.com/ossc-db/pg_hint_plan/") extension is updated to 1.3.7.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.13 on Amazon RDS

(Deprecated)

PostgreSQL version 11.13 is now available on Amazon RDS. PostgreSQL version 11.13
contains several improvements that were announced for PostgreSQL release [11.13](https://www.postgresql.org/docs/release/11.13/ "https://www.postgresql.org/docs/release/11.13/").

This version also includes the following changes:

- The [pgrouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html") extension is updated to version 2.6.3.
- The `pglogical` extension is updated to version 2.4.0.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.1.4, along with the
  following related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.12 on Amazon RDS

(Deprecated)

PostgreSQL version 11.12 is now available on Amazon RDS. PostgreSQL version 11.12
contains several improvements that were announced for PostgreSQL release [11.12](https://www.postgresql.org/docs/release/11.12/ "https://www.postgresql.org/docs/release/11.12/").

This version also includes the following change:

- The [orafce](https://github.com/orafce/orafce "https://github.com/orafce/orafce") extension
  is updated to version 3.15.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.11 on Amazon RDS

(Deprecated)

PostgreSQL version 11.11 is now available on Amazon RDS. PostgreSQL version 11.11
contains several improvements that were announced for PostgreSQL release [11.11](https://www.postgresql.org/docs/release/11.11/ "https://www.postgresql.org/docs/release/11.11/").

This version also added the following new extension:

- The [pg_bigm](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html "https://pgbigm.osdn.jp/pg_bigm_en-1-2.html") extension version 1.2.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.10 on Amazon RDS

(Deprecated)

PostgreSQL version 11.10 is now available on Amazon RDS. PostgreSQL version 11.10
contains several improvements that were announced for PostgreSQL release [11.10](https://www.postgresql.org/docs/11/release-11-10.html "https://www.postgresql.org/docs/11/release-11-10.html").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.9 on Amazon RDS

(Deprecated)

PostgreSQL version 11.9 is now available on Amazon RDS. PostgreSQL version 11.9
contains several improvements that were announced for PostgreSQL release [11.9](https://www.postgresql.org/docs/11/release-11-9.html "https://www.postgresql.org/docs/11/release-11-9.html").

This version also includes the following changes:

- Added the `aws_s3` extension version 1.1
- Added the `pg_proctab` extension version 0.0.9
- Upgraded the `pgaudit` extension to version 1.3.1
- Upgraded the `pglogical` extension to version 2.2.2
- Added the `rdkit` extension version 3.8

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.8 on Amazon RDS

(Deprecated)

PostgreSQL version 11.8 contains several bug fixes for issues in release 11.7. For
more information on the fixes in PostgreSQL 11.8, see the [PostgreSQL 11.8
documentation](https://www.postgresql.org/docs/11/release-11-8.html "https://www.postgresql.org/docs/11/release-11-8.html").

This version also includes the following change:

- Upgraded the `pg_hint_plan` extension to version 1.3.5.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.7 on Amazon RDS

(Deprecated)

PostgreSQL version 11.7 contains several bug fixes for issues in release 11.6. For
more information on the fixes in PostgreSQL 11.7, see the [PostgreSQL 11.7
documentation](https://www.postgresql.org/docs/11/release-11-7.html "https://www.postgresql.org/docs/11/release-11-7.html").

### PostgreSQL version 11.6 on Amazon RDS

(Deprecated)

PostgreSQL version 11.6 contains several bug fixes for issues in release 11.5. For
more information on the fixes in PostgreSQL 11.6, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/11/release-11-6.html "https://www.postgresql.org/docs/11/release-11-6.html").

This version also includes the following changes:

- Upgraded the `pgTAP` extension to version 1.1.0.
- Added the `plprofiler` extension.
- Added to `shared_preload_libraries` support for
  `pg_prewarm` to start automatically.

### PostgreSQL version 11.5 on Amazon RDS

(Deprecated)

PostgreSQL version 11.5 contains several bug fixes for issues in release 11.4. For
more information on the fixes in PostgreSQL 11.5, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/11/release-11-5.html "https://www.postgresql.org/docs/11/release-11-5.html").

This version also includes the following changes:

- A new extension `pg_transport` is added.
- The extension `aws_s3` has been updated to support
  virtual-hosted style requests. For more information, see [Amazon
  S3 path deprecation plan – The rest of the story](https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/ "https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/").
- The `PostGIS` extension is updated to version 2.5.2.

### PostgreSQL version 11.4 on Amazon RDS

(Deprecated)

This release contains an important security fix and also bug fixes and
improvements done by the PostgreSQL community. For more information on the security
fix, see the [PostgreSQL
community announcement](https://www.postgresql.org/about/news/1949/ "https://www.postgresql.org/about/news/1949/") and the security fix CVE-2019-10164.

With this release, the `pg_hint_plan` extension has been updated to
version 1.3.4.

For more information on the fixes in PostgreSQL 11.4, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/11/release-11-4.html "https://www.postgresql.org/docs/11/release-11-4.html").

### PostgreSQL version 11.2 on Amazon RDS

(Deprecated)

PostgreSQL version 11.2 contains several bug fixes for issues in release 11.1. For
more information on the fixes in PostgreSQL 11.2, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/11/release-11-2.html "https://www.postgresql.org/docs/11/release-11-2.html").

This version also includes the following changes:

- A new [pgTAP](https://pgtap.org/ "https://pgtap.org/") extension version
  1.0.
- Support for Amazon S3 import. For more information, see [Importing Amazon S3 data into an RDS for PostgreSQL DB instance](../UserGuide/USER_PostgreSQL.md "../UserGuide/USER_PostgreSQL.md") in the
  _Amazon RDS User Guide_.
- Multiple major version upgrade is available to PostgreSQL 11.2 from
  certain previous PostgreSQL versions. For more information, see [Choosing a major version upgrade for PostgreSQL](../UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion "../UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion") in the
  _Amazon RDS User Guide_.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

### PostgreSQL version 11.1 on Amazon RDS

(Deprecated)

PostgreSQL version 11.1 contains several improvements that were announced in
[PostgreSQL 11.1
released!](https://www.postgresql.org/about/news/1905/ "https://www.postgresql.org/about/news/1905/") This version includes SQL stored procedures that enable
embedded transactions within a procedure. This version also includes major
improvements to partitioning and parallelism and many useful performance
improvements. For example, by using a non-null constant for a column default, you
can now use an ALTER TABLE command to add a column without causing a table
rewrite.

PostgreSQL version 11.1 contains several bug fixes for issues in release 11. For
complete details, see the [PostgreSQL release
11.1 documentation](https://www.postgresql.org/docs/11/release-11-1.html "https://www.postgresql.org/docs/11/release-11-1.html"). Some changes in this version include the
following:

- Partitioning – Partitioning improvements include support for hash
  partitioning, enabling creation of a default partition, and dynamic row
  movement to another partition based on the key column update.
- Performance – Performance improvements include parallelism while
  creating indexes, materialized views, hash joins, and sequential scans to
  make the operations perform better.
- Stored procedures – SQL stored procedures now added support
  embedded transactions.
- Support for Just-In-Time (JIT) capability – RDS for PostgreSQL 11
  instances are created with JIT capability, speeding evaluation of
  expressions. To enable JIT capability, set the `jit` parameter to
  1 in the PostgreSQL parameter group for the database.
- Segment size – The write-ahead logging (WAL) segment size has been
  changed from 16 MB to 64 MB.
- Autovacuum improvements – To provide valuable logging, the
  parameter `rds.force_autovacuum_logging` is ON by default in
  conjunction with the `log_autovacuum_min_duration` parameter set
  to 10 seconds. To increase autovacuum effectiveness, the values for the
  `autovacuum_max_workers` and
  `autovacuum_vacuum_cost_limit` parameters are computed based
  on host memory capacity to provide larger default values.
- Improved transaction timeout – The parameter
  `idle_in_transaction_session_timeout` is set to 24 hours. Any
  session that has been idle more than 24 hours is terminated.
- Performance metrics – The `pg_stat_statements` extension
  is included in `shared_preload_libraries` by default. This avoids
  having to reboot the instance immediately after creation. However, this
  functionality still requires you to run the statement `CREATE EXTENSION
pg_stat_statements;`. Also, `track_io_timing` is
  enabled by default to add more granular data to
  `pg_stat_statements`.
- The tsearch2 extension is no longer supported – If your application
  uses `tsearch2` functions, update it to use the equivalent
  functions provided by the core PostgreSQL engine. For more information about
  the tsearch2 extension, see [PostgreSQL tsearch2](https://www.postgresql.org/docs/9.6/static/tsearch2.html "https://www.postgresql.org/docs/9.6/static/tsearch2.html").
- The chkpass extension is no longer supported – For more information
  about the `chkpass` extension, see [PostgreSQL
  chkpass](https://www.postgresql.org/docs/10/chkpass.html "https://www.postgresql.org/docs/10/chkpass.html").
- Extension updates for RDS for PostgreSQL 11.1 include the following:
  - `pgaudit` is updated to 1.3.0
  - `pg_hint_plan` is updated to 1.3.2
  - `pglogical` is updated to 2.2.1
  - `plcoffee` is updated to 2.3.8
  - `plv8` is updated to 2.3.8
  - `PostGIS` is updated to 2.5.1
  - `prefix` is updated to 1.2.8
  - `wal2json` is updated to hash 9e962bad

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
11](postgresql-extensions.md#postgresql-extensions-11x "postgresql-extensions.md#postgresql-extensions-11x").

## PostgreSQL 10 versions (Deprecated)

###### Minor versions

- [PostgreSQL version 10.23 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1023 "#postgresql-versions-version1023")
- [PostgreSQL version 10.22 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1022 "#postgresql-versions-version1022")
- [PostgreSQL version 10.21 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1021 "#postgresql-versions-version1021")
- [PostgreSQL version 10.20 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1020 "#postgresql-versions-version1020")
- [PostgreSQL version 10.19 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1019 "#postgresql-versions-version1019")
- [PostgreSQL version 10.18 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1018 "#postgresql-versions-version1018")
- [PostgreSQL version 10.17 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1017 "#postgresql-versions-version1017")
- [PostgreSQL version 10.16 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1016 "#postgresql-versions-version1016")
- [PostgreSQL version 10.15 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1015 "#postgresql-versions-version1015")
- [PostgreSQL version 10.14 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1014 "#postgresql-versions-version1014")
- [PostgreSQL version 10.13 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1013 "#postgresql-versions-version1013")
- [PostgreSQL version 10.12 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1012 "#postgresql-versions-version1012")
- [PostgreSQL version 10.11 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1011 "#postgresql-versions-version1011")
- [PostgreSQL version 10.10 on Amazon RDS
  (Deprecated)](#postgresql-versions-version1010 "#postgresql-versions-version1010")
- [PostgreSQL version 10.9 on Amazon RDS
  (Deprecated)](#postgresql-versions-version109 "#postgresql-versions-version109")
- [PostgreSQL version 10.7 on Amazon RDS
  (Deprecated)](#postgresql-versions-version107 "#postgresql-versions-version107")
- [PostgreSQL version 10.6 on Amazon RDS
  (Deprecated)](#postgresql-versions-version106 "#postgresql-versions-version106")
- [PostgreSQL version 10.5 on Amazon RDS
  (Deprecated)](#postgresql-versions-version105 "#postgresql-versions-version105")
- [PostgreSQL version 10.4 on Amazon RDS
  (Deprecated)](#postgresql-versions-version104 "#postgresql-versions-version104")
- [PostgreSQL version 10.3 on Amazon RDS
  (Deprecated)](#postgresql-versions-version103 "#postgresql-versions-version103")
- [PostgreSQL version 10.1 on Amazon RDS
  (Deprecated)](#postgresql-versions-version101 "#postgresql-versions-version101")

### PostgreSQL version 10.23 on Amazon RDS

(Deprecated)

PostgreSQL version 10.23 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in the [PostgreSQL 10.23
release](https://www.postgresql.org/docs/release/10.23/ "https://www.postgresql.org/docs/release/10.23/").

New features and enhancements

- PostgreSQL version 10.23 added support for the `tcn`
  ("triggered change notification") extension which generates notification
  events on table changes via a trigger function called
  `triggered_change_notification`. The tcn extension is useful
  for applications using drivers which support asynchronous notification. This
  makes it possible to notify all clients if the contents of a table have been
  changed, enabling them to take appropriate action in near-real time, such as
  updating a table cache or information display.

However, such functionality should only be used with care as it makes all
data changes on the table available to all clients (including unprivileged
users) through the notification events when they listen on the tcn channel.
It is the user’s responsibility to avoid using tcn trigger on a table with
sensitive data to avoid information leakage.

This version includes the following changes:

- The seg extension version 1.1 is added.
- The tcn extension version 1.0 is added.
- The orafce extension is updated to 3.24.
- The pgaudit extension is updated to 1.2.4.
- PostGIS dependency GDAL is updated to 3.4.3.
- PostGIS dependency PROJ is updated to 7.0.1.
- The wal2json extension is updated to 2.5.
- The aws_s3 extension is updated to 1.1.

For version information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.22 on Amazon RDS

(Deprecated)

PostgreSQL version 10.22 is now available on Amazon RDS. This release contains several
fixes and improvements for PostgreSQL announced in [PostgreSQL
10.22](https://www.postgresql.org/docs/release/10.22/ "https://www.postgresql.org/docs/release/10.22/").

This version includes the following change:

- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to 3.1.7

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.21 on Amazon RDS

(Deprecated)

PostgreSQL version 10.21 is now available on Amazon RDS. This release contains several
fixes and improvements that were announced in [PostgreSQL
10.21](https://www.postgresql.org/docs/release/10.21/ "https://www.postgresql.org/docs/release/10.21/").

This version also includes the following changes:

- The [pglogical](https://github.com/2ndQuadrant/pglogical "https://github.com/2ndQuadrant/pglogical") extension is updated to 2.4.1.
- The [aws_commons](../UserGuide/USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri "../UserGuide/USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.create_s3_uri") extension is updated to 1.2.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.20 on Amazon RDS

(Deprecated)

PostgreSQL version 10.20 is now available on Amazon RDS. PostgreSQL version 10.20
contains several improvements that were announced for PostgreSQL release [10.20](https://www.postgresql.org/docs/release/10.20/ "https://www.postgresql.org/docs/release/10.20/").

This version also includes the following changes:

- The [pgaudit](https://github.com/pgaudit/pgaudit/ "https://github.com/pgaudit/pgaudit/")
  extension is updated to 1.2.3. For information about using this extension
  with RDS for PostgreSQL, see [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit") in the _Amazon RDS User Guide_.
- The [lo](https://www.postgresql.org/docs/current/lo.html "https://www.postgresql.org/docs/current/lo.html") module is updated to version 1.1.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.19 on Amazon RDS

(Deprecated)

PostgreSQL version 10.19 is now available on Amazon RDS. PostgreSQL version 10.19
contains several improvements that were announced for PostgreSQL release [10.19](https://www.postgresql.org/docs/release/10.19/ "https://www.postgresql.org/docs/release/10.19/").

This version also includes the following change:

- The [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan/ "https://github.com/ossc-db/pg_hint_plan/") extension is updated to 1.3.6.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.18 on Amazon RDS

(Deprecated)

PostgreSQL version 10.18 is now available on Amazon RDS. PostgreSQL version 10.18
contains several improvements that were announced for PostgreSQL release [10.18](https://www.postgresql.org/docs/release/10.18/ "https://www.postgresql.org/docs/release/10.18/").

This version also includes the following changes:

- The [pgrouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html") extension is updated to version 2.5.5.
- The `pglogical` extension is updated to version 2.4.0.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 3.1.4, along with the
  following related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_raster](https://postgis.net/docs/raster.html "https://postgis.net/docs/raster.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.17 on Amazon RDS

(Deprecated)

PostgreSQL version 10.17 is now available on Amazon RDS. PostgreSQL version 10.17
contains several improvements that were announced for PostgreSQL release [10.17](https://www.postgresql.org/docs/release/10.17/ "https://www.postgresql.org/docs/release/10.17/").

This version also includes the following change:

- The [orafce](https://github.com/orafce/orafce "https://github.com/orafce/orafce") extension
  is updated to version 3.15.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.16 on Amazon RDS

(Deprecated)

PostgreSQL version 10.16 is now available on Amazon RDS. PostgreSQL version 10.16
contains several improvements that were announced for PostgreSQL release [10.16](https://www.postgresql.org/docs/release/10.16/ "https://www.postgresql.org/docs/release/10.16/").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.15 on Amazon RDS

(Deprecated)

PostgreSQL version 10.15 is now available on Amazon RDS. PostgreSQL version 10.15
contains several improvements that were announced for PostgreSQL release [10.15](https://www.postgresql.org/docs/10/release-10-15.html "https://www.postgresql.org/docs/10/release-10-15.html").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.14 on Amazon RDS

(Deprecated)

PostgreSQL version 10.14 is now available on Amazon RDS. PostgreSQL version 10.14
contains several improvements that were announced for PostgreSQL release [10.14](https://www.postgresql.org/docs/10/release-10-14.html "https://www.postgresql.org/docs/10/release-10-14.html").

This version also includes the following changes:

- Added the `aws_s3` extension version 1.1. For more information,
  see [Exporting
  data from an RDS for PostgreSQL DB instance to Amazon S3](../UserGuide/postgresql-s3-export.md "../UserGuide/postgresql-s3-export.md") in the
  _Amazon RDS User Guide_.
- Upgraded the `pgaudit` extension to version 1.2.1
- Upgraded the `pglogical` extension to version 2.2.2
- Upgraded the `wal2json` extension to version 2.3

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.13 on Amazon RDS

(Deprecated)

PostgreSQL version 10.13 contains several bug fixes for issues in release 10.12.
For more information on the fixes in PostgreSQL 10.13, see the [PostgreSQL 10.13
documentation](https://www.postgresql.org/docs/10/release-10-13.html "https://www.postgresql.org/docs/10/release-10-13.html").

This version also includes the following change:

- Upgraded the `pg_hint_plan` extension to version 1.3.5.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL
10](postgresql-extensions.md#postgresql-extensions-101x "postgresql-extensions.md#postgresql-extensions-101x").

### PostgreSQL version 10.12 on Amazon RDS

(Deprecated)

PostgreSQL version 10.12 contains several bug fixes for issues in release 10.11.
For more information on the fixes in PostgreSQL 10.12, see the [PostgreSQL 10.12
documentation](https://www.postgresql.org/docs/10/release-10-12.html "https://www.postgresql.org/docs/10/release-10-12.html").

### PostgreSQL version 10.11 on Amazon RDS

(Deprecated)

PostgreSQL version 10.11 contains several bug fixes for issues in release 10.10.
For more information on the fixes in PostgreSQL 10.11, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/10/release-10-11.html "https://www.postgresql.org/docs/10/release-10-11.html"). Changes in this version include the following:

- Added the `plprofiler` extension.

### PostgreSQL version 10.10 on Amazon RDS

(Deprecated)

PostgreSQL version 10.10 contains several bug fixes for issues in release 10.9.
For more information on the fixes in PostgreSQL 10.10, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/10/release-10-10.html "https://www.postgresql.org/docs/10/release-10-10.html"). Changes in this version include the following:

- The `aws_s3` extension is updated to support virtual-hosted
  style requests. For more information, see [Amazon
  S3 path deprecation plan – The rest of the story](https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/ "https://aws.amazon.com/blogs/aws/amazon-s3-path-deprecation-plan-the-rest-of-the-story/").
- The `The PostGIS` extension is updated to version 2.5.2.

### PostgreSQL version 10.9 on Amazon RDS

(Deprecated)

This release contains an important security fix and also bug fixes and
improvements done by the PostgreSQL community. For more information on the security
fix, see the [PostgreSQL
community announcement](https://www.postgresql.org/about/news/1949/ "https://www.postgresql.org/about/news/1949/") and [security fix
CVE-2019-10164](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-10164 "https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-10164").

With this release, the `pg_hint_plan` extension has been updated to
version 1.3.3.

For more information on the fixes in PostgreSQL 10.9, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/10/release-10-9.html "https://www.postgresql.org/docs/10/release-10-9.html").

### PostgreSQL version 10.7 on Amazon RDS

(Deprecated)

PostgreSQL version 10.7 contains several bug fixes for issues in release 10.6. For
more information on the fixes in 10.7, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/10/release-10-7.html "https://www.postgresql.org/docs/10/release-10-7.html").

This version also includes the following changes:

- Support for Amazon S3 import. For more information, see [Importing Amazon S3 data into an RDS for PostgreSQL DB instance](../UserGuide/USER_PostgreSQL.md "../UserGuide/USER_PostgreSQL.md") in the
  _Amazon RDS User Guide_.
- Multiple major version upgrade is available to PostgreSQL 10.7 from
  certain previous PostgreSQL versions. For more information, see [Choosing a major version upgrade for PostgreSQL](../UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion "../UserGuide/USER_UpgradeDBInstance.md#USER_UpgradeDBInstance.PostgreSQL.MajorVersion") in the
  _Amazon RDS User Guide_.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

### PostgreSQL version 10.6 on Amazon RDS

(Deprecated)

PostgreSQL version 10.6 contains several bug fixes for issues in release 10.5. For
more information on the fixes in PostgreSQL 10.6, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/10/static/release-10-6.html "http://www.postgresql.org/docs/10/static/release-10-6.html").

This version also includes the following changes:

- A new `rds.restrict_password_commands` parameter and a new
  `rds_password` role have been introduced. When the
  `rds.restrict_password_commands` parameter is enabled, only
  users who have the `rds_password` role can make user password and
  password expiration changes. By restricting password-related operations to a
  limited set of roles, you can implement policies such as password complexity
  requirements from the client side. The
  `rds.restrict_password_commands` parameter is static, so it
  requires a database restart to change it. For more information, see [Restricting password management](../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.RestrictPasswordMgmt "../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.RestrictPasswordMgmt") in the _Amazon RDS User
  Guide_.
- The logical decoding plugin `wal2json` has been updated to
  commit `9e962ba`.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

###### Note

Amazon RDS for PostgreSQL has announced the removal of the `tsearch2`
extension in the next major release. We encourage customers still using pre-8.3
text search to migrate to the equivalent built-in features. For more information
about migrating, see the [PostgreSQL documentation](https://www.postgresql.org/docs/9.6/static/textsearch-migration.html "https://www.postgresql.org/docs/9.6/static/textsearch-migration.html").

### PostgreSQL version 10.5 on Amazon RDS

(Deprecated)

PostgreSQL version 10.5 contains several bug fixes for issues in release 10.4. For
more information on the fixes in 10.5, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/10/static/release-10-5.html "http://www.postgresql.org/docs/10/static/release-10-5.html").

This version also includes the following changes:

- Support for the `pglogical` extension version 2.2.0.
  Prerequisites for using this extension are the same as the prerequisites for
  using logical replication for PostgreSQL as described in [Performing logical replication for Amazon RDS for PostgreSQL](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication") in the
  _Amazon RDS User Guide_.
- Support for the `pg_similarity` extension version 1.0.
- Support for the `pageinspect` extension version 1.6.
- Support for the `libprotobuf` extension version 1.3.0 for the
  PostGIS component.
- An update for the `pg_hint_plan` extension to version
  1.3.1.
- An update for the `wal2json` extension to version
  01c5c1e.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 10.4 on Amazon RDS

(Deprecated)

PostgreSQL version 10.4 contains several bug fixes for issues in release 10.3. For
more information on the fixes in 10.4, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/10/static/release-10-4.html "http://www.postgresql.org/docs/10/static/release-10-4.html").

This version also includes the following changes:

- Support for PostgreSQL 10 Logical Replication using the native publication
  and subscription framework. RDS for PostgreSQL databases can function as both
  publishers and subscribers. You can specify replication to other PostgreSQL
  databases at the database-level or at the table-level. With logical
  replication, the publisher and subscriber databases need not be physically
  identical (block-to-block) to each other. This allows for use cases such as
  data consolidation, data distribution, and data replication across different
  database versions for 10.4 and above. For more information, see [Performing logical replication for Amazon RDS for PostgreSQL](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication") in the
  _Amazon RDS User Guide_.
- The temporary file size limitation is user-configurable. You require the
  **rds_superuser** role to modify the
  `temp_file_limit` parameter.
- Update of the `GDAL` library, which is used by the PostGIS
  extension. See [Managing spatial data with the PostGIS extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") in the
  _Amazon RDS User Guide_.
- Update of the `ip4r` extension to version 2.1.1.
- Update of the `pg_repack` extension to version 1.4.3. See
  [Working with the pg_repack extension](../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack "../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack") in the
  _Amazon RDS User Guide_.
- Update of the `plv8` extension to version 2.1.2.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

###### Note

The `tsearch2` extension is to be removed in the next major
release. We encourage customers still using pre-8.3 text search to migrate to
the equivalent built-in features. For more information about migrating, see the
[PostgreSQL documentation](https://www.postgresql.org/docs/9.6/static/textsearch-migration.html "https://www.postgresql.org/docs/9.6/static/textsearch-migration.html").

### PostgreSQL version 10.3 on Amazon RDS

(Deprecated)

PostgreSQL version 10.3 contains several bug fixes for issues in release 10. For
more information on the fixes in 10.3, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/10/static/release-10-3.html "http://www.postgresql.org/docs/10/static/release-10-3.html").

Version 2.1.0 of plv8 is now available. If you use plv8 and upgrade PostgreSQL to
a new plv8 version, you immediately take advantage of the new extension but the
catalog metadata doesn't reflect this fact. For the steps to synchronize your
catalog metadata with the new version of plv8, see [Upgrading PLV8](../UserGuide/CHAP_PostgreSQL.md#postgresql-versions-UpgradingPLv8 "../UserGuide/CHAP_PostgreSQL.md#postgresql-versions-UpgradingPLv8") in the _Amazon RDS User Guide_.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 10.1 on Amazon RDS

(Deprecated)

PostgreSQL version 10.1 contains several bug fixes for issues in release 10. For
more information on the fixes in 10.1, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/10/static/release-10-1.html "http://www.postgresql.org/docs/10/static/release-10-1.html") and the [PostgreSQL 10 community
announcement](https://www.postgresql.org/about/news/1786/ "https://www.postgresql.org/about/news/1786/").

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

PostgreSQL version 10.1 includes the following changes:

- Declarative table partitioning –
  PostgreSQL 10 adds table partitioning to SQL syntax and native tuple
  routing.
- Parallel queries – When you create a
  new PostgreSQL 10.1 instance, parallel queries are enabled for the
  `default.postgres10` parameter group. The parameter [max_parallel_workers_per_gather](https://www.postgresql.org/docs/10/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER "https://www.postgresql.org/docs/10/static/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER") is set to 2 by default, but you
  can modify it to support your specific workload requirements.
- Support for the international components for unicode
  (ICU) – You can use the ICU library to provide
  explicitly versioned collations. Amazon RDS for PostgreSQL 10.1 is compiled with
  ICU version 60.2. For more information about ICU implementation in
  PostgreSQL, see [Collation
  support](https://www.postgresql.org/docs/10/static/collation.html "https://www.postgresql.org/docs/10/static/collation.html").
- Huge pages – Huge pages is a feature
  of the Linux kernel that uses multiple page size capabilities of modern
  hardware architectures. Amazon RDS for PostgreSQL supports huge pages with a
  global configuration parameter. When you create a new PostgreSQL 10.1
  instance with RDS, the `huge_pages` parameter is set to
  `"on"` for the `default.postgres10` parameter
  group. You can modify this setting to support your specific workload
  requirements.
- Extension plv8 update – plv8 is a
  procedural language that you can use to write functions in JavaScript that
  you can then call from SQL. This release of PostgreSQL supports version
  2.1.0 of plv8.
- Renaming of xlog and location – In
  PostgreSQL version 10 the abbreviation "xlog" has changed to "wal", and the
  term "location" has changed to "lsn". For more information, see [https://www.postgresql.org/docs/10/static/release-10.html#id-1.11.6.8.4](https://www.postgresql.org/docs/10/static/release-10.html#id-1.11.6.8.4 "https://www.postgresql.org/docs/10/static/release-10.html#id-1.11.6.8.4").
- tsearch2 extension – Amazon RDS continues
  to provide the `tsearch2` extension in PostgreSQL version 10, but
  is to remove it in the next major version release. If your application uses
  tsearch2 functions update it to use the equivalent functions the core engine
  provides. For more information see [tsearch2](https://www.postgresql.org/docs/9.6/static/tsearch2.html "https://www.postgresql.org/docs/9.6/static/tsearch2.html") in the PostgreSQL documentation.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

## PostgreSQL 9.6 versions (Deprecated)

###### Minor versions

- [PostgreSQL version 9.6.24 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9624 "#postgresql-versions-version9624")
- [PostgreSQL version 9.6.23 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9623 "#postgresql-versions-version9623")
- [PostgreSQL version 9.6.22 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9622 "#postgresql-versions-version9622")
- [PostgreSQL version 9.6.21 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9621 "#postgresql-versions-version9621")
- [PostgreSQL version 9.6.20 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9620 "#postgresql-versions-version9620")
- [PostgreSQL version 9.6.19 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9619 "#postgresql-versions-version9619")
- [PostgreSQL version 9.6.18 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9618 "#postgresql-versions-version9618")
- [PostgreSQL version 9.6.17 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9617 "#postgresql-versions-version9617")
- [PostgreSQL version 9.6.16 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9616 "#postgresql-versions-version9616")
- [PostgreSQL version 9.6.15 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9615 "#postgresql-versions-version9615")
- [PostgreSQL version 9.6.14 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9614 "#postgresql-versions-version9614")
- [PostgreSQL version 9.6.12 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9612 "#postgresql-versions-version9612")
- [PostgreSQL version 9.6.11 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9611 "#postgresql-versions-version9611")
- [PostgreSQL version 9.6.10 on Amazon RDS
  (Deprecated)](#postgresql-versions-version9610 "#postgresql-versions-version9610")
- [PostgreSQL version 9.6.9 on Amazon RDS
  (Deprecated)](#postgresql-versions-version969 "#postgresql-versions-version969")
- [PostgreSQL version 9.6.8 on Amazon RDS
  (Deprecated)](#postgresql-versions-version968 "#postgresql-versions-version968")
- [PostgreSQL version 9.6.6 on Amazon RDS
  (Deprecated)](#postgresql-versions-version966 "#postgresql-versions-version966")
- [PostgreSQL version 9.6.5 on Amazon RDS
  (Deprecated)](#postgresql-versions-version965 "#postgresql-versions-version965")
- [PostgreSQL version 9.6.3 on Amazon RDS
  (Deprecated)](#postgresql-versions-version963 "#postgresql-versions-version963")
- [PostgreSQL version 9.6.2 on Amazon RDS
  (Deprecated)](#postgresql-versions-version962 "#postgresql-versions-version962")
- [PostgreSQL version 9.6.1 on Amazon RDS
  (Deprecated)](#postgresql-versions-version961 "#postgresql-versions-version961")

### PostgreSQL version 9.6.24 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.24 is now available on Amazon RDS. PostgreSQL version 9.6.24
contains several improvements that were announced for PostgreSQL release [9.6.24](https://www.postgresql.org/docs/release/9.6.24/ "https://www.postgresql.org/docs/release/9.6.24/").

This version also includes the following change:

- The [pg_hint_plan](https://github.com/ossc-db/pg_hint_plan/ "https://github.com/ossc-db/pg_hint_plan/") extension is updated to 1.2.7.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.23 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.23 is now available on Amazon RDS. PostgreSQL version 9.6.23
contains several improvements that were announced for PostgreSQL release [9.6.23](https://www.postgresql.org/docs/release/9.6.23/ "https://www.postgresql.org/docs/release/9.6.23/").

This version also includes the following changes:

- The `pglogical` extension is updated to version 2.4.0.
- The [PostGIS](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") extension is updated to version 2.5.5, along with the
  following related extensions:
  - [address_standardizer](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [address_standardizer_data_us](https://postgis.net/docs/standardize_address.html "https://postgis.net/docs/standardize_address.html")
  - [PostGIS_tiger_geocoder](http://postgis.net/docs/Geocode.html "http://postgis.net/docs/Geocode.html")
  - [PostGIS_topology](http://postgis.net/docs/manual-dev/Topology.html "http://postgis.net/docs/manual-dev/Topology.html")

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.22 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.22 is now available on Amazon RDS. PostgreSQL version 9.6.22
contains several improvements that were announced for PostgreSQL release [9.6.22](https://www.postgresql.org/docs/release/9.6.22/ "https://www.postgresql.org/docs/release/9.6.22/").

This version also includes the following change:

- The [orafce](https://github.com/orafce/orafce "https://github.com/orafce/orafce") extension
  is updated to version 3.15.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.21 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.21 is now available on Amazon RDS. PostgreSQL version 9.6.21
contains several improvements that were announced for PostgreSQL release [9.6.21](https://www.postgresql.org/docs/release/9.6.21/ "https://www.postgresql.org/docs/release/9.6.21/").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.20 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.20 is now available on Amazon RDS. PostgreSQL version 9.6.20
contains several improvements that were announced for PostgreSQL release [9.6.20](https://www.postgresql.org/docs/9.6/release-9-6-20.html "https://www.postgresql.org/docs/9.6/release-9-6-20.html").

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.19 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.19 is now available on Amazon RDS. PostgreSQL version 9.6.19
contains several improvements that were announced for PostgreSQL release [9.6.19](https://www.postgresql.org/docs/9.6/release-9-6-19.html "https://www.postgresql.org/docs/9.6/release-9-6-19.html").

This version also includes the following changes:

- Upgraded the `pgaudit` extension to version 1.1.2
- Upgraded the `pglogical` extension to version 2.2.2
- Upgraded the `wal2json` extension to version 2.3

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.18 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.18 contains several bug fixes for issues in release 9.6.17.
For more information on the fixes in PostgreSQL 9.6.18, see the [PostgreSQL 9.6.18
documentation](https://www.postgresql.org/docs/9.6/release-9-6-18.html "https://www.postgresql.org/docs/9.6/release-9-6-18.html").

This version also includes the following change:

- Upgraded the `pg_hint_plan` extension to version 1.2.6.

For information on all extensions, see [Extensions supported for RDS for PostgreSQL 9.6](postgresql-extensions.md#postgresql-extensions-96x "postgresql-extensions.md#postgresql-extensions-96x") .

### PostgreSQL version 9.6.17 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.17 contains several bug fixes for issues in release 9.6.16.
For more information on the fixes in PostgreSQL 9.6.17, see the [PostgreSQL 9.6.17
documentation](https://www.postgresql.org/docs/9.6/release-9-6-17.html "https://www.postgresql.org/docs/9.6/release-9-6-17.html").

### PostgreSQL version 9.6.16 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.16 contains several bug fixes for issues in release 9.6.15.
For more information on the fixes in PostgreSQL 9.6.16, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/9.6/release-9-6-16.html "https://www.postgresql.org/docs/9.6/release-9-6-16.html").

### PostgreSQL version 9.6.15 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.15 contains several bug fixes for issues in release 9.6.14.
For more information on the fixes in PostgreSQL 9.6.15, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/9.6/release-9-6-15.html "https://www.postgresql.org/docs/9.6/release-9-6-15.html").

The `PostGIS` extension is updated to version 2.5.2.

### PostgreSQL version 9.6.14 on Amazon RDS

(Deprecated)

This release contains bug fixes and improvements done by the PostgreSQL community.

With this release, the `pg_hint_plan` extension has been updated to
version 1.2.5.

For more information on the fixes in PostgreSQL 9.6.14, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/9.6/release-9-6-14.html "https://www.postgresql.org/docs/9.6/release-9-6-14.html").

### PostgreSQL version 9.6.12 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.12 contains several bug fixes for issues in release 9.6.11.
For more information on the fixes in 9.6.12, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/release-9-6-12.html "http://www.postgresql.org/docs/9.6/release-9-6-12.html").

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

### PostgreSQL version 9.6.11 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.11 contains several bug fixes for issues in release 9.6.10.
For more information on the fixes in PostgreSQL 9.6.11, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-11.html "http://www.postgresql.org/docs/9.6/static/release-9-6-11.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

With this version, the logical decoding plugin `wal2json` has been
updated to commit `9e962ba`.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.10 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.10 contains several bug fixes for issues in release 9.6.9.
For more information on the fixes in 9.6.10, see the [PostgreSQL documentation](http://www.postgresql.org/docs/current/static/release-9-6-10.html "http://www.postgresql.org/docs/current/static/release-9-6-10.html").

This version includes the following changes:

- Support for the `pglogical` extension version 2.2.0.
  Prerequisites for using this extension are the same as the prerequisites for
  using logical replication for PostgreSQL as described in [Performing logical replication for Amazon RDS for PostgreSQL](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.LogicalReplication") in the
  _Amazon RDS User Guide_.
- Support for the `pg_similarity` extension version 2.2.0.
- An update for the `wal2json` extension to version
  01c5c1e.
- An update for the `pg_hint_plan` extension to version
  1.2.3.

For information on upgrading the engine version for your PostgreSQL DB instance,
see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.9 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.9 contains several bug fixes for issues in release 9.6.8.
For more information on the fixes in 9.6.9, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-9.html "http://www.postgresql.org/docs/9.6/static/release-9-6-9.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

This version includes the following changes:

- The temporary file size limitation is user-configurable. You require the
  **rds_superuser** role to modify the
  `temp_file_limit` parameter.
- Update of the `GDAL` library, which is used by the PostGIS
  extension. See [Working with the PostGIS extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md") in the
  _Amazon RDS User Guide_.
- Update of the `ip4r` extension to version 2.1.1.
- Update of the `pgaudit` extension to version 1.1.1. See [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit") in the _Amazon RDS User Guide_.

Update of the `pg_repack` extension to version 1.4.3. See
[Working with the pg_repack extension](../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack "../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack") in the
_Amazon RDS User Guide_.

- Update of the `plv8` extension to version 2.1.2.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.8 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.8 contains several bug fixes for issues in release 9.6.6.
For more information on the fixes in 9.6.8, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-8.html "http://www.postgresql.org/docs/9.6/static/release-9-6-8.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.6 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.6 contains several bug fixes for issues in release 9.6.5.
For more information on the fixes in 9.6.6, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-6.html "http://www.postgresql.org/docs/9.6/static/release-9-6-6.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

This version includes the following features:

- Supports the `orafce` extension, version 3.6.1. This extension
  contains functions that are native to commercial databases, and can be
  helpful if you are porting a commercial database to PostgreSQL. For more
  information about using `orafce` with Amazon RDS, see [Using functions from the orafce extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.orafce "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.orafce")in the
  _Amazon RDS User Guide_.
- Supports the `prefix` extension, version 1.2.6. This extension
  provides an operator for text prefix searches. For more information about
  `prefix`, see the [prefix project on
  GitHub](https://github.com/dimitri/prefix "https://github.com/dimitri/prefix").
- Supports version 2.3.4 of PostGIS, version 2.4.2 of [pgrouting](https://docs.pgrouting.org/latest/en/index.html "https://docs.pgrouting.org/latest/en/index.html"),
  and an updated version of wal2json.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.5 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.5 contains several bug fixes for issues in release 9.6.4.
For more information on the fixes in 9.6.5, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-5.html "http://www.postgresql.org/docs/9.6/static/release-9-6-5.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

This version also includes support for the [pgrouting](http://pgrouting.org/ "http://pgrouting.org/"), [postgresql-hll](https://github.com/citusdata/postgresql-hll/releases/tag/v2.10.2 "https://github.com/citusdata/postgresql-hll/releases/tag/v2.10.2") extensions, and the [decoder_raw](https://github.com/michaelpq/pg_plugins/tree/master/decoder_raw "https://github.com/michaelpq/pg_plugins/tree/master/decoder_raw") optional extension.

For the complete list of extensions supported by Amazon RDS for PostgreSQL, see [Extension versions for Amazon RDS for PostgreSQL](postgresql-extensions.md "postgresql-extensions.md").

### PostgreSQL version 9.6.3 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.3 contains several new features and bug fixes. This version
includes the following features:

- Supports the extension `pg_repack` version 1.4.0. You can use
  this extension to remove bloat from tables and indexes. For more information
  on using `pg_repack` with Amazon RDS, see [Reducing bloat in tables and indexes with the pg_repack
  extension](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.md#Appendix.PostgreSQL.CommonDBATasks.pg_repack") in the _Amazon RDS User Guide_.
- Supports the extension `pgaudit` version 1.1.0. This extension
  provides detailed session and object audit logging. For more information on
  using pgaudit with Amazon RDS, see [Logging at the session and object level with the pgaudit
  extension](../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit "../UserGuide/Appendix.PostgreSQL.md#Appendix.PostgreSQL.CommonDBATasks.pgaudit") in the _Amazon RDS User Guide_.
- Supports `wal2json`, an output plugin for logical
  decoding.
- Supports the `auto_explain` extension. You can use this
  extension to log execution plans of slow statements automatically. The
  following example shows how to use `auto_explain` from within an
  Amazon RDS PostgreSQL session:

```
LOAD '$libdir/plugins/auto_explain';
```

For more information on using `auto_explain`, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/static/auto-explain.html "https://www.postgresql.org/docs/current/static/auto-explain.html").

### PostgreSQL version 9.6.2 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.2 contains several new features and bug fixes. The new
version also includes the following extension versions:

- PostGIS version 2.3.2
- [pg_freespacemap](https://www.postgresql.org/docs/current/static/pgfreespacemap.html "https://www.postgresql.org/docs/current/static/pgfreespacemap.html") version 1.1–Provides a way to examine
  the free space map (FSM). This extension provides an overloaded function
  called pg_freespace. The functions show the value recorded in the free space
  map for a given page, or for all pages in the relation.
- [pg_hint_plan](http://pghintplan.osdn.jp/pg_hint_plan.html "http://pghintplan.osdn.jp/pg_hint_plan.html") version 1.1.3– Provides control of
  execution plans by using hinting phrases at the beginning of SQL
  statements.
- log_fdw version 1.0–Using this extension from Amazon RDS, you can load
  and query your database engine log from within the database. For more
  information, see [Using the log_fdw extension to access the DB log using SQL](../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#CHAP_PostgreSQL.Extensions.log_fdw "../UserGuide/Appendix.PostgreSQL.CommonDBATasks.Extensions.md#CHAP_PostgreSQL.Extensions.log_fdw") in
  the _Amazon RDS User Guide_.
- With this version release, you can now edit the
  `max_worker_processes` parameter in a DB parameter group.

PostgreSQL version 9.6.2 on Amazon RDS also supports altering enum values. For more
information, see [Custom data types and enumerations with RDS for PostgreSQL](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.AlterEnum "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.FeatureSupport.AlterEnum") in the
_Amazon RDS User Guide_.

For more information on the fixes in 9.6.2, see the [PostgreSQL
documentation](http://www.postgresql.org/docs/9.6/static/release-9-6-2.html "http://www.postgresql.org/docs/9.6/static/release-9-6-2.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

### PostgreSQL version 9.6.1 on Amazon RDS

(Deprecated)

PostgreSQL version 9.6.1 contains several new features and improvements. For more
information about the fixes and improvements in PostgreSQL 9.6.1, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/9.6/static/release-9-6-1.html "https://www.postgresql.org/docs/9.6/static/release-9-6-1.html"). For information on upgrading the engine version for your
PostgreSQL DB instance, see [Upgrading the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_. For information about performing parallel
queries and phrase searching using Amazon RDS for PostgreSQL 9.6.1, see the [AWS Database Blog](https://aws.amazon.com/blogs/database/performing-parallel-queries-and-phrase-searching-with-amazon-rds-for-postgresql-9-6-1/ "https://aws.amazon.com/blogs/database/performing-parallel-queries-and-phrase-searching-with-amazon-rds-for-postgresql-9-6-1/").

PostgreSQL version 9.6.1 includes the following changes:

- **Parallel query processing**: Supports
  parallel processing of large read-only queries, allowing sequential scans,
  hash joins, nested loops, and aggregates to be run in parallel. By default,
  parallel query processing isn't enabled. To enable parallel query
  processing, set the parameter `max_parallel_workers_per_gather`
  to a value larger than zero.

- **Updated postgres_fdw extension**: Supports
  remote JOINs, SORTs, UPDATEs, and DELETE operations.
- **plv8 update**: Provides version 1.5.3 of
  the plv8 language.
- **PostGIS version update**: Supports
  POSTGIS="2.3.0 r15146" GEOS="3.5.0-CAPI-1.9.0 r4084" PROJ="Rel. 4.9.2, 08
  September 2015" GDAL="GDAL 2.1.1, released 2016/07/07" LIBXML="2.9.1"
  LIBJSON="0.12" RASTER

- **Vacuum improvement**: Avoids scanning pages
  unnecessarily during vacuum freeze operations.

- **Full-text search support for phrases**:
  Supports the ability to specify a phrase-search query in tsquery input using
  the new operators <-> and <N>.

- **Two new extensions are supported**:
  - `bloom`, an index access method based on [Bloom
    filters](http://en.wikipedia.org/wiki/Bloom_filter "http://en.wikipedia.org/wiki/Bloom_filter")
  - `pg_visibility`, which provides a means for examining
    the visibility map and page-level visibility information of a
    table.

- With the release of version 9.6.2, you can now edit the
  `max_worker_processes` parameter in a PostgreSQL version
  9.6.1 DB parameter group.

## Deprecation of

PostgreSQL 10

On April 17, 2023, Amazon RDS deprecated PostgreSQL 10. For more information, see [Deprecation of PostgreSQL version 10](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.DBVersions.Deprecation10 "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.DBVersions.Deprecation10") in the
_Amazon RDS User Guide_. We strongly recommend that you take action as
soon as possible and upgrade your PostgreSQL databases running on major version 10 to a
later major version, such as version 14. For information about how to do so, see [Upgrading
the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.

## Deprecation of

PostgreSQL 9.6

On March 31, 2022, Amazon RDS deprecated PostgreSQL 9.6. This extended the previously
announced date of January 18, 2022 to April 26, 2022. For more information, see [Deprecation of PostgreSQL version 9.6](../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.DBVersions.Deprecation96 "../UserGuide/CHAP_PostgreSQL.md#PostgreSQL.Concepts.General.DBVersions.Deprecation96") in the
_Amazon RDS User Guide_. We strongly recommend that you upgrade all
your PostgreSQL 9.6 DB instances to PostgreSQL 12 or higher as soon as possible. For
information about how to do so, see [Upgrading
the PostgreSQL DB engine for Amazon RDS](../UserGuide/USER_UpgradeDBInstance.md "../UserGuide/USER_UpgradeDBInstance.md") in the
_Amazon RDS User Guide_.
