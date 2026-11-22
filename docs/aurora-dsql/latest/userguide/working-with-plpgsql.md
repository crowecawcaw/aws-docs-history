

# PL/pgSQL in Aurora DSQL

Aurora DSQL supports PL/pgSQL, the procedural language for PostgreSQL. With PL/pgSQL, you can create functions, procedures, and anonymous code blocks. These blocks combine SQL statements with procedural control flow, including conditionals, loops, and variable assignments. If you have existing PostgreSQL apps that use stored procedures or functions, you can run them in Aurora DSQL with minimal changes.

Aurora DSQL supports the PL/pgSQL features described in the [PostgreSQL PL/pgSQL documentation](https://www.postgresql.org/docs/current/plpgsql.html) on the PostgreSQL website. The following sections describe the supported SQL statements and the Aurora DSQL-specific considerations that apply.

## Supported statements
<a name="working-with-plpgsql-statements"></a>

Aurora DSQL supports the following statements for creating and invoking PL/pgSQL code.

**`CREATE FUNCTION`**  
Creates a PL/pgSQL function that returns a value.  

```sql
CREATE FUNCTION increment(val integer) RETURNS integer
LANGUAGE plpgsql AS $$
BEGIN
  RETURN val + 1;
END;
$$;
```

**`CREATE PROCEDURE`**  
Creates a PL/pgSQL procedure that performs actions without returning a value. Procedures can contain transaction control statements (`COMMIT` and `ROLLBACK`) when called at the top level.  

```sql
CREATE PROCEDURE insert_row(p_id integer, p_value text)
LANGUAGE plpgsql AS $$
BEGIN
  INSERT INTO my_table VALUES (p_id, p_value);
END;
$$;
```

**`CALL`**  
Invokes a procedure.  

```sql
CALL insert_row(1, 'hello');
```

**`DO`**  
Runs an anonymous PL/pgSQL code block without creating a persistent function.  

```sql
DO $$
BEGIN
  INSERT INTO my_table VALUES (1, 'from do block');
END;
$$;
```

## Considerations
<a name="working-with-plpgsql-considerations"></a>

The following Aurora DSQL-specific considerations apply when using PL/pgSQL features. Attempts to use unsupported features return an error with SQLSTATE `0A000` (`FEATURE_NOT_SUPPORTED`).

**Trapping errors**  
Handle errors at the app level instead of using `EXCEPTION` blocks. `BEGIN...EXCEPTION...END` blocks aren't supported.  

```sql
-- Not supported
BEGIN
  INSERT INTO t VALUES (1);
EXCEPTION
  WHEN unique_violation THEN
    RAISE NOTICE 'duplicate';
END;
```

**Explicit cursor operations**  
Use `FOR...IN query` loops for iterating over result sets. Explicit cursor declarations (`CURSOR`, `REFCURSOR`), cursor operations (`OPEN`, `FETCH`, `MOVE`, `CLOSE`), and `FOR...IN cursor` loops aren't supported.

**Diagnostic messages**  
Use `RAISE NOTICE` or `RAISE WARNING` to send messages to the client. `RAISE LOG` and `RAISE DEBUG` aren't supported.

**Error codes in `RAISE`**  
Use standard user-defined error codes such as `P0001` with `RAISE EXCEPTION`. System-reserved error codes (such as `XX000`, data corruption codes, or I/O error codes) aren't supported for user code.