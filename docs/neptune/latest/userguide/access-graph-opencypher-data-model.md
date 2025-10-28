# openCypher data model

The Neptune openCypher engine builds on the same property-graph model as Gremlin.
In particular:

- Every node has one or more labels. If you insert a node without labels,
  a default label named `vertex` is attached. If you try to delete all of a node's labels,
  an error is thrown.
- A relationship is an entity that has exactly one relationship type
  and that forms a unidirectional connection between two nodes (that is,
  _from_ one of the nodes _to_ the other).
- Both nodes and relationships can have properties, but don't have to.
  Neptune supports nodes and relationships with zero properties.
- Neptune does not support metaproperties, which are not included in
  the openCypher specification either.
- Properties in your graph can be multi-valued if they were created
  using Gremlin. That is a node or relationship property can have a set of different
  values rather than only one. Neptune has extended openCypher semantics to handle
  multi-valued properties gracefully.
  Supported data types are documented in [openCypher data format](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md").
  However, we do not recommend inserting `Array` property values into an openCypher
  graph at present. Although it is possible to insert an array property value
  using the bulk loader, the current Neptune openCypher release treats it as a set of
  multi-valued properties instead of as a single list value.

Below is the list of data types supported in this release:

- `Bool`
- `Byte`
- `Short`
- `Int`
- `Long`
- `Float` (Includes plus and minus Infinity and NaN, but not INF)
- `Double` (Includes plus and minus Infinity and NaN, but not INF)
- `DateTime`
- `String`
