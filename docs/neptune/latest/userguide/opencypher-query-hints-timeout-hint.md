# openCypher query timeout hint

Query timeout behavior can be configured on a per-query basis by query-level query hint
`QUERY:TIMEOUTMILLISECONDS`. It must be used with the `USING` clause. The query hint accepts
non-negative long as a value.

```
# Using query-level timeout hint

% curl https://<endpoint>:<port>/opencypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"
```

Query timeout behavior will consider the minimum of cluster-level timeout and query-level timeout. Please see below
examples to understand query timeout behavior. For more information on cluster-level query timeout, see
[neptune_query_timeout](parameters.md#parameters-db-cluster-parameters-neptune_query_timeout "parameters.md#parameters-db-cluster-parameters-neptune_query_timeout").

```
# Suppose `neptune_query_timeout` is 10000 ms and query-level timeout is set to 100 ms
# It will consider 100 ms as the final timeout

% curl https://<endpoint>:<port>/opencypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 100 MATCH(n) RETURN n LIMIT 1"

# Suppose `neptune_query_timeout` is 100 ms and query-level timeout is set to 10000 ms
# It will still consider 100 ms as the final timeout

% curl https://<endpoint>:<port>/opencypher \
  -d "query=USING QUERY:TIMEOUTMILLISECONDS 10000 MATCH(n) RETURN n LIMIT 1"
```
