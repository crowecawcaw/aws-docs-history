Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating stored procedures in Amazon Redshift

This topic describes how to create and use stored procedures in Amazon Redshift. A stored
procedure is a collection of SQL statements that multiple programs can use.

You can define an Amazon Redshift stored procedure using the PostgreSQL procedural language PL/pgSQL
to perform a set of SQL queries and logical operations. The procedure is stored in the
database and available for any user with sufficient database privileges.

Unlike a user-defined function (UDF), a stored procedure can incorporate data definition
language (DDL) and data manipulation language (DML) in addition to SELECT queries. A stored
procedure doesn't need to return a value. You can use procedural language, including looping
and conditional expressions, to control logical flow.

For details about SQL commands to create and manage stored procedures, see the following
command topics:

- [CREATE PROCEDURE](r_CREATE_PROCEDURE.md "r_CREATE_PROCEDURE.md")
- [ALTER PROCEDURE](r_ALTER_PROCEDURE.md "r_ALTER_PROCEDURE.md")
- [DROP PROCEDURE](r_DROP_PROCEDURE.md "r_DROP_PROCEDURE.md")
- [SHOW PROCEDURE](r_SHOW_PROCEDURE.md "r_SHOW_PROCEDURE.md")
- [CALL](r_CALL_procedure.md "r_CALL_procedure.md")
- [GRANT](r_GRANT.md "r_GRANT.md")
- [REVOKE](r_REVOKE.md "r_REVOKE.md")
- [ALTER DEFAULT PRIVILEGES](r_ALTER_DEFAULT_PRIVILEGES.md "r_ALTER_DEFAULT_PRIVILEGES.md")

###### Topics

- [Overview of stored procedures in Amazon Redshift](stored-procedure-create.md "stored-procedure-create.md")
- [PL/pgSQL language reference](c_pl_pgSQL_reference.md "c_pl_pgSQL_reference.md")
