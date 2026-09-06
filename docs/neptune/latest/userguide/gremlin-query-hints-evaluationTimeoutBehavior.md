

# Gremlin `evaluationTimeoutBehavior` query hint
<a name="gremlin-query-hints-evaluationTimeoutBehavior"></a>

By default, when a Gremlin query exceeds the query timeout, Neptune cancels the query and returns an error. The `evaluationTimeoutBehavior` query hint changes this behavior so that Neptune streams back any partial results that were computed before the timeout occurred, instead of returning an error.

**Note**  
This query hint uses the `with` step, not `withSideEffect`, and does not use the `Neptune#` prefix.

## Syntax
<a name="gremlin-query-hints-evaluationTimeoutBehavior-syntax"></a>

```
g.with('evaluationTimeoutBehavior', '{{value}}').{{gremlin-traversal}}
```

**Available Values**
+ `partialResults` – When the query times out, Neptune returns any results that were computed before the timeout.
+ `exception` – When the query times out, Neptune returns an error. This is the default behavior.

**Important**  
This query hint can only be used with read-only queries. If you use this hint with a mutating query or with DFE enabled (either via the `useDFE` query hint or the `neptune_dfe_query_engine` instance parameter), Neptune returns an error.

## Example
<a name="gremlin-query-hints-evaluationTimeoutBehavior-example"></a>

The following query returns partial results if it exceeds the query timeout:

```
g.with('evaluationTimeoutBehavior', 'partialResults').V().out().valueMap()
```