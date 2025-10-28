# Analyzing Neptune query execution using SPARQL `explain`

Amazon Neptune has added a SPARQL feature named _explain_. This feature is
a self-service tool for understanding the execution approach taken by the Neptune engine. You
invoke it by adding an `explain` parameter to an HTTP call that submits a SPARQL
query.

The `explain` feature provides information about the logical structure of query
execution plans. You can use this information to identify potential evaluation and execution
bottlenecks. You can then use [query hints](sparql-query-hints.md "sparql-query-hints.md") to improve
your query execution plans.

###### Topics

- [How the SPARQL query engine works in Neptune](sparql-explain-engine.md "sparql-explain-engine.md")
- [How to use SPARQL explain to analyze Neptune query
  execution](sparql-explain-using.md "sparql-explain-using.md")
- [Examples of invoking SPARQL explain in Neptune](sparql-explain-examples.md "sparql-explain-examples.md")
- [Neptune SPARQL explain operators](sparql-explain-operators.md "sparql-explain-operators.md")
- [Limitations of SPARQL explain in Neptune](sparql-explain-limitations.md "sparql-explain-limitations.md")
