

# Aurora MySQL database engine updates 2024-06-04 (version 3.07.0) (Deprecated)
<a name="AuroraMySQL.Updates.3070"></a><a name="3.07.0"></a><a name="3.07.0"></a>

**Version:** 3.07.0

Aurora MySQL 3.07.0 is generally available. Aurora MySQL 3.07 versions are compatible with MySQL 8.0.36. For more information on the community changes that have occurred, see [MySQL 8.0 Release Notes](https://dev.mysql.com/doc/relnotes/mysql/8.0/en/).

For details of the new features in Aurora MySQL version 3, see [Aurora MySQL version 3 compatible with MySQL 8.0](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.MySQL80.html). For differences between Aurora MySQL version 3 and Aurora MySQL version 2, see [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-v2-v3.html). For a comparison of Aurora MySQL version 3 and MySQL 8.0 Community Edition, see [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Compare-80-v3.html) in the *Amazon Aurora User Guide*.

Currently supported Aurora MySQL releases are 2.07.9, 2.07.10, 2.11.\*, 2.12.\*, 3.03.\*, 3.04.\*, 3.05.\*, 3.06.\*, and 3.07.\*.

If you have any questions or concerns, AWS Support is available on the community forums and through [AWS Support](https://aws.amazon.com/support). For more information, see [Maintaining an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.Maintenance.html) in the *Amazon Aurora User Guide*.

## Improvements
<a name="AuroraMySQL.Updates.3070.Improvements"></a>

**Fixed security issues and CVEs:**
+ Enabled support for FIPS-validated cryptography, a fully owned AWS implementation. For more information, see [AWS-LC is now FIPS 140-3 certified](https://aws.amazon.com/blogs/security/aws-lc-is-now-fips-140-3-certified/) on [AWS Security Blog](https://aws.amazon.com/blogs/security/).

This release includes all community CVE fixes up to and including MySQL 8.0.36. The following CVE fixes are included:
+ [CVE-2020-11104](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11104)
+ [CVE-2020-11105](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-11105)
+ [CVE-2023-38545](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38545)
+ [CVE-2023-38546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-38546)
+ [CVE-2023-39975](https://nvd.nist.gov/vuln/detail/CVE-2023-39975)

**Availability improvements:**
+ Fixed an issue that can cause a reader DB instance to restart when reading a table that is being altered or dropped on the writer DB instance.
+ Fixed an issue that can cause an Aurora MySQL writer DB instance to restart when a write forwarding session is closed while running a forwarded query.
+ Fixed an issue that causes a DB instance to restart when handling large GTID sets on a binary log–enabled instance.
+ Fixed an issue when processing `INSERT` queries on InnoDB partitioned tables that can cause a gradual decline of free memory in the instance.
+ Fixed an issue that, in rare conditions, can cause the reader DB instances to restart.
+ Fixed an issue that can cause a database instance to restart when running [SHOW STATUS](https://dev.mysql.com/doc/refman/8.0/en/show-status.html) and [PURGE BINARY LOGS](https://dev.mysql.com/doc/refman/8.0/en/purge-binary-logs.html) statements concurrently. `PURGE BINARY LOGS` is a managed statement that is run to honor the user-configured binlog retention period.
+ Fixed an issue that can cause the server to unexpectedly close after running Data Manipulation Language (DML) statements on a table whose nonvirtual columns were reordered with a `MODIFY COLUMN` or `CHANGE COLUMN` statement.
+ Fixed an issue that, during the restart of a database instance, can cause an additional restart.
+ Fixed an issue that can cause a reader DB instance that uses write forwarding to restart when a forwarded [implicit commit statement](https://dev.mysql.com/doc/refman/8.0/en/implicit-commit.html) encounters an error.
+ Fixed an issue that, in rare conditions, can cause a reader instance to restart when performing `SELECT` queries on tables with a foreign key constraint.
+ Fixed an issue where DB instances using multi-TB Aurora cluster volumes can experience increased downtime during restart due to InnoDB buffer pool validation failures.
+ Fixed an issue that can cause a database to restart when a cascading `UPDATE` or `DELETE` foreign key constraint is defined on a table where a virtual column is involved either as a column in the foreign key constraint, or as a member of the referenced table.
+ Fixed an issue that can interrupt database recovery during startup if the restart occurred while running heavy insert operations involving `AUTO_INCREMENT` columns.
+ Fixed an issue in Aurora serverless that can lead to a database restart while scaling up.

**General improvements:**
+ Reduced I/O usage and improved performance for a subset of primary key range scan queries that employ parallel query.
+ [Aurora MySQL version 3.06.0](AuroraMySQL.Updates.3060.md) added support for Amazon Bedrock integration. As part of this, new reserved keywords (`accept`, `aws_bedrock_invoke_model`, `aws_sagemaker_invoke_endpoint`, `content_type`, and `timeout_ms`) were added. In Aurora MySQL version 3.07.0, these keywords have been changed to nonreserved keywords, which are permitted as identifiers without quoting. For more information on how MySQL handles reserved and nonreserved keywords, see [Keywords and reserved words](https://dev.mysql.com/doc/refman/8.0/en/keywords.html) in the MySQL documentation.
+ Fixed an issue that didn't clearly return an error message to the client when invoking the Amazon Bedrock service from an Aurora MySQL DB cluster in an AWS Region where Amazon Bedrock isn't yet available.
+ Fixed an issue that can cause excessive memory consumption when querying `BLOB` columns using Aurora parallel query.
+ Added support for the `connection_memory_limit` and `connection_memory_chunk_size` parameters to be set at the session level to behave the same as in MySQL Community Edition. The `connection_memory_limit` is used to set the maximum amount of memory that can be used by a single user connection. The `connection_memory_chunk_size` parameter can be used to set the chunking size for updates to the [global memory usage counter](https://dev.mysql.com/doc/refman/8.0/en/server-status-variables.html#statvar_Global_connection_memory).
+ Fixed an issue where the user is unable to interrupt any query or set session timeouts for `performance_schema` queries.
+ Fixed an issue where binary log (binlog) replication configured to use custom SSL certificates ([mysql.rds\_import\_binlog\_ssl\_material](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/mysql-stored-proc-replicating.html#mysql_rds_import_binlog_ssl_material)) could fail when the replication instance is undergoing a host replacement.
+ Added the `Aurora_fts_cache_memory_used` global status variable to track memory usage for the full-text search system across all tables. For more information, see [Aurora MySQL global status variables](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ParameterGroups.html#AuroraMySQL.Reference.GlobalStatusVars) in the *Amazon Aurora User Guide*.
+ Fixed an issue where an Amazon Redshift cluster configured as a zero-ETL destination might experience a temporary increase in [IntegrationLag](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.monitoring.html) when an Amazon Aurora MySQL DB cluster is configured as a binary log replica, with Enhanced Binlog and zero-ETL integration enabled.
+ Fixed an issue related to audit log file management that can cause log files to be inaccessible for download or rotation, and in some cases increase CPU usage.
+ Optimized `AUTO_INCREMENT` key recovery to reduce the completion time for restoring snapshots, performing point-in-time recovery, and cloning DB clusters with large numbers of tables in the database.
+ Fixed an issue where the [wait/io/redo\_log\_flush](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/ams-waits.io-auredologflush.html) event wasn't shown in the Performance Schema [wait event summary tables](https://dev.mysql.com/doc/refman/8.0/en/performance-schema-wait-summary-tables.html).
+ Fixed an issue that can cause duplicate key errors for `AUTO_INCREMENT` columns using descending indices after a snapshot restore, backtrack, or database cloning operation.
+ Fixed an issue that can cause a writer DB instance to restart when a reader DB instance using write forwarding runs a Data Manipulation Language (DML) statement that contains a timestamp value and the ` time_zone` database parameter is set to `UTC`.
+ Fixed an issue where a `SELECT` query on an Aurora reader instance might fail with the error table doesn't exist when the table has at least one full-text search (FTS) index and a `TRUNCATE` statement is being run on the Aurora writer DB instance.
+ Fixed an issue that, in rare cases, causes zero-downtime patching (ZDP) to fail.
+ Fixed an issue that can cause an incomplete result set when running queries involving `LEFT JOIN` or `RIGHT JOIN` operations using the hash join algorithm with parallel query.

**Upgrades and migrations:**
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 when there is a user-defined `FTS_DOC_ID` column present in the table schema.
+ Fixed an issue that can cause upgrade failures from Aurora MySQL version 2 to Aurora MySQL version 3 due to a synchronization issue while processing InnoDB tablespaces.
+ Fixed an issue that can cause major version upgrades to Aurora MySQL version 3 to fail due to the presence of orphaned entries for already deleted tablespaces in InnoDB system tables in Aurora MySQL version 2.
+ Fixed an issue where the [SERVER\_ID](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Reference.ISTables.html#AuroraMySQL.Reference.ISTables.replica_host_status) value wasn't updated after an Amazon RDS Blue/Green Deployment switchover. This led to issues where smart drivers such as the [Amazon Web Services (AWS) JDBC Driver](https://github.com/awslabs/aws-advanced-jdbc-wrapper) were unable to discover the DB cluster topology after a blue/green switchover. With this fix, Aurora DB clusters renamed as part of an RDS Blue/Green Deployment, that are running on Aurora MySQL version 3.07 and higher, will have the `SERVER_ID` value updated as part of the switchover. For earlier versions, the DB instances in the blue and green clusters can be rebooted to update the `SERVER_ID` value.

## Integration of MySQL Community Edition bug fixes
<a name="AuroraMySQL.Updates.3070.Patches"></a>

This release includes all community bug fixes up to and including 8.0.36, in addition to the following. For more information, see [MySQL bugs fixed by Aurora MySQL 3.x database engine updates](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraMySQLReleaseNotes/AuroraMySQL.Updates.MySQLBugs.html#AuroraMySQL.Updates.MySQLBugs.v3).
+ Fixed an issue where cache line value can be calculated incorrectly, causing a failure during database restart on Graviton-based instances. (Community Bug Fix \#35479763)
+ Fixed an issue where some instances of subqueries within stored routines were not handled correctly. (Community Bug Fix \#35377192)
+ Fixed an issue that can cause higher CPU usage due to background TLS certificate rotation (Community Bug Fix \#34284186).
+ Fixed an issue where InnoDB allowed the addition of `INSTANT` columns to tables in the MySQL system schema in Aurora MySQL versions lower than 3.05, which could lead to the server unexpectedly closing (database instance restarting) after upgrading to Aurora MySQL version 3.05.0. (Community Bug Fix \#35625510).