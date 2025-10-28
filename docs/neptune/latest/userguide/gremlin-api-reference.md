# Using the Gremlin API with Amazon Neptune

###### Note

Amazon Neptune does not support the `bindings` property.

Gremlin HTTPS requests all use a single endpoint: `https://`your-neptune-endpoint`:`port`/gremlin`.
All Neptune connections must use HTTPS.

You can connect the Gremlin Console to a Neptune graph directly through WebSockets.

For more information about connecting to the Gremlin endpoint, see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

The Amazon Neptune implementation of Gremlin has specific details and differences that you
need to consider. For more information, see [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md "access-graph-gremlin-differences.md").

For information about the Gremlin language and traversals, see [The
Traversal](https://tinkerpop.apache.org/docs/current/reference/#traversal "https://tinkerpop.apache.org/docs/current/reference/#traversal") in the Apache TinkerPop documentation.
