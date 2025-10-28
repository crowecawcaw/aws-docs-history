# Neptune Graph Data Model

The basic unit of Amazon Neptune graph data is a four-position (quad) element, which is
similar to a Resource Description Framework (RDF) quad. The following are the four positions of
a Neptune quad:

- `subject    (S)`
- `predicate  (P)`
- `object     (O)`
- `graph      (G)`
  Each quad is a statement that makes an assertion about one or more resources. A statement
  can assert the existence of a relationship between two resources, or it can attach a property
  (key-value pair) to a resource. You can think of the quad predicate value generally as the
  verb of the statement. It describes the type of relationship or property that's being defined.
  The object is the target of the relationship, or the value of the property. The following are
  examples:

- A relationship between two vertices can be represented by storing the source
  vertex identifier in the `S` position, the target vertex identifier in the
  `O` position, and the edge label in the `P` position.
- A property can be represented by storing the element identifier in the
  `S` position, the property key in the `P` position, and the property
  value in the `O` position.
  The graph position `G` is used differently in the different stacks. For RDF
  data in Neptune, the `G` position contains a [named graph identifier](https://www.w3.org/TR/rdf11-concepts/#section-dataset "https://www.w3.org/TR/rdf11-concepts/#section-dataset").
  For property graphs in Gremlin, it is used to store the edge ID value in the case of an edge.
  In all other cases, it defaults to a fixed value.

A set of quad statements with shared resource identifiers creates a graph.
