# Case sensitivity differences for ANSI SQL

Object name case sensitivity is different for SQL Server and Amazon Aurora MySQL-Compatible Edition (Aurora MySQL). SQL Server object names case sensitivity is being determined by the collection. Aurora MySQL names are case sensitive and can be adjusted based on the parameter mentioned following.

In Aurora MySQL, the case sensitivity is determined by the `lower_case_table_names` parameter value. In general, you can use one of the three possible values for this parameter. To avoid issues, we recommend that you use only the two following values for `lower_case_table_names`:

- 0 — names stored as given and comparisons are case-sensitive. You can choose this value for all Amazon Relational Database Service (Amazon RDS) for MySQL versions.
- 1 — names stored in lowercase and comparisons aren’t case-sensitive. You can choose this value for Amazon RDS for MySQL version 5.6, version 5.7, and version 8.0.19 and higher 8.0 versions.
  In Aurora MySQL version 2.10 and higher 2.x versions, make sure to reboot all reader instances after changing the `lower_case_table_names` setting and rebooting the writer instance. For details, see [Rebooting an Aurora MySQL cluster (version 2.10 and higher)](../../../AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.md#aurora-mysql-survivable-replicas "../../../AmazonRDS/latest/AuroraUserGuide/USER_RebootCluster.md#aurora-mysql-survivable-replicas").

In Aurora MySQL version 3, the value of the `lower_case_table_names` parameter is set permanently at the time when you create the cluster. If you use a nondefault value for this option, set up your Aurora MySQL version 3 custom parameter group before upgrading, and specify the parameter group during the snapshot restore operation that creates the version 3 cluster.

With an Aurora global database based on Aurora MySQL, you can’t perform an in-place upgrade from Aurora MySQL version 2 to version 3 if the `lower_case_table_names` parameter is turned on. For more information on the methods that you can use, see [Major version upgrades](../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.md#aurora-global-database-upgrade.major "../../../AmazonRDS/latest/AuroraUserGuide/aurora-global-database-upgrade.md#aurora-global-database-upgrade.major").

We recommend that you don’t changE the `lower_case_table_names` parameter for existing database instances. Doing so can cause inconsistencies with point-in-time recovery backups and read replica DB instances.

Read replicas should always use the same `lower_case_table_names` parameter value as the source DB instance.

By default, object names are being stored in lowercase for MySQL. In most cases, you’ll want to use AWS Database Migration Service transformations to change schema, table, and column names to lowercase.

## Examples

For example, to create a table named EMPLOYEES in uppercase in MySQL, you should use the following:

```
CREATE TABLE EMPLOYEES (
    EMP_ID NUMERIC PRIMARY KEY,
    EMP_FULL_NAME VARCHAR(60) NOT NULL,
    AVG_SALARY NUMERIC NOT NULL);
```

The following command creates a table named employees in lowercase.

```
CREATE TABLE employees (
    EMP_ID NUMERIC PRIMARY KEY,
    EMP_FULL_NAME VARCHAR(60) NOT NULL,
    AVG_SALARY NUMERIC NOT NULL);
```

MySQL will look for objects names in with the exact case sensitivity as written in the query.

You can turn off table name case sensitivity in MySQL by setting the parameter `lower_case_table_names` to 1. Column, index, stored routine, event names, and column aliases aren’t case sensitive on either platform.

For more information, see [Identifier Case Sensitivity](https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html "https://dev.mysql.com/doc/refman/5.7/en/identifier-case-sensitivity.html") in the _MySQL documentation_.
