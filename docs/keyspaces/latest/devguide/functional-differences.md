# Functional differences: Amazon Keyspaces vs. Apache Cassandra

The following are the functional differences between Amazon Keyspaces and Apache Cassandra.

###### Topics

- [Apache Cassandra APIs, operations,
  and data types](#functional-differences.cassandra-apis "#functional-differences.cassandra-apis")
- [Asynchronous creation
  and deletion of keyspaces and tables](#functional-differences.table-keyspace-management "#functional-differences.table-keyspace-management")
- [Authentication and authorization](#functional-differences.auth "#functional-differences.auth")
- [Batch](#functional-differences.batch "#functional-differences.batch")
- [Change data capture (CDC)](#functional-differences.cdc "#functional-differences.cdc")
- [Cluster configuration](#functional-differences.cluster-config "#functional-differences.cluster-config")
- [Connections](#functional-differences.connections "#functional-differences.connections")
- [IN keyword](#functional-differences.IN-keyword "#functional-differences.IN-keyword")
- [FROZEN
  collections](#functional-differences.frozen-collections "#functional-differences.frozen-collections")
- [Lightweight
  transactions](#functional-differences.light-transactions "#functional-differences.light-transactions")
- [Load balancing](#functional-differences.load-balancing "#functional-differences.load-balancing")
- [Pagination](#functional-differences.paging "#functional-differences.paging")
- [Partitioners](#functional-differences.partitioners "#functional-differences.partitioners")
- [Prepared statements](#functional-differences.prepared-statements "#functional-differences.prepared-statements")
- [Range delete](#functional-differences.range-delete "#functional-differences.range-delete")
- [System tables](#functional-differences.system-tables "#functional-differences.system-tables")
- [Timestamps](#functional-differences.timestamps "#functional-differences.timestamps")
- [User-defined types (UDTs)](#functional-differences.UDTs "#functional-differences.UDTs")

## Apache Cassandra APIs, operations,

and data types

Amazon Keyspaces supports all commonly used Cassandra data-plane operations, such as creating
keyspaces and tables, reading data, and writing data. To see what is currently supported,
see [Supported Cassandra APIs, operations, functions, and data
types](cassandra-apis.md "cassandra-apis.md").

## Asynchronous creation

and deletion of keyspaces and tables

Amazon Keyspaces performs data definition language (DDL) operations, such as creating and deleting
keyspaces , tables, and types asynchronously. To learn how to monitor the creation status
of resources, see [Check keyspace creation status in Amazon Keyspaces](keyspaces-create.md "keyspaces-create.md") and [Check table creation status in Amazon Keyspaces](tables-create.md "tables-create.md").
For a list of DDL statements in the CQL language reference, see [DDL statements (data definition language) in Amazon Keyspaces](cql.md "cql.md").

## Authentication and authorization

Amazon Keyspaces (for Apache Cassandra) uses AWS Identity and Access Management (IAM)
for user authentication and authorization, and supports the equivalent authorization
policies as Apache Cassandra. As such, Amazon Keyspaces does not support Apache Cassandra's
security configuration commands.

## Batch

Amazon Keyspaces supports unlogged batch commands with up to 30 commands in the batch. Only
unconditional **INSERT**, **UPDATE**, or
**DELETE** commands are permitted in a batch. Logged batches are not
supported.

## Change data capture (CDC)

In Apache Cassandra, change data capture (CDC) copies commit log segments
that capture table updates to a specified directory on the node. Each change record in the CDC log can include updates across multiple
keyspaces and tables. When a row is updated
or deleted, the Apache Cassandra CDC log shows only the modified columns. The log doesn't include the previous state of the data before the change.
To understand the full details of the data modifications, you need to deserialize these logs using specific Cassandra tools.

With Amazon Keyspaces CDC streams, you can select the type
of information that the CDC stream collects for each row. By default, Amazon Keyspaces CDC streams capture the version of the row before and after
the change occurred. Amazon Keyspaces CDC provides de-duplicated and ordered change records at the table level.

In Amazon Keyspaces, each CDC stream is an AWS resource with an Amazon Resource Name (ARN) and
your application can consume Amazon Keyspaces CDC streams using the Amazon Keyspaces CDC API using one of the
available [endpoints](CDC_access-endpoints.md "CDC_access-endpoints.md").

For more information about Amazon Keyspaces CDC, see [Working with change data capture (CDC) streams in Amazon Keyspaces](cdc.md "cdc.md").

## Cluster configuration

Amazon Keyspaces is serverless, so there are no clusters, hosts, or Java virtual machines
(JVMs) to configure. Cassandra’s settings for compaction, compression, caching, garbage
collection, and bloom filtering are not applicable to Amazon Keyspaces and are ignored if
specified.

## Connections

You can use existing Cassandra drivers to communicate with Amazon Keyspaces, but you need to
configure the drivers differently. Amazon Keyspaces supports up to 3,000 CQL queries per TCP
connection per second, but there is no limit on the number of connections a driver can
establish.

Most open-source Cassandra drivers establish a connection pool to Cassandra and load
balance queries over that pool of connections. Amazon Keyspaces exposes 9 peer IP addresses to
drivers, and the default behavior of most drivers is to establish a single connection to
each peer IP address. Therefore, the maximum CQL query throughput of a driver using the
default settings is 27,000 CQL queries per second.

To increase this number, we recommend increasing the number of connections per IP
address your driver is maintaining in its connection pool. For example, setting the maximum
connections per IP address to 2 doubles the maximum throughput of your driver to 54,000 CQL
queries per second.

As a best practice, we recommend configuring drivers to use 500 CQL queries per second
per connection to allow for overhead and to improve distribution. In this scenario,
planning for 18,000 CQL queries per second requires 36 connections. Configuring the driver
for 4 connections across 9 endpoints provides for 36 connections performing 500 request per
second. For more information about best practices for connections, see [Optimize client driver connections for the serverless environment](connections.md "connections.md").

When connecting with VPC endpoints, there might be fewer endpoints available. This means
that you have to increase the number of connections in the driver configuration. For more
information about best practices for VPC connections, see [How to configure connections over VPC endpoints in Amazon Keyspaces](connections.md#connections.VPCendpoints "connections.md#connections.VPCendpoints").

## `IN` keyword

Amazon Keyspaces supports the `IN` keyword in the `SELECT` statement.
`IN` is not supported with `UPDATE` and `DELETE`. When
using the `IN` keyword in the `SELECT` statement, the results of the
query are returned in the order of how the keys are presented in the `SELECT`
statement. In Cassandra, the results are ordered lexicographically.

When using `ORDER BY`, full re-ordering with disabled pagination is not
supported and results are ordered within a page. Slice queries are not supported with the
`IN` keyword. `TOKENS` are not supported with the `IN`
keyword. Amazon Keyspaces processes queries with the `IN` keyword by creating subqueries.
Each subquery counts as a connection towards the 3,000 CQL queries per TCP connection per
second limit. For more information, see [Use the IN operator with the SELECT statement in a query in Amazon Keyspaces](in.md "in.md").

## `FROZEN`

collections

The `FROZEN` keyword in Cassandra serializes multiple components of a collection data type into a single
immutable value that is treated like a `BLOB`. `INSERT` and `UPDATE` statements overwrite the entire collection.

Amazon Keyspaces supports up to 8 levels of nesting for frozen collections by default. For more information, see [Amazon Keyspaces service quotas](quotas.md#table "quotas.md#table").

Amazon Keyspaces doesn't support inequality comparisons that use the entire frozen collection in a
conditional `UPDATE` or `SELECT` statement. The behavior for
collections and frozen collections is the same in Amazon Keyspaces.

When you're using frozen collections with client-side timestamps, in the case where the timestamp of a
write operation is the same as the timestamp of an existing column that isn't expired or
tombstoned, Amazon Keyspaces doesn't perform comparisons. Instead, it lets the server determine the
latest writer, and the latest writer wins.

For more information about frozen collections, see [Collection types](cql.md#cql.data-types.collection "cql.md#cql.data-types.collection").

## Lightweight

transactions

Amazon Keyspaces (for Apache Cassandra) fully supports compare and set functionality on **INSERT**, **UPDATE**,
and **DELETE** commands, which are known as _lightweight
transactions_ (LWTs) in Apache Cassandra. As a serverless offering, Amazon Keyspaces (for Apache Cassandra)
provides consistent performance at any scale, including for
lightweight transactions. With Amazon Keyspaces, there is no performance penalty for using
lightweight transactions.

## Load balancing

The `system.peers` table entries correspond to Amazon Keyspaces load balancers. For
best results, we recommend using a round robin load-balancing policy and tuning the number
of connections per IP to suit your application's needs.

## Pagination

Amazon Keyspaces paginates results based on the number of rows that it reads to process a request,
not the number of rows returned in the result set. As a result, some pages might contain
fewer rows than you specify in PAGE SIZE for filtered queries. In addition, Amazon Keyspaces paginates
results automatically after reading 1 MB of data to provide customers with
consistent, single-digit millisecond read performance. For more information, see [Paginate results in Amazon Keyspaces](paginating-results.md "paginating-results.md").

In tables with static columns, both Apache Cassandra and Amazon Keyspaces establish the partition's
static column value at the start of each page in a multi-page query. When a table has large
data rows, as a result of the Amazon Keyspaces pagination behavior, the likelihood is higher that a
range read operation result could return more pages for Amazon Keyspaces than for Apache Cassandra.
Consequently, there is a higher likelihood in Amazon Keyspaces that concurrent updates to the static
column could result in the static column value being different in different pages of the
range read result set.

## Partitioners

The default partitioner in Amazon Keyspaces is the Cassandra-compatible
`Murmur3Partitioner`. In addition, you have the choice of using either the
Amazon Keyspaces `DefaultPartitioner` or the Cassandra-compatible
`RandomPartitioner`.

With Amazon Keyspaces, you can safely change the partitioner for your account without having to
reload your Amazon Keyspaces data. After the configuration change has completed, which takes
approximately 10 minutes, clients will see the new partitioner setting automatically the
next time they connect. For more information, see [Working with partitioners in Amazon Keyspaces](working-with-partitioners.md "working-with-partitioners.md").

## Prepared statements

Amazon Keyspaces supports the use of prepared statements for data manipulation language (DML)
operations, such as reading and writing data. Amazon Keyspaces does not currently support the use of
prepared statements for data definition language (DDL) operations, such as creating tables
and keyspaces. DDL operations must be run outside of prepared statements.

## Range delete

Amazon Keyspaces supports deleting rows in range. A range is a contiguous set of rows within a
partition. You specify a range in a DELETE operation by using a WHERE clause. You can
specify the range to be an entire partition.

Furthermore, you can specify a range to be a subset of contiguous rows within a
partition by using relational operators (for example, '>', '<'), or by including the
partition key and omitting one or more clustering columns. With Amazon Keyspaces, you can delete up to
1,000 rows within a range in a single operation.

Range deletes are not isolated. Individual
row deletions are visible to other operations while a range delete is in process.

## System tables

Amazon Keyspaces populates the system tables that are required by Apache 2.0 open-source Cassandra
drivers. The system tables that are visible to a client contain information that's unique
to the authenticated user. The system tables are fully controlled by Amazon Keyspaces and are
read-only. For more information, see [System keyspaces in Amazon Keyspaces](working-with-keyspaces.md "working-with-keyspaces.md").

Read-only access to system tables is required, and you can control it with IAM access
policies. For more information, see [Managing access using policies](security-iam.md#security_iam_access-manage "security-iam.md#security_iam_access-manage"). You must
define tag-based access control policies for system tables differently depending on whether
you use the AWS SDK or Cassandra Query Language (CQL) API calls through Cassandra drivers
and developer tools. To learn more about tag-based access control for system tables, see
[Amazon Keyspaces resource access based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-tags").

If you access Amazon Keyspaces using [Amazon VPC endpoints](vpc-endpoints.md "vpc-endpoints.md"), you see
entries in the `system.peers` table for each Amazon VPC endpoint that Amazon Keyspaces has
permissions to see. As a result, your Cassandra driver might issue a [warning message](vpc-endpoints.md#vpc_troubleshooting "vpc-endpoints.md#vpc_troubleshooting") about the control node itself in
the `system.peers` table. You can safely ignore this warning.

## Timestamps

In Amazon Keyspaces, cell-level timestamps that are compatible with the default timestamps in
Apache Cassandra are an opt-in feature.

The `USING TIMESTAMP` clause and the `WRITETIME` function are only
available when client-side timestamps are turned on for a table.
To learn more about client-side timestamps in Amazon Keyspaces, see [Client-side timestamps in Amazon Keyspaces](client-side-timestamps.md "client-side-timestamps.md").

## User-defined types (UDTs)

The inequality operator is not supported for UDTs in Amazon Keyspaces.

To learn how to work with UDTs in Amazon Keyspaces, see [User-defined types (UDTs) in Amazon Keyspaces](udts.md "udts.md").

To review how many UDTs are supported per keyspace, supported levels of nesting,
and other default values and quotas related to UDTs, see [Quotas and default values for user-defined types (UDTs) in Amazon Keyspaces](quotas.md#quotas-udts "quotas.md#quotas-udts").
