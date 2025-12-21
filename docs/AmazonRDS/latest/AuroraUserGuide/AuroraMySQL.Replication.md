# Configuring replication filters with Aurora MySQL

You can use replication filters to specify which databases and tables are replicated with a read replica. Replication filters
can include databases and tables in replication or exclude them from replication.

The following are some use cases for replication filters:

- To reduce the size of a read replica. With replication filtering, you can
  exclude the databases and tables that aren't needed on the read
  replica.
- To exclude databases and tables from read replicas for security reasons.
- To replicate different databases and tables for specific use cases at different
  read replicas. For example, you might use specific read replicas for
  analytics or sharding.
- For a DB cluster that has read replicas in different AWS Regions, to replicate different databases or tables in
  different AWS Regions.
- To specify which databases and tables are replicated with an Aurora MySQL DB cluster that is configured as a replica in
  an inbound replication topology. For more information about this configuration, see [Replication between Aurora and MySQL or between Aurora and another Aurora DB
  cluster (binary log replication)](AuroraMySQL.Replication.md "AuroraMySQL.Replication.md").

###### Topics

- [Setting replication filtering parameters for Aurora MySQL](#AuroraMySQL.Replication.Filters.Configuring "#AuroraMySQL.Replication.Filters.Configuring")
- [Replication filtering limitations for Aurora MySQL](#AuroraMySQL.Replication.Filters.Limitations "#AuroraMySQL.Replication.Filters.Limitations")
- [Replication filtering examples for Aurora MySQL](#AuroraMySQL.Replication.Filters.Examples "#AuroraMySQL.Replication.Filters.Examples")
- [Viewing the replication filters for a read replica](#AuroraMySQL.Replication.Filters.Viewing "#AuroraMySQL.Replication.Filters.Viewing")

## Setting replication filtering parameters for Aurora MySQL

To configure replication filters, set the following parameters:

- `binlog-do-db` – Replicate changes to the specified binary logs. When you set this parameter for
  a binlog source cluster, only the binary logs specified in the parameter are replicated.
- `binlog-ignore-db` – Don't replicate changes to the specified binary logs. When the
  `binlog-do-db` parameter is set for a binlog source cluster, this parameter isn't
  evaluated.
- `replicate-do-db` – Replicate changes to the specified databases. When you set this parameter for
  a binlog replica cluster, only the databases specified in the parameter are replicated.
- `replicate-ignore-db` – Don't replicate changes to the specified databases. When the
  `replicate-do-db` parameter is set for a binlog replica cluster, this parameter isn't
  evaluated.
- `replicate-do-table` – Replicate changes to the specified tables. When you set this parameter for
  a read replica, only the tables specified in the parameter are replicated. Also, when the
  `replicate-do-db` or `replicate-ignore-db` parameter is set, make sure to include the
  database that includes the specified tables in replication with the binlog replica cluster.
- `replicate-ignore-table` – Don't replicate changes to the specified tables. When the
  `replicate-do-table` parameter is set for a binlog replica cluster, this parameter isn't
  evaluated.
- `replicate-wild-do-table` – Replicate tables based on the specified database and table name
  patterns. The `%` and `_` wildcard characters are supported. When the
  `replicate-do-db` or `replicate-ignore-db` parameter is set, make sure to include the
  database that includes the specified tables in replication with the binlog replica cluster.
- `replicate-wild-ignore-table` – Don't replicate tables based on the specified database and
  table name patterns. The `%` and `_` wildcard characters are supported. When the
  `replicate-do-table` or `replicate-wild-do-table` parameter is set for a binlog replica
  cluster, this parameter isn't evaluated.

The parameters are evaluated in the order that they are listed. For more information about how these parameters work,
see the MySQL documentation:

- For general information, see [Replica Server Options and Variables](https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html "https://dev.mysql.com/doc/refman/8.0/en/replication-options-replica.html").
- For information about how database replication filtering parameters are evaluated, see
  [Evaluation of Database-Level Replication and Binary Logging Options](https://dev.mysql.com/doc/refman/8.0/en/replication-rules-db-options.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rules-db-options.html").
- For information about how table replication filtering parameters are evaluated, see
  [Evaluation of Table-Level Replication Options](https://dev.mysql.com/doc/refman/8.0/en/replication-rules-table-options.html "https://dev.mysql.com/doc/refman/8.0/en/replication-rules-table-options.html").

By default, each of these parameters has an empty value. On each binlog cluster, you can use these parameters to set,
change, and delete replication filters. When you set one of these parameters, separate each filter from others with a comma.

You can use the `%` and `_` wildcard characters in the `replicate-wild-do-table` and
`replicate-wild-ignore-table` parameters. The `%` wildcard matches any number of characters, and the
`_` wildcard matches only one character.

The binary logging format of the source DB instance is important for replication because it determines the record of data
changes. The setting of the `binlog_format` parameter determines whether the replication is row-based or
statement-based. For more information, see
[Configuring Aurora MySQL binary logging for Single-AZ databases](USER_LogAccess.MySQL.md "USER_LogAccess.MySQL.md").

###### Note

All data definition language (DDL) statements are replicated as statements, regardless of the
`binlog_format` setting on the source DB instance.

## Replication filtering limitations for Aurora MySQL

The following limitations apply to replication filtering for Aurora MySQL:

- Replication filters are supported only for Aurora MySQL version 3.
- Each replication filtering parameter has a 2,000-character limit.
- Commas aren't supported in replication filters.
- Replication filtering doesn't support XA transactions.

For more information, see [Restrictions
on XA Transactions](https://dev.mysql.com/doc/refman/8.0/en/xa-restrictions.html "https://dev.mysql.com/doc/refman/8.0/en/xa-restrictions.html") in the MySQL documentation.

## Replication filtering examples for Aurora MySQL

To configure replication filtering for a read replica, modify the replication filtering parameters in the DB cluster
parameter group associated with the read replica.

###### Note

You can't modify a default DB cluster parameter group. If the read replica is using a default parameter group,
create a new parameter group and associate it with the read replica. For more information on DB cluster parameter
groups, see [Parameter groups for Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

You can set parameters in a DB cluster parameter group using the AWS Management Console, AWS CLI, or RDS API. For information about
setting parameters, see [Modifying parameters in a DB parameter group
in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). When you set parameters in a DB cluster parameter group, all of
the DB clusters associated with the parameter group use the parameter settings. If you set the replication filtering
parameters in a DB cluster parameter group, make sure that the parameter group is associated only with read replica
clusters. Leave the replication filtering parameters empty for source DB instances.

The following examples set the parameters using the AWS CLI. These examples set `ApplyMethod` to
`immediate` so that the parameter changes occur immediately after the CLI command completes. If you want a
pending change to be applied after the read replica is rebooted, set `ApplyMethod` to
`pending-reboot`.

The following examples set replication filters:

- [Including databases in replication](#rep-filter-in-dbs-ams "#rep-filter-in-dbs-ams")
- [Including tables in replication](#rep-filter-in-tables-ams "#rep-filter-in-tables-ams")
- [Including tables in replication with wildcard characters](#rep-filter-in-tables-wildcards-ams "#rep-filter-in-tables-wildcards-ams")
- [Excluding databases from replication](#rep-filter-ex-dbs-ams "#rep-filter-ex-dbs-ams")
- [Excluding tables from replication](#rep-filter-ex-tables-ams "#rep-filter-ex-tables-ams")
- [Excluding tables from replication using wildcard characters](#rep-filter-ex-tables-wildcards-ams "#rep-filter-ex-tables-wildcards-ams")

###### Example Including databases in replication

The following example includes the `mydb1` and `mydb2` databases in replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-do-db,ParameterValue='mydb1,mydb2',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-do-db,ParameterValue='mydb1,mydb2',ApplyMethod=immediate"
```

###### Example Including tables in replication

The following example includes the `table1` and `table2` tables in database `mydb1`
in replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-do-table,ParameterValue='mydb1.table1,mydb1.table2',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-do-table,ParameterValue='mydb1.table1,mydb1.table2',ApplyMethod=immediate"
```

###### Example Including tables in replication using wildcard characters

The following example includes tables with names that begin with `order` and `return` in
database `mydb` in replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-wild-do-table,ParameterValue='mydb.order%,mydb.return%',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-wild-do-table,ParameterValue='mydb.order%,mydb.return%',ApplyMethod=immediate"
```

###### Example Excluding databases from replication

The following example excludes the `mydb5` and `mydb6` databases from replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-ignore-db,ParameterValue='mydb5,mydb6',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-ignore-db,ParameterValue='mydb5,mydb6,ApplyMethod=immediate"
```

###### Example Excluding tables from replication

The following example excludes tables `table1` in database `mydb5` and `table2` in
database `mydb6` from replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-ignore-table,ParameterValue='mydb5.table1,mydb6.table2',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-ignore-table,ParameterValue='mydb5.table1,mydb6.table2',ApplyMethod=immediate"
```

###### Example Excluding tables from replication using wildcard characters

The following example excludes tables with names that begin with `order` and `return` in
database `mydb7` from replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster-parameter-group \
  --db-cluster-parameter-group-name myparametergroup \
  --parameters "ParameterName=replicate-wild-ignore-table,ParameterValue='mydb7.order%,mydb7.return%',ApplyMethod=immediate"
```

For Windows:

```
aws rds modify-db-cluster-parameter-group ^
  --db-cluster-parameter-group-name myparametergroup ^
  --parameters "ParameterName=replicate-wild-ignore-table,ParameterValue='mydb7.order%,mydb7.return%',ApplyMethod=immediate"
```

## Viewing the replication filters for a read replica

You can view the replication filters for a read replica in the following ways:

- Check the settings of the replication filtering parameters in the parameter group associated with the read replica.

For instructions, see [Viewing parameter values for a
DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

- In a MySQL client, connect to the read replica and run the `SHOW REPLICA STATUS` statement.

In the output, the following fields show the replication filters for the read replica:

    + `Binlog_Do_DB`
    + `Binlog_Ignore_DB`
    + `Replicate_Do_DB`
    + `Replicate_Ignore_DB`
    + `Replicate_Do_Table`
    + `Replicate_Ignore_Table`
    + `Replicate_Wild_Do_Table`
    + `Replicate_Wild_Ignore_Table`

For more information about these fields, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html "https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html")
in the MySQL documentation.
