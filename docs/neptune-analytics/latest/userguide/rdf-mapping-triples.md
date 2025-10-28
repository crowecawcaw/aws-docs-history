# Mapping RDF triples to LPG concepts

There are three rules that define how RDF triples correspond to LPG concepts:

```
Case     RDF triple                   ⇆    LPG concept
-----------------------------------------------------------------
Case #1  { <iri> rdf:type <iri> }     ⇆    vertex with id + label
Case #2  { <iri> <iri> "literal"}     ⇆    vertex property
Case #3  { <iri> <iri> <iri> }        ⇆    edge with label
```

**Case #1: Vertex with id and label**

A triple like:

```
<http://example.com/Alice> rdf:type <http://xmlns.com/foaf/0.1/Person>
```

is equivalent to creating the vertex in openCypher like:

```
CREATE (:`<http://xmlns.com/foaf/0.1/Person>` {`~id`: "<http://example.com/Alice>"})
```

In this example, the vertex label `<http://xmlns.com/foaf/0.1/Person>` is interpreted
and stored as an IRI.

###### Note

The back quote syntax ```` is part of openCypher which allows inserting characters that
normally cannot be used in labels. Using this mechanism, it’s possible to include complete IRIs in a query.

Using `PREFIX`, the same `CREATE` query could look like:

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ex: <http://example.com/>
CREATE (: foaf::Person {`~id`: ex::Alice})
```

To match the newly created vertex based on its id:

```
MATCH (v {`~id`: "<http://example.com/Alice>"}) RETURN v
```

or equivalently:

```
PREFIX ex: <http://example.com/>
MATCH (v {`~id`: ex::Alice}) RETURN v
```

To find vertices with that RDF Class/LPG Label:

```
MATCH (v:`<http://xmlns.com/foaf/0.1/Person>`) RETURN v
```

or equivalently:

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
MATCH (v : foaf::Person) RETURN v
```

**Case #2: Vertex property**

A triple like:

```
<http://example.com/Alice> <http://xmlns.com/foaf/0.1/name> "Alice Smith"
```

is equivalent to defining with openCypher node with a given `~id` and property, where both the `~id`
and the property key are IRIs:

```
CREATE ({`~id`: "<http://example.com/Alice>",
        `<http://xmlns.com/foaf/0.1/name>`: "Alice Smith" })
```

or equivalently:

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ex: <http://example.com/>
CREATE ({`~id`: ex::Alice, foaf::name: "Alice Smith" })
```

To match the vertex with that property:

```
MATCH (v {`<http://xmlns.com/foaf/0.1/name>`: "Alice Smith"}) RETURN v
```

or equivalently:

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
MATCH (v { foaf::name : "Alice Smith"}) RETURN v
```

**Case #3: Edge**

A triple like:

```
<http://example.com/Alice> <http://example.com/knows> <http://example.com/Bob>
```

is equivalent to defining with OpenCypher an edge like this, where the edge label and vertices ids are all IRIs:

```
CREATE ({`~id`: "<http://example.com/Alice>"})
          -[:`<http://example.com/knows>`]->({`~id`: "<http://example.com/Bob>"})
```

or equivalently:

```
PREFIX ex: <http://example.com/>
CREATE ({`~id`: ex::Alice })-[: ex::knows ]->({`~id`: ex::Bob })
```

To match the edges with that label:

```
MATCH (v)-[:`<http://example.com/knows>`]->(w) RETURN v, w
```

or equivalently:

```
PREFIX ex: <http://example.com/>
MATCH (v)-[: ex::knows ]->(w) RETURN v, w
```

## Query Examples

**Matching language-tagged literals**

If this triple was loaded from a dataset:

```
<http://example.com/German> <http://example.com/greeting> "Hallo"@de
```

then it will **not** be matched by this query:

```
MATCH (n) WHERE n.`<http://example.com/greeting>` = "Hallo"
```

because the language-tagged literal `"Hallo"@de` and the string “Hallo” are not equal. For more information,
see [Language-tagged literals](using-rdf-data.md#rdf-handling-language-tagged-literals "using-rdf-data.md#rdf-handling-language-tagged-literals").
The query can use `TOSTRING()` in order to find the match:

```
MATCH (n) WHERE TOSTRING(n.`<http://example.com/greeting>`) = "Hallo"
```
