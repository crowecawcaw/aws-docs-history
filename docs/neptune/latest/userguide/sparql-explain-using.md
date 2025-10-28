# How to use SPARQL `explain` to analyze Neptune query

execution

The SPARQL `explain` feature is a self-service tool in Amazon Neptune that helps
you understand the execution approach taken by the Neptune engine. To invoke
`explain`, you pass a parameter to an HTTP or HTTPS request in the form
`explain=`mode``.

The mode value can be one of `static` `dynamic`, or `details`:

- In _static_ mode, `explain` prints
  only the static structure of the query plan.
- In _dynamic_ mode, `explain` also includes dynamic aspects of
  the query plan. These aspects might include the number of intermediate bindings flowing
  through the operators, the ratio of incoming bindings to outgoing bindings, and the total
  time taken by operators.
- In _details_ mode, `explain` prints
  the information shown in `dynamic` mode plus additional details such as
  the actual SPARQL query string and the estimated range count for the pattern underlying
  a join operator.
  Neptune supports using `explain` with all three SPARQL query
  access protocols listed in the [W3C SPARQL 1.1
  Protocol](https://www.w3.org/TR/sparql11-protocol/#query-operation "https://www.w3.org/TR/sparql11-protocol/#query-operation") specification, namely:

1. HTTP GET
2. HTTP POST using URL-encoded parameters
3. HTTP POST using text parameters
   For information about the SPARQL query engine, see [How the SPARQL query engine works in Neptune](sparql-explain-engine.md "sparql-explain-engine.md").

For information about the kind of output produced by invoking SPARQL `explain`,
see [Examples of invoking SPARQL explain in Neptune](sparql-explain-examples.md "sparql-explain-examples.md").
