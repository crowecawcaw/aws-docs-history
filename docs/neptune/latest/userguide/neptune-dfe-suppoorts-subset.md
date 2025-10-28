# Query constructs supported by the Neptune DFE

Currently, the Neptune DFE supports a subset of SPARQL and Gremlin query constructs.

For SPARQL, this is the subset of conjunctive [basic graph
patterns](https://www.w3.org/TR/sparql11-query/#BasicGraphPatterns "https://www.w3.org/TR/sparql11-query/#BasicGraphPatterns").

For Gremlin, it is generally the subset of queries that contain a chain of
traversals which do not contain some of the more complex steps.

You can find out whether one of your queries is being executed in whole or in part
by the DFE as follows:

- In Gremlin, `explain` and `profile` results tell you
  what parts of a query are being executed by the DFE, if any. See
  [Information contained in a Gremlin explain report](gremlin-explain-api.md#gremlin-explain-api-results "gremlin-explain-api.md#gremlin-explain-api-results")
  for `explain` and [DFE profile reports](gremlin-profile-api.md#gremlin-profile-dfe-output "gremlin-profile-api.md#gremlin-profile-dfe-output") for `profile`.
  Also, see [Tuning Gremlin queries using explain and profile](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md").

Details about Neptune engine support for individual Gremlin steps are documented in
[Gremlin step support](gremlin-step-support.md "gremlin-step-support.md").

- Similarly, SPARQL `explain` tells you whether a SPARQL query is being
  executed by the DFE. See [Example of SPARQL explain output when the DFE is enabled](sparql-explain-examples.md#sparql-explain-output-dfe "sparql-explain-examples.md#sparql-explain-output-dfe")
  and [DFENode operator](sparql-explain-operators.md#sparql-explain-operator-dfenode "sparql-explain-operators.md#sparql-explain-operator-dfenode")
  for more details.
