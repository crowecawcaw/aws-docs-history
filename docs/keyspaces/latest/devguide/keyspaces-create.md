# Check keyspace creation status in Amazon Keyspaces

Amazon Keyspaces performs data definition language (DDL) operations, such as creating and
deleting keyspaces, asynchronously.

You can monitor the creation status of new keyspaces in the AWS Management Console, which indicates
when a keyspace is pending or active. You can also monitor the creation status of a new
keyspace programmatically by using the `system_schema_mcs` keyspace. A
keyspace becomes visible in the `system_schema_mcs`
`keyspaces` table when it's ready for use.

The recommended design pattern to check when a new keyspace is ready for use is to
poll the Amazon Keyspaces `system_schema_mcs`
`keyspaces` table (system_schema_mcs.\*). For a list of DDL statements for
keyspaces, see the [Keyspaces](cql.ddl.md "cql.ddl.md") section in the CQL language
reference.

The following query shows whether a keyspace has been successfully created.

```
SELECT * FROM system_schema_mcs.keyspaces WHERE keyspace_name = `'mykeyspace'`;
```

For a keyspace that has been successfully created, the output of the query looks like
the following.

```
`keyspace_name | durable_writes | replication
--------------+-----------------+--------------
 mykeyspace | true |{...} 1 item`
```
