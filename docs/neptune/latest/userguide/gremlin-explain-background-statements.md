# Gremlin statements in Neptune

Property graph data in Amazon Neptune is composed of four-position (quad) statements. Each
of these statements represents an individual atomic unit of property graph data. For more
information, see [Neptune Graph Data Model](feature-overview-data-model.md "feature-overview-data-model.md"). Similar to the Resource Description Framework
(RDF) data model, these four positions are as follows:

- `subject (S)`
- `predicate (P)`
- `object (O)`
- `graph (G)`
  Each statement is an assertion about one or more resources. For example, a statement can
  assert the existence of a relationship between two resources, or it can attach a property
  (key-value pair) to some resource.

You can think of the predicate as the verb of the statement, describing the type of
relationship or property. The object is the target of the relationship, or the value of the
property. The graph position is optional and can be used in many different ways. For the
Neptune property graph (PG) data, it is either unused (null graph) or it is used to
represent the identifier for an edge. A set of statements with shared resource identifiers
creates a graph.

There are three classes of statements in the Neptune property graph data model:

###### Topics

- [Vertex Label Statements](#gremlin-explain-background-vertex-labels "#gremlin-explain-background-vertex-labels")
- [Edge Statements](#gremlin-explain-background-edge-statements "#gremlin-explain-background-edge-statements")
- [Property Statements](#gremlin-explain-background-property-statements "#gremlin-explain-background-property-statements")

## Gremlin Vertex Label Statements

Vertex label statements in Neptune serve two purposes:

- They track the labels for a vertex.
- The presence of at least one of these statements is what implies
  the existence of a particular vertex in the graph.

The subject of these statements is a vertex identifier, and the object is a label, both
of which are specified by the user. You use a special fixed predicate for these statements,
displayed as `<~label>`, and a default graph identifier (the null graph),
displayed as `<~>`.

For example, consider the following `addV` traversal.

```
g.addV("Person").property(id, "v1")
```

This traversal results in the following statement being added to the graph.

```
StatementEvent[Added(<v1> <~label> <Person> <~>) .]
```

## Gremlin Edge Statements

A Gremlin edge statement is what implies the existence of an edge between two vertices
in a graph in Neptune. The subject (S) of an edge statement is the source
`from` vertex. The predicate (P) is a user-supplied edge label. The object (O)
is the target `to` vertex. The graph (G) is a user-supplied edge
identifier.

For example, consider the following `addE` traversal.

```
g.addE("knows").from(V("v1")).to(V("v2")).property(id, "e1")
```

The traversal results in the following statement being added to the graph.

```
StatementEvent[Added(<v1> <knows> <v2> <e1>) .]
```

## Gremlin Property Statements

A Gremlin property statement in Neptune asserts an individual property value for a
vertex or edge. The subject is a user-supplied vertex or edge identifier. The predicate is
the property name (key), and the object is the individual property value. The graph (G) is
again the default graph identifier, the null graph, displayed as
`<~>`.

Consider the following example.

```
g.V("v1").property("name", "John")
```

This statement results in the following.

```
StatementEvent[Added(<v1> <name> "John" <~>) .]
```

Property statements differ from others in that their object is a primitive value (a
`string`, `date`, `byte`, `short`,
`int`, `long`, `float`, or `double`). Their
object is not a resource identifier that could be used as the subject of another
assertion.

For multi-properties, each individual property value in the set receives its own
statement.

```
g.V("v1").property(set, "phone", "956-424-2563").property(set, "phone", "956-354-3692 (tel:9563543692)")
```

This results in the following.

```
StatementEvent[Added(<v1> <phone> "956-424-2563" <~>) .]
StatementEvent[Added(<v1> <phone> "956-354-3692" <~>) .]
```
