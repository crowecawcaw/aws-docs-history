# Change capacity mode

When you switch a table from provisioned capacity mode to on-demand capacity mode,
Amazon Keyspaces makes several changes to the structure of your table and partitions. This
process can take several minutes. During the switching period, your table delivers
throughput that is consistent with the previously provisioned WCU and RCU amounts.

When you switch from on-demand capacity mode back to provisioned capacity mode,
your table delivers throughput that is consistent with the previous peak reached
when the table was set to on-demand capacity mode.

The following waiting periods apply when you switch capacity modes:

- You can switch a newly created table in on-demand mode to provisioned capacity mode at any time.
  However, you can only switch it back to on-demand mode 24 hours after the table’s creation timestamp.
- You can switch an existing table in on-demand mode to provisioned capacity mode at any time.
  However, you can switch capacity modes from provisioned to on-demand only once in a 24-hour period.

Cassandra Query Language (CQL)

###### Change a table's throughput capacity mode using CQL

1. To change a table's capacity mode to `PROVIOSIONED` you
   have to configure the read capacity and write capacity units
   based on your workloads expected peak values. the following
   statement is an example of this. You can also run this
   statement to adjust the read capacity or the write capacity
   units of the table.

```
ALTER TABLE catalog.book_awards WITH CUSTOM_PROPERTIES={'capacity_mode':{'throughput_mode': 'PROVISIONED', 'read_capacity_units': 6000, 'write_capacity_units': 3000}};
```

To configure provisioned capacity mode with auto-scaling, see
[Configure automatic scaling on an existing table](autoscaling.md "autoscaling.md"). 2. To change
the capacity mode of a table to on-demand mode, set the throughput mode to `PAY_PER_REQUEST`.
The following statement is an example of this.

```
ALTER TABLE catalog.book_awards WITH CUSTOM_PROPERTIES={'capacity_mode':{'throughput_mode': 'PAY_PER_REQUEST'}};
```

3. You can use the following statement to confirm the table's capacity mode.

```
SELECT * from system_schema_mcs.tables where keyspace_name = 'catalog' and table_name = 'book_awards';
```

A table configured with on-demand capacity mode returns the following.

```
`{
 "capacity_mode":{
 "last_update_to_pay_per_request_timestamp":"1727952499092",
 "throughput_mode":"PAY_PER_REQUEST"
 }
}`
```

The `last_update_to_pay_per_request_timestamp` value is measured in
milliseconds.

CLI

###### Change a table's throughput capacity mode using the AWS CLI

1. To change the table's capacity mode to `PROVIOSIONED`
   you have to configure the read capacity and write capacity units
   based on the expected peak values of your workload. The
   following command is an example of this. You can also run this
   command to adjust the read capacity or the write capacity units
   of the table.

```
aws keyspaces update-table --keyspace-name catalog --table-name book_awards
                                    \--capacity-specification throughputMode=PROVISIONED,readCapacityUnits=6000,writeCapacityUnits=3000
```

To configure provisioned capacity mode with auto-scaling, see
[Configure automatic scaling on an existing table](autoscaling.md "autoscaling.md"). 2. To change
the capacity mode of a table to on-demand mode, you set the throughput mode to `PAY_PER_REQUEST`.
The following statement is an example of this.

```
aws keyspaces update-table --keyspace-name catalog --table-name book_awards
                                    \--capacity-specification throughputMode=PAY_PER_REQUEST
```

3. You can use the following command to review the capacity mode that's configured for a table.

```
aws keyspaces get-table --keyspace-name catalog --table-name book_awards
```

The output for a table in on-demand mode looks like this.

```
`"capacitySpecification": {
 "throughputMode": "PAY_PER_REQUEST",
 "lastUpdateToPayPerRequestTimestamp": "2024-10-03T10:48:19.092000+00:00"
 }`
```
