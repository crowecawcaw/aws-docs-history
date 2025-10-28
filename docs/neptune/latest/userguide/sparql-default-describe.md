# SPARQL DESCRIBE behavior with respect to the default graph

The SPARQL [`DESCRIBE`](https://www.w3.org/TR/sparql11-query/#describe "https://www.w3.org/TR/sparql11-query/#describe")
query form lets you retrieve information about resources without knowing the
structure of the data and without having to compose a query. How this
information is assembled is left up to the SPARQL implementation. Neptune
provides [several query hints](sparql-query-hints-for-describe.md "sparql-query-hints-for-describe.md")
that invoke different modes and algorithms for `DESCRIBE` to use.

In Neptune's implementation, regardless of the mode, `DESCRIBE`
only uses data present in the [SPARQL default
graph](feature-sparql-compliance.md#sparql-default-graph "feature-sparql-compliance.md#sparql-default-graph"). This is consistent with the way SPARQL treats datasets (see
[Specifying
RDF Datasets](https://www.w3.org/TR/sparql11-query/#specifyingDataset "https://www.w3.org/TR/sparql11-query/#specifyingDataset") in the SPARQL specification).

In Neptune, the default graph contains all unique triples in the union of all
named graphs in the database, unless particular named graphs are specified
using `FROM` and/or `FROM NAMED` clauses. All RDF data in
Neptune is stored in a named graph. If a triple is inserted without a named-graph
context, Neptune stores it in a named graph designated
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.

When one or more named graphs are specified using the `FROM` clause,
the default graph is the union of all unique triples in those named graphs. If
there is no `FROM` clause and there are one or more `FROM NAMED`
clauses, then the default graph is empty.

## SPARQL `DESCRIBE` examples

Consider the following data:

```
PREFIX ex: <https://example.com/>

GRAPH ex:g1 {
    ex:s ex:p1 "a" .
    ex:s ex:p2 "c" .
}

GRAPH ex:g2 {
    ex:s ex:p3 "b" .
    ex:s ex:p2 "c" .
}

ex:s ex:p3 "d" .
```

For this query:

```
PREFIX ex: <https://example.com/>
DESCRIBE ?s
FROM ex:g1
FROM NAMED ex:g2
WHERE {
  GRAPH ex:g2 { ?s ?p "b" . }
}
```

Neptune would return:

```
ex:s ex:p1 "a" .
ex:s ex:p2 "c" .
```

Here, the graph pattern `GRAPH ex:g2 { ?s ?p "b" }`
is evaluated first, resulting in bindings for `?s`, and
then the `DESCRIBE` part is evaluated over the default
graph, which is now just `ex:g1`.

However, for this query:

```
PREFIX ex: <https://example.com/>
DESCRIBE ?s
FROM NAMED ex:g1
WHERE {
  GRAPH ex:g1 { ?s ?p "a" . }
}
```

Neptune would return nothing, because when a `FROM NAMED`
clause is present without any `FROM` clause, the default graph
is empty.

In the following query, `DESCRIBE` is used with no
`FROM` or `FROM NAMED` clause present:

```
PREFIX ex: <https://example.com/>
DESCRIBE ?s
WHERE {
  GRAPH ex:g1 { ?s ?p "a" . }
}
```

In this situation, the default graph is composed of all the
unique triples in the union of all the named graphs in the
database (formally, the RDF merge), so Neptune would return:

```
ex:s ex:p1 "a" .
ex:s ex:p2 "c" .
ex:s ex:p3 "b" .
ex:s ex:p3 "d" .
```
