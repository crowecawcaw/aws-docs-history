# DNS names and underlying IP

Clients maintain a server list containing the addresses and ports of
the servers holding the cache data. When using ElastiCache, the DescribeCacheClusters API
(or the describe-cache-clusters command line utility) returns a fully
qualified DNS entry and port number that can be used for the server list.

###### Important

It is important that client applications are configured to frequently
resolve DNS names of cache nodes when they attempt to connect to a cache
node endpoint.

ElastiCache ensures that the DNS name of cache nodes remain the same when cache
nodes are recovered in case of failure.

Most client libraries support persistent cache node connections by
default. We recommend using persistent cache node connections when using ElastiCache.
Client-side DNS caching can occur in multiple places, including client libraries,
the language runtime, or the client operating system. You should review your
application configuration at each layer to ensure that you are frequently resolving
IP addresses for your cache nodes.
