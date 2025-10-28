# Making efficient upserts with Gremlin

`mergeV()` and `mergeE()` steps

An upsert (or conditional insert) reuses a vertex or edge if it already exists,
or creates it if it doesn't. Efficient upserts can make a significant difference in
the performance of Gremlin queries.

Upserts allow you to write idempotent insert operations: no matter how many times
you run such an operation, the overall outcome is the same. This is useful in highly
concurrent write scenarios where concurrent modifications to the same part of the graph
can force one or more transactions to roll back with a `ConcurrentModificationException`,
thereby necessitating retries.

For example, the following query upserts a vertex by using the supplied `Map`
to first try to find a vertex with a `T.id` of `"v-1"`. If that
vertex is found then it is returned. If it is not found then a vertex with that `id`
and property are created through the `onCreate` clause.

```
g.mergeV([(id):'v-1']).
  option(onCreate, [(label): 'PERSON', 'email': 'person-1@example.org'])
```

## Batching upserts to improve throughput

For high throughput write scenarios, you can chain `mergeV()` and
`mergeE()` steps together to upsert vertices and edges in batches.
Batching reduces the transactional overhead of upserting large numbers of vertices
and edges. You can then further improve throughput by upserting batch requests
in parallel using multiple clients.

As a rule of thumb we recommend upserting approximately 200 records per batch request.
A record is a single vertex or edge label or property. A vertex with a single label and
4 properties, for example, creates 5 records. An edge with a label and a single property
creates 2 records. If you wanted to upsert batches of vertices, each with a single label
and 4 properties, you should start with a batch size of 40, because `200 / (1 + 4)
 = 40`.

You can experiment with the batch size. 200 records per batch is a good starting
point, but the ideal batch size may be higher or lower depending on your workload.
Note, however, that Neptune may limit the overall number of Gremlin steps per request.
This limit is not documented, but to be on the safe side, try to ensure that your
requests contain no more than 1,500 Gremlin steps. Neptune may reject large batch
requests with more than 1,500 steps.

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

See [Mixing upserts and inserts](#gremlin-upserts-and-inserts "#gremlin-upserts-and-inserts")
for ways to deal with operations that can emit multiple traversers.

## Upserting vertices

The `mergeV()` step is specifically designed for upserting vertices.
It takes as an argument a `Map` that represents elements to match for
existing vertices in the graph, and if an element is not found, uses that
`Map` to create a new vertex. The step also allows you to alter
the behavior in the event of a creation or a match, where the `option()`
modulator can be applied with `Merge.onCreate` and `Merge.onMatch`
tokens to control those respective behaviors. See the TinkerPop [Reference
Documentation](https://tinkerpop.apache.org/docs/current/reference/#mergevertex-step "https://tinkerpop.apache.org/docs/current/reference/#mergevertex-step") for further information about how to use this step.

You can use a vertex ID to determine whether a specific vertex exists. This is the
preferred approach, because Neptune optimizes upserts for highly concurrent use cases
around IDs. As an example, the following query creates a vertex with a given vertex ID
if it doesn't already exist, or reuses it if it does:

```
g.mergeV([(T.id): 'v-1']).
    option(onCreate, [(T.label): 'PERSON', email: 'person-1@example.org', age: 21]).
    option(onMatch, [age: 22]).
  id()
```

Note that this query ends with an `id()` step. While not strictly necessary
for the purpose of upserting the vertex, an `id()` step to the end of an upsert
query ensures that the server doesn't serialize all the vertex properties back to the client,
which helps reduce the locking cost of the query.

Alternatively, you can use a vertex property to identify a vertex:

```
g.mergeV([email: 'person-1@example.org']).
    option(onCreate, [(T.label): 'PERSON', age: 21]).
    option(onMatch, [age: 22]).
  id()
```

If possible, use your own user-supplied IDs to create vertices, and use these IDs
to determine whether a vertex exists during an upsert operation. This lets Neptune
optimize the upserts. An ID-based upsert can be significantly more efficient than
a property-based upsert when concurrent modifications are common.

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

Alternatively, you can also use this `mergeV()` syntax:

```
g.mergeV([(T.id): 'v-1', (T.label): 'PERSON', email: 'person-1@example.org']).
  mergeV([(T.id): 'v-2', (T.label): 'PERSON', email: 'person-2@example.org']).
  mergeV([(T.id): 'v-3', (T.label): 'PERSON', email: 'person-3@example.org'])
```

However, because this form of the query includes elements in the search
criteria that are superfluous to the basic lookup by `id`, it
isn't as efficient as the previous query.

## Upserting edges

The `mergeE()` step is specifically designed for upserting edges.
It takes a `Map` as an argument that represents elements to match for
existing edges in the graph and if an element is not found, uses that `Map`
to create a new edge. The step also allows you to alter the behavior in the event
of a creation or a match, where the `option()` modulator can be applied
with `Merge.onCreate` and `Merge.onMatch` tokens to control
those respective behaviors. See the TinkerPop [Reference
Documentation](https://tinkerpop.apache.org/docs/current/reference/#mergeedge-step "https://tinkerpop.apache.org/docs/current/reference/#mergeedge-step") for further information about how to use this step.

You can use edge IDs to upsert edges in the same way you upsert vertices
using custom vertex IDs. Again, this is the preferred approach because it
allows Neptune to optimize the query. For example, the following query
creates an edge based on its edge ID if it doesn't already exist, or reuses
it if it does. The query also uses the IDs of the `Direction.from`
and `Direction.to` vertices if it needs to create a new edge:

```
g.mergeE([(T.id): 'e-1']).
    option(onCreate, [(from): 'v-1', (to): 'v-2', weight: 1.0]).
    option(onMatch, [weight: 0.5]).
  id()
```

Note that this query ends with an `id()` step. While not strictly
necessary for the purpose of upserting the edge, adding an `id()` step to
the end of an upsert query ensures that the server doesn't serialize all the edge
properties back to the client, which helps reduce the locking cost of the query.

Many applications use custom vertex IDs, but leave Neptune to generate edge
IDs. If you don't know the ID of an edge, but you do know the `from` and
`to` vertex IDs, you can use this kind of query to upsert an edge:

```
g.mergeE([(from): 'v-1', (to): 'v-2', (T.label): 'KNOWS']).
  id()
```

All vertices referenced by `mergeE()` must exist for the step to
create the edge.

### Chaining edge upserts

As with vertex upserts, it's straightforward to chain `mergeE()`
steps together for batch requests:

```
g.mergeE([(from): 'v-1', (to): 'v-2', (T.label): 'KNOWS']).
  mergeE([(from): 'v-2', (to): 'v-3', (T.label): 'KNOWS']).
  mergeE([(from): 'v-3', (to): 'v-4', (T.label): 'KNOWS']).
  id()
```

## Combining vertex and edge upserts

Sometimes you may want to upsert both vertices and the edges that connect them. You
can mix the batch examples presented here. The following example upserts 3 vertices and
2 edges:

```
g.mergeV([(id):'v-1']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-1@example.org']).
  mergeV([(id):'v-2']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-2@example.org']).
  mergeV([(id):'v-3']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-3@example.org']).
  mergeE([(from): 'v-1', (to): 'v-2', (T.label): 'KNOWS']).
  mergeE([(from): 'v-2', (to): 'v-3', (T.label): 'KNOWS']).
 id()
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
g.mergeV([(id):'v-1']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-1@example.org']).
  mergeV([(id):'v-2']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-2@example.org']).
  mergeV([(id):'v-3']).
    option(onCreate, [(label): 'PERSON', 'email': 'person-3@example.org']).
  mergeV([(T.id): 'c-1', (T.label): 'CITY', name: 'city-1']).
  V('p-1', 'p-2').
  addE('FOLLOWED').to(V('p-1')).
  V('p-1', 'p-2', 'p-3').
  addE('VISITED').to(V('c-1')).
  id()
```

The query should insert 5 edges: 2 FOLLOWED edges and 3 VISITED edges. However, the
query as written inserts 8 edges: 2 FOLLOWED and 6 VISITED. The reason for this is that
the operation that inserts the 2 FOLLOWED edges emits 2 traversers, causing the subsequent
insert operation, which inserts 3 edges, to be executed twice.

The fix is to add a `fold()` step after each operation that can potentially
emit more than one traverser:

```
g.mergeV([(T.id): 'v-1', (T.label): 'PERSON', email: 'person-1@example.org']).
  mergeV([(T.id): 'v-2', (T.label): 'PERSON', email: 'person-2@example.org']).
  mergeV([(T.id): 'v-3', (T.label): 'PERSON', email: 'person-3@example.org']).
  mergeV([(T.id): 'c-1', (T.label): 'CITY', name: 'city-1']).
  V('p-1', 'p-2').
  addE('FOLLOWED').
    to(V('p-1')).
  fold().
  V('p-1', 'p-2', 'p-3').
  addE('VISITED').
    to(V('c-1')).
  id()
```

Here we’ve inserted a `fold()` step after the operation that inserts
FOLLOWED edges. This results in a single traverser, which then causes the subsequent
operation to be executed only once.

The downside of this approach is that the query is now not fully optimized, because
`fold()` is not optimized. The insert operation that follows `fold()`
will now also not be optimized.

If you need to use `fold()` to reduce the number of traversers on behalf
of subsequent steps, try to order your operations so that the least expensive ones occupy
the non-optimized part of the query.

## Setting Cardinality

The default cardinality for vertex properties in Neptune is set, which means that when using mergeV() the values
supplied in the map are all going to be given that cardinality. To use single cardinality, you must be explicit in its
usage. Starting in TinkerPop 3.7.0, there is a new syntax that allows the cardinality to be supplied as part of the map
as shown in the following example:

```
g.mergeV([(T.id): '1234']).
  option(onMatch, ['age': single(20), 'name': single('alice'), 'city': set('miami')])
```

Alternatively, you may set the cardinality as a default for that `option` as follows:

```
// age and name are set to single cardinality by default
g.mergeV([(T.id): '1234']).
  option(onMatch, ['age': 22, 'name': 'alice', 'city': set('boston')], single)
```

There are fewer options for setting cardinality in `mergeV()` prior to version 3.7.0. The general approach is
to fall back to the `property()` step as follows:

```
g.mergeV([(T.id): '1234']).
  option(onMatch, sideEffect(property(single,'age', 20).
  property(set,'city','miami')).constant([:]))
```

###### Note

This approach will only work with `mergeV()` when it is used with a start step. You would therefore not be
able to chain `mergeV()` within a single traversal as the first `mergeV()` after the start step
that uses this syntax will produce an error should the incoming traverser be a graph element. In this case, you would
want to break up your `mergeV()` calls into multiple requests where each can be a start step.
