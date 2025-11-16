# Oracle database links and MySQL fully-qualified table names

With AWS DMS, you can migrate data between different database platforms, including Oracle and MySQL, while preserving database links and fully-qualified table names. Oracle database links provide a way to access data in remote databases, while MySQL fully-qualified table names specify the database and table for a given object.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                       |
| ------------------------------ | ---------------------------------- | ------------------------- | ------------------------------------- |
| Two star feature compatibility | N/A                                | N/A                       | MySQL doesn’t support database links. |

## Oracle usage

Database links are schema objects used to interact with remote database objects such as tables. Common use cases for database links include selecting data from tables that reside in a remote database.

To use database links, Oracle net services must be installed on both the local and remote database servers to facilitate communications.

### Examples

Create a database link named `remote_db`. When creating a database link, you have the option to specify the remote database destination using a TNS Entry or to specify the full TNS Connection string.

```
CREATE DATABASE LINK remote_db CONNECT TO username IDENTIFIED BY password USING 'remote';

CREATE DATABASE LINK remotenoTNS CONNECT TO username IDENTIFIED BY password
  USING '(DESCRIPTION=(ADDRESS_LIST=(ADDRESS = (PROTOCOL = TCP)(HOST =192.168.1.1)
  (PORT =1521)))(CONNECT_DATA =(SERVICE_NAME = orcl)))';
```

After the database link is created, you can use the database link directly as part of a SQL query using the database link name `@remote_db` as a suffix to the table name.

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

For more information, see [Managing Database Links](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-a-distributed-database.html#GUID-7B0C4627-4473-4313-88D5-FD03CA42D9EA "https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-a-distributed-database.html#GUID-7B0C4627-4473-4313-88D5-FD03CA42D9EA") in the _Oracle documentation_.

## MySQL usage

Currently, MySQL doesn’t provide a direct comparable alternative for Oracle Database Links. You can use the fully-qualified names to query data from another database within the same cluster. This functionality is similar to querying data from a different schema in Oracle. If the data cannot be stored under the same MySQL Cluster, then there is no equivalent to Oracle Database Links in MySQL.

If the data can’t be placed under the same MySQL Cluster then there is no relevant equivalent to Oracle Database Links in MySQL.

### Examples

Query all flight ids from the `all_flights` table in the flights database, assume that this code runs from another database.

```
SELECT flight_id from flights.all_flights;
```

This query returns the data only if the user has permissions to the table and the database.
