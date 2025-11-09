# Java-based Gremlin clients to use with Amazon Neptune

You can use either of two open-source Java-based Gremlin clients with Amazon Neptune:
the [Apache
TinkerPop Java Gremlin client](https://search.maven.org/artifact/org.apache.tinkerpop/gremlin-driver "https://search.maven.org/artifact/org.apache.tinkerpop/gremlin-driver"), or the [Gremlin
client for Amazon Neptune](https://search.maven.org/artifact/software.amazon.neptune/gremlin-client "https://search.maven.org/artifact/software.amazon.neptune/gremlin-client").

## Apache TinkerPop Java Gremlin client

If you can, always use the latest version of the [Apache TinkerPop
Java Gremlin client](https://github.com/apache/tinkerpop/tree/master/gremlin-driver "https://github.com/apache/tinkerpop/tree/master/gremlin-driver") that your engine version supports. Newer versions contain
numerous bug fixes which can improves the stability, performance and usability of the client.

The table below lists the earliest and latest versions of TinkerPop client
supported by different Neptune engine versions:

| Neptune Engine Version | Minimum TinkerPop Version | Maximum TinkerPop Version |
| ---------------------- | ------------------------- | ------------------------- |
| `1.3.2.0 <= current`   | `3.7.1`                   | `3.7.3`                   |
| `1.3.1.0`              | `3.6.2`                   | `3.6.5`                   |
| `1.3.0.0`              | `3.6.2`                   | `3.6.4`                   |
| `1.2.1.0 <= 1.2.1.2`   | `3.6.2`                   | `3.6.2`                   |
| `1.1.1.0 <= 1.2.0.2`   | `3.5.5`                   | `3.5.6`                   |
| `1.1.0.0`              | `3.4.0`                   | `3.4.13`                  |
| `1.0.5.1 and older`    | `(deprecated)`            | `(deprecated)`            |

TinkerPop clients are usually backwards compatible within a series (`3.3.x`,
for example, or `3.4.x`). There are exceptional cases where backward
compatibility has to be broken, so it's best to check the
[TinkerPop
upgrade recommendation](http://tinkerpop.apache.org/docs/current/upgrade/ "http://tinkerpop.apache.org/docs/current/upgrade/") before upgrading to a new client version.

The client might not be able to use new steps or new features introduced in versions
later than what the server supports, but you can expect existing queries and features
to work unless the [upgrade
recommendation](http://tinkerpop.apache.org/docs/current/upgrade/ "http://tinkerpop.apache.org/docs/current/upgrade/") calls out a breaking change.

###### Note

Starting with [Neptune engine release 1.1.1.0](engine-releases-1.1.1.md "engine-releases-1.1.1.md")
don't use a TinkerPop version lower than `3.5.2`.

Python users should avoid using TinkerPop version `3.4.9`
because of a default timeout setting that requires direct configuration (see [TINKERPOP-2505](https://issues.apache.org/jira/browse/TINKERPOP-2505 "https://issues.apache.org/jira/browse/TINKERPOP-2505")).

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
