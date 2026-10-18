

# Using Gremlin with the Amazon Neptune DFE query engine
<a name="gremlin-with-dfe"></a>

You can enable Neptune's [alternative query engine](neptune-dfe-engine.md), known as DFE, in two ways:
+ Set the [`neptune_dfe_query_engine`](parameters.md#parameters-instance-parameters-neptune_dfe_query_engine) instance parameter to `enabled` for all queries on the instance.
+ Use the [`useDFE` query hint](gremlin-query-hints-useDFE.md) on individual queries (requires `neptune_dfe_query_engine` to be set to its default value of `viaQueryHint`).

When DFE is enabled, Neptune translates read-only Gremlin queries and traversals into an intermediate logical representation and runs them on DFE whenever possible.

Starting with Neptune engine release 1.5.0.0, DFE natively supports most Gremlin steps. When a step isn't supported by DFE, Neptune falls back to TinkerPop to run the step. The `explain` and `profile` reports include warnings when this happens.

## Query planning interleaving
<a name="gremlin-with-dfe-interleaving"></a>

When Neptune encounters a Gremlin step without a corresponding native DFE operator, it runs as much of the traversal on DFE as possible. It then falls back to TinkerPop only for the unsupported step.

Neptune represents any intermediate, non-prefix query translation as a `NeptuneInterleavingStep` in the `explain` and `profile` outputs.

For performance comparison, you can turn off interleaving in a query while still using the DFE engine to run the prefix part. You can also use only the TinkerPop engine for non-prefix query execution. To do this, use the `disableInterleaving` query hint.

Just as the [useDFE](gremlin-query-hints-useDFE.md) query hint with a value of `false` prevents a query from being run on the DFE at all, the `disableInterleaving` query hint with a value of `true` turns off DFE interleaving for translation of a query. For example:

```
g.with('Neptune#disableInterleaving', true)
 .V().has('genre','drama').in('likes')
```

## Updated Gremlin `explain` and `profile` output
<a name="gremlin-with-dfe-explain-update"></a>

Gremlin [explain](gremlin-explain.md) provides details about the optimized traversal that Neptune uses to run a query. See the [sample DFE `explain` output](gremlin-explain-api.md#gremlin-explain-dfe) for an example of what `explain` output looks like when DFE is enabled.

The [Gremlin `profile` API](gremlin-profile-api.md) runs a specified Gremlin traversal, collects various metrics about the run, and produces a profile report that contains details about the optimized query plan and the runtime statistics of various operators. See [sample DFE `profile` output](gremlin-profile-api.md#gremlin-profile-sample-dfe-output) for an example of what `profile` output looks like when DFE is enabled.

**Note**  
As of Neptune engine release 1.5.0.0, DFE support for Gremlin is no longer considered experimental. In engine releases before 1.5.0.0, DFE support for Gremlin was experimental and the exact format of the `explain` and `profile` output was subject to change. See [Neptune engine releases before 1.5.0.0](gremlin-step-coverage-in-DFE.md#gremlin-step-coverage-in-DFE-pre15) for the limitations that applied to earlier releases.