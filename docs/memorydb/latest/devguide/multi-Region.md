# Monitoring MemoryDB Multi-Region

You can use Amazon CloudWatch to monitor the behavior and performance of a Multi-Region cluster. MemoryDB publishes the `MultiRegionClusterReplicationLag` metric for each regional cluster within the Multi-Region cluster.

`MultiRegionClusterReplicationLag` shows the elapsed time between when an update is written to the remote Multi-Region regional cluster multi-AZ transaction log, and when that update is written to the primary node in the local Multi-Region regional cluster. This metric is expressed in milliseconds, is emitted for every source- and destination-Region pair at shard level.

During normal operation, `MultiRegionClusterReplicationLag` should be fairly constant. An elevated value for `MultiRegionClusterReplicationLag` could indicate that updates from one regional cluster are not propagating to other regional clusters in a timely manner. Over time, this could result in other regional clusters _falling behind_ because they no longer receive updates consistently.

`MultiRegionClusterReplicationLag` can increase if an AWS Region becomes isolated or degraded and you have a regional cluster in that Region. In this case, you can temporarily redirect your application's read and write activity to a different healthy AWS Region.
