Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

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

_function\_name_

The name of the function to be altered. Either specify the name of the
function in the current search path, or use the format
`schema_name.function_name` to use a specific schema.

_py\_arg\_name py\_arg\_data\_type | sql\_arg\_data\_type_

Optional. A list of input argument names and data types for the Python
user-defined function, or a list of input argument data types for the SQL
user-defined function.

_new\_name_

A new name for the user-defined function.

_new\_owner_ | CURRENT\_USER | SESSION\_USER

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
