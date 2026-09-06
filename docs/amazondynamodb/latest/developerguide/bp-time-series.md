

# Best practices for handling time series data in DynamoDB
<a name="bp-time-series"></a>

General design principles in Amazon DynamoDB recommend that you keep the number of tables you use to a minimum. For most applications, a single table is all you need. However, for time series data, you can often best handle it by using one table per application per period.

## Design pattern for time series data
<a name="bp-time-series-pattern"></a>

Consider a typical time series scenario, where you want to track a high volume of events. Your write access pattern is that all the events being recorded have today's date. Your read access pattern might be to read today's events most frequently, yesterday's events much less frequently, and then older events very little at all. One way to handle this is by building the current date and time into the primary key.

The following design pattern often handles this kind of scenario effectively:
+ Create one table per period, provisioned with the required read and write capacity and the required indexes.
+ Before the end of each period, prebuild the table for the next period. Just as the current period ends, direct event traffic to the new table. You can assign names to these tables that specify the periods they have recorded.
+ As soon as a table is no longer being written to, reduce its provisioned write capacity to a lower value (for example, 1 WCU), and provision whatever read capacity is appropriate. Reduce the provisioned read capacity of earlier tables as they age. You might choose to archive or delete the tables whose contents are rarely or never needed.

The idea is to allocate the required resources for the current period that will experience the highest volume of traffic and scale down provisioning for older tables that are not used actively, therefore saving costs. Depending on your business needs, you might consider write sharding to distribute traffic evenly to the logical partition key. For more information, see [Using write sharding to distribute workloads evenly in your DynamoDB table](bp-partition-key-sharding.md).

## Optimize storage costs with the Standard-IA table class
<a name="bp-time-series-table-class"></a>

DynamoDB offers two table classes: DynamoDB Standard and DynamoDB Standard-Infrequent Access (DynamoDB Standard-IA). The Standard-IA table class lowers your storage costs while increasing the cost of read and write throughput. It's a good fit when storage is the dominant portion of a table's cost and the table is accessed infrequently.

This trade-off maps naturally onto the time series pattern. The current period's table receives most of the read and write traffic, so keep it on the DynamoDB Standard table class, where throughput is less expensive. As a table ages out of active use, it is written to rarely (or not at all) and read infrequently, while you continue to retain its data. For these older tables, storage typically becomes the largest cost, so switching them to the Standard-IA table class can lower your overall cost.

Consider the following when you apply table classes to time series tables:
+ Keep the current (active) period on the DynamoDB Standard table class. The higher throughput cost of Standard-IA would outweigh its storage savings for a table that serves a high volume of reads and writes.
+ Switch a period's table to Standard-IA after it is no longer actively written to and is accessed infrequently, but you still need to retain its data (for example, for compliance or occasional historical queries).
+ You can set the table class when you create a table or change it later. Evaluate each table's storage-to-throughput cost ratio before switching, and monitor costs after the change.

For more information about table classes and how to choose between them, see [DynamoDB table classes](HowItWorks.TableClasses.md) and [Evaluate your DynamoDB table class selection](CostOptimization_TableClass.md).

## Time series table examples
<a name="bp-time-series-examples"></a>

The following is a time series data example in which the current table is provisioned at a higher read/write capacity and the older tables are scaled down because they are accessed infrequently.

![Table schema for high-volume time-series data.](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/images/TimeSeries.png)
