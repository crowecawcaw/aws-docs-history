# View the capacity mode of a table in Amazon Keyspaces

You can query the system table in the Amazon Keyspaces system keyspace to review capacity
mode information about a table. You can also see whether a table is using on-demand
or provisioned throughput capacity mode. If the table is configured with provisioned
throughput capacity mode, you can see the throughput capacity provisioned for the
table.

You can also use the AWS CLI to view the capacity mode of a table.

To change the provisioned throughput of a table, see [Change the capacity mode of a table in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

Cassandra Query Language (CQL)
Example

```
SELECT * from system_schema_mcs.tables where keyspace_name = 'mykeyspace' and table_name = 'mytable';
```

A table configured with on-demand capacity mode returns the following.

```
`{
 "capacity_mode":{
 "last_update_to_pay_per_request_timestamp":"1579551547603",
 "throughput_mode":"PAY_PER_REQUEST"
 }
}`
```

A table configured with provisioned throughput capacity mode returns the
following.

```
`{
 "capacity_mode":{
 "last_update_to_pay_per_request_timestamp":"1579048006000",
 "read_capacity_units":"5000",
 "throughput_mode":"PROVISIONED",
 "write_capacity_units":"6000"
 }
}`
```

The `last_update_to_pay_per_request_timestamp` value is measured in
milliseconds.

CLI
View a table's throughput capacity mode using the AWS CLI

```
aws keyspaces get-table --keyspace-name myKeyspace --table-name myTable
```

The output of the command can look similar to this for a table in provisioned capacity mode.

```
`"capacitySpecification": {
 "throughputMode": "PROVISIONED",
 "readCapacityUnits": 4000,
 "writeCapacityUnits": 2000
 }`
```

The output for a table in on-demand mode looks like this.

```
`"capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": "2024-10-03T10:48:19.092000+00:00"
 }`
```
