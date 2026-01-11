# Error handling for T-SQL

This topic provides reference information about error handling in SQL Server and Amazon Aurora PostgreSQL, focusing on the differences and similarities between the two systems. You can use this knowledge to understand how error handling mechanisms in SQL Server translate to Aurora PostgreSQL when migrating your database. The topic compares specific error handling features, such as TRY…​CATCH blocks and THROW statements, with their PostgreSQL equivalents.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                                                            |
| ------------------------------ | ---------------------------------- | ------------------------- | -------------------------------------------------------------------------- |
| Two star feature compatibility | Three star automation level        | N/A                       | Different paradigm and syntax will require rewrite of error handling code. |

## SQL Server Usage

SQL Server error handling capabilities have significantly improved throughout the years. However, previous features are retained for backward compatibility.

Before SQL Server 2008, only very basic error handling features were available. `RAISERROR` was the primary statement used for error handling.

Starting from SQL Server 2008, the extensive .NET-like error handling capabilities were added. They included `TRY…​CATCH` blocks, `THROW` statements, the `FORMATMESSAGE` function, and a set of system functions that return metadata for the current error condition.

### TRY…​CATCH Blocks

`TRY…​CATCH` blocks implement error handling similar to Microsoft Visual C# and Microsoft Visual C++. `TRY …​ END TRY` statement blocks can contain T-SQL statements.

If an error is raised by any of the statements within the `TRY …​ END TRY` block, the run stops and is moved to the nearest set of statements that are bounded by a `CATCH …​ END CATCH` block.

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

```
THROW [Error Number>, <Error Message>, < Error State>] [;]
```

### Examples

The following example uses `TRY…​CATCH` error blocks to handle key violations.

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
Can't insert duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
```

###### Note

Contrary to what many SQL developers believe, the values 1 and 2 are indeed inserted into `ErrorTestTable` in the preceding example. This behavior is in accordance with ANSI specifications stating that a constraint violation should not roll back an entire transaction.

The following example uses `THROW` with variables.

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
Can't insert duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
```

### RAISERROR

The `RAISERROR` statement is used to explicitly raise an error message, similar to `THROW`. It causes an error state for the run session and forwards run to either the calling scope or, if the error occurred within a `TRY …​ END TRY` block, to the associated `CATCH …​ END CATCH` block. `RAISERROR` can reference a user-defined message stored in the `sys.messages` system table or can be used with dynamic message text.

The key differences between `THROW` and `RAISERROR` are:

- Message IDs passed to `RAISERROR` must exist in the sys.messages system table. The error number parameter passed to THROW doesn’t.
- `RAISERROR` message text may contain `printf` formatting styles. The message text of `THROW` may not.
- `RAISERROR` uses the severity parameter for the error returned. For `THROW`, severity is always 16.

```
RAISERROR (<Message ID>|<Message Text>, <Message Severity>, <Message State>
[WITH option [<Option List>]])
```

The following example raises a custom error.

```
RAISERROR (N'This is a custom error message with severity 10 and state 1.', 10, 1)
```

### FORMATMESSAGE

`FORMATMESSAGE` returns a sting message consisting of an existing error message in the `sys.messages` system table, or from a text string, using the optional parameter list replacements. The `FORMATMESSAGE` statement is similar to the `RAISERROR` statement.

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

The following example uses error state functions within a `CATCH` block.

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
Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE543C8912D8'. Can't insert
duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
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
Violation of PRIMARY KEY constraint 'PK__ErrorTes__A259EE543C8912D8'. Can't insert
duplicate key in object 'dbo.ErrorTest'. The duplicate key value is (1).
```

For more information, see [RAISERROR (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-ver15"), [TRY…​CATCH (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/try-catch-transact-sql?view=sql-server-ver15"), and [THROW (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/throw-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/language-elements/throw-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Amazon Aurora PostgreSQL-Compatible Edition (Aurora PostgreSQL) doesn’t provide native replacement for SQL Server error handling features and options, but it has many comparable options.

To trap the errors, use the `BEGIN.. EXCEPTION.. END`. By default, any error raised in a PL/pgSQL function block stops running and the surrounding transaction. You can trap and recover from errors using a `BEGIN` block with an `EXCEPTION` clause. The syntax is an extension to the normal syntax for a `BEGIN` block.

### Syntax

```
[ <<label>> ]
[ DECLARE
  declarations ]
BEGIN
  statements
EXCEPTION
  WHEN condition [ OR condition ... ] THEN
    handler_statements
  [ WHEN condition [ OR condition ... ] THEN
    handler_statements
  ... ]
END;
```

For the preceding example, condition is related to the error or the code. For example:

- `WHEN interval_field_overflow THEN…​`
- `WHEN SQLSTATE '22015' THEN…​`

For all error codes, see [PostgreSQL Error Codes](https://www.postgresql.org/docs/13/errcodes-appendix.html "https://www.postgresql.org/docs/13/errcodes-appendix.html") in the _PostgreSQL documentation_.

### Throw errors

You can use the PostgreSQL `RAISE` statement to throw errors. You can combine `RAISE` with several levels of severity including:

| Severity       | Usage                                                                                |
| -------------- | ------------------------------------------------------------------------------------ |
| DEBUG1..DEBUG5 | Provides successively more detailed information for use by developers.               |
| INFO           | Provides information implicitly requested by the user.                               |
| NOTICE         | Provides information that might be helpful to users.                                 |
| WARNING        | Provides warnings of likely problems.                                                |
| ERROR          | Reports an error that caused the current command to abort.                           |
| LOG            | Reports information of interest to administrators. For example, checkpoint activity. |
| FATAL          | Reports an error that caused the current session to abort.                           |
| PANIC          | Reports an error that caused all database sessions to abort.                         |

### Examples

The following example uses `RAISE DEBUG`, where `DEBUG` is the configurable severity level.

```
SET CLIENT_MIN_MESSAGES = 'debug';

DO $$
BEGIN
RAISE DEBUG USING MESSAGE := 'hello world';
END $$;

DEBUG: hello world
DO
```

The following example uses the `client_min_messages` parameter to control the level of messages sent to the client. The default is `NOTICE`. Use the `log_min_messages` parameter to control which message levels are written to the server log. The default is `WARNING`.

```
SET CLIENT_MIN_MESSAGES = 'debug';
```

The following example uses `EXCEPTION..WHEN…​THEN` inside `BEGIN` and `END` block to handle dividing by zero violations.

```
CREATE TABLE ErrorTest (Col1 INT NOT NULL PRIMARY KEY);
```

```
INSERT INTO employee values ('John',10);
BEGIN
  SELECT 5/0;
EXCEPTION
  WHEN division_by_zero THEN
    RAISE NOTICE 'caught division_by_zero';
  return 0;
END;
```

## Summary

The following table identifies similarities, differences, and key migration considerations.

| SQL Server error handling feature                         | Aurora PostgreSQL equivalent                                      |
| --------------------------------------------------------- | ----------------------------------------------------------------- |
| `TRY …​ END TRY` and `CATCH …​ END CATCH` blocks          | `<br>Inner<br>BEGIN<br>...<br>EXCEPTION WHEN ... THEN<br>END<br>` |
| `THROW` and `RAISERROR`                                   | `RAISE`                                                           |
| `FORMATMESSAGE`                                           | `RAISE [ level ] 'format'` or `ASSERT`                            |
| Error state functions                                     | `GET STACKED DIAGNOSTICS`                                         |
| Proprietary error messages in `sys.messages` system table | RAISE                                                             |

For more information, see [Error Handling](https://www.postgresql.org/docs/13/ecpg-errors.html "https://www.postgresql.org/docs/13/ecpg-errors.html"), [Errors and Messages](https://www.postgresql.org/docs/13/plpgsql-errors-and-messages.html "https://www.postgresql.org/docs/13/plpgsql-errors-and-messages.html"), and [When to Log](https://www.postgresql.org/docs/13/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES "https://www.postgresql.org/docs/13/runtime-config-logging.html#GUC-LOG-MIN-MESSAGES") in the _PostgreSQL documentation_.
