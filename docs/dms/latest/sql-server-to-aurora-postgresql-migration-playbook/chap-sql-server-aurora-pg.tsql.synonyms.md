

# Synonyms for T-SQL
<a name="chap-sql-server-aurora-pg.tsql.synonyms"></a>

This topic provides reference information about the differences in synonym functionality between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. You can understand how SQL Server uses synonyms as alternative identifiers for database objects and how this feature is not directly supported in PostgreSQL. The topic explains the purpose and benefits of synonyms in SQL Server, such as providing an abstraction layer and simplifying the use of four-part identifiers for remote instances.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-2.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  | N/A | PostgreSQL doesn’t support synonyms. There is an available workaround. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.tsql.synonyms.sqlserver"></a>

Synonyms are database objects that serve as alternative identifiers for other database objects. The referenced database object is called the base object and may reside in the same database, another database on the same instance, or a remote server.

Synonyms provide an abstraction layer to isolate client application code from changes to the name or location of the base object.

In SQL Server, synonyms are often used to simplify the use of four-part identifiers when accessing remote instances.

For example, the table A resides on the server A, and the client application accesses it directly. For scale out reasons, the table A needs to be moved to the server B to offload resource consumption on the server A. Without synonyms, the client application code must be rewritten to access the server B. Instead, you can create a synonym called Table A and it will transparently redirect the calling application to the server B without any code changes.

You can create synonyms for the following objects:
+ Assembly (CLR) stored procedures, table-valued functions, scalar functions, and aggregate functions.
+ Replication-filter-procedures.
+ Extended stored procedures.
+ SQL scalar functions, table-valued functions, inline-tabled-valued functions, views, and stored procedures.
+ User-defined tables including local and global temporary tables.

### Syntax
<a name="chap-sql-server-aurora-pg.tsql.synonyms.sqlserver.syntax"></a>

```
CREATE SYNONYM [ <Synonym Schema> ] . <Synonym Name>
FOR [ <Server Name> ] . [ <Database Name> ] . [ Schema Name> ] . <Object Name>
```

### Examples
<a name="chap-sql-server-aurora-pg.tsql.synonyms.sqlserver.examples"></a>

The following example creates a synonym for a local object in a separate database.

```
CREATE TABLE DB1.Schema1.MyTable
(
KeyColumn INT IDENTITY PRIMARY KEY,
DataColumn VARCHAR(20) NOT NULL
);

USE DB2;
CREATE SYNONYM Schema2.MyTable
FOR DB1.Schema1.MyTable
```

The following example creates a synonym for a remote object.

```
-- On ServerA
CREATE TABLE DB1.Schema1.MyTable
(
KeyColumn INT IDENTITY PRIMARY KEY,
DataColumn VARCHAR(20) NOT NULL
);

-- On Server B
USE DB2;
CREATE SYNONYM Schema2.MyTable
FOR ServerA.DB1.Schema1.MyTable;
```

The example preceding assumes a linked server named ServerA exists on Server B that points to Server A.

For more information, see [CREATE SYNONYM (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-synonym-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.tsql.synonyms.pg"></a>

SQL Server synonyms are often used to give another name for an object. PostgreSQL doesn’t provide a feature comparable to SQL Server Synonyms. However, you can achieve similar functionality by using a few PostgreSQL objects.

 AWS SCT converts different source databases into one target database. Each source database becomes a schema in the new target database. AWS SCT adds the name of the source schemas as a prefix to the name of the target database schema. If you migrate several databases as part of one migration project, then you can avoid using synonyms because all converted objects are in the same database.

This lack of functionality in PostgreSQL adds a manual dimension to the migration process of SQL Server synonyms. Make sure that your database user has privileges on the base object and the relevant PostgreSQL options.

### Examples
<a name="chap-sql-server-aurora-pg.tsql.synonyms.pg.examples"></a>

To create a synonym of a table in PostgreSQL, use views.

The first step is to create a table that will be used as the base object, and on top of it, a view that will be used as synonym.

```
CREATE TABLE target_db_name.DB1_Schema1.MyTable
(
  KeyColumn NUMERIC PRIMARY KEY,
  DataColumn VARCHAR(20) NOT NULL
);

CREATE VIEW target_db_name.DB2_Schema2.MyTable_Syn
AS SELECT * FROM target_db_name.DB1_Schema1.MyTable
```

For more information, see [Views](chap-sql-server-aurora-pg.sql.views.md).

To create a synonym of a user-defined type in PostgreSQL, another user-defined type should be used to wrap the source type.

The first step is to create the user-defined type that will be used as the base object, and on top of it, a user-defined type that will be used as the synonym.

```
CREATE TYPE DB1.Schema1.MyType AS (
ID NUMERIC,
name CHARACTER VARYING(100));

CREATE TYPE DB2.Schema2.MyType_Syn AS (
udt DB1.Schema1.MyT);
```

For more information, see [User-Defined Types](chap-sql-server-aurora-pg.tsql.udt.md).

To create a synonym for a function in PostgreSQL, another function should be used to wrap the source type.

As before, the first step is to create the function that will be used as the base object. And then, on top of it, create a function that will be used as the synonym.

```
CREATE OR REPLACE FUNCTION DB1.Schema1.MyFunc (P_NUM NUMERIC)
RETURNS numeric AS $$
begin
  RETURN P_NUM * 2;
END; $$
LANGUAGE PLPGSQL;

CREATE OR REPLACE FUNCTION DB2.Schema2.MyFunc_Syn (P_NUM NUMERIC)
RETURNS numeric AS $$
begin
  RETURN DB1.Schema1.MyFunc(P_NUM);
END; $$
LANGUAGE PLPGSQL;
```

For more information, see [User-Defined Functions](chap-sql-server-aurora-pg.tsql.udf.md).