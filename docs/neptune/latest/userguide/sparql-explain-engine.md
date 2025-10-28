# How the SPARQL query engine works in Neptune

To use the information that the SPARQL `explain` feature provides, you need to
understand some details about how the Amazon Neptune SPARQL query engine works.

The engine translates every SPARQL query into a pipeline of operators. Starting from the
first operator, intermediate solutions known as _binding lists_ flow through
this operator pipeline. You can think of a binding list as a table in which the table headers
are a subset of the variables used in the query. Each row in the table represents a result, up
to the point of evaluation.

Let's assume that two namespace prefixes have been defined for our data:

```
  @prefix ex:   <http://example.com> .
  @prefix foaf: <http://xmlns.com/foaf/0.1/> .
```

The following would be an example of a simple binding list in this context:

```
  ?person       | ?firstName
  ------------------------------------------------------
  ex:JaneDoe    | "Jane"
  ex:JohnDoe    | "John"
  ex:RichardRoe | "Richard"
```

For each of three people, the list binds the `?person` variable
to an identifier of the person, and the `?firstName` variable to the
person's first name.

In the general case, variables can remain unbound, if, for example, there is an
`OPTIONAL` selection of a variable in a query for which no value is present in the
data.

The `PipelineJoin` operator is an example of a Neptune query engine operator
present in the `explain` output. It takes as input an incoming binding set from the
previous operator and joins it against a triple pattern, say `(?person, foaf:lastName,
 ?lastName)`. This operation uses the bindings for the `?person` variable in
its input stream, substitutes them into the triple pattern, and looks up triples from the database.

When executed in the context of the incoming bindings from the previous table,
`PipelineJoin` would evaluate three lookups, namely the following:

```
  (ex:JaneDoe,    foaf:lastName, ?lastName)
  (ex:JohnDoe,    foaf:lastName, ?lastName)
  (ex:RichardRoe, foaf:lastName, ?lastName)
```

This approach is called _as-bound_ evaluation. The solutions from this
evaluation process are joined back against the incoming solutions, padding the detected
`?lastName` in the incoming solutions. Assuming that you find a last name for all
three persons, the operator would produce an outgoing binding list that would look something
like this:

```

  ?person       | ?firstName | ?lastName
  ---------------------------------------
  ex:JaneDoe    | "Jane"     | "Doe"
  ex:JohnDoe    | "John"     | "Doe"
  ex:RichardRoe | "Richard"  | "Roe"
```

This outgoing binding list then serves as input for the next operator in the pipeline.
At the end, the output of the last operator in the pipeline defines the query result.

Operator pipelines are often linear, in the sense that every operator emits solutions for a
single connected operator. However, in some cases, they can have more complex structures. For
example, a `UNION` operator in a SPARQL query is mapped to a `Copy`
operation. This operation duplicates the bindings and forwards the copies into two subplans, one
for the left side and the other for the right side of the `UNION`.

For more information about operators, see [Neptune SPARQL explain operators](sparql-explain-operators.md "sparql-explain-operators.md").
