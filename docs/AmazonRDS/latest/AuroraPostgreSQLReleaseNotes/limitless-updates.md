# Amazon Aurora PostgreSQL Limitless Database updates

Here you can find information about versions of Amazon Aurora PostgreSQL Limitless Database. Limitless Database provides automated horizontal scaling to process millions of write
transactions per second and manages petabytes of data while maintaining the simplicity of operating inside a single database. With Limitless Database, you
can focus on building high-scale applications without having to build and maintain complex solutions for scaling your data across multiple DB instances
to support your workloads.

For more information, see [Using Amazon Aurora PostgreSQL Limitless Database](../AuroraUserGuide/limitless.md "../AuroraUserGuide/limitless.md") in the
_Amazon Aurora User Guide_.

Amazon Amazon Aurora PostgreSQL Limitless Database follows the same engine version lifecycle policy as Aurora PostgreSQL. For more information, see [Release calendars for Aurora PostgreSQL](aurorapostgresql-release-calendar.md "aurorapostgresql-release-calendar.md").

###### Topics

- [Amazon Aurora PostgreSQL Limitless Database version 16.9-limitless](#16.9-limitless "#16.9-limitless")
- [Amazon Aurora PostgreSQL Limitless Database version 16.8-limitless](#16.8-limitless "#16.8-limitless")
- [Amazon Aurora PostgreSQL Limitless Database version 16.6-limitless](#16.6-limitless "#16.6-limitless")
- [Amazon Aurora PostgreSQL Limitless Database version 16.4-limitless](#16.4-limitless "#16.4-limitless")

## Amazon Aurora PostgreSQL Limitless Database version 16.9-limitless

This version of Aurora PostgreSQL Limitless Database is compatible with PostgreSQL 16.9. For more information about the improvements in PostgreSQL 16.9, see
[PostgreSQL release 16.9](https://www.postgresql.org/docs/release/16.9/ "https://www.postgresql.org/docs/release/16.9/").

###### Releases and patches

- [Aurora PostgreSQL Limitless Database 16.9.102, November 21, 2025](#16.9.102 "#16.9.102")
- [Aurora PostgreSQL Limitless Database 16.9.101, November 6, 2025](#16.9.101 "#16.9.101")
- [Aurora PostgreSQL Limitless Database 16.9.100, September 5, 2025](#16.9.100 "#16.9.100")

### Aurora PostgreSQL Limitless Database 16.9.102, November 21, 2025

**Enhancements**

- Improved performance for shard split.
- Improved error messages when queries fail during (minor) upgrades due to inconsistent instance versions.

**Bug fixes**

- Fixed an issue where database remained unusable after `DROP DATABASE` through JDBC.
- Fixed an issue with privilege grants which failed with `invalid role OID: 0` when all privileges are `GRANT`ed to public.
- Fixed an issue with `SELECT` queries with type casts which failed with `cannot cast type cstring to text[]`.
- Fixed an issue with `CREATE DATABASE` which failed with `connection_limit requires an integer value` when also setting `connection_limit`.
- Fixed table transformation from standard table to distributed table or reference table to keep Row Level Security Policies.
- Fixed correctness and data leak issues in Row Level Security (RLS) policies. We recommend to drop and re-create any existing RLS policies.
- Fixed `DROP POLICY` statement when used with `IF EXISTS`.
- Fixed incorrect result when selecting `tableoid` system column. The `tableoid` is the OID of the table, which is a distinct identification given to the database object by a given system. If the query is eligible for Single Shard Optimization, the `tableoid` will be obtained from the Shard. Otherwise, the `tableoid` will be obtained from the connected router. Different routers may result in different `tableoid` for the same query.
- Fixed an issue where internal processes were no longer working properly after revoking `CONNECT` privilege for internal system roles.
- Fixed stats update for tables with User Defined Types.
- Fixed one edge case in resolving prepared transaction.

### Aurora PostgreSQL Limitless Database 16.9.101, November 6, 2025

**Bug fixes**

- Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
- Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
- Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.9.100, September 5, 2025

**Features**

- Added support for `CREATE INDEX IF NOT EXISTS`.
- Added support for SEQUENCES in the `pgstattuple` extension.
- Added support for the hstore extension. Note that hstore columns cannot be used as shard keys in sharded tables.
- Added support for the auto_explain extension.

**Enhancements**

- Reduced waiting period required between `DROP DATABASE`
  and `CREATE DATABASE` operations when using the same database name.
- Improved performance for `DELETE` and `UPDATE` operations involving semi-join and anti-join.
- Improved performance for `INSERT INTO ... SELECT FROM` statements with expressions or projections that can be pushed down to shards
- Improved error messages for detected deadlocks with involved queries listed in the **DETAIL** section.

**Bug fixes**

- Fixed an issue where the background worker pool could be completely exhausted by database internal processes.
- Fixed an issue where non-immutable functions in extensions
  unexpectedly failed with _permission denied_ errors.
- Fixed _commit time is invalid_ errors.
- Fixed an issue where `INSERT INTO` failed after the
  `ROLLBACK` of a `READ ONLY` transaction with the error
  **`ERROR: failed to execute remote query with message: transaction
read-write mode must be set before any query`**.
- Fixed an issue where `SELECT` queries failed with
  **`ERROR: failed to execute remote query with message: collations
are not supported by type integer`**.
- Fixed an issue where `DELETE FROM` failed with
  **`ERROR: failed to execute remote query`**.
- Fixed an issue where expressions in `DEFAULT/CHECK` constraints
  might generate incorrect backfill data for existing rows. This issue is seen
  specifically when the expression in the constraint relies on parenthesis.
- Fixed an issue with `PREPARE` and `EXECUTE`
  statements which failed with **`bind message supplies 2 parameters, but 
prepared statement requires 1`** when the `PREPARE` statement used fewer parameters than it
  declared.
- Fixed an issue where `RESET` of
  `rds_aurora.limitless_explain_options` setting was not correctly
  reflected in `EXPLAIN` output.

## Amazon Aurora PostgreSQL Limitless Database version 16.8-limitless

This version of Aurora PostgreSQL Limitless Database is compatible with PostgreSQL 16.8. For more information about the improvements in PostgreSQL 16.8, see
[PostgreSQL release 16.8](https://www.postgresql.org/docs/16/release-16-8.html "https://www.postgresql.org/docs/16/release-16-8.html").

###### Releases and patches

- [Aurora PostgreSQL Limitless Database 16.8.103, October 30, 2025](#16.8.103 "#16.8.103")
- [Aurora PostgreSQL Limitless Database 16.8.102, October 13, 2025](#16.8.102 "#16.8.102")
- [Aurora PostgreSQL Limitless Database 16.8.101, June 30, 2025](#16.8.101 "#16.8.101")
- [Aurora PostgreSQL Limitless Database 16.8.100, May 8, 2025](#16.8.100 "#16.8.100")

### Aurora PostgreSQL Limitless Database 16.8.103, October 30, 2025

**Bug fixes**

- Fixed an issue with privilege grants which failed with `invalid role OID: 0` when all privileges are `GRANT`ed to public.
- Fixed an issue with `SELECT` queries with type casts which failed with `cannot cast type cstring to text[]`.
- Fixed an issue with `CREATE DATABASE` which failed with `connection_limit requires an integer value` when also setting `connection_limit`.
- Fixed incorrect result when selecting `tableoid` system column. The `tableoid` is the OID of the table, which is a distinct identification given to the database object by a given system. If the query is eligible for Single Shard Optimization, the `tableoid` will be obtained from the Shard. Otherwise, the `tableoid` will be obtained from the connected router. Different routers may result in different `tableoid` for the same query.
- Fixed one edge case in resolving prepared transaction.

### Aurora PostgreSQL Limitless Database 16.8.102, October 13, 2025

**Bug fixes**

- Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
- Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
- Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.8.101, June 30, 2025

**Enhancements**

- Improved error messages for detected deadlocks, now listing the involved queries in the `DETAIL` section.
- Added support for sub-query containing tableoid as target list.

**Bug fixes**

- Fixed the `ANALYZE` SQL query result to also include foreign tables.
- Fixed multiple issues which might lead to a database restart.
- Fixed an issue with `PREPARE` and `EXECUTE` statements which failed incorrectly with
  **`bind message supplies 2 parameters, but prepared statement requires 1`**
  when the `PREPARE` statement used less parameters than declared.
- Fixed multiple issues in vacuum operations leading to increased space consumption.
- Fixed an issue with `INSERT` statements after rolling back a `READ_ONLY` transaction.
- Fixed an issue where `DELETE` statements with `RETURNING` clause fails.

### Aurora PostgreSQL Limitless Database 16.8.100, May 8, 2025

**Features**

- Added support for the `ltree` extension. `ltree` datatype columns cannot be used as shard keys in sharded tables.
- Added support for the `btree_gist` extension in Aurora PostgreSQL Limitless Database.
  Exclusion constraints using GIST index are not supported. For example, the following command is not supported:

```
CREATE TABLE zoo (
    cage INTEGER,
    animal TEXT,
    EXCLUDE USING GIST (cage WITH =, animal WITH <>)
);
```

**Enhancements**

- Improved query performance in these scenarios:
  - Queries with range clauses.
  - Multiple tuple access with different shard keys from same shard.
  - Delete and update operations involving semi- and anti-joins.

- Enhanced async foreign scan nodes with prefetch capability.
- Strengthened deadlock detection fault tolerance.

**Bug fixes**

- Fixed an issue where database backends stopped responding to system signals, which could cause DROP DATABASE operations to hang.
- Fixed a race condition in commit log (clog) background processing that causes _commit time is invalid_ errors.
- Fixed an issue that could cause unexpected crashes during automatic table analysis operations.

## Amazon Aurora PostgreSQL Limitless Database version 16.6-limitless

This version of Aurora PostgreSQL Limitless Database is compatible with PostgreSQL 16.6. For more information about the improvements in PostgreSQL 16.6, see
[PostgreSQL release 16.6](https://www.postgresql.org/docs/16/release-16-6.html "https://www.postgresql.org/docs/16/release-16-6.html").

###### Releases and patches

- [Aurora PostgreSQL Limitless Database 16.6.103, October 13, 2025](#16.6.103 "#16.6.103")
- [Aurora PostgreSQL Limitless Database 16.6.102, June 30, 2025](#16.6.102 "#16.6.102")
- [Aurora PostgreSQL Limitless Database 16.6.101, April 17, 2025](#16.6.101 "#16.6.101")
- [Aurora PostgreSQL Limitless Database 16.6.100, January 24, 2025](#16.6.100 "#16.6.100")

### Aurora PostgreSQL Limitless Database 16.6.103, October 13, 2025

**Bug fixes**

- Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
- Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
- Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.6.102, June 30, 2025

**Enhancements**

- Improved error messages for detected deadlocks now list the involved queries in the `DETAIL`.
- Improved the distribute deadlock detection algorithm to be arbitrary resilient to network or node failures.
- Added support for sub-query containing tableoid as target list.

**Bug fixes**

- Fixed the `ANALYZE` SQL query result to include foreign tables.
- Fixed multiple issues which might lead to a database restart.
- Fixed an issue with `PREPARE` and `EXECUTE` statements which failed incorrectly
  with **`bind message supplies 2 parameters, but prepared statement requires 1`** when
  the `PREPARE` statement uses less parameters than declared.
- Fixed multiple issues in vacuum operations leading to increased space consumption.
- Fixed an issue with `INSERT` statements after rolling back a `READ_ONLY` transaction.
- Fixed an issue where `DELETE` statements with `RETURNING` clause failed.
- Fixed cases where expressions in `DEFAULT`/`CHECK` constraints can generate incorrect results,
  specifically when the expression in the constraint relies on parenthesis for generating the correct result.

### Aurora PostgreSQL Limitless Database 16.6.101, April 17, 2025

This release includes Aurora PostgreSQL patches till
[16.6.3](AuroraPostgreSQL.md#aurorapostgresql-versions-version1663x-1663 "AuroraPostgreSQL.md#aurorapostgresql-versions-version1663x-1663").

**Bug fixes**

- Fixed multiple issues that might lead to brief periods of unavailability.
- Fixed a correctness issue when `limitless_minimum_adaptive_fetch_size` is set to lower than the default value (100).
- Enhanced error handling for querying tableoid attribute of a relation in Aurora PostgreSQL Limitless Database,
  considering it might have different values across nodes in `DBShardGroup`.
- Fixed a permission issue that can occur when using `rds_aurora.limitless_active_shard_key`.
  This resolves permission errors when retrieving data.
- Fixed a race condition in clog background operation whcih may cause the client to recieve the _commit time is invalid_ error.
- Optimized execution of distributed functions with variable length shard key.
  Previously, routers performed distributed functions but they are performed locally now on a single shard as per shard key.
- Fixed an error when executing `update/delete` on standard table joining reference tables.
- Fixed an issue where any user could invoke specific internal limitless functions.
- Fixed an issue that lead to incorrect rollback for subtransaction during node crash.
- Fixed issues where expressions with nested parentheses in `DEFAULT/CHECK` constraints might generate incorrect results.

### Aurora PostgreSQL Limitless Database 16.6.100, January 24, 2025

**Features**

- Aurora PostgreSQL Limitless Database now supports Aurora PostgreSQL version 16.6.
- You can now install and use the `btree_gin` extension.
- The `DISCARD` Data Manipulation Language (DML) command is supported.

**Enhancements**

- Improved query performance with better pushdown capabilities for queries that include reference tables within subqueries. This enhancement
  optimizes query execution, potentially resulting in faster performance for complex queries involving reference table joins in subqueries.
- Enhanced the error handling for `pg_advisory_lock`. Previously, attempts to use this unsupported feature didn't generate an explicit
  error message, potentially leading to unexpected behavior. Now, users will receive a clear error notification when attempting to use
  `pg_advisory_lock`, ensuring better clarity and preventing unintended consequences.

**Bug fixes**

- Fixed an issue where certain `ALTER TABLE` and `CREATE TABLE` commands fail with the error: **`Unable to deparse the
given statement`**.
- Fixed an issue where an `ALTER TABLE` command with a `NOT NULL` or `DEFAULT` constraint fails when it contains
  functions unsafe to push down to shards (such as volatile functions), requiring backfilling data in existing rows.

**Known issues**

- Setting the `rds_aurora.limitless_minimum_adaptive_fetch_size` variable can cause incorrect results.

## Amazon Aurora PostgreSQL Limitless Database version 16.4-limitless

This version of Aurora PostgreSQL Limitless Database is compatible with PostgreSQL 16.4. For more information about the improvements in PostgreSQL 16.4, see
[PostgreSQL release 16.4](https://www.postgresql.org/docs/16/release-16-4.html "https://www.postgresql.org/docs/16/release-16-4.html").

###### Releases and patches

- [Aurora PostgreSQL Limitless Database 16.4.106, October 13, 2025](#16.4.106 "#16.4.106")
- [Aurora PostgreSQL Limitless Database 16.4.105, April 17, 2025](#16.4.105 "#16.4.105")
- [Aurora PostgreSQL Limitless Database 16.4.104, November 19, 2024](#16.4.104 "#16.4.104")
- [Aurora PostgreSQL Limitless Database 16.4.103, October 31, 2024](#16.4.103 "#16.4.103")

### Aurora PostgreSQL Limitless Database 16.4.106, October 13, 2025

**Bug fixes**

- Fixed an issue where tables weren't deleted on shards when `CREATE`, `ALTER`, and `DROP` statements were repeatedly executed using prepared statements through JDBC or ODBC drivers (for example, when using `preferQueryMode=extendedCacheEverything` in JDBC), or when `CREATE`, `ALTER`, and `DROP` statements were executed as part of `PROCEDURE` or `FUNCTION`.
- Fixed incorrect results when querying tables using `UNIQUE INDEX` scans while the table had broken Heap-Only Tuple (HOT) chains from `UPDATE` statements.
- Fixed an issue where healthy nodes were unnecessarily replaced, causing system unavailability.

### Aurora PostgreSQL Limitless Database 16.4.105, April 17, 2025

**Bug fixes**

- Fixed multiple issues that could lead to brief periods of unavailability.
- Fixed an issue resulting in incorrect results for anti-join queries containing a predicate on an outer relation.
- Added pushdown capability for the following system functions:
  - `pg_char_to_encoding`
  - `pg_encoding_to_char`
  - `textanycat`
  - `anytextcat`

- Enhanced error handling for `pg_advisory_lock` in Aurora PostgreSQL Limitless Database.
  With this change, you receive a clear error notification when attempting to use `pg_advisory_lock`.
- Fixed an issue where adding an expression with nested parentheses in `DEFAULT/CHECK` constraints might generate incorrect results.

### Aurora PostgreSQL Limitless Database 16.4.104, November 19, 2024

**Bug fixes**

- Fixed an issue where deadlocks can occur in processing Data Definition Language (DDL) statements when `CREATE INDEX CONCURRENTLY`
  runs.
- Fixed an issue where an error in distributed deadlock resolution can block the detection of subsequent distributed deadlocks.
- Fixed an issue where DDL statements with underlying Data Manipulation Language (DML) statements (such as `CREATE TABLE AS` or calling
  for a table with data) result in errors if the `rds_aurora.limitless_active_shard_key` variable is used in a session.
- Fixed an issue where a shard split operation results in an error.
- Fixed an issue where the `rds_aurora.limitless_alter_table_type_sharded` procedure for converting the table type to sharded fails if
  the `rds_aurora.limitless_alter_table_type_sharded` variable is set.
- Fixed an issue in the deparsing logic of polymorphic objects that resulted in invalid queries not producing errors when the implicit cast of
  passing data caused incorrect object versions to be used.

**Known issues**

- An issue can occur when part of a query is converted to a left or anti-join condition. In these cases, if the inner relation has no results a null
  row is used.
- An issue can occur when adding a column with a `NOT NULL` or `DEFAULT` constraint, that contains functions unsafe to push
  down to shards (such as volatile functions), requires backfilling data in existing rows.
- An issue can occur when the deparsing logic for preparing queries to shards doesn't use parentheses where possible. This can lead to errors when
  `COLLATE` is used in queries.

### Aurora PostgreSQL Limitless Database 16.4.103, October 31, 2024

Release 16.4.103 is the GA version of Aurora PostgreSQL Limitless Database.

For information on this release, see [Using Amazon Aurora PostgreSQL Limitless Database](../AuroraUserGuide/limitless.md "../AuroraUserGuide/limitless.md") in
the _Amazon Aurora User Guide_.
