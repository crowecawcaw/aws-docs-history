# Estimate capacity throughput requirements for read/write operations on static

data in Amazon Keyspaces

Static data is associated with logical partitions in Cassandra, not individual
rows. Logical partitions in Amazon Keyspaces can be virtually unbound in size by spanning
across multiple physical storage partitions. As a result, Amazon Keyspaces meters write
operations on static and nonstatic data separately. Furthermore, writes that include
both static and nonstatic data require additional underlying operations to provide
data consistency.

If you perform a mixed write operation of both static and nonstatic data, this
results in two separate write operations—one for nonstatic and one for static
data. This applies to both on-demand and provisioned read/write capacity
modes.

The following example provides details about how to estimate the required read
capacity units (RCUs) and write capacity units (WCUs) when you're calculating
provisioned throughput capacity requirements for tables in Amazon Keyspaces that have static
columns. You can estimate how much capacity your table needs to process writes that
include both static and nonstatic data by using the following formula:

```
2 x WCUs required for nonstatic data + 2 x WCUs required for static data
```

For example, if your application writes 27 KBs of data per second and each write
includes 25.5 KBs of nonstatic data and 1.5 KBs of static data, then your table
requires 56 WCUs (2 x 26 WCUs + 2 x 2 WCUs).

Amazon Keyspaces meters the reads of static and nonstatic data the same as reads of multiple
rows. As a result, the price of reading static and nonstatic data in the same
operation is based on the aggregate size of the data processed to perform the
read.

To learn how to monitor serverless resources with Amazon CloudWatch, see [Monitoring Amazon Keyspaces with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
