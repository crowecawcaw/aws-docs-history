# Gremlin noReordering query hint

When you submit a Gremlin traversal, the Neptune query engine investigates the structure
of the traversal and reorders parts of the query, trying to minimize the amount of work
required for evaluation and query response time. For example, a traversal with multiple
constraints, such as multiple `has()` steps, is typically not evaluated in the
given order. Instead it is reordered after the query is checked with static analysis.

The Neptune query engine tries to identify which constraint is more selective and runs
that one first. This often results in better performance, but the order in which Neptune
chooses to evaluate the query might not always be optimal.

If you know the exact characteristics of the data and want to manually dictate the order of
the query execution, you can use the Neptune `noReordering` query hint to specify
that the traversal be evaluated in the order given.

## Syntax

The `noReordering` query hint is specified by adding a
`withSideEffect` step to the query.

```
g.withSideEffect('Neptune#noReordering', `true or false`).`gremlin-traversal`
```

###### Note

All Gremlin query hints side effects are prefixed with
`Neptune#`.

###### Available Values

- `true`
- `false`
