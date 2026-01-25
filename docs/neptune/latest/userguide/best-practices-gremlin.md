# General Best Practices for Using Gremlin with Neptune

Follow these recommendations when using the Gremlin graph traversal language with
Neptune. For information about using Gremlin with Neptune, see [Accessing a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

###### Topics

- [Structure upsert queries to take advantage of the DFE engine](#best-practices-gremlin-upserts "#best-practices-gremlin-upserts")
- [Test Gremlin code in the context where you will deploy it](best-practices-gremlin-console-glv-differences.md "best-practices-gremlin-console-glv-differences.md")
- [Creating Efficient Multithreaded
  Gremlin Writes](best-practices-gremlin-multithreaded-writes.md "best-practices-gremlin-multithreaded-writes.md")
- [Pruning Records with the Creation Time
  Property](best-practices-gremlin-prune.md "best-practices-gremlin-prune.md")
- [Using the datetime( ) Function
  for Gremlin Scripts](best-practices-gremlin-datetime.md "best-practices-gremlin-datetime.md")
- [Using Native Date and Time for GLV
  Time Data](best-practices-gremlin-datetime-glv.md "best-practices-gremlin-datetime-glv.md")

## Structure upsert queries to take advantage of the DFE engine

[Making efficient upserts with Gremlin
mergeV() and mergeE() steps](gremlin-efficient-upserts.md "gremlin-efficient-upserts.md")
explains how to structure upsert queries to use the DFE engine as effectively as possible.
