# Use cases for

the Neptune lookup cache

The lookup cache only helps when your read queries are returning the properties
of a very large number of vertices and edges, or of RDF triples.

To optimize query performance, Amazon Neptune uses the `R5d` instance
type to create a large cache for such property values or literals. Retrieving them
from the cache is then much faster than retrieving them from cluster storage
volumes.

As a rule of thumb, it's only worthwhile to enable the lookup cache if all three
of the following conditions are met:

- You have been observing increased latency in read queries.
- You're also observing a drop in the `BufferCacheHitRatio`
  [CloudWatch metric](cw-metrics.md#cw-metrics-available "cw-metrics.md#cw-metrics-available") when running read queries
  (see [Monitoring Neptune Using Amazon CloudWatch](cloudwatch.md "cloudwatch.md")).
- Your read queries are spending a lot of time in materializing return
  values prior to rendering the results (see the Gremlin-profile example below for
  a way to determine how many property values are being materialized for a query).

###### Note

This feature is helpful _only_ in the specific scenario
described above. For example, the lookup cache doesn't help aggregation queries
at all. Unless you are running queries that would benefit from the lookup cache,
there is no reason to use an `R5d` instance type instead of an
equivalent and less expensive `R5` instance type.

If you're using Gremlin, you can assess the materialization costs of a query
with the [Gremlin profile API](gremlin-profile-api.md "gremlin-profile-api.md").
Under "Index Operations', it shows the number of terms materialized during execution:

```
Index Operations
Query execution:
    # of statement index ops: 3
    # of unique statement index ops: 3
    Duplication ratio: 1.0
    `# of terms materialized: 5273`
Serialization:
    # of statement index ops: 200
    # of unique statement index ops: 140
    Duplication ratio: 1.43
    `# of terms materialized: 32693`
```

The number of non-numerical terms that are materialized is directly proportional to
the number of term look-ups that Neptune has to perform.
