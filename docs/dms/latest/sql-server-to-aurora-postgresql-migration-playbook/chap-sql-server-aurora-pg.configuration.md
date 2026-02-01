# Configuring database options

This topic provides reference information about the differences in database options and features between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can understand how SQL Server’s database-level options and features translate to cluster and instance-level parameters. The topic helps you grasp the architectural differences between the two database systems, particularly in terms of database configuration, security settings, and high availability options.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| ------------------------------ | ---------------------------------- | ------------------------- | --------------- |
| One star feature compatibility | N/A                                | N/A                       | Difference.     |

## SQL Server Usage

SQL Server provides database level options that you can set using the `ALTER DATABASE …​ SET` command. You can use these settings to:

- Set default session options. For more information, see [Session Options](chap-sql-server-aurora-pg.configuration.md "chap-sql-server-aurora-pg.configuration.md").
- Enable or disable database features such as `SNAPSHOT_ISOLATION`, `CHANGE_TRANCKING`, and `ENABLE_BROKER`.
- Configure high availability and disaster recovery options such as always on availability groups.
- Configure security access control such as restricting access to a single user, setting the database offline, or setting the database to read-only.

### Syntax

Syntax for setting database options:

```
ALTER DATABASE { <database name> } SET { <option> [ ,...n ] };
```

### Examples

Set a database to read-only and use ARITHABORT by default.

```
ALTER DATABASE Demo SET READ_ONLY, ARITHABORT ON;
```

Set a database to use automatic statistic creation.

```
ALTER DATABASE Demo SET AUTO_CREATE_STATISTICS ON;
```

Set a database offline immediately.

```
ALTER DATABASE DEMO SET OFFLINE WITH ROLLBACK IMMEDIATE;
```

For more information, see [ALTER DATABASE SET options (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-set-options?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports `CREATE SCHEMA` and `CREATE DATABASE` statements.

As with SQL Server, Aurora PostgreSQL does have the concept of an instance hosting multiple databases, which in turn contain multiple schemas. Objects in Aurora PostgreSQL are referenced as a three-part name: `<database>.<schema>.<object>`.

Database options are related to the cluster-level parameters which are managed by the AWS Cluster Parameter Groups. You can find some SQL Server equivalent parameters at the instance level in the AWS Database Parameter Group.

Datable options are being compared to AWS Database Parameter Group and Server Options are being compared to AWS Cluster Parameter Group. For more information, see [Server Options](chap-sql-server-aurora-pg.configuration.md "chap-sql-server-aurora-pg.configuration.md").
