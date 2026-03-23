# Delete a keyspace in Amazon Keyspaces

To avoid being charged for keyspaces, delete all the keyspaces
that you're not using. When you
delete a keyspace, the keyspace and all its tables are deleted and you stop accruing
charges for them.

You can delete a keyspace using either the console, CQL, or the AWS CLI.

The following procedure deletes a keyspace and all its tables and data using the
console.

###### To delete a keyspace using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**.
3. Choose the box to the left of the name of each keyspace that you want to
   delete.
4. Choose **Delete**.
5. On the **Delete keyspace** screen, enter
   `Delete` in the box. Then, choose **Delete
   keyspace**.
6. To verify that the keyspace `catalog` was deleted,
   choose **Keyspaces** in the navigation pane and confirm
   that it is no longer listed. Because you deleted its keyspace, the
   `book_awards` table under **Tables** should
   also not be listed.
   The following procedure deletes a keyspace and all its tables and data using
   CQL.

###### To delete a keyspace using CQL

1. Open AWS CloudShell and connect to Amazon Keyspaces using the following command. Make sure to update `us-east-1`
   with your own Region.

```
cqlsh-expansion cassandra.`us-east-1`.amazonaws.com 9142 --ssl
```

2. Delete your keyspace by entering the following statement.

```
DROP KEYSPACE IF EXISTS catalog ;
```

3. Verify that your keyspace was deleted.

```
SELECT * from system_schema.keyspaces ;
```

Your keyspace should not be listed. Note that because this is an asynchronous operation,
there can be a delay until the keyspace is deleted. After the keyspace has been deleted, the output of the
statement should look like this.

```
`keyspace_name | durable_writes | replication
-------------------------+----------------+-------------------------------------------------------------------------------------
 system_schema | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system_schema_mcs | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
 system_multiregion_info | True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}

(4 rows)`
```

The following procedure deletes a keyspace and all its tables and data using
the AWS CLI.

###### To delete a keyspace using the AWS CLI

1. Open AWS CloudShell
2. Delete your keyspace by entering the following statement.

```
aws keyspaces delete-keyspace --keyspace-name 'catalog'
```

3. Verify that your keyspace was deleted.

```
aws keyspaces list-keyspaces
```

The output of this statement should look similar to this, and only list
the system keyspaces. Note that because this is an asynchronous operation,
there can be a delay until your keyspace is deleted.

```
`{
 "keyspaces": [
 {
 "keyspaceName": "system_schema",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/system_schema/",
 "replicationStrategy": "SINGLE_REGION"
 },
 {
 "keyspaceName": "system_schema_mcs",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/system_schema_mcs/",
 "replicationStrategy": "SINGLE_REGION"
 },
 {
 "keyspaceName": "system",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/system/",
 "replicationStrategy": "SINGLE_REGION"
 },
 {
 "keyspaceName": "system_multiregion_info",
 "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/system_multiregion_info/",
 "replicationStrategy": "SINGLE_REGION"
 }
 ]
}`
```
