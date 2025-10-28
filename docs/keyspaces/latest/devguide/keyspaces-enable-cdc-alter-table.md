# Enable a CDC stream for an existing table in Amazon Keyspaces

To enable a CDC stream for an existing table, you can use the `ALTER TABLE` statement in CQL,
the `update-table` command with the AWS CLI, or you can use the console.

For each changed row in the table, Amazon Keyspaces can capture the following changes based on the `view_type` of the
`cdc_specification` you select:

- `NEW_AND_OLD_IMAGES` – both versions of the row, before and after the change. This is the default.
- `NEW_IMAGE` – the version of the row after the change.
- `OLD_IMAGE` – the version of the row before the change.
- `KEYS_ONLY` – the partition and clustering keys of the row that was changed.
  For information about how to tag a stream, see [Add new tags to a stream](Tagging.Operations.existing.md "Tagging.Operations.existing.md").

###### Note

Amazon Keyspaces CDC requires the presence of a service-linked role
(`AWSServiceRoleForAmazonKeyspacesCDC`) that publishes metric data
from Amazon Keyspaces CDC streams into the `"cloudwatch:namespace": "AWS/Cassandra"`
in your CloudWatch account on your behalf. This role is created automatically for you. For
more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").

Cassandra Query Language (CQL)

###### Enable a stream (CDC stream) with CQL

You can use `ALTER TABLE` to enable a stream for an existing table.

1. The following example creates a stream that only captures changes to partition and clustering keys of a changed row.

```
ALTER TABLE mykeyspace.mytable
WITH cdc = TRUE
WITH CUSTOM_PROPERTIES={'cdc_specification': {'view_type': 'KEYS_ONLY'}};
```

2. To verify the stream settings, you can use the following statement.

```
SELECT keyspace_name, table_name, cdc, custom_properties FROM system_schema_mcs.tables WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';
```

The output of the statement looks similar to this.

```
 `keyspace_name | table_name | cdc | custom_properties
---------------+------------+------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mykeyspace | mytable | True | {'capacity_mode': {'last_update_to_pay_per_request_timestamp': '1741385897045', 'throughput_mode': 'PAY_PER_REQUEST'}, 'cdc_specification': {'latest_stream_arn': 'arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable/stream/2025-03-07T22:20:10.454', 'status': 'ENABLED', 'view_type': 'KEYS_ONLY'}, 'encryption_specification': {'encryption_type': 'AWS_OWNED_KMS_KEY'}, 'point_in_time_recovery': {'status': 'disabled'}}`
```

CLI

###### Create a CDC stream with the AWS CLI

1. To create a stream for an existing table you can use the following syntax.

```
aws keyspaces update-table \
--keyspace-name 'mykeyspace' \
--table-name 'mytable' \
--cdc-specification status=ENABLED,viewType=NEW_AND_OLD_IMAGES
```

2. The output of that command shows the standard `create-table` response and looks similar to this example.

```
`{ "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable" }`
```

Console

###### Enable a CDC stream with the Amazon Keyspaces console

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. In the navigation pane, choose **Tables**, and then choose a table from the list.
3. Choose the **Streams** tab.
4. Choose **Edit** to enable a stream.
5. Select **Turn on streams**.
6. Choose **View type** of the stream. The following options are available. Note that you can't change the view type
   of a stream after it's been created.
   - **New and old images** – Amazon Keyspaces captures both versions of the row, before and after the change. This is the default.
   - **New image** – Amazon Keyspaces captures only the version of the row after the change.
   - **Old image** – Amazon Keyspaces captures only the version of the row before the change.
   - **Primary key only** – Amazon Keyspaces captures only the partition and clustering key columns of the row that was changed.

7. To finish, choose **Save changes**.
