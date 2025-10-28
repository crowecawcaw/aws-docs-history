Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations for data sharing

reads and writes in Amazon Redshift

###### Note

Amazon Redshift multi-warehouse writes using data sharing is only supported on Amazon Redshift
patch 186 for provisioned clusters on current track version 1.0.78881 or greater, and
for Amazon Redshift Serverless workgroups on version 1.0.78890 or greater.

The following are considerations when working with datashare reads and writes in
Amazon Redshift:

- You can only share SQL UDFs through datashares. Python and Lambda UDFs
  aren't supported.
- If the producer database has specific collation, use the same collation
  settings for the consumer database.
- Amazon Redshift doesn't support nested SQL user-defined functions on producer
  clusters.
- Amazon Redshift doesn't support sharing tables with interleaved sort keys and
  views that refer to tables with interleaved sort keys.
- Amazon Redshift doesn't support accessing a datashare object which had a
  concurrent DDL occur between the Prepare and Execute of the access.
- Amazon Redshift doesn't support sharing stored procedures through
  datashares.
- Amazon Redshift doesn't support sharing metadata system views and system
  tables.
- _Compute type_ – You must use Serverless workgroups,
  ra3.large clusters, ra3.xlplus clusters, ra3.4xl clusters, or ra3.16xl clusters to use this feature.
- _Isolation level_ – Your database’s isolation level
  must be snapshot isolation in order to allow other Serverless workgroups and
  provisioned clusters to write to it.
- _Multi-statement queries and transactions_ –
  Multi-statement queries outside of a transaction block aren't currently supported.
  As a result, if you are using a query editor like dbeaver and you have multiple
  write queries, you need to wrap your queries in an explicit BEGIN...END
  transaction statement.

When multi-command statements are used outside of transactions, if the first
command is a write to a producer database, subsequent write commands in the
statement are only allowed to that producer database. If the first command is a
read, subsequent write commands are only allowed to the used database, if set,
otherwise to the local database. Note that the writes in a transaction are only
supported to a single database.

- _Consumer sizing_ – Consumer clusters must have at
  least 64 slices or more to perform writes using data sharing.
- _Views and materialized views_ – You can't create,
  update, or alter views or materialized views on a datashare database.
- _Security_ – You can't attach or remove security
  policies such as column-level (CLS), row-level (RLS) and dynamic data masking
  (DDM) to datashare objects.
- _Manageability_ – Consumers warehouses can't add
  datashare objects or views referencing datashare objects to another datashare.
  Consumers also can't modify or drop an existing datashare.
- _Truncate operations_ – Datashare writes support
  transactional truncates for remote tables. This is different than truncates that
  you run locally on a cluster, which are auto-commit. For more information about
  the SQL command, see [TRUNCATE](r_TRUNCATE.md "r_TRUNCATE.md").
- _Cloning_ – CREATE TABLE with LIKE clause statements
  support cloning from a single parent table when you write from consumer warehouses
  to producers.
