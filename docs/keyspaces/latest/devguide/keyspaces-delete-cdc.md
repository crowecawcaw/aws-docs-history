# Disable a CDC stream in Amazon Keyspaces

To disable a CDC stream in a keyspace, you can use the `ALTER TABLE`
statement in CQL, the `update-table` command with the AWS CLI, or the
console.

Cassandra Query Language (CQL)

###### Disable a stream (CDC stream) with CQL

1. To disable a stream, you can use the following statement.

```
ALTER TABLE mykeyspace.mytable
WITH cdc = FALSE;
```

2. To confirm that the stream is disabled, you can use the following statement.

```
SELECT keyspace_name, table_name, cdc, custom_properties FROM system_schema_mcs.tables WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

The output of that statement looks similar to this.

```
 `keyspace_name | table_name | cdc | custom_properties
---------------+------------+-------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mykeyspace | mytable | False | {'capacity_mode': {'last_update_to_pay_per_request_timestamp': '1741385668642', 'throughput_mode': 'PAY_PER_REQUEST'}, 'encryption_specification': {'encryption_type': 'AWS_OWNED_KMS_KEY'}, 'point_in_time_recovery': {'status': 'disabled'}}`
```

CLI

###### Disable a stream (CDC stream) with the AWS CLI

1. To disable a stream, you can use the following command.

```
aws keyspaces update-table \
--keyspace-name 'mykeyspace' \
--table-name 'mytable' \
--cdc-specification status=DISABLED
```

2. The output of the command looks similar to this example.

```
`{
 "keyspaceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/my_keyspace/",
 "streamName": "my_stream"
}`
```

Console

###### Disable a stream (CDC stream) with the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose a table from the list.
3. Choose the **Streams** tab.
4. Choose **Edit**.
5. Unselect **Turn on streams**.
6. Choose **Save changes** to disable the stream.
