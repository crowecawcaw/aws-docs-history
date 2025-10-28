# Bulk add vertices and edges in batches

Every query to the Neptune DB runs in the scope of a single transaction, unless
you use a session. This means that if you need to insert a lot of data using gremlin queries,
batching them together in a batch size of 50-100 improves performance by reducing
the number of transactions created for the load.

As an example, adding 5 vertices to the database would look like this:

```
// Create a GraphTraversalSource for the remote connection
final GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));
// Add 5 vertices in a single query
g.addV("Person").property(T.id, "P1")
 .addV("Person").property(T.id, "P2")
 .addV("Person").property(T.id, "P3")
 .addV("Person").property(T.id, "P4")
 .addV("Person").property(T.id, "P5").iterate();
```
