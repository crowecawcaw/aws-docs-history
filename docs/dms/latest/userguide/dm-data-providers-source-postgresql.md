# Using a PostgreSQL database as a source for homogeneous data migrations in AWS DMS

You can use a PostgreSQL database as a source for [Homogeneous data migrations](data-migrations.md "data-migrations.md") in AWS DMS. In this case, your
source data provider can be an on-premises, Amazon EC2, or RDS for PostgreSQL database.

To run homogeneous data migrations, grant superuser permissions for the database user
that you specified in AWS DMS for your PostgreSQL source database. The database user needs
superuser permissions to access replication-specific functions in the source. For a full
load data migration, your database user needs `SELECT` permissions on tables
to migrate them.

Use the following script to create a database user with the required permissions in
your PostgreSQL source database. Run the `GRANT` query for all databases
that you migrate to AWS.

```
CREATE USER `your_user` WITH LOGIN PASSWORD '`your_password`';
ALTER USER `your_user` WITH SUPERUSER;
GRANT SELECT ON ALL TABLES IN SCHEMA `schema_name` TO `your_user`;
```

In the preceding example, replace each `user input placeholder`
with your own information.

AWS DMS supports CDC for PostgreSQL tables with primary keys. If a table doesn't have a primary key, the
write-ahead logs (WAL) don't include a before image of the database row. Here, you can use additional
configuration settings and use table replica identity as a workaround. However, this approach can generate
extra logs. We recommend that you use table replica identity as a workaround only after careful testing.
For more information, see [Additional configuration settings
when using a PostgreSQL database as a DMS source](CHAP_Source.md#CHAP_Source.PostgreSQL.Advanced "CHAP_Source.md#CHAP_Source.PostgreSQL.Advanced").

The following sections describe specific configuration prerequisites for self-managed and
AWS-managed PostgreSQL databases.

###### Topics

- [Using a self-managed
  PostgreSQL database as a source for homogeneous data migrations in AWS DMS](#dm-data-providers-source-postgresql-sm "#dm-data-providers-source-postgresql-sm")
- [Using an AWS-managed
  PostgreSQL database as a source for homogeneous data migrations in AWS DMS](#dm-data-providers-source-postgresql-aws "#dm-data-providers-source-postgresql-aws")
- [Limitations for using a
  PostgreSQL compatible database as a source for homogeneous data migrations](#dm-data-providers-source-postgresql-limitations "#dm-data-providers-source-postgresql-limitations")

## Using a self-managed

PostgreSQL database as a source for homogeneous data migrations in AWS DMS

This section describes how to configure your PostgreSQL databases that are hosted on-premises
or on Amazon EC2 instances.

Check the version of your source PostgreSQL database. Make sure that AWS DMS supports
your source PostgreSQL database version as described in [Sources for DMS homogeneous data migrations](CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations "CHAP_Introduction.md#CHAP_Introduction.Sources.HomogeneousDataMigrations").

Homogeneous data migrations support change data capture (CDC) using logical replication.
To turn on logical replication on a self-managed PostgreSQL source database, set the
following parameters and values in the `postgresql.conf`
configuration file:

- Set `wal_level` to `logical`.
- Set `max_replication_slots` to a value greater than 1.

Set the `max_replication_slots` value according to the
number of tasks that you want to run. For example, to run five tasks you
set a minimum of five slots. Slots open automatically as soon as a task
starts and remain open even when the task is no longer running. Make
sure to manually delete open slots.

- Set `max_wal_senders` to a value greater than 1.

The `max_wal_senders` parameter sets the number of
concurrent tasks that can run.

- The `wal_sender_timeout` parameter ends replication connections that
  are inactive longer than the specified number of milliseconds.
  The default is 60000 milliseconds (60 seconds). Setting the value to 0 (zero) disables
  the timeout mechanism, and is a valid setting for DMS.

Some parameters are static, and you can only set them at server start. Any
changes to their entries in the configuration file are ignored until the
server is restarted. For more information, see the [PostgreSQL
documentation](https://www.postgresql.org/docs/current/intro-whatis.html "https://www.postgresql.org/docs/current/intro-whatis.html").

## Using an AWS-managed

PostgreSQL database as a source for homogeneous data migrations in AWS DMS

This section describes how to configure your Amazon RDS for PostgreSQL database instances.

Use the AWS master user account for the PostgreSQL DB instance as the user account
for the PostgreSQL source data provider for homogeneous data migrations in AWS DMS. The master user account has the
required roles that allow it to set up CDC. If you use an account other than the master
user account, then the account must have the `rds_superuser` role and the
`rds_replication` role. The `rds_replication` role grants permissions
to manage logical slots and to stream data using logical slots.

Use the following code example grant the `rds_superuser` and
`rds_replication` roles.

```
GRANT rds_superuser to `your_user`;
GRANT rds_replication to `your_user`;
```

In the preceding example, replace `your_user`
with the name of your database user.

To turn on logical replication, set the `rds.logical_replication` parameter in
your DB parameter group to 1. This static parameter requires a reboot of the DB instance
to take effect.

## Limitations for using a

PostgreSQL compatible database as a source for homogeneous data migrations

The following limitations apply when using a PostgreSQL compatible database as a source for homogeneous data migrations:

- The username you use to connect to your data source has the following limitations:
  - Can be 2 to 64 characters in length.
  - Can't have spaces.
  - Can include the following characters: a-z, A-Z, 0-9, underscore (\_).
  - Must start with a-z or A-Z.

- The password you use to connect to your data source has the following limitations:
  - Can be 1 to 128 characters in length.
  - Can't contain any of the following: single quote ('), double quote ("), semicolon (;) or space.
