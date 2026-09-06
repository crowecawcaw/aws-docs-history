

# Databases and schemas for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.schemas"></a>

This topic provides reference information comparing database and schema structures between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can gain insights into how these database management systems handle logical containers for security and access control. The topic explores the similarities and differences in how databases, schemas, and objects are organized and referenced in both systems.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Five star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-5.png)  |  ![Five star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-5.png)  | N/A | N/A | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.schemas.sqlserver"></a>

Databases and schemas are logical containers for security and access control. Administrators can grant permissions collectively at both the databases and the schema levels. SQL Server instances provide security at three levels: individual objects, schemas (collections of objects), and databases (collections of schemas). For more information, see [Data Control Language](chap-sql-server-aurora-pg.security.datacontrollanguage.md).

**Note**  
In previous versions of SQL server, the term user was interchangeable with the term schema. For backward compatibility, each database has several built-in security schemas including `guest`, `dbo`, `db_datareaded`, `sys`, `INFORMATION_SCHEMA`, and others. Most likely, you don’t need to migrate these schemas.

Each SQL Server instance can host and manage a collection of databases, which consists of SQL Server processes and the Master, Model, TempDB, and MSDB system databases.

The most common SQL Server administrator tasks at the database level are:
+ Managing physical files: add, remove, change file growth settings, and re-size files.
+ Managing filegroups: partition schemes, object distribution, and read-only protection of tables.
+ Managing default options.
+ Creating database snapshots.

Unique object identifiers within an instance use three-part identifiers: <Database name>.<Schema name>.<Objectname>.

The recommended way to view database object meta data, including schemas, is to use the ANSI standard information schema views. In most cases, these views are compatible with other ANSI-compliant Relational Database Management Systems (RDBMS).

To view a list of all databases on the server, use the sys.databases table.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.schemas.sqlserver.syntax"></a>

Simplified syntax for `CREATE DATABASE`.

```
CREATE DATABASE <database name>
[ ON [ PRIMARY ] <file specifications>[,<filegroup>]
[ LOG ON <file specifications>
[ WITH <options specification> ] ;
```

Simplified syntax for `CREATE SCHEMA`.

```
CREATE SCHEMA <schema name> | AUTHORIZATION <owner name>;
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.schemas.sqlserver.examples"></a>

The following example adds a file to a database and creates a table using the new file.

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

The following example creates a table within a new schema and database.

```
USE master
CREATE DATABASE NewDB;

USE NewDB;
CREATE SCHEMA NewSchema;

CREATE TABLE NewSchema.NewTable
(
  NewColumn VARCHAR(20) NOT NULL PRIMARY KEY
);
```

This example uses default settings for the new database and schema.

For more information, see [sys.databases (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-catalog-views/sys-databases-transact-sql?view=sql-server-ver15), [CREATE SCHEMA (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-schema-transact-sql?view=sql-server-ver15), and [CREATE DATABASE](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-database-transact-sql?view=sql-server-ver15&tabs=sqlpool) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.schemas.pg"></a>

 Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) supports both the `CREATE SCHEMA` and `CREATE DATABASE` statements.

As with SQL Server, Aurora PostgreSQL does have the concept of an instance hosting multiple databases, which in turn contain multiple schemas. Objects in Aurora PostgreSQL are referenced as a three-part name: `<database>.<schema>.<object>`.

A schema is essentially a namespace that contains named objects.

When database is created, it is cloned from a template.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.schemas.pg.syntax"></a>

Syntax for `CREATE DATABASE`.

```
CREATE DATABASE name
  [ [ WITH ] [ OWNER [=] user_name ]
    [ TEMPLATE [=] template ]
    [ ENCODING [=] encoding ]
    [ LC_COLLATE [=] lc_collate ]
    [ LC_CTYPE [=] lc_ctype ]
    [ TABLESPACE [=] tablespace_name ]
    [ ALLOW_CONNECTIONS [=] allowconn ]
    [ CONNECTION LIMIT [=] connlimit ]
    [ IS_TEMPLATE [=] istemplate ] ]
```

Syntax for `CREATE SCHEMA`.

```
CREATE SCHEMA schema_name [ AUTHORIZATION role_specification ] [ schema_element [ ... ] ]
CREATE SCHEMA AUTHORIZATION role_specification [ schema_element [ ... ] ]
CREATE SCHEMA IF NOT EXISTS schema_name [ AUTHORIZATION role_specification ]
CREATE SCHEMA IF NOT EXISTS AUTHORIZATION role_specification

where role_specification can be:
user_name | CURRENT_USER | SESSION_USER
```

### Migration Considerations
<a name="chap-sql-server-aurora-pg.tsql.schemas.pg.considerations"></a>

Unlike SQL Server, Aurora PostgreSQL doesn’t support the `USE` command to specify the default database or schema for missing object qualifiers. To use a different database, use a new connection, obtain the required permissions, and refer to the object using the database name.

For applications using a single database and multiple schemas, the migration path is the same and requires fewer rewrites because two-part names are already being used.

Query the `postgres.pg_catalog.pg_database` table to view databases in Aurora PostgreSQL.

```
SELECT datname, datcollate, datistemplate, datallowconn
FROM postgres.pg_catalog.pg_database;

datname    datcollate   datistemplate  datallowconn
template0  en_US.UTF-8  true           false
rdsadmin   en_US.UTF-8  false          true
template1  en_US.UTF-8  true           true
postgres   en_US.UTF-8  false          true
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.schemas.pg.examples"></a>

The following example creates a new database.

```
CREATE DATABASE NewDatabase;
```

The following example creates a schema for user testing.

```
CREATE SCHEMA AUTHORIZATION joe;
```

The following example creates a schema, a table and a view.

```
CREATE SCHEMA world_flights
  CREATE TABLE flights (flight_id VARCHAR(10), departure DATE, airport VARCHAR(30))
  CREATE VIEW us_flights AS
    SELECT flight_id, departure FROM flights WHERE airport='United States';
```

For more information, see [CREATE DATABASE](https://www.postgresql.org/docs/13/sql-createdatabase.html) and [CREATE SCHEMA](https://www.postgresql.org/docs/13/sql-createschema.html) in the *PostgreSQL documentation*.