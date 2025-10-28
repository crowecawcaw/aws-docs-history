# General Best Practices for Using Gremlin with Neptune

Follow these recommendations when using the Gremlin graph traversal language with
Neptune. For information about using Gremlin with Neptune, see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

###### Important

A change was made in TinkerPop version 3.4.11 that improves correctness of
how queries are processed, but for the moment can sometimes seriously impact
query performance.

For example, a query of this sort may run significantly slower:

```
g.V().hasLabel('airport').
  order().
    by(out().count(),desc).
  limit(10).
  out()
```

The vertices after the limit step are now fetched in a non-optimal way because
of the TinkerPop 3.4.11 change. To avoid this, you can modify the query by adding
the barrier() step at any point after the `order().by()`.
For example:

```
g.V().hasLabel('airport').
  order().
    by(out().count(),desc).
  limit(10).
  barrier().
  out()
```

TinkerPop 3.4.11 was enabled in Neptune [engine version 1.0.5.0](engine-releases-1.0.5.md "engine-releases-1.0.5.md").

###### Topics

- [Structure upsert queries to take advantage of the DFE engine](#best-practices-gremlin-upserts "#best-practices-gremlin-upserts")
- [Test Gremlin code in the context where you will deploy it](best-practices-gremlin-console-glv-differences.md "best-practices-gremlin-console-glv-differences.md")
- [Creating Efficient Multithreaded
  Gremlin Writes](best-practices-gremlin-multithreaded-writes.md "best-practices-gremlin-multithreaded-writes.md")
- [Pruning Records with the Creation Time
  Property](best-practices-gremlin-prune.md "best-practices-gremlin-prune.md")
- [Using the datetime( ) Method
  for Groovy Time Data](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
- [Using Native Date and Time for GLV
  Time Data](best-practices-gremlin-datetime-glv.md "best-practices-gremlin-datetime-glv.md")

## Structure upsert queries to take advantage of the DFE engine

[Making efficient upserts with Gremlin
mergeV() and mergeE() steps](gremlin-efficient-upserts.md "gremlin-efficient-upserts.md")
explains how to structure upsert queries to use the DFE engine as effectively as possible.
