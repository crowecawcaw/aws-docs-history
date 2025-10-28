# Gremlin repeatMode query hint

The Neptune `repeatMode` query hint specifies how the Neptune engine
evaluates the `repeat()` step in a Gremlin traversal: breadth first, depth first,
or chunked depth first.

The evaluation mode of the `repeat()` step is important when it is used to find
or follow a path, rather than simply repeating a step a limited number of times.

## Syntax

The `repeatMode` query hint is specified by adding a
`withSideEffect` step to the query.

```
g.withSideEffect('Neptune#repeatMode', '`mode`').`gremlin-traversal`
```

###### Note

All Gremlin query hints side effects are prefixed with `Neptune#`.

###### Available Modes

- `BFS`

Breadth-First Search

Default execution mode for the `repeat()` step. This gets all sibling
nodes before going deeper along the path.

This version is memory-intensive and frontiers can get very large. There is a higher
risk that the query will run out of memory and be cancelled by the Neptune engine.
This most closely matches other Gremlin implementations.

- `DFS`

Depth-First Search

Follows each path to the maximum depth before moving on to the next solution.

This uses less memory. It may provide better performance in situations like finding
a single path from a starting point out multiple hops.

- `CHUNKED_DFS`

Chunked Depth-First Search

A hybrid approach that explores the graph depth-first in chunks of 1,000 nodes,
rather than 1 node (`DFS`) or all nodes (`BFS)`.

The Neptune engine will get up to 1,000 nodes at each level before following the
path deeper.

This is a balanced approach between speed and memory usage.

It is also useful if you want to use `BFS`, but the query is using too
much memory.

## Example

The following section describes the effect of the repeat mode on a Gremlin
traversal.

In Neptune the default mode for the `repeat()` step is to perform a
breadth-first (`BFS`) execution strategy for all traversals.

In most cases, the TinkerGraph implementation uses the same execution strategy, but in
some cases it alters the execution of a traversal.

For example, the TinkerGraph implementation modifies the following query.

```
g.V("`3`").repeat(out()).times(10).limit(1).path()
```

The `repeat()` step in this traversal is "unrolled" into the following
traversal, which results in a depth-first (`DFS`) strategy.

```
g.V(<id>).out().out().out().out().out().out().out().out().out().out().limit(1).path()
```

###### Important

The Neptune query engine does not do this automatically.

Breadth-first (`BFS`) is the default execution strategy, and is similar to
TinkerGraph in most cases. However, there are certain cases where depth-first
(`DFS`) strategies are preferable.

###### BFS (Default)

Breadth-first (BFS) is the default execution strategy for the `repeat()`
operator.

```
g.V("`3`").repeat(out()).times(10).limit(1).path()
```

The Neptune engine fully explores the first nine-hop frontiers before finding a
solution ten hops out. This is effective in many cases, such as a shortest-path
query.

However, for the preceding example, the traversal would be much faster using the
depth-first (`DFS`) mode for the `repeat()` operator.

###### DFS

The following query uses the depth-first (`DFS`) mode for the
`repeat()` operator.

```
g.withSideEffect("Neptune#repeatMode", "DFS").V("`3`").repeat(out()).times(10).limit(1)
```

This follows each individual solution out to the maximum depth before exploring the next
solution.
