# View CDC streams in Amazon Keyspaces

To view or list all streams in keyspace, you can query the table
`system_schema_mcs.streams` in the system keyspace using a statement in
CQL, or use the `get-stream` and `list-stream` commands with the
AWS CLI, or the console.

For the required permissions, see [Configure permissions to work with CDC streams in Amazon Keyspaces](configure-cdc-permissions.md "configure-cdc-permissions.md").

Cassandra Query Language (CQL)

###### View CDC streams with CQL

- To monitor the CDC status of your table, you can use the following
  statement.

```
SELECT custom_properties
FROM system_schema_mcs.tables
WHERE keyspace_name='my_keyspace' and table_name='my_table';
```

The output of the command looks similar to this.

```
`...
custom_properties
----------------------------------------------------------------------------------
{'cdc_specification':{'status': 'Enabled', 'view_type': 'NEW_IMAGE', 'latest_stream_arn': 'arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table/stream/stream_label''}}
...`
```

CLI

###### View CDC streams with the AWS CLI

1. This example shows how to see the stream information for a table.

```
aws keyspaces get-table \
--keyspace-name 'my_keyspace' \
--table-name 'my_table'
```

The output of the command looks like this.

```
`{
 "keyspaceName": "my_keyspace",
 "tableName": "my_table",
 ... Other fields ...,
 "latestStreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/table/my_table/stream/stream_label",
 "cdcSpecification": {
 "status": "ENABLED",
 "viewType": "NEW_AND_OLD_IMAGES"
 }
}`
```

2. You can list all streams in your account in a specified AWS Region. The following
   command is an example of this.

```
aws keyspacesstreams list-streams --region `us-east-1`
```

The output of the command could look similar to this.

```
`{
 "Streams": [
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_1/table/t1/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_1"
 "TableName": "t1",
 },
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_1/table/t2/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_1"Create a keyspace with the name `catalog`. Note
 that streams are not supported in multi-Region keyspaces.
 "TableName": "t2",
 },
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_2/table/t1/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_3"
 "TableName": "t1",
 }
 ]
}`
```

3. You can also list the CDC streams for a given keyspace using the following parameters.

```
aws keyspacesstreams list-streams --keyspace-name ks_1 --region `us-east-1`
```

The output of the command looks similar to this.

```
`{
 "Streams": [
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_1/table/t1/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_1"
 "TableName": "t1",
 },
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_1/table/t2/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_1"
 "TableName": "t2",
 }
 ]
}`
```

4. You can also list the CDC streams for a given table using the following parameters.

```
aws keyspacesstreams list-streams --keyspace-name ks_1 --table-name t2 --region `us-east-1`
```

The output of the command looks similar to this.

```
`{
 "Streams": [
 {
 "StreamArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/ks_1/table/t2/stream/2023-05-11T21:21:33.291",
 "StreamLabel": "2023-05-11T21:21:33.291",
 "KeyspaceName": "ks_1"
 "TableName": "t2",
 }
 ]
}`
```

Console

###### View CDC streams in the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose a table from the list.
3. Choose the **Streams** tab to review the stream details.
