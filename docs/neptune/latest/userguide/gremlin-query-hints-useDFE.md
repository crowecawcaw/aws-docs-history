# Gremlin useDFE query hint

Use this query hint to enable use of the DFE for executing the query. By default
Neptune does not use the DFE without this query hint being set to `true`,
because the [neptune_dfe_query_engine](parameters.md#parameters-instance-parameters-neptune_dfe_query_engine "parameters.md#parameters-instance-parameters-neptune_dfe_query_engine")
instance parameter defaults to `viaQueryHint`. If you set that instance
parameter to `enabled`, the DFE engine is used for all queries except those
having the `useDFE` query hint set to `false`.

Example of enabling the DFE for a query:

```
g.withSideEffect('Neptune#useDFE', true).V().out()
```
