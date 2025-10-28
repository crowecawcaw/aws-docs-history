# Prefer directed to bi-directional edges in queries

When Neptune performs query optimizations, bi-directional edges make it difficult
to create optimal query plans. Sub-optimal plans require the engine to do unnecessary
work and result in poorer performance.

Therefore, use directed edges rather than bi-directional ones whenever possible.
For example, use:

```
MATCH p=(:airport {code: 'ANC'})-[:route]->(d) RETURN p)
```

instead of:

```
MATCH p=(:airport {code: 'ANC'})-[:route]-(d) RETURN p)
```

Most data models don't actually need to traverse edges in both directions, so
queries can achieve significant performance improvements by making the switch to
using directed edges.

If your data model does require traversing bi-directional edges, make the first
node (left-hand side) in the `MATCH` pattern the node with the most
restrictive filtering.

Take the example, "Find me all the `routes` to and from the
`ANC` airport". Write this query to start at the `ANC`
airport, like this:

```
MATCH p=(src:airport {code: 'ANC'})-[:route]-(d) RETURN p
```

The engine can perform the minimal amount of work to satisfy the query,
because the most restricted node is placed as the first node (left-hand side)
in the pattern. The engine can then optimize the query.

This is far preferable than filtering the `ANC` airport at the end
of the pattern, like this:

```
MATCH p=(d)-[:route]-(src:airport {code: 'ANC'}) RETURN p
```

When the most restricted node is not placed first in the pattern,
the engine must perform additional work because it can't optimize the query
and has to perform additional lookups to arrive at the results.
