# sp_babelfish_volatility

PostgreSQL function volatility helps the optimizer for a better query execution which when used in parts of certain clauses has a significant impact on query performance.

## Syntax

```
sp_babelfish_volatility ‘function_name’, ‘volatility’
```

## Arguments

_function_name (optional)_

You can either specify the value of this argument with a two-part name as `schema_name.function_name`or only the `function_name`.
If you specify only the `function_name`, the schema name is the default schema for the current user.

_volatility (optional)_

The valid PostgreSQL values of volatility are `stable`, `volatile`, or `immutable`. For more information,
see [https://www.postgresql.org/docs/current/xfunc-volatility.html](https://www.postgresql.org/docs/current/xfunc-volatility.html "https://www.postgresql.org/docs/current/xfunc-volatility.html")

###### Note

When `sp_babelfish_volatility` is called with `function_name` which has multiple definitions, it will throw an error.

## Result set

If the parameters are not mentioned then the result set is displayed under the following columns: `schemaname`, `functionname`, `volatility`.

## Usage notes

PostgreSQL function volatility helps the optimizer for a better query execution which when used in parts of certain clauses has a significant impact on query performance.

## Examples

The following examples shows how to create simple functions and later explains how to use `sp_babelfish_volatility` on these functions
using different methods.

```
`1>` create function f1() returns int as begin return 0 end
`2>` go
```

```
`1>` create schema test_schema
`2>` go
```

```
`1>` create function test_schema.f1() returns int as begin return 0 end
`2>` go
```

The following example displays volatility of the functions:

```
`1>` exec sp_babelfish_volatility
`2>` go
            `schemaname functionname volatility
----------- ------------ ----------
dbo f1 volatile
test_schema f1 volatile`
```

The following example shows how to change the volatility of the functions:

```
`1>` exec sp_babelfish_volatility 'f1','stable'
`2>` go
`1>` exec sp_babelfish_volatility 'test_schema.f1','immutable'
`2>` go

```

When you specify only the function_name, it displays the schema name, function name and volatility of that function.
The following example displays volatility of functions after changing the values:

```
`1>` exec sp_babelfish_volatility 'test_schema.f1'
`2>` go
            `schemaname functionname volatility
----------- ------------ ----------
test_schema f1 immutable`
```

```
`1>` exec sp_babelfish_volatility 'f1'
`2>` go
            `schemaname functionname volatility
----------- ------------ ----------
dbo f1 stable`
```

When you don't specify any argument, it displays a list of functions (schema name, function name, volatility of the functions) present in the current database:

```
`1>` exec sp_babelfish_volatility
`2>` go
            `schemaname functionname volatility
----------- ------------ ----------
dbo f1 stable
test_schema f1 immutable`
```
