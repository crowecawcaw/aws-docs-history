# Property graph schema

The `neptune.graph.pg_schema()` procedure provides a comprehensive overview of the graph structure. It
extracts and summarizes the current schema of a Neptune Analytics graph, i.e., customers can observe the property names and types that appear on
vertices and edges of particular labels within the graph. The procedure is designed for use cases such as: schema visualization,
integration with third-party applications, and inclusion in open-source tools.

###### Benefits:

- Node and edge label enumeration: The procedure identifies and lists all unique labels for nodes and edges present in the graph
  (`nodeLabels` and `edgeLabels`, respectively).
- Property and data type analysis: For each node and edge label, it catalogs associated properties and their corresponding data
  types (`nodeLabelDetails` and `edgeLabelDetails`, respectively). This information is crucial for understanding
  the attributes of different graph elements.
- Topological relationship mapping: The procedure generates a set of triples in the format
  (`nodeLabel)-[edgeLabel]->(nodeLabel`), effectively summarizing the graph's topology and the relationships
  between different node types (`labelTriples`).
- Consistency across tools: By providing a standardized schema representation, the procedure ensures consistency across various
  third-party and open-source tools that interact with the graph database.
- Integration-friendly output: The schema information is formatted in a way that facilitates easy integration with AI tools,
  visualization software, and reporting systems.

This procedure provides a unified method of complete and up-to-date information extraction to support a wide range of applications
from AI-driven query generation to data visualization and reporting.

## Inputs for neptune.graph.pg_schema()

There are no inputs for neptune.graph.pg_schema().

## Outputs for neptune.graph.pg_schema()

There is a single column in the output containing a map schema containing the following key components in the schema map:

- `nodeLabels`: A list of all unique labels assigned to nodes/vertices in the graph.
- `edgeLabels`: A list of all unique labels assigned to relationships/edges in the graph.
- `nodeLabelDetails`: For each node label, all properties associated with that node containing an enumeration
  of each property and the various data types it can manifest as across different nodes with the same label.
  - `label` - The node label or labels.
  - `properties` - An array of the superset of properties for the node:
    - `<key:> name` - The property name.
    - `<value:> A key-value dictionary (map)` - Stores data types that are available for the property.
      - `<key:> "datatypes"` ,
      - `<value:> array[string]`

    - e.g.,

    ```
    "contains": {
      "properties": {
        "weight": {
          "datatypes": ["Int"]
        }
      }
    }
    ```

- `edgeLabelDetails`: For each edge label, all properties associated with edges that have that label containing
  an enumeration of each property and the various data types it can manifest as across different edges with the same label.
  - `label` - The edge label.
  - `properties` - A key-value dictionary (map) of properties for the edge label:
    - `<key:>` name - The property name
    - `<value:>` A key-value dictionary (map) - Stores data types that are available for the property.
      - `<key:> "datatypes"` ,
      - `<value:> array[string]`

- `labelTriples`: A set of `nodeLabel-edgeLabel->nodeLabel` combinations that represent the connections between
  different types of nodes in the graph. These triples summarize the graph's topology by showing how different node types are related
  through various edge types. Each entry is a key-value dictionary, holding the following:
  - `~type` - The edge label.
  - `~from` - The node label of the head node of the node-edge->node.
  - `~to` - The node label of the tail node of the node-edge->node.

## neptune.graph.pg_schema() query example

```
## Syntax
CALL neptune.graph.pg_schema()
YIELD schema
RETURN schema
```

## neptune.graph.pg_schema() query integration

```
# sample query integration.
# Calls pg_schema,
# Then acquires node labels,
# Then sorts them alphabetically,
# Then counts number of vertices with each label and returns it

CALL neptune.graph.pg_schema()
YIELD schema
WITH schema.nodeLabels as nl
UNWIND collSort(nl) as label
MATCH (n)
WHERE label in labels(n)
RETURN label, COUNT(n) as count

# output

{
  "results": [{
      "label": "airport",
      "count": 27
    }, {
      "label": "country",
      "count": 3
    }, {
      "label": "version",
      "count": 3
    }]
}%
```

## Sample neptune.graph.pg_schema() output

```
% aws neptune-graph execute-query \
    --graph-identifier ${graphIdentifier} \
    --query-string 'CALL neptune.graph.pg_schema()
                    YIELD schema
                    RETURN schema' \
    --language open_cypher \
    /tmp/out.txt
{
  "results": [{
      "schema": {
        "edgeLabelDetails": {
          "route": {
            "properties": {
              "weight": {
                "datatypes": ["Int"]
              },
              "dist": {
                "datatypes": ["Int"]
              }
            }
          },
          "contains": {
            "properties": {
              "weight": {
                "datatypes": ["Int"]
              }
            }
          }
        },
        "edgeLabels": ["route", "contains"],
        "nodeLabels": ["version", "airport", "continent", "country"],
        "labelTriples": [{
            "~type": "route",
            "~from": "airport",
            "~to": "airport"
          }, {
            "~type": "contains",
            "~from": "country",
            "~to": "airport"
          }, {
            "~type": "contains",
            "~from": "continent",
            "~to": "airport"
          }],
        "nodeLabelDetails": {
          "continent": {
            "properties": {
              "type": {
                "datatypes": ["String"]
              },
              "code": {
                "datatypes": ["String"]
              },
              "desc": {
                "datatypes": ["String"]
              }
            }
          },
          "airport": {
            "properties": {
              "type": {
                "datatypes": ["String"]
              },
              "city": {
                "datatypes": ["String"]
              },
              "icao": {
                "datatypes": ["String"]
              },
              "code": {
                "datatypes": ["String"]
              },
              "country": {
                "datatypes": ["String"]
              },
              "lat": {
                "datatypes": ["Double"]
              },
              "longest": {
                "datatypes": ["Int"]
              },
              "runways": {
                "datatypes": ["Int"]
              },
              "desc": {
                "datatypes": ["String"]
              },
              "lon": {
                "datatypes": ["Double"]
              },
              "region": {
                "datatypes": ["String"]
              },
              "elev": {
                "datatypes": ["Int"]
              }
            }
          },
          "country": {
            "properties": {
              "type": {
                "datatypes": ["String"]
              },
              "code": {
                "datatypes": ["String"]
              },
              "desc": {
                "datatypes": ["String"]
              }
            }
          },
          "version": {
            "properties": {
              "date": {
                "datatypes": ["String"]
              },
              "desc": {
                "datatypes": ["String"]
              },
              "author": {
                "datatypes": ["String"]
              },
              "type": {
                "datatypes": ["String"]
              },
              "code": {
                "datatypes": ["String"]
              }
            }
          }
        }
      }
    }]
}
```
