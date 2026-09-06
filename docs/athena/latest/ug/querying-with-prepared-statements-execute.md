

# EXECUTE
<a name="querying-with-prepared-statements-execute"></a>

Runs a prepared statement. Values for parameters are specified in the `USING` clause.

## Syntax
<a name="querying-with-prepared-statements-execute-syntax"></a>

```
EXECUTE {{statement_name}} [USING {{value1}} [ ,{{value2}}, ... ] ]
```

{{statement\_name}} is the name of the prepared statement. {{value1}} and {{value2}} are the values to be specified for the parameters in the statement.

## EXECUTE examples
<a name="querying-with-prepared-statements-execute-examples"></a>

The following example runs the `my_select1` prepared statement, which contains no parameters.

```
EXECUTE my_select1
```

The following example runs the `my_select2` prepared statement, which contains a single parameter.

```
EXECUTE my_select2 USING 2012
```

The following example runs the `my_select3` prepared statement, which has two parameters.

```
EXECUTE my_select3 USING 346078, 12
```

The following example supplies a string value for a parameter in the prepared statement `my_insert`.

```
EXECUTE my_insert USING 'usa'
```

The following example supplies a numerical value for the `productid` parameter in the prepared statement `my_unload`.

```
EXECUTE my_unload USING 12
```