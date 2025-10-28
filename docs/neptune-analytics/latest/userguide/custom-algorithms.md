# Misc. graph procedures

The miscellaneous graph procedures can be ran on your graphs to give you insight into your graphs and their metrics.

Property Graph Information (`graph.pg_info`) summarizes some of the basic metrics of the graph, such as the number of
vertices, the number of edges, the number of edge properties, the number of vertex properties, the number of edge labels,
and the number of vertex labels.

The `neptune.graph.pg_schema()` procedure provides a comprehensive overview of the graph structure. It
extracts and summarizes the current schema of a Neptune Analytics graph, i.e., customers can observe the property names and types that appear on
vertices and edges of particular labels within the graph. The procedure is designed for use cases such as: schema visualization,
integration with third-party applications, and inclusion in open-source tools.

###### Topics

- [Property graph information](custom-algorithms-property-graph.md "custom-algorithms-property-graph.md")
- [Property graph schema](custom-algorithms-property-graph-schema.md "custom-algorithms-property-graph-schema.md")
