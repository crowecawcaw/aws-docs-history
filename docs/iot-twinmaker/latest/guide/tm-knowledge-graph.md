# AWS IoT TwinMaker knowledge graph

The AWS IoT TwinMaker knowledge graph organizes all the information contained within your AWS IoT TwinMaker workspaces
and presents it in a visual graph format. You can run queries against your entities, components, and
component types to generate visual graphs that show you the relationships between your AWS IoT TwinMaker
resources.

The following topics show you how to use and integrate the knowledge graph.

###### Topics

- [AWS IoT TwinMaker knowledge graph core concepts](#tm-knowledge-graph-concepts "#tm-knowledge-graph-concepts")
- [How to Run AWS IoT TwinMaker knowledge graph queries](tm-knowledge-graph-use.md "tm-knowledge-graph-use.md")
- [Knowledge graph scene integration](tm-knowledge-graph-scene.md "tm-knowledge-graph-scene.md")
- [How to use AWS IoT TwinMaker knowledge graph with Grafana](tm-knowledge-Grafana-panel.md "tm-knowledge-Grafana-panel.md")
- [AWS IoT TwinMaker knowledge graph additional
  resources](tm-knowledge-graph-resources.md "tm-knowledge-graph-resources.md")

## AWS IoT TwinMaker knowledge graph core concepts

This topic covers the key concepts and vocabulary of the knowledge graph feature.

**How knowledge graph works**:

Knowledge graph creates relationships between entities and their components with
the existing [CreateEntity](../apireference/API_CreateEntity.md "../apireference/API_CreateEntity.md") or
[UpdateEntity](../apireference/API_UpdateEntity.md "../apireference/API_UpdateEntity.md") APIs. A relationship is just a property of a special data type
[RELATIONSHIP](../apireference/API_DataType.md#:~:text=Valid%20Values%3A-,RELATIONSHIP,-%7C%20STRING%20%7C%20LONG%20%7C%20BOOLEAN "../apireference/API_DataType.md#:~:text=Valid%20Values%3A-,RELATIONSHIP,-%7C%20STRING%20%7C%20LONG%20%7C%20BOOLEAN") that is defined on a component of an entity. AWS IoT TwinMaker knowledge
graph calls the [ExecuteQuery](../apireference/API_ExecuteQuery.md "../apireference/API_ExecuteQuery.md") API
to make a query based on any data in the entities or the relationships between them.
Knowledge graph uses the flexible PartiQL query language (used by many AWS services)
that has newly added graph match syntax support to help you write your queries. After
the calls are made, you can view the results as a table or visualize them as a graph
of connected nodes and edges.

**Knowledge graph key terms**:

- **Entity graph**: A collection of nodes and edges
  within a workspace.
- **Node**: Every entity in your workspace becomes
  a node in the entity graph.
- **Edge**: Every relationship property defined on
  a component of an entity becomes an edge in the entity graph. In addition, a
  hierarchical parent-child relationship defined using the parentEntityId field
  of an entity also becomes an edge in the entity graph with an "isChildOf"
  relationship name. All edges are directional edges.
- **Relationship**: An AWS IoT TwinMaker Relationship is a
  special type of property of an Entity’s component. You can use the AWS IoT TwinMaker
  [CreateEntity](../apireference/API_CreateEntity.md "../apireference/API_CreateEntity.md") or [UpdateEntity](../apireference/API_UpdateEntity.md "../apireference/API_UpdateEntity.md")
  API to define and edit a relationship. In AWS IoT TwinMaker, a relationship must be
  defined in a component of an entity. A relationship cannot be defined as an
  isolated resource. A relationship must be directional from one entity to
  another.
