# Using Gremlin with the Neptune DFE query engine

If you enable Neptunes [alternative
query engine](neptune-dfe-engine.md "neptune-dfe-engine.md") known as the DFE in [lab mode](features-lab-mode.md "features-lab-mode.md")
(by setting the `neptune_lab_mode` DB cluster parameter
to `DFEQueryEngine=enabled`), then Neptune translates read-only Gremlin
queries/traversals into an intermediate logical representation and runs them on the DFE
engine whenever possible.

However, the DFE does not yet support all Gremlin steps. When a step can't
be run natively on the DFE, Neptune falls back on TinkerPop to run the
step. The `explain` and `profile` reports include warnings
when this happens.

## Query planning interleaving

When the translation process encounters a Gremlin step that does not have a
corresponding native DFE operator, before falling back to using Tinkerpop
it tries to find other intermediate query parts that can be run natively on
the DFE engine. It does this by applying interleaving logic to the top level traversal.
The result is that supported steps are used wherever possible.

Any such intermediate, non-prefix query translation is represented using
`NeptuneInterleavingStep` in the `explain` and `profile`
outputs.

For performance comparison, you might want to turn off interleaving in a query,
while still using the DFE engine to run the prefix part. Or, you might want to use
only the TinkerPop engine for non-prefix query execution. You can do this by using
`disableInterleaving` query hint.

Just as the [useDFE](gremlin-query-hints-useDFE.md "gremlin-query-hints-useDFE.md") query hint with a value of
`false` prevents a query from being run on the DFE at all, the
`disableInterleaving` query hint with a value of `true`
turns off DFE interleaving for translation of a query. For example:

```
g.with('Neptune#disableInterleaving', true)
 .V().has('genre','drama').in('likes')
```

## Updated Gremlin `explain` and `profile` output

Gremlin [explain](gremlin-explain.md "gremlin-explain.md") provides details about the
optimized traversal that Neptune uses to run a query. See the
[sample DFE explain output](gremlin-explain-api.md#gremlin-explain-dfe "gremlin-explain-api.md#gremlin-explain-dfe") for
an example of what `explain` output looks like when the DFE engine is enabled.

The [Gremlin profile API](gremlin-profile-api.md "gremlin-profile-api.md")
runs a specified Gremlin traversal, collects various metrics about the run, and produces
a profile report that contains details about the optimized query plan and the runtime
statistics of various operators. See [sample
DFE profile output](gremlin-profile-api.md#gremlin-profile-sample-dfe-output "gremlin-profile-api.md#gremlin-profile-sample-dfe-output") for an example of what `profile` output
looks like when the DFE engine is enabled.

###### Note

Because the DFE engine is an experimental feature released in lab mode,
the exact format of the `explain` and `profile` output is
subject to change.
