# Specifying a filter

The `vertexFilter` is used to specify filters on a per-label basis for vertices. This allows you to control which
vertex labels and properties are included in the export.

- `vertexFilter` - This is the top-level field for specifying vertex filters.
- If the `vertexFilter` is not provided at all, then all vertex properties for all vertex labels will be
  exported. If the `vertexFilter` is provided but is an empty object, then no vertices will be exported.
- Each key in the `vertexFilter` object corresponds to a vertex label that you want to describe a filter for.
  For example, `"Person"` or `"Organization"`.
- For each vertex label key, the value is an object with a `"properties"` field.
- The "properties" field allows you to specify which properties of that vertex label should be included in
  the export. Each property is defined by a key-value pair, where the key is the desired output property name (e.g.
  `"name"`), and the value is an object with the following fields:

  - `outputType`: Specifies the data type to use for the property in the exported data (e.g.
    "String", "Int", "Float"). For a full-list of supported types and the corresponding type names that can be
    used in filtering, see [Using CSV data](using-CSV-data.md "using-CSV-data.md"). If a type is not provided,
    the export process
    will determine the type. If a given property is present as multiple types (e.g. one vertex has `"height"`
    stored as a double, and another edge has it stored as a string), the type will be of `Any` type. Otherwise, it
    will be the type of the property as present in vertices.
  - `sourcePropertyName`: The name of the property as it exists in the original graph data. If not provided,
    it is assumed that the key matches the desired `sourcePropertyName`.
  - `multiValueHandling`: Specifies how to handle properties that have multiple values. Can be either
    "TO\_LIST" to export all values as a list, or "PICK\_FIRST" to export the first value encountered. If not specified,
    the default value is "PICK\_FIRST".

`edgeFilter` is used to specify filters on a per-label basis for edges. This allows you to control which edge labels and
properties are included in the export.

- `edgeFilter` - This is the top-level field for specifying edge filters.
- If the `edgeFilter` is not provided at all, then all edge properties for all edge labels will be
  exported. If the `edgeFilter` is provided but is an empty object, then no edges will be exported.
- Each key in the `edgeFilter` object corresponds to a edge label that you want to describe a filter for.
  For example, `"knows"` or `"friendOf"`.
- For each edge label key, the value is an object with a `"properties"` field.
- The "properties" field allows you to specify which properties of that edge label should be included in
  the export. Each property is defined by a key-value pair, where the key is the desired output property name (e.g.
  `"weight"`), and the value is an object with the following fields:

  - `outputType`: Specifies the data type to use for the property in the exported data (e.g.
    "String", "Int", "Float"). For a full-list of supported types and the corresponding type names that can be
    used in filtering, see `here`. If a type is not provided, the export process
    will determine the type. If a given property is present as multiple types (e.g. one edge has `"weight"`
    stored as a double, and another edge has it stored as a string), the type will be of Any type. Otherwise, it
    will be the type of the property as present in edges.
  - `sourcePropertyName`: The name of the property as it exists in the original graph data. If not provided,
    it is assumed that the key matches the desired `sourcePropertyName`.
  - `multiValueHandling`: Specifies how to handle properties that have multiple values. Can be either
    "TO\_LIST" to export all values as a list, or "PICK\_FIRST" to export the first value encountered. If not specified,
    the default value is "PICK\_FIRST".

## Filter syntax

The filter is specified as a JSON object, as follows:

```
{
    "vertexFilter": {"string": {
          "properties": {"string": {
                "outputType": "string",
                "sourcePropertyName": "string",
                "multiValueHandling": "TO_LIST"|"PICK_FIRST"
                }
            ...}
            }
      ...},
    "edgeFilter": {"string": {
          "properties": {"string": {
                "outputType": "string",
                "sourcePropertyName": "string",
                "multiValueHandling": "TO_LIST"|"PICK_FIRST"
            }
        ...}
        }
  ...}
}
```

## Filtering label-less vertices and default-labeled edges

Neptune Analytics supports loading vertices without labels and assigns a default label `"edge"`
to edges that have no explicit label. The export filter provides special keys to target these
entities.

### Filtering label-less vertices

Neptune Analytics supports vertices without labels (vertices loaded with an empty
`~label` value or with the `~label` column omitted from the
file). To include such vertices in an export, there are three ways:

1. **Omit `vertexFilter` entirely.**
   If you do not specify a `vertexFilter`, all vertices are exported
   regardless of label, including label-less ones.
2. **Include `"_NO_LABEL_"` (or equivalently
   `""`) as a `vertexFilter` key.**
   Use the sentinel key to target label-less vertices alongside your typed
   labels:

```
{
  "vertexFilter": {
    "Person": { "properties": {} },
    "_NO_LABEL_": {
      "properties": {
        "name": { "outputType": "String" }
      }
    }
  }
}
```

Both `"_NO_LABEL_"` and `""` match the same set of
vertices — those loaded without a `~label` value. 3. **Use the `"*"` wildcard.**
The wildcard key matches all vertex labels including label-less vertices.

###### Warning

If your `vertexFilter` names only explicitly-typed labels (for
example, `"Person"` and `"Organization"`) but your graph
contains label-less vertices, those vertices are silently excluded from the
export. To avoid unexpected data loss, use one of the three approaches listed
above.

### Filtering default-labeled edges

Because every edge in Neptune Analytics has a label (edges loaded without an explicit
`~label` are assigned the default label `"edge"`), there are three
ways to include such edges in an export:

1. **Omit `edgeFilter` entirely.**
   If you do not specify an `edgeFilter`, all edges are exported regardless
   of label, including default-labeled ones.
2. **Include `"edge"` as an
   `edgeFilter` key.**
   Use the literal string `"edge"` (not `"_NO_LABEL_"`) to
   target default-labeled edges alongside your typed labels:

```
{
  "edgeFilter": {
    "route": { "properties": {} },
    "edge": { "properties": {} }
  }
}
```

3. **Use the `"*"` wildcard.**
   The wildcard key matches all edge labels including the default
   `"edge"` label.

###### Warning

If your `edgeFilter` names only explicitly-typed labels (for example,
`"route"` and `"knows"`) but your graph contains edges that
were loaded without a `~label`, those default-labeled edges are silently
excluded from the export. To avoid unexpected data loss, use one of the three
approaches listed above.

###### Note

Do **not** use `"_NO_LABEL_"` as an
`edgeFilter` key to try to target default-labeled edges. Unlike vertices,
edges are never truly label-less — the loader always assigns
`"edge"` as the label when `~label` is missing or empty. An
`edgeFilter` that names `"_NO_LABEL_"` matches zero edges and
exports no edge files.

### Non-existent labels in filters

If a filter key names a label that is not present among the graph's labels, the export
fails with a `NotFound` error during initialization, before any data is
written. This fail-fast behavior helps catch typos in filter specifications.

###### Note

The sentinel keys `"_NO_LABEL_"`, `""`,
`"_VERTEX_ALL_LABELS_"`, `"_EDGE_ALL_LABELS_"`, and
`"*"` are always accepted and are not checked against the graph's labels.
