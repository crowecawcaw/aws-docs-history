

# `CREATE FUNCTION`
<a name="create-function-syntax-support"></a>

`CREATE FUNCTION` defines a new function.

**Important**  
In Amazon Aurora DSQL, `CREATE FUNCTION` only supports SQL-language functions (`LANGUAGE sql`). 

## Supported syntax
<a name="create-function-supported-syntax"></a>

```
CREATE [ OR REPLACE ] FUNCTION
    name ( [ [ argmode ] [ argname ] argtype [ { DEFAULT | = } default_expr ] [, ...] ] )
    [ RETURNS rettype
      | RETURNS TABLE ( column_name column_type [, ...] ) ]
  { LANGUAGE sql
    | { IMMUTABLE | STABLE | VOLATILE }
    | { CALLED ON NULL INPUT | RETURNS NULL ON NULL INPUT | STRICT }
    | { [ EXTERNAL ] SECURITY INVOKER | [ EXTERNAL ] SECURITY DEFINER }
    | PARALLEL { UNSAFE | RESTRICTED | SAFE }
    | COST execution_cost
    | ROWS result_rows
    | SET configuration_parameter { TO value | = value | FROM CURRENT }
    | AS 'definition'
    | RETURN expression
    | BEGIN ATOMIC statement; [ statement; ... ] END
  } ...

where LANGUAGE must be sql
```

## Description
<a name="create-function-description"></a>

`CREATE FUNCTION` defines a new function. `CREATE OR REPLACE FUNCTION` will either create a new function, or replace an existing definition. To be able to define a function, you must have the `USAGE` privilege on the language.

If a schema name is included, then the function is created in the specified schema. Otherwise, the function is created in the current schema. The name of the new function must not match any existing function with the same input argument types in the same schema. However, functions of different argument types can share a name (this is called *overloading*).

To replace the current definition of an existing function, use `CREATE OR REPLACE FUNCTION`. You can't change the name or argument types of a function this way (this would actually create a new, distinct function). Also, you can't use `CREATE OR REPLACE FUNCTION` to change the return type of an existing function. To do that, you must drop and recreate the function.

When `CREATE OR REPLACE FUNCTION` is used to replace an existing function, the ownership and permissions of the function don't change. All other function properties are assigned the values specified or implied in the command. You must own the function to replace it (this includes being a member of the owning role). 

If you drop and then recreate a function, the new function isn't the same entity as the old; you will have to drop existing rules, views, and so on, that refer to the old function. Use `CREATE OR REPLACE FUNCTION` to change a function definition without breaking objects that refer to the function. 

You become the owner of a function that you created.

To be able to create a function, you must have `USAGE` privilege on the argument types and the return type.

A `SQL` function wraps one or more `SQL` statements into a reusable, callable unit. Use functions to centralize common expressions or calculations, apply consistent logic across multiple queries, and simplify application code by calling a single function instead of repeating the same `SQL`. 

## Parameters
<a name="create-function-parameters"></a>

**{{name}}**  
The name (optionally schema-qualified) of the function to create.

**{{argmode}}**  
The mode of an argument: `IN`, `OUT`, `INOUT`, or `VARIADIC`. If omitted, the default is `IN`. `VARIADIC` must be the last input parameter; only `OUT` arguments can follow it. `OUT` and `INOUT` arguments can't be combined with the `RETURNS TABLE` notation.

**{{argname}}**  
The name of an argument. In a SQL function, you can refer to an argument by name in the function body. The name of an `OUT` or `INOUT` argument is also significant, because it defines the corresponding column name in the result row type.

**{{argtype}}**  
The data type of an argument. This can be any Aurora DSQL-supported base type, array type, or domain. For more information, see [Supported data types in Aurora DSQL](working-with-postgresql-compatibility-supported-data-types.md). You can also reference the type of an existing table column by using the `%TYPE` notation.

**{{default\_expr}}**  
An expression to be used as the default value if the argument isn't specified. The expression has to be coercible to the argument type of the parameter. Only `IN` and `INOUT` arguments can have a default value. Each argument after one with a default value must also have a default value.

**{{rettype}}**  
The return data type. This can be any Aurora DSQL-supported base type, array type, or domain. For more information, see [Supported data types in Aurora DSQL](working-with-postgresql-compatibility-supported-data-types.md). To return a set of rows, use `SETOF {{rettype}}` or `RETURNS TABLE`. If the function isn't supposed to return a value, specify `void` as the return type. When there are `OUT` or `INOUT` parameters, the `RETURNS` clause can be omitted, and the function returns a `record` or the corresponding row type.

**`RETURNS TABLE ( {{column_name}} {{column_type}} [, ...] )`**  
Specifies that the function returns a set of rows with the named columns and their types. This is equivalent to declaring one or more `OUT` parameters and specifying `SETOF` as the return type.

**`LANGUAGE sql`**  
The language used to implement the function. In Aurora DSQL, this must be `sql`. If you omit the `LANGUAGE` clause and provide a `BEGIN ATOMIC` or `RETURN` body, `sql` is assumed. A string-constant body (`AS '{{definition}}'`) requires an explicit `LANGUAGE sql` clause; omitting it fails with the error `no language specified`.

**`IMMUTABLE` / `STABLE` / `VOLATILE`**  
These attributes inform the query optimizer about the behavior of the function. You can specify at most one. If you omit all three, the function defaults to `VOLATILE`.  
+ `IMMUTABLE` indicates that the function can't modify the database and always returns the same result when given the same argument values.
+ `STABLE` indicates that the function can't modify the database. Within a single table scan, it consistently returns the same result for the same argument values, but the result might change across SQL statements.
+ `VOLATILE` indicates that the function value can change even within a single table scan, so no optimizations can be made.

**`CALLED ON NULL INPUT` / `RETURNS NULL ON NULL INPUT` / `STRICT`**  
`CALLED ON NULL INPUT` (the default) indicates that the function is called normally when some of its arguments are null. `RETURNS NULL ON NULL INPUT` or `STRICT` indicates that the function always returns null when any of its arguments are null. If specified, Aurora DSQL doesn't execute the function when any argument is null; instead, the function automatically returns null. 

**`[ EXTERNAL ] SECURITY INVOKER` / `[ EXTERNAL ] SECURITY DEFINER`**  
`SECURITY INVOKER` (the default) indicates that the function is to be executed with the privileges of the user that calls it. `SECURITY DEFINER` specifies that the function is to be executed with the privileges of the user that owns it. The key word `EXTERNAL` is allowed for SQL conformance, but it's optional.

**`PARALLEL { UNSAFE | RESTRICTED | SAFE }`**  
Aurora DSQL accepts and stores the `PARALLEL` marking. However, this marking doesn't affect query execution. 

**`COST {{execution_cost}}`**  
A positive number giving the estimated execution cost for the function. If the function returns a set, this value is the estimated cost per returned row. The query planner uses this estimate when it does not inline the function.

**`ROWS {{result_rows}}`**  
A positive number giving the estimated number of rows that the query planner should expect the function to return. This is only allowed when the function is declared to return a set. The default assumption is 1000 rows.

**`SET {{configuration_parameter}} { TO {{value}} | = {{value}} | FROM CURRENT }`**  
The `SET` clause causes the specified configuration parameter to be set to the specified value when the function is entered, and then restored to its prior value when the function exits. `SET FROM CURRENT` saves the value of the parameter that is current when `CREATE FUNCTION` is run as the value to be applied when the function is entered.

**`AS '{{definition}}'`**  
A string constant defining the function; the meaning depends on the language. For a SQL-language function, it is the SQL statements that make up the function body.

**`RETURN {{expression}}`**  
Defines the function body using the SQL-standard syntax for a function that returns a single expression. This is an alternative to the string-constant form.

**`BEGIN ATOMIC {{statement}}; [ ... ] END`**  
Defines the function body using the SQL-standard syntax. The body consists of one or more SQL statements. This form is only valid for `LANGUAGE sql`. The statements in an atomic body are tracked as dependencies of the function. For example, a table referenced in the body cannot be dropped without also dropping the function, or using `DROP ... CASCADE`.

## Notes
<a name="create-function-notes"></a>

Use the `DROP FUNCTION` statement to remove a function. You can also grant and revoke privileges on a function with `GRANT` and `REVOKE` (for example, `REVOKE ALL ON FUNCTION`).

Any function that reads or modifies data in tables is subject to the same transaction and concurrency behavior as the equivalent SQL statements run directly. Functions declared `IMMUTABLE` or `STABLE` must not modify the database.

To update the definition of an existing function, use `CREATE OR REPLACE FUNCTION`. You can't change the argument types or return type of a function this way; instead, drop and recreate the function.

To rename a function, change its owner, or move it to another schema, use `ALTER FUNCTION`. To change any other attributes, use `CREATE OR REPLACE FUNCTION` with the desired changes. For more information, see [`ALTER FUNCTION`](alter-function-syntax-support.md).

Function overloading is supported: you can define several functions with the same name as long as their input argument types differ. A user-defined function can also call other functions, and can shadow a built-in function of the same name and argument types.

For a function that returns a set (`SETOF` or `RETURNS TABLE`) whose body contains more than one statement, only the result of the final statement is returned. The function still executes the earlier statements, but discards their results. This is the standard behavior for SQL-language functions. Structure the function so that its final statement produces the complete result set.

A set-returning function doesn't guarantee any particular row order. To control row order, include an `ORDER BY` clause in the query.

## Considerations
<a name="create-function-considerations"></a>

The following `CREATE FUNCTION` capabilities return the error shown.

**`LEAKPROOF`**  
Returns the error `only superuser can define a leakproof function`. `NOT LEAKPROOF` (the default) is accepted.

**`TRANSFORM FOR TYPE`**  
Returns the error `transform for type {{type}} language "sql" does not exist`.

**`SUPPORT` (planner support function)**  
Returns the error `function {{name}}(internal) does not exist`.

**User-defined composite types (`CREATE TYPE ... AS`), including functions that return a composite type**  
Returns the error `unsupported statement: CompositeType`.

Aurora DSQL doesn't support `CREATE PROCEDURE`, which fails with the error `PROCEDURE is not supported`.

The `WINDOW` attribute is accepted syntactically but isn't useful for SQL-language functions. Avoid using this attribute.

## Examples
<a name="create-function-examples"></a>

Create a simple SQL function that adds two integers, using a string-constant body:

```
CREATE FUNCTION add(integer, integer) RETURNS integer
    AS 'SELECT $1 + $2;'
    LANGUAGE sql
    IMMUTABLE
    RETURNS NULL ON NULL INPUT;
```

Create the same function using the SQL-standard `RETURN` body and named arguments:

```
CREATE FUNCTION add(a integer, b integer) RETURNS integer
    LANGUAGE sql
    IMMUTABLE
    RETURN a + b;
```

Create a function that returns a set of rows using `RETURNS TABLE` and a `BEGIN ATOMIC` body:

```
CREATE FUNCTION employees_in_dept(dept_id integer)
    RETURNS TABLE (id integer, name text)
    LANGUAGE sql
    STABLE
    BEGIN ATOMIC
        SELECT id, name FROM employees WHERE department_id = dept_id;
    END;
```

Create a function that runs with the privileges of its owner, and sets a configuration parameter for the duration of the call:

```
CREATE FUNCTION current_department() RETURNS text
    LANGUAGE sql
    STABLE
    SECURITY DEFINER
    SET search_path = app
    AS 'SELECT current_setting(''app.department'');';
```

## Compatibility
<a name="create-function-compatibility"></a>

A `CREATE FUNCTION` command is defined in the SQL standard. The PostgreSQL implementation can be used in a compatible way but has many extensions. Conversely, the SQL standard specifies a number of optional features that are not implemented in PostgreSQL.

The following are important compatibility issues:
+ `OR REPLACE` is a PostgreSQL extension.
+ For compatibility with some other database systems, {{argmode}} can be written either before or after {{argname}}. But only the first way is standard-compliant.
+ For parameter defaults, the SQL standard specifies only the syntax with the `DEFAULT` key word. The syntax with `=` is used in T-SQL and Firebird.
+ The `SETOF` modifier is a PostgreSQL extension.
+ Only SQL is standardized as a language.
+ All other attributes except `CALLED ON NULL INPUT` and `RETURNS NULL ON NULL INPUT` are not standardized.
+ For the body of `LANGUAGE sql` functions, the SQL standard only specifies the {{sql\_body}} form.

Simple `LANGUAGE sql` functions can be written in a way that is both standard-conforming and portable to other implementations. More complex functions using advanced features, optimization attributes, or other languages will necessarily be specific to PostgreSQL in a significant way.