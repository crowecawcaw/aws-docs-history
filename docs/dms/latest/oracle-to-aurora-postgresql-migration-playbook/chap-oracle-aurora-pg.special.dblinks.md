

# Oracle database links and PostgreSQL dblink and fdwrapper
<a name="chap-oracle-aurora-pg.special.dblinks"></a>

With AWS DMS, you can integrate heterogeneous database systems by creating database links between different database management systems. Oracle database links and PostgreSQL dblink/fdwrapper facilitate access to data in remote databases from a local database, enabling queries and data manipulation across distributed environments.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-compatibility-3.png)  |  ![No automation](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-postgresql-migration-playbook/images/pb-automation-0.png)  |  [Database Links](chap-oracle-aurora-pg.tools.actioncode.md#chap-oracle-aurora-pg.tools.actioncode.databaselinks)  | Different paradigm and syntax | 

## Oracle usage
<a name="chap-oracle-aurora-pg.special.dblinks.ora"></a>

Database links are schema objects used to interact with remote database objects such as tables. Common use cases for database links include selecting data from tables that reside in a remote database.

To use database links, Oracle net services must be installed on both the local and remote database servers to facilitate communications.

 **Examples** 

Create a database link named remote\_db. When creating a database link, you have the option to specify the remote database destination using a TNS Entry or to specify the full TNS Connection string.

```
CREATE DATABASE LINK remote_db CONNECT TO username IDENTIFIED BY password USING 'remote';
CREATE DATABASE LINK remotenoTNS CONNECT TO username IDENTIFIED BY password
  USING '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS = (PROTOCOL = TCP)(HOST =192.168.1.1)
  (PORT =1521)))(CONNECT_DATA =(SERVICE_NAME = orcl)))';
```

After the database link is created, you can use the database link directly as part of a SQL query using the database link name (@remote\_db) as a suffix to the table name.

```
SELECT * FROM employees@remote_db;
```

Database links also support DML commands.

```
INSERT INTO employees@remote_db
(employee_id, last_name, email, hire_date, job_id) VALUES
(999, 'Claus', 'sclaus@example.com', SYSDATE, 'SH_CLERK');

UPDATE jobs@remote_db SET min_salary = 3000 WHERE job_id = 'SH_CLERK';

DELETE FROM employees@remote_db WHERE employee_id = 999;
```

For more information, see [Managing Database Links](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-a-distributed-database.html#GUID-7B0C4627-4473-4313-88D5-FD03CA42D9EA) in the *Oracle documentation*.

## PostgreSQL usage
<a name="chap-oracle-aurora-pg.special.dblinks.pg"></a>

Querying data in remote databases in PostgreSQL is available through two primary options:

1.  `dblink` database link function.

1.  `postgresql_fdw` (Foreign Data Wrapper, FDW) extension.

The PostgreSQL foreign data wrapper extension is new to PostgreSQL and offers functionality that is similar to dblink. However, the PostgreSQL foreign data wrapper aligns closer with the SQL standard and can provide improved performance.

 **Example of using dblink** 

Load the `dblink` extension into PostgreSQL.

```
CREATE EXTENSION dblink;
```

Create a persistent connection to a remote PostgreSQL database using the dblink\_connect function specifying a connection name (myconn), database name (postgresql), port (5432), host (hostname), user (username) and password (password).

```
SELECT dblink_connect
('myconn', 'dbname=postgres port=5432
host=hostname user=username password=password');
```

The connection can be used to run queries against the remote database.

Run a query using the previously created connection (myconn) using the dblink function.

The query returns the id and name columns from the employees table. On the remote database, you must specify the connection name and the SQL query to execute as well as parameters and datatypes for selected columns (id and name in this example).

```
SELECT * from dblink
('myconn', 'SELECT id, name FROM EMPLOYEES')
AS p(id int,fullname text);
```

Close the connection using the dblink\_disconnect function.

```
SELECT dblink_disconnect('myconn');
```

Alternatively, you can use the `dblink` function specifying the full connection string to the remote PostgreSQL database, including: database name, port, hostname, username, and password. This can be done instead of using a previously defined connection. You must also specify the SQL query to run as well as parameters and datatypes for the selected columns (id and name, in this example).

```
SELECT * from dblink
('dbname=postgres port=5432 host=hostname user=username password=password',
'SELECT id, name FROM EMPLOYEES') AS p(id int,fullname text);
```

DML commands are supported on tables referenced through the `dblink` function. For example, you can insert a new row and then delete it from the remote table.

```
SELECT * FROM dblink('myconn',$$INSERT into employees
VALUES (3,'New Employees No.3!')$$) AS t(message text);

SELECT * FROM dblink('myconn',$$DELETE FROM employees
WHERE id=3$$) AS t(message text);
```

Create a new local `new_employees_table` table by querying data from a remote table.

```
SELECT emps.* INTO new_employees_table
FROM dblink('myconn','SELECT * FROM employees')
AS emps(id int, name varchar);
```

Join remote data with local data.

```
SELECT local_emps.id , local_emps.name, s.sale_year, s.sale_amount
FROM local_emps INNER JOIN
dblink('myconn','SELECT * FROM working_hours')
AS s(id int, hours worked int)
ON local_emps.id = s.id;
```

Run DDL statements in the remote database.

```
SELECT * FROM dblink('myconn',$$CREATE table new_remote_tbl
(a int, b text)$$) AS t(a text);
```

For more information, see [dblink](https://www.postgresql.org/docs/13/dblink.html) in the *PostgreSQL documentation*.

 **Example of using the PostgreSQL Foreign Data Wrapper** 

Load the fdw extension into PostgreSQL.

```
CREATE EXTENSION postgres_fdw;
```

Create a connection to the remote PostgreSQL database specifying the remote server (hostname), database name (postgresql) and the port (5432).

```
CREATE SERVER remote_db
FOREIGN DATA WRAPPER postgres_fdw
OPTIONS (host 'hostname', dbname 'postgresql', port '5432');
```

Create the user mapping, specifying the local\_user is a user with permissions in the current database, the server connection created in the previous command (remote\_db), and the user and password arguments specified in the options clause must have the required permissions in the remote database.

```
CREATE USER MAPPING FOR local_user
SERVER remote_db
OPTIONS (user 'remote_user', password 'remote_password');
```

After the connection with login credentials for the remote database was created, we can either import individual tables or the entire schema containing all, or some, of the tables and views.

Create a `FOREIGN TABLE` named `foreign_emp_tbl` using the remote\_db remote connection created earlier specifying both the schema name and table name in the remote database to be queried. For example, the `hr.employees` table.

```
CREATE FOREIGN TABLE foreign_emp_tbl (
  id int, name text)
  SERVER remote_db
  OPTIONS (schema_name 'hr', table_name 'employees');
```

Queries running on the local `foreign_emp_tbl` table will actually query data directly from the remote `hr.employees` table.

```
SELECT * FROM foreign_emp_tbl;
```

You can also import an entire schema, or specific tables, without specifying a specific table name.

```
IMPORT FOREIGN SCHEMA hr LIMIT TO (employees)
FROM SERVER remote_db INTO local_hr;
```

Both dblink and FDW store the remote database username and password as plain-text, in two locations:
+ The pg\_user\_mapping view, accessible only to “super users” in the database.
+ When using the dblink function, passwords can be stored in your code or procedures inside the database.

Any changes to PostgreSQL user passwords require changing the FDW/dblink specifications as well.

When using FDW, if columns in the remote tables have been dropped or renamed, the queries will fail. The FDW tables must be re-created.

### PostgreSQL dblink compared to PostgreSQL foreign data wrapper
<a name="chap-oracle-aurora-pg.special.dblinks.pg.compare"></a>


| Description | PostgreSQL dblink | PostgreSQL Foreign Data Wrapper | 
| --- | --- | --- | 
| Create a permanent reference to a remote table using a database link | Not supported | After creating: define DFW server, create user mapping, and run.<pre>CREATE FOREIGN TABLE foreign_emp_tbl<br />(id int, name text, address text )<br />SERVER foreign_server<br />OPTIONS (schema_name 'hr',<br />table_name 'employees');</pre> | 
| Query remote data |  <pre>SELECT * FROM dblink('myconn',<br />  'SELECT * FROM employees')<br />  AS p(id int,fullname text,<br />  address text);</pre>  |  <pre>SELECT * FROM foreign_emp_tbl;</pre>  | 
| DML on remote data |  <pre>SELECT * FROM dblink('myconn',<br />$$INSERT into employees<br />VALUES (45,'Dan','South side 7432,<br />NY')$$) AS t(id int, name text,<br />address text);</pre>  |  <pre>INSERT into foreign_emp_tb<br />VALUES (45,'Dan','South side 7432,<br />NY'); (Regular DML)</pre>  | 
| Run DDL on remote objects |  <pre>SELECT * FROM dblink ('myconn',$$CREATE table<br />my_remote_tbl (a int, b text)$$) AS t(a text);</pre>  | Not supported | 

## Summary
<a name="chap-oracle-aurora-pg.special.dblinks.summary"></a>


| Description | Oracle | PostgreSQL dblink | 
| --- | --- | --- | 
| Create a permanent named database link |  <pre>CREATE DATABASE LINK remote<br />CONNECT TO username IDENTIFIED<br />BY password USING 'remote';</pre>  | Not Supported. You have to manually open the connection to the remote database in your sessions / queries:<pre>SELECT dblink_connect('myconn',<br />'dbname=postgres port=5432<br />hostt=hostname user=username<br />password=password');</pre> | 
| Query using a database link |  <pre>SELECT * FROM employees@remote;</pre>  |  <pre>SELECT * FROM dblink<br />('myconn','SELECT * FROM employees')<br /> AS p(id int,fullname text, address text);</pre>  | 
| DML using database link |  <pre>INSERT INTO employees@remote<br />(employee_id, last_name, email,<br />hire_date, job_id) VALUES (999,<br />'Claus','sclaus@example.com',<br />SYSDATE,'SH_CLERK');</pre>  |  <pre>SELECT * FROM dblink<br />('myconn',$$INSERT into employees<br />VALUES (45,'Dan','South side 7432, NY'<br />)$$) AS t(id int, name text, address text);</pre>  | 
| Heterogeneous database link connections, such as Oracle to PostgreSQL or vice-versa | Supported. | Create extension oracle\_fdw not supported by Amazon RDS. | 
| Run DDL using a database link | Not supported directly, but you can run a procedure or create a job on the remote database and runs the desired DDL commands.<pre>dbms_job@remote.submit(<br />  l_job, 'execute immediate<br />  ''create table t ( x int)'''<br />  ); commit;</pre> |  <pre>SELECT * FROM dblink (<br />  'myconn',$$CREATE table my_remote_tbl<br />  (a int, b text)$$) AS t(a text);</pre>  | 
| Delete a database link |  <pre>drop database link remote;</pre>  | Not supported. Close the DBLink connection instead.<pre>SELECT dblink_disconnect ('myconn');</pre> | 

For more information, see [postgres\_fdw](https://www.postgresql.org/docs/13/postgres-fdw.html) in the *PostgreSQL documentation*.