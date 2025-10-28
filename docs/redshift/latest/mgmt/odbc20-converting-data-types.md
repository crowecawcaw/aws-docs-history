Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data types conversions

The Amazon Redshift ODBC driver version 2.x supports many common data formats, converting
between Amazon Redshift and SQL data types.

The following table lists the supported data type mappings.

| Amazon Redshift type | SQL type             |
| -------------------- | -------------------- |
| BIGINT               | SQL_BIGINT           |
| BOOLEAN              | SQL_BIT              |
| CHAR                 | SQL_CHAR             |
| DATE                 | SQL_TYPE_DATE        |
| DECIMAL              | SQL_NUMERIC          |
| DOUBLE PRECISION     | SQL_DOUBLE           |
| GEOGRAPHY            | SQL\_ LONGVARBINARY  |
| GEOMETRY             | SQL\_ LONGVARBINARY  |
| INTEGER              | SQL_INTEGER          |
| REAL                 | SQL_REAL             |
| SMALLINT             | SQL_SMALLINT         |
| SUPER                | SQL_LONGVARCHAR      |
| TEXT                 | SQL_LONGVARCHAR      |
| TIME                 | SQL_TYPE_TIME        |
| TIMETZ               | SQL_TYPE_TIME        |
| TIMESTAMP            | SQL_TYPE\_ TIMESTAMP |
| TIMESTAMPTZ          | SQL_TYPE\_ TIMESTAMP |
| VARBYTE              | SQL_LONGVARBINARY    |
| VARCHAR              | SQL_VARCHAR          |
