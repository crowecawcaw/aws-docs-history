# DDL statements (data definition language) in Amazon Keyspaces

_Data definition language_ (DDL) is the set of Cassandra Query
Language (CQL) statements that you use to manage data structures in Amazon Keyspaces (for Apache Cassandra), such as
keyspaces and tables. You use DDL to create these data structures, modify them after
they are created, and remove them when they're no longer in use. Amazon Keyspaces performs DDL
operations asynchronously. For more information about how to confirm that an
asynchronous operation has completed, see [Asynchronous creation
and deletion of keyspaces and tables](functional-differences.md#functional-differences.table-keyspace-management "functional-differences.md#functional-differences.table-keyspace-management").

The following DDL statements are supported:

- [CREATE KEYSPACE](cql.ddl.md#cql.ddl.keyspace.create "cql.ddl.md#cql.ddl.keyspace.create")
- [ALTER KEYSPACE](cql.ddl.md#cql.ddl.keyspace.alter "cql.ddl.md#cql.ddl.keyspace.alter")
- [DROP KEYSPACE](cql.ddl.md#cql.ddl.keyspace.drop "cql.ddl.md#cql.ddl.keyspace.drop")
- [USE](cql.ddl.md#cql.ddl.keyspace.use "cql.ddl.md#cql.ddl.keyspace.use")
- [CREATE TABLE](cql.ddl.md#cql.ddl.table.create "cql.ddl.md#cql.ddl.table.create")
- [ALTER TABLE](cql.ddl.md#cql.ddl.table.alter "cql.ddl.md#cql.ddl.table.alter")
- [RESTORE TABLE](cql.ddl.md#cql.ddl.table.restore "cql.ddl.md#cql.ddl.table.restore")
- [DROP TABLE](cql.ddl.md#cql.ddl.table.drop "cql.ddl.md#cql.ddl.table.drop")
- [CREATE TYPE](cql.ddl.md#cql.ddl.type.create "cql.ddl.md#cql.ddl.type.create")
- [DROP TYPE](cql.ddl.md#cql.ddl.type.drop "cql.ddl.md#cql.ddl.type.drop")

###### Topics

- [Keyspaces](cql.ddl.md "cql.ddl.md")
- [Tables](cql.ddl.md "cql.ddl.md")
- [User-defined types (UDTs)](cql.ddl.md "cql.ddl.md")
