# View the tags of a table

The following examples show how to view the tags of a table in Amazon Keyspaces using the console, CQL, or the AWS CLI.

Console

###### View the tags of a table using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**.
3. Choose a table from the list and choose the **Tags** tab.

Cassandra Query Language (CQL)

###### View the tags of a table using CQL

To read the tags attached to a table, use the following CQL statement.

```
SELECT * FROM system_schema_mcs.tags WHERE `valid_where_clause`;
```

The `WHERE` clause is required, and must use one of the following formats:

- `keyspace_name = `'mykeyspace'`AND resource_name =`'mytable'``
- `resource_id = `arn``
- The following query returns the tags of the specified table.

```

SELECT * FROM system_schema_mcs.tags WHERE keyspace_name = `'mykeyspace'` AND resource_name = `'mytable'`;
```

The output of that query looks like the following.

```
`resource_id | keyspace_name | resource_name | resource_type | tags
----------------------------------------------------------------------------+---------------+---------------+---------------+------
arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable| mykeyspace | mytable | table | {'key1': 'val1', 'key2': 'val2'}`
```

CLI

###### View the tags of a table using the AWS CLI

- This example shows how to list the tags of the specified resource.

```
aws keyspaces list-tags-for-resource --resource-arn '`arn:aws:`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/my_keyspace/table/my_table/stream/2025-05-11T21:21:33.291`cassandra:`us-east-1`:`111122223333`:/keyspace/myKeyspace/table/myTable`'
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
