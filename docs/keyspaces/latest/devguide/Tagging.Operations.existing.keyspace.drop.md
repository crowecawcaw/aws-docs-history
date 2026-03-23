# Delete tags from a keyspace

Console

###### Delete a tag from an existing keyspace using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**.
3. Choose a keyspace from the list. Then choose the **Tags** tab where you can view the tags of the keyspace.
4. Choose **Manage tags** and delete the tags you don't need anymore.
5. Choose **Save changes**.

Cassandra Query Language (CQL)

###### Delete a tag from an existing keyspace using CQL

- ```
  ALTER KEYSPACE `mykeyspace` DROP TAGS `{'key1':'val1', 'key2':'val2'}`;
  ```

```


CLI
###### Delete a tag from an existing keyspace using the AWS CLI

* The following statement removes the specified tags from a keyspace.



```

aws keyspaces untag-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/myKeyspace/`' --tags 'key=key3,value=val3' 'key=key4,value=val4'

```

```
