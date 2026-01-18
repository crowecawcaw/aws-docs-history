# Databases and schemas for T-SQL

This topic provides reference content comparing database and schema concepts between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can gain insight into how these two database systems differ in their approach to logical containers, security, and object hierarchies.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                     |
| ------------------------------ | ---------------------------------- | ------------------------- | ----------------------------------- |
| Two star feature compatibility | Two star automation level          | N/A                       | Schema and database are synonymous. |

## SQL Server Usage

Databases and schemas are logical containers for security and access control. Administrators can grant permissions collectively at both the databases and the schema levels. SQL Server instances provide security at three levels: individual objects, schemas (collections of objects), and databases (collections of schemas). For more information, see [Data Control Language](chap-sql-server-aurora-mysql.security.md "chap-sql-server-aurora-mysql.security.md").

###### Note

In previous versions of SQL server, the term _user_ was interchangeable with the term _schema_. For backward compatibility, each database has several built-in security schemas including `guest`, `dbo`,
`db_datareaded`, `sys`, `INFORMATION_SCHEMA`, and so on. You should migrate these schemas.

Each SQL Server instance can host and manage a collection of databases, which consist of SQL Server processes and the Master, Model, TempDB, and MSDB system databases.

The most common SQL Server administrator tasks at the database level are:

- **Managing Physical Files** — Add, remove, change file growth settings, and re-size files.
- **Managing Filegroups** — Partition schemes, object distribution, and read-only protection of tables.
- **Managing default options**.
- **Creating database snapshots**.

Unique object identifiers within an instance use three-part identifiers: `<Database name>.<Schema name>.<Object name>`.

The recommended way to view the metadata of database objects, including schemas, is to use the ANSI standard Information Schema views. In most cases, these views are compatible with other ANSI compliant RDBMS.

To view a list of all databases on the server, use the `sys.databases` table.

### Syntax

Simplified syntax for `CREATE DATABASE`:

```
CREATE DATABASE <database name>
[ ON [ PRIMARY ] <file specifications>[,<filegroup>]
[ LOG ON <file specifications>
[ WITH <options specification> ] ;
```

Simplified syntax for CREATE SCHEMA:

```
CREATE SCHEMA <schema name> | AUTHORIZATION <owner name>;
```

### Examples

Add a file to a database and create a table using the new file.

```
USE master;
```

```
ALTER DATABASE NewDB
ADD FILEGROUP NewGroup;
```

```
ALTER DATABASE NewDB
ADD FILE (
    NAME = 'NewFile',
    FILENAME = 'D:\NewFile.ndf',
    SIZE = 2 MB
    )
TO FILEGROUP NewGroup;
```

```
USE NewDB;
```

```
CREATE TABLE NewTable
(
    Col1 INT PRIMARY KEY
)
ON NewGroup;
```

```
SELECT Name
FROM sys.databases
WHERE database_id > 4;
```

Create a table within a new schema and database.

```
USE master
```

```
CREATE DATABASE NewDB;
```

```
USE NewDB;
```

```
CREATE SCHEMA NewSchema;
```

```
CREATE TABLE NewSchema.NewTable
(
    NewColumn VARCHAR(20) NOT NULL PRIMARY KEY
);
```

###### Note

The preceding example uses default settings for the new database and schema.

For more information, see [sys.databases (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=sql-server-ver15"), [CREATE SCHEMA (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-schema-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-schema-transact-sql?view=sql-server-ver15"), and [CREATE DATABASE](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql?view=sql-server-ver15&tabs=sqlpool "https://docs.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql?view=sql-server-ver15&tabs=sqlpool") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) supports both the `CREATE SCHEMA` and `CREATE DATABASE` statements. However, in Aurora MySQL, these statements are synonymous.

Unlike SQL Server, Aurora MySQL doesn’t have the concept of an instance hosting multiple databases, which in turn contain multiple schemas. Objects in Aurora MySQL are referenced as a two part name: `<schema>.<object>`. You can use the term _database_ in place of schema, but it is conceptually the same thing.

###### Note

This terminology conflict can lead to confusion for SQL Server database administrators unfamiliar with the Aurora MySQL concept of a database.

###### Note

Each database and schema in Aurora MySQL is managed as a separate set of physical files similar to an SQL Server database.

Aurora MySQL doesn’t have the concept of a schema owner. Permissions must be granted explicitly. However, Aurora MySQL supports a custom default collation at the schema level, whereas SQL Server supports it at the database level only. For more information, see [Collations](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").

### Syntax

Syntax for CREATE DATABASE:

```
CREATE {DATABASE | SCHEMA} <database name>
[DEFAULT] CHARACTER SET [=] <character set>|
[DEFAULT] COLLATE [=] <collation>
```

### Migration Considerations

Similar to SQL Server, Aurora MySQL supports the USE command to specify the default database or schema for missing object qualifiers.

The syntax is identical to SQL Server:

```
USE <database name>;
```

After you run the `USE` command, the default database for the calling scope is changed to the specified database.

There is a relatively straightforward migration path for a class of common application architectures that use multiple databases but have all objects in a single schema (typically the default `dbo` schema) and require cross database queries. For these types of applications, create an Aurora MySQL Instance and then create multiple databases as you would in SQL Server using the `CREATE DATABASE` command.

Reference all objects using a two-part name instead of a three-part name by omitting the default schema identifier. For application code using the USE command instead of a three-part identifier, no rewrite is needed other than replacing the double dot with a single dot.

```
SELECT * FROM MyDB..MyTable -> SELECT * FROM MyDB.MyTable
```

For applications using a single database and multiple schemas, the migration path is the same and requires fewer rewrites because two-part names are already being used.

Applications that use multiple schemas and multiple databases will need to use multiple instances.

Use the `SHOW DATABASES` command to view databases or schemas in Aurora MySQL.

```
SHOW DATABASES;
```

For the preceding example, the result looks as shown following.

```
database

information_schema
Demo
mysql
performance_schema
sys
```

Aurora MySQL also supports a `CREATE DATABASE` syntax reminder command.

```
SHOW CREATE DATABASE Demo;
```

For the preceding example, the result looks as shown following.

```
Database  Create Database
Demo      CREATE DATABASE `Demo` /*!40100 DEFAULT CHARACTER SET latin1 */
```

### Examples

The following examples create a new table in a new database.

```
CREATE DATABASE NewDatabase;
```

```
USE NewDatabase;
```

```
CREATE TABLE NewTable
(
    NewColumn VARCHAR(20) NOT NULL PRIMARY KEY
);
```

```
INSERT INTO NewTable VALUES('NewValue');
```

```
SELECT * FROM NewTable;
```

## Summary

The following table summarizes the migration path for each architecture.

| Current object architecture                          | Migrate to Aurora MySQL                         | Rewrites                                                                                                                                                            |
| ---------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single database, all objects in dbo schema.          | Single instance, single database or schema.     | If the code already uses two-part object notation such as `dbo.<object>`, consider creating a `dbo` schema in Aurora MySQL to minimize code changes.                |
| Single database, objects in multiple schemas.        | Single instance, multiple databases or schemas. | No identifier hierarchy rewrites needed. Code should be compatible with respect to the object hierarchy.                                                            |
| Multiple databases, all objects in the `dbo` schema. | Single instance, multiple databases or schemas. | Identifier rewrite is required to remove the SQL Server schema name or the default dot. Change `SELECT<br>• FROM MyDB..MyTable` to `SELECT<br>• FROM MyDB.MyTable`. |
| Multiple databases, objects in multiple schemas.     | Multiple instances.                             | Connectivity between the instances will need to be implemented at the application level.                                                                            |

For more information, see [CREATE DATABASE Statement](https://dev.mysql.com/doc/refman/5.7/en/create-database.html "https://dev.mysql.com/doc/refman/5.7/en/create-database.html") in the _MySQL documentation_.
