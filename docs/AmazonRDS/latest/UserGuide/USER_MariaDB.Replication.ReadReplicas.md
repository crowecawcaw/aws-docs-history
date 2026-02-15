# Configuring replication filters with MariaDB

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
- For a DB instance that has read replicas in different AWS Regions, to replicate
  different databases or tables in different AWS Regions.

###### Note

You can also use replication filters to specify which databases and tables are replicated with
a primary MariaDB DB instance that is configured as a replica in an inbound replication topology. For more
information about this configuration, see [Configuring binary log file position replication with an external source instance](MySQL.Procedural.Importing.External.md "MySQL.Procedural.Importing.External.md").

###### Topics

- [Setting replication filtering parameters for RDS for MariaDB](#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Configuring "#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Configuring")
- [Replication filtering limitations for RDS for MariaDB](#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Limitations "#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Limitations")
- [Replication filtering examples for RDS for MariaDB](#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Examples "#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Examples")
- [Viewing the replication filters for a read replica](#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Viewing "#USER_MariaDB.Replication.ReadReplicas.ReplicationFilters.Viewing")

## Setting replication filtering parameters for RDS for MariaDB

To configure replication filters, set the following replication filtering parameters on the read replica:

- `replicate-do-db` – Replicate changes to the specified databases.
  When you set this parameter for a read replica, only the databases specified in the parameter are
  replicated.
- `replicate-ignore-db` – Don't replicate changes to the specified databases.
  When the `replicate-do-db` parameter is set for a read replica, this parameter isn't
  evaluated.
- `replicate-do-table` – Replicate changes to the specified tables. When you set
  this parameter for a read replica, only the tables specified in the parameter are
  replicated. Also, when the `replicate-do-db` or `replicate-ignore-db` parameter
  is set, the database that includes the specified tables must be included in replication with the read replica.
- `replicate-ignore-table` – Don't replicate changes to the specified tables.
  When the `replicate-do-table` parameter is set for a read replica, this parameter isn't evaluated.
- `replicate-wild-do-table` – Replicate tables based on the
  specified database and table name patterns. The `%` and
  `_` wildcard characters are supported. When the
  `replicate-do-db` or `replicate-ignore-db`
  parameter is set, make sure to include the database that includes the
  specified tables in replication with the read replica.
- `replicate-wild-ignore-table` – Don't replicate tables based on the specified database and table name patterns.
  The `%` and `_` wildcard characters are supported. When the `replicate-do-table` or
  `replicate-wild-do-table` parameter is set for a read replica, this parameter isn't
  evaluated.

The parameters are evaluated in the order that they are listed. For more
information about how these parameters work, see [the MariaDB documentation](https://mariadb.com/kb/en/replication-filters/#replication-filters-for-replication-slaves "https://mariadb.com/kb/en/replication-filters/#replication-filters-for-replication-slaves").

By default, each of these parameters has an empty value. On each read replica, you
can use these parameters to set, change, and delete replication filters. When
you set one of these parameters, separate each filter from others with a
comma.

You can use the `%` and `_` wildcard characters in the
`replicate-wild-do-table` and
`replicate-wild-ignore-table` parameters. The `%`
wildcard matches any number of characters, and the `_` wildcard
matches only one character.

The binary logging format of the source DB instance is important for replication because it determines the record of
data changes. The setting of the `binlog_format` parameter determines whether the replication is row-based or
statement-based. For more information, see [Configuring MariaDB binary
logging](USER_LogAccess.MariaDB.md "USER_LogAccess.MariaDB.md").

###### Note

All data definition language (DDL) statements are replicated as statements, regardless of the
`binlog_format` setting on the source DB instance.

## Replication filtering limitations for RDS for MariaDB

The following limitations apply to replication filtering for RDS for MariaDB:

- Each replication filtering parameter has a 2,000-character limit.
- Commas aren't supported in replication filters.
- The MariaDB `binlog_do_db` and `binlog_ignore_db`
  options for binary log filtering aren't supported.
- Replication filtering doesn't support XA transactions.

For more information, see [Restrictions on XA Transactions](https://dev.mysql.com/doc/refman/8.0/en/xa-restrictions.html "https://dev.mysql.com/doc/refman/8.0/en/xa-restrictions.html") in the MySQL documentation.

- Replication filtering isn't supported for RDS for MariaDB version 10.2.

## Replication filtering examples for RDS for MariaDB

To configure replication filtering for a read replica, modify the replication filtering parameters in the parameter group
associated with the read replica.

###### Note

You can't modify a default parameter group. If the read replica is using a default parameter group, create a new parameter group
and associate it with the read replica. For more information on DB parameter groups, see
[Parameter groups for Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

You can set parameters in a parameter group using the AWS Management Console, AWS CLI, or RDS API.
For information about setting parameters, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). When you set
parameters in a parameter group, all of the DB instances associated with the
parameter group use the parameter settings. If you set the replication filtering
parameters in a parameter group, make sure that the parameter group is
associated only with read replicas. Leave the replication filtering parameters
empty for source DB instances.

The following examples set the parameters using the AWS CLI. These examples set `ApplyMethod` to `immediate` so that the
parameter changes occur immediately after the CLI command completes. If you want a pending change to be applied after the read replica is
rebooted, set `ApplyMethod` to `pending-reboot`.

The following examples set replication filters:

- [Including databases in replication](#rep-filter-in-dbs-mariadb "#rep-filter-in-dbs-mariadb")
- [Including tables in replication](#rep-filter-in-tables-mariadb "#rep-filter-in-tables-mariadb")
- [Including tables in replication with wildcard characters](#rep-filter-in-tables-wildcards-mariadb "#rep-filter-in-tables-wildcards-mariadb")
- [Escaping wildcard characters in names](#rep-filter-escape-wildcards-mariadb "#rep-filter-escape-wildcards-mariadb")
- [Excluding databases from replication](#rep-filter-ex-dbs-mariadb "#rep-filter-ex-dbs-mariadb")
- [Excluding tables from replication](#rep-filter-ex-tables-mariadb "#rep-filter-ex-tables-mariadb")
- [Excluding tables from replication using wildcard characters](#rep-filter-ex-tables-wildcards-mariadb "#rep-filter-ex-tables-wildcards-mariadb")

###### Example Including databases in replication

The following example includes the `mydb1` and `mydb2`
databases in replication. When you set `replicate-do-db` for a
read replica, only the databases specified in the parameter are
replicated.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-do-db", "ParameterValue": "mydb1,mydb2", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-do-db", "ParameterValue": "mydb1,mydb2", "ApplyMethod":"immediate"}]"
```

###### Example Including tables in replication

The following example includes the `table1` and `table2`
tables in database `mydb1` in replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-do-table", "ParameterValue": "mydb1.table1,mydb1.table2", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-do-table", "ParameterValue": "mydb1.table1,mydb1.table2", "ApplyMethod":"immediate"}]"
```

###### Example Including tables in replication using wildcard characters

The following example includes tables with names that begin with
`orders` and `returns` in database
`mydb` in replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-wild-do-table", "ParameterValue": "mydb.orders%,mydb.returns%", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-wild-do-table", "ParameterValue": "mydb.orders%,mydb.returns%", "ApplyMethod":"immediate"}]"
```

###### Example Escaping wildcard characters in names

The following example shows you how to use the escape character `\`
to escape a wildcard character that is part of a name.

Assume that you have several table names in database `mydb1`
that start with `my_table`, and you want to include these tables
in replication. The table names include an underscore, which is also a
wildcard character, so the example escapes the underscore in the table
names.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-wild-do-table", "ParameterValue": "my\_table%", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-wild-do-table", "ParameterValue": "my\_table%", "ApplyMethod":"immediate"}]"
```

###### Example Excluding databases from replication

The following example excludes the `mydb1` and `mydb2`
databases from replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-ignore-db", "ParameterValue": "mydb1,mydb2", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-ignore-db", "ParameterValue": "mydb1,mydb2", "ApplyMethod":"immediate"}]"
```

###### Example Excluding tables from replication

The following example excludes tables `table1` and
`table2` in database `mydb1` from
replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-ignore-table", "ParameterValue": "mydb1.table1,mydb1.table2", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-ignore-table", "ParameterValue": "mydb1.table1,mydb1.table2", "ApplyMethod":"immediate"}]"
```

###### Example Excluding tables from replication using wildcard characters

The following example excludes tables with names that begin with
`orders` and `returns` in database
`mydb` from replication.

For Linux, macOS, or Unix:

```
aws rds modify-db-parameter-group \
  --db-parameter-group-name myparametergroup \
  --parameters "[{"ParameterName": "replicate-wild-ignore-table", "ParameterValue": "mydb.orders%,mydb.returns%", "ApplyMethod":"immediate"}]"
```

For Windows:

```
aws rds modify-db-parameter-group ^
  --db-parameter-group-name myparametergroup ^
  --parameters "[{"ParameterName": "replicate-wild-ignore-table", "ParameterValue": "mydb.orders%,mydb.returns%", "ApplyMethod":"immediate"}]"
```

## Viewing the replication filters for a read replica

You can view the replication filters for a read replica in the following ways:

- Check the settings of the replication filtering parameters in the parameter group associated with the read replica.

For instructions, see [Viewing parameter values for a
DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

- In a MariaDB client, connect to the read replica and run the `SHOW REPLICA STATUS` statement.

In the output, the following fields show the replication filters for the read replica:

    + `Replicate_Do_DB`
    + `Replicate_Ignore_DB`
    + `Replicate_Do_Table`
    + `Replicate_Ignore_Table`
    + `Replicate_Wild_Do_Table`
    + `Replicate_Wild_Ignore_Table`

For more information about these fields, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html "https://dev.mysql.com/doc/refman/8.0/en/replication-administration-status.html")
in the MySQL documentation.

###### Note

Previous versions of MariaDB used `SHOW SLAVE STATUS` instead of
`SHOW REPLICA STATUS`. If you are using a MariaDB version before 10.5,
then use `SHOW SLAVE STATUS`.
