# Supported Cassandra APIs, operations, functions, and data

types

Amazon Keyspaces (for Apache Cassandra) is compatible with Cassandra Query Language (CQL) 3.11 API
(backward-compatible with version 2.x).

Amazon Keyspaces supports all commonly used Cassandra data-plane operations, such as creating
keyspaces and tables, reading data, and writing data.

The following sections list the supported functionality.

###### Topics

- [Cassandra API support](#cassandra-api-support "#cassandra-api-support")
- [Cassandra control plane API support](#cassandra-control-plane-apis "#cassandra-control-plane-apis")
- [Cassandra data plane API support](#cassandra-data-plane-apis "#cassandra-data-plane-apis")
- [Cassandra function support](#cassandra-functions "#cassandra-functions")
- [Cassandra data type support](#cassandra-data-type "#cassandra-data-type")

## Cassandra API support

| API operation              | Supported |
| -------------------------- | --------- |
| `CREATE KEYSPACE`          | Yes       |
| `ALTER KEYSPACE`           | Yes       |
| `DROP KEYSPACE`            | Yes       |
| `CREATE TABLE`             | Yes       |
| `ALTER TABLE`              | Yes       |
| `DROP TABLE`               | Yes       |
| `CREATE INDEX`             | No        |
| `DROP INDEX`               | No        |
| `UNLOGGED BATCH`           | Yes       |
| `LOGGED BATCH`             | Yes       |
| `SELECT`                   | Yes       |
| `INSERT`                   | Yes       |
| `DELETE`                   | Yes       |
| `UPDATE`                   | Yes       |
| `USE`                      | Yes       |
| `CREATE TYPE`              | Yes       |
| `ALTER TYPE`               | No        |
| `DROP TYPE`                | Yes       |
| `CREATE TRIGGER`           | No        |
| `DROP TRIGGER`             | No        |
| `CREATE FUNCTION`          | No        |
| `DROP FUNCTION`            | No        |
| `CREATE AGGREGATE`         | No        |
| `DROP AGGREGATE`           | No        |
| `CREATE MATERIALIZED VIEW` | No        |
| `ALTER MATERIALIZED VIEW`  | No        |
| `DROP MATERIALIZED VIEW`   | No        |
| `TRUNCATE`                 | No        |

## Cassandra control plane API support

Because Amazon Keyspaces is managed, the Cassandra control plane API operations to manage
cluster and node settings are not required. As a result, the following Cassandra features
are not applicable.

| Feature               | Reason                 |
| --------------------- | ---------------------- |
| Durable writes toggle | All writes are durable |
| Read repair settings  | Not applicable         |
| GC grace seconds      | Not applicable         |
| Bloom filter settings | Not applicable         |
| Compaction settings   | Not applicable         |
| Compression settings  | Not applicable         |
| Caching settings      | Not applicable         |
| Security settings     | Replaced by IAM        |

## Cassandra data plane API support

| Feature                                       | Supported |
| --------------------------------------------- | --------- |
| JSON support for SELECT and INSERT statements | Yes       |
| Static columns                                | Yes       |
| Time to Live (TTL)                            | Yes       |

## Cassandra function support

For more information about the supported functions, see [Built-in functions in Amazon Keyspaces](cql.md "cql.md").

| Function                         | Supported |
| -------------------------------- | --------- |
| `Aggregate` functions            | No        |
| `Blob` conversion                | Yes       |
| `Cast`                           | Yes       |
| `Datetime` functions             | Yes       |
| Timeconversion functions         | Yes       |
| `TimeUuid` functions             | Yes       |
| `Token`                          | Yes       |
| `User defined functions` (`UDF`) | No        |
| `Uuid`                           | Yes       |

## Cassandra data type support

The following table lists the Apache Cassandra data types supported in Amazon Keyspaces. For more
information about data types in Amazon Keyspaces, see [Data types](cql.md#cql.data-types "cql.md#cql.data-types").

| Data type                     | Supported |
| ----------------------------- | --------- |
| `ascii`                       | Yes       |
| `bigint`                      | Yes       |
| `blob`                        | Yes       |
| `boolean`                     | Yes       |
| `counter`                     | Yes       |
| `date`                        | Yes       |
| `decimal`                     | Yes       |
| `double`                      | Yes       |
| `float`                       | Yes       |
| `frozen`                      | Yes       |
| `inet`                        | Yes       |
| `int`                         | Yes       |
| `list`                        | Yes       |
| `map`                         | Yes       |
| `set`                         | Yes       |
| `smallint`                    | Yes       |
| `text`                        | Yes       |
| `time`                        | Yes       |
| `timestamp`                   | Yes       |
| `timeuuid`                    | Yes       |
| `tinyint`                     | Yes       |
| `tuple`                       | Yes       |
| `user-defined types` (`UDTs`) | Yes       |
| `uuid`                        | Yes       |
| `varchar`                     | Yes       |
| `varint`                      | Yes       |
