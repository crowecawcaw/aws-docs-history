# Node graph panel (Beta)

This documentation topic is designed
for Grafana workspaces that support **Grafana version
8.x**.

For Grafana workspaces that support Grafana version 10.x, see
[Working in Grafana version 10](using-grafana-v10.md "using-grafana-v10.md").

For Grafana workspaces that support Grafana version 9.x, see
[Working in Grafana version 9](using-grafana-v9.md "using-grafana-v9.md").

The node graph panel visualizes directed graphs or networks. It uses directed force
layout to effectively position the nodes so it can help with displaying complex
infrastructure maps, hierarchies, or execution diagrams.

## Data requirements

The node graph panel requires a specific shape of the data to be able to display
its nodes and edges. Not every data source or query can be visualized in this
panel.

The Node graph visualization consists of _nodes_ and
_edges_.

- A _node_ is displayed as a circle. A node might
  represent an application, a service, or anything else that is relevant from
  an application perspective.
- An _edge_ is displayed as a line that connects two
  nodes. The connection might be a request, an execution, or some other
  relationship between the two nodes.

## Nodes

Usually, nodes show two statistical values inside the node and two identifiers
just below the node, usually name and type. Nodes can also show another set of
values as a color circle around the node, with sections of different color
represents different values that should add up to 1. For example, you can have the
percentage of errors represented by red portion of the circle.

Additional details can be displayed in a context menu, which is displayed when
you choose the node. There also can be additional links in the context menu that can
target either other parts of the Grafana workspace or any external link.

## Edges

Edges can also show statistics when you hover over the edge. Similar to nodes,
you can open a context menu with additional details and links by choosing the
edge.

The first data source supporting this visualization is the AWS X-Ray data source
for its service map feature. For more information, see [Connect to an AWS X-Ray data source](x-ray-data-source.md "x-ray-data-source.md").

Additional details can be displayed in a context menu ,which is displayed when
you choose the node. There also can be additional links in the context menu that can
target either other parts of the Grafana workspace or any external link.

## Navigating the node graph

You can pan within the node graph by choosing outside of any node or edge and
dragging the mouse.

You can zoom by using the buttons on the upper left corner of the node
graph.
