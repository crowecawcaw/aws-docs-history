# Neptune Analytics openCypher data model

For details on the openCypher data model, please refer to the Neptune Database
[documentation](../../../neptune/latest/userguide/access-graph-opencypher-data-model.md "../../../neptune/latest/userguide/access-graph-opencypher-data-model.md").
There are some differences in modeling of vertices without labels. Neptune Database adds vertices with a default label if one is
not explicitly provided. All but the last label of a vertex can be deleted.

### What is a vertex?

As well as loading both vertices and edges, unlike Neptune Database, Neptune Analytics also allows loading just edges and is still
able to run algorithms and queries from that starting point. This is useful if your main interest is, for example,
loading a file of edge data from a CSV file and running an algorithm over the data without needing to provide
any additional vertex information. This has some implications on how vertices are managed. For the
Neptune Analytics query engine, a vertex implicitly exists if it either has an explicit label, a property, or an edge.
Likewise, a vertex gets implicitly deleted if all its labels, properties, and edges get removed.
Unlike Neptune Database, Neptune Analytics stores a label for a vertex only if one is explicitly provided by the user, and all
labels of a vertex can be deleted.

This affects some common openCypher queries. An attempt to create a vertex that has neither a label
nor properties or edges has no effect. That is, queries such as `CREATE (n)` or
`CREATE (n {`~id`: "xyz"})` do not add any vertices to the graph. `CREATE (n {key:value})`,
where `key` is different from `~id`, creates a vertex with the property `key`,
and `CREATE (n)-[knows]->(m)` creates two vertices with the one shared edge.

`CREATE (n {key:value})`, where key is different from `~id`, creates a vertex with
the property `key`, and a subsequent `MATCH (n)` will discover that vertex. A
query such as `MATCH (n {key:value}) REMOVE n.key` will remove the only property for the
(edge- and label-less) vertex, which implicitly deletes the vertex. A subsequent `MATCH (n)`
query will not return that vertex. Likewise, `CREATE (n:Label)` adds a vertex with the label
`Label` (and no other properties or edges). Now, `MATCH (n) REMOVE n:Label` deletes the
only label of the vertex, which implicitly deletes the vertex.

Similarly, `CREATE (n)-[knows]->(m)` creates two nodes and one edge. `MATCH (n)` will
discover those two vertices. Now, `MATCH (n)-[r:knows]->(m) DELETE r` will delete that edge,
and implicitly deletes the two vertices. Those two vertices are no longer returned when running a
`MATCH (n)` query.

Merge on empty vertices, `MERGE (n)` or `MERGE (n {`~id`: "xyz"})`, are not permitted
and will throw an exception. `MERGE (n {key:value})` creates a vertex with property `key`
if a matching vertex does not exist.

The following table illustrates the differences between Neptune Database and Neptune Analytics.

| Query (run on empty graph)                                                                | Neptune Database                                                                                                                                                              | Neptune Analytics                                                                                                                                                                |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE (n)`                                                                              | Adds a vertex with label "vertex" to the graph.<br>Each repeat request adds a new vertex to the graph.                                                                        | No change to the graph, query returns without exception.<br>Repeat requests similarly do not change the graph, and query returns without exception.                              |
| `CREATE (n {`~id`: "xyz"})`                                                               | Adds a vertex with id "xyz" and label "vertex" to the graph.<br>Repeat request fails with exception.                                                                          | No change to the graph, query returns without exception.<br>Repeat requests similarly do not change the graph, and query returns without exception.                              |
| `CREATE (n {key:value})`                                                                  | Adds a vertex with label "vertex" and property "key" to the graph.                                                                                                            | Adds a vertex with property "key" to the graph. This vertex has no label.                                                                                                        |
| `CREATE (n {key:value})`<br>`MATCH (n {key:value}) REMOVE n.key`                          | The REMOVE query removes the "key" property on the vertex.<br>The graph contains a vertex with label "vertex" but no property.<br>`MATCH (n)` returns the vertex.             | The remove query removes the property on the vertex, and as a<br>side effect the vertex gets deleted from the graph.<br>`MATCH (n)` does not return the vertex.                  |
| `CREATE (n:Label {`~id`: "xyz", key:value})`<br>`MATCH (n {`~id`: "xyz"}) REMOVE n:Label` | The REMOVE query errors out, the last label on a vertex cannot be deleted.                                                                                                    | The REMOVE query removes the label. The graph contains a graph with id "xyz" and property "key".                                                                                 |
| `CREATE (n)-[:knows]->(m)`                                                                | Adds two vertices with label "vertex" and an edge with label "knows" to the graph.<br>`MATCH (n)` returns both those vertices.                                                | Adds an edge between two new vertices to the graph.<br>`MATCH (n)` returns both those vertices.                                                                                  |
| `CREATE (n)-[:knows]->(m)`<br>`MATCH (n)-[r:knows]->(n) DELETE r`                         | Deletes the edge. The graph contains two isolated vertices.<br>`MATCH (n)` returns both those vertices.                                                                       | Deletes the edge, and as a side effect the two vertices also get deleted from the graph.<br>The graph is now empty.<br>`MATCH (n)` does not return the two vertices.             |
| `MERGE (n)`                                                                               | Adds a vertex with label "vertex" if graph is empty.<br>Matches all vertices in a non-empty graph.                                                                            | Throws an exception.                                                                                                                                                             |
| `MERGE (n {`~id`: "xyz"})`                                                                | Adds a vertex with label "vertex" and id "xyz" if one does not exist in the graph.<br>Matches vertex with id "xyz".                                                           | Throws an exception.                                                                                                                                                             |
| `MERGE (n {key:value})`                                                                   | Adds a vertex with label "vertex" and property "key" to the graph, if such a vertex does not<br>already exists.                                                               | Adds a vertex with property "key" to the graph, if such a vertex does not already exist. This<br>vertex has no label.                                                            |
| `MERGE (n)-[knows]->(m)`                                                                  | Adds two vertices with label "vertex" and an edge with label "knows" to the graph,<br>if an edge with label knows does not exist.<br>`MATCH (n)` returns both those vertices. | Adds an edge between two new vertices to the graph, if an edge with label "knows" does<br>not exist. The two vertices have no label.<br>`MATCH (n)` returns both those vertices. |

###### Note

A workaround to implicit deletion of a vertex when all of its labels, properties, and edges get removed is
to assign immutable labels to all vertices. This way, the deletion of all properties, edges, or mutable labels
of a vertex will not lead to an implicit deletion. A vertex would not get deleted until explicitly deleted.

Likewise a workaround to no-op vertex create queries is to always create a vertex with a label or a property.
To combine it with the previous point, always create a vertex with an immutable label. Extending this to bulk
or batch loads, include all vertices in some vertex files and assign a property or an immutable label to all
vertices.
