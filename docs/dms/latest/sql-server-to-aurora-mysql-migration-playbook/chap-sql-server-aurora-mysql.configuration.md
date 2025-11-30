# Configuring database options

This topic provides reference information about database options in Microsoft SQL Server and how they differ from Amazon Aurora MySQL. You can understand the key differences in database configuration between these two database systems.

| Feature compatibility    | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                               |
| ------------------------ | ---------------------------------- | ------------------------- | ------------------------------------------------------------- |
| No feature compatibility | N/A                                | N/A                       | SQL Server database options are inapplicable to Aurora MySQL. |

## SQL Server Usage

SQL Server provides database level options that can be set using the `ALTER DATABASE …​ SET` command.

These settings enable you to:

- Set default session options. For more information, see [Session Options](chap-sql-server-aurora-mysql.configuration.md "chap-sql-server-aurora-mysql.configuration.md").
- Turn on or turn off database features such as `SNAPSHOT_ISOLATION`, `CHANGE_TRANCKING`, and `ENABLE_BROKER`.
- Configure high availability and disaster recovery options such as always on availability groups
- Configure security access control such as restricting access to a single user, setting the database offline, or setting the database to read-only.

### Syntax

Use the following syntax to set database options:

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

## MySQL Usage

The concept of a database in Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) is different than SQL Server. In Aurora MySQL, a database is synonymous with a schema. Therefore, the notion of database options isn’t applicable to Aurora MySQL.

###### Note

Aurora MySQL has two settings that are saved with the database/schema: the default character set, and the default collation for creating new objects.

## Migration Considerations

For migration considerations, see [Server Options](chap-sql-server-aurora-mysql.configuration.md "chap-sql-server-aurora-mysql.configuration.md").
