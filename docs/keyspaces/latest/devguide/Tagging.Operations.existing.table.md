# Delete tags from a table

Console

###### Delete tags from a table using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**.
3. Choose a table from the list and choose the **Tags** tab.
4. Choose **Manage
   tags** to delete tags from the table.
5. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Delete tags from a table using CQL

- The following statement shows how to delete tags from an existing table.

```
ALTER TABLE `mytable` DROP TAGS `{'key3':'val3', 'key4':'val4'}`;
```

CLI

###### Add tags to a table using the AWS CLI

- The following statement removes the specified tags from a keyspace.

```
aws keyspaces untag-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/myKeyspace/table/myTable`' --tags 'key=key3,value=val3' 'key=key4,value=val4'
```
