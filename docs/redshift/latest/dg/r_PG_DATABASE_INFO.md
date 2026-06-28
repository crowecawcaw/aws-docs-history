Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG\_DATABASE\_INFO

PG\_DATABASE\_INFO is an Amazon Redshift system view that extends the PostgreSQL catalog table PG\_DATABASE.

PG\_DATABASE\_INFO is visible to all users.

## Table columns

PG\_DATABASE\_INFO contains the following columns in addition to columns in PG\_DATABASE. The `oid` column in PG\_DATABASE is called `datid` in the PG\_DATABASE\_INFO table. For more information, see the
[PostgreSQL documentation](https://www.postgresql.org/docs/8.0/catalog-pg-database.html "https://www.postgresql.org/docs/8.0/catalog-pg-database.html").

| Column name  | Data type | Description                                                                                                   |
| ------------ | --------- | ------------------------------------------------------------------------------------------------------------- |
| datid        | oid       | The object identifier (OID) used internally by system tables.                                                 |
| datconnlimit | text      | The maximum number of concurrent connections that can be made to this database. A value of -1 means no limit. |
