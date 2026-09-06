

# Client-side timestamps in Amazon Keyspaces
<a name="client-side-timestamps"></a>

In Amazon Keyspaces, client-side timestamps are Cassandra-compatible timestamps that are persisted for each cell in your table. You can use client-side timestamps for conflict resolution by letting your client applications determine the order of writes. For example, when clients of a globally distributed application make updates to the same data, client-side timestamps persist the order in which the updates were made on the clients. Amazon Keyspaces uses these timestamps to process the writes. 

Amazon Keyspaces client-side timestamps are fully managed. You don’t have to manage low-level system settings such as clean-up and compaction strategies. 

When you delete data, the rows are marked for deletion with a tombstone. Amazon Keyspaces removes tombstoned data automatically (typically within 10 days) without impacting your application performance or availability. Tombstoned data isn't available for data manipulation language (DML) statements. As you continue to perform reads and writes on rows that contain tombstoned data, the tombstoned data continues to count towards storage, read capacity units (RCUs), and write capacity units (WCUs) until it's deleted from storage. 

After client-side timestamps have been turned on for a table, you can specify a timestamp with the `USING TIMESTAMP` clause in your Data Manipulation Language (DML) CQL query. For more information, see [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md). If you do not specify a timestamp in your CQL query, Amazon Keyspaces uses the timestamp passed by your client driver. If the client driver doesn’t supply timestamps, Amazon Keyspaces assigns a cell-level timestamp automatically, because timestamps can't be `NULL`. To query for timestamps, you can use the `WRITETIME` function in your DML statement. 

Amazon Keyspaces doesn't charge extra to turn on client-side timestamps. However, with client-side timestamps you store and write additional data for each value in your row. This can lead to additional storage usage and in some cases additional throughput usage. For more information about Amazon Keyspaces pricing, see [Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing).

When client-side timestamps are turned on in Amazon Keyspaces, additional metadata is stored alongside your row data. The per-row overhead depends on your column types, whether the row uses TTL, and (for multi-Region tables) the number of replicating Regions. Overhead can range from a few bytes for rows of simple scalar columns to tens of bytes or more for rows with non-frozen collections or multi-Region counters. This metadata counts toward both your storage cost and your 1-MB row size quota.

To determine the overall impact on storage and throughput, consider the number of columns in your table, the data types used, and the number of collection elements in each row. For example, rows with many non-frozen collection columns containing large numbers of elements will have higher overhead than rows with only scalar columns. The additional metadata also affects the number of write capacity units (WCUs) consumed per write. For more information on how to estimate the overhead for your specific schema, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md). For more information on how to calculate read and write capacity, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md).

After client-side timestamps have been turned on for a table, you can't turn it off. 

To learn more about how to use client-side timestamps in queries, see [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md).

**Topics**
+ [How Amazon Keyspaces client-side timestamps integrate with AWS services](#client-side-timestamps_integration)
+ [Create a new table with client-side timestamps in Amazon Keyspaces](client-side-timestamps-create-new-table.md)
+ [Configure client-side timestamps for a table in Amazon Keyspaces](client-side-timestamps-existing-table.md)
+ [Use client-side timestamps in queries in Amazon Keyspaces](client-side-timestamps-how-to-queries.md)

## How Amazon Keyspaces client-side timestamps integrate with AWS services
<a name="client-side-timestamps_integration"></a>

The following client-side timestamps metric is available in Amazon CloudWatch to enable continuous monitoring.
+ `SystemReconciliationDeletes` – The number of delete operations required to remove tombstoned data.

For more information about how to monitor CloudWatch metrics, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md).

When you use CloudFormation, you can enable client-side timestamps when creating a Amazon Keyspaces table. For more information, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html). 