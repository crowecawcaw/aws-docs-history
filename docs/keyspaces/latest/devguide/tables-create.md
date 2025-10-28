# Check table creation status in Amazon Keyspaces

Amazon Keyspaces performs data definition language (DDL) operations, such as creating and
deleting tables, asynchronously. You can monitor the creation status of new tables in
the AWS Management Console, which indicates when a table is pending or active. You can also monitor
the creation status of a new table programmatically by using the system schema table.

A table shows as active in the system schema when it's ready for use. The recommended
design pattern to check when a new table is ready for use is to poll the Amazon Keyspaces system
schema tables (`system_schema_mcs.*`). For a list of DDL statements for tables, see the
[Tables](cql.ddl.md "cql.ddl.md") section in the CQL language reference.

The following query shows the status of a table.

```
SELECT keyspace_name, table_name, status FROM system_schema_mcs.tables WHERE keyspace_name = `'mykeyspace'` AND table_name = `'mytable'`;
```

For a table that is still being created and is pending,the output of the query looks
like this.

```
`keyspace_name | table_name | status
--------------+------------+--------
 mykeyspace | mytable | CREATING`
```

For a table that has been successfully created and is active, the output of the query
looks like the following.

```
`keyspace_name | table_name | status
--------------+------------+--------
 mykeyspace | mytable | ACTIVE`
```
