

# Failure scenarios
<a name="Durability.FailureScenarios"></a>

If a primary node fails, ElastiCache automatically triggers a failover to a replica, and the new primary takes over write operations. The failed primary is replaced and syncs data from the Multi-AZ transactional log. With synchronous writes, this process ensures no data loss. With asynchronous writes, up to 10 seconds of uncommitted data can be lost during the failover. If a read replica fails, the failed node is replaced and syncs data from the Multi-AZ transactional log regardless of the durability option selected.

When all nodes in a shard fail, all nodes are replaced and sync data from the Multi-AZ transactional log at the same time. With synchronous writes, this process ensures no data loss. With asynchronous writes, up to 10 seconds of uncommitted data can be lost. After committed data is restored, one of the replaced nodes will automatically be elected as the new primary with other nodes as replicas.