# Aurora MySQL version 3 compatible with MySQL 8.0

You can use Aurora MySQL version 3 to get the latest MySQL-compatible features, performance enhancements, and bug
fixes. Following, you can learn about Aurora MySQL version 3, with MySQL 8.0 compatibility. You can learn how to
upgrade your clusters and applications to Aurora MySQL version 3.

Some Aurora features, such as Aurora Serverless v2, require Aurora MySQL version 3.

###### Topics

- [Features from MySQL 8.0 Community Edition](#AuroraMySQL.8.0-features-community "#AuroraMySQL.8.0-features-community")
- [Aurora MySQL version 3 prerequisite for Aurora MySQL Serverless v2](#AuroraMySQL.serverless-v2-8.0-prereq "#AuroraMySQL.serverless-v2-8.0-prereq")
- [Release notes for Aurora MySQL version 3](#AuroraMySQL.mysql80-bugs-fixed "#AuroraMySQL.mysql80-bugs-fixed")
- [New parallel query optimizations](#AuroraMySQL.8.0-features-pq "#AuroraMySQL.8.0-features-pq")
- [Optimizations to reduce database restart time](#ReducedRestartTime "#ReducedRestartTime")
- [New temporary table behavior in Aurora MySQL version 3](ams3-temptable-behavior.md "ams3-temptable-behavior.md")
- [Comparing Aurora MySQL version 2 and Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md")
- [Comparing Aurora MySQL version 3 and MySQL 8.0 Community Edition](AuroraMySQL.md "AuroraMySQL.md")
- [Upgrading to Aurora MySQL version 3](AuroraMySQL.md "AuroraMySQL.md")

## Features from MySQL 8.0 Community Edition

The initial release of Aurora MySQL version 3 is compatible with MySQL 8.0.23 Community Edition. MySQL 8.0 introduces several new
features, including the following:

- Atomic Data Definition Language (DDL) support. For more information, see [Atomic Data Definition Language (DDL) support](AuroraMySQL.md#AuroraMySQL.Compare-v2-v3-atomic-ddl "AuroraMySQL.md#AuroraMySQL.Compare-v2-v3-atomic-ddl").
- JSON functions. For usage information, see [JSON Functions](https://dev.mysql.com/doc/refman/8.0/en/json-functions.html "https://dev.mysql.com/doc/refman/8.0/en/json-functions.html") in the
  _MySQL Reference Manual_.
- Window functions. For usage information, see [Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html "https://dev.mysql.com/doc/refman/8.0/en/window-functions.html")
  in the _MySQL Reference Manual_.
- Common table expressions (CTEs), using the `WITH` clause. For usage information, see [WITH (Common Table Expressions)](https://dev.mysql.com/doc/refman/8.0/en/with.html "https://dev.mysql.com/doc/refman/8.0/en/with.html") in the _MySQL Reference
  Manual_.
- Optimized `ADD COLUMN` and `RENAME COLUMN` clauses for the `ALTER TABLE` statement. These optimizations are
  called "instant DDL." Aurora MySQL version 3 is compatible with the community MySQL instant DDL feature. The former Aurora fast DDL
  feature isn't used. For usage information for instant DDL, see [Instant DDL (Aurora MySQL version 3)](AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl "AuroraMySQL.Managing.md#AuroraMySQL.mysql80-instant-ddl").
- Descending, functional, and invisible indexes. For usage information, see [Invisible Indexes](https://dev.mysql.com/doc/refman/8.0/en/invisible-indexes.html "https://dev.mysql.com/doc/refman/8.0/en/invisible-indexes.html"), [Descending Indexes](https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html "https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html"), and [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html#create-index-functional-key-parts "https://dev.mysql.com/doc/refman/8.0/en/create-index.html#create-index-functional-key-parts") in the
  _MySQL Reference Manual_.
- Role-based privileges controlled through SQL statements. For more information on changes to the privilege model, see [Role-based privilege model](AuroraMySQL.md#AuroraMySQL.privilege-model "AuroraMySQL.md#AuroraMySQL.privilege-model").
- `NOWAIT` and `SKIP LOCKED` clauses with the `SELECT ... FOR SHARE` statement. These clauses avoid waiting for
  other transactions to release row locks. For usage information, see [Locking Reads](https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-locking-reads.html") in the _MySQL Reference
  Manual_.
- Improvements to binary log (binlog) replication. For the Aurora MySQL details, see [Binary log replication](AuroraMySQL.md#AuroraMySQL.mysql80-binlog "AuroraMySQL.md#AuroraMySQL.mysql80-binlog"). In particular, you can perform filtered replication. For usage information about filtered
  replication, see [How Servers Evaluate Replication Filtering
  Rules](https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html") in the _MySQL Reference Manual_.
- Hints. Some of the MySQL 8.0–compatible hints were already backported to Aurora MySQL version 2. For information about using hints with
  Aurora MySQL, see [Aurora MySQL hints](AuroraMySQL.Reference.md "AuroraMySQL.Reference.md"). For the full list of hints in
  community MySQL 8.0, see [Optimizer Hints](https://dev.mysql.com/doc/refman/8.0/en/optimizer-hints.html "https://dev.mysql.com/doc/refman/8.0/en/optimizer-hints.html") in the
  _MySQL Reference Manual_.

For the full list of features added to MySQL 8.0 community edition, see the blog post [The complete list of new features in MySQL
8.0](https://dev.mysql.com/blog-archive/the-complete-list-of-new-features-in-mysql-8-0/ "https://dev.mysql.com/blog-archive/the-complete-list-of-new-features-in-mysql-8-0/").

Aurora MySQL version 3 also includes changes to keywords for inclusive language, backported from community MySQL 8.0.26. For details about those
changes, see [Inclusive language changes for Aurora MySQL version 3](AuroraMySQL.md#AuroraMySQL.8.0-inclusive-language "AuroraMySQL.md#AuroraMySQL.8.0-inclusive-language").

## Aurora MySQL version 3 prerequisite for Aurora MySQL Serverless v2

Aurora MySQL version 3 is a prerequisite for all DB instances in an Aurora MySQL Serverless v2 cluster.
Aurora MySQL Serverless v2 includes support for reader instances in a DB cluster, and other Aurora features
that aren't available for Aurora MySQL Serverless v1. It also has faster and more granular scaling than
Aurora MySQL Serverless v1.

## Release notes for Aurora MySQL version 3

For the release notes for all Aurora MySQL version 3 releases, see
[Database engine updates for Amazon Aurora MySQL version 3](../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md "../AuroraMySQLReleaseNotes/AuroraMySQL.Updates.md") in the _Release Notes for Aurora MySQL_.

## New parallel query optimizations

The Aurora parallel query optimization now applies to more SQL operations:

- Parallel query now applies to tables containing the data types `TEXT`, `BLOB`,
  `JSON`, `GEOMETRY`, and `VARCHAR` and `CHAR` longer than 768 bytes.
- Parallel query can optimize queries involving partitioned tables.
- Parallel query can optimize queries involving aggregate function calls in the select list and the `HAVING`
  clause.

For more information about these enhancements, see [Upgrading parallel query clusters to Aurora MySQL version 3](aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-pqv2 "aurora-mysql-parallel-query-optimizing.md#aurora-mysql-parallel-query-upgrade-pqv2"). For general information about Aurora parallel query, see [Parallel query for Amazon Aurora MySQL](aurora-mysql-parallel-query.md "aurora-mysql-parallel-query.md").

## Optimizations to reduce database restart time

Your Aurora MySQL DB cluster must be highly available during both planned and unplanned outages.

Database administrators need to perform occasional database maintenance. This maintenance includes database patching,
upgrades, database parameter modifications requiring a manual reboot, performing a failover to reduce the time it takes for
instance class changes, and so on. These planned actions require downtime.

However, downtime can also be caused by unplanned actions, such as an unexpected failover due to an underlying hardware fault
or database resource throttling. All of these planned and unplanned actions result in a database restart.

In Aurora MySQL version 3.05 and higher, we've introduced optimizations that reduce the database restart time. These
optimizations provide up to 65% less downtime than without optimizations, and fewer disruptions to your database workloads,
after a restart.

During database startup, many internal memory components are initialized. The largest of these is the [InnoDB buffer
pool](https://aws.amazon.com/blogs/database/best-practices-for-amazon-aurora-mysql-database-configuration/ "https://aws.amazon.com/blogs/database/best-practices-for-amazon-aurora-mysql-database-configuration/"), which in Aurora MySQL is 75% of the instance memory size by default. Our testing has found that the
initialization time is proportional to the size of InnoDB buffer pool, and therefore scales with the DB instance class size.
During this initialization phase, the database can't accept connections, which causes longer downtime during restarts. The first
phase of Aurora MySQL fast restart optimizes the buffer pool initialization, which reduces the time for database initialization
and thereby reduces the overall restart time.

For more details, see the blog [Reduce downtime with Amazon Aurora MySQL database restart time optimizations](https://aws.amazon.com/blogs/database/reduce-downtime-with-amazon-aurora-mysql-database-restart-time-optimizations/ "https://aws.amazon.com/blogs/database/reduce-downtime-with-amazon-aurora-mysql-database-restart-time-optimizations/").
