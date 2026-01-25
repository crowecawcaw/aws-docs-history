# Oracle read-only tables and partitions and PostgreSQL Aurora replicas

With AWS DMS, you can migrate data from Oracle databases to Amazon Aurora PostgreSQL-Compatible Edition with minimal downtime by leveraging Oracle read-only tables and partitions for ongoing replication, and PostgreSQL Aurora replicas for read scaling. Oracle read-only tables and partitions facilitate ongoing replication from an Oracle source database, while PostgreSQL Aurora replicas provide read scaling for the migrated Aurora PostgreSQL database.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences |
| -------------------------------- | ---------------------------------- | ------------------------- | --------------- |
| Three star feature compatibility | No automation                      | N/A                       | N/A             |

## Oracle usage

Beginning with Oracle 11g, tables can be marked as read-only to prevent DML operations from altering table data.

Prior to Oracle 11g, the only way to set a table to read-only mode was by limiting table privileges to `SELECT`. The table owner was still able to perform read and write operations. Begining with Oracle 11g, users can run an `ALTER TABLE` statement and change the table mode to either `READ ONLY` or `READ WRITE`.

Oracle 12c Release 2 introduces greater granularity for read-only objects and supports read-only table partitions. Any attempt to perform a DML operation on a partition, or sub-partition, set to `READ ONLY` results in an error.

`SELECT FOR UPDATE` statements aren’t allowed.

DDL operations are permitted if they don’t modify table data.

Operations on indexes are allowed on tables set to `READ ONLY` mode.

**Examples**

```
CREATE TABLE EMP_READ_ONLY (
EMP_ID NUMBER PRIMARY KEY,
EMP_FULL_NAME VARCHAR2(60) NOT NULL);

INSERT INTO EMP_READ_ONLY VALUES(1, 'John Smith');

1 row created

ALTER TABLE EMP_READ_ONLY READ ONLY;

INSERT INTO EMP_READ_ONLY VALUES(2, 'Steven King');

ORA-12081: update operation not allowed on table "SCT"."TBL_READ_ONLY"

ALTER TABLE EMP_READ_ONLY READ WRITE;

INSERT INTO EMP_READ_ONLY VALUES(2, 'Steven King');

1 row created

COMMIT;

SELECT * FROM EMP_READ_ONLY;

EMP_ID  EMP_FULL_NAME
1       John Smith
2       Steven King
```

For more information, see [ALTER TABLE](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-TABLE.html "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ALTER-TABLE.html") and [Changes in This Release for Oracle Database VLDB and Partitioning Guide](https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/release-changes.html#GUID-C7A9BAD4-E4C9-4765-88C5-51AC7E97BAF1 "https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/release-changes.html#GUID-C7A9BAD4-E4C9-4765-88C5-51AC7E97BAF1") in the _Oracle documentation_.

## PostgreSQL usage

PostgreSQL doesn’t provide an equivalent to the `READ ONLY` mode supported in Oracle.

You can use the following alternatives as a workaround:

- Read-only user or role.
- Read-only database.
- Creating a read-only database trigger or a using a read-only constraint.

**PostgreSQL read-only user or role example**

To achieve some degree of protection from unwanted DML operations on table for a specific database user, you can grant the user only the `SELECT` privilege on the table and set the user `default_transaction_read_only` parameter to `ON`.

Create a PostgreSQL user with `READ ONLY` privileges.

```
CREATE TABLE EMP_READ_ONLY (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL);

CREATE USER aws_readonly PASSWORD 'aws_readonly';
CREATE ROLE

ALTER USER aws_readonly SET DEFAULT_TRANSACTION_READ_ONLY=ON;
ALTER ROLE

GRANT SELECT ON EMP_READ_ONLY TO aws_readonly;
GRANT

-- Open a new session with user “aws_readonly”
SELECT * FROM EMP_READ_ONLY;

emp_id  emp_full_name
(0 rows)

INSERT INTO EMP_READ_ONLY VALUES(1, 'John Smith');
ERROR: can't execute INSERT in a read-only transaction
```

**PostgreSQL read-only database example**

As an alternative solution for restricting write operations on database objects, a dedicated read-only PostgreSQL database can be created to store all read-only tables. PostgreSQL supports multiple databases under the same database instance. Adding a dedicated “read-only” database is a simple and straightforward solution.

- Set the `DEFAULT_TRANSACTION_READ_ONLY` to `ON` for a database. If a session attempts to perform DDL or DML operations, and error will be raised.
- The database can be altered back to `READ WRITE` mode when the parameter is set to `OFF`.

Create a PostgreSQL READ ONLY database.

```
CREATE DATABASE readonly_db;

ALTER DATABASE readonly_db SET DEFAULT_TRANSACTION_READ_ONLY=ON;

-- Open a new session connected to the “readonly_db” database

CREATE TABLE EMP_READ_ONLY (
  EMP_ID NUMERIC PRIMARY KEY,
  EMP_FULL_NAME VARCHAR(60) NOT NULL);
ERROR: can't execute CREATE TABLE in a read-only transaction

-- In case of an existing table

INSERT INTO EMP_READ_ONLY VALUES(1, 'John Smith');
ERROR: can't execute INSERT in a read-only transaction
```

**PostgreSQL read-only database trigger example**

You can create an `INSTEAD OF` trigger to prevent data modifications on a specific table, such as restricting `INSERT`, `UPDATE`, `DELETE` and `TRUNCATE`.

Create PostgreSQL function which contains the logic for restricting to read-only operations:

```
CREATE OR REPLACE FUNCTION READONLY_TRIGGER_FUNCTION()
  RETURNS
  TRIGGER AS $$
  BEGIN
RAISE EXCEPTION 'THE "%" TABLE IS READ ONLY!', TG_TABLE_NAME
  using hint = 'Operation Ignored';
    RETURN NULL;
  END;
$$ language 'plpgsql';
```

Create a trigger which will run the function that was previously created.

```
CREATE TRIGGER EMP_READONLY_TRIGGER
  BEFORE INSERT OR UPDATE OR DELETE OR TRUNCATE
  ON EMP_READ_ONLY FOR EACH STATEMENT
  EXECUTE PROCEDURE READONLY_TRIGGER_FUNCTION();
```

Test DML and truncate commands against the table with the new trigger.

```
INSERT INTO EMP_READ_ONLY VALUES(1, 'John Smith');
  ERROR: THE "EMP_READ_ONLY" TABLE IS READ ONLY!
  HINT: Operation Ignored
  CONTEXT: PL/pgSQL function readonly_trigger_function() line 3 at
  RAISE

demo>= TRUNCATE TABLE SRC;
  ERROR: THE " EMP_READ_ONLY" TABLE IS READ ONLY!
  HINT: Operation Ignored
  CONTEXT: PL/pgSQL function readonly_trigger_function() line 3 at
  RAISE
```

For more information, see [Privileges](https://www.postgresql.org/docs/13/ddl-priv.html "https://www.postgresql.org/docs/13/ddl-priv.html"), [GRANT](https://www.postgresql.org/docs/13/sql-grant.html "https://www.postgresql.org/docs/13/sql-grant.html"), and [Client Connection Defaults](https://www.postgresql.org/docs/13/runtime-config-client.html "https://www.postgresql.org/docs/13/runtime-config-client.html") in the _PostgreSQL documentation_.
