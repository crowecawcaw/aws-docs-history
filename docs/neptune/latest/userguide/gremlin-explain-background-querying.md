# How Gremlin queries are processed in Neptune

In Amazon Neptune, more complex traversals can be represented by a series of patterns that
create a relation based on the definition of named variables that can be shared across
patterns to create joins. This is shown in the following example.

**Question: What is the two-hop neighborhood of vertex `v1`?**

```
  Gremlin code:      g.V(‘v1’).out('knows').out('knows').path()
  Pattern:           (?1=<v1>, <knows>, ?2, ?) X Pattern(?2, <knows>, ?3, ?)

  The pattern produces a three-column relation (?1, ?2, ?3) like this:
                     ?1     ?2     ?3
                     ================
                     v1     v2     v3
                     v1     v2     v4
                     v1     v5     v6
```

By sharing the `?2` variable across the two patterns (at the O position in the
first pattern and the S position of the second pattern), you create a join from the first hop
neighbors to the second hop neighbors. Each Neptune solution has bindings for the three
named variables, which can be used to re-create a [TinkerPop
Traverser](http://tinkerpop.apache.org/docs/current/reference/#_the_traverser "http://tinkerpop.apache.org/docs/current/reference/#_the_traverser") (including path information).

The first step in Gremlin query processing is to parse the query into a TinkerPop [Traversal](http://tinkerpop.apache.org/docs/current/reference/#traversal "http://tinkerpop.apache.org/docs/current/reference/#traversal")
object, composed of a series of TinkerPop [steps](http://tinkerpop.apache.org/docs/current/reference/#graph-traversal-steps "http://tinkerpop.apache.org/docs/current/reference/#graph-traversal-steps").
These steps, which are part of the open-source [Apache TinkerPop project](http://tinkerpop.apache.org/ "http://tinkerpop.apache.org/"), are both the logical and physical operators that compose
a Gremlin traversal in the reference implementation. They are both used to represent the model
of the query. They are executable operators that can produce solutions according to the
semantics of the operator that they represent. For example, `.V()` is both
represented and executed by the TinkerPop [GraphStep](http://tinkerpop.apache.org/docs/current/reference/#graph-step "http://tinkerpop.apache.org/docs/current/reference/#graph-step").

Because these off-the-shelf TinkerPop steps are executable, such a TinkerPop Traversal can
execute any Gremlin query and produce the correct answer. However, when executed against a
large graph, TinkerPop steps can sometimes be very inefficient and slow. Instead of using
them, Neptune tries to convert the traversal into a declarative form composed of groups of
patterns, as described previously.

Neptune doesn't currently support all Gremlin operators (steps) in its native query
engine. So it tries to collapse as many steps as possible down into a single
`NeptuneGraphQueryStep`, which contains the declarative logical query plan for
all the steps that have been converted. Ideally, all steps are converted. But when a step is
encountered that can't be converted, Neptune breaks out of native execution and defers all
query execution from that point forward to the TinkerPop steps. It doesn't try to weave in and
out of native execution.

After the steps are translated into a logical query plan, Neptune runs a series of query
optimizers that rewrite the query plan based on static analysis and estimated cardinalities.
These optimizers do things like reorder operators based on range counts, prune unnecessary or
redundant operators, rearrange filters, push operators into different groups, and so
on.

After an optimized query plan is produced, Neptune creates a pipeline of physical
operators that do the work of executing the query. This includes reading data from the
statement indices, performing joins of various types, filtering, ordering, and so on. The
pipeline produces a solution stream that is then converted back into a stream of TinkerPop
Traverser objects.

## Serialization of query results

Amazon Neptune currently relies on the TinkerPop response message serializers to convert
query results (TinkerPop Traversers) into the serialized data to be sent over the wire back
to the client. These serialization formats tend to be quite verbose.

For example, to serialize the result of a vertex query such as
`g.V().limit(1)`, the Neptune query engine must perform a single search to
produce the query result. However, the `GraphSON` serializer would perform a
large number of additional searches to package the vertex into the serialization format. It
would have to perform one search to get the label, one to get the property keys, and one
search per property key for the vertex to get all the values for each key.

Some of the serialization formats are more efficient, but all require additional
searches. Additionally, the TinkerPop serializers don't try to avoid duplicated searches,
often resulting in many searches being repeated unnecessarily.

This makes it very important to write your queries so that they ask specifically
just for the information they need. For example, `g.V().limit(1).id()` would
return just the vertex ID and eliminate all the additional serializer searches. The [Gremlin profile API in Neptune](gremlin-profile-api.md "gremlin-profile-api.md") allows you to see
how many search calls are made during query execution and during serialization.
