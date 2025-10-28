# Automatically identify nodes in your cluster (Memcached)

For clusters running the Memcached engine,
ElastiCache supports _Auto Discovery_—the ability for client
programs to automatically identify all of the nodes in a cluster, and to initiate and
maintain connections to all of these nodes.

###### Note

Auto Discovery is added for clusters running on Amazon ElastiCache Memcached. Auto Discovery is not available for Valkey or Redis OSS engines.

With Auto Discovery, your application does not need to manually connect to individual cache nodes;
instead, your application connects to one Memcached node and retrieves the list of nodes.
From that list your application is aware of the rest of the nodes in the cluster
and can connect to any of them.
You do not need to hard code the individual cache node endpoints in your application.

If you are using dual stack network type on your cluster, Auto Discovery will return only IPv4 or IPv6 addresses, depending on which one you select.
For more information, see [Choosing a network type in ElastiCache](network-type.md "network-type.md")
.

All of the cache nodes in the cluster maintain a list of metadata about all of the
other nodes. This metadata is updated whenever nodes are added or removed from the
cluster.

###### Topics

- [Benefits of Auto Discovery with Memcached](AutoDiscovery.md "AutoDiscovery.md")
- [How Auto Discovery Works](AutoDiscovery.md "AutoDiscovery.md")
- [Using Auto Discovery](AutoDiscovery.md "AutoDiscovery.md")
- [Connecting to Memcached Cache Nodes Manually](AutoDiscovery.md "AutoDiscovery.md")
- [Adding Auto Discovery to your Memcached client library](AutoDiscovery.md "AutoDiscovery.md")
- [ElastiCache clients with auto discovery](Clients.md "Clients.md")
