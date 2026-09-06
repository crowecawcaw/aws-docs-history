

# Triggers for T-SQL
<a name="chap-sql-server-aurora-mysql.tsql.triggers"></a>

This topic provides reference information about migrating triggers from Microsoft SQL Server 2019 to Amazon Aurora MySQL. It compares the trigger functionality between the two database systems, highlighting key differences and similarities. You can understand how triggers work in both environments, including their scope, access to change sets, supported event types, and execution phases.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Two star feature compatibility](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-compatibility-2.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/sql-server-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  |  [Triggers](chap-sql-server-aurora-mysql.tools.actioncode.md#chap-sql-server-aurora-mysql.tools.actioncode.triggers)  | Only `FOR EACH ROW` processing. No DDL or `EVENT` triggers. `BEFORE` triggers replace `INSTEAD OF` triggers. | 

## SQL Server Usage
<a name="chap-sql-server-aurora-mysql.tsql.triggers.sqlserver"></a>

Triggers are special type of stored procedure that run automatically in response to events and are most commonly used for Data Manipulation Language (DML).

SQL Server supports `AFTER/FOR` and `INSTEAD OF` triggers, which can be created on tables and views. `AFTER` and `FOR` are synonymous. SQL Server also provides an event trigger framework at the server and database levels that includes Data Definition Language (DDL), Data Control Language (DCL), and general system events such as login.

**Note**  
SQL Server doesn’t support `FOR EACH ROW` triggers in which the trigger code is run once for each row of modified data.

### Trigger Run
<a name="chap-sql-server-aurora-mysql.tsql.triggers.sqlserver.run"></a>
+  `AFTER` triggers run after DML statements complete run.
+  `INSTEAD OF` triggers run code in place of the original DML statement.

You can create `AFTER` triggers only on a table. You can create `INSTEAD OF` triggers on tables and views.

You can create only a single `INSTEAD OF` trigger for any given object and event. When multiple `AFTER` triggers exist for the same event and object, you can partially set the trigger order by using the `sp_settriggerorder` system stored procedure. It enables setting the first and last triggers to be run, but not the order of others.

### Trigger Scope
<a name="chap-sql-server-aurora-mysql.tsql.triggers.sqlserver.scope"></a>

SQL Server supports only statement level triggers. The trigger code runs only once for each statement. The data modified by the DML statement is available to the trigger scope and is saved in two virtual tables: `INSERTED` and `DELETED`. These tables contain the entire set of changes performed by the DML statement that caused trigger run.

SQL triggers always run within the transaction of the statement that triggered the run. If the trigger code issues an explicit ROLLBACK, or causes an exception that mandates a rollback, the DML statement is also rolled back. For `INSTEAD OF` triggers, the DML statement isn’t run and, therefore, doesn’t require a rollback.

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.triggers.sqlserver.examples"></a>

 **Use a DML trigger to audit invoice deletions** 

The following example demonstrates how to use a trigger to log rows deleted from a table.

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
InvoiceID  Customer TotalAmount  InvoiceID  Customer  TotalAmount  DeleteDate      DeletedBy
1          John     1400.23      NULL       NULL      NULL         NULL            NULL
2          Jeff     245.00       NULL       NULL      NULL         NULL            NULL
NULL       NULL     NULL         3          James     677.22       20180224 13:02  Domain/JohnCortney
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

The system displays the follow message indicating the `Invoices` table can’t be dropped.

```
Msg 50000, Level 16, State 1, Procedure PreventTableDrop, Line 5 [Batch Start Line 56]
Tables Can't be dropped in this database
Msg 3609, Level 16, State 2, Line 57
The transaction ended in the trigger. The batch has been aborted.
```

For more information, see [DML Triggers](https://docs.microsoft.com/en-us/sql/relational-databases/triggers/dml-triggers?view=sql-server-ver15) and [DDL Triggers](https://docs.microsoft.com/en-us/sql/relational-databases/triggers/ddl-triggers?view=sql-server-ver15) in the *SQL Server documentation*.

## MySQL Usage
<a name="chap-sql-server-aurora-mysql.tsql.triggers.mysql"></a>

 Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) provides Data manipulation Language (DML) triggers only.

MySQL supports `BEFORE` and `AFTER` triggers for `INSERT`, `UPDATE`, and `DELETE` with full control over trigger run order.

MySQL triggers differ substantially from SQL Server. However, you can migrate most common use cases with minimal code changes. The following list identifies the major differences between the SQL Server and Aurora MySQL triggers:
+  Aurora MySQL triggers are run once for each row, not once for each statement as with SQL Server.
+  Aurora MySQL doesn’t support DDL or system event triggers.
+  Aurora MySQL supports `BEFORE` triggers; SQL Server doesn’t support `BEFORE` triggers. l Aurora MySQL supports full run order control for multiple triggers.

**Note**  
Stored procedures, triggers, and user-defined functions in Aurora MySQL are collectively referred to as stored routines. When binary logging is turned on, MySQL `SUPER` privilege is required to run stored routines. However, you can run stored routines with binary logging enabled without `SUPER` privilege by setting `thelog_bin_trust_function_creators` parameter to true for the DB parameter group for your MySQL instance.

### Syntax
<a name="chap-sql-server-aurora-mysql.tsql.triggers.mysql.syntax"></a>

```
CREATE [DEFINER = { user | CURRENT_USER }] TRIGGER <Trigger Name>
{ BEFORE | AFTER } { INSERT | UPDATE | DELETE }
ON <Table Name>
FOR EACH ROW
[{ FOLLOWS | PRECEDES } <Other Trigger Name>]
<Trigger Code Body>
```

### Examples
<a name="chap-sql-server-aurora-mysql.tsql.triggers.mysql.examples"></a>

 **Use a DML trigger to audit invoice deletions** 

The following example demonstrates how to use a trigger to log rows deleted from a table.

Create and populate the `Invoices` table.

```
CREATE TABLE Invoices
(
    InvoiceID INT NOT NULL PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    TotalAmount DECIMAL(9,2) NOT NULL
);

INSERT INTO Invoices (InvoiceID, Customer, TotalAmount)
VALUES
(1, 'John', 1400.23),
(2, 'Jeff', 245.00),
(3, 'James', 677.22);
```

Create the `InvoiceAuditLog` table.

```
CREATE TABLE InvoiceAuditLog
(
    InvoiceID INT NOT NULL
        PRIMARY KEY,
    Customer VARCHAR(20) NOT NULL,
    TotalAmount DECIMAL(9,2) NOT NULL,
    DeleteDate DATETIME NOT NULL
        DEFAULT (GETDATE()),
    DeletedBy VARCHAR(128) NOT NULL
        DEFAULT (CURRENT_USER)
);
```

Create a trigger to log deleted rows.

```
CREATE OR REPLACE TRIGGER LogInvoiceDeletes
ON Invoices
FOR EACH ROW
AFTER DELETE
AS
    BEGIN
    INSERT INTO InvoiceAuditLog (InvoiceID, Customer, TotalAmount, DeleteDate, DeletedBy)
    SELECT InvoiceID,
        Customer,
        TotalAmount,
        NOW(),
        CURRENT_USER()
    FROM OLD
END;
```

Test the trigger by deleting an invoice.

```
DELETE FROM Invoices
WHERE InvoiceID = 3;
```

Select all rows from the `InvoiceAuditLog` table.

```
SELECT * FROM InvoiceAuditLog;
```

For the preceding example, the result looks as shown following.

```
InvoiceID  Customer  TotalAmount  DeleteDate      DeletedBy
3          James     677.22       20180224 13:02  George
```

**Note**  
Additional code changes were required for this example because the `GETDATE()` function isn’t supported by MySQL. For more information, see [Date and Time Functions](chap-sql-server-aurora-mysql.tsql.datetime.md).

## Summary
<a name="chap-sql-server-aurora-mysql.tsql.triggers.summary"></a>


| Feature | SQL Server |  Aurora MySQL  | Workaround | 
| --- | --- | --- | --- | 
| DML triggers scope | Statement-level only |  `FOR EACH ROW` only | Most trigger code, such as the SQL Server example in the previous section, will work without significant code changes. Even though SQL Server triggers process a set of rows at once, typically no changes are needed to process one row at a time. A set of one row, is a valid set and should be processed correctly either way.<br />The main drawback of `FOR EACH ROW` triggers, is that you can’t access other rows that were modified in the same operation. The `NEW` and `OLD` virtual tables can only reference the current row. Therefore, for example, tasks such as logging aggregate data for the entire DML statement set, may require more significant code changes.<br />If your SQL Server trigger code uses loops and cursors to process one row at a time, the loop and cursor sections can be safely removed. | 
| Access to change set |  `INSERTED` and `DELETED` virtual multi-row tables |  `OLD` and `NEW` virtual one-row tables | Make sure that you modify the trigger code to use `NEW` instead of `INSERTED`, and `OLD` instead of `DELETED`. | 
| System event triggers | DDL, DCL and other event types | Not supported |  | 
| Trigger run phase |  `AFTER` and `INSTEAD OF`  |  `AFTER` and `BEFORE`  | For `INSTEAD OF` triggers, make sure that your modify the trigger code to remove the explicit run of the calling DML, which isn’t needed in a `BEFORE` trigger.<br />In Aurora MySQL, the `OLD` and `NEW` tables are updateable. If your trigger code needs to modify the change set, update the `OLD` and `NEW` tables with the changes. The updated data is applied to the table data when the trigger run completes. | 
| Multi-trigger run order | Can only set first and last using `sp_settriggerorder`. | Can set any run order using `PRECEDS` and `FOLLOWS`. | Update the trigger code to reflect the desired run order. | 
| Drop a trigger |  `DROP TRIGGER <trigger name>;`  |  `DROP TRIGGER <trigger name>;`  | Compatible syntax. | 
| Modify trigger code | Use the `ALTER TRIGGER` statement. | Not supported |  | 
| Turn on and turn off a trigger | Use the `ALTER TRIGGER <trigger name> ENABLE;` and `ALTER TRIGGER <trigger name> DISABLE;`  | Not supported | A common workaround is to use a database table with flags indicating which trigger to run.<br />Modify the trigger code using conditional flow control (IF) to query the table and determine whether or not the trigger should run additional code or exit without performing any modifications to the database. | 
| Triggers on views |  `INSTEAD OF` triggers only | Not supported |  | 

For more information, see [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/5.7/en/trigger-syntax.html) and [CREATE TRIGGER Statement](https://dev.mysql.com/doc/refman/5.7/en/create-trigger.html) in the *MySQL documentation*.