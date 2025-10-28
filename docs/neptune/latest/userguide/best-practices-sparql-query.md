# Querying All Named Graphs by Default

Amazon Neptune associates every triple with a named graph. The default graph is defined
as the union of all named graphs.

If you submit a SPARQL query without explicitly specifying a graph via the
`GRAPH` keyword or constructs such as `FROM NAMED`, Neptune always
considers all triples in your DB instance. For example, the following query returns all
triples from a Neptune SPARQL endpoint:

```
SELECT * WHERE { ?s ?p ?o }
```

Triples that appear in more than one graph are returned only once.

For information about the default graph specification, see the [RDF Dataset](https://www.w3.org/TR/sparql11-query/#rdfDataset "https://www.w3.org/TR/sparql11-query/#rdfDataset") section of the
SPARQL 1.1 Query Language specification.
