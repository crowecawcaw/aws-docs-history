# Query plan cache in Amazon Neptune

When a query is submitted to Neptune, the query string is parsed, optimized, and transformed into a query plan, which
then gets executed by the engine. Applications are often backed by common query patterns that are instantiated with
different values. Query plan cache can reduce the overall latency by caching the query plans and thereby avoiding parsing
and optimization for such repeated patterns.

Query Plan Cache can be used for **OpenCypher** queries — both non-parameterized or
parameterized queries. It is enabled for READ, and for HTTP and Bolt. It is **not** supported
for OC mutation queries. It is **not** supported for Gremlin or SPARQL queries.

## How to force enable or disable query plan cache

Query plan cache is enabled by default for low-latency parameterized queries. A plan for a parameterized query is cached
only when latency is lower than the threshold of **100ms**. This behavior can be overridden
on a per-query (parameterized or not) basis by the query-level Query Hint `QUERY:PLANCACHE`. It needs to be used
with the `USING` clause. The query hint accepts `enabled` or `disabled` as a value.

```
# Forcing plan to be cached or reused
% curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"enabled\" MATCH(n) RETURN n LIMIT 1"

% curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"enabled\" RETURN \$arg" \
  -d "parameters={\"arg\": 123}"

# Forcing plan to be neither cached nor reused
% curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"disabled\" MATCH(n) RETURN n LIMIT 1"

```

## How to determine if a plan is cached or not

For HTTP READ, if the query was submitted and the plan was cached, `explain` would show details relevant to
query plan cache.

```
% curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"enabled\" MATCH(n) RETURN n LIMIT 1" \
  -d "explain=[static|details]"

Query: <QUERY STRING>
Plan cached by request: <REQUEST ID OF FIRST TIME EXECUTION>
Plan cached at: <TIMESTAMP OF FIRST TIME EXECUTION>
Parameters: <PARAMETERS, IF QUERY IS PARAMETERIZED QUERY>
Plan cache hits: <NUMBER OF CACHE HITS FOR CACHED PLAN>
First query evaluation time: <LATENCY OF FIRST TIME EXECUTION>

The query has been executed based on a cached query plan. Detailed explain with operator runtime statistics can be obtained by running the query with plan cache disabled (using HTTP parameter planCache=disabled).
```

When using Bolt, the explain feature is not supported.

## Eviction

A query plan is evicted by the cache time to live (TTL) or when a maximum number of cached query plans have been reached.
When the query plan is hit, the TTL is refreshed. The defaults are:

- 1000 - The maximum number of plans that can be cached per instance.
- TTL - 300,000 milliseconds or 5 minutes. The cache hit restarts the TTL, and resets it back to 5 min.

## Conditions causing the plan not to be cached

Query plan cache would not be used under the following conditions:

1. When a query is submitted using the query hint `QUERY:PLANCACHE "disabled"`. You can re-run the query and
   remove `QUERY:PLANCACHE "disabled"` to enable the query plan cache.
2. If the query that was submitted is not a parameterized query and does not contain the hint
   `QUERY:PLANCACHE "enabled"`.
3. If the query evaluation time is larger than the latency threshold, the query is not cached and is considered a
   long-running query that would not benefit from the query plan cache.
4. If the query contains a pattern that doesn't return any results.
   - i.e. `MATCH (n:nonexistentLabel) return n` when there are zero nodes with the specified label.
   - i.e. `MATCH (n {name: $param}) return n` with `parameters={"param": "abcde"}` when
     there are zero nodes containing `name=abcde`.

5. If the query parameter is a composite type, such as a `list` or a `map`.

```
curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"enabled\" RETURN \$arg" \
  -d "parameters={\"arg\": [1, 2, 3]}"

curl -k https://<endpoint>:<port>/opencypher \
  -d "query=Using QUERY:PLANCACHE \"enabled\" RETURN \$arg" \
  -d "parameters={\"arg\": {\"a\": 1}}"
```

6. If the query parameter is a string that has not been part of a data load or data insertion operation. For example, if
   `CREATE (n {name: "X"})` is ran to insert `"X"`, then `RETURN "X"` is cached, while
   `RETURN "Y"` would not be cached, as `"Y"` has not been inserted and does not exist in the
   database.
