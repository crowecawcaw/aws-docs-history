Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Data type differences between Amazon Redshift and supported PostgreSQL and MySQL databases

The following table shows the mapping of an Amazon Redshift data type to a corresponding Amazon RDS PostgreSQL or Aurora PostgreSQL data type.

| Amazon Redshift data type | RDS PostgreSQL or Aurora PostgreSQL data type | Description                                                |
| ------------------------- | --------------------------------------------- | ---------------------------------------------------------- |
| SMALLINT                  | SMALLINT                                      | Signed two-byte integer                                    |
| INTEGER                   | INTEGER                                       | Signed four-byte integer                                   |
| BIGINT                    | BIGINT                                        | Signed eight-byte integer                                  |
| DECIMAL                   | DECIMAL                                       | Exact numeric of selectable precision                      |
| REAL                      | REAL                                          | Single precision floating-point number                     |
| DOUBLE PRECISION          | DOUBLE PRECISION                              | Double precision floating-point number                     |
| BOOLEAN                   | BOOLEAN                                       | Logical Boolean (true/false)                               |
| CHAR                      | CHAR                                          | Fixed-length character string                              |
| VARCHAR                   | VARCHAR                                       | Variable-length character string with a user-defined limit |
| DATE                      | DATE                                          | Calendar date (year, month, day)                           |
| TIMESTAMP                 | TIMESTAMP                                     | Date and time (without time zone)                          |
| TIMESTAMPTZ               | TIMESTAMPTZ                                   | Date and time (with time zone)                             |
| GEOMETRY                  | PostGIS GEOMETRY                              | Spatial data                                               |

The following RDS PostgreSQL and Aurora PostgreSQL data types are converted to VARCHAR(64K) in
Amazon Redshift:

- JSON, JSONB
- Arrays
- BIT, BIT VARYING
- BYTEA
- Composite types
- Date and time types INTERVAL, TIME, TIME WITH TIMEZONE
- Enumerated types
- Monetary types
- Network address types
- Numeric types SERIAL, BIGSERIAL, SMALLSERIAL, and MONEY
- Object identifier types
- pg_lsn type
- Pseudotypes
- Range types
- Text search types
- TXID_SNAPSHOT
- UUID
- XML type
  The following table shows the mapping of an Amazon Redshift data type to a corresponding Amazon RDS MySQL or Aurora MySQL data type.

| Amazon Redshift data type | RDS MySQL or Aurora MySQL data type | Description                                                |
| ------------------------- | ----------------------------------- | ---------------------------------------------------------- |
| BOOLEAN                   | TINYINT(1)                          | Logical Boolean (true or false)                            |
| SMALLINT                  | TINYINT(UNSIGNED)                   | Signed two-byte integer                                    |
| SMALLINT                  | SMALLINT                            | Signed two-byte integer                                    |
| INTEGER                   | SMALLINT UNSIGNED                   | Signed four-byte integer                                   |
| INTEGER                   | MEDIUMINT (UNSIGNED)                | Signed four-byte integer                                   |
| INTEGER                   | INT                                 | Signed four-byte integer                                   |
| BIGINT                    | INT UNSIGNED                        | Signed eight-byte integer                                  |
| BIGINT                    | BIGINT                              | Signed eight-byte integer                                  |
| DECIMAL                   | BIGINT UNSIGNED                     | Exact numeric of selectable precision                      |
| DECIMAL                   | DECIMAL(M,D)                        | Exact numeric of selectable precision                      |
| REAL                      | FLOAT                               | Single precision floating-point number                     |
| DOUBLE PRECISION          | DOUBLE                              | Double precision floating-point number                     |
| CHAR                      | CHAR                                | Fixed-length character string                              |
| VARCHAR                   | VARCHAR                             | Variable-length character string with a user-defined limit |
| DATE                      | DATE                                | Calendar date (year, month, day)                           |
| TIME                      | TIME                                | Time (without time zone)                                   |
| TIMESTAMP                 | TIMESTAMP                           | Date and time (without time zone)                          |
| TIMESTAMP                 | DATETIME                            | Time (without time zone)                                   |
| VARCHAR(4)                | YEAR                                | Variable length character representing year                |

An error results when TIME data is out of range (00:00:00 – 24:00:00).

The following RDS MySQL and Aurora MySQL data types are converted to VARCHAR(64K) in
Amazon Redshift:

- BIT
- BINARY
- VARBINARY
- TINYBLOB, BLOB, MEDIUMBLOB, LONGBLOB
- TINYTEXT, TEXT, MEDIUMTEXT, LONGTEXT
- ENUM
- SET
- SPATIAL
