# Restore a deleted table using Amazon Keyspaces PITR

The following procedure shows how to restore a deleted table from backup to the time of deletion. You can do this using CQL or the AWS CLI.

###### Note

This procedure assumes that PITR was enabled on the deleted table.

Cassandra Query Language (CQL)

###### Restore a deleted table using CQL

1. To confirm that point-in-time recovery is enabled for a deleted table, query
   the system table. Only tables with point-in-time recovery enabled are
   shown.

```
SELECT custom_properties
FROM system_schema_mcs.tables_history
WHERE keyspace_name = 'mykeyspace' AND table_name = 'my_table';
```

The query shows the following output.

```
`custom_properties
------------------
{
 ...,
 "point_in_time_recovery":{
 "restorable_until_time":"2020-08-04T00:48:58.381Z",
 "status":"enabled"
 }
}`
```

2. Restore the table to the time of deletion with the following sample
   statement.

```
RESTORE TABLE mykeyspace.mytable_restored
FROM TABLE mykeyspace.mytable;
```

CLI

###### Restore a deleted table using the AWS CLI

1. Delete a table that you created previously that has PITR enabled. The following command is an example.

```
aws keyspaces delete-table --keyspace-name 'myKeyspace' --table-name 'myTable'
```

2. Restore the deleted table to the time of deletion with the following command.

```
aws keyspaces restore-table --source-keyspace-name 'myKeyspace' --source-table-name 'myTable' --target-keyspace-name 'myKeyspace' --target-table-name 'myTable_restored2'
```

The output of this command returns the ARN of the restored table.

```
`{
 "restoredTableARN": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/myKeyspace/table/myTable_restored2"
}`
```
