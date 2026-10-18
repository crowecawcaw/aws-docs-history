

# Query constructs supported by Neptune DFE
<a name="neptune-dfe-suppoorts-subset"></a>

Neptune DFE supports SPARQL and Gremlin query constructs. For SPARQL, DFE handles the subset of conjunctive [basic graph patterns](https://www.w3.org/TR/sparql11-query/#BasicGraphPatterns). For Gremlin, starting with Neptune engine release 1.5.0.0, DFE natively supports most Gremlin steps. For a categorized list of supported and unsupported Gremlin steps, see [Gremlin step coverage in DFE](gremlin-step-coverage-in-DFE.md).

You can find out whether one of your queries is being executed in whole or in part by DFE as follows:
+ In Gremlin, `explain` and `profile` results tell you what parts of a query are being executed by DFE, if any. See [Information contained in a Gremlin `explain` report](gremlin-explain-api.md#gremlin-explain-api-results) for `explain` and [DFE `profile` reports](gremlin-profile-api.md#gremlin-profile-dfe-output) for `profile`. Also, see [Tuning Gremlin queries using `explain` and `profile`](gremlin-traversal-tuning.md).

  Details about Neptune engine support for individual Gremlin steps are documented in [Gremlin step support](gremlin-step-support.md).
+ Similarly, SPARQL `explain` tells you whether a SPARQL query is being executed by DFE. See [Example of SPARQL `explain` output when the DFE is enabled](sparql-explain-examples.md#sparql-explain-output-dfe) and [`DFENode` operator](sparql-explain-operators.md#sparql-explain-operator-dfenode) for more details.