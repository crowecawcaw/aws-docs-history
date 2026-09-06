

# Amazon Aurora PostgreSQL Limitless Database updates
<a name="limitless-updates"></a>

Here you can find information about versions of Amazon Aurora PostgreSQL Limitless Database. Limitless Database provides automated horizontal scaling to process millions of write transactions per second and manages petabytes of data while maintaining the simplicity of operating inside a single database. With Limitless Database, you can focus on building high-scale applications without having to build and maintain complex solutions for scaling your data across multiple DB instances to support your workloads.

For more information, see [Using Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) in the *Amazon Aurora User Guide*.

Amazon Amazon Aurora PostgreSQL Limitless Database follows the same engine version lifecycle policy as Aurora PostgreSQL. For more information, see [Release calendars for Aurora PostgreSQL](aurorapostgresql-release-calendar.md).

**Topics**
+ [Amazon Aurora PostgreSQL Limitless Database version 16.13-limitless](#16.13-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.11-limitless](#16.11-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.10-limitless](#16.10-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.9-limitless](#16.9-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.8-limitless](#16.8-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.6-limitless](#16.6-limitless)
+ [Amazon Aurora PostgreSQL Limitless Database version 16.4-limitless](#16.4-limitless)

## Amazon Aurora PostgreSQL Limitless Database version 16.13-limitless
<a name="16.13-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.13](https://www.postgresql.org/docs/release/16.13/). For more information about the improvements in PostgreSQL 16.13, see [ Aurora PostgreSQL 16.13](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version1613x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.13.102, September 3, 2026](#16.13.102)
+ [Aurora PostgreSQL Limitless Database 16.13.101, July 13, 2026](#16.13.101)
+ [Aurora PostgreSQL Limitless Database 16.13.100, April 25, 2026](#16.13.100)

### Aurora PostgreSQL Limitless Database 16.13.102, September 3, 2026
<a name="16.13.102"></a>

**Bug fixes**
+ Fixed a distributed deadlock between `GRANT` or `REVOKE` on a table and concurrent reads or writes of the same table.
+ Fixed an issue where a node in a shard group could repeatedly restart while recovering an in-progress distributed transaction due to OID mismatch for database object. This made the node unavailable and required manual intervention.
+ Fixed an issue where, in rare cases, a router continued using outdated writer information after a failover. Write requests routed through that router were rejected.

### Aurora PostgreSQL Limitless Database 16.13.101, July 13, 2026
<a name="16.13.101"></a>

**Bug fixes**
+ Fixed an issue with fast-path locking that might cause increased LWLock:LockManager contention.

### Aurora PostgreSQL Limitless Database 16.13.100, April 25, 2026
<a name="16.13.100"></a>

**Features**
+ Added support for batch `INSERT`, `UPDATE`, and `DELETE` operations with `RETURNING` clause.
+ Added a virtual function to show whether a prepared transaction is detached.

**Enhancements**
+ Improved performance for single-statement transactions using the extended query protocol.
+ Improved read performance with future commit time optimization for time-based MVCC readers.
+ Improved performance for single-shard `SELECT` queries by fetching all result rows at once instead of in batches. This optimization is enabled by default and can be controlled with the `rds_aurora.limitless_fetch_all` parameter.
+ Improved distributed transaction performance by enabling two-phase commit backend affinity by default.
+ Improved performance of multi-row `INSERT` statements with `RETURNING` clause by enabling batch insert optimization when the `RETURNING` list consists of `*` and column references.
+ Reduced commit log extension spikes through proactive segment extension.

**Bug fixes**
+ Fixed an issue where `SELECT` queries crashed when a sharded table attribute was referenced in a function.
+ Fixed an issue where calling `nextval` on a sequence inside an explicit transaction blocked concurrent `nextval` calls on the same sequence when the call triggered a chunk refresh. The refresh held an `AccessExclusiveLock` on the sequence until the parent transaction ended, rather than releasing it when the chunk update completed.
+ Fixed a crash caused by SIMD alignment.
+ Fixed an issue where queries hung indefinitely when retrieving results from shard nodes under certain connection conditions.
+ Fixed an issue where client and database connections weren't properly reset on RPC connection timeout and broken connections.
+ Fixed an issue where `DROP DATABASE` with `FORCE` option intermittently failed with `database is being accessed by other users`.
+ Reduced distributed deadlocks generated by autovacuum with table `DDL` operations.
+ Fixed an issue where `CREATE SEQUENCE` failed with `not enough values to create distributed sequence` when using a narrow sequence range (such as the `smallint` type or a small `MAXVALUE`) with an `INCREMENT BY` value greater than 1. The automatic chunk size adjustment didn't account for the increment value, so it couldn't shrink the chunk size enough to fit the sequence range.

## Amazon Aurora PostgreSQL Limitless Database version 16.11-limitless
<a name="16.11-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.11](https://www.postgresql.org/docs/release/16.11/). For more information about the improvements in PostgreSQL 16.11, see [ Aurora PostgreSQL 16.11](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version1611x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.11.102, September 1, 2026](#16.11.102)
+ [Aurora PostgreSQL Limitless Database 16.11.101, June 9, 2026](#16.11.101)
+ [Aurora PostgreSQL Limitless Database 16.11.100, February 25, 2026](#16.11.100)

### Aurora PostgreSQL Limitless Database 16.11.102, September 1, 2026
<a name="16.11.102"></a>

**Bug fixes**
+ Fixed a distributed deadlock between `GRANT` or `REVOKE` on a table and concurrent reads or writes of the same table.
+ Fixed an issue where a node in a shard group could repeatedly restart while recovering an in-progress distributed transaction due to OID mismatch for database object. This made the node unavailable and required manual intervention.
+ Fixed an issue where, in rare cases, a router continued using outdated writer information after a failover. Write requests routed through that router were rejected.
+ Fixed an issue where queries hung indefinitely when retrieving results from a shard node. This occurred after the connection to that node was reset or stopped responding.
+ Fixed an issue where errors returned when requesting a new chunk for a global sequence were misclassified. A sequence that reached its last value was reported as a connection failure. A transient failure could also stop `nextval` from returning new values.

### Aurora PostgreSQL Limitless Database 16.11.101, June 9, 2026
<a name="16.11.101"></a>

**Bug fixes**
+ Fixed an issue where a unique index did not guarantee uniqueness when created with a custom operator class.
+ Fixed an issue where `DROP DATABASE` with `FORCE` option failed with `database is being accessed by other users`.
+ Fixed an issue where cross-node version mismatch occurred after upgrade due to stale cached extension version.

### Aurora PostgreSQL Limitless Database 16.11.100, February 25, 2026
<a name="16.11.100"></a>

**Features**
+ Added support for `ALTER VIEW ... OWNER TO ...` statements.
+ Added support for `pg_prewarm` extension.

**Enhancements**
+ Enhanced `EXPLAIN` output for `INSERT INTO` with `SELECT` statements.
+ Enhanced query performance for `ENUM` usage.
+ Enhanced error messaging for `INSERT INTO` statements. The messaging now points out values where it failed.

**Bug fixes**
+ Fixed an issue where `SELECT` statements deadlocked when sharded table attribute was referenced in a function and joined.
+ Fixed `UNIQUE` and `PRIMARY KEY` constraints when used with `INCLUDE` clause where all columns (both constraint and included columns) have been incorrectly treated. This caused the index structure to differ from the original table definition.

## Amazon Aurora PostgreSQL Limitless Database version 16.10-limitless
<a name="16.10-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.10](https://www.postgresql.org/docs/release/16.10/). For more information about the improvements in PostgreSQL 16.10, see [ Aurora PostgreSQL 16.10](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version1610x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.10.101](#16.10.101)
+ [Aurora PostgreSQL Limitless Database 16.10.100, February 24, 2026](#16.10.100)

### Aurora PostgreSQL Limitless Database 16.10.101
<a name="16.10.101"></a>

**Enhancements**
+ Enhanced `EXPLAIN` output for `INSERT INTO` with `SELECT`.

**Bug fixes**
+ Fixed a crash when joining a table with a set-returning function that references the table's columns.
+ Fixed a crash caused by SIMD alignment issues with generic wrapper functions.

### Aurora PostgreSQL Limitless Database 16.10.100, February 24, 2026
<a name="16.10.100"></a>

**Features**
+ Added support for ENUM as shard key type.
+ Added support for `CHECK` constraints involving literals as well as expressions. For more information, see [Constraints](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DDL-limitations.html#limitless-reference.DDL-limitations.Constraints).
+ Added support for `VIEW`s with foreign key constraints. For more information, see [Foreign keys](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-reference.DDL-limitations.html#limitless-reference.DDL-limitations.FKs).
+ Added support for Advisory Locks. For more information, see [Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html#ADVISORY-LOCKS) in the PostgreSQL documentation.
+ Added support for `pg_dump` and `pg_restore` for database migrations. You can dump from Aurora Limitless databases and restore to other Aurora Limitless clusters or regular PostgreSQL databases. This support includes preservation of sharded and reference table configurations when migrating between Aurora Limitless clusters using metadata capture functions. For more information, see [Backing up and restoring Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless-bak.html).

**Enhancements**
+ Improved performance for schema and table lookups.
+ Improved performance for shard split.
+ Improved performance for `INSERT INTO` and `UPDATE` queries.

**Bug fixes**
+ Fixed an issue with privilege grants which failed with `invalid role OID: 0` when all privileges are `GRANT`ed to public.
+ Fixed an issue with `EXPLAIN` and `UPDATE` queries which failed with `wrong number of parameters for prepared statement`.
+ Fixed an issue with `CREATE TABLE` which failed with `duplicate key value violates unique constraint`.
+ Fixed an issue where database remained unusable after `DROP DATABASE` through JDBC.
+ Fixed an issue with `UPDATE` queries on distributed tables which failed with `relation * does not exist`.
+ Fixed an issue with `SELECT` queries with type casts which failed with `cannot cast type cstring to text[]`.
+ Fixed an issue with `CREATE DATABASE` which failed with `connection_limit requires an integer value` when also setting `connection_limit`.
+ Fixed table transformation from standard table to distributed table or reference table to keep Row Level Security Policies.
+ Fixed correctness and data leak issues in Row Level Security (RLS) policies. We recommend to drop and re-create any existing RLS policies.
+ Fixed `DROP POLICY` statement when used with `IF EXISTS`.
+ Fixed incorrect result when selecting `tableoid` system column. The `tableoid` is the OID of the table, which is a distinct identification given to the database object by a given system. If the query is eligible for Single Shard Optimization, the `tableoid` will be obtained from the Shard. Otherwise, the `tableoid` will be obtained from the connected router. Different routers may result in different `tableoid` for the same query.
+ Fixed stats update for tables with User Defined Types.
+ Fixed an issue with `CREATE TABLE` which failed with `FATAL: Unexpected error occurred while committing transaction` when `debug_parallel_query` is set to `on`.

## Amazon Aurora PostgreSQL Limitless Database version 16.9-limitless
<a name="16.9-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.9](https://www.postgresql.org/docs/release/16.9/). For more information about the improvements in PostgreSQL 16.9, see [ Aurora PostgreSQL 16.9](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version169x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.9.103, February 11, 2026](#16.9.103)
+ [Aurora PostgreSQL Limitless Database 16.9.102, November 21, 2025](#16.9.102)
+ [Aurora PostgreSQL Limitless Database 16.9.101, November 6, 2025](#16.9.101)
+ [Aurora PostgreSQL Limitless Database 16.9.100, September 5, 2025](#16.9.100)

### Aurora PostgreSQL Limitless Database 16.9.103, February 11, 2026
<a name="16.9.103"></a>

**Enhancements**
+ Enhanced `EXPLAIN` output for `INSERT INTO` with `SELECT`.

**Bug fixes**
+ Fixed an issue where `SELECT` statements did not return when sharded table attribute was referenced in a function and joined.

### Aurora PostgreSQL Limitless Database 16.9.102, November 21, 2025
<a name="16.9.102"></a>

**Enhancements**
+ Improved performance for shard split.
+ Improved error messages when queries fail during (minor) upgrades due to inconsistent instance versions.

**Bug fixes**
+ Fixed an issue where database remained unusable after `DROP DATABASE` through JDBC.
+ Fixed an issue with privilege grants which failed with `invalid role OID: 0` when all privileges are `GRANT`ed to public.
+ Fixed an issue with `SELECT` queries with type casts which failed with `cannot cast type cstring to text[]`.
+ Fixed an issue with `CREATE DATABASE` which failed with `connection_limit requires an integer value` when also setting `connection_limit`.
+ Fixed table transformation from standard table to distributed table or reference table to keep Row Level Security Policies.
+ Fixed correctness and data leak issues in Row Level Security (RLS) policies. We recommend to drop and re-create any existing RLS policies.
+ Fixed `DROP POLICY` statement when used with `IF EXISTS`.
+ Fixed incorrect result when selecting `tableoid` system column. The `tableoid` is the OID of the table, which is a distinct identification given to the database object by a given system. If the query is eligible for Single Shard Optimization, the `tableoid` will be obtained from the Shard. Otherwise, the `tableoid` will be obtained from the connected router. Different routers may result in different `tableoid` for the same query.
+ Fixed an issue where internal processes were no longer working properly after revoking `CONNECT` privilege for internal system roles.
+ Fixed stats update for tables with User Defined Types.
+ Fixed one edge case in resolving prepared transaction.

### Aurora PostgreSQL Limitless Database 16.9.101, November 6, 2025
<a name="16.9.101"></a>

**Bug fixes**
+ Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
+ Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
+ Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.9.100, September 5, 2025
<a name="16.9.100"></a>

**Features**
+ Added support for `CREATE INDEX IF NOT EXISTS`.
+ Added support for SEQUENCES in the `pgstattuple` extension.
+ Added support for the hstore extension. Note that hstore columns cannot be used as shard keys in sharded tables.
+ Added support for the auto\_explain extension.

**Enhancements**
+ Reduced waiting period required between `DROP DATABASE` and `CREATE DATABASE` operations when using the same database name.
+ Improved performance for `DELETE` and `UPDATE` operations involving semi-join and anti-join.
+ Improved performance for `INSERT INTO ... SELECT FROM` statements with expressions or projections that can be pushed down to shards
+ Improved error messages for detected deadlocks with involved queries listed in the **DETAIL** section.

**Bug fixes**
+ Fixed an issue where the background worker pool could be completely exhausted by database internal processes.
+ Fixed an issue where non-immutable functions in extensions unexpectedly failed with *permission denied* errors.
+ Fixed *commit time is invalid* errors.
+ Fixed an issue where `INSERT INTO` failed after the `ROLLBACK` of a `READ ONLY` transaction with the error ERROR: failed to execute remote query with message: transaction read-write mode must be set before any query.
+ Fixed an issue where `SELECT` queries failed with ERROR: failed to execute remote query with message: collations are not supported by type integer.
+ Fixed an issue where `DELETE FROM` failed with ERROR: failed to execute remote query.
+ Fixed an issue where expressions in `DEFAULT/CHECK` constraints might generate incorrect backfill data for existing rows. This issue is seen specifically when the expression in the constraint relies on parenthesis.
+ Fixed an issue with `PREPARE` and `EXECUTE` statements which failed with bind message supplies 2 parameters, but prepared statement requires 1 when the `PREPARE` statement used fewer parameters than it declared. 
+ Fixed an issue where `RESET` of `rds_aurora.limitless_explain_options` setting was not correctly reflected in `EXPLAIN` output.

## Amazon Aurora PostgreSQL Limitless Database version 16.8-limitless
<a name="16.8-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.8](https://www.postgresql.org/docs/release/16.8/). For more information about the improvements in PostgreSQL 16.8, see [ Aurora PostgreSQL 16.8](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version168x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.8.104, May 12, 2026](#16.8.104)
+ [Aurora PostgreSQL Limitless Database 16.8.103, October 30, 2025](#16.8.103)
+ [Aurora PostgreSQL Limitless Database 16.8.102, October 13, 2025](#16.8.102)
+ [Aurora PostgreSQL Limitless Database 16.8.101, June 30, 2025](#16.8.101)
+ [Aurora PostgreSQL Limitless Database 16.8.100, May 8, 2025](#16.8.100)

### Aurora PostgreSQL Limitless Database 16.8.104, May 12, 2026
<a name="16.8.104"></a>

**Bug fixes**
+ Fixed a file descriptor leak in `rds_aurora_limitless_get_max_connections`.

### Aurora PostgreSQL Limitless Database 16.8.103, October 30, 2025
<a name="16.8.103"></a>

**Bug fixes**
+ Fixed an issue with privilege grants which failed with `invalid role OID: 0` when all privileges are `GRANT`ed to public.
+ Fixed an issue with `SELECT` queries with type casts which failed with `cannot cast type cstring to text[]`.
+ Fixed an issue with `CREATE DATABASE` which failed with `connection_limit requires an integer value` when also setting `connection_limit`.
+ Fixed incorrect result when selecting `tableoid` system column. The `tableoid` is the OID of the table, which is a distinct identification given to the database object by a given system. If the query is eligible for Single Shard Optimization, the `tableoid` will be obtained from the Shard. Otherwise, the `tableoid` will be obtained from the connected router. Different routers may result in different `tableoid` for the same query.
+ Fixed one edge case in resolving prepared transaction.

### Aurora PostgreSQL Limitless Database 16.8.102, October 13, 2025
<a name="16.8.102"></a>

**Bug fixes**
+ Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
+ Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
+ Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.8.101, June 30, 2025
<a name="16.8.101"></a>

**Enhancements**
+ Improved error messages for detected deadlocks, now listing the involved queries in the `DETAIL` section.
+ Added support for sub-query containing tableoid as target list.

**Bug fixes**
+ Fixed the `ANALYZE` SQL query result to also include foreign tables.
+ Fixed multiple issues which might lead to a database restart.
+ Fixed an issue with `PREPARE` and `EXECUTE` statements which failed incorrectly with bind message supplies 2 parameters, but prepared statement requires 1 when the `PREPARE` statement used less parameters than declared.
+ Fixed multiple issues in vacuum operations leading to increased space consumption.
+ Fixed an issue with `INSERT` statements after rolling back a `READ_ONLY` transaction.
+ Fixed an issue where `DELETE` statements with `RETURNING` clause fails.

### Aurora PostgreSQL Limitless Database 16.8.100, May 8, 2025
<a name="16.8.100"></a>

**Features**
+ Added support for the `ltree` extension. `ltree` datatype columns cannot be used as shard keys in sharded tables.
+ Added support for the `btree_gist` extension in Aurora PostgreSQL Limitless Database. Exclusion constraints using GIST index are not supported. For example, the following command is not supported: 

  ```
  CREATE TABLE zoo (
      cage INTEGER,
      animal TEXT,
      EXCLUDE USING GIST (cage WITH =, animal WITH <>)
  );
  ```

**Enhancements**
+ Improved query performance in these scenarios:
  + Queries with range clauses.
  + Multiple tuple access with different shard keys from same shard.
  + Delete and update operations involving semi- and anti-joins.
+ Enhanced async foreign scan nodes with prefetch capability.
+ Strengthened deadlock detection fault tolerance.

**Bug fixes**
+ Fixed an issue where database backends stopped responding to system signals, which could cause DROP DATABASE operations to hang.
+ Fixed a race condition in commit log (clog) background processing that causes *commit time is invalid* errors.
+ Fixed an issue that could cause unexpected crashes during automatic table analysis operations.

## Amazon Aurora PostgreSQL Limitless Database version 16.6-limitless
<a name="16.6-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.6](https://www.postgresql.org/docs/release/16.6/). For more information about the improvements in PostgreSQL 16.6, see [ Aurora PostgreSQL 16.6](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version166x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.6.103, October 13, 2025](#16.6.103)
+ [Aurora PostgreSQL Limitless Database 16.6.102, June 30, 2025](#16.6.102)
+ [Aurora PostgreSQL Limitless Database 16.6.101, April 17, 2025](#16.6.101)
+ [Aurora PostgreSQL Limitless Database 16.6.100, January 24, 2025](#16.6.100)

### Aurora PostgreSQL Limitless Database 16.6.103, October 13, 2025
<a name="16.6.103"></a>

**Bug fixes**
+ Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
+ Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
+ Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.6.102, June 30, 2025
<a name="16.6.102"></a>

**Enhancements**
+ Improved error messages for detected deadlocks now list the involved queries in the `DETAIL`.
+ Improved the distribute deadlock detection algorithm to be arbitrary resilient to network or node failures.
+ Added support for sub-query containing tableoid as target list.

**Bug fixes**
+ Fixed the `ANALYZE` SQL query result to include foreign tables.
+ Fixed multiple issues which might lead to a database restart.
+ Fixed an issue with `PREPARE` and `EXECUTE` statements which failed incorrectly with bind message supplies 2 parameters, but prepared statement requires 1 when the `PREPARE` statement uses less parameters than declared.
+ Fixed multiple issues in vacuum operations leading to increased space consumption.
+ Fixed an issue with `INSERT` statements after rolling back a `READ_ONLY` transaction.
+ Fixed an issue where `DELETE` statements with `RETURNING` clause failed.
+ Fixed cases where expressions in `DEFAULT`/`CHECK` constraints can generate incorrect results, specifically when the expression in the constraint relies on parenthesis for generating the correct result.

### Aurora PostgreSQL Limitless Database 16.6.101, April 17, 2025
<a name="16.6.101"></a>

This release includes Aurora PostgreSQL patches till [ 16.6.3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version1663x-1663).

**Bug fixes**
+ Fixed multiple issues that might lead to brief periods of unavailability.
+ Fixed a correctness issue when `limitless_minimum_adaptive_fetch_size` is set to lower than the default value (100).
+ Enhanced error handling for querying tableoid attribute of a relation in Aurora PostgreSQL Limitless Database, considering it might have different values across nodes in `DBShardGroup`.
+ Fixed a permission issue that can occur when using `rds_aurora.limitless_active_shard_key`. This resolves permission errors when retrieving data.
+ Fixed a race condition in clog background operation whcih may cause the client to recieve the *commit time is invalid* error.
+ Optimized execution of distributed functions with variable length shard key. Previously, routers performed distributed functions but they are performed locally now on a single shard as per shard key.
+ Fixed an error when executing `update/delete` on standard table joining reference tables.
+ Fixed an issue where any user could invoke specific internal limitless functions.
+ Fixed an issue that lead to incorrect rollback for subtransaction during node crash.
+ Fixed issues where expressions with nested parentheses in `DEFAULT/CHECK` constraints might generate incorrect results.

### Aurora PostgreSQL Limitless Database 16.6.100, January 24, 2025
<a name="16.6.100"></a>

**Features**
+ Aurora PostgreSQL Limitless Database now supports Aurora PostgreSQL version 16.6.
+ You can now install and use the `btree_gin` extension.
+ The `DISCARD` Data Manipulation Language (DML) command is supported.

**Enhancements**
+ Improved query performance with better pushdown capabilities for queries that include reference tables within subqueries. This enhancement optimizes query execution, potentially resulting in faster performance for complex queries involving reference table joins in subqueries.
+ Enhanced the error handling for `pg_advisory_lock`. Previously, attempts to use this unsupported feature didn't generate an explicit error message, potentially leading to unexpected behavior. Now, users will receive a clear error notification when attempting to use `pg_advisory_lock`, ensuring better clarity and preventing unintended consequences.

**Bug fixes**
+ Fixed an issue where certain `ALTER TABLE` and `CREATE TABLE` commands fail with the error: Unable to deparse the given statement.
+ Fixed an issue where an `ALTER TABLE` command with a `NOT NULL` or `DEFAULT` constraint fails when it contains functions unsafe to push down to shards (such as volatile functions), requiring backfilling data in existing rows.

**Known issues**
+ Setting the `rds_aurora.limitless_minimum_adaptive_fetch_size` variable can cause incorrect results.

## Amazon Aurora PostgreSQL Limitless Database version 16.4-limitless
<a name="16.4-limitless"></a>

 This version of Aurora PostgreSQL Limitless Database is compatible with [PostgreSQL 16.4](https://www.postgresql.org/docs/release/16.4/). For more information about the improvements in PostgreSQL 16.4, see [ Aurora PostgreSQL 16.4](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.Updates.html#aurorapostgresql-versions-version164x). 

**Topics**
+ [Aurora PostgreSQL Limitless Database 16.4.106, October 13, 2025](#16.4.106)
+ [Aurora PostgreSQL Limitless Database 16.4.105, April 17, 2025](#16.4.105)
+ [Aurora PostgreSQL Limitless Database 16.4.104, November 19, 2024](#16.4.104)
+ [Aurora PostgreSQL Limitless Database 16.4.103, October 31, 2024](#16.4.103)

### Aurora PostgreSQL Limitless Database 16.4.106, October 13, 2025
<a name="16.4.106"></a>

**Bug fixes**
+ Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
+ Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
+ Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.4.105, April 17, 2025
<a name="16.4.105"></a>

**Bug fixes**
+ Fixed multiple issues that could lead to brief periods of unavailability.
+ Fixed an issue resulting in incorrect results for anti-join queries containing a predicate on an outer relation.
+ Added pushdown capability for the following system functions:
  + `pg_char_to_encoding`
  + `pg_encoding_to_char`
  + `textanycat`
  + `anytextcat`
+ Enhanced error handling for `pg_advisory_lock` in Aurora PostgreSQL Limitless Database. With this change, you receive a clear error notification when attempting to use `pg_advisory_lock`.
+ Fixed an issue where adding an expression with nested parentheses in `DEFAULT/CHECK` constraints might generate incorrect results.

### Aurora PostgreSQL Limitless Database 16.4.104, November 19, 2024
<a name="16.4.104"></a>

**Bug fixes**
+ Fixed an issue where deadlocks can occur in processing Data Definition Language (DDL) statements when `CREATE INDEX CONCURRENTLY` runs.
+ Fixed an issue where an error in distributed deadlock resolution can block the detection of subsequent distributed deadlocks.
+ Fixed an issue where DDL statements with underlying Data Manipulation Language (DML) statements (such as `CREATE TABLE AS` or calling for a table with data) result in errors if the `rds_aurora.limitless_active_shard_key` variable is used in a session.
+ Fixed an issue where a shard split operation results in an error.
+ Fixed an issue where the `rds_aurora.limitless_alter_table_type_sharded` procedure for converting the table type to sharded fails if the `rds_aurora.limitless_alter_table_type_sharded` variable is set.
+ Fixed an issue in the deparsing logic of polymorphic objects that resulted in invalid queries not producing errors when the implicit cast of passing data caused incorrect object versions to be used.

**Known issues**
+ An issue can occur when part of a query is converted to a left or anti-join condition. In these cases, if the inner relation has no results a null row is used.
+ An issue can occur when adding a column with a `NOT NULL` or `DEFAULT` constraint, that contains functions unsafe to push down to shards (such as volatile functions), requires backfilling data in existing rows.
+ An issue can occur when the deparsing logic for preparing queries to shards doesn't use parentheses where possible. This can lead to errors when `COLLATE` is used in queries.

### Aurora PostgreSQL Limitless Database 16.4.103, October 31, 2024
<a name="16.4.103"></a>

Release 16.4.103 is the GA version of Aurora PostgreSQL Limitless Database.

For information on this release, see [Using Amazon Aurora PostgreSQL Limitless Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/limitless.html) in the *Amazon Aurora User Guide*.