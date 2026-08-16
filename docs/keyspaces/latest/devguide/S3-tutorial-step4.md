# Step 4: (Optional) Cleanup

Follow these steps to remove all the AWS resources created in this tutorial. The AWS Glue job stacks
must be deleted before the parent infrastructure stack because they reference its exported values.

###### To remove the resources created in this tutorial

1. Delete the Amazon S3 bucket contents created by bootstrap. Replace `YOURACCOUNTID` with your AWS account ID.

```
`$` `aws s3 rm s3://amazon-keyspaces-bulk-cli-`aksglue`-`YOURACCOUNTID` --recursive`
```

2. Delete the AWS Glue job stacks created by the bootstrap command. These child stacks must be
   deleted before the parent stack. You can use the following commands.

```
`$` `aws cloudformation delete-stack --stack-name `aksglue`-export`
`$` `aws cloudformation delete-stack --stack-name `aksglue`-import`
`$` `aws cloudformation delete-stack --stack-name `aksglue`-count`
```

Wait for the child stacks to finish deleting before proceeding. You can check the status
with the following command.

```
`$` `aws cloudformation wait stack-delete-complete --stack-name `aksglue`-export`
`$` `aws cloudformation wait stack-delete-complete --stack-name `aksglue`-import`
`$` `aws cloudformation wait stack-delete-complete --stack-name `aksglue`-count`
```

3. Delete the parent CloudFormation stack. This removes the Amazon S3 bucket resource and the IAM role
   created in this tutorial.

```
`$` `aws cloudformation delete-stack --stack-name `aksglue``
```

4. If you created a trigger in the previous step, delete it using the following command.

```
`$` `aws glue delete-trigger --name `KeyspacesExportWeeklyTrigger``
```

5. Delete the Amazon Keyspaces keyspace and table. Deleting the keyspace automatically deletes all tables in that keyspace. You can use one of the following options.

AWS CLI

```
`$` `aws keyspaces delete-keyspace --keyspace-name '`catalog`'`
```

To confirm that the keyspace was deleted, you can use the following command.

```
`$` `aws keyspaces list-keyspaces`
```

To delete the table first, you can use the following command.

```
`$` `aws keyspaces delete-table --keyspace-name '`catalog`' --table-name '`book_awards`'`
```

To confirm that your table was deleted, you can use the following command.

```
`$` `aws keyspaces list-tables --keyspace-name '`catalog`'`
```

For more information, see [delete keyspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html") and [delete table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html") in the _AWS CLI Command Reference_.

cqlsh

```
DROP KEYSPACE IF EXISTS "`catalog`";
```

To verify that your keyspace was deleted, you can use the following statement.

```
SELECT * FROM system_schema.keyspaces ;
```

Your keyspace should not be listed in the output of this
statement. Note that there can be a delay until the keyspace is
deleted. For more information, see [DROP KEYSPACE](cql.ddl.keyspace.md#cql.ddl.keyspace.drop "cql.ddl.keyspace.md#cql.ddl.keyspace.drop").

To delete the table first, you can use the following command.

```
DROP TABLE "`catalog`"."`book_awards`";
```

To confirm that your table was deleted, you can use the following command.

```
SELECT * FROM system_schema.tables WHERE keyspace_name = "`catalog`";
```

Your table should not be listed in the output of this
statement. Note that there can be a delay until the table is
deleted. For more information, see [DROP TABLE](cql.ddl.table.md#cql.ddl.table.drop "cql.ddl.table.md#cql.ddl.table.drop").
