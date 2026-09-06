

# Linked servers
<a name="chap-sql-server-aurora-pg.management.linkedservers"></a>

This topic provides reference information about linked servers in SQL Server and their equivalent functionality in PostgreSQL. You can understand how linked servers enable SQL Server to connect to external data sources, allowing for distributed queries and data access across heterogeneous systems. The topic explains the benefits of using linked servers, how they are configured, and the methods for accessing remote data.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  | N/A |  [Linked Servers](chap-sql-server-aurora-pg.tools.actioncode.md#chap-sql-server-aurora-pg.tools.actioncode.linkedservers)  | Syntax and option differences, similar functionality. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-pg.management.linkedservers.sqlserver"></a>

Linked servers enable the database engine to connect to external Object Linking and Embedding for databases (OLE-DB) sources. They are typically used to run T-SQL commands and include tables in other instances of SQL Server, or other RDBMS engines such as Oracle. SQL Server supports multiple types of OLE-DB sources as linked servers, including Microsoft Access, Microsoft Excel, text files and others.

The main benefits of using linked servers are:
+ Reading external data for import or processing.
+ Running distributed queries, data modifications, and transactions for enterprise-wide data sources.
+ Querying heterogeneous data source using the familiar T-SQL API.

You can configure linked servers using either SQL Server Management Studio, or the system stored procedure `sp_addlinkedserver`. The available functionality and the specific requirements vary significantly between the various OLE-DB sources. Some sources may allow read only access, others may require specific security context settings, and so on.

The linked server definition contains the linked server alias, the OLE DB provider, and all the parameters needed to connect to a specific OLE-DB data source.

The OLE-DB provider is a .NET Dynamic Link Library (DLL) that handles the interaction of SQL Server with all data sources of its type. For example, OLE-DB Provider for Oracle. The OLE-DB data source is the specific data source to be accessed, using the specified OLE-DB provider.

**Note**  
You can use SQL Server distributed queries with any custom OLE DB provider as long as the required interfaces are implemented correctly.

SQL Server parses the T-SQL commands that access the linked server and sends the appropriate requests to the OLE-DB provider. There are several access methods for remote data, including opening the base table for read or issuing SQL queries against the remote data source.

You can manage linked servers using SQL Server Management Studio graphical user interface or T-SQL system stored procedures.
+  `EXECUTE sp_addlinkedserver` to add new server definitions.
+  `EXECUTE sp_addlinkedserverlogin` to define security context.
+  `EXECUTE sp_linkedservers` or `SELECT * FROM sys.servers` system catalog view to retrieve meta data.
+  `EXECUTE sp_dropserver` to delete a linked server.

You can access linked server data sources from T-SQL using a fully qualified, four-part naming scheme: `<Server Name>.<Database Name>.<Schema Name>.<Object Name>`.

Additionally, you can use the `OPENQUERY` row set function to explicitly invoke pass-through queries on the remote linked server. Also, you can use the `OPENROWSET` and `OPENDATASOURCE` row set functions for one-time remote data access without defining the linked server in advance.

### Syntax
<a name="chap-sql-server-aurora-pg.management.linkedservers.sqlserver.syntax"></a>

```
EXECUTE sp_addlinkedserver
    [ @server= ] <Linked Server Name>
    [ , [ @srvproduct= ] <Product Name>]
    [ , [ @provider= ] <OLE DB Provider>]
    [ , [ @datasrc= ] <Data Source>]
    [ , [ @location= ] <Data Source Address>]
    [ , [ @provstr= ] <Provider Connection String>]
    [ , [ @catalog= ] <Database>];
```

### Examples
<a name="chap-sql-server-aurora-pg.management.linkedservers.sqlserver.examples"></a>

Create a linked server to a local text file.

```
EXECUTE sp_addlinkedserver MyTextLinkedServer, N'Jet 4.0',
    N'Microsoft.Jet.OLEDB.4.0',
    N'D:\TextFiles\MyFolder',
    NULL,
    N'Text';
```

Define security context.

```
EXECUTE sp_addlinkedsrvlogin MyTextLinkedServer, FALSE, Admin, NULL;
```

Use `sp_tables_ex` to list tables in a folder.

```
EXEC sp_tables_ex MyTextLinkedServer;
```

Issue a `SELECT` query using a four-part name.

```
SELECT *
FROM MyTextLinkedServer...[FileName#text];
```

For more information, see [sp\_addlinkedserver (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlinkedserver-transact-sql?view=sql-server-ver15) and [Distributed Queries Stored Procedures (Transact-SQL)](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/distributed-queries-stored-procedures-transact-sql?view=sql-server-ver15) in the *SQL Server documentation*.

## PostgreSQL Usage
<a name="chap-sql-server-aurora-pg.management.linkedservers.pg"></a>

Querying data in remote databases is available through two primary options:
+  `dblink` database link function.
+ Foreign data wrapper (FDW) `postgresql_fdw` extension.

The PostgreSQL foreign data wrapper extension is new to PostgreSQL and provides functionality similar to `dblink`. However, the PostgreSQL foreign data wrapper aligns closer with the SQL standard and can provide improved performance.

### Examples
<a name="chap-sql-server-aurora-pg.management.linkedservers.pg.examples"></a>

Load the `dblink` extension into PostgreSQL.

```
CREATE EXTENSION dblink;
```

Create a persistent connection to a remote PostgreSQL database using the `dblink_connect` function specifying a connection name (`myconn`), database name (`postgresql`), port (`5432`), host (`hostname`), user (`username`), and password (`password`).

```
SELECT dblink_connect ('myconn',
    'dbname=postgres port=5432 host=hostname user=username password=password');
```

You can use the connection to run queries against the remote database.

Run a query using the previously created `myconn` connection by using the `dblink` function. The query returns the id and name columns from the employees table. On the remote database, you must specify the connection name and the SQL query to run as well as parameters and datatypes for selected columns (id and name in this example).

```
SELECT * from dblink ('myconn',
    'SELECT id, name FROM EMPLOYEES') AS p(id int,fullname text);
```

Close the connection using the `dblink_disconnect` function.

```
SELECT dblink_disconnect('myconn');
```

Alternatively, you can use the `dblink` function specifying the full connection string to the remote PostgreSQL database including the database name, port, hostname, username, and password. You can do this instead of using a previously defined connection. Make sure that you specify the SQL query to run as well as parameters and data types for the selected columns (id and name, in this example).

```
SELECT * from dblink ('dbname=postgres port=5432 host=hostname user=username password=password',
    'SELECT id, name FROM EMPLOYEES') AS p(id int,fullname text);
```

DML commands are supported on tables referenced by the `dblink` function. For example, you can insert a new row and then delete it from the remote table.

```
SELECT * FROM dblink('myconn',$$INSERT into employees VALUES (3,'New Employees No. 3!')$$) AS t(message text);

SELECT * FROM dblink('myconn',$$DELETE FROM employees WHERE id=3$$) AS t(message text);
```

Create a new `new_employees_table` local table by querying data from a remote table.

```
SELECT emps.* INTO new_employees_table
    FROM dblink('myconn','SELECT * FROM employees')
    AS emps(id int, name varchar);
```

Join remote data with local data.

```
SELECT local_emps.id , local_emps.name, s.sale_year, s.sale_amount
    FROM local_emps INNER JOIN
    dblink('myconn','SELECT * FROM working_hours') AS s(id int, hours worked int)
    ON local_emps.id = s.id;
```

Run DDL statements in the remote database.

```
SELECT * FROM dblink('myconn',$$CREATE table new_remote_tbl (a int, b text)$$) AS t(a text);
```

For more information, see [dblink](https://www.postgresql.org/docs/13/dblink.html) in the *PostgreSQL documentation*.