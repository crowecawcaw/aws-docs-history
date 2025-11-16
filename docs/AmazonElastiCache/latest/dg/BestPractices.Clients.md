# Best practices for clients (Valkey and Redis OSS)

Learn best practices for common scenarios and follow along with code examples of some of the most popular open source Valkey and Redis OSS client libraries
(redis-py, PHPRedis, and Lettuce), as well as best practices for interacting with ElastiCache resources with commonly used open-source Memcached client libraries.

###### Topics

- [Large number of connections (Valkey and Redis OSS)](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Cluster client discovery and exponential backoff (Valkey and Redis OSS)](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Configure a client-side timeout (Valkey and Redis OSS)](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Configure a server-side idle timeout (Valkey and Redis OSS)](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Lua scripts](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Storing large composite items (Valkey and Redis OSS)](BestPractices.Clients.Redis.md "BestPractices.Clients.Redis.md")
- [Lettuce client configuration (Valkey and Redis OSS)](BestPractices.md "BestPractices.md")
- [Configuring a preferred protocol for dual stack clusters (Valkey and Redis OSS)](#network-type-configuring-dual-stack-redis "#network-type-configuring-dual-stack-redis")

## Configuring a preferred protocol for dual stack clusters (Valkey and Redis OSS)

For cluster mode enabled Valkey or Redis OSS clusters, you can control the protocol clients will use to connect to the nodes in the cluster with the
IP Discovery parameter. The IP Discovery parameter can be set to either IPv4 or IPv6.

For Valkey or Redis OSS clusters, the IP discovery parameter sets the IP protocol used in the [cluster slots ()](https://valkey.io/commands/cluster-slots/ "https://valkey.io/commands/cluster-slots/"),
[cluster shards ()](https://valkey.io/commands/cluster-shards/ "https://valkey.io/commands/cluster-shards/"),
and [cluster nodes ()](https://valkey.io/commands/cluster-nodes/ "https://valkey.io/commands/cluster-nodes/") output.
These commands are used by clients to discover the cluster topology. Clients use the IPs in theses commands
to connect to the other nodes in the cluster.

Changing the IP Discovery will not result in any downtime for connected clients. However, the changes will take some time to propagate.
To determine when the changes have completely propagated for a Valkey or Redis OSS Cluster,
monitor the output of `cluster slots`. Once all of the nodes returned by the cluster slots command report IPs with
the new protocol the changes have finished propagating.

Example with Redis-Py:

```
cluster = RedisCluster(host="xxxx", port=6379)
target_type = IPv6Address # Or IPv4Address if changing to IPv4

nodes = set()
while len(nodes) == 0 or not all((type(ip_address(host)) is target_type) for host in nodes):
    nodes = set()

   # This refreshes the cluster topology and will discovery any node updates.
   # Under the hood it calls cluster slots
    cluster.nodes_manager.initialize()
    for node in cluster.get_nodes():
        nodes.add(node.host)
    self.logger.info(nodes)

    time.sleep(1)
```

Example with Lettuce:

```
RedisClusterClient clusterClient = RedisClusterClient.create(RedisURI.create("xxxx", 6379));

Class targetProtocolType = Inet6Address.class; // Or Inet4Address.class if you're switching to IPv4

Set<String> nodes;

do {
   // Check for any changes in the cluster topology.
   // Under the hood this calls cluster slots
    clusterClient.refreshPartitions();
    Set<String> nodes = new HashSet<>();

    for (RedisClusterNode node : clusterClient.getPartitions().getPartitions()) {
        nodes.add(node.getUri().getHost());
    }

    Thread.sleep(1000);
} while (!nodes.stream().allMatch(node -> {
            try {
                return finalTargetProtocolType.isInstance(InetAddress.getByName(node));
            } catch (UnknownHostException ignored) {}
            return false;
}));
```
