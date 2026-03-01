# EXECUTE

Runs a prepared statement. Values for parameters are specified in the
`USING` clause.

## Syntax

```
EXECUTE `statement_name` [USING `value1` [ ,`value2`, ... ] ]
```

`statement_name` is the name of the prepared
statement. `value1` and
`value2` are the values to be specified for the
parameters in the statement.

## EXECUTE examples

The following example runs the `my_select1` prepared statement,
which contains no parameters.

```
EXECUTE **my\_select1**
```

The following example runs the `my_select2` prepared statement,
which contains a single parameter.

```
EXECUTE **my\_select2** USING 2012
```

The following example runs the `my_select3` prepared statement,
which has two parameters.

```
EXECUTE **my\_select3** USING 346078, 12
```

The following example supplies a string value for a parameter in the
prepared statement `my_insert`.

```
EXECUTE **my\_insert** USING 'usa'
```

The following example supplies a numerical value for the
`productid` parameter in the prepared statement
`my_unload`.

```
EXECUTE **my\_unload** USING 12
```
