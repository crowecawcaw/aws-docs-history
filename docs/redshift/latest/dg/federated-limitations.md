Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when accessing federated data with Amazon Redshift

Some Amazon Redshift features don't support access to federated data. You can find related
limitations and considerations following.

The following are limitations and considerations when using federated queries with
Amazon Redshift:

- Federated queries support read access to external data sources. You can't write or create
  database objects in the external data source.
- In some cases, you might access an Amazon RDS or Aurora DB cluster database in a different AWS Region than
  Amazon Redshift. In these cases, you typically incur network latency and billing charges for
  transferring data across AWS Regions. We recommend using an Aurora global database
  with a local endpoint in the same AWS Region as your Amazon Redshift cluster. Aurora global
  databases use dedicated infrastructure for storage-based replication across any two
  AWS Regions with typical latency of less than 1 second.
- Consider the cost of accessing Amazon RDS or Aurora DB cluster. For example, when using this feature to access
  Aurora DB cluster, Aurora DB cluster charges are based on IOPS.
- Federated queries don't enable access to Amazon Redshift from RDS or Aurora DB cluster.
- Federated queries are only available in AWS Regions where both Amazon Redshift and Amazon RDS or Aurora DB cluster are
  available.
- Federated queries currently don't support `ALTER SCHEMA`. To change a schema, use
  `DROP` and then `CREATE EXTERNAL SCHEMA`.
- Federated queries don't work with concurrency scaling.
- Federated queries currently don't support access through a PostgreSQL foreign data wrapper.
- Federated queries to RDS MySQL or Aurora MySQL support transaction isolation at the READ
  COMMITTED level.
- If not specified, Amazon Redshift connects to RDS for MySQL or Aurora MySQL on port 3306. Confirm the MySQL port number before creating an
  external schema for MySQL.
- If not specified, Amazon Redshift connects to RDS PostgreSQL or Aurora PostgreSQL on port 5432. Confirm the PostgreSQL port number before creating an
  external schema for PostgreSQL.
- When fetching TIMESTAMP and DATE data types from MySQL, zero values are treated as NULL.
- If an Aurora DB cluster database reader endpoint is used, an "invalid snapshot" error can occur. This can be avoided by one of the following methods:

      + Use a specific Aurora DB cluster instance endpoint (instead of using the Aurora DB cluster cluster endpoint). This method uses REPEATABLE READ transaction isolation for the results from the PostgreSQL database.
      + Use an Aurora DB cluster reader endpoint and set `pg_federation_repeatable_read` to false for the session. This method uses READ COMMITTED transaction isolation for the results from the PostgreSQL database.
       For more information about Aurora DB cluster reader endpoints, see
       [Types of Aurora DB cluster endpoints](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md#Aurora.Overview.Endpoints.Types "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md#Aurora.Overview.Endpoints.Types")
       in the *Amazon Aurora User Guide*.
       For information about `pg_federation_repeatable_read`, see
       [pg\_federation\_repeatable\_read](r_pg_federation_repeatable_read.md "r_pg_federation_repeatable_read.md").

  The following are considerations for transactions when working with federated queries to
  PostgreSQL databases:

- If a query consists of federated tables, the leader node starts a READ ONLY
  REPEATABLE READ transaction on the remote database. This transaction remains for the
  duration of the Amazon Redshift transaction.
- The leader node creates a snapshot of the remote database by calling
  `pg_export_snapshot` and makes a read lock on the affected
  tables.
- A compute node starts a transaction and uses the snapshot created at the leader node to issue queries to the remote database.

## Supported versions of federated databases

An Amazon Redshift external schema can reference a database in an external RDS PostgreSQL or
Aurora PostgreSQL. When it does, these limitations apply:

- When creating an external schema referencing Aurora DB cluster, the Aurora PostgreSQL database must be at
  version 9.6, or later.
- When creating an external schema referencing Amazon RDS, the Amazon RDS PostgreSQL database must be at
  version 9.6, or later.

An Amazon Redshift external schema can reference a database in an external RDS MySQL or
Aurora MySQL. When it does, these limitations apply:

- When creating an external schema referencing Aurora DB cluster, the Aurora MySQL database must be at version
  5.6 or later.
- When creating an external schema referencing Amazon RDS, the RDS MySQL database must be at version
  5.6 or later.
