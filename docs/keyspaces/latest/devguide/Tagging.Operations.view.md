# View the tags of a keyspace

The following examples show how to read tags using the console, CQL or the AWS CLI.

Console

###### View the tags of a keyspace using the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Keyspaces**.
3. Choose a keyspace from the list. Then choose the **Tags** tab where you can view the tags of the keyspace.

Cassandra Query Language (CQL)

###### View the tags of a keyspace using CQL

To read the tags attached to a keyspace, use the following CQL statement.

```
SELECT * FROM system_schema_mcs.tags WHERE `valid_where_clause`;
```

The `WHERE` clause is required, and must use one of the following formats:

- `keyspace_name = `'mykeyspace'` AND resource_type = 'keyspace'`
- `resource_id = `arn``
- The following statement shows whether a keyspace has tags.

```
SELECT * FROM system_schema_mcs.tags WHERE keyspace_name = `'mykeyspace'` AND resource_type = 'keyspace';
```

The output of the query looks like the following.

```
`resource_id | keyspace_name | resource_name | resource_type | tags
-----------------------------------------------------------------+---------------+---------------+---------------+------
arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/ | mykeyspace | mykeyspace | keyspace | {'key1': 'val1', 'key2': 'val2'}`
```

CLI

###### View the tags of a keyspace using the AWS CLI

- This example shows how to list the tags of the specified resource.

```
aws keyspaces list-tags-for-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/myKeyspace/`'
```

The output of the last command looks like this.

```
`{
 "tags": [
 {
 "key": "key1",
 "value": "val1"
 },
 {
 "key": "key2",
 "value": "val2"
 },
 {
 "key": "key3",
 "value": "val3"
 },
 {
 "key": "key4",
 "value": "val4"
 }
 ]
}`
```
