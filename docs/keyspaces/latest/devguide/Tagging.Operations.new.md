# Add tags when creating a new keyspace

You can use the Amazon Keyspaces console, CQL or the AWS CLI to add tags when you create a new keyspace.

Console

###### Set a tag when creating a new keyspace using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**, and then choose
   **Create keyspace**.
3. On the **Create keyspace** page, provide a name for the keyspace.
4. Under **Tags** choose **Add new tag** and enter a key and a value.
5. Choose **Create keyspace**.

Cassandra Query Language (CQL)

###### Set a tag when creating a new keyspace using CQL

- The following example creates a new keyspace with tags.

```
CREATE KEYSPACE `mykeyspace` WITH TAGS = `{'key1':'val1', 'key2':'val2'}`;
```

CLI

###### Set a tag when creating a new keyspace using the AWS CLI

- The following statement creates a new keyspace with tags.

```
aws keyspaces create-keyspace --keyspace-name 'myKeyspace' --tags 'key=key1,value=val1' 'key=key2,value=val2'
```
