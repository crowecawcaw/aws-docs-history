# Node graph

This documentation topic is designed
for Grafana workspaces that support **Grafana version
10.x**.

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

For Grafana workspaces that support Grafana version 8.x, see
[Working in Grafana version 8](using-grafana-v8.md "using-grafana-v8.md").

Node graphs can visualize directed graphs or networks. They use a directed force
layout to effectively position the nodes, so they can help with displaying complex
infrastructure maps, hierarchies, or run diagrams.

## Data requirements

A node graph requires a specific shape of the data to be able to display its
nodes and edges. Not every data source or query can be visualized with this
graph. If you want to use this as a data source developer, see the section about
data API.

A node graph consists of _nodes_ and _edges_.

- A _node_ is displayed as a circle. A node might
  represent an application, a service, or anything else that is relevant from
  an application perspective.
- An _edge_ is displayed as a line that connects two
  nodes. The connection might be a request, an operation, or some other
  relationship between the two nodes.

Both nodes and edges can have associated metadata or statistics. The data source
defines what information and values is shown, so different data sources can show
different type of values or not show some values.

## Nodes

Usually, nodes show two statistical values inside the node and two identifiers
just below the node, usually name and type. Nodes can also show another set of
values as a color circle around the node, with sections of different color
representing different values that should add up to 1. For example, you can have
the percentage of errors represented by red portion of the circle.

Additional details can be displayed in a context menu, which is displayed when
you choose the node. There also can be additional links in the context menu that can
target either other parts of the Grafana workspace or any external link.

###### Note

Node graph can show only 1,500 nodes. If this limit is crossed, a warning is
visible in the upper right corner, and some nodes will be hidden. You can expand
hidden parts of the graph by clicking on the **Hidden nodes**
markers in the graph.

## Edges

Edges can also show statistics when you hover over the edge. Similar to nodes,
you can open a context menu with additional details and links by choosing the
edge.

The first data source supporting this visualization is the AWS X-Ray data source
for its service map feature. For more information, see [Connect to an AWS X-Ray data source](x-ray-data-source.md "x-ray-data-source.md").

## Navigating the node graph

**Pan**

You can pan within the node graph by choosing outside of any node or edge and
dragging the pointer.

**Zoom in or out**

You can zoom by using the buttons on the upper left corner of the node
graph, or use a mouse wheel or other scroll input with the `Ctrl`
(or `Cmd`) key.

**Explore hidden nodes**

The number of nodes shown at a given time is limited to maintain a reasonable
performance. Nodes that are outside this limit are hidden behind selectable markers
that show an approximate number of hidden nodes that are connected to that edge. You
can choose the marker to expand the graph around that node.

**Grid view**

You can switch to the grid view to have a better overview of the most interesting
nodes in the graph. Grid view shows nodes in a grid without edges and can be sorted
by stats shown inside the node or by stats represented by the a colored border of
the nodes.

To sort the nodes, choose the stats inside the legend. The marker next to the stat
name (either `˄` or `˅`) shows which stat is currently used
for sorting and sorting direction.

Choose a node and then select the **Show in Graph layout**
option to switch back to graph layout with focus on the selected node, to show it
in context of the full graph.

## Data API

This visualization needs a specific shape of the data to be returned from the
data source in order to correctly display it.

Node Graph at minimum requires a data frame describing the edges of the graph.
By default, node graph will compute the nodes and any stats based on this data
frame. Optionally a second data frame describing the nodes can be sent in case
there is need to show more node specific metadata. You have to set
`frame.meta.preferredVisualisationType = 'nodeGraph'` on both data
frames or name them `nodes` and `edges` respectively for
the node graph to render.

**Edges data from structure**

Required fields:

| Field name    | Type          | Description                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| id            | string        | Unique identifier of the edge.                                                                                                                                                                                                                                                                                                                                         |
| source        | string        | Id of the source node.                                                                                                                                                                                                                                                                                                                                                 |
| target        | string        | Id of the target.                                                                                                                                                                                                                                                                                                                                                      | Optional fields:                               |
| Field name    | Type          | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---           | ---           | ---                                                                                                                                                                                                                                                                                                                                                                    |
| mainstat      | string/number | First stat shown in the overlay when hovering over the edge. It can be a string showing the value as is or it can be a number. If it is a number, any unit associated with that field is also shown.                                                                                                                                                                   |
| secondarystat | string/number | Same as mainStat, but shown right under it.                                                                                                                                                                                                                                                                                                                            |
| detail\_\_\*  | string/number | Any field prefixed with `detail__` will be shown in the header of context menu when clicked on the edge. Use `config.displayName` for a more human readable label.                                                                                                                                                                                                     | **Nodes data from structure** Required fields: |
| Field name    | Type          | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---           | ---           | ---                                                                                                                                                                                                                                                                                                                                                                    |
| id            | string        | Unique identifier of the node. This ID is referenced by edge in its source and target field.                                                                                                                                                                                                                                                                           | Optional fields:                               |
| Field name    | Type          | Description                                                                                                                                                                                                                                                                                                                                                            |
| ---           | ---           | ---                                                                                                                                                                                                                                                                                                                                                                    |
| title         | string        | Name of the node visible just under the node.                                                                                                                                                                                                                                                                                                                          |
| subtitle      | string        | Additional, name, type or other identifier shown under the title.                                                                                                                                                                                                                                                                                                      |
| mainstat      | string/number | First stat shown inside the node itself. It can either be a string showing the value as is or a number. If it is a number, any unit associated with that field is also shown.                                                                                                                                                                                          |
| secondarystat | string/number | Same as mainStat, but shown under it inside the node.                                                                                                                                                                                                                                                                                                                  |
| arc\_\_\*     | number        | Any field prefixed with `arc__` will be used to create the color circle around the node. All values in these fields should add up to 1. You can specify color using `config.color.fixedColor`.                                                                                                                                                                         |
| detail\_\_\*  | string/number | Any field prefixed with `detail__` will be shown in the header of context menu when clicked on the node. Use `config.displayName` for more human readable label.                                                                                                                                                                                                       |
| color         | string/number | Can be used to specify a single color instead of using the `arc__` fields to specify color sections. It can either be a string (it must be an acceptable HTML color string), or it can be a number, in which case the behavior depends on the `field.config.color.mode` setting. This can be used, for example, to create gradient colors controlled by a field value. |
| icon          | string        | Name of the icon to show inside the node instead of the default stats. Only Grafana built in icons are allowed (see the available icons [here](https://developers.grafana.com/ui/latest/index.html?path=/story/docs-overview-icon--icons-overview "https://developers.grafana.com/ui/latest/index.html?path=/story/docs-overview-icon--icons-overview")).              |
| nodeRadius    | number        | Radius value in pixels. Used to manage node size.                                                                                                                                                                                                                                                                                                                      |
| highlighted   | Boolean       | Sets whether the node should be highlighted. Use, for example, to represent a specific path in the graph by highlighting several nodes and edges. Defaults to `false`.                                                                                                                                                                                                 |
