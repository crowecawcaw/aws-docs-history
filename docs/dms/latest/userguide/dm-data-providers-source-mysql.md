# Using a MySQL compatible database

as a source for homogeneous data migrations in AWS DMS

You can use a MySQL-compatible database (MySQL or MariaDB) as a source for [Homogeneous data migrations](data-migrations.md "data-migrations.md") in AWS DMS. In this case, your
source data provider can be an on-premises, Amazon EC2, or RDS for MySQL or MariaDB database.

To run homogeneous data migrations, you must use a database user with the `SELECT`
privileges for the all source tables and secondary objects for replication.
For change data capture (CDC) tasks, this user must also have the `REPLICATION CLIENT`
(`BINLOG MONITOR` for MariaDB versions later than 10.5.2)
and `REPLICATION SLAVE` privileges. For a full load data migration, you don't need these
two privileges.

Use the following script to create a database user with the required permissions in your
MySQL database. Run the `GRANT` queries for all databases that you migrate to AWS.

```
CREATE USER '`your_user`'@'%' IDENTIFIED BY '`your_password`';

GRANT REPLICATION SLAVE, REPLICATION CLIENT  ON *.* TO '`your_user`'@'%';
GRANT SELECT, RELOAD, LOCK TABLES, SHOW VIEW, EVENT, TRIGGER ON *.* TO '`your_user`'@'%';

GRANT BACKUP_ADMIN ON *.* TO '`your_user`'@'%';
```

In the preceding example, replace each `user input placeholder`
with your own information. If your source MySQL database version is lower than 8.0, then you
can skip the `GRANT BACKUP_ADMIN` command.

Use the following script to create a database user with the required permissions in your MariaDB
database. Run the GRANT queries for all databases that you migrate to AWS.

```
CREATE USER '`your_user`'@'%' IDENTIFIED BY '`your_password`';
GRANT SELECT, RELOAD, LOCK TABLES, REPLICATION SLAVE, BINLOG MONITOR, SHOW VIEW ON  *.* TO 'your_user'@'%';
```

In the preceding example, replace each `user input placeholder`
with your own information.

The following sections describe specific configuration prerequisites for self-managed and
AWS-managed MySQL databases.

###### Topics

- [Using a self-managed
  MySQL compatible database as a source for homogeneous data migrations](#dm-data-providers-source-mysql-sm "#dm-data-providers-source-mysql-sm")
- [Using an AWS-managed
  MySQL compatible database as a source for homogeneous data migrations in AWS DMS](#dm-data-providers-source-mysql-aws "#dm-data-providers-source-mysql-aws")
- [Limitations for using a
  MySQL compatible database as a source for homogeneous data migrations](#dm-data-providers-source-mysql-limitations "#dm-data-providers-source-mysql-limitations")

## Using a self-managed

MySQL compatible database as a source for homogeneous data migrations

This section describes how to configure your MySQL compatible databases that are hosted on-premises
or on Amazon EC2 instances.

Check the version of your source MySQL or MariaDB database. Make sure that AWS DMS supports
your source MySQL or MariaDB database version as described in [Sources for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").

To use CDC, make sure to enable binary logging. To enable binary logging, configure the
following parameters in the `my.ini` (Windows) or
`my.cnf` (UNIX) file of your MySQL or MariaDB database.

| Parameter           | Value                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `server-id`         | Set this parameter to a value of 1 or<br>greater.                                                                                                                                                                                                                                                                                                                                                                                    |
| `log-bin`           | Set the path to the binary log file, such as<br>`log-bin=E:\MySql_Logs\BinLog`. Don't<br>include the file extension.                                                                                                                                                                                                                                                                                                                 |
| `binlog_format`     | Set this parameter to `ROW`. We recommend this<br>setting during replication because in certain cases when<br>`binlog_format` is set to `STATEMENT`,<br>it can cause inconsistency when replicating data to the target.<br>The database engine also writes similar inconsistent data to the<br>target when `binlog_format` is set to<br>`MIXED`, because the database engine<br>automatically switches to `STATEMENT`-based logging. |
| `expire_logs_days`  | Set this parameter to a value of 1 or greater. To prevent<br>overuse of disk space, we recommend that you don't use the<br>default value of 0.                                                                                                                                                                                                                                                                                       |
| `binlog_checksum`   | Set this parameter to `NONE`.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `binlog_row_image`  | Set this parameter to `FULL`.                                                                                                                                                                                                                                                                                                                                                                                                        |
| `log_slave_updates` | Set this parameter to `TRUE` if you are using a<br>MySQL or MariaDB replica as a source.                                                                                                                                                                                                                                                                                                                                             |

## Using an AWS-managed

MySQL compatible database as a source for homogeneous data migrations in AWS DMS

This section describes how to configure your Amazon RDS for MySQL and Amazon RDS for MariaDB database instances.

When you use an AWS-managed MySQL or MariaDB database as a source for homogeneous data migrations in AWS DMS, make
sure that you have the following prerequisites for CDC:

- To enable binary logs for RDS for MySQL and MariaDB, enable automatic backups at the instance level.
  To enable binary logs for an Aurora MySQL cluster, change the variable `binlog_format`
  in the parameter group. You don't need to enable automatic backups for an Aurora MySQL cluster.

Next, set the `binlog_format` parameter to `ROW`.

For more information about setting up automatic backups, see [Enabling automated backups](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.Enabling") in the _Amazon RDS User Guide_.

For more information about setting up binary logging for an
Amazon RDS for MySQL or MariaDB database, see
[Setting the binary logging format](../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.md "../../../AmazonRDS/latest/UserGuide/USER_LogAccess.MySQL.md") in the _Amazon RDS User Guide_.

For more information about setting up binary logging for an Aurora MySQL cluster, see
[How do I turn on binary logging for my Amazon Aurora MySQL cluster?](https://aws.amazon.com/premiumsupport/knowledge-center/enable-binary-logging-aurora/ "https://aws.amazon.com/premiumsupport/knowledge-center/enable-binary-logging-aurora/").

- Ensure that the binary logs are available to AWS DMS. Because AWS-managed
  MySQL and MariaDB databases purge the binary logs as soon as possible, you
  should increase the length of time that the logs remain available. For
  example, to increase log retention to 24 hours, run the following command.

```
call mysql.rds_set_configuration('binlog retention hours', 24);
```

- Set the `binlog_row_image` parameter to `Full`.
- Set the `binlog_checksum` parameter to `NONE`.
- If you are using an Amazon RDS MySQL or MariaDB replica as a source,
  enable backups on the read replica, and ensure the `log_slave_updates` parameter is set to
  `TRUE`.

## Limitations for using a

MySQL compatible database as a source for homogeneous data migrations

The following limitations apply when using a MySQL compatible database as a source for homogeneous data migrations:

- MariaDB objects such as sequences are not supported in homogeneous migration tasks.
- Migration from MariaDB to Amazon RDS MySQL/Aurora MySQL might fail due to incompatible object differences.
- The username you use to connect to your data source has the following limitations:
  - Can be 2 to 64 characters in length.
  - Can't have spaces.
  - Can include the following characters: a-z, A-Z, 0-9, underscore (\_).
  - Must start with a-z or A-Z.

- The password you use to connect to your data source has the following limitations:
  - Can be 1 to 128 characters in length.
  - Can't contain any of the following: single quote ('), double quote ("), semicolon (;) or space.

- AWS DMS homogeneous data migrations creates unencrypted MySQL and MariaDB objects on the target Amazon RDS instances even if the source objects were encrypted.
  RDS for MySQL doesn't support the MySQL keyring_aws AWS Keyring Plugin required for encrypted objects.
  Refer to the [MySQL Keyring Plugin not supported documentation](../../../AmazonRDS/latest/UserGuide/MySQL.md#MySQL.Concepts.Limits.KeyRing "../../../AmazonRDS/latest/UserGuide/MySQL.md#MySQL.Concepts.Limits.KeyRing") in the Amazon RDS User Guide
- AWS DMS does not use Global Transaction Identifiers (GTIDs) for for data
  replication even if the source data contains them.
