Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER FUNCTION

Renames a function or changes the owner. Both the function name and data types are
required. Only the owner or a superuser can rename a function. Only a superuser can change
the owner of a function.

## Syntax

```
ALTER FUNCTION function_name ( { [ py_arg_name py_arg_data_type | sql_arg_data_type } [ , ... ] ] )
     RENAME TO new_name

```

```
ALTER FUNCTION function_name ( { [ py_arg_name py_arg_data_type | sql_arg_data_type } [ , ... ] ] )
     OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

```

## Parameters

_function_name_

The name of the function to be altered. Either specify the name of the
function in the current search path, or use the format
`schema_name.function_name` to use a specific schema.

_py_arg_name py_arg_data_type | sql_arg_data_type_

Optional. A list of input argument names and data types for the Python
user-defined function, or a list of input argument data types for the SQL
user-defined function.

_new_name_

A new name for the user-defined function.

_new_owner_ | CURRENT_USER | SESSION_USER

A new owner for the user-defined function.

## Examples

The following example changes the name of a function from
`first_quarter_revenue` to `quarterly_revenue`.

```
ALTER FUNCTION first_quarter_revenue(bigint, numeric, int)
         RENAME TO quarterly_revenue;
```

The following example changes the owner of the `quarterly_revenue`
function to `etl_user`.

```
ALTER FUNCTION quarterly_revenue(bigint, numeric) OWNER TO etl_user;
```
