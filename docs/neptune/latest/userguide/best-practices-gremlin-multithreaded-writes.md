# Creating Efficient Multithreaded

Gremlin Writes

There are a few guidelines for multithreaded loading of data into Neptune using
Gremlin.

If possible, give each thread a set of vertices or edges to insert or modify that do not
collide. For example, thread 1 addresses ID range 1–50,000, thread 2 addresses ID range
50,001–100,000, and so on. This reduces the chance of hitting a
`ConcurrentModificationException`. To be safe, put a `try/catch` block
around all writes. If any fail, you can retry them after a short delay.

Batching writes in a batch size between 50 and 100 (vertices or edges) generally works
well. If you have a lot of properties being added for each vertex, a number closer to 50 than
100 might be a better choice. Some experimentation is worthwhile. So for batched writes, you
can use something like this:

```
g.addV(‘test’).property(id,’1’).as(‘a’).
  addV(‘test’).property(id,’2’).
  addE(‘friend’).to(‘a’).
```

This is then repeated in each batch operation.

Using batches is significantly more efficient than adding one vertex
or edge per Gremlin round trip to the server.

If you are using a Gremlin Language Variant (GLV) client, you can create a batch
programmatically by first creating a traversal. Then add to it, and finally, iterate over it;
for example:

```
  t.addV(‘test’).property(id,’1’).as(‘a’)
  t.addV(‘test’).property(id,’2’)
  t.addE(‘friend’).to(‘a’)
  t.iterate()
```

It's best to use the Gremlin Language Variant client if possible. But you can do something
similar with a client that submits queries as text strings by concatenating strings to build
up a batch.

If you are using one of the Gremlin Client libraries rather than basic HTTP for queries,
the threads should all share the same client, cluster, or connection pool. You might need to
tune settings to get the best possible throughput—settings such as the size of the
connection pool and the number of worker threads that the Gremlin client uses.
