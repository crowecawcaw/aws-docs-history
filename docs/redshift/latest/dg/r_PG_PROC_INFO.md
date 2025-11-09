Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_PROC_INFO

PG_PROC_INFO is an Amazon Redshift system view built on the PostgreSQL catalog table PG_PROC and
the internal catalog table PG_PROC_EXTENDED. PG_PROC_INFO includes details about stored
procedures and functions, including information related to output arguments, if
any.

## Table columns

PG_PROC_INFO shows the following columns in addition to the columns in
PG_PROC. The `oid` column in PG_PROC is called `prooid` in the PG_PROC_INFO table.

| Column name    | Data type | Description                                                                                                                                                                                                                                                                                            |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| prooid         | oid       | The object ID of the function or stored<br>procedure.                                                                                                                                                                                                                                                  |
| prokind        | "char"    | A value that indicates the type of functions or<br>stored procedures. This value is 'f' for regular functions, 'p' for<br>stored procedures, and 'a' for aggregate functions.                                                                                                                          |
| proargmodes    | "char"[ ] | An array with the modes of the procedure<br>arguments, encoded as 'i' for IN arguments, 'o' for OUT arguments,<br>and 'b' for INOUT arguments. If all the arguments are IN arguments,<br>this field is NULL. Subscripts correspond to positions in the<br>proallargtypes array.                        |
| proallargtypes | oid[ ]    | An array with the data types of the procedure<br>arguments. This array includes all types of arguments (including OUT<br>and INOUT arguments). However, if all the arguments are IN<br>arguments, this field is NULL. Subscripting is one-based. In contrast,<br>proargtypes is subscripted from zero. |

The field proargnames in PG_PROC_INFO contains the names of all types of arguments
(including OUT and INOUT), if any.
