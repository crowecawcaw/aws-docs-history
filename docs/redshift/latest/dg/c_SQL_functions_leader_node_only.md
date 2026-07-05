Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Leader node–only functions

Some Amazon Redshift queries are distributed and run on the compute nodes; other queries run
exclusively on the leader node.

The leader node distributes SQL to the compute nodes when a query references
user-created tables or system tables (tables with an STL or STV prefix and system views
with an SVL or SVV prefix). A query that references only catalog tables (tables with a PG
prefix, such as PG\_TABLE\_DEF) or that does not reference any tables, runs exclusively on
the leader node.

Some Amazon Redshift SQL functions are supported only on the leader node and are not supported
on the compute nodes. A query that uses a leader-node function must run exclusively on the
leader node, not on the compute nodes, or it will return an error.

The documentation for each leader-node only function includes a note stating that the
function will return an error if it references user-defined tables or Amazon Redshift system
tables.

For more information, see [SQL functions supported on the leader node](c_sql-functions-leader-node.md "c_sql-functions-leader-node.md").

The following SQL functions are leader-node only functions and are not supported on the
compute nodes:

System information functions

- CURRENT\_SCHEMA
- CURRENT\_SCHEMAS
- HAS\_DATABASE\_PRIVILEGE
- HAS\_SCHEMA\_PRIVILEGE
- HAS\_TABLE\_PRIVILEGE
  String functions

- SUBSTR
  Math functions

- FACTORIAL
- LOG
  The following leader-node only functions are deprecated and are no longer supported:

Date functions

- AGE
- CURRENT\_TIME
- CURRENT\_TIMESTAMP
- LOCALTIME
- ISFINITE
- NOW
  String functions

- GETBIT
- GET\_BYTE
- SET\_BIT
- SET\_BYTE
- TO\_ASCII
