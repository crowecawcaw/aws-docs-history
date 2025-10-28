# Making efficient Gremlin upserts with `fold()/coalesce()/unfold()`

An upsert (or conditional insert) reuses a vertex or edge if it already exists,
or creates it if it doesn't. Efficient upserts can make a significant difference in
the performance of Gremlin queries.

This page shows how use the `fold()/coalesce()/unfold()` Gremlin pattern
to make efficient upserts. However, with the release of TinkerPop version 3.6.x
introduced in Neptune in engine version [1.2.1.0](engine-releases-1.2.1.md "engine-releases-1.2.1.md"),
the new `mergeV()` and `mergeE()` steps are preferable
in most cases. The `fold()/coalesce()/unfold()` pattern described
here may still be useful in a some complex situations, but in general use
`mergeV()` and `mergeE()` if you can, as described in
[Making efficient upserts with Gremlin
mergeV() and mergeE() steps](gremlin-efficient-upserts.md "gremlin-efficient-upserts.md").

Upserts allow you to write idempotent insert operations: no matter how many times
you run such an operation, the overall outcome is the same. This is useful in highly
concurrent write scenarios where concurrent modifications to the same part of the graph
can force one or more transactions to roll back with a `ConcurrentModificationException`,
thereby necessitating a retry.

For example, the following query upserts a vertex by first looking for the specified
vertex in the dataset, and then folding the results into a list. In the first traversal
supplied to the `coalesce()` step, the query then unfolds this list. If the
unfolded list is not empty, the results are emitted from the `coalesce()`.
If, however, the `unfold()` returns an empty collection because the vertex
does not currently exist, `coalesce()` moves on to evaluate the second
traversal with which it has been supplied, and in this second traversal the query creates
the missing vertex.

```
g.V('v-1').fold()
          .coalesce(
             unfold(),
             addV('Person').property(id, 'v-1')
                           .property('email', 'person-1@example.org')
           )
```

## Use an optimized form of `coalesce()` for upserts

Neptune can optimize the `fold().coalesce(unfold(), ...)` idiom to
make high-throughput updates, but this optimization only works if both parts of the
`coalesce()` return either a vertex or an edge but nothing else.
If you try to return something different, such as a property, from any part of
the `coalesce()`, the Neptune optimization does not occur. The query may
succeed, but it will not perform as well as an optimized version, particularly against
large datasets.

Because unoptimized upsert queries increase execution times and reduce throughput,
it's worth using the Gremlin `explain` endpoint to determine whether an upsert
query is fully optimized. When reviewing `explain` plans, look for lines that
begin with `+ not converted into Neptune steps` and `WARNING: >>`.
For example:

```
+ not converted into Neptune steps: [FoldStep, CoalesceStep([[UnfoldStep], [AddEdgeSte`...`
WARNING: >> FoldStep << is not supported natively yet
```

These warnings can help you identify the parts of a query that are preventing it from
being fully optimized.

Sometimes it isn't possible to optimize a query fully. In these situations you should
try to put the steps that cannot be optimized at the end of the query, thereby allowing
the engine to optimize as many steps as possible. This technique is used in some of the
batch upsert examples, where all optimized upserts for a set of vertices or edges are
performed before any additional, potentially unoptimized modifications are applied to
the same vertices or edges.

## Batching upserts to improve throughput

For high throughput write scenarios, you can chain upsert steps together to upsert
vertices and edges in batches. Batching reduces the transactional overhead of upserting
large numbers of vertices and edges. You can then further improve throughput by upserting
batch requests in parallel using multiple clients.

As a rule of thumb we recommend upserting approximately 200 records per batch request.
A record is a single vertex or edge label or property. A vertex with a single label and
4 properties, for example, creates 5 records. An edge with a label and a single property
creates 2 records. If you wanted to upsert batches of vertices, each with a single label
and 4 properties, you should start with a batch size of 40, because `200 / (1 + 4)
 = 40`.

You can experiment with the batch size. 200 records per batch is a good starting
point, but the ideal batch size may be higher or lower depending on your workload.
Note, however, that Neptune may limit the overall number of Gremlin steps per request.
This limit is not documented, but to be on the safe side try to ensure that your
requests contain no more than 1500 Gremlin steps. Neptune may reject large batch
requests with more than 1500 steps.

To increase throughput, you can upsert batches in parallel using multiple clients
(see [Creating Efficient Multithreaded
Gremlin Writes](best-practices-gremlin-multithreaded-writes.md "best-practices-gremlin-multithreaded-writes.md")).
The number of clients should be the same as the number of worker threads on your
Neptune writer instance, which is typically 2 x the number of vCPUs on the server.
For instance, an `r5.8xlarge` instance has 32 vCPUs and 64 worker threads.
For high-throughput write scenarios using an `r5.8xlarge`, you would use
64 clients writing batch upserts to Neptune in parallel.

Each client should submit a batch request and wait for the request to complete
before submitting another request. Although the multiple clients run in parallel,
each individual client submits requests in a serial fashion. This ensures that the
server is supplied with a steady stream of requests that occupy all the worker threads
without flooding the server-side request queue (see [Sizing DB instances in a Neptune DB cluster](feature-overview-db-clusters.md#feature-overview-sizing-instances "feature-overview-db-clusters.md#feature-overview-sizing-instances")).

## Try to avoid steps that generate multiple traversers

When a Gremlin step executes, it takes an incoming traverser, and emits one or more
output traversers. The number of traversers emitted by a step determines the number of times
the next step is executed.

Typically, when performing batch operations you want each operation, such as upsert
vertex A, to execute once, so that the sequence of operations looks like this: upsert
vertex A, then upsert vertex B, then upsert vertex C, and so on. As long as a step creates
or modifies only one element, it emits only one traverser, and the steps that represent
the next operation are executed only once. If, on the other hand, an operation creates or
modifies more than one element, it emits multiple traversers, which in turn cause
the subsequent steps to be executed multiple times, once per emitted traverser. This
can result in the database performing unnecessary additional work, and in some cases
can result in the creation of unwanted additional vertices, edges or property values.

An example of how things can go wrong is with a query like `g.V().addV()`.
This simple query adds a vertex for every vertex found in the graph, because `V()`
emits a traverser for each vertex in the graph and each of those traversers triggers
a call to `addV()`.

See [Mixing upserts and inserts](#gremlin-upserts-pre-3.6-and-inserts "#gremlin-upserts-pre-3.6-and-inserts")
for ways to deal with operations that can emit multiple traversers.

## Upserting vertices

You can use a vertex ID to determine whether a corresponding vertex exists. This
is the preferred approach, because Neptune optimizes upserts for highly concurrent
use cases around IDs. As an example, the following query creates a vertex with a
given vertex ID if it doesn't already exist, or reuses it if it does:

```
g.V('v-1')
 .fold()
  .coalesce(unfold(),
            addV('Person').property(id, 'v-1')
                          .property('email', 'person-1@example.org'))
  .id()
```

Note that this query ends with an `id()` step. While not strictly
necessary for the purpose of upserting the vertex, adding an `id()` step
to the end of an upsert query ensures that the server doesn't serialize all the
vertex properties back to the client, which helps reduce the locking cost of the query.

Alternatively, you can use a vertex property to determine whether the vertex exists:

```
g.V()
 .hasLabel('Person')
 .has('email', 'person-1@example.org')
 .fold()
 .coalesce(unfold(),
           addV('Person').property('email', 'person-1@example.org'))
 .id()
```

If possible, use your own user-supplied IDs to create vertices, and use these
IDs to determine whether a vertex exists during an upsert operation. This lets Neptune
optimize upserts around the IDs. An ID-based upsert can be significantly more efficient
than a property-based upsert in highly concurrent modification scenarios.

### Chaining vertex upserts

You can chain vertex upserts together to insert them in a batch:

```
g.V('v-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-1')
                         .property('email', 'person-1@example.org'))
 .V('v-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-2')
                         .property('email', 'person-2@example.org'))
 .V('v-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-3')
                         .property('email', 'person-3@example.org'))
 .id()
```

## Upserting edges

You can use edge IDs to upsert edges in the same way you upsert vertices using custom
vertex IDs. Again, this is the preferred approach because it allows Neptune to optimize
the query. For example, the following query creates an edge based on its edge ID if it
doesn't already exist, or reuses it if it does. The query also uses the IDs of the
`from` and `to` vertices if it needs to create a new edge.

```
g.E('e-1')
 .fold()
 .coalesce(unfold(),
           addE('KNOWS').from(V('v-1'))
                        .to(V('v-2'))
                        .property(id, 'e-1'))
 .id()
```

Many applications use custom vertex IDs, but leave Neptune to generate
edge IDs. If you don't know the ID of an edge, but you do know the `from`
and `to` vertex IDs, you can use this formulation to upsert an edge:

```
g.V('v-1')
 .outE('KNOWS')
 .where(inV().hasId('v-2'))
 .fold()
 .coalesce(unfold(),
           addE('KNOWS').from(V('v-1'))
                        .to(V('v-2')))
 .id()
```

Note that the vertex step in the `where()` clause should be
`inV()` (or `outV()` if you've used `inE()`
to find the edge), not `otherV()`. Do not use `otherV()`,
here, or the query will not be optimized and performance will suffer. For
example, Neptune would not optimize the following query:

```
// Unoptimized upsert, because of otherV()
g.V('v-1')
 .outE('KNOWS')
 .where(otherV().hasId('v-2'))
 .fold()
 .coalesce(unfold(),
           addE('KNOWS').from(V('v-1'))
                        .to(V('v-2')))
 .id()
```

If you don't know the edge or vertex IDs up front, you can upsert using
vertex properties:

```
g.V()
 .hasLabel('Person')
 .has('name', 'person-1')
 .outE('LIVES_IN')
 .where(inV().hasLabel('City').has('name', 'city-1'))
 .fold()
 .coalesce(unfold(),
           addE('LIVES_IN').from(V().hasLabel('Person')
                                    .has('name', 'person-1'))
                           .to(V().hasLabel('City')
                                  .has('name', 'city-1')))
 .id()
```

As with vertex upserts, it's preferable to use ID-based edge upserts
using either an edge ID or `from` and `to` vertex IDs,
rather than property-based upserts, so that Neptune can fully optimize
the upsert.

### Checking for `from` and `to` vertex existence

Note the construction of the steps that create a new edge: `addE().from().to()`.
This construction ensures that the query checks the existence of both the `from`
and the `to` vertex. If either of these does not exist, the query returns
an error as follows:

```
{
  "detailedMessage": "Encountered a traverser that does not map to a value for child`...`
  "code": "IllegalArgumentException",
  "requestId": "..."
}
```

If it's possible that either the `from` or the `to` vertex
doesn't exist, you should attempt to upsert them before upserting the edge between
them. See [Combining vertex and edge upserts](#gremlin-upserts-pre-3.6-vertexes-and-edges "#gremlin-upserts-pre-3.6-vertexes-and-edges").

There's an alternative construction for creating an edge that you shouldn't use:
`V().addE().to()`. It only adds an edge if the `from` vertex
exists. If the `to` vertex doesn't exist the, query generates an error,
as described previously, but if the `from` vertex doesn't exist, it
silently fails to insert an edge, without generating any error. For example, the
following upsert completes without upserting an edge if the `from` vertex
doesn't exist:

```
// Will not insert edge if from vertex does not exist
g.V('v-1')
 .outE('KNOWS')
 .where(inV().hasId('v-2'))
 .fold()
 .coalesce(unfold(),
           V('v-1').addE('KNOWS')
                   .to(V('v-2')))
 .id()
```

### Chaining edge upserts

If you want to chain edge upserts together to create a batch request, you must begin
each upsert with a vertex lookup, even if you already know the edge IDs.

If you do already know the IDs of the edges you want to upsert, and the IDs of the
`from` and `to` vertices, you can use this formulation:

```
g.V('v-1')
 .outE('KNOWS')
 .hasId('e-1')
 .fold()
 .coalesce(unfold(),
           V('v-1').addE('KNOWS')
                   .to(V('v-2'))
                   .property(id, 'e-1'))
 .V('v-3')
 .outE('KNOWS')
 .hasId('e-2').fold()
 .coalesce(unfold(),
           V('v-3').addE('KNOWS')
                   .to(V('v-4'))
                   .property(id, 'e-2'))
 .V('v-5')
 .outE('KNOWS')
 .hasId('e-3')
 .fold()
 .coalesce(unfold(),
           V('v-5').addE('KNOWS')
                   .to(V('v-6'))
                   .property(id, 'e-3'))
 .id()
```

Perhaps the most common batch edge upsert scenario is that you know the
`from` and `to` vertex IDs, but don't know the IDs of
the edges you want to upsert. In that case, use the following formulation:

```
g.V('v-1')
 .outE('KNOWS')
 .where(inV().hasId('v-2'))
 .fold()
 .coalesce(unfold(),
           V('v-1').addE('KNOWS')
                   .to(V('v-2')))

 .V('v-3')
 .outE('KNOWS')
 .where(inV().hasId('v-4'))
 .fold()
 .coalesce(unfold(),
           V('v-3').addE('KNOWS')
                   .to(V('v-4')))
 .V('v-5')
 .outE('KNOWS')
 .where(inV().hasId('v-6'))
 .fold()
 .coalesce(unfold(),
           V('v-5').addE('KNOWS').to(V('v-6')))
 .id()
```

If you know IDs of the edges you want to upsert, but don’t know the IDs of
the `from` and `to` vertices (this is unusual), you can use
this formulation:

```
g.V()
 .hasLabel('Person')
 .has('email', 'person-1@example.org')
 .outE('KNOWS')
 .hasId('e-1')
 .fold()
 .coalesce(unfold(),
           V().hasLabel('Person')
              .has('email', 'person-1@example.org')
              .addE('KNOWS')
              .to(V().hasLabel('Person')
                     .has('email', 'person-2@example.org'))
                     .property(id, 'e-1'))
 .V()
 .hasLabel('Person')
 .has('email', 'person-3@example.org')
 .outE('KNOWS')
 .hasId('e-2')
 .fold()
 .coalesce(unfold(),
           V().hasLabel('Person')
              .has('email', 'person-3@example.org')
              .addE('KNOWS')
              .to(V().hasLabel('Person')
                     .has('email', 'person-4@example.org'))
              .property(id, 'e-2'))
 .V()
 .hasLabel('Person')
 .has('email', 'person-5@example.org')
 .outE('KNOWS')
 .hasId('e-1')
 .fold()
 .coalesce(unfold(),
           V().hasLabel('Person')
              .has('email', 'person-5@example.org')
              .addE('KNOWS')
              .to(V().hasLabel('Person')
                     .has('email', 'person-6@example.org'))
                     .property(id, 'e-3'))
 .id()
```

## Combining vertex and edge upserts

Sometimes you may want to upsert both vertices and the edges that connect them. You
can mix the batch examples presented here. The following example upserts 3 vertices and
2 edges:

```
g.V('p-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-1')
                         .property('email', 'person-1@example.org'))
 .V('p-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-2')
                         .property('name', 'person-2@example.org'))
 .V('c-1')
 .fold()
 .coalesce(unfold(),
           addV('City').property(id, 'c-1')
                       .property('name', 'city-1'))
 .V('p-1')
 .outE('LIVES_IN')
 .where(inV().hasId('c-1'))
 .fold()
 .coalesce(unfold(),
           V('p-1').addE('LIVES_IN')
                   .to(V('c-1')))
 .V('p-2')
 .outE('LIVES_IN')
 .where(inV().hasId('c-1'))
 .fold()
 .coalesce(unfold(),
           V('p-2').addE('LIVES_IN')
                   .to(V('c-1')))
 .id()
```

## Mixing upserts and inserts

Sometimes you may want to upsert both vertices and the edges that connect them. You
can mix the batch examples presented here. The following example upserts 3 vertices and
2 edges:

Upserts typically proceed one element at a time. If you stick to the upsert patterns
presented here, each upsert operation emits a single traverser, which causes the subsequent
operation to be executed just once.

However, sometimes you may want to mix upserts with inserts. This can be the case, for
example, if you use edges to represent instances of actions or events. A request might use
upserts to ensure that all necessary vertices exist, and then use inserts to add edges.
With requests of this kind, pay attention to the potential number of traversers being
emitted from each operation.

Consider the following example, which mixes upserts and inserts to add edges that
represent events into the graph:

```

// Fully optimized, but inserts too many edges
g.V('p-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-1')
                         .property('email', 'person-1@example.org'))
 .V('p-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-2')
                         .property('name', 'person-2@example.org'))
 .V('p-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-3')
                         .property('name', 'person-3@example.org'))
 .V('c-1')
 .fold()
 .coalesce(unfold(),
           addV('City').property(id, 'c-1')
                       .property('name', 'city-1'))
 .V('p-1', 'p-2')
 .addE('FOLLOWED')
 .to(V('p-1'))
 .V('p-1', 'p-2', 'p-3')
 .addE('VISITED')
 .to(V('c-1'))
 .id()
```

The query should insert 5 edges: 2 FOLLOWED edges and 3 VISITED edges. However, the
query as written inserts 8 edges: 2 FOLLOWED and 6 VISITED. The reason for this is that
the operation that inserts the 2 FOLLOWED edges emits 2 traversers, causing the subsequent
insert operation, which inserts 3 edges, to be executed twice.

The fix is to add a `fold()` step after each operation that can potentially
emit more than one traverser:

```
g.V('p-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-1')
                         .property('email', 'person-1@example.org'))
 .V('p-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-2').
                         .property('name', 'person-2@example.org'))
 .V('p-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'p-3').
                         .property('name', 'person-3@example.org'))
 .V('c-1')
 .fold().
 .coalesce(unfold(),
            addV('City').property(id, 'c-1').
                        .property('name', 'city-1'))
 .V('p-1', 'p-2')
 .addE('FOLLOWED')
 .to(V('p-1'))
 .fold()
 .V('p-1', 'p-2', 'p-3')
 .addE('VISITED')
 .to(V('c-1')).
 .id()
```

Here we’ve inserted a `fold()` step after the operation that inserts
FOLLOWED edges. This results in a single traverser, which then causes the subsequent
operation to be executed only once.

The downside of this approach is that the query is now not fully optimized, because
`fold()` is not optimized. The insert operation that follows `fold()`
will now not be optimized.

If you need to use `fold()` to reduce the number of traversers on behalf
of subsequent steps, try to order your operations so that the least expensive ones occupy
the non-optimized part of the query.

## Upserts that modify existing vertices and edges

Sometimes you want to create a vertex or edge if it doesn’t exist, and then add or
update a property to it, regardless of whether it is a new or existing vertex or edge.

To add or modify a property, use the `property()` step. Use this step outside
the `coalesce()` step. If you try to modify the property of an existing vertex
or edge inside the `coalesce()` step, the query may not be optimized by the
Neptune query engine.

The following query adds or updates a counter property on each upserted vertex.
Each `property()` step has single cardinality to ensure that the new values
replace any existing values, rather than being added to a set of existing values.

```
g.V('v-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-1')
                         .property('email', 'person-1@example.org'))
 .property(single, 'counter', 1)
 .V('v-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-2')
                         .property('email', 'person-2@example.org'))
 .property(single, 'counter', 2)
 .V('v-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-3')
                         .property('email', 'person-3@example.org'))
 .property(single, 'counter', 3)
 .id()
```

If you have a property value, such as a `lastUpdated` timestamp value,
that applies to all upserted elements, you can add or update it at the end of the query:

```

g.V('v-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-1')
                         .property('email', 'person-1@example.org'))
 .V('v-2').
 .fold().
 .coalesce(unfold(),
           addV('Person').property(id, 'v-2')
                         .property('email', 'person-2@example.org'))
 .V('v-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-3')
                         .property('email', 'person-3@example.org'))
 .V('v-1', 'v-2', 'v-3')
 .property(single, 'lastUpdated', datetime('2020-02-08'))
 .id()
```

If there are additional conditions that determine whether or not a vertex
or edge should be further modified, you can use a `has()` step to
filter the elements to which a modification will be applied. The following
example uses a `has()` step to filter upserted vertices based on
the value of their `version` property. The query then updates
to 3 the `version` of any vertex whose `version` is
less than 3:

```

g.V('v-1')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-1')
                         .property('email', 'person-1@example.org')
                         .property('version', 3))
 .V('v-2')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-2')
                         .property('email', 'person-2@example.org')
                         .property('version', 3))
 .V('v-3')
 .fold()
 .coalesce(unfold(),
           addV('Person').property(id, 'v-3')
                         .property('email', 'person-3@example.org')
                         .property('version', 3))
 .V('v-1', 'v-2', 'v-3')
 .has('version', lt(3))
 .property(single, 'version', 3)
 .id()
```
