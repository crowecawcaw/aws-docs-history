# Getting started using openCypher

You can query property-graph data in Neptune using openCypher regardless of how it
was loaded, but you can't use openCypher to query data loaded as RDF.

The [Neptune bulk loader](bulk-load.md "bulk-load.md") accepts property-graph
data in a [CSV format for Gremlin](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md"),
and in a [CSV format for openCypher](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md").
Also, of course, you can add property data to your graph using Gremlin and/or openCypher
queries.

There are many online tutorials available for learning the Cypher
query language. Here, a few quick examples of openCypher queries may help you get an
idea of the language, but by far the best and easiest way to get started using
openCypher to query your Neptune graph is by using the openCypher notebooks in the
[Neptune workbench](graph-notebooks.md "graph-notebooks.md"). The
workbench is open-source, and is hosted on GitHub at [https://github.com/aws-samples/amazon-neptune-samples](https://github.com/aws-samples/amazon-neptune-samples/ "https://github.com/aws-samples/amazon-neptune-samples/").

You'll find the openCypher notebooks in the GitHub [Neptune
graph-notebook repository](https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks "https://github.com/aws/graph-notebook/tree/main/src/graph_notebook/notebooks"). In particular, check out the [Air-routes
visualization](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/02-Visualization/Air-Routes-openCypher.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/02-Visualization/Air-Routes-openCypher.ipynb"), and [English
Premier Teams](https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/02-Visualization/EPL-openCypher.ipynb "https://github.com/aws/graph-notebook/blob/main/src/graph_notebook/notebooks/02-Visualization/EPL-openCypher.ipynb") notebooks for openCypher.

Data processed by openCypher takes the form of an unordered series of key/value maps.
The main way to refine, manipulate, and augment these maps is to use clauses that perform
tasks such as pattern matching, insertion, update, and deletion on the key/value pairs.

There are several clauses in openCypher for finding data patterns in the graph, of
which `MATCH` is the most common. `MATCH` lets you specify the
pattern of nodes, relationships, and filters that you want to look for in your graph.
For example:

- **Get all nodes**

```
MATCH (n) RETURN n
```

- **Find connected nodes**

```
MATCH (n)-[r]->(d) RETURN n, r, d
```

- **Find a path**

```
MATCH p=(n)-[r]->(d) RETURN p
```

- **Get all nodes with a label**

```
MATCH (n:airport) RETURN n
```

Note that the first query above returns every single node in your graph, and
the next two return every node that has a relationship— this is not
generally recommended! In almost all cases, you want to narrow down the data
being returned, which you can do by specifying node or relationship labels
and properties, as in the fourth example.

You can find a handy cheat-sheet for openCypher syntax in the Neptune
[github
sample repository](https://github.com/aws-samples/amazon-neptune-samples/tree/master/opencypher/Cheatsheet.md "https://github.com/aws-samples/amazon-neptune-samples/tree/master/opencypher/Cheatsheet.md").
