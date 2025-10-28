Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SET_CONFIG

Sets a configuration parameter to a new setting.

This function is equivalent to the SET command in SQL.

## Syntax

```
SET_CONFIG(*'parameter'*, '*new\_value*' , *is\_local*)
```

The following statement sets a session context variable to a new setting.

```
set_config(*'variable\_name'*, '*new\_value*' , *is\_local*)
```

## Arguments

_parameter_

Parameter to set.

_variable_name_

The name of the variable to set.

_new_value_

New value of the parameter.

_is_local_

If true, parameter value applies only to the current transaction. Valid
values are `true` or `1` and `false` or
`0`.

## Return type

Returns a `CHAR` or `VARCHAR` string.

## Examples

To set the value of the `query_group` parameter to
`test` for the current transaction only, use the following example.

````
`SELECT SET_CONFIG('query_group', 'test', true);`

`+------------+
| set_config | +------------+
| test | +------------+` ``` To set session context variables, use the following example. ``` `SELECT SET_CONFIG(‘app.username’, ‘cuddy’, FALSE);` ```
````
