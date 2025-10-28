# Client-side timestamps in Amazon Keyspaces

In Amazon Keyspaces, client-side timestamps are Cassandra-compatible timestamps that are persisted
for each cell in your table. You can use client-side timestamps for conflict resolution by
letting your client applications determine the order of writes. For example, when clients of
a globally distributed application make updates to the same data, client-side timestamps
persist the order in which the updates were made on the clients. Amazon Keyspaces uses these timestamps
to process the writes.

Amazon Keyspaces client-side timestamps are fully managed. You don’t have to manage low-level system settings
such as clean-up and compaction strategies.

When you delete data, the rows are marked for deletion with a tombstone. Amazon Keyspaces removes tombstoned data
automatically (typically within 10 days) without impacting your application performance or availability.
Tombstoned data isn't available for data manipulation language
(DML) statements. As you continue to perform reads and writes on rows that contain tombstoned
data, the tombstoned data continues to count towards storage, read capacity units (RCUs), and write
capacity units (WCUs) until it's deleted from storage.

After client-side timestamps have been turned on for a table, you can specify a timestamp with the
`USING TIMESTAMP` clause in your Data Manipulation Language (DML) CQL query.
For more information, see [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md "client-side-timestamps-how-to-queries.md"). If you do
not specify a timestamp in your CQL query, Amazon Keyspaces uses the timestamp passed by your client
driver. If the client driver doesn’t supply timestamps, Amazon Keyspaces assigns a cell-level timestamp
automatically, because timestamps can't be `NULL`. To query for timestamps, you
can use the `WRITETIME` function in your DML statement.

Amazon Keyspaces doesn't charge extra to turn on client-side timestamps. However, with client-side timestamps you store and write additional data for each value in your row.
This can lead to additional storage usage and in some cases additional throughput usage. For more information about Amazon Keyspaces pricing, see
[Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").

When client-side timestamps are turned on in Amazon Keyspaces, every column of every row stores a timestamp. These
timestamps take up approximately 20–40 bytes (depending on your data), and
contribute to the storage and throughput cost for the row. These metadata bytes also
count towards your 1-MB row size quota. To determine the overall increase in storage
space (to ensure that the row size stays under 1 MB), consider the number of
columns in your table and the number of collection elements in each row. For example, if
a table has 20 columns, with each column storing 40 bytes of data, the size of the row
increases from 800 bytes to 1200 bytes. For more information on how to estimate the size
of a row, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md"). In addition to the extra 400 bytes
for storage, in this example, the number of write capacity units (WCUs) consumed per
write increases from 1 WCU to 2 WCUs. For more information on how to calculate read and
write capacity, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

After client-side timestamps have been turned on for a table, you can't turn it off.

To learn more about how to use client-side timestamps in queries, see [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md "client-side-timestamps-how-to-queries.md").

###### Topics

- [How Amazon Keyspaces client-side timestamps integrate with AWS
  services](#client-side-timestamps_integration "#client-side-timestamps_integration")
- [Create a new table with client-side timestamps in Amazon Keyspaces](client-side-timestamps-create-new-table.md "client-side-timestamps-create-new-table.md")
- [Configure client-side timestamps for a table in Amazon Keyspaces](client-side-timestamps-existing-table.md "client-side-timestamps-existing-table.md")
- [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md "client-side-timestamps-how-to-queries.md")

## How Amazon Keyspaces client-side timestamps integrate with AWS

services

The following client-side timestamps metric is available in Amazon CloudWatch to enable continuous
monitoring.

- `SystemReconciliationDeletes` – The number of delete operations required to remove tombstoned data.

For more information about how to monitor CloudWatch metrics, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

When you use AWS CloudFormation, you can enable client-side timestamps when creating a Amazon Keyspaces table. For more information,
see the [AWS CloudFormation User Guide](../../../AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.md").
