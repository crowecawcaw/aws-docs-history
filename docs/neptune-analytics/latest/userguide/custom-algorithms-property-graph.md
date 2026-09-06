

# Property graph information
<a name="custom-algorithms-property-graph"></a>

 Property Graph Information (graph.pg\_info) summarizes some of the basic metrics of the graph, such as the number of vertices, the number of edges, the number of edge properties, the number of vertex properties, the number of edge labels, and the number of vertex labels. 

## Inputs for graph.pg\_info
<a name="custom-algorithms-property-graph-input"></a>

There are no inputs for graph.pg\_info.

## Outputs for graph.pg\_info
<a name="custom-algorithms-property-graph-output"></a>

There are two columns in the output relation: the first column is the metric name and the second column is the count.

**metric: the metrics that graph.pg\_info will return, which include:**
+ numVertices: the number of vertices in the graph.
+ numEdges: the number of edges in the graph.
+ numVertexProperties: the number of node properties in the graph.
+ numEdgeProperties: the number of edge properties in the graph.
+ numVertexLabels: the number of unique vertex labels in the graph.
+ numEdgeLabels: the number of unique edge labels in the graph.

**count**
+ count: the value of the above metrics.

## graph.pg\_info query example
<a name="custom-algorithms-property-graph-query-example"></a>

```
## Syntax
CALL neptune.graph.pg_info() 
YIELD metric, count
RETURN metric, count
```

## graph.pg\_info query integration
<a name="custom-algorithms-property-graph-query-integration"></a>

```
# sample query integration 
CALL neptune.graph.pg_info()
YIELD metric, count
WHERE metric = 'numVertices'
RETURN count
```

## Sample graph.pg\_info output
<a name="custom-algorithms-property-graph-output-example"></a>

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