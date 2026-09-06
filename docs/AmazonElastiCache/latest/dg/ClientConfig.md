

# Configuring ElastiCache clients
<a name="ClientConfig"></a>

An ElastiCache cluster is protocol-compliant with Valkey, Memcached, and Redis OSS. The code, applications, and most popular tools that you use today with your existing environment will work seamlessly with the service.

This section discusses specific considerations for connecting to cache nodes in ElastiCache.

**Topics**
+ [Restricted commands](ClientConfig.RestrictedCommands.md)
+ [Finding node endpoints and port numbers](ClientConfig.FindingEndpointsAndPorts.md)
+ [Connecting for using auto discovery](ClientConfig.AutoDiscovery.md)
+ [Connecting to nodes in a Valkey or Redis OSS cluster](ClientConfig.ReplicationGroup.md)
+ [DNS names and underlying IP](ClientConfig.DNS.md)