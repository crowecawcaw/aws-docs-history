# Configure provisioned capacity

mode

If you choose _provisioned throughput_ capacity mode, you
specify the number of reads and writes per second that are required for your
application. This helps you manage your Amazon Keyspaces usage to stay at or below a defined
request rate to maintain predictability. To learn more about
automatic scaling for provisioned throughput see [Manage throughput capacity automatically with Amazon Keyspaces auto scaling](autoscaling.md "autoscaling.md").

Provisioned throughput capacity mode is a good option if any of the following is
true:

- You have predictable application traffic.
- You run applications whose traffic is consistent or ramps up gradually.
- You can forecast capacity requirements.

## Read capacity units

and write capacity units

For provisioned throughput capacity mode tables, you specify throughput
capacity in terms of read capacity units (RCUs) and write capacity units (WCUs):

- One _RCU_ represents one `LOCAL_QUORUM`
  read per second, or two `LOCAL_ONE` reads per second, for a
  row up to 4 KB in size. If you need to read a row that is larger than
  4 KB, the read operation uses additional RCUs.

The total number of RCUs required depends on the row size, and whether
you want `LOCAL_QUORUM` or `LOCAL_ONE` reads. For
example, if your row size is 8 KB, you require 2 RCUs to sustain one
`LOCAL_QUORUM` read per second, and 1 RCU if you choose
`LOCAL_ONE` reads.

- One _WCU_ represents one write per second for a row
  up to 1 KB in size. All writes are using
  `LOCAL_QUORUM` consistency, and there is no additional
  charge for using lightweight transactions (LWTs). If you need to write a
  row that is larger than 1 KB, the write operation uses
  additional WCUs.

The total number of WCUs required depends on the row size. For
example, if your row size is 2 KB, you require 2 WCUs to sustain one
write request per second. For more information about how to estimate read and write capacity consumption of a table, see
[Estimate capacity consumption of read and write throughput in Amazon Keyspaces](capacity-examples.md "capacity-examples.md").

If your application reads or writes larger rows (up to the Amazon Keyspaces maximum row
size of 1 MB), it consumes more capacity units. To learn more about
how to estimate the row size, see [Estimate row size in Amazon Keyspaces](calculating-row-size.md "calculating-row-size.md"). For
example, suppose that you create a provisioned table with 6 RCUs and 6 WCUs.
With these settings, your application could do the following:

- Perform `LOCAL_QUORUM` reads of up to 24 KB per second
  (4 KB × 6 RCUs).
- Perform `LOCAL_ONE` reads of up to 48 KB per second (twice
  as much read throughput).
- Write up to 6 KB per second (1 KB × 6 WCUs).

_Provisioned throughput_ is the maximum amount of throughput
capacity an application can consume from a table. If your application exceeds
your provisioned throughput capacity, you might observe insufficient capacity
errors.

For example, a read request that doesn’t have enough throughput capacity fails
with a `Read_Timeout` exception and is posted to the
`ReadThrottleEvents` metric. A write request that doesn’t have
enough throughput capacity fails with a `Write_Timeout` exception and
is posted to the `WriteThrottleEvents` metric.

You can use Amazon CloudWatch to monitor your provisioned and actual throughput metrics
and insufficient capacity events. For more information about these metrics, see
[Amazon Keyspaces metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").

###### Note

Repeated errors due to insufficient capacity can lead to client-side
driver specific exceptions, for example the DataStax Java driver fails with
a `NoHostAvailableException`.

To change the throughput capacity settings for tables, you can use the
AWS Management Console or the `ALTER TABLE` statement using CQL, for more
information see [ALTER TABLE](cql.ddl.md#cql.ddl.table.alter "cql.ddl.md#cql.ddl.table.alter").

To learn more about default quotas for your account and how to increase them,
see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").
