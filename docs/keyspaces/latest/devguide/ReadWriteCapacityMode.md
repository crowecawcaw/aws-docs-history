# Configure on-demand capacity mode

Amazon Keyspaces (for Apache Cassandra) _on-demand_ capacity mode is a flexible billing
option capable of serving thousands of requests per second without capacity
planning. This option offers pay-per-request pricing for read and write requests so
that you pay only for what you use.

When you choose on-demand mode, Amazon Keyspaces can scale the throughput capacity for your
table up to any previously reached traffic level instantly, and then back down when
application traffic decreases. If a workload’s traffic level hits a new peak, the
service adapts rapidly to increase throughput capacity for your table. You can
enable on-demand capacity mode for both new and existing tables.

On-demand mode is a good option if any of the following is true:

- You create new tables with unknown workloads.
- You have unpredictable application traffic.
- You prefer the ease of paying for only what you use.
  To get started with on-demand mode, you can create a new table or update an
  existing table to use on-demand capacity mode using the console or with a few lines
  of Cassandra Query Language (CQL) code. For more information, see [Tables](cql.ddl.md "cql.ddl.md").

###### Topics

- [Read request units and write
  request units](#ReadWriteCapacityMode.requests "#ReadWriteCapacityMode.requests")
- [Peak traffic and scaling
  properties](#ReadWriteCapacityMode.PeakTraffic "#ReadWriteCapacityMode.PeakTraffic")
- [Initial throughput for
  on-demand capacity mode](#ReadWriteCapacityMode.InitialThroughput "#ReadWriteCapacityMode.InitialThroughput")

## Read request units and write

request units

With on-demand capacity mode tables, you don't need to specify how much read
and write throughput you expect your application to use in advance. Amazon Keyspaces
charges you for the reads and writes that you perform on your tables in terms of
read request units (RRUs) and write request units (WRUs).

- One _RRU_ represents one `LOCAL_QUORUM`
  read request, or two `LOCAL_ONE` read requests, for a row up
  to 4 KB in size. If you need to read a row that is larger than
  4 KB, the read operation uses additional RRUs. The total number
  of RRUs required depends on the row size, and whether you want to use
  `LOCAL_QUORUM` or `LOCAL_ONE` read
  consistency. For example, reading an 8 KB row requires 2 RRUs using
  `LOCAL_QUORUM` read consistency, and 1 RRU if you choose
  `LOCAL_ONE` read consistency.
- One _WRU_ represents one write for a row up to
  1 KB in size. All writes are using `LOCAL_QUORUM`
  consistency, and there is no additional charge for using lightweight
  transactions (LWTs). If you need to write a row that is larger than
  1 KB, the write operation uses additional WRUs. The total number
  of WRUs required depends on the row size. For example, if your row size
  is 2 KB, you require 2 WRUs to perform one write request.

For information about supported consistency levels, see [Supported Apache Cassandra read and write consistency levels and associated costs](consistency.md "consistency.md").

## Peak traffic and scaling

properties

Amazon Keyspaces tables that use on-demand capacity mode automatically adapt to your
application’s traffic volume. On-demand capacity mode instantly accommodates up
to double the previous peak traffic on a table. For example, your application's
traffic pattern might vary between 5,000 and 10,000 `LOCAL_QUORUM`
reads per second, where 10,000 reads per second is the previous traffic peak.

With this pattern, on-demand capacity mode instantly accommodates sustained
traffic of up to 20,000 reads per second. If your application sustains traffic
of 20,000 reads per second, that peak becomes your new previous peak, enabling
subsequent traffic to reach up to 40,000 reads per second.

If you need more than double your previous peak on a table, Amazon Keyspaces
automatically allocates more capacity as your traffic volume increases. This
helps ensure that your table has enough throughput capacity to process the
additional requests. However, you might observe insufficient throughput capacity
errors if you exceed double your previous peak within 30 minutes.

For example, suppose that your application's traffic pattern varies between
5,000 and 10,000 strongly consistent reads per second, where 20,000 reads per
second is the previously reached traffic peak. In this case, the service
recommends that you space your traffic growth over at least 30 minutes before
driving up to 40,000 reads per second.

To learn how to estimate read and write capacity consumption of a table, see
[Estimate capacity consumption of read and write throughput in Amazon Keyspaces](capacity-examples.md "capacity-examples.md").

To learn more about default quotas for your account and how to increase them,
see [Quotas for Amazon Keyspaces (for Apache Cassandra)](quotas.md "quotas.md").

## Initial throughput for

on-demand capacity mode

If you create a new table with on-demand capacity mode enabled or switch an
existing table to on-demand capacity mode for the first time, the table has the
following previous peak settings, even though it hasn't served traffic
previously using on-demand capacity mode:

- **Newly created table with on-demand capacity
  mode:** The previous peak is 2,000 WRUs and 6,000 RRUs. You
  can drive up to double the previous peak immediately. Doing this enables
  newly created on-demand tables to serve up to 4,000 WRUs and 12,000
  RRUs.
- **Existing table switched to on-demand capacity
  mode:** The previous peak is half the previous WCUs and
  RCUs provisioned for the table or the settings for a newly created table
  with on-demand capacity mode, whichever is higher.
