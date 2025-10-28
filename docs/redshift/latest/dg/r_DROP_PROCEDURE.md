Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# DROP PROCEDURE

Drops a procedure. To drop a procedure, both the procedure name and input argument data
types (signature), are required. Optionally, you can include the full argument data types,
including OUT arguments. To find the signature for a procedure, use the [SHOW PROCEDURE](r_SHOW_PROCEDURE.md "r_SHOW_PROCEDURE.md") command. For more
information about procedure signatures, see [PG_PROC_INFO](r_PG_PROC_INFO.md "r_PG_PROC_INFO.md").

## Required privileges

Following are required privileges for DROP PROCEDURE:

- Superuser
- Users with the DROP PROCEDURE privilege
- Procedure owner

## Syntax

```
DROP PROCEDURE sp_name ( [ [ argname ] [ argmode ] argtype [, ...] ] )

```

## Parameters

_sp_name_

The name of the procedure to be removed.

_argname_

The name of an input argument. DROP PROCEDURE ignores argument names,
because only the argument data types are needed to determine the
procedure's identity.

_argmode_

The mode of an argument, which can be IN, OUT, or INOUT. OUT arguments are
optional because they aren't used to identify a stored procedure.

_argtype_

The data type of the input argument. For a list of the supported data types,
see [Data types](c_Supported_data_types.md "c_Supported_data_types.md").

## Examples

The following example drops a stored procedure named
`quarterly_revenue`.

```
DROP PROCEDURE quarterly_revenue(volume INOUT bigint, at_price IN numeric,result OUT int);
```
