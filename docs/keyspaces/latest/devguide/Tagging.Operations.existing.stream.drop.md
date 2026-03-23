# Delete tags from a stream

To delete tags from a stream, you can use CQL or the AWS CLI. You can only delete the
tags for the latest stream.

Console

###### Delete tags from a table using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**.
3. Choose a table from the list and choose the **Streams** tab.
4. In the **Tags** section choose **Manage
   tags** to delete tags from the table.
5. After the tag you want to delete, choose **Remove**.
6. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Delete tags from a stream using CQL

- The following statement shows how to delete tags from an existing stream.

```
ALTER TABLE `mytable` DROP TAGS_FOR_CDC `{'key3':'val3', 'key4':'val4'}`;
```

CLI

###### Delete tags from a stream using the AWS CLI

- The following statement removes the specified tags from a stream.

```
aws keyspaces untag-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/my_keyspace/table/my_table/stream/2025-05-11T21:21:33.291`' --tags 'key=key3,value=val3' 'key=key4,value=val4'
```
