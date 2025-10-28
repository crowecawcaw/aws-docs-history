Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Leader node–only

functions

Some Amazon Redshift queries are distributed and run on the compute nodes; other queries run
exclusively on the leader node.

The leader node distributes SQL to the compute nodes when a query references
user-created tables or system tables (tables with an STL or STV prefix and system views
with an SVL or SVV prefix). A query that references only catalog tables (tables with a PG
prefix, such as PG_TABLE_DEF) or that does not reference any tables, runs exclusively on
the leader node.

Some Amazon Redshift SQL functions are supported only on the leader node and are not supported
on the compute nodes. A query that uses a leader-node function must run exclusively on the
leader node, not on the compute nodes, or it will return an error.

The documentation for each leader-node only function includes a note stating that the
function will return an error if it references user-defined tables or Amazon Redshift system
tables.

For more information, see [SQL functions supported on the leader
node](c_sql-functions-leader-node.md "c_sql-functions-leader-node.md").

The following SQL functions are leader-node only functions and are not supported on the
compute nodes:

System information functions

- CURRENT_SCHEMA
- CURRENT_SCHEMAS
- HAS_DATABASE_PRIVILEGE
- HAS_SCHEMA_PRIVILEGE
- HAS_TABLE_PRIVILEGE
  String functions

- SUBSTR
  Math functions

- FACTORIAL
- LOG
  The following leader-node only functions are deprecated and are no longer supported:

Date functions

- AGE
- CURRENT_TIME
- CURRENT_TIMESTAMP
- LOCALTIME
- ISFINITE
- NOW
  String functions

- GETBIT
- GET_BYTE
- SET_BIT
- SET_BYTE
- TO_ASCII
