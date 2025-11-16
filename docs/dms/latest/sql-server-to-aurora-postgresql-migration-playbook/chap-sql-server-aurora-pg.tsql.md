# Triggers for T-SQL

This topic provides reference information about migrating triggers from Microsoft SQL Server 2019 to Amazon Aurora PostgreSQL. It compares the trigger functionality between the two database systems, highlighting similarities and differences in syntax, scope, and usage. You’ll gain insights into how triggers work in both environments, including their types, execution phases, and management capabilities.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                   | Key differences                                       |
| -------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Three star feature compatibility | Three star automation level        | [Triggers](chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.triggers "chap-sql-server-aurora-pg.tools.md#chap-sql-server-aurora-pg.tools.actioncode.triggers") | Syntax and option differences, similar functionality. |

## SQL Server Usage

Triggers are special types of stored procedures that run automatically in response to events. They are most commonly used for Data Manipulation Language (DML).

SQL Server supports `AFTER`, `FOR`, and `INSTEAD OF` triggers, which you can create on tables and views (`AFTER` and `FOR` are synonymous). SQL Server also provides an event trigger framework at the server and database levels that includes Data Definition Language (DDL), Data Control Language (DCL), and general system events such as login.

###### Note

SQL Server doesn’t support `FOR EACH ROW` triggers in which the trigger code is run once for each row of modified data.

### Trigger Run

`AFTER` triggers runs after DML statements complete run. `INSTEAD OF` triggers run code in place of the original DML statement. You can create `AFTER` triggers on tables only. You can create `INSTEAD OF` triggers on tables and views.

You can create only one `INSTEAD OF` trigger for any given object and event. When multiple `AFTER` triggers exist for the same event and object, you can partially set the trigger order by using the `sp_settriggerorder` system stored procedure. You can use it to set the first and last triggers to be run, but not the order of others.

### Trigger Scope

SQL Server supports statement level triggers only. The trigger code runs once for each statement. The data modified by the DML statement is available to the trigger scope and is saved in two virtual tables: `INSERTED` and `DELETED`. These tables contain the entire set of changes performed by the DML statement that caused trigger run.

SQL Server triggers always run within the transaction of the statement that triggered the run. If the trigger code issues an explicit `ROLLBACK`, or causes an exception that mandates a rollback, the DML statement is also rolled back. For `INSTEAD OF` triggers, the DML statement doesn’t run and doesn’t require a rollback.

### Examples

**Use a DML trigger to audit invoice deletions**

The following examples demonstrate how to use a trigger to log rows deleted from a table.

Create and populate the `Invoices` table.

```
CREATE TABLE Invoices
(
  InvoiceID INT NOT NULL PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  TotalAmount DECIMAL(9,2) NOT NULL
);

INSERT INTO Invoices (InvoiceID,Customer,TotalAmount)
VALUES
(1, 'John', 1400.23),
(2, 'Jeff', 245.00),
(3, 'James', 677.22);
```

Create the `InvoiceAuditLog` table.

```
CREATE TABLE InvoiceAuditLog
(
  InvoiceID INT NOT NULL PRIMARY KEY,
  Customer VARCHAR(20) NOT NULL,
  TotalAmount DECIMAL(9,2) NOT NULL,
  DeleteDate DATETIME NOT NULL DEFAULT (GETDATE()),
  DeletedBy VARCHAR(128) NOT NULL DEFAULT (CURRENT_USER)
);
```

Create an `AFTER DELETE` trigger to log deletions from the `Invoices` table to the audit log.

```
CREATE TRIGGER LogInvoiceDeletes
ON Invoices
AFTER DELETE
AS
BEGIN
INSERT INTO InvoiceAuditLog (InvoiceID, Customer, TotalAmount)
SELECT InvoiceID,
  Customer,
  TotalAmount
FROM Deleted
END;
```

Delete an invoice.

```
DELETE FROM Invoices
WHERE InvoiceID = 3;
```

Query the content of both tables.

```
SELECT *
FROM Invoices AS I
  FULL OUTER JOIN
  InvoiceAuditLog AS IAG
  ON I.InvoiceID = IAG.InvoiceID;
```

For the preceding example, the result looks as shown following.

```
InvoiceID  Customer  TotalAmount  InvoiceID  Customer  TotalAmount  DeleteDate      DeletedBy
1          John      1400.23      NULL       NULL      NULL         NULL            NULL
2          Jeff      245.00       NULL       NULL      NULL         NULL            NULL
NULL       NULL      NULL         3          James     677.22       20180224 13:02  Domain/JohnCortney
```

**Create a DDL trigger**

Create a trigger to protect all tables in the database from accidental deletion.

```
CREATE TRIGGER PreventTableDrop
ON DATABASE FOR DROP_TABLE
AS
BEGIN
  RAISERROR ('Tables can't be dropped in this database', 16, 1)
  ROLLBACK TRANSACTION
END;
```

Test the trigger by attempting to drop a table.

```
DROP TABLE [Invoices];
  GO
```

The system displays the following message explaining that the Invoices table can’t be dropped:

```
Msg 50000, Level 16, State 1, Procedure PreventTableDrop, Line 5 [Batch Start Line 56]
Tables Can't be dropped in this database.
Msg 3609, Level 16, State 2, Line 57
The transaction ended in the trigger. The batch has been aborted.
```

For more information, see [DML Triggers](https://docs.microsoft.com/en-us/sql/relational-databases/triggers/dml-triggers?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/triggers/dml-triggers?view=sql-server-ver15") and [DDL Triggers](https://docs.microsoft.com/en-us/sql/relational-databases/triggers/ddl-triggers?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/triggers/ddl-triggers?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Triggers provide much of the same functionality as SQL Server:

- DML triggers run based on table related events, such as DML.
- Event triggers run after certain database events, such as running DDL commands.

Unlike SQL Server triggers, PostgreSQL triggers must call a function. They don’t support anonymous blocks of PL/pgSQL code as part of the trigger body. The user-supplied function is declared with no arguments and has a return type of trigger.

### PostgreSQL DML Triggers

PostgreSQL triggers can be fired BEFORE or AFTER a DML operation.

- They run before the operation is attempted on a row.
  - Before constraints are checked and the INSERT, UPDATE, or DELETE is attempted.
  - If the trigger runs before or instead of the event, the trigger can skip the operation for the current row or change the row being inserted (for INSERT and UPDATE operations only).

- Triggers can run after the operation was completed, after constraints are checked, and the `INSERT`, `UPDATE`, or `DELETE` command completed. If the trigger runs after the event, all changes, including the effects of other triggers, are visible to the trigger.

PostgreSQL triggers can run `INSTEAD OF` a DML command when created on views.

PostgreSQL triggers can run `FOR EACH ROW` affected by the DML statement or `FOR EACH STATEMENT` running only once as part of a DML statement.

| When fired | Database event         | Row-Level trigger (FOR EACH ROW) | Statement-level trigger (FOR EACH STATEMENT) |
| ---------- | ---------------------- | -------------------------------- | -------------------------------------------- |
| BEFORE     | INSERT, UPDATE, DELETE | Tables and foreign tables        | Tables, views, and foreign tables            |
| BEFORE     | TRUNCATE               | —                                | Tables                                       |
| AFTER      | INSERT, UPDATE, DELETE | Tables and foreign tables        | Tables, views, and foreign tables            |
| AFTER      | TRUNCATE               | —                                | Tables                                       |
| INSTEAD OF | INSERT, UPDATE, DELETE | Views                            | —                                            |
| INSTEAD OF | TRUNCATE               | —                                | —                                            |

### PostgreSQL Event Triggers

An event trigger runs when a specific event associated with the trigger occurs in the database. Supported events include `ddl_command_start`, `ddl_command_end`, `table_rewrite`, and `sql_drop`.

- `ddl_command_start` occurs before the run of a `CREATE`, `ALTER`, `DROP`, `SECURITY LABEL`, `COMMENT`, `GRANT`, `REVOKE`, or `SELECT INTO` command.
- `ddl_command_end` occurs after the command completed and before the transaction commits.
- `sql_drop` runs only for the `DROP` DDL command, before the `ddl_command_end` trigger runs.

For a full list of supported PostgreSQL event trigger types, see [Event Trigger Firing Matrix](https://www.postgresql.org/docs/10/event-trigger-matrix.html "https://www.postgresql.org/docs/10/event-trigger-matrix.html") in the _PostgreSQL documentation_.

### PostgreSQL CREATE TRIGGER Synopsis

```
CREATE [ CONSTRAINT ] TRIGGER name { BEFORE | AFTER | INSTEAD OF } { event [ OR ... ]}
  ON table_name
  [ FROM referenced_table_name ]
  [ NOT DEFERRABLE | [ DEFERRABLE ] [ INITIALLY IMMEDIATE | INITIALLY DEFERRED ] ]
  [ REFERENCING { { OLD | NEW } TABLE [ AS ] transition_relation_name } [ ... ] ]
  [ FOR [ EACH ] { ROW | STATEMENT } ]
  [ WHEN ( condition ) ]
  EXECUTE PROCEDURE function_name ( arguments )

where event can be one of:

  INSERT
  UPDATE [ OF column_name [, ... ] ]
  DELETE
  TRUNCATE
```

###### Note

`REFERENCING` is a new option since PostgreSQL 10. You can use it with `AFTER` trigger to interact with the overall view of the `OLD` or the `NEW TABLE` changed rows.

### Examples

**Create a trigger**

Create a trigger function that stores the run logic (this is the same as a SQL Server DML trigger).

```
CREATE OR REPLACE FUNCTION PROJECTS_SET_NULL()
  RETURNS TRIGGER
  AS $$
  BEGIN
IF TG_OP = 'UPDATE' AND OLD.PROJECTNO != NEW.PROJECTNO OR
  TG_OP = 'DELETE' THEN
UPDATE EMP
  SET PROJECTNO = NULL
  WHERE EMP.PROJECTNO = OLD.PROJECTNO;
  END IF;
  IF TG_OP = 'UPDATE' THEN RETURN NULL;
    ELSIF TG_OP = 'DELETE' THEN RETURN NULL;
  END IF;
END; $$
LANGUAGE PLPGSQL;

CREATE FUNCTION
```

Create the trigger.

```
CREATE TRIGGER TRG_PROJECTS_SET_NULL
AFTER UPDATE OF PROJECTNO OR DELETE
ON PROJECTS
FOR EACH ROW
EXECUTE PROCEDURE PROJECTS_SET_NULL();

CREATE TRIGGER
```

Test the trigger by deleting a row from the `PROJECTS` table.

```
DELETE FROM PROJECTS WHERE PROJECTNO=123;
SELECT PROJECTNO FROM EMP WHERE PROJECTNO=123;

projectno
(0 rows)
```

**Create a trigger**

Create an event trigger function. This is the same as a SQL Server DDL System/Schema level trigger, such as a trigger that prevents running a DDL DROP on objects in the HR schema.

Note that trigger functions are created with no arguments and must have a return type of `TRIGGER` or `EVENT_TRIGGER`.

```
CREATE OR REPLACE FUNCTION ABORT_DROP_COMMAND()
  RETURNS EVENT_TRIGGER
  AS $$
BEGIN
  RAISE EXCEPTION 'The % Command is Disabled', tg_tag;
END; $$
LANGUAGE PLPGSQL;

CREATE FUNCTION
```

Create the event trigger, which runs before the start of a DDL `DROP` command.

```
CREATE EVENT TRIGGER trg_abort_drop_command
  ON DDL_COMMAND_START
  WHEN TAG IN ('DROP TABLE', 'DROP VIEW', 'DROP FUNCTION', 'DROP
    SEQUENCE', 'DROP MATERIALIZED VIEW', 'DROP TYPE')
  EXECUTE PROCEDURE abort_drop_command();
```

Test the trigger by attempting to drop the `EMPLOYEES` table.

```
DROP TABLE EMPLOYEES;

ERROR: The DROP TABLE Command is Disabled
CONTEXT: PL/pgSQL function abort_drop_command() line 3 at RAISE
```

## Summary

| Feature                     | SQL Server                                                                                 | Aurora PostgreSQL                                                        |
| --------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| DML Triggers Scope          | Statement level only                                                                       | `FOR EACH ROW` and `FOR EACH STATMENT`                                   |
| Access to change set        | `INSERTED` and `DELETED` virtual multi-row tables                                          | `OLD` and `NEW` virtual one-row tables or the whole view of changed rows |
| System event triggers       | DDL, DCL, and other event types                                                            | Event triggers                                                           |
| Trigger run phase           | `AFTER` and `INSTEAD OF`                                                                   | `AFTER`, `BEFORE`, and `INSTEAD OF`                                      |
| Multi-trigger run order     | Can only set first and last using `sp_settriggerorder`                                     | Call function within a function                                          |
| Drop a trigger              | `DROP TRIGGER <trigger name>;`                                                             | `DROP TRIGGER <trigger name>;`                                           |
| Modify trigger code         | Use the `ALTER TRIGGER` statement                                                          | Modify function code                                                     |
| Enable or disable a trigger | Use the `ALTER TRIGGER <trigger name> ENABLE;` and `ALTER TRIGGER <trigger name> DISABLE;` | `ALTER TABLE`                                                            |
| Triggers on views           | `INSTEAD OF` triggers only                                                                 | `INSTEAD OF` triggers only                                               |

For more information, see [Trigger Functions](https://www.postgresql.org/docs/13/plpgsql-trigger.html "https://www.postgresql.org/docs/13/plpgsql-trigger.html") in the _PostgreSQL documentation_.
