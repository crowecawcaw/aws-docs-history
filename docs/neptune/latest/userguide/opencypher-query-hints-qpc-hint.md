# openCypher query plan cache hint

Query plan cache behavior can be overridden on a per-query (parameterized or not) basis by query-level query hint
`QUERY:PLANCACHE`. It needs to be used with the `USING` clause. The query hint accepts
`enabled` or `disabled` as a value. For more information on query plan cache, see
[Query plan cache in Amazon Neptune](access-graph-qpc.md "access-graph-qpc.md").

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
