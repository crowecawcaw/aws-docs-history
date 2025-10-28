# Serialization Formats in Neptune Streams

Amazon Neptune uses two different formats for serializing graph-changes data to log streams,
depending on whether the graph was created using Gremlin or SPARQL.

Both formats share a common record serialization format, as described in [Neptune Streams API Response Format](streams-using-api-reponse.md "streams-using-api-reponse.md"), that
contains the following fields:

- `commitTimestamp`   –  
  The time at which the commit for the transaction was requested,
  in milliseconds from the Unix epoch.
- `eventId`   –  
  The sequence identifier of the stream change record.
- `data`   –  
  The serialized Gremlin, SPARQL, or OpenCypher change record.
  The serialization formats of each record are described in more
  detail in the next sections.
- `op`   –  
  The operation that created the change.

###### Topics

- [PG_JSON Change Serialization
  Format](#streams-change-formats-gremlin "#streams-change-formats-gremlin")
- [SPARQL NQUADS Change Serialization
  Format](#streams-change-formats-sparql "#streams-change-formats-sparql")

## PG_JSON Change Serialization

Format

###### Note

As of [engine release 1.1.0.0](engine-releases-1.1.0.md "engine-releases-1.1.0.md"),
the Gremlin stream output format (`GREMLIN_JSON`) output by the Gremlin
stream endpoint (`https://`Neptune-DNS`:8182/gremlin/stream`)
is being deprecated. It is replaced by PG_JSON, which is currently identical to
`GREMLIN_JSON`.

A Gremlin or openCypher change record, contained in the `data` field
of a log stream response, has the following fields:

- `id` – String, required.

The ID of the Gremlin or openCypher element.

- `type` – String, required.

The type of this Gremlin or openCypher element. Must be one of the following:

    + `vl` – Vertex label for Gremlin; node label for openCypher.
    + `vp` – Vertex properties for Gremlin; node properties for openCypher.
    + `e` – Edge and edge label for Gremlin; relationship and relationship type for openCypher.
    + `ep` – Edge properties for Gremlin; relationship properties for openCypher.

- `key` – String, required.

The property name. For element labels, this is "label".

- `value` – `value` object, required.

This is a JSON object that contains a `value` field for the value itself,
and a `datatype` field for the JSON data type of that value.

```
  "value": {
    "value": "`the new value`",
    "dataType": "`the JSON datatype of the new value`"
  }
```

- `from` – String, optional.

If this is an edge (type="e"), the ID of the corresponding
_from_ vertex or source node.

- `to` – String, optional.

If this is an edge (type="e"), the ID of the corresponding
_to_ vertex or target node.

###### Gremlin Examples

- The following is an example of a Gremlin vertex label.

```
{
  "id": "`an ID string`",
  "type": "vl",
  "key": "label",
  "value": {
    "value": "`the new value of the vertex label`",
    "dataType": "String"
  }
}
```

- The following is an example of a Gremlin vertex property.

```
{
  "id": "`an ID string`",
  "type": "vp",
  "key": "`the property name`",
  "value": {
    "value": "`the new value of the vertex property`",
    "dataType": "`the datatype of the vertex property`"
  }
}
```

- The following is an example of a Gremlin edge.

```
{
  "id": "`an ID string`",
  "type": "e",
  "key": "label",
  "value": {
    "value": "`the new value of the edge`",
    "dataType": "String"
  },
  "from": "`the ID of the corresponding "from" vertex`",
  "to": "`the ID of the corresponding "to" vertex`"
}
```

###### openCypher Examples

- The following is an example of an openCypher node label.

```
{
  "id": "`an ID string`",
  "type": "vl",
  "key": "label",
  "value": {
    "value": "`the new value of the node label`",
    "dataType": "String"
  }
}
```

- The following is an example of an openCypher node property.

```
{
  "id": "`an ID string`",
  "type": "vp",
  "key": "`the property name`",
  "value": {
    "value": "`the new value of the node property`",
    "dataType": "`the datatype of the node property`"
  }
}
```

- The following is an example of an openCypher relationship.

```
{
  "id": "`an ID string`",
  "type": "e",
  "key": "label",
  "value": {
    "value": "`the new value of the relationship`",
    "dataType": "String"
  },
  "from": "`the ID of the corresponding source node`",
  "to": "`the ID of the corresponding target node`"
}
```

## SPARQL NQUADS Change Serialization

Format

Neptune logs changes to SPARQL quads in the graph using the Resource Description
Framework (RDF) `N-QUADS` language defined in the [W3C RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/") specification.

The `data` field in the change record simply contains a `stmt` field
that holds an N-QUADS statement expressing the changed quad, as in the following
example.

```
  "stmt" : "<https://test.com/s> <https://test.com/p> <https://test.com/o> .\n"
```
