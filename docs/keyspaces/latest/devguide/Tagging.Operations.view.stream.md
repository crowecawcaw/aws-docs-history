# View the tags of a stream

The following examples show how to view the tags of a stream in Amazon Keyspaces using CQL or the
AWS CLI.

Console

###### View the tags of a stream using the console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**.
3. Choose a table from the list and choose the **Streams** tab.
4. You can view the tags of the stream in the **Tags** section.

Cassandra Query Language (CQL)

###### View the tags of a stream using CQL

To read the tags attached to a stream, you must specify the resource
ARN of the stream in the `WHERE` clause. The following CQL
syntax is an example of this.

```
SELECT * FROM system_schema_mcs.tags WHERE resource_id = `stream_arn`;
```

- The following query returns the tags for the specified
  stream.

```
SELECT tags FROM system_schema_mcs.tags WHERE resource_id = '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/my_keyspace/table/my_table/stream/2025-05-06T17:17:39.800`';
```

The output of that query looks like the following.

```
 `resource_id | keyspace_name | resource_name | resource_type | tags
 ------------------------------------------------------------------------------------------------------------------+---------------+-------------------------+---------------+----------------------
 arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table/stream/2025-04-02T23:00:07.052 | singleks | 2025-04-02T23:00:07.052 | stream | {'tagkey': 'tagval'}`
```

CLI

###### View the tags of a stream using the AWS CLI

- This example shows how to list the tags for all streams under the specified keyspace.

```
aws keyspaces list-tags-for-resource --resource-arn '`arn:aws:cassandra:`us-east-1`:`111122223333`:/keyspace/my_keyspace/table/my_table/stream/2025-05-11T21:21:33.291`'
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
