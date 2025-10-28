# Using SPARQL to access graph data in Amazon Neptune

SPARQL is a query language for the Resource Description Framework (RDF), which is a
graph data format designed for the web. Amazon Neptune is compatible with SPARQL 1.1. This
means that you can connect to a Neptune DB instance and query the graph using the query language
described in the [SPARQL 1.1 Query
Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/") specification.

A query in SPARQL consists of a `SELECT` clause to specify the variables to
return and a `WHERE` clause to specify which data to match in the graph. If you
are unfamiliar with SPARQL queries, see [Writing Simple
Queries](https://www.w3.org/TR/sparql11-query/#WritingSimpleQueries "https://www.w3.org/TR/sparql11-query/#WritingSimpleQueries") in the [SPARQL 1.1 Query
Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/").

The HTTP endpoint for SPARQL queries to a Neptune DB instance is
`https://`your-neptune-endpoint`:`port`/sparql`.

###### To connect to SPARQL

1. You can get the SPARQL endpoint for your Neptune cluster from the
   **SparqlEndpoint** item in the **Outputs** section of
   the AWS CloudFormation stack.
2. Enter the following to submit a SPARQL **`UPDATE`** using HTTP `POST` and the **curl** command.

```
curl -X POST --data-binary 'update=INSERT DATA { <https://test.com/s> <https://test.com/p> <https://test.com/o> . }' https://`your-neptune-endpoint`:`port`/sparql
```

The preceding example inserts the following triple into the SPARQL default graph:
`<https://test.com/s> <https://test.com/p> <https://test.com/o>` 3. Enter the following to submit a SPARQL **`QUERY`** using HTTP `POST` and the **curl** command.

```
curl -X POST --data-binary 'query=select ?s ?p ?o where {?s ?p ?o} limit 10' https://`your-neptune-endpoint`:`port`/sparql
```

The preceding example returns up to 10 of the triples (subject-predicate-object) in
the graph by using the `?s ?p ?o` query with a limit of 10. To query for
something else, replace it with another SPARQL query.

###### Note

The default MIME type of a response is
`application/sparql-results+json` for `SELECT` and
`ASK` queries.

The default MIME type of a response is `application/n-quads` for
`CONSTRUCT` and `DESCRIBE` queries.

For a list of all available MIME types, see [SPARQL HTTP API](sparql-api-reference.md "sparql-api-reference.md").
