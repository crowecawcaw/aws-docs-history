Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data type conversions

The Amazon Redshift JDBC driver version 2.x supports many common data formats, converting
between Amazon Redshift, SQL, and Java data types.

The following table lists the supported data type mappings.

| Amazon Redshift type | SQL type             | Java type          |
| -------------------- | -------------------- | ------------------ |
| BIGINT               | SQL_BIGINT           | Long               |
| BOOLEAN              | SQL_BIT              | Boolean            |
| CHAR                 | SQL_CHAR             | String             |
| DATE                 | SQL_TYPE_DATE        | java.sql.Date      |
| DECIMAL              | SQL_NUMERIC          | BigDecimal         |
| DOUBLE PRECISION     | SQL_DOUBLE           | Double             |
| GEOMETRY             | SQL\_ LONGVARBINARY  | byte[]             |
| INTEGER              | SQL_INTEGER          | Integer            |
| OID                  | SQL_BIGINT           | Long               |
| SUPER                | SQL_LONGVARCHAR      | String             |
| REAL                 | SQL_REAL             | Float              |
| SMALLINT             | SQL_SMALLINT         | Short              |
| TEXT                 | SQL_VARCHAR          | String             |
| TIME                 | SQL_TYPE_TIME        | java.sql.Time      |
| TIMETZ               | SQL_TYPE_TIME        | java.sql.Time      |
| TIMESTAMP            | SQL_TYPE\_ TIMESTAMP | java.sql.Timestamp |
| TIMESTAMPTZ          | SQL_TYPE\_ TIMESTAMP | java.sql.Timestamp |
| VARCHAR              | SQL_VARCHAR          | String             |
