# Error handling for T-SQL

This topic provides reference content comparing error handling approaches between Microsoft SQL Server 2019 and Amazon Aurora MySQL. You can gain insights into the differences in error handling paradigms, syntax, and capabilities between these two database systems.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index                                                                                                                                                                                               | Key differences                                                        |
| ------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Four star feature compatibility | Four star automation level         | [Error Handling](chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.errorhandling "chap-sql-server-aurora-mysql.tools.md#chap-sql-server-aurora-mysql.tools.actioncode.errorhandling") | Different paradigm and syntax requires rewrite of error handling code. |

## SQL Server Usage

SQL Server error handling capabilities have significantly improved throughout the years. However, previous features are retained for backward compatibility.

Before SQL Server 2008, only very basic error handling features were available. `RAISERROR` was the primary statement used for error handling.

Starting from SQL Server 2008, SQL Server has added extensive .NET-like error handling capabilities including `TRY/CATCH` blocks, `THROW` statements, the `FORMATMESSAGE` function, and a set of system functions that return metadata for the current error condition.

### TRY/CATCH Blocks

`TRY/CATCH` blocks implement error handling similar to Microsoft Visual C# and Microsoft Visual C++. `TRY …​ END TRY` statement blocks can contain T-SQL statements.

If an error is raised by any of the statements within the `TRY …​ END TRY` block, the run stops and is moved to the nearest set of statements that are bounded by a `CATCH …​ END CATCH` block.

**Syntax**

```
BEGIN TRY
<Set of SQL Statements>
END TRY
BEGIN CATCH
<Set of SQL Error Handling Statements>
END CATCH
```

### THROW

The `THROW` statement raises an exception and transfers run of the `TRY …​ END TRY` block of statements to the associated `CATCH …​ END CATCH` block of statements.

Throw accepts either constant literals or variables for all parameters.

**Syntax**

```
THROW [Error Number>, <Error Message>, < Error State>] [;]
```

**Examples**

Use `TRY/CATCH` error blocks to handle key violations.

```
CREATE TABLE ErrorTest (Col1 INT NOT NULL PRIMARY KEY);
```

```
BEGIN TRY
    BEGIN TRANSACTION
        INSERT INTO ErrorTest(Col1) VALUES(1);
        INSERT INTO ErrorTest(Col1) VALUES(2);
        INSERT INTO ErrorTest(Col1) VALUES(1);
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    THROW; -- Throw with no parameters = RETHROW
END CATCH;
```

```
(1 row affected)
(1 row affected)
(0 rows affected)
Msg 2627, Level 14, State 1, Line 7
Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE54D8676973'.
Cannot insert duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
```

###### Note

Contrary to what many SQL developers believe, the values 1 and 2 are indeed inserted into `ErrorTestTable` in the preceding example. This behavior is in accordance with ANSI specifications stating that a constraint violation shouldn’t roll back an entire transaction.

Use `THROW` with variables.

```
BEGIN TRY
BEGIN TRANSACTION
INSERT INTO ErrorTest(Col1) VALUES(1);
INSERT INTO ErrorTest(Col1) VALUES(2);
INSERT INTO ErrorTest(Col1) VALUES(1);
COMMIT TRANSACTION;
END TRY
BEGIN CATCH
DECLARE @CustomMessage VARCHAR(1000),
    @CustomError INT,
    @CustomState INT;
SET @CustomMessage = 'My Custom Text ' + ERROR_MESSAGE();
SET @CustomError = 54321;
SET @CustomState = 1;
THROW @CustomError, @CustomMessage, @CustomState;
END CATCH;
```

```
(0 rows affected)
Msg 54321, Level 16, State 1, Line 19
My Custom Text Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE545CBDBB9A'.
Cannot insert duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
```

### RAISERROR

The `RAISERROR` statement is used to explicitly raise an error message, similar to `THROW`. It causes an error state for the running session and forwards run to either the calling scope or, if the error occurred within a `TRY …​ END TRY` block, to the associated `CATCH …​ END CATCH` block. `RAISERROR` can reference a user-defined message stored in the `sys.messages` system table or can be used with dynamic message text.

The key differences between `THROW` and `RAISERROR` are:

- Message IDs passed to `RAISERROR` must exist in the `sys.messages` system table. The error number parameter passed to `THROW` doesn’t.
- `RAISERROR` message text may contain printf formatting styles. The message text of `THROW` may not.
- `RAISERROR` uses the severity parameter for the error returned. For `THROW`, severity is always 16.

**Syntax**

```
RAISERROR (<Message ID>|<Message Text> ,<Message Severity> ,<Message State>
[WITH option [<Option List>]])
```

**Example**

Raise a custom error.

```
RAISERROR (N'This is a custom error message with severity 10 and state 1.', 10, 1)
```

### FORMATMESSAGE

`FORMATMESSAGE` returns a sting message consisting of an existing error message in the `sys.messages` system table, or from a text string, using the optional parameter list replacements. The `FORMATMESSAGE` statement is similar to the `RAISERROR` statement.

**Syntax**

```
FORMATMESSAGE (<Message Number> | <Message String>, <Parameter List>)
```

### Error State Functions

SQL Server provides the following error state functions:

- ERROR_LINE
- ERROR_MESSAGE
- ERROR_NUMBER
- ERROR_PROCEDURE
- ERROR_SEVERITY
- ERROR_STATE
- @@ERROR

**Examples**

Use error state functions within a `CATCH` block.

```
CREATE TABLE ErrorTest (Col1 INT NOT NULL PRIMARY KEY);
```

```
BEGIN TRY;
    BEGIN TRANSACTION;
        INSERT INTO ErrorTest(Col1) VALUES(1);
        INSERT INTO ErrorTest(Col1) VALUES(2);
        INSERT INTO ErrorTest(Col1) VALUES(1);
    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    SELECT ERROR_LINE(),
        ERROR_MESSAGE(),
        ERROR_NUMBER(),
        ERROR_PROCEDURE(),
        ERROR_SEVERITY(),
        ERROR_STATE(),
        @@Error;
THROW;
END CATCH;
```

```
6
Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE543C8912D8'.
Cannot insert duplicate key in object 'dbo.ErrorTest'.
The duplicate key value is (1).
2627
NULL
14
1
2627
```

```
(1 row affected)
(1 row affected)
(0 rows affected)
(1 row affected)
Msg 2627, Level 14, State 1, Line 25
Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE543C8912D8'.
Cannot insert duplicate key in object 'dbo.ErrorTest'.
The duplicate key value is (1).
```

For more information, see [RAISERROR (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-ver15"), [TRY…​CATCH (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver15"), and [THROW (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/throw-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/throw-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## MySQL Usage

Amazon Aurora MySQL-Compatible Edition (Aurora MySQL) offers a rich error handling framework with a different paradigm than SQL Server. The Aurora MySQL terminology is:

- `CONDITION` — The equivalent of an `ERROR` in SQL Server.
- `HANDLER` — An object that can handle conditions and perform actions.
- `DIAGNOSTICS` — The metadata about the `CONDITION`.
- `SIGNAL` and `RESIGNAL` — Statements similar to `THROW` and `RAISERROR` in SQL Server.

Errors in Aurora MySQL are identified by the follow items:

- A numeric error code specific to MySQL and, therefore, is not compatible with other database systems.
- A five character `SQLSTATE` value that uses the ANSI SQL and ODBC standard error conditions.

###### Note

Not every MySQL error number has a corresponding `SQLSTATE` value. For errors that don’t have a corresponding `SQLSTATE`, the general `HY000` error is used.

- A textual message string that describes the nature of the error.

### DECLARE …​ CONDITION

The `DECLARE …​ CONDITION` statement declares a named error condition and associates the name with a condition that requires handling. You can reference this declared name in subsequent `DECLARE …​ HANDLER` statements.

**Syntax**

```
DECLARE <Condition Name> CONDITION
FOR <Condition Value>
```

```
<Condition Value> = <MySQL Error Code> | <SQLSTATE [VALUE] <SQLState Value>
```

**Examples**

Declare a condition for MySQL error 1051 (Unknown table error).

```
DECLARE TableDoesNotExist CONDITION FOR 1051;
```

Declare a condition for SQL State 42S02 (Base table or view not found) .

###### Note

This SQLState error corresponds to the MySQL Error 1051.

```
DECLARE TableDoesNotExist CONDITION FOR SQLSTATE VALUE '42S02';
```

### DECLARE …​ HANDLER

A `HANDLER` object defines the actions or statements to be ran when a `CONDITION` arises. The handler object may be used to `CONTINUE` or `EXIT` the run.

The condition may be a previously defined condition using the `DECLARE …​ CONDITION` statement or an explicit condition for one of the following items:

- An explicit Aurora MySQL error code. For example 1051, which represents an **Unknown Table Error**.
- An explicit `SQLSTATE` value. For example `42S02`.
- Any `SQLWARNING` event representing any `SQLSTATE` with a `01` prefix.
- Any `NOTFOUND` event representing any `SQLSTATE` with a `02` prefix. This condition is relevant for cursors. For more information, see [Cursors](chap-sql-server-aurora-mysql.tsql.md "chap-sql-server-aurora-mysql.tsql.md").
- Any `SQLEXCEPTION` event, representing any `SQLSTATE` without a `00`, `01`, or `02` prefix. These conditions are considered exception errors.

###### Note

`SQLSTATE` events with a `00` prefix aren’t errors; they are used to represent successful runs of statements.

**Syntax**

```
DECLARE {CONTINUE | EXIT | UNDO}
HANDLER FOR
<MySQL Error Code> |
<SQLSTATE [VALUE] <SQLState Value> |
<Condition Name> |
SQLWARNING |
NOT FOUND |
SQLEXCEPTION
<Statement Block>
```

**Examples**

Declare a handler to ignore warning messages and continue run by assigning an empty statement block.

```
DECLARE CONTINUE HANDLER
FOR SQLWARNING BEGIN END
```

Declare a handler to `EXIT` upon duplicate key violation and log a message to a table.

```
DECLARE EXIT HANDLER
FOR SQLSTATE '23000'
BEGIN
    INSERT INTO MyErrorLogTable
        VALUES(NOW(), CURRENT_USER(), 'Error 23000')
END
```

### GET DIAGNOSTICS

Each run of an SQL statement produces diagnostic information that is stored in the diagnostics area. The `GET DIAGNOSTICS` statement enables users to retrieve and inspect this information.

###### Note

Aurora MySQL also supports the SHOW WARNINGS and SHOW ERRORS statements to retrieve conditions and errors.

The `GET DIAGNOSTICS` statement is typically used in the handler code within a stored routine. `GET CURRENT DIAGNOSTICS` is permitted outside the context of a handler to check the run result of an SQL statement.

The `CURRENT` keyword causes retrieval of the current diagnostics area. The `STACKED` keyword causes retrieval of the information from the second diagnostics area. The second diagnostic area is only available if the current context is within a code block of a condition handler. The default is `CURRENT`.

**Syntax**

```
GET [CURRENT | STACKED] DIAGNOSTICS
<@Parameter = NUMBER | ROW_COUNT>
|
CONDITION <Condition Number> <@Parameter = CLASS_ORIGIN | SUBCLASS_ORIGIN | RETURNED_
SQLSTATE | MESSAGE_TEXT | MYSQL_ERRNO | CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA |
CONSTRAINT_NAME | CATALOG_NAME | SCHEMA_NAME | TABLE_NAME | COLUMN_NAME | CURSOR_NAME>
```

**Example**

Retrieve `SQLSTATE` and `MESSAGE_TEXT` from the diagnostic area for the last statement that you ran.

```
GET DIAGNOSTICS CONDITION 1 @p1 = RETURNED_SQLSTATE, @p2 = MESSAGE_TEXT
```

### SIGNAL/RESIGNAL

The `SIGNAL` statement is used to raise an explicit condition or error. It can be used to provide full error information to a handle, to an outer scope of run, or to the SQL client. The SIGNAL statement enables explicitly defining the error’s properties such as error number, `SQLSTATE` value, message, and so on.

The difference between `SIGNAL` and `RESIGNAL` is that `RESIGNAL` is used to pass on the error condition information available during the run of a condition handler within a compound statement inside a stored routine or an event. `RESIGNAL` can be used to change none, some, or all the related condition information before passing it for processing in the next calling scope of the stack.

###### Note

It is not possible to issue `SIGNAL` statements using variables.

**Syntax**

```
SIGNAL | RESIGNAL <SQLSTATE [VALUE] sqlstate_value | <Condition Name>
[SET <Condition Information Item Name> = <Value> [,...n]]
<Condition Information Item Name> = CLASS_ORIGIN | SUBCLASS_ORIGIN | RETURNED_SQLSTATE
| MESSAGE_TEXT | MYSQL_ERRNO | CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA | CONSTRAINT_
NAME | CATALOG_NAME | SCHEMA_NAME | TABLE_NAME | COLUMN_NAME | CURSOR_NAME
```

**Examples**

Raise an explicit error with `SQLSTATE` 55555.

```
SIGNAL SQLSTATE '55555'
```

Re-raise an error with an explicit MySQL error number.

```
RESIGNAL SET MYSQL_ERRNO = 5
```

### Migration Considerations

###### Note

Error handling is a critical aspect of any software solution. Code migrated from one paradigm to another should be carefully evaluated and tested.

The basic operations of raising, processing, responding, and obtaining metadata is similar in nature for most relational database management systems. The technical aspects of rewriting the code to use different types of objects isn’t difficult.

In SQL Server, there can only be one handler, or `CATCH` code block, that handles exceptions for a given statement. In Aurora MySQL, multiple handler objects can be declared. A condition may trigger more than one handler. Be sure the correct handlers are ran as expected, especially when there are multiple handlers. The following sections provides rules to help establish your requirements.

### Handler Scope

A handler can be specific or general. Specific handlers are handlers defined for a specific MySQL error code, `SQLSTATE`, or a condition name. Therefore, only one type of event will trigger a specific handler. General handlers are handlers defined for conditions in the `SQLWARNING`, `SQLEXCEPTION`, or `NOT FOUND` classes. More than one event may trigger the handler.

A handler is in scope for the block in which it is declared. It can’t be triggered by conditions occurring outside the block boundaries.

A handler declared in a `BEGIN …​ END` block is in scope for the SQL statements that follow the handler declaration.

One or more handlers may be declared in different or the same scopes using different specifications. For example, a specific MySQL error code handler may be defined in an outer code block while a more general `SQLWARNING` handler is defined within an inner code block. Specific MySQL error code handlers and a general `SQLWARNING` class handler may exist within the same code block.

### Handler Choice

Only one handler is triggered for a single event. Aurora MySQL decides which handler should be triggered. The decision regarding which handler should be triggered as a response to a condition depends on the handler’s scope and value. It also depends on whether or not other handlers are present that may be more appropriate to handle the event.

When a condition occurs in a stored routine, the server searches for valid handlers in the current `BEGIN …​ END` block scope. If none are found, the engine searches for handlers in each successive containing `BEGIN …​ END` code block scope. When the server finds one or more applicable handlers at any given scope, the choice of which one to trigger is based on the following condition precedence:

- A MySQL error code handler takes precedence over a `SQLSTATE` value handler.
- An `SQLSTATE` value handler takes precedence over general `SQLWARNING`, `SQLEXCEPTION`, or `NOT FOUND` handlers.
- An `SQLEXCEPTION` handler takes precedence over an `SQLWARNING` handler.

Multiple applicable handlers with the same precedence may exist for a condition. For example, a statement could generate several warnings having different error codes. There may exist a specific MySQL error handler for each. In such cases, the choice is non-deterministic. Different handlers may be triggered at different times depending on the circumstances.

## Summary

The following table identifies similarities, differences, and key migration considerations.

| SQL Server error handling feature                                                                    | Migrate to Aurora MySQL                                                           | Comments                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `TRY …​ END TRY` and `CATCH …​ END CATCH` blocks.                                                    | Nested `BEGIN …​ END` code blocks with per-scope handlers.                        | `DECLARE` specific event handlers for each `BEGIN-END` code block. Note that unlike `CATCH` blocks, the handlers must be defined first, not later. Review the handler scope and handler choice sections. |
| `THROW` and `RAISERROR`                                                                              | `SIGNAL` and `RESIGNAL`                                                           | Review the handler scope and handler choice sections.                                                                                                                                                    |
| `THROW` with variables.                                                                              | Not supported.                                                                    |                                                                                                                                                                                                          |
| FORMATMESSAGE                                                                                        | N/A                                                                               |                                                                                                                                                                                                          |
| Error state functions.                                                                               | GET DIAGNOSTIC                                                                    |                                                                                                                                                                                                          |
| Proprietary error messages in `sys.messages` system table.                                           | Proprietary MySQL error codes and `SQLSTATE` ANSI and ODBC standard.              | When rewriting error handling code, consider switching to the more standard `SQLSTATE` error codes.                                                                                                      |
| Deterministic rules regarding condition handler run — always the next code block in statement order. | May be non-deterministic if multiple handlers have the same precedence and scope. | Review the handler scope and handler choice sections.                                                                                                                                                    |

For more information, see [The MySQL Diagnostics Area](https://dev.mysql.com/doc/refman/5.7/en/diagnostics-area.html "https://dev.mysql.com/doc/refman/5.7/en/diagnostics-area.html") and [Condition Handling](https://dev.mysql.com/doc/refman/5.7/en/condition-handling.html "https://dev.mysql.com/doc/refman/5.7/en/condition-handling.html") in the _MySQL documentation_.
