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
| `1.1.0.0 and older`    | `(deprecated)`            | `(deprecated)`            |

TinkerPop clients are usually backwards compatible within a series (`3.6.x`,
for example, or `3.7.x`) and while they can often work across those boundaries,
the table above recommends the version combinations to use for the best possible experience
and compatibility. Unless otherwise advised, it is generally best to adhere to these guidelines
and upgrade client applications to match the version of TinkerPop you are using.

When upgrading TinkerPop versions it is always important to refer to [TinkerPop's upgrade
recommendation](http://tinkerpop.apache.org/docs/current/upgrade/ "http://tinkerpop.apache.org/docs/current/upgrade/") which will help you identify new features you can take advantage of,
but also issues you may need to be aware of as you approach your upgrade. You should typically
expect existing queries and features to work after upgrade unless something in particular is
called out as a breaking change. Finally, it is important to note that should a version you
upgrade to have a new feature, you may not be able to use it if it is from a version later than
what Neptune supports.

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
