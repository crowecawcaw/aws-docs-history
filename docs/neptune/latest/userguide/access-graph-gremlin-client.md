# Java-based Gremlin clients to use with Amazon Neptune

You can use either of two open-source Java-based Gremlin clients with Amazon Neptune:
the [Apache
TinkerPop Java Gremlin client](https://search.maven.org/artifact/org.apache.tinkerpop/gremlin-driver "https://search.maven.org/artifact/org.apache.tinkerpop/gremlin-driver"), or the [Gremlin
client for Amazon Neptune](https://search.maven.org/artifact/software.amazon.neptune/gremlin-client "https://search.maven.org/artifact/software.amazon.neptune/gremlin-client").

## Apache TinkerPop Java Gremlin client

The Apache TinkerPop Java [gremlin-driver](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java "https://tinkerpop.apache.org/docs/current/reference/#gremlin-java")
is the standard, official Gremlin client that works with any TinkerPop-enabled graph database.
Use this client when you need maximum compatibility with the broader TinkerPop development space,
when you're working with multiple graph database systems, or when you don't require the advanced
cluster management and load balancing features specific to Neptune. This client is also suitable
for simple applications that connect to a single Neptune instance or when you prefer to handle
load balancing at the infrastructure level rather than within the client.

###### Important

Choosing the correct Apache TinkerPop Gremlin driver version is critical for compatibility
with your Neptune engine version. Using an incompatible version can result in connection
failures or unexpected behavior. For detailed version compatibility information, see
[Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

###### Note

The table that helps you determine the correct Apache TinkerPop version to use with Neptune
has been moved to [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md"). This table was previously located
on this page for many years and is now more centralized for reference for all programming
languages that TinkerPop supports.

## Gremlin Java client for Amazon Neptune

The Gremlin client for Amazon Neptune is an [open-source
Java-based Gremlin client](https://github.com/aws/neptune-gremlin-client "https://github.com/aws/neptune-gremlin-client") that acts as a drop-in replacement for the standard
TinkerPop Java client.

The Neptune Gremlin client is optimized for Neptune clusters. It lets you manage
traffic distribution across multiple instances in a cluster, and adapts to changes in cluster
topology when you add or remove a replica. You can even configure the client to
distribute requests across a subset of instances in your cluster, based on role,
instance type, availability zone (AZ), or tags associated with instances.

The [latest
version of the Neptune Gremlin Java client](https://search.maven.org/artifact/software.amazon.neptune/gremlin-client "https://search.maven.org/artifact/software.amazon.neptune/gremlin-client") is available on Maven Central.

For more information about the Neptune Gremlin Java client, see [this
blog post](https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/ "https://aws.amazon.com/blogs/database/load-balance-graph-queries-using-the-amazon-neptune-gremlin-client/"). For code samples and demos, check out the [client's GitHub project](https://github.com/aws/neptune-gremlin-client "https://github.com/aws/neptune-gremlin-client").

When choosing the version of the Neptune Gremlin client, you need to consider the
underlying TinkerPop version in relation to your Neptune engine version. Refer to the
compatibility table at [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md") to determine the correct
TinkerPop version for your Neptune engine, then use the following table to select
the appropriate Neptune Gremlin client version:

| Neptune Gremlin client version compatibility | Neptune Gremlin client version   | TinkerPop version |
| -------------------------------------------- | -------------------------------- | ----------------- |
| 3.x                                          | 3.7.x (AWS SDK for Java 2.x/1.x) |
| 2.1.x                                        | 3.7.x (AWS SDK for Java 1.x)     |
| 2.0.x                                        | 3.6.x                            |
| 1.12                                         | 3.5.x                            |
