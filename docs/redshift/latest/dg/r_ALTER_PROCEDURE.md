Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER PROCEDURE

Renames a procedure or changes the owner. Both the procedure name and data types, or
signature, are required. Only the owner or a superuser can rename a procedure. Only a
superuser can change the owner of a procedure.

## Syntax

```
ALTER PROCEDURE *sp\_name* [ ( [ [ argname ] [ argmode ] argtype [, ...] ] ) ]
    RENAME TO new_name

```

```
ALTER PROCEDURE *sp\_name* [ ( [ [ argname ] [ argmode ] argtype [, ...] ] ) ]
    OWNER TO { new_owner | CURRENT_USER | SESSION_USER }

```

## Parameters

_sp_name_

The name of the procedure to be altered. Either specify just the name of the
procedure in the current search path, or use the format
`schema_name.sp_procedure_name` to use a specific schema.

_[argname] [argmode] argtype_

A list of argument names, argument modes, and data types. Only the input
data types are required, which are used to identify the stored procedure.
Alternatively, you can provide the full signature used to create the procedure
including the input and output parameters with their modes.

_new_name_

A new name for the stored procedure.

_new_owner_ | CURRENT_USER | SESSION_USER

A new owner for the stored procedure.

## Examples

The following example changes the name of a procedure from
`first_quarter_revenue` to `quarterly_revenue`.

```
ALTER PROCEDURE first_quarter_revenue(volume INOUT bigint, at_price IN numeric,
 result OUT int) RENAME TO quarterly_revenue;

```

This example is equivalent to the following.

```
ALTER PROCEDURE first_quarter_revenue(bigint, numeric) RENAME TO quarterly_revenue;
```

The following example changes the owner of a procedure to
`etl_user`.

```
ALTER PROCEDURE quarterly_revenue(bigint, numeric) OWNER TO etl_user;
```
