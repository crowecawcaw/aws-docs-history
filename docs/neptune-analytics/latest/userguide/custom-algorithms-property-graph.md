# Property graph information

Property Graph Information (graph.pg_info) summarizes some of the basic metrics of the graph, such as the number of
vertices, the number of edges, the number of edge properties, the number of vertex properties, the number of edge labels,
and the number of vertex labels.

## Inputs for graph.pg_info

There are no inputs for graph.pg_info.

## Outputs for graph.pg_info

There are two columns in the output relation: the first column is the metric name and the second column is the
count.

###### metric: the metrics that graph.pg_info will return, which include:

- numVertices: the number of vertices in the graph.
- numEdges: the number of edges in the graph.
- numVertexProperties: the number of node properties in the graph.
- numEdgeProperties: the number of edge properties in the graph.
- numVertexLabels: the number of unique vertex labels in the graph.
- numEdgeLabels: the number of unique edge labels in the graph.

###### count

- count: the value of the above metrics.

## graph.pg_info query example

```
## Syntax
CALL neptune.graph.pg_info()
YIELD metric, count
RETURN metric, count
```

## graph.pg_info query integration

```
# sample query integration
CALL neptune.graph.pg_info()
YIELD metric, count
WHERE metric = 'numVertices'
RETURN count
```

## Sample graph.pg_info output

```
# sample output of graph.pg_info
aws neptune-graph execute-query \
     --graph-identifier ${graphIdentifier} \
     --query-string "CALL neptune.graph.pg_info()
     YIELD metric, count
     RETURN metric, count " \
     --language open_cypher \
     /tmp/out.txt
cat /tmp/out.txt
{
  "results": [{
      "metric": "numVertices",
      "count": 3748
    }, {
      "metric": "numEdges",
      "count": 57538
    }, {
      "metric": "numVertexProperties",
      "count": 42773
    }, {
      "metric": "numEdgeProperties",
      "count": 50532
    }, {
      "metric": "numVertexLabels",
      "count": 4
    }, {
      "metric": "numEdgeLabels",
      "count": 2
    }]
}
```
