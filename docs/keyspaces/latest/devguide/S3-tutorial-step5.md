# Step 5: (Optional) Cleanup

Follow these steps to remove all the AWS resources created in this tutorial.

###### Remove the resources created in this tutorial

1. Delete the second CloudFormation stack created in this tutorial. This removes the AWS Glue job and trigger created in this tutorial.
   You can use the following command to do this.

```
aws cloudformation delete-stack --stack-name `cfn-glue`
```

2. Delete the Amazon S3 bucket along with all data stored in it. You can use the following command to do so.

```
aws s3 rm `s3://s3-keyspaces` --recursive
```

3. Delete the first stack created in this tutorial. This deletes the IAM role and associated permissions created in this tutorial.
   You can use the following command as an example.

```
aws cloudformation delete-stack --stack-name `cfn-setup`
```

4. Delete the Amazon Keyspaces keyspace and table. Deleting the keyspace automatically deletes all tables in that keyspace. You can use one the following options to do so.

AWS CLI

```
aws keyspaces delete-keyspace --keyspace-name '`aws`'
```

To confirm that the keyspace was deleted, you can use the following command.

```
aws keyspaces list-keyspaces
```

To delete the table first, you can use the following command.

```
aws keyspaces delete-table --keyspace-name '`aws`' --table-name '`user`'
```

To confirm that your table was deleted, you can use the following command.

```
aws keyspaces list-tables --keyspace-name '`aws`'
```

For more information, see [delete keyspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html") and [delete table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html") in the _AWS CLI Command Reference_.

cqlsh

```
DROP KEYSPACE IF EXISTS "`aws`";
```

To verify that your keyspaces was deleted, you can use the following statement.

```
SELECT * FROM system_schema.keyspaces ;
```

Your keyspace should not be listed in the output of this
statement. Note that there can be a delay until the keyspaces is
deleted. For more information, see [DROP KEYSPACE](cql.ddl.md#cql.ddl.keyspace.drop "cql.ddl.md#cql.ddl.keyspace.drop").

To delete the table first, you can use the following command.

```
DROP TABLE "`aws.user`"
```

To confirm that your table was deleted, you can use the following command.

```
SELECT * FROM system_schema.tables WHERE keyspace_name = "`aws`";
```

Your table should not be listed in the output of this
statement. Note that there can be a delay until the table is
deleted. For more information, see [DROP TABLE](cql.ddl.md#cql.ddl.table.drop "cql.ddl.md#cql.ddl.table.drop").
