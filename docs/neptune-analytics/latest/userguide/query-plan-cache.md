# Query plan cache

When a query is submitted to Neptune , the query string is parsed and translated into a query plan,
which then gets optimized and executed by the engine. Often, the applications are backed by common query
patterns that are instantiated with different values, and query plan cache would be optimal to reduce
latency of those common query patterns. The query plan cache does this by storing a parameterized version
of frequently used query plans (at most 1000 at any point), which gets reused and instantiated properly based
on new parameter values provided, if any.

**Why use the query plan cache?**

Reusing the query plan can reduce the latency, as the later executions skip parsing and optimization steps.

**Where can it be used?**

Query plan cache can be used for all type of queries. By default, it automatically caches plan for low-latency
parameterized queries, whose execution time is less than 100ms.

**How to force enable/disable the query plan cache?**

For read-only queries, query plan cache is enabled by default for low-latency queries. A plan is cached only when latency is lower
than the threshold of 100ms. This behavior can be overridden on a per-query basis by HTTP parameter. HTTP parameter
`--plan-cache` can take `enabled` or `disabled` as a value.

```
# Forcing plan to be cached or reused
% aws neptune-graph execute-query \
   --graph-identifier <graph-id> \
   --query-string "MATCH (n) RETURN n LIMIT 1"
   --region <region> \
   --plan-cache "enabled"
   --language open_cypher /tmp/out.txt

% aws neptune-graph execute-query \
   --graph-identifier <graph-id> \
   --query-string "RETURN \$arg"
   --region <region> \
   --plan-cache "enabled" \
   --parameters "{\"arg\": 123}"
   --language open_cypher /tmp/out.txt
```

**How to check if a plan is cached?**

To check if a plan is cached, use `explain`. For read-only queries, if the query was submitted
and the plan was cached, explain would show explain details relevant to the query plan cache.

```
% aws neptune-graph execute-query \
   --graph-identifier <graph-id> \
   --query-string "MATCH (n) RETURN n LIMIT 1"
   --region <region> \
   --plan-cache "enabled" \
   --explain-mode "static" \
   --language open_cypher /tmp/out.txt
```

```
Query: <QUERY STRING>
Plan cached by request: <REQUEST ID OF FIRST TIME EXECUTION>
Plan cached at: <TIMESTAMP OF FIRST TIME EXECUTION>
Parameters: <PARAMETERS IF QUERY IS PARAMETERIZED QUERY>
Plan cache hits: <NUMBER OF CACHE HITS FOR CACHED PLAN>
First query evaluation time: <LATENCY OF FIRST TIME EXECUTION>
```

The query has been executed based on a cached query plan. Detailed explain with operator runtime statistics can be obtained
by running the query with plan cache disabled (using HTTP parameter planCache=disabled).

###### Note

For a mutation query, explain is not yet supported.

**Eviction**

A query plan is evicted by cache TTL or maximum number of cached query plans reached. When the query plan is hit,
the TTL is refreshed. The defaults are:

- The maximum number of plans cached per instance is 1000.
- TTL: 300_000 milliseconds or 5 minutes. Note that cache hit refreshes the TTL back to 5 min.
  **Conditions when a query plan is not cached**

The following list demonstrates conditions for when a query plan would not be cached.

- If submitted with query-specific parameter `--plan-cache "disabled"`.
  - If a cache is wanted, you can rerun the query without `--plan-cache "disabled"`.

- If the query evaluation time is larger than latency threshold, it’s not cached since it’s a long-running
  query and is considered to not benefit from query plan cache.
- If the query contains pattern that does not return any results.
  - i.e. `MATCH (n:nonexistentLabel) return n` when there are zero nodes with specified label.
  - i.e. `MATCH (n {name: $param}) return n with parameters={"param": "abcde"}` when there are zero
    nodes with name=abcde.

- If the query parameter is composite type (list, map).

```
aws neptune-graph execute-query \
   --graph-identifier <graph-id> \
   --query-string "RETURN \$arg"
   --region <region> \
   --plan-cache "enabled" \
   --parameters "{\"arg\": [1, 2, 3]}"
   --language open_cypher /tmp/out.txt

 aws neptune-graph execute-query \
   --graph-identifier <graph-id> \
   --query-string "RETURN \$arg"
   --region <region> \
   --plan-cache "enabled" \
   --parameters "{\"arg\": {\"a\": 1}}"
   --language open_cypher /tmp/out.txt
```

- If the query parameter is a string that has not been part of data load or data insertion.
  - If `CREATE (n {name: "X"})`, is done to insert “X”.
  - `RETURN “X”` is cached, while `RETURN “Y”` isn’t, as “Y” has not been
    inserted and does not exist in the database.
