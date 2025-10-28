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
    "TO_LIST" to export all values as a list, or "PICK_FIRST" to export the first value encountered. If not specified,
    the default value is "PICK_FIRST".

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
    "TO_LIST" to export all values as a list, or "PICK_FIRST" to export the first value encountered. If not specified,
    the default value is "PICK_FIRST".

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
