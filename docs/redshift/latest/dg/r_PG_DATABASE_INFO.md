Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_DATABASE_INFO

PG_DATABASE_INFO is an Amazon Redshift system view that extends the PostgreSQL catalog table PG_DATABASE.

PG_DATABASE_INFO is visible to all users.

## Table columns

PG_DATABASE_INFO contains the following columns in addition to columns in PG_DATABASE. The `oid` column in PG_DATABASE is called `datid` in the PG_DATABASE_INFO table. For more information, see the
[PostgreSQL documentation](https://www.postgresql.org/docs/8.0/catalog-pg-database.html "https://www.postgresql.org/docs/8.0/catalog-pg-database.html").

| Column name  | Data type | Description                                                                                                   |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------- |
| datid        | oid       | The object identifier (OID) used internally by system tables.                                                 |
| datconnlimit | text      | The maximum number of concurrent connections that can be made to this database. A value of -1 means no limit. |
