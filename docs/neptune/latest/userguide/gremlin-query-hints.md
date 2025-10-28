# Gremlin query hints

You can use query hints to specify optimization and evaluation strategies for a particular
Gremlin query in Amazon Neptune.

Query hints are specified by adding a `withSideEffect` step to the query with
the following syntax.

```
g.withSideEffect(`hint`, `value`)
```

- *hint* – Identifies the type of the
  hint to apply.
- *value* – Determines the behavior of
  the system aspect under consideration.
  For example, the following shows how to include a `repeatMode` hint in a Gremlin
  traversal.

###### Note

All Gremlin query hints side effects are prefixed with `Neptune#`.

```
g.withSideEffect('Neptune#repeatMode', 'DFS').V("3").repeat(out()).times(10).limit(1).path()
```

The preceding query instructs the Neptune engine to traverse the graph _Depth First_ (`DFS`) rather than the default Neptune,
_Breadth First_ (`BFS`).

The following sections provide more information about the available query hints and their
usage.

###### Topics

- [Gremlin repeatMode query hint](gremlin-query-hints-repeatMode.md "gremlin-query-hints-repeatMode.md")
- [Gremlin noReordering query hint](gremlin-query-hints-noReordering.md "gremlin-query-hints-noReordering.md")
- [Gremlin typePromotion query hint](gremlin-query-hints-typePromotion.md "gremlin-query-hints-typePromotion.md")
- [Gremlin useDFE query hint](gremlin-query-hints-useDFE.md "gremlin-query-hints-useDFE.md")
- [Gremlin query hints for using the results cache](gremlin-query-hints-results-cache.md "gremlin-query-hints-results-cache.md")
