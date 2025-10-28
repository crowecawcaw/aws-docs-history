# Multi-Region replication for Amazon Keyspaces (for Apache Cassandra)

You can use Amazon Keyspaces multi-Region replication to replicate your data with automated, fully managed, _active-active_ replication across the AWS Regions of your
choice. With active-active replication, each Region is able to perform reads and writes in
isolation. You can improve both availability and resiliency from Regional degradation, while
also benefiting from low-latency local reads and writes for global applications.

With multi-Region replication, Amazon Keyspaces asynchronously replicates data between Regions, and data is typically
propagated across Regions within a second. Also, with multi-Region replication, you no longer have the
difficult work of resolving conflicts and correcting data divergence issues, so you can
focus on your application.

By default, Amazon Keyspaces replicates data across three [Availability
Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") within the same AWS Region for durability and high availability. With
multi-Region replication, you can create multi-Region keyspaces that replicate your tables in
different geographic AWS Regions of your choice.

###### Topics

- [Benefits of using multi-Region replication](#mrr-benefits "#mrr-benefits")
- [Capacity modes and pricing](#mrr-pricing "#mrr-pricing")
- [How multi-Region replication works in Amazon Keyspaces](multiRegion-replication_how-it-works.md "multiRegion-replication_how-it-works.md")
- [Amazon Keyspaces multi-Region replication usage notes](multiRegion-replication_usage-notes.md "multiRegion-replication_usage-notes.md")
- [Configure multi-Region replication for Amazon Keyspaces (for Apache Cassandra)](multiRegion-replication-configure.md "multiRegion-replication-configure.md")

## Benefits of using multi-Region replication

Multi-Region replication provides the following benefits.

- Global reads and writes with single-digit millisecond
  latency – In Amazon Keyspaces, replication is active-active. You can serve both reads and writes
  locally from the Regions closest to your customers with single-digit millisecond
  latency at any scale. You can use Amazon Keyspaces multi-Region tables for global applications
  that need a fast response time anywhere in the world.
- Improved business continuity and protection from
  single-Region degradation – With multi-Region replication, you can recover from degradation in a single AWS Region by
  redirecting your application to a different Region in your multi-Region keyspace.
  Because Amazon Keyspaces offers active-active replication, there is no impact to your reads and
  writes.

Amazon Keyspaces keeps track of any writes that have been performed on your multi-Region
keyspace but haven't been propagated to all replica Regions. After the Region comes
back online, Amazon Keyspaces automatically syncs any missing changes so that you can recover
without any application impact.

- High-speed replication across Regions –
  Multi-Region replication uses fast, storage-based physical replication of data across Regions, with a
  replication lag that is typically less than 1 second.

Replication in Amazon Keyspaces has little to no impact on your database queries because it
doesn’t share compute resources with your application. This means that you can
address high-write throughput use cases or use cases with sudden spikes or bursts in
throughput without any application impact.

- Consistency and conflict resolution –
  Any changes made to data in any Region are replicated to the other Regions in a
  multi-Region keyspace. If applications update the same data in different Regions at
  the same time, conflicts can arise.

To help provide eventual consistency, Amazon Keyspaces uses cell-level timestamps and a
_last writer wins_ reconciliation between concurrent updates.
Conflict resolution is fully managed and happens in the background without any
application impact.

For more information about supported configurations and features, see [Amazon Keyspaces multi-Region replication usage notes](multiRegion-replication_usage-notes.md "multiRegion-replication_usage-notes.md").

## Capacity modes and pricing

For a multi-Region keyspace, you can either use _on-demand capacity
mode_ or _provisioned capacity mode_. For
more information, see [Configure read/write capacity modes in Amazon Keyspaces](ReadWriteCapacityMode.md "ReadWriteCapacityMode.md").

For on-demand mode, you're billed 1 write request unit (WRU) to write up to 1 KB of
data per row the same way as for single-Region tables. But you're billed for writes in each Region of your multi-Region keyspace. For
example, writing a row of 3 KB of data in a multi-Region keyspace with two Regions requires
6 WRUs: 3 \* 2 = 6 WRUs. Additionally, writes that include both static and
non-static data require additional write operations.

For provisioned mode, you're billed 1 write capacity unit (WCU) to write up to 1 KB
of data per row, the same way as for single-Region tables. But you're billed for writes in each Region of your multi-Region keyspace. For
example, writing a row of 3 KB of data per second in a multi-Region keyspace with two
Regions requires 6 WCUs: 3 \* 2 = 6 WCUs. Additionally, writes that include both
static and non-static data require additional write operations.

For more information about pricing, see [Amazon Keyspaces (for Apache Cassandra) pricing](https://aws.amazon.com/keyspaces/pricing "https://aws.amazon.com/keyspaces/pricing").
