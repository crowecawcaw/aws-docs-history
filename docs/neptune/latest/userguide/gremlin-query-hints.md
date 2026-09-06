

# Gremlin query hints
<a name="gremlin-query-hints"></a>

You can use query hints to specify optimization and evaluation strategies for a particular Gremlin query in Amazon Neptune. 

Most query hints are specified by adding a `withSideEffect` step to the query with the following syntax.

```
g.withSideEffect({{hint}}, {{value}})
```
+ *hint* – Identifies the type of the hint to apply.
+ *value* – Determines the behavior of the system aspect under consideration.

For example, the following shows how to include a `repeatMode` hint in a Gremlin traversal.

**Note**  
Query hints that use `withSideEffect` are always prefixed with `Neptune#`.

```
g.withSideEffect('Neptune#repeatMode', 'DFS').V("3").repeat(out()).times(10).limit(1).path()
```

The preceding query instructs the Neptune engine to traverse the graph *Depth First* (`DFS`) rather than the default Neptune, *Breadth First* (`BFS`).

**Important**  
Some query hints use the `with` step instead of `withSideEffect`. The two are not interchangeable. Each query hint section on this page shows the correct syntax to use.

The following sections provide more information about the available query hints and their usage.

**Topics**
+ [Gremlin repeatMode query hint](gremlin-query-hints-repeatMode.md)
+ [Gremlin noReordering query hint](gremlin-query-hints-noReordering.md)
+ [Gremlin typePromotion query hint](gremlin-query-hints-typePromotion.md)
+ [Gremlin useDFE query hint](gremlin-query-hints-useDFE.md)
+ [Gremlin `evaluationTimeoutBehavior` query hint](gremlin-query-hints-evaluationTimeoutBehavior.md)
+ [Gremlin query hints for using the results cache](gremlin-query-hints-results-cache.md)