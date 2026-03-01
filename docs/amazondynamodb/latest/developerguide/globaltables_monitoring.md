# Monitoring global tables

###### Important

This documentation is for version 2017.11.29 (Legacy) of global tables, which
should be avoided for new global tables. Customers should use [Global Tables version 2019.11.21 (Current)](GlobalTables.md "GlobalTables.md") when possible,
as it provides greater flexibility, higher efficiency and consumes less write capacity than
2017.11.29 (Legacy).

To determine which version you are using, see [Determining the version of a global table](V2globaltables_versions.md#globaltables.DetermineVersion "V2globaltables_versions.md#globaltables.DetermineVersion").
To update existing global tables from version 2017.11.29 (Legacy) to version 2019.11.21 (Current), see
[DynamoDB global tables versions](V2globaltables_versions.md "V2globaltables_versions.md").

You can use Amazon CloudWatch to monitor the behavior and performance of a global table. Amazon DynamoDB
publishes `ReplicationLatency` and `PendingReplicationCount` metrics
for each replica in the global table.

- **`ReplicationLatency`**—The elapsed
  time between when an updated item appears in the DynamoDB stream for one replica table,
  and when that item appears in another replica in the global table.
  `ReplicationLatency` is expressed in milliseconds and is emitted for
  every source- and destination-Region pair.

During normal operation, `ReplicationLatency` should be fairly
constant. An elevated value for `ReplicationLatency` could indicate that
updates from one replica are not propagating to other replica tables in a timely
manner. Over time, this could result in other replica tables _falling
behind_ because they no longer receive updates consistently. In this
case, you should verify that the read capacity units (RCUs) and write capacity units
(WCUs) are identical for each of the replica tables. In addition, when choosing WCU
settings, follow the recommendations in [Global tables version](globaltables_reqs_bestpractices.md#globaltables_reqs_bestpractices.tables "globaltables_reqs_bestpractices.md#globaltables_reqs_bestpractices.tables").

`ReplicationLatency` can increase if an AWS Region becomes degraded and
you have a replica table in that Region. In this case, you can temporarily redirect
your application's read and write activity to a different AWS Region.

- **`PendingReplicationCount`**—The number of item updates
  that are written to one replica table, but that have not yet been written to another
  replica in the global table. `PendingReplicationCount` is expressed in
  number of items and is emitted for every source- and destination-Region pair.

During normal operation, `PendingReplicationCount` should be very low.
If `PendingReplicationCount` increases for extended periods, investigate
whether your replica tables' provisioned write capacity settings are sufficient for
your current workload.

`PendingReplicationCount` can increase if an AWS Region becomes
degraded and you have a replica table in that Region. In this case, you can
temporarily redirect your application's read and write activity to a different AWS
Region.

For more information, see
[DynamoDB Metrics and dimensions](metrics-dimensions.md "metrics-dimensions.md").
