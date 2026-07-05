Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Unsupported PostgreSQL functions

Many functions that are not excluded have different semantics or usage. For
example, some supported functions will run only on the leader node. Also, some
unsupported functions will not return an error when run on the leader node. The fact
that these functions do not return an error in some cases should not be taken to
indicate that the function is supported by Amazon Redshift.

###### Important

Do not assume that the semantics of elements that Amazon Redshift and PostgreSQL have
in common are identical. Make sure to consult the _Amazon Redshift Database Developer Guide_
[SQL commands](c_SQL_commands.md "c_SQL_commands.md") to understand the
often subtle differences.

For more information, see [SQL functions supported on the leader node](c_sql-functions-leader-node.md "c_sql-functions-leader-node.md").

These PostgreSQL functions are not supported in Amazon Redshift.

- Access privilege inquiry functions
- Advisory lock functions
- Aggregate functions

  - STRING\_AGG()
  - ARRAY\_AGG()
  - EVERY()
  - XML\_AGG()
  - CORR()
  - COVAR\_POP()
  - COVAR\_SAMP()
  - REGR\_AVGX(), REGR\_AVGY()
  - REGR\_COUNT()
  - REGR\_INTERCEPT()
  - REGR\_R2()
  - REGR\_SLOPE()
  - REGR\_SXX(), REGR\_SXY(), REGR\_SYY()

- Array functions and operators
- Backup control functions
- Comment information functions
- Database object location functions
- Database object size functions
- Date/Time functions and operators

  - CLOCK\_TIMESTAMP()
  - JUSTIFY\_DAYS(), JUSTIFY\_HOURS(), JUSTIFY\_INTERVAL()
  - PG\_SLEEP()
  - TRANSACTION\_TIMESTAMP()

- ENUM support functions
- Geometric functions and operators
- Generic file access functions
- IS DISTINCT FROM
- Network address functions and operators
- Mathematical functions

  - DIV()
  - SETSEED()
  - WIDTH\_BUCKET()

- Set returning functions

  - GENERATE\_SERIES()
  - GENERATE\_SUBSCRIPTS()

- Range functions and operators
- Recovery control functions
- Recovery information functions
- ROLLBACK TO SAVEPOINT function
- Schema visibility inquiry functions
- Server signaling functions
- Snapshot synchronization functions
- Sequence manipulation functions
- String functions

  - BIT\_LENGTH()
  - OVERLAY()
  - CONVERT(), CONVERT\_FROM(), CONVERT\_TO()
  - ENCODE()
  - FORMAT()
  - QUOTE\_NULLABLE()
  - REGEXP\_MATCHES()
  - REGEXP\_SPLIT\_TO\_ARRAY()
  - REGEXP\_SPLIT\_TO\_TABLE()

- System catalog information functions
- System information functions

  - CURRENT\_CATALOG CURRENT\_QUERY()
  - INET\_CLIENT\_ADDR()
  - INET\_CLIENT\_PORT()
  - INET\_SERVER\_ADDR() INET\_SERVER\_PORT()
  - PG\_CONF\_LOAD\_TIME()
  - PG\_IS\_OTHER\_TEMP\_SCHEMA()
  - PG\_LISTENING\_CHANNELS()
  - PG\_MY\_TEMP\_SCHEMA()
  - PG\_POSTMASTER\_START\_TIME()
  - PG\_TRIGGER\_DEPTH()
  - SHOW VERSION()

- Text search functions and operators
- Transaction IDs and snapshots functions
- Trigger functions
- XML functions
