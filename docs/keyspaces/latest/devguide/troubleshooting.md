# Troubleshooting data definition language errors in Amazon Keyspaces

Having trouble creating resources? Here are some common issues and how to resolve them.

## Data definition language errors

Amazon Keyspaces performs data definition language (DDL) operations asynchronously—for
example, creating and deleting keyspaces and tables. If an application is trying to use the
resource before it's ready, the operation fails.

You can monitor the creation status of new keyspaces and tables in the AWS Management Console, which
indicates when a keyspace or table is pending or active. You can also monitor the creation
status of a new keyspace or table programmatically by querying the system schema table. A
keyspace or table becomes visible in the system schema when it's ready for use.

###### Note

To optimize the creation of keyspaces using CloudFormation, you can use this utility to convert
CQL scripts into CloudFormation templates. The tool is available from the [GitHub repository](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter "https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter").

###### Topics

- [Keyspace creation errors](#troubleshooting.cql.keyspace "#troubleshooting.cql.keyspace")
- [Table creation errors](#troubleshooting.cql.table "#troubleshooting.cql.table")
- [I'm trying to restore a table using Amazon Keyspaces
  point-in-time recovery (PITR), but the restore fails](#troubleshooting.cql.pitr "#troubleshooting.cql.pitr")
- [I'm trying to use INSERT/UPDATE to edit custom
  Time to Live (TTL) settings, but the operation
  fails](#troubleshooting.cql.ttl "#troubleshooting.cql.ttl")
- [Columns exceeded](#troubleshooting.cql.upload "#troubleshooting.cql.upload")
- [Range delete error](#troubleshooting.cql.rangedelete "#troubleshooting.cql.rangedelete")

### I created a new keyspace, but I can't

view or access it

**You're receiving errors from your application that is trying to
access a new keyspace.**

If you try to access a newly created Amazon Keyspaces keyspace that is still being created
asynchronously, you will get an error. The following error is an example.

```
InvalidRequest: Error from server: code=2200 [Invalid query] message="unconfigured keyspace mykeyspace"
```

The recommended design pattern to check when a new keyspace is ready for use
is to poll the Amazon Keyspaces system schema tables (system_schema_mcs.\*).

For more information, see [Check keyspace creation status in Amazon Keyspaces](keyspaces-create.md "keyspaces-create.md").

### I created a new table, but I can't view or

access it

**You're receiving errors from your application that is trying to
access a new table.**

If you try to access a newly created Amazon Keyspaces table that is still being created
asynchronously, you will get an error. For example, trying to query a table that isn't
available yet fails with an `unconfigured table` error.

```
InvalidRequest: Error from server: code=2200 [Invalid query] message="unconfigured table mykeyspace.mytable"
```

Trying to view the table with `sync_table()` fails with a `KeyError`.

```
KeyError: 'mytable'
```

The recommended design pattern to check when a new table is ready for use
is to poll the Amazon Keyspaces system schema tables (system_schema_mcs.\*).

This is the example output for a table that is being created.

```
`user-at-123@cqlsh:system_schema_mcs> select table_name,status from system_schema_mcs.tables where keyspace_name='example_keyspace' and table_name='example_table';

table_name | status

------------+----------

example_table | CREATING

(1 rows)`
```

This is the example output for a table that is active.

```
`user-at-123@cqlsh:system_schema_mcs> select table_name,status from system_schema_mcs.tables where keyspace_name='example_keyspace' and table_name='example_table';

table_name | status

------------+----------

example_table | ACTIVE

(1 rows)`
```

For more information, see [Check table creation status in Amazon Keyspaces](tables-create.md "tables-create.md").

### I'm trying to restore a table using Amazon Keyspaces

point-in-time recovery (PITR), but the restore fails

If you're trying to restore an Amazon Keyspaces table with point-in-time recovery (PITR), and
you see the restore process begin but not complete successfully, you might not have
configured all of the required permissions that are needed by the restore process
for this particular table.

In addition to user permissions, Amazon Keyspaces might require permissions to perform
actions during the restore process on your principal's behalf. This is the case if
the table is encrypted with a customer managed key, or if you're using IAM
policies that restrict incoming traffic.

For example, if you're using condition keys in your IAM policy to restrict
source traffic to specific endpoints or IP ranges, the restore operation fails. To
allow Amazon Keyspaces to perform the table restore operation on your principal's behalf, you
must add an `aws:ViaAWSService` global condition key in the IAM
policy.

For more information about permissions to restore tables, see [Configure restore table IAM permissions for Amazon Keyspaces PITR](howitworks_restore_permissions.md "howitworks_restore_permissions.md").

### I'm trying to use INSERT/UPDATE to edit custom

Time to Live (TTL) settings, but the operation
fails

If you're trying to insert or update a custom TTL value, the operation might fail with the following error.

```
`TTL is not yet supported.`
```

To specify custom TTL values for rows or columns by using `INSERT` or
`UPDATE` operations, you must first enable TTL for the table. You can
enable TTL for a table using the `ttl` custom property.

For more information about enabling custom TTL settings for tables, see [Update table with custom Time to Live (TTL)](TTL-how-to-enable-custom-alter.md "TTL-how-to-enable-custom-alter.md").

### I'm trying to upload data to my Amazon Keyspaces table

and I get an error about exceeding the number of columns

**You're uploading data and have exceeded the number of columns
that can be updated simultaneously.**

This error occurs when your table schema exceeds the maximum size of 350 KB. For more
information, see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

### I'm trying to delete data in my Amazon Keyspaces

table and the deletion fails for the range

**You're trying to delete data by partition key and receive a
range delete error.**

This error occurs when you're trying to delete more than 1,000 rows in one delete
operation.

```
`Range delete requests are limited by the amount of items that can be deleted in a single range.`
```

For more information, see [Range delete](functional-differences.md#functional-differences.range-delete "functional-differences.md#functional-differences.range-delete").

To delete more than 1,000 rows within a single partition, consider the following options.

- Delete by partition – If the majority of partitions are under 1,000
  rows, you can attempt to delete data by partition. If the partitions contain
  more than 1,000 rows, attempt to delete by the clustering column instead.
- Delete by clustering column – If your model contains multiple clustering
  columns, you can use the column hierarchy to delete multiple rows. Clustering
  columns are a nested structure, and you can delete many rows by operating
  against the top-level column.
- Delete by individual row – You can iterate through the rows and delete each row by its
  full primary key (partition columns and clustering columns).
- As a best practice, consider splitting your rows across partitions – In Amazon Keyspaces, we
  recommend that you distribute your throughput across table partitions. This
  distributes data and access evenly across physical resources, which provides the
  best throughput. For more information, see [Data modeling best practices: recommendations for designing data models](data-modeling.md "data-modeling.md").

Consider also the following recommendations when you're planning delete operations for
heavy workloads.

- With Amazon Keyspaces, partitions can contain a virtually unbounded number of rows. This allows you to
  scale partitions “wider” than the traditional Cassandra guidance of 100 MB. It’s
  not uncommon for time series or ledgers to grow over a gigabyte of data over
  time.
- With Amazon Keyspaces, there are no compaction strategies or tombstones to consider when you have to
  perform delete operations for heavy workloads. You can delete as much data as
  you want without impacting read performance.
