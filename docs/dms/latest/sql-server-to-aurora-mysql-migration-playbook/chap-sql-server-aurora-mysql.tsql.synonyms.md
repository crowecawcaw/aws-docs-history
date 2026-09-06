

# Synonyms for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.synonyms"></a>

This topic provides reference information about the compatibility of synonyms between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can understand the differences in how these database systems handle synonyms, which are alternative identifiers for database objects.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![One star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-1.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-0.png)  |  [Synonyms](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.synonyms)  | Use stored procedures and functions to abstract instance-wide objects. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.synonyms.sqlserver"></a>

Synonyms are database objects that server as alternative identifiers for other database objects. The referenced database object is called the *base object* and may reside in the same database, another database on the same instance, or a remote server.

Synonyms provide an abstraction layer to isolate client application code from changes to the name or location of the base object.

In SQL Server, synonyms are often used to simplify the use of four-part identifiers when accessing remote instances.

For example, table A resides on server A, and the client application accesses it directly. For scale out reasons, table A needs to be moved to server B to offload resource consumption on server A. Without synonyms, the client application code must be rewritten to access server B. Instead, you can create a synonym called table A and it will transparently redirect the calling application to Server B without any code changes.

You can create synonyms for the following objects:
+ Assembly stored procedures, table-valued functions, scalar functions, and aggregate functions.
+ Replication filter procedures.
+ Extended stored procedures.
+ SQL scalar functions, table-valued functions, inline-tabled-valued functions, views, and stored procedures.
+ User-defined tables including local and global temporary tables.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.synonyms.sqlserver.syntax"></a>

```
CREATE SYNONYM [ <Synonym Schema> ] . <Synonym Name>
FOR [ <Server Name> ] . [ <Database Name> ] . [ Schema Name> ] . <Object Name>
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.synonyms.sqlserver.examples"></a>

Create a synonym for a local object in a separate database.

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

Create a synonym for a remote object.

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

**Note**  
This example assumes a linked server named server A exists on server B that points to server A.

For more information, see [CREATE SYNONYM (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/statements/create-synonym-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.synonyms.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) doesn’t support synonyms and there is no known generic workaround.

For accessing tables or views, a partial workaround is to use encapsulating views as an abstraction layer. Similarly, you can use functions or stored procedures that call other functions or stored procedures.

**Note**  
Synonyms are often used in conjunction with linked servers, which aren’t supported by Aurora MySQL.

For more information, see [Linked Servers](chap-sql-server-aurora-mysql.management.linkedservers.md), [Views](chap-sql-server-aurora-mysql.sql.views.md), [User-Defined Functions](chap-sql-server-aurora-mysql.tsql.udf.md), and [Stored Procedures](chap-sql-server-aurora-mysql.tsql.storedprocedures.md).