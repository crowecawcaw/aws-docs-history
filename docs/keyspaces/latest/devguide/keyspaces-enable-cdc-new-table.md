# Enable a CDC stream when creating a new table in Amazon Keyspaces

To enable a CDC stream when you create a table, you can use the `CREATE TABLE`
statement in CQL or the `create-table` command with the AWS CLI.

For each changed row in the table, Amazon Keyspaces can capture the following changes based on the `view_type` of the
`cdc_specification` you select:

- `NEW_AND_OLD_IMAGES` – both versions of the row, before and after the change. This is the default.
- `NEW_IMAGE` – the version of the row after the change.
- `OLD_IMAGE` – the version of the row before the change.
- `KEYS_ONLY` – the partition and clustering keys of the row that was changed.
  For information about how to tag a stream, see [Add tags to a new stream when creating a table](Tagging.Operations.new.table.md "Tagging.Operations.new.table.md").

###### Note

Amazon Keyspaces CDC requires the presence of a service-linked role
(`AWSServiceRoleForAmazonKeyspacesCDC`) that publishes metric data
from Amazon Keyspaces CDC streams into the `"cloudwatch:namespace": "AWS/Cassandra"`
in your CloudWatch account on your behalf. This role is created automatically for you. For
more information, see [Using roles for Amazon Keyspaces CDC streams](using-service-linked-roles-CDC-streams.md "using-service-linked-roles-CDC-streams.md").

Cassandra Query Language (CQL)

###### Enable a CDC stream when you create a table with CQL

1. ```
   CREATE TABLE mykeyspace.mytable (a text, b text, PRIMARY KEY(a))
   WITH CUSTOM_PROPERTIES={'cdc_specification': {'view_type': 'NEW_IMAGE'}} AND CDC = TRUE;
   ```

```
2. To confirm the stream settings, you can use the following statement.



```

SELECT keyspace_name, table_name, cdc, custom_properties FROM system_schema_mcs.tables WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';

```

The output of that statement should look similar to this.



```

SELECT keyspace_name, table_name, cdc, custom_properties FROM system_schema_mcs.tables WHERE keyspace_name = 'mykeyspace' AND table_name = 'mytable';`keyspace_name | table_name | cdc | custom_properties
---------------+------------+------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 mykeyspace | mytable | True | {'capacity_mode': {'last_update_to_pay_per_request_timestamp': '1741383893782', 'throughput_mode': 'PAY_PER_REQUEST'}, 'cdc_specification': {'latest_stream_arn': 'arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable/stream/2025-03-07T21:44:53.783', 'status': 'ENABLED', 'view_type': 'NEW_IMAGE'}, 'encryption_specification': {'encryption_type': 'AWS_OWNED_KMS_KEY'}, 'point_in_time_recovery': {'status': 'disabled'}}`>

```


CLI
###### Enable a CDC stream when you create a table with the AWS CLI

1. To create a stream you can use the following syntax.



```

aws keyspaces create-table \
--keyspace-name 'mykeyspace' \
--table-name 'mytable' \
--schema-definition 'allColumns=[{name=a,type=text},{name=b,type=text}],partitionKeys=[{name=a}]' \
--cdc-specification status=ENABLED,viewType=NEW_IMAGE

```
2. The output of that command shows the standard `create-table` response and looks similar to this example.



```

`{ "resourceArn": "arn:aws:cassandra:us-east-1:111122223333:/keyspace/mykeyspace/table/mytable" }`

```

```
