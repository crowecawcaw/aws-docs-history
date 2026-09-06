

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# PG\_PROC\_INFO
<a name="r_PG_PROC_INFO"></a>

PG\_PROC\_INFO is an Amazon Redshift system view built on the PostgreSQL catalog table PG\_PROC and the internal catalog table PG\_PROC\_EXTENDED. PG\_PROC\_INFO includes details about stored procedures and functions, including information related to output arguments, if any.

## Table columns
<a name="r_PG_PROC_INFO-table-columns"></a>

PG\_PROC\_INFO shows the following columns in addition to the columns in PG\_PROC. The `oid` column in PG\_PROC is called `prooid` in the PG\_PROC\_INFO table.


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| prooid | oid | The object ID of the function or stored procedure. | 
| prokind | "char" | A value that indicates the type of functions or stored procedures. This value is 'f' for regular functions, 'p' for stored procedures, and 'a' for aggregate functions. | 
| proargmodes | "char"[ ]  | An array with the modes of the procedure arguments, encoded as 'i' for IN arguments, 'o' for OUT arguments, and 'b' for INOUT arguments. If all the arguments are IN arguments, this field is NULL. Subscripts correspond to positions in the proallargtypes array. | 
| proallargtypes | oid[ ]  | An array with the data types of the procedure arguments. This array includes all types of arguments (including OUT and INOUT arguments). However, if all the arguments are IN arguments, this field is NULL. Subscripting is one-based. In contrast, proargtypes is subscripted from zero. | 

The field proargnames in PG\_PROC\_INFO contains the names of all types of arguments (including OUT and INOUT), if any.