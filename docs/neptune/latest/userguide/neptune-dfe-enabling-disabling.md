# Controlling where the Neptune DFE engine is used

By default, the [neptune_dfe_query_engine](parameters.md#parameters-instance-parameters-neptune_dfe_query_engine "parameters.md#parameters-instance-parameters-neptune_dfe_query_engine")
instance parameter of an instance is set to `viaQueryHint`, which causes
the DFE engine to be used only for openCypher queries and for Gremlin and SPARQL queries
that explicitly include the `useDFE` query hint set to `true`.

You can fully enable the DFE engine so that it is used wherever possible by setting
the `neptune_dfe_query_engine` instance parameter to `enabled`.

You can also disable the DFE by including the `useDFE` query hint
for a particular [Gremlin query](gremlin-query-hints-useDFE.md "gremlin-query-hints-useDFE.md") or
[SPARQL query](sparql-query-hints-useDFE.md "sparql-query-hints-useDFE.md"). This query hint lets
you prevent the DFE from executing that particular query.

You can determine whether or not the DFE is enabled in an instance using an [Instance Status](access-graph-status.md "access-graph-status.md") call,
like this:

```
curl -G https://`your-neptune-endpoint`:`port`/status
```

The status response then specifies whether the DFE is enabled or not:

```
{
  "status":"healthy",
  "startTime":"Wed Dec 29 02:29:24 UTC 2021",
  "dbEngineVersion":"development",
  "role":"writer",
  "dfeQueryEngine":"viaQueryHint",
  "gremlin":{"version":"tinkerpop-3.5.2"},
  "sparql":{"version":"sparql-1.1"},
  "opencypher":{"version":"Neptune-9.0.20190305-1.0"},
  "labMode":{
    "ObjectIndex":"disabled",
    "ReadWriteConflictDetection":"enabled"
  },
  "features":{
    "ResultCache":{"status":"disabled"},
    "IAMAuthentication":"disabled",
    "Streams":"disabled",
    "AuditLog":"disabled"
  },
  "settings":{"clusterQueryTimeoutInMs":"120000"}
}
```

The Gremlin `explain` and `profile` results tell you
whether a query is being executed by the DFE. See [Information contained in a Gremlin explain report](gremlin-explain-api.md#gremlin-explain-api-results "gremlin-explain-api.md#gremlin-explain-api-results") for `explain` and [DFE profile reports](gremlin-profile-api.md#gremlin-profile-dfe-output "gremlin-profile-api.md#gremlin-profile-dfe-output")
for `profile`.

Similarly, SPARQL `explain` tells you whether a SPARQL query is being
executed by the DFE. See [Example of SPARQL explain output when the DFE is enabled](sparql-explain-examples.md#sparql-explain-output-dfe "sparql-explain-examples.md#sparql-explain-output-dfe")
and [DFENode operator](sparql-explain-operators.md#sparql-explain-operator-dfenode "sparql-explain-operators.md#sparql-explain-operator-dfenode")
for more details.
