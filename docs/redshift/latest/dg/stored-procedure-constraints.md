Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Stored procedure limitations

This topic describes limitations for Amazon Redshift stored procedures.

The following considerations apply when you use Amazon Redshift stored procedures.

## Differences between Amazon Redshift and PostgreSQL for stored procedure support

The following are differences between stored procedure support in Amazon Redshift and
PostgreSQL:

- Amazon Redshift doesn't support subtransactions, and hence has limited support for exception handling blocks.

## Considerations and limits

The following are considerations on stored procedures in Amazon Redshift:

- The maximum number of stored procedures for a database is 10,000.
- The maximum size of the source code for a procedure is 2 MB.
- The maximum number of explicit and implicit cursors that you can open concurrently in a user
  session is one. FOR loops that iterate over the result set of a SQL statement
  open implicit cursors. Nested cursors aren't supported.
- Explicit and implicit cursors have the same restrictions on the result set size as standard Amazon Redshift cursors.
  For more information, see [Cursor constraints](declare.md#declare-constraints "declare.md#declare-constraints").
- The maximum number of levels for nested calls is 16.
- The maximum number of procedure parameters is 32 for input arguments and 32 for output arguments.
- The maximum number of variables in a stored procedure is 1,024.
- Any SQL command that requires its own transaction context isn't supported inside a stored
  procedure. Examples include:
  - PREPARE
  - CREATE/DROP DATABASE
  - CREATE EXTERNAL TABLE
  - VACUUM
  - SET LOCAL
  - ALTER TABLE APPEND

- The `registerOutParameter` method call through the Java
  Database Connectivity (JDBC) driver isn't supported for the `refcursor` data type.

For an example of using the `refcursor` data type, see [Returning a result set from a stored procedure](stored-procedure-result-set.md "stored-procedure-result-set.md").
