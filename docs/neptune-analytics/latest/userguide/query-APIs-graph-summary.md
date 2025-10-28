# GraphSummary

You can use the GetGraphSummary API to quickly gain a high-level understanding of your graph data, size and content.
In a graph application, this API can be used to improve the search results by providing discovered node or edge labels as
part of the search.

The GetGraphSummary API retrieves a read-only list of node and edge labels and property keys, along with counts of nodes,
edges, and properties. The API also accepts an optional parameter named mode, which can take one of two values, namely basic
(the default) and detailed. The detailed graph summary response contains two additional fields, nodeStructures and
edgeStructures.

## GetGraphSummary inputs

GetGraphSummary accepts two inputs:

- graph-identifier (required) - The unique identifier of the graph.
- mode (optional) - Can be `basic` or `detailed`.

## GetGraphSummary outputs

The response contains the following fields:

- `version` - The version of this graph summary response.
- `lastStatisticsComputationTime` - The timestamp, in ISO 8601 format, of the time at which
  Neptune Analytics last computed statistics.
- `graphSummary`
  - `numNodes` - The number of nodes in the graph.
  - `numEdges` - The number of edges in the graph.
  - `numNodeLabels` - The number of distinct node labels in the graph.
  - `numEdgeLabels` - The number of disctinct edge labels in the graph.
  - `nodeLabels` - List of distinct node labels in the graph.
  - `edgeLabels` - List of distinct edge labels in the graph.
  - `numNodeProperties` - The number of distinct node properties in the graph.
  - `numEdgeProperites` - The number of distinct edge properties in the graph.
  - `nodeProperties` - List of distinct node properties in the graph along with the count
    of nodes where each property is used.
  - `edgeProperties` - List of distinct edge properties in the graph along with the count
    of edges where each property is used.
  - `totalNodePropertyValues` - Total number of usages of all node properties.
  - `totalEdgePropertyValues` - Total number of usages of all edge properties.
  - `nodeStructures` (only present for mode=detailed) - Contains a list of node
    structures, each containing the following fields:
    - `count` - Number of nodes that have this specific structure.
    - `nodeProperties` - List of node properties present in this specific structure.
    - `distinctOutgoingEdgeLabels` - List of distinct outgoing edge labels present in
      this specific structure.

  - `edgeStructures` (only present for mode=detailed) - Contains a list of edge structures
    each containing the following fields:
    - `count` - Number of edges that have this specific structure.
    - `edgeProperties` - List of edge properties present in this specific structure.

## GetGraphSummary examples

AWS CLI

```
# Sample query
aws neptune-graph get-graph-summary \
--graph-identifier <graph-id> \
--region <region>
--mode detailed

# parmeters supported
mode [Optional] : basic | detailed
```

AWSCURL

```
# Sample query
awscurl "https://<graph-id>.<endpoint>/summary" \
--region <region> \
--service neptune-graph
```

Sample output payload:

```
# this is the graph summary with "mode=detailed"
{
    "version": "v1",
    "lastStatisticsComputationTime": "2024-01-25T19:50:42+00:00",
    "graphSummary": {
        "numNodes": 3749,
        "numEdges": 57645,
        "numNodeLabels": 4,
        "numEdgeLabels": 2,
        "nodeLabels": [
            "continent",
            "country",
            "version",
            "airport"
        ],
        "edgeLabels": [
            "contains",
            "route"
        ],
        "numNodeProperties": 14,
        "numEdgeProperties": 1,
        "nodeProperties": [
            {
                "code": 3749
            },
            {
                "desc": 3749
            },
            {
                "type": 3749
            },
            {
                "city": 3504
            },
            {
                "country": 3504
            },
            {
                "elev": 3504
            },
            {
                "icao": 3504
            },
            {
                "lat": 3504
            },
            {
                "lon": 3504
            },
            {
                "longest": 3504
            },
            {
                "region": 3504
            },
            {
                "runways": 3504
            },
            {
                "author": 1
            },
            {
                "date": 1
            }
        ],
        "edgeProperties": [
            {
                "dist": 50637
            }
        ],
        "totalNodePropertyValues": 42785,
        "totalEdgePropertyValues": 50637,
        "nodeStructures": [          // will not be present with mode=basic
            {
                "count": 3475,
                "nodeProperties": [
                    "city",
                    "code",
                    "country",
                    "desc",
                    "elev",
                    "icao",
                    "lat",
                    "lon",
                    "longest",
                    "region",
                    "runways",
                    "type"
                ],
                "distinctOutgoingEdgeLabels": [
                    "route"
                ]
            },
            {
                "count": 238,
                "nodeProperties": [
                    "code",
                    "desc",
                    "type"
                ],
                "distinctOutgoingEdgeLabels": [
                    "contains"
                ]
            },
            {
                "count": 29,
                "nodeProperties": [
                    "city",
                    "code",
                    "country",
                    "desc",
                    "elev",
                    "icao",
                    "lat",
                    "lon",
                    "longest",
                    "region",
                    "runways",
                    "type"
                ],
                "distinctOutgoingEdgeLabels": []
            },
            {
                "count": 6,
                "nodeProperties": [
                    "code",
                    "desc",
                    "type"
                ],
                "distinctOutgoingEdgeLabels": []
            },
            {
                "count": 1,
                "nodeProperties": [
                    "author",
                    "code",
                    "date",
                    "desc",
                    "type"
                ],
                "distinctOutgoingEdgeLabels": []
            }
        ],
        "edgeStructures": [          //will not be present with mode=basic
            {
                "count": 50637,
                "edgeProperties": [
                    "dist"
                ]
            }
        ]
    }
}
```
