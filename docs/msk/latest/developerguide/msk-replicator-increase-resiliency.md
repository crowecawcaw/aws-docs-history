# Use replication to increase the resiliency of a

Kafka streaming application across Regions

You can use MSK Replicator to set up active-active or active-passive cluster topologies to increase resiliency of your Apache Kafka application across AWS Regions. In an active-active setup, both MSK clusters are actively serving reads and writes. In an active-passive setup, only one MSK cluster at a time is actively serving streaming data, while the other cluster is on standby.

## Considerations for building

multi-Region Apache Kafka applications

Your consumers must be able to reprocess duplicate messages without downstream
impact. MSK Replicator replicates data at-least-once which may result in duplicates
in the standby cluster. When you switch over to the secondary AWS Region, your
consumers may process the same data more than once. MSK Replicator prioritizes
copying data over consumer offsets for better performance. After a failover, the
consumer may start reading from earlier offsets resulting in duplicate
processing.

Producers and consumers must also tolerate losing minimal data. Since MSK
Replicator replicates data asynchronously, when the primary AWS Region starts
experiencing failures, there is no guarantee that all data is replicated to the
secondary Region. You can use the replication latency to determine maximum data that
was not copied into the secondary Region.

## Using active-active versus active-passive cluster topology

An active-active cluster topology offers near zero recovery time and the
capability for your streaming application to operate simultaneously in multiple
AWS Regions. When a cluster in one Region is impaired, applications connected
to the cluster in the other Region continue processing data.

Active-passive setups are suited to applications that can run in only one
AWS Region at a time, or when you need more control over the data processing
order. Active-passive setups require more recovery time than active-active
setups, as you must start your entire active-passive setup, including your
producers and consumers, in the secondary Region to resume streaming data after
a failover.
