

# Best practices using the Gremlin Java client with Neptune
<a name="best-practices-gremlin-java-client"></a>

Follow these recommendations when using the Gremlin Java client with Neptune. These best practices help you optimize performance, manage connections effectively, and avoid common pitfalls when working with the Java driver.

For information about configuring heartbeat intervals for Neptune Serverless, see [Heartbeat Configuration for Neptune Serverless](best-practices-gremlin-heartbeat-serverless.md).

**Topics**
+ [Re-use the client object across multiple threads](best-practices-gremlin-java-reuse.md)
+ [Create separate Gremlin Java client objects for read and write endpoints](best-practices-gremlin-java-separate.md)
+ [Add multiple read replica endpoints to a Gremlin Java connection pool](best-practices-gremlin-java-multiple.md)
+ [Close the client to avoid the connections limit](best-practices-gremlin-java-close-connections.md)
+ [Create a new connection after failover](best-practices-gremlin-java-new-connection.md)
+ [Set `maxInProcessPerConnection` and `maxSimultaneousUsagePerConnection` to the same value](best-practices-gremlin-java-maxes.md)
+ [Send queries to the server as bytecode rather than as strings](best-practices-gremlin-java-bytecode.md)
+ [Always completely consume the ResultSet or Iterator returned by a query](best-practices-gremlin-java-resultset.md)
+ [Bulk add vertices and edges in batches](best-practices-gremlin-java-batch-add.md)
+ [Disable DNS caching in the Java Virtual Machine](best-practices-gremlin-java-disable-dns-caching.md)
+ [Optionally, set timeouts at a per-query level](best-practices-gremlin-java-per-query-timeout.md)
+ [Troubleshooting `java.util.concurrent.TimeoutException`](best-practices-gremlin-java-exceptions-TimeoutException.md)