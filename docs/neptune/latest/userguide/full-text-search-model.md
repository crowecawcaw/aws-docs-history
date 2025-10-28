# Neptune data model for OpenSearch data

Amazon Neptune uses a unified JSON document structure for storing both SPARQL and Gremlin
data in OpenSearch Service. Each document in OpenSearch corresponds to an entity and stores all
the relevant information for that entity. For Gremlin, vertexes and edges are considered
entities, so the corresponding OpenSearch documents have information about vertexes,
labels, and properties. For SPARQL, subjects can be considered entities, so corresponding
OpenSearch documents have information about all the predicate-object pairs in one
document.

###### Note

The Neptune-to-OpenSearch replication implementation only stores
string data. However, you can modify it to store other data types.

The unified JSON document structure looks like the following.

```
{
  "entity_id": "`Vertex Id/Edge Id/Subject URI`",
  "entity_type": [`List of Labels/rdf:type object value`],
  "document_type": "`vertex/edge/rdf-resource`"
  "predicates": {
    "`Property name or predicate URI`": [
      {
        "value": "`Property Value or Object Value`",
        "graph": "`(Only for Sparql) Named Graph Quad is present`"
        "language": "`(Only for Sparql) rdf:langString`"
      },
      {
        "value": "`Property Value 2/ Object Value 2`",
      }
    ]
  }
}
```

######

- `entity_id` – Entity unique ID representing the
  document.
  - For SPARQL, this is the subject URI.
  - For Gremlin, this is the `Vertex_ID` or `Edge_ID`.

- `entity_type` – Represents one or more labels for
  a vertex or edge, or zero or more `rdf:type` predicate values for a subject.
- `document_type` – Used to specify whether the current document
  represents a vertex, edge, or rdf-resource.
- `predicates` – For Gremlin, stores properties and values for
  a vertex or edge. For SPARQL, it stores predicate-object pairs.

The property name takes the form `properties.name.value` in OpenSearch.
To query it, you have to name it in that form.

- `value`  – A property value for Gremlin or an object value for
  SPARQL.
- `graph` – A named graph for SPARQL.
- `language` – A language tag for a `rdf:langString`
  literal in SPARQL.

## Sample SPARQL OpenSearch document

**Data**

```
@prefix dt:   <http://example.org/datatype#> .
@prefix ex:   <http://example.org/> .
@prefix xsd:  <http://www.w3.org/2001/XMLSchema#> .
@prefix rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

ex:simone   rdf:type     ex:Person                    ex:g1
ex:michael  rdf:type     ex:Person                    ex:g1
ex:simone   ex:likes     "spaghetti"                  ex:g1

ex:simone   ex:knows     ex:michael                   ex:g2   # Not stored in ES
ex:simone   ex:likes     "spaghetti"                  ex:g2
ex:simone   ex:status    "La vita è un sogno"@it      ex:g2

ex:simone   ex:age       "40"^^xsd:int                DG      # Not stored in ES
ex:simone   ex:dummy     "testData"^^dt:newDataType   DG      # Not stored in ES
ex:simone   ex:hates     _:bnode                              # Not stored in ES
_:bnode     ex:means     "coding"                     DG      # Not stored in ES
```

**Documents**

```
{
  "entity_id": "http://example.org/simone",
  "entity_type": ["http://example.org/Person"],
  "document_type": "rdf-resource"
  "predicates": {
    "http://example.org/likes": [
      {
        "value": "spaghetti",
        "graph": "http://example.org/g1"
      },
      {
        "value": "spaghetti",
        "graph": "http://example.org/g2"
      }
    ]
    "http://example.org/status": [
      {
        "value": "La vita è un sogno",
        "language": "it"       // Only present for rdf:langString
      }
    ]
  }
}
```

```
{
  "entity_id" : "http://example.org/michael",
  "entity_type" : ["http://example.org/Person"],
  "document_type": "rdf-resource"
}
```

## Sample Gremlin OpenSearch document

**Data**

```
# Vertex 1
simone   label    Person       <== Label
simone   likes    "spaghetti"  <== Property
simone   likes    "rice"       <== Property
simone   age      40           <== Property

# Vertex 2
michael  label    Person       <== Label

# Edge 1
simone  knows     michael      <== Edge
e1      updated  "2019-07-03"  <== Edge Property
e1      through  "company"     <== Edge Property
e1      since     10           <== Edge Property
```

**Documents**

```
{
  "entity_id": "simone",
  "entity_type": ["Person"],
  "document_type": "vertex",
  "predicates": {
    "likes": [
      {
        "value": "spaghetti"
      },
      {
        "value": "rice"
      }
    ]
  }
}
```

```
{
  "entity_id" : "michael",
  "entity_type" : ["Person"],
  "document_type": "vertex"
}
```

```
{
  "entity_id": "e1",
  "entity_type": ["knows"],
  "document_type": "edge"
  "predicates": {
    "through": [
      {
        "value": "company"
      }
    ]
  }
}
```
