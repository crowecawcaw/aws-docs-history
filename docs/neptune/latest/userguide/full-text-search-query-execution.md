# Full-text-search query execution

in Amazon Neptune

In a query that includes full-text-search, Neptune tries to put the full-text-search
calls first, before other parts of the query. This reduces the number of calls to
OpenSearch and in most cases significantly improves performance. However, this is
by no means a hard-and-fast rule. There are situations, for example, where
a `PatternNode` or `UnionNode` may precede a full-text search call.

Consider the following Gremlin query to a database that contains
100,000 instances of `Person`:

```
g.withSideEffect('Neptune#fts.endpoint', '`your-es-endpoint-URL`')
 .hasLabel('Person')
 .has('name', 'Neptune#fts marcello~');
```

If this query were executed in the order in which the steps appear then 100,000
solutions would flow into OpenSearch, causing hundreds of OpenSearch calls.
In fact, Neptune calls OpenSearch first and then joins results with the Neptune
results. In most cases, this is much faster than executing the query in the original order.

You can prevent this re-ordering of query-step execution using the [noReordering query hint](gremlin-query-hints-noReordering.md "gremlin-query-hints-noReordering.md"):

```
g.withSideEffect('Neptune#fts.endpoint', '`your-es-endpoint-URL`')
 .withSideEffect('Neptune#noReordering', true)
 .hasLabel('Person')
 .has('name', 'Neptune#fts marcello~');
```

In this second case, the `.hasLabel` step is executed first and the
`.has('name', 'Neptune#fts marcello~')` step second.

For another example, consider a SPARQL query against the same kind of data:

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX neptune-fts: <http://aws.amazon.com/neptune/vocab/v01/services/fts#>
SELECT ?person WHERE {
  ?person rdf:type foaf:Person .
  SERVICE neptune-fts:search {
    neptune-fts:config neptune-fts:endpoint '`http://your-es-endpoint.com`' .
    neptune-fts:config neptune-fts:field foaf:name .
    neptune-fts:config neptune-fts:query 'mike' .
    neptune-fts:config neptune-fts:return ?person .
  }
}
```

Here again, Neptune executes the `SERVICE` part of the query first,
and then joins the results with the `Person` data. You can suppress this
behavior using the [joinOrder query
hint](sparql-query-hints-joinOrder.md "sparql-query-hints-joinOrder.md"):

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX neptune-fts: <http://aws.amazon.com/neptune/vocab/v01/services/fts#>
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT ?person WHERE {
  hint:Query hint:joinOrder "Ordered" .
  ?person rdf:type foaf:Person .
  SERVICE neptune-fts:search {
    neptune-fts:config neptune-fts:endpoint '`http://your-es-endpoint.com`' .
    neptune-fts:config neptune-fts:field foaf:name .
    neptune-fts:config neptune-fts:query 'mike' .
    neptune-fts:config neptune-fts:return ?person .
  }
}
```

Again, in the second query the parts are executed in the order they appear
in the query.

###### Note

Querying an opensearch alias over an index, instead of directly querying an opensearch index can produce incorrect results.
You should query the opensearch index directly and not the alias.
