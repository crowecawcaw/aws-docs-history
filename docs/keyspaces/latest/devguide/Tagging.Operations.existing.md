# Add tags to a table

You can add tags to an existing table in Amazon Keyspaces using the console, CQL or the AWS CLI.

Console

###### Add tags to a table using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**.
3. Choose a table from the list and choose the **Tags** tab.
4. Choose **Manage
   tags** to add tags to the table.
5. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Add tags to a table using CQL

- The following statement shows how to add tags to an existing table.

```
ALTER TABLE `mykeyspace.mytable` ADD TAGS `{'key1':'val1', 'key2':'val2'}`;
```

CLI

###### Add tags to a table using the AWS CLI

- The following example shows how to add new tags to an existing table.

```
aws keyspaces tag-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/myKeyspace/table/myTable`' --tags 'key=key3,value=val3' 'key=key4,value=val4'
```
