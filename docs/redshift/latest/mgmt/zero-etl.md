Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Considerations when using zero-ETL integrations with Amazon Redshift

The following considerations apply to zero-ETL integrations with Amazon Redshift.

- Your target Amazon Redshift data warehouse must meet the following prerequisites:
  - Running Amazon Redshift Serverless or an RA3 node type.
  - Encrypted (if using a provisioned cluster).
  - Has case sensitivity enabled.

- If you delete a source that is an authorized integration source for an Amazon Redshift data
  warehouse, all associated integrations will go into the `FAILED` state. Any
  previously replicated data remains in your Amazon Redshift database and can be queried.
- The destination database is read-only. You can't create tables, views, or
  materialized views in the destination database. However, you can use materialized views on
  other tables in the target data warehouse.
- Materialized views are supported when used in cross-database queries. For information
  about creating materialized views with data replicated through zero-ETL integrations, see [Querying replicated data with materialized
  views](zero-etl-using.md#zero-etl-using.transforming "zero-etl-using.md#zero-etl-using.transforming").
- By default, you can query tables only in the target data warehouse that are in the
  `Synced` state. To query tables in another state, set the database parameter
  `QUERY_ALL_STATES` to `TRUE`. For information about setting
  `QUERY_ALL_STATES`, see [CREATE DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER
  DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the _Amazon Redshift Database Developer Guide_. For more information about
  the state of your database, see [SVV_INTEGRATION_TABLE_STATE](../dg/r_SVV_INTEGRATION_TABLE_STATE.md "../dg/r_SVV_INTEGRATION_TABLE_STATE.md") in the _Amazon Redshift Database Developer Guide_.
- Amazon Redshift accepts only UTF-8 characters, so it might not honor the collation defined in
  your source. The sorting and comparison rules might be different, which can ultimately
  change the query results.
- Zero-ETL integrations is limited to 50 per Amazon Redshift data warehouse target.
- Tables in the integration source must have a primary key. Otherwise, your tables can't
  be replicated to the target data warehouse in Amazon Redshift.

For information about how to add a primary key to Amazon Aurora PostgreSQL, see [Handle tables without primary keys while creating Amazon Aurora PostgreSQL zero-ETL integrations with
Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_. For information about how
to add a primary key to Amazon Aurora MySQL or RDS for MySQL, see [Handle tables without primary keys while creating Amazon Aurora MySQL or Amazon RDS for MySQL
zero-ETL integrations with Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_.

- You can use data filtering for Aurora zero-ETL integrations to define the scope of replication
  from the source Aurora DB cluster to the target Amazon Redshift data warehouse. Rather than
  replicating all data to the target, you can define one or more filters that selectively
  include or exclude certain tables from being replicated. For more information, see [Data
  filtering for Aurora zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") in the
  _Amazon Aurora User Guide_.
- For Aurora PostgreSQL zero-ETL integrations with Amazon Redshift, Amazon Redshift supports a maximum of 100 databases from
  Aurora PostgreSQL. Each database replicates from source to target independently.
- Zero-ETL integration does not support transformations while replicating the data from
  transactional data stores to Amazon Redshift. Data is replicated as-is from the source data base.
  However, you can apply transformations on the replicated data in Amazon Redshift.
- Zero-ETL integration runs in Amazon Redshift using parallel connections. It runs using the credentials of
  the user who created the database from the integration. When the query runs, concurrency
  scaling does not kick in for these connections during the sync (writes). Concurrency
  scaling reads (from Amazon Redshift clients) works for synced objects.
- You can set the `REFRESH_INTERVAL` for a zero-ETL integration to control the
  frequency of data replication into Amazon Redshift. For more information, see [CREATE
  DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
  _Amazon Redshift Database Developer Guide_.
- After you create an Amazon Redshift database from a zero-ETL integration with Amazon DynamoDB, the database state
  should change from **Creating** to **Active**. This starts the replication of data in the source DynamoDB tables to
  the target Redshift tables, which are created under the public schema of the destination
  database (`ddb_rs_customerprofiles_zetl_db`).

## Considerations when using history

mode on the target

The following considerations apply when using history mode on the target database. For
more information, see [History mode](zero-etl-history-mode.md "zero-etl-history-mode.md").

- When you drop a table on a source, the table on the target is not dropped, but is
  changed to `DroppedSource` state. You can drop or rename the table from the
  Amazon Redshift database.
- When you truncate a table on a source, deletes are run on the target table. For
  example, if all records are truncated on the source, corresponding records on the target
  column `_record_is_active` are changed to `false`.
- When you run TRUNCATE table SQL on the target table, active history rows are marked
  inactive with a corresponding timestamp.
- When a row in a table is set to inactive, it can be deleted after a short (about 10
  minute) delay. To delete inactive rows, connect to your zero-ETL database with query editor v2 or
  another SQL client.
- You can only delete inactive rows from a table with history mode on. For example, a
  SQL command similar to the following only deletes inactive rows.

```
delete from schema.user_table where _record_delete_time <= '2024-09-10 12:34:56'
```

This is equivalent to a SQL command like the following.

```
delete from schema.user_table where _record_delete_time <= '2024-09-10 12:34:56' and _record_is_active = False
```

- When turning history mode off for a table, all historical data is saved to table
  named with `<schema>.<table-name>_historical_<timestamp>`
  while the original table named `<schema>.<table-name>` is
  refreshed.
- When a table with history mode on is excluded from replication using a table filter,
  all rows are set as inactive and it is changed to `DroppedSource` state. For
  more information about table filters, see [Data filtering for
  Aurora zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") in the
  _Amazon Aurora User Guide_.
- History mode can only be switched to `true` or `false` for
  tables in `Synced` state.
- Materialized views for tables with history mode on are created as full recompute.

## Considerations when the zero-ETL integration

source is Aurora or Amazon RDS

The following considerations apply to Aurora and Amazon RDS zero-ETL integrations with Amazon Redshift.

- You can use data filtering for Aurora and RDS for MySQL zero-ETL integrations to define the scope
  of replication from the source DB cluster to the target Amazon Redshift data warehouse. Rather than
  replicating all data to the target, you can define one or more filters that selectively
  include or exclude certain tables from being replicated. For more information, see
  [Data filtering for
  Aurora zero-ETL integrations with Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md") in the
  _Amazon Aurora User Guide_.
- Tables in the integration source must have a primary key. Otherwise, your tables
  can't be replicated to the target data warehouse in Amazon Redshift.

For information about how to add a primary key to Amazon Aurora PostgreSQL, see [Handle tables without primary keys while creating Amazon Aurora PostgreSQL zero-ETL integrations with
Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-postgresql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_. For information about
how to add a primary key to Amazon Aurora MySQL or RDS for MySQL, see [Handle tables without primary keys while creating Amazon Aurora MySQL or Amazon RDS for MySQL
zero-ETL integrations with Amazon Redshift](https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/ "https://aws.amazon.com/blogs/database/handle-tables-without-primary-keys-while-creating-amazon-aurora-mysql-or-amazon-rds-for-mysql-zero-etl-integrations-with-amazon-redshift/") in the _AWS Database Blog_.

- The maximum length of an Amazon Redshift VARCHAR data type is 65,535 bytes. When the content
  from the source does not fit into this limit, replication does not proceed and the table
  is put into a failed state. You can set the database parameter
  `TRUNCATECOLUMNS` to `TRUE` to truncate content to fit in the
  column. For information about setting `TRUNCATECOLUMNS`, see [CREATE
  DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
  _Amazon Redshift Database Developer Guide_.

For more information about data type differences between zero-ETL integration sources and Amazon Redshift
databases, see [Data type differences between Aurora and Amazon Redshift](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.data-type-mapping") in the
_Amazon Aurora User Guide_.

For Aurora sources, also see [Limitations](../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.reqs-lims "../../../AmazonRDS/latest/AuroraUserGuide/zero-etl.md#zero-etl.reqs-lims") in the _Amazon Aurora User Guide_.

For Amazon RDS sources, also see [Limitations](../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.reqs-lims "../../../AmazonRDS/latest/UserGuide/zero-etl.md#zero-etl.reqs-lims") in
the _Amazon RDS User Guide_.

## Considerations when the zero-ETL integration source is

DynamoDB

The following considerations apply to DynamoDB zero-ETL integrations with Amazon Redshift.

- Table names from DynamoDB greater than 127 characters are not supported.
- The data from a DynamoDB zero-ETL integration maps to a SUPER data type column in Amazon Redshift.
- Column names for the partition key or sort key greater than 127 characters are not
  supported.
- A zero-ETL integration from DynamoDB can map to only one Amazon Redshift database.
- For partition and sort keys, the precision and scale maximum is (38,18). Numeric
  data types on DynamoDB support a maximum precision up to 38. Amazon Redshift also supports a maximum
  precision of 38, but the default decimal precision/scale on Amazon Redshift is (38,10). That means
  values scale values can be truncated.
- For a successful zero-ETL integration, an individual attribute (consisting of name+value) in a
  DynamoDB item, must not be larger than 64 KB.
- On activation, the zero-ETL integration exports the full DynamoDB table to populate the Amazon Redshift
  database. The time it takes for this initial process to complete depends on the DynamoDB
  table size. The zero-ETL integration then incrementally replicates updates from DynamoDB to Amazon Redshift
  using DynamoDB incremental exports. This means the replicated DynamoDB data in Amazon Redshift is kept
  up-to-date automatically.

Currently, the minimum latency for DynamoDB zero-ETL integration is 15 minutes. You can increase
it further by setting a non-zero `REFRESH_INTERVAL` for a zero-ETL integration. For
more information, see [CREATE DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER
DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the _Amazon Redshift Database Developer Guide_.

For Amazon DynamoDB sources, also see [Prerequisites and limitations](../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs "../../../amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.md#RedshiftforDynamoDB-zero-etl-prereqs") in the _Amazon DynamoDB Developer Guide_.

## Considerations when the zero-ETL integration source is

applications, such as, Salesforce, SAP, ServiceNow, and Zendesk

The following considerations apply to source is applications, such as, Salesforce, SAP,
ServiceNow, and Zendesk with Amazon Redshift.

- Table names and column names from application sources greater than 127 characters
  are not supported.
- The maximum length of an Amazon Redshift VARCHAR data type is 65,535 bytes. When the content
  from the source does not fit into this limit, replication does not proceed and the table
  is put into a failed state. You can set the database parameter
  `TRUNCATECOLUMNS` to `TRUE` to truncate content to fit in the
  column. For information about setting `TRUNCATECOLUMNS` see [CREATE
  DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the
  _Amazon Redshift Database Developer Guide_.

For more information about data type differences between zero-ETL integration application
sources and Amazon Redshift databases, see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the
_AWS Glue Developer Guide_.

- The minimum latency for a zero-ETL integration with applications is 1 hour. You can increase
  it further by setting a non-zero `REFRESH_INTERVAL` for a zero-ETL integration. For
  more information, see [CREATE DATABASE](../dg/r_CREATE_DATABASE.md "../dg/r_CREATE_DATABASE.md") and [ALTER
  DATABASE](../dg/r_ALTER_DATABASE.md "../dg/r_ALTER_DATABASE.md") in the _Amazon Redshift Database Developer Guide_.

For sources of zero-ETL integrations with applications, also see [Zero-ETL integrations](../../../glue/latest/dg/zero-etl-using.md "../../../glue/latest/dg/zero-etl-using.md") in the
_AWS Glue Developer Guide_.
